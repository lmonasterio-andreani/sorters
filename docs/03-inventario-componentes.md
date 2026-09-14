# 03. Catálogo e Inventario de Componentes

Este inventario consolida todos los componentes de software, mensajería, bases de datos y hardware relevados a partir de la toma de servicio de Sorters, la sesión de arquitectura técnica y los registros de infraestructura.

> 📁 **Documentos fuente de relevamiento:** El detalle original de componentes, repositorios, accesos y minutas de reuniones se encuentra resguardado en la carpeta [**`Relevamiento/`**](../Relevamiento/README.md) (especialmente en `Toma_de_Servicio - Sorters.xlsx` y `Observabilidad integral de los Sorters 01.docx`).

---

## 1. Microservicios, APIs y Workers

### 1.1. Core SPP y Clasificación General

| Componente | Tipo | Namespace | Ambiente / Cluster | Tecnología | Descripción y Rol Operativo |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`altas-suscriber`** (`spp-altas-suscriber`) | WORKER | `TYD-SPP` | CCE | .NET 6.0 | Consume eventos de alta (`OrdenEnvioCreada`) desde Kafka y dispara la creación en SPP invocando a `altas-api`. |
| **`altas-api`** (`spp-altas-api`) | API | `TYD-SPP` | CCE | .NET 6.0 | Orquesta el enriquecimiento de domicilio, geolocalización y zonificación, e inserta el paquete en `DBSORTER`. |
| **`publisher-event-spp`** | WORKER | `TYD-SPP` | CCE | .NET 6.0 | Lee nuevos envíos desde `DBSORTER` y los publica a los tópicos Kafka downstream (`spp.alta-envio`, `spp.asignacion-custodia`, etc.). |
| **`acciones-suscriber`** | WORKER | `TYD-SPP` | AKS-BR | .NET | Escucha eventos de acciones y modificaciones operativas originadas en DMS. |
| **`acciones-api`** | API | `TYD-SPP` | AKS-BR | .NET | Endpoint de actualización de acciones sobre bultos. |
| **`geocerca-consumer`** | WORKER | `TYD-SPP` | CCE | .NET | Escucha `geocerca-calculada` y `envios-traza-fin-de-custodia` e invoca a la API de normalización. |
| **`eventosaforo-api`** | WORKER | `TYD-SPP` | CCE | .NET | Suscriptor de `bulto-informado`, procesa métricas de balanza y publica `bulto-pesado-y-medido`. |
| **`dotnet-consolidacion-spp-api`** | WORKER | `TYD-SPP` | CCE | .NET | Suscriptor de `apto-para-consolidar` y publica `bulto-pesado-y-medido`. |
| **`dotnet-stream-EnvioAptoParaConsolidar-publisher`** | WORKER | `TYD-SORTERS` | CCE | .NET | Lee de la tabla `EventosParaPublicar` de Integra y publica eventos `apto-para-consolidar`. |
| **`mq-bridge`** | API | `TYD-SPP` | CCE | .NET | Puente de mensajería para compatibilidad con sistemas MQ legados. |
| **`administracion-api`** | API | `TYD-SPP` | AKS-BR (Migrar a CCE) | .NET | API de backend para gestión y configuración de parámetros de clasificación. |
| **`procesamiento-api`** | API / PUB | `TYD-SPP` | CCE | .NET | Publicador y procesador de eventos de bultos para paquetería. |
| **`consolidacion-automatica-api`** | API | `TYD-SPP` | CCE | .NET | Servicio de consolidación de bultos en contenedores/jaulas. |
| **`oneclick`** | API / PUB | `TYD-SPP` | CCE | .NET | Orquestador de operaciones express de despacho y sincronización. |
| **`tracking-api`** | API | `TYD-SPP` | AKS-BR (Migrar a CCE) | .NET | Consulta de estado de trazabilidad interna de envíos en planta. |
| **`MobileTrackingInternoAPP`** | WEB / APP | `TYD-SPP` | CCE | React / Web | Aplicación web para seguimiento y escaneo manual en planta. |

---

### 1.2. Componentes Específicos del Vertical Sorter

