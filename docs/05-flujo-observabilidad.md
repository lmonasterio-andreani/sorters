# 05. Diagrama End-to-End y Puntos de Control de Observabilidad: Ecosistema Sorters

> 🚧 **DOCUMENTO EN PROCESO DE REVISIÓN TÉCNICA**  
> *Este contenido es un borrador preliminar y se encuentra en etapa de adecuación metodológica interna para alinearse con los lineamientos del [**Estándar de Incorporación de Servicios al Modelo de Observabilidad**](../estandar-observabilidad/README.md).*

---

Este documento describe el **flujo de observabilidad de punta a punta** para el ecosistema de Sorters de Andreani, focalizado en la operación del **Vertical Sorter (CIT 1° Piso)** y su integración con los microservicios de **SPP (Sistema de Planificación de Paquetería)**.

Alineado con el estándar metodológico oficial de la organización, los **10 sensores y puntos de control (S1 a S10)** se organizan en las **4 capacidades técnicas de observabilidad** (APM, Infraestructura, Logs y UX/Sintéticos) y alimentan la doble visualización requerida: **Dashboard Operativo** (L2/L3 y NOC) y **Dashboard Ejecutivo** (Líderes y Negocio).

---

## 🗺️ Diagrama de Arquitectura End-to-End y Sensores

> 💡 **Formatos disponibles para ver el diagrama con flechas y colores:**
> - 🌐 **Visor Interactivo:** Abrir [`diagramas/diagrama-flujo-observabilidad.html`](./diagramas/diagrama-flujo-observabilidad.html) en tu navegador con zoom y navegación.
> - 🖼️ **Imagen Vectorial:** Abrir [`diagramas/diagrama-flujo-observabilidad.svg`](./diagramas/diagrama-flujo-observabilidad.svg) o [`diagramas/diagrama-flujo-observabilidad.png`](./diagramas/diagrama-flujo-observabilidad.png).
> - 📁 **Catálogo Completo:** Ver todos los diagramas en [**`docs/diagramas/`**](./diagramas/README.md).

![Diagrama End-to-End de Observabilidad Sorters](./diagramas/diagrama-flujo-observabilidad.svg)

---

## 🎯 Clasificación de Sensores según Capacidades del Estándar

A continuación se detallan los 10 puntos de control del circuito clasificados según la capacidad técnica de observabilidad correspondiente:

### 1. Capacidad APM (Application Performance Monitoring) & Tracing
*Responsable Funcional:* Discovery | *Implementación:* Platform y Equipo SPP.

| Sensor | Componente Monitoreado | Señal / Métrica Observada | Umbral y Severidad |
| :--- | :--- | :--- | :--- |
| **[S1]** | Ingesta Kafka (`orden-envio-creada`) | Consumer Lag de `spp-altas-suscriber` y tiempo de propagación de traza `X-Trace-Id`. | **P1**: Lag > 1.000 mensajes sostenido por más de 5 min. |
| **[S2]** | APIs de Enriquecimiento (NDD / Geo / Sucursales) | Latencia HTTP P95, tasa de error HTTP 5xx y tiempo de respuesta en llamadas salientes. | **P2**: Latencia > 800 ms o tasa de error > 2% durante 3 min consecutivos. |
| **[S7]** | Publicador de Retorno (`verticaltoSpp-publisher`) | Transacciones APM activas, tiempo de procesamiento de batches de Redis y despacho a Kafka. | **P1**: 0 eventos emitidos durante 10 min en franja operativa de clasificación ("Tablero en Cero"). |
| **[S8]** | Backend de Reportes (`reportes-api`) | Latencia de endpoints de consulta y disponibilidad para la UI operativa. | **P2**: Latencia > 1.200 ms o timeouts frecuentes afectando a supervisores de planta. |

---

### 2. Capacidad Monitoreo de Infraestructura (Zabbix & K8s)
*Responsable:* Platform | *Acompaña:* Discovery y Equipo del Servicio.

