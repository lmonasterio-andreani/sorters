# 02. Flujo End-to-End: Vertical Sorter (CIT 1° Piso)

## 1. Visión General del Circuito
El **Vertical Sorter** ubicado en el primer piso de la Central Inteligente de Transferencia (CIT) es el modelo de referencia para la integración y observabilidad de clasificadores en Andreani. 

Este clasificador de bandejas verticales/cross-belt clasifica paquetería estándar y de e-commerce a alta cadencia. El flujo completo abarca desde la solicitud de envío digital por parte de un cliente hasta el momento en que el paquete es expulsado físicamente por una rampa y su estado es consolidado en los tableros operativos de planta.

---

## 2. Diagrama de Secuencia End-to-End

![Diagrama de Secuencia Vertical Sorter](./flujo-vertical.svg)

---

## 3. Descripción Detallada de las Fases

### Fase 1: Ingesta y Creación de la Orden en TMS
1. **Cliente / API Unificada**:
   - Una cuenta comercial, cliente B2C o plataforma de e-commerce genera un requerimiento de transporte.
   - `API Unificada` recibe la solicitud e interactúa con el broker Kafka publicando el evento `OrdenEnvioSolicitada`.
2. **Consumo por TMS**:
   - Los dos sistemas centrales de transporte de Andreani, **DMS** (Delivery Management System) e **Integra** (sistema core), consumen dicho evento.
   - Al persistir y validar la orden con éxito, emiten el evento `OrdenEnvioCreada`.
   - *Nota de arquitectura*: DMS e Integra manejan grupos de tópicos independientes. Adicionalmente, ante solicitudes de cambio de entrega por parte del cliente, se emiten eventos de `Cambios Destino` que son sincronizados vía `dotnet-NovedadesALSAtoCasaIntegra`.

---

### Fase 2: Procesamiento en SPP y Enriquecimiento
1. **Consumo del Alta**:
   - El worker **`spp-altas-suscriber`** (desplegado en cluster CCE, namespace `TYD-SPP`) escucha el tópico de alta.
   - Deriva la carga invocando la API REST interna **`spp-altas-api`**.
2. **Orquestación de Enriquecimiento**:
   - Para que el clasificador sepa exactamente por qué rampa debe bajar un bulto, no basta con el código postal provisto por el remitente.
   - `spp-altas-api` realiza llamadas síncronas a tres componentes críticos:
     - **API Normalización (NDD)**: Normaliza calles, alturas y localidades (`https://ndd-api-aa-domicilios-test.apps.ocptest.andreani.com.ar/normalizar-domicilio`).
     - **API Geo**: Convierte la dirección normalizada en coordenadas exactas de latitud y longitud.
     - **API Sucursales / Zonificación**: Calcula la **geocerca** operativa y determina la sucursal de distribución y rampa correspondiente (`apis.andreani.com/v2/sucursales?canal=B2C`).
3. **Persistencia en Base Central de Sorters**:
   - `spp-altas-api` inserta el bulto en la base de datos **`DBSORTER`** (nodo primario transaccional).

---

### Fase 3: Despacho de Eventos SPP
1. **Worker de Despacho**:
   - El servicio **`publisher-events-spp`** (.NET 6 en cluster CCE) detecta los registros insertados en `DBSORTER`.
2. **Tópicos Emitidos**:
   - `spp.alta-envio`: Notifica la disponibilidad de un nuevo bulto listo para clasificación en clasificadores automatizados.
   - `spp.asignacion-custodia`: Notifica la confirmación de custodia para sorters regionales e in-house (Giops).
   - `spp.cambio-destino`: Notifica modificaciones dinámicas de rampa o sucursal final.
   - `spp.geocerca-calculada`: Devuelve la información geocodificada hacia Integra y otros sistemas downstream.

---

### Fase 4: Ingesta en Vertical Sorter
1. **Consumo hacia Base Intermedia**:
   - El worker **`spptovertical-suscriber`** consume `spp.alta-envio`.
   - Inserta la orden en la tabla `tb_evento` de la base de datos **`Integración Vertical`** (SQL Server AlwaysOn).
   - En este punto finaliza la responsabilidad directa de la plataforma Cloud/K8s de Andreani y comienza la frontera con el software del clasificador.