| Componente | Tipo | Namespace | Ambiente / Cluster | Tecnología | Descripción y Rol Operativo |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`spptovertical-suscriber`** | WORKER | `TYD-SPP` | CCE | .NET 6.0 | Suscriptor del tópico `spp.alta-envio`. Inserta el registro en la tabla `tb_evento` de la base `Integración Vertical`. |
| **`job-spptovertical`** (Job Rampa 6) | WORKER | `TYD-SPP` | CCE | .NET / Batch | Job de resiliencia. Pollea `DBSORTER` buscando bultos expulsados por Rampa 6 y los reinyecta en `Integración Vertical`. |
| **`verticaltoSpp-publisher`** | WORKER | `TYD-SPP` | CCE | .NET 6.0 | Background service que lee bultos clasificados de `Integración Vertical`, usa Redis para el cursor y publica eventos a Kafka. |
| **`sortervertical-api`** | WORKER / API | `TYD-SPP` | CCE | .NET 6.0 | Consume eventos de clasificación del Vertical Sorter, procesa aforo (peso/medidas) y actualiza `DBSORTER`. |

---

### 1.3. Componentes TruxSorter (Vanderlande) y Wayzim

| Componente | Tipo | Namespace | Ambiente / Cluster | Tecnología | Descripción y Rol Operativo |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`spp-truxsorter-worker`** | WORKER | `TYD-SORTERS` | AKS-BR | .NET | Worker de integración para el TruxSorter de planta baja CIT (Vanderlande). |
| **`generador-de-archivo-worker`** | WORKER | `TYD-SPP` | AKS-BR | .NET | Genera los archivos batch para alimentación de clasificadores por lotes. |
| **`archivos-pendientes-job`** | WORKER | `TYD-SPP` | AKS-BR | .NET | Job de control y reintento de archivos batch pendientes de procesamiento. |
| **`archivos-excepciones-worker`** | WORKER | `TYD-SPP` | AKS-BR | .NET | Gestión de archivos rechazados o con inconsistencias de formato. |
| **`integration-sorters-api` (Nube)** | API | `TYD-SPP` | AKS-BR | .NET | API central de integración para clasificadores Wayzim. |
| **`integration-sorters-api` (Pacheco)** | API | `TYD-SPP` | K3H (Pacheco) | .NET | Instancia local de baja latencia para el clasificador Wayzim en Pacheco. |
| **`integration-sorters-api` (Avellaneda)** | API | `TYD-SPP` | K3S (Avellaneda) | .NET | Instancia local de baja latencia para el clasificador Wayzim en Avellaneda. |

---

### 1.4. Microservicios de Sorters Regionales e Irregulares (`sorter-delivery-*`)

Todos estos microservicios operan en el namespace **`TYD-SORTERS`** en ambiente **CCE**:

| Servicio | Ubicación / Destino | Finalidad |
| :--- | :--- | :--- |
| `sorter-delivery-bariloche` | Bariloche | Clasificación y derivación local |
| `sorter-delivery-cas` | Casa Central / CAS | Ruteo interno de transferencias |
| `sorter-delivery-chascomus` | Chascomús | Clasificación local |
| `sorter-delivery-cordoba` | Córdoba Planta 1 | Clasificación troncal |
| `sorter-delivery-cordoba-2` | Córdoba Planta 2 | Clasificación distribución |
| `sorter-delivery-ctc` | CTC Roca (CABA) | Clasificación de paquetería urbana |
| `sorter-delivery-ctc2` | CTC 2 | Segundo anillo de clasificación |
| `sorter-delivery-irregulares` | CIT Irregulares | Paquetes de gran porte o formas no estándar |
| `sorter-delivery-irregulares-ctc` | CTC Irregulares | Paquetes irregulares en CTC |
| `sorter-delivery-irregulares-mbp` | MBP Irregulares | Paquetes irregulares en MBP |
| `sorter-delivery-irregulares-tucuman`| Tucumán Irregulares | Clasificación de bultos fuera de norma |
| `sorter-delivery-mardelplata` | Mar del Plata 1 | Clasificación costa atlántica |
| `sorter-delivery-mardelplata-2` | Mar del Plata 2 | Distribución local |
| `sorter-delivery-mendoza` | Mendoza | Clasificación Cuyo |
| `sorter-delivery-salta` | Salta | Clasificación NOA |
| `sorter-delivery-tortugitas` | Tortuguitas | Clasificación Norte GBA |
| `sorter-delivery-tucuman` | Tucumán | Clasificación NOA Troncal |
| `sorter-delivery-villasoldati` | Villa Soldati | Clasificación Sur CABA |
| `sorter-delivery-barracas` | Barracas | Hub logístico de distribución |