| Sensor | Componente Monitoreado | Señal / Métrica Observada | Umbral y Severidad |
| :--- | :--- | :--- | :--- |
| **[S3]** | Clúster `DBSORTER` (SQL AlwaysOn) | Estado de replicación del nodo secundario (Réplica de lectura), latencia de réplica y cola de transacciones. | **P1**: Estado `NOT SYNCHRONIZING` o lag de replicación > 15 segundos sostenido. |
| **[S6]** | Hardware Industrial y Software Proveedor | ICMP Ping a PC industrial `10.20.48.108`, SNMP a PLC Siemens S7-400 y consumo de recursos en host de Optisoft. | **P1**: Host o PLC inalcanzable por red, o fallas en interfaz Ethernet industrial. |

---

### 3. Capacidad Logs y Trazabilidad (Elasticsearch / Kibana ECS)
*Responsable Funcional:* Discovery | *Implementación:* Platform y Equipo SPP.

| Sensor | Componente Monitoreado | Señal / Métrica Observada | Umbral y Severidad |
| :--- | :--- | :--- | :--- |
| **[S5]** | Resiliencia Rampa 6 (`job-spptovertical`) | Volumen de logs de paquetes derivados a Rampa 6 por falta de sincronización previa o bultos no reconocidos. | **P2**: Desvíos a Rampa 6 > 5% del total clasificado en la última hora. |
| **[S9]** | Tópico de Custodia (`spp.asignacion-custodia`) | Logs de emisión y consumer lag en sorters regionales / Giops. | **P3**: Acumulación de lag en nodos remotos por corte de enlace regional. |
| **[S10]** | Modificación de Destino (`spp.cambio-destino`) | Auditoría de actualización de datos de rampa sobre paquetes ya pre-cargados en memoria del sorter. | **P3**: Demora > 30 segundos en el impacto de redirección solicitada por cliente. |

---

### 4. Capacidad UX y Monitoreo Sintético
*Responsable Funcional:* Discovery | *Implementación:* Platform.

| Sensor | Componente Monitoreado | Señal / Métrica Observada | Umbral y Severidad |
| :--- | :--- | :--- | :--- |
| **[S4]** | Tópico Kafka `spp.alta-envio` | Consumer Lag de `spptovertical-suscriber`. Mide el retardo en preparar bultos para el sorter antes de que el paquete llegue físicamente al escáner. | **P2**: Lag > 300 mensajes (riesgo inminente de caída en Rampa 6 por falta de pre-sincronización). |
| **[S6-S]** | Heartbeat de Caja Negra (Optisoft / `tb_evento`) | Sonda sintética periódica verificando actualización de `FechaModificacion` cuando existen bultos pendientes de clasificación. | **P1**: Sin actualización en `tb_evento` durante > 5 minutos con paquetes en cola física. |
| **[S8-S]** | Portales Web (`spp-dashboard-ui`, `spp-ui`) | Sonda sintética HTTP/HTTPS externa de disponibilidad (código 200) y tiempo de carga total del frontend. | **P2**: Tiempo de carga > 3.5 segundos o código HTTP distinto de 200. |

---

## 📊 Mapeo hacia Dashboards Estándar

En concordancia con el estándar corporativo, la telemetría recolectada por los 10 sensores se proyecta en dos dashboards con propósitos y audiencias diferenciadas:

```mermaid
graph TD
    subgraph Sensores Ecosistema Sorters
        S1["[S1] Ingesta Kafka"]
        S2["[S2] APIs Enriquecimiento"]
        S3["[S3] SQL AlwaysOn"]
        S4["[S4] Sincronización Previa"]
        S5["[S5] Resiliencia Rampa 6"]
        S6["[S6] PC Industrial y PLC"]
        S7["[S7] Worker Retorno"]
        S8["[S8] Tableros y APIs UI"]
        S9["[S9] Custodia Regional"]
        S10["[S10] Cambio Destino"]
    end

    subgraph Dashboards Estándar
        DO["🛠️ DASHBOARD OPERATIVO<br/><i>(Soporte L2/L3, NOC, Operaciones Planta)</i>"]
        DE["📈 DASHBOARD EJECUTIVO<br/><i>(Líderes Técnicos, Gerencia Operaciones)</i>"]
    end

    S1 --> DO
    S2 --> DO
    S3 --> DO
    S4 --> DO
    S5 --> DO
    S6 --> DO
    S7 --> DO
    S8 --> DO
    S9 --> DO
    S10 --> DO

    S1 -.->|Volumen Ingesta| DE
    S5 -.->|% Fallas Primer Intento| DE
    S7 -.->|Throughput Bultos/Hora| DE
    S3 -.->|Disponibilidad Circuito (SLO)| DE
    S8 -.->|SLA Acceso Servicios| DE
```

### Dashboard Operativo (Diagnóstico en Vivo)
* **Destinatarios:** Equipo de Soporte L2/L3, Guardias SRE, NOC y Supervisores de Planta CIT.
* **Componentes alimentados por sensores:**
  1. **Semáforo de Hardware y Conectividad Industrial (S6):** Ping ICMP a `10.20.48.108` y estado de enlaces.
  2. **Cola de Ingesta y Lag de Mensajería (S1, S4, S9):** Gráficos de líneas con el consumer lag en tiempo real de cada worker.
  3. **Salud de Base de Datos y Réplicas (S3):** Indicador de estado de sincronización de `DBSORTER` (Nodo 1 vs. Réplica Nodo 2).
  4. **Tasa de Desvíos a Rampa 6 (S5):** Indicador porcentual con alarma de umbral superior a 5%.
  5. **Monitor de Actividad del Publicador (S7):** Tasa de paquetes emitidos hacia Kafka en los últimos 5/15 minutos para detectar tempranamente "Tableros en Cero".

### Dashboard Ejecutivo (Nivel de Servicio y Negocio)
* **Destinatarios:** Jefatura de Operaciones, Product Owners, Gerencia de Logística e IT.
* **Métricas consolidadas:**
  1. **SLO de Disponibilidad del Ecosistema:** Porcentaje de tiempo mensual con el circuito operativo (> 99.5%).
  2. **Throughput de Clasificación (Bultos/Hora):** Curva de procesamiento real versus capacidad nominal del Vertical Sorter.
  3. **Índice de Eficiencia de Clasificación (First-Pass Sort):** Porcentaje de bultos clasificados con éxito sin requerir reinducción vía Rampa 6.
  4. **Tiempos de Ciclo de Información:** Latencia media desde que un bulto es leído en el escáner hasta que su estado impacta en los sistemas troncales de tracking.

---

## 🛡️ Matriz de Mitigación de Puntos Únicos de Falla (SPOF)

```text
+------------------------------------+-------------------------------------------+----------------------------------------------+
| Componente Crítico                 | Modo de Falla                             | Mecanismo de Resiliencia Implementado        |
+------------------------------------+-------------------------------------------+----------------------------------------------+
| spp-altas-api                      | Caída de API NDD / Geo                    | Encolamiento en Kafka + Reintentos con Backoff|
| Integración Vertical               | Bulto antiguo depurado (> 15/30 días)     | Rampa 6 física + job-spptovertical (polling) |
| verticaltoSpp-publisher            | Caída de conexión a Redis Cursor          | Resguardo de offset en memoria + reconexión  |
| DBSORTER (Primario)                | Falla de hardware en servidor SQL         | Conmutación por error automática (AlwaysOn)  |
| DBSORTER (Réplica de Lectura)      | Desincronización o reinicio de réplica    | Fallback controlado hacia nodo primario      |
| PC Industrial Optisoft             | Desconexión de cable de red / Switch      | Alarma inmediata P1 en Zabbix por ICMP/SNMP  |
+------------------------------------+-------------------------------------------+----------------------------------------------+
```