---

### Fase 4B: Circuito de Resiliencia de Rampa 6 (Excepciones)
> [!IMPORTANT]
> **¿Por qué existe el `job-spptovertical` y la Rampa 6?**
> - La base de datos del Vertical Sorter gestiona una ventana de retención local (históricamente configurada entre 15 y 30 días) para evitar sobrecarga de almacenamiento.
> - Si un paquete arriba a planta y es colocado en la cinta clasificadora tras más de 30 días de emitida su orden, o si el paquete llegó a la cinta antes de que el mensaje de Kafka terminara de sincronizarse con la base local, el clasificador físico no encuentra el registro en su memoria.
> - El PLC desvía automáticamente el paquete a la **Rampa 6 (Rampa de Excepciones)**.
> - El servicio **`job-spptovertical`** corre de forma cíclica (polling), ejecuta una consulta que cruza `bulto`, `paqueteria_envio` y `trazabilidad_registro_sorter` donde `rampa = 6`, recupera los datos desde `DBSORTER` y los **reinyecta masivamente en `Integración Vertical`**.
> - Cuando el operador recoge el paquete de la rampa 6 y lo vuelve a inducir en la cinta, el Sorter ya cuenta con la información y lo desvía con éxito a su rampa destino final.

---

### Fase 5: Inducción Física y Clasificación en Planta
1. **Software del Proveedor (Optisoft / Optimus)**:
   - Reside en la PC industrial asociada al clasificador (`PC100454` - IP `10.20.48.108`).
   - Realiza polling sobre la tabla `tb_evento` de la base `Integración Vertical`, descarga los envíos pendientes, marca los registros como leídos y los carga en su memoria local.
2. **Ciclo Electromecánico**:
   - El operario induce el paquete en el alimentador del Sorter.
   - Los lectores de código de barras (escáneres cenitales / arcos) leen la etiqueta de Andreani.
   - Las celdas de carga y barreras infrarrojas efectúan el aforo dinámico (peso en gramos y volumen en cm³).
   - El PLC **Siemens Simatic S7-400** comanda los desvíos neumáticos/mecánicos depositando el bulto en la rampa asignada.
   - Optisoft registra el resultado de la clasificación física en la base `Integración Vertical`.

---

### Fase 6: Retorno de Datos, Cierre de Trazabilidad y Dashboards
1. **Publicador de Retorno (`verticaltoSpp-publisher`)**:
   - Servicio en segundo plano (.NET 6) desplegado en cluster CCE.
   - Lee los eventos de clasificación completada desde la base `Integración Vertical`.
   - Utiliza **Redis (`DBSORTERPROD`)** como caché persistente para almacenar el cursor (offset/timestamp) del último evento procesado, evitando lecturas duplicadas o sobrecarga de consultas SQL.
   - Publica el evento consolidado en Kafka (ej. `spp.bulto-procesado-vertical-sorter` o `bulto-pesado-y-medido`).
2. **Actualización de Trazabilidad**:
   - **`sortervertical-api`** y **`eventosaforo-api`** consumen el evento, registran el aforo oficial y actualizan el estado final en `DBSORTER`.
   - Los datos se replican en tiempo real al nodo secundario AlwaysOn de `DBSORTER`.
3. **Monitoreo en Planta**:
   - Los supervisores de planta visualizan el rendimiento en **`spp-dashboard-ui`**, que consulta exclusivamente la **réplica de lectura de `DBSORTER`**.

> [!CAUTION]
> **El síntoma del "Tablero en Cero":**  
> Si el servicio `verticaltoSpp-publisher` se detiene o pierde conexión con Redis/SQL, el Vertical Sorter físico seguirá operando y clasificando bultos con normalidad, pero ningún dato regresará a `DBSORTER`. En consecuencia:
> - Los tableros de control mostrarán **0 bultos clasificados por hora**.
> - Se perderá la trazabilidad en vivo de los paquetes.
> - Este desacoplamiento hace mandatorio el monitoreo activo de `verticaltoSpp-publisher` como servicio crítico P1.