---

### 1.5. Capa de Monitoreo Operativo y UI

| Componente | Tipo | Namespace | Ambiente | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| **`spp-dashboard-ui`** | WEB | `TYD-SPP` | AKS-BR (Pasar a CCE) | Frontend de monitoreo en tiempo real de paquetería clasificada (alimentado por réplica de `DBSORTER`). |
| **`reportes-api`** | API | `TYD-SPP` | CCE | Backend de consultas analíticas y rendimiento histórico. |
| **`abm-ui`** | WEB | `TYD-SPP` | CCE | Frontend de configuración de reglas de negocio, rampas y usuarios. |
| **`react-native-spp-app`** | APP | - | Intune | Aplicación móvil para operarios de piso. |

---

## 2. Inventario de Tópicos de Apache Kafka

| Nombre del Tópico | Productores Principales | Consumidores Principales | Finalidad Operativa |
| :--- | :--- | :--- | :--- |
| `orden-envio-solicitada` | API Unificada | DMS, Integra | Inicia el pedido de creación de envío en los TMS. |
| `orden-envio-creada` | DMS, Integra | `spp-altas-suscriber` | Notifica que la orden fue persistida y está lista para ingresar a SPP. |
| `spp.alta-envio` | `publisher-events-spp` | `spptovertical-suscriber` | Notifica un nuevo paquete listo para clasificar en Vertical Sorter. |
| `spp.asignacion-custodia` | `publisher-events-spp` | Sorters Regionales, Hiops/Jiops | Notifica asignación y toma de custodia por un clasificador. |
| `spp.cambio-destino` | `publisher-events-spp` / TMS | SPP, Sorters | Propaga cambios de sucursal o rampa solicitados dinámicamente. |
| `spp.geocerca-calculada` | `publisher-events-spp` | Integra, `geocerca-consumer` | Difunde las coordenadas y zona calculada para sincronización de sistemas. |
| `bulto-informado` | Sorters, Balanzas | `eventosaforo-api` | Emite la lectura cruda de escaneo y peso detectado. |
| `bulto-pesado-y-medido` | `eventosaforo-api` | SPP, Facturación, Trazabilidad | Evento oficial con peso dimensional y métrico consolidado. |
| `apto-para-consolidar` | `dotnet-stream-publisher` | `dotnet-consolidacion-spp-api`| Habilita el bulto para ser consolidado en contenedor final. |
| `spp.bulto-procesado-vertical`| `verticaltoSpp-publisher` | `sortervertical-api` | Reporta el bulto físicamente clasificado en rampa por el Vertical Sorter. |

---

## 3. Bases de Datos y Caches

| Instancia / Identificador | Motor | Topología / Alta Disponibilidad | Uso Principal |
| :--- | :--- | :--- | :--- |
| **`DBSORTER`** (Primario) | Microsoft SQL Server | AlwaysOn Availability Group | Transaccional primario: altas, ruteo, estados y trazabilidad central de bultos. |
| **`DBSORTER`** (Réplica Nodo 2) | Microsoft SQL Server | AlwaysOn Secondary (Read-Only) | Consultas analíticas, reportes y dashboards en vivo (`spp-dashboard-ui`). No debe caerse. |
| **`Integración Vertical`** (Primario) | Microsoft SQL Server | AlwaysOn Availability Group | Tabla intermedia `tb_evento` donde escribe SPP y de donde lee/escribe Optisoft. |
| **`Integración Vertical`** (Nodo 2) | Microsoft SQL Server | AlwaysOn Secondary (Read-Only) | Respaldo y auditoría del circuito vertical. |
| **`DBSORTERPROD`** (Redis) | Redis Cache | Standalone / Sentinel | Almacena el cursor (offset/timestamp) de `verticaltoSpp-publisher` para control de lectura. |
| **`INTEGRA`** | SQL Server / Oracle | Cluster Corporativo | Base de datos maestra de clientes, contratos y logística histórica. |

---

## 4. Inventario de PCs Industriales y Sorters Físicos

| Nombre de PC | Nombre Visible / Ubicación | Dirección IP | En Dominio | Observaciones |
| :--- | :--- | :--- | :--- | :--- |
| `PC100454` | **PC_SORTER_Vertical** (CIT 1° Piso) | `10.20.48.108` | Relevado | PC industrial que corre Optisoft para el clasificador vertical. |
| `PC044588` | **PC_SORTER_Vanderlande** (CIT PB) | `10.20.52.140` | Relevado | Control y procesamiento batch del TruxSorter Vanderlande. |
| `PC029006` | **PC_SORTER_Cordoba 2** | `10.20.177.10` | Relevado | Clasificador troncal Córdoba. |
| `PC040350` | **PC_SORTER_Bariloche** | `10.20.142.101` | Relevado | Clasificador estándar Bariloche. |
| `PC101006` | **PC_SORTER_Bariloche (Irregulares)**| `10.200.86.102` | Relevado | Clasificador de irregulares Bariloche. |
| `PC100062` | **PC_SORTER_Gualeguaychu** | `10.20.145.67` | Relevado | Clasificador Gualeguaychú. |
| `PC043836` | **PC_SORTER_Tucuman** | `10.20.137.49` | Relevado | Clasificador troncal Tucumán. |
| `PC042990` | **PC_SORTER_Tow Line 2** | *A relevar* | Pendiente | Tow Line CIT. |
| `PC035497` | **PC_SORTER_CIT (Irregulares)** | *A relevar* | Pendiente | Clasificador de irregulares CIT. |
| `PC047083` | **PC_SORTER_Tucuman (Irregulares)** | *A relevar* | Pendiente | Clasificador de irregulares Tucumán. |
| `PC100038` | **PC_SORTER_Salta** | *A relevar* | Pendiente | Clasificador Salta. |
| `PC038915` | **PC_SORTER_Bahia (Irregulares)** | *A relevar* | Pendiente | Clasificador Bahía Blanca. |
| `PC044150` | **PC_SORTER_Chascomus** | *A relevar* | Pendiente | Clasificador Chascomús. |
| `PC044652` | **PC_SORTER_Avellaneda** | *A relevar* | Pendiente | Clasificador Avellaneda. |
| `PC047076` | **PC_SORTER_Avellaneda 2** | *A relevar* | Pendiente | Segundo clasificador Avellaneda. |
| `PC046981` | **PC_SORTER_CTC 2** | *A relevar* | Pendiente | Clasificador CTC Roca. |
| `PC047072` | **PC_SORTER_Cordoba AU9** | *A relevar* | Pendiente | Clasificador Córdoba AU9. |
| `PC100036` | **PC_SORTER_Cordoba** | *A relevar* | Pendiente | Clasificador Córdoba Planta Central. |
| `PC100112` | **PC_SORTER_Mendoza** | *A relevar* | Pendiente | Clasificador Mendoza. |
| `PC101044` | **PC_SORTER_Mar del Plata 2** | *A relevar* | Pendiente | Clasificador Mar del Plata. |

---

## 5. Controladores Industriales (PLCs)

- **Marca / Modelo**: **Siemens Simatic S7-400**
- **Protocolo de Diagnóstico de Red**: SNMP v2c / v3 (MIB estándar de automatización industrial y módulos de comunicación Ethernet CP 443-1).
- **Rol en Planta**: Control en tiempo real de fotocélulas, velocidad de cinta, encoders de posición y activación de zapatas o brazos desviadores hacia las rampas de salida.
