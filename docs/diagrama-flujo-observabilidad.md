# Diagrama End-to-End de Observabilidad: Ecosistema Sorters

Este documento contiene el **mapa integral de observabilidad** del circuito de Sorters, con foco en el **Vertical Sorter (CIT 1° Piso)**. Representa el flujo de información y paquetería de punta a punta, señalizando los **puntos de control y sensores de monitoreo (S1 a S10)** recomendados para la instrumentación.

---

## 🗺️ Diagrama de Arquitectura y Puntos de Control

> 💡 **Formatos disponibles para ver el diagrama con flechas y colores:**
> - 🌐 **Visor Interactivo:** Abrir [`diagrama-flujo-observabilidad.html`](./diagrama-flujo-observabilidad.html) en tu navegador con zoom y navegación.
> - 🖼️ **Imagen Vectorial:** Abrir [`diagrama-flujo-observabilidad.svg`](./diagrama-flujo-observabilidad.svg) o [`diagrama-flujo-observabilidad.png`](./diagrama-flujo-observabilidad.png).
> - 👁️ **En el Editor (IDE):** Presiona `Ctrl + Shift + V` (o `Ctrl + K, V`) para abrir la vista previa Markdown de este archivo.

![Diagrama End-to-End de Observabilidad Sorters](./diagrama-flujo-observabilidad.svg)

<details>
<summary><b>Haz clic aquí para ver o editar el código fuente Mermaid</b></summary>

```mermaid
flowchart TD
    classDef client fill:#E1F5FE,stroke:#0288D1,stroke-width:2px;
    classDef tms fill:#F3E5F5,stroke:#7B1FA2,stroke-width:2px;
    classDef spp fill:#E8F5E9,stroke:#388E3C,stroke-width:2px;
    classDef db fill:#FFF3E0,stroke:#F57C00,stroke-width:2px;
    classDef machine fill:#FFEBEE,stroke:#D32F2F,stroke-width:2px;
    classDef obs fill:#FCE4EC,stroke:#C2185B,stroke-width:2px;
    classDef sensor fill:#FFF9C4,stroke:#FBC02D,stroke-width:2px,stroke-dasharray: 5 5;

    %% 1. Ingesta
    subgraph G1 ["1. Capa de Ingesta & TMS"]
        C["Cliente Final / B2C"]:::client
        API_U["API Unificada Andreani"]:::client
        K_SOL["Kafka:<br/>orden-envio-solicitada"]:::tms
        DMS["DMS (Delivery Mgmt)"]:::tms
        INT["Integra (TMS Core)"]:::tms
        K_CREADA["Kafka:<br/>orden-envio-creada"]:::tms
        K_CAMBIOS["Kafka:<br/>cambios-destino"]:::tms
    end

    %% Sensores Ingesta
    S1{{"[S1] Monitor Kafka Lag<br/>& Latencia TMS"}}:::sensor
    K_CREADA -.-> S1

    %% 2. Middleware SPP
    subgraph G2 ["2. Middleware SPP & Enriquecimiento"]
        SUB_A["spp-altas-suscriber<br/>(Worker K8s .NET 6)"]:::spp
        API_A["spp-altas-api<br/>(API K8s .NET 6)"]:::spp
        
        subgraph G_ENRICH ["APIs de Enriquecimiento"]
            API_NDD["API Normalización (NDD)"]:::spp
            API_GEO["API Geo (Lat/Long)"]:::spp
            API_SUC["API Sucursales / Zonificación"]:::spp
        end

        PUB_SPP["publisher-events-spp<br/>(Worker K8s .NET 6)"]:::spp
    end

    %% Sensores SPP
    S2{{"[S2] Latencia & HTTP 5xx<br/>APIs Enriquecimiento"}}:::sensor
    S3{{"[S3] Monitor AlwaysOn DB<br/>& Query Latency"}}:::sensor
    API_A -.-> S2

    %% 3. Bases de Datos Centrales
    subgraph G3 ["3. Persistencia Central Sorters"]
        DB_S_P[("DBSORTER<br/>Nodo Primario (Transaccional)")]:::db
        DB_S_R[("DBSORTER<br/>Nodo Secundario (AlwaysOn)")]:::db
    end

    DB_S_P -.->|"Replicación AlwaysOn"| DB_S_R
    DB_S_R -.-> S3

    %% 4. Tópicos de Distribución SPP
    subgraph G4 ["4. Tópicos de Distribución Kafka SPP"]
        K_ALTA["Kafka: spp.alta-envio"]:::spp
        K_CUST["Kafka: spp.asignacion-custodia"]:::spp
        K_DEST["Kafka: spp.cambio-destino"]:::spp
        K_GEO["Kafka: spp.geocerca-calculada"]:::spp
    end

    S4{{"[S4] Monitor Kafka Lag<br/>spp.alta-envio"}}:::sensor
    K_ALTA -.-> S4

    %% 5. Integración Vertical Sorter
    subgraph G5 ["5. Integración Vertical Sorter"]
        SUB_V["spptovertical-suscriber<br/>(Worker K8s)"]:::spp
        DB_V_P[("DB Integración Vertical<br/>Primario (tb_evento)")]:::db
        DB_V_R[("DB Integración Vertical<br/>Nodo 2 (AlwaysOn)")]:::db
        JOB_R6["job-spptovertical<br/>(Resiliencia Rampa 6)"]:::spp
    end

    DB_V_P -.->|"Replicación"| DB_V_R
    S5{{"[S5] Ratio de Desvío a Rampa 6<br/>(Alarma > 5%)"}}:::sensor
    JOB_R6 -.-> S5

    %% 6. Máquina y Fabricante
    subgraph G6 ["6. Capa de Clasificación Física (CIT 1° Piso)"]
        OPTISOFT["Software Optisoft / Optimus<br/>(PC100454: 10.20.48.108)"]:::machine
        PLC["PLC Siemens Simatic S7-400"]:::machine
        SCANNERS["Lectores Ópticos & Balanzas"]:::machine
        RAMPAS["Rampas de Despacho (1..N)<br/>+ Rampa 6 (Excepciones)"]:::machine
    end

    S6{{"[S6] Heartbeat Optisoft &<br/>ICMP/SNMP Host/PLC"}}:::sensor
    OPTISOFT -.-> S6
    PLC -.-> S6

    %% 7. Retorno de Datos y Cierre de Trazabilidad
    subgraph G7 ["7. Retorno de Datos & Trazabilidad"]
        PUB_V["verticaltoSpp-publisher<br/>(Background Service .NET 6)"]:::spp
        REDIS[("Redis Cache<br/>(DBSORTERPROD Cursor)")]:::db
        K_PROC["Kafka:<br/>spp.bulto-procesado-vertical"]:::spp
        API_V["sortervertical-api<br/>& eventosaforo-api"]:::spp
    end

    S7{{"[S7] Alarma 'Tablero en Cero'<br/>Publisher / Redis Status"}}:::sensor
    PUB_V -.-> S7

    %% 8. Monitoreo Operativo y Dashboards
    subgraph G8 ["8. Monitoreo en Planta & Dashboards"]
        DASH["spp-dashboard-ui<br/>(Monitores de Planta CIT)"]:::obs
        REP_API["reportes-api<br/>(Consultas Analíticas)"]:::obs
    end

    S8{{"[S8] Alarma Disponibilidad Dashboards<br/>& HTTP 5xx Reportes"}}:::sensor
    DASH -.-> S8

    %% Conexiones del Flujo
    C --> API_U
    API_U --> K_SOL
    K_SOL --> DMS & INT
    DMS & INT --> K_CREADA
    DMS & INT --> K_CAMBIOS
    K_CREADA --> SUB_A
    SUB_A --> API_A
    API_A <--> G_ENRICH
    API_A --> DB_S_P
    DB_S_P --> PUB_SPP
    PUB_SPP --> K_ALTA & K_CUST & K_DEST & K_GEO
    
    %% Hacia Vertical
    K_ALTA --> SUB_V
    SUB_V --> DB_V_P
    DB_V_P <--> OPTISOFT
    OPTISOFT <--> PLC
    PLC <--> SCANNERS
    PLC --> RAMPAS

    %% Resiliencia R6
    RAMPAS -.->|"Bultos sin rampa"| JOB_R6
    DB_S_P -.->|"Query Rampa 6"| JOB_R6
    JOB_R6 -.->|"Reinyección tb_evento"| DB_V_P

    %% Retorno
    DB_V_P --> PUB_V
    PUB_V <--> REDIS
    PUB_V --> K_PROC
    K_PROC --> API_V
    API_V --> DB_S_P

    %% Consumo Dashboards
    DB_S_R --> REP_API
    REP_API --> DASH
```
</details>

---

## 🎯 Catálogo de Sensores y Puntos de Control

| Sensor | Punto del Flujo | Métrica / Señal Monitoreada | Severidad y Criterio de Alarma |
| :--- | :--- | :--- | :--- |
| **[S1]** | Ingesta Kafka (`orden-envio-creada`) | Consumer Lag de `spp-altas-suscriber`. | **P1**: Lag > 1.000 mensajes sostenido por más de 5 minutos. |
| **[S2]** | APIs de Enriquecimiento (NDD / Geo / Sucursales) | Latencia HTTP P95 y tasa de error HTTP 5xx. | **P2**: Latencia > 800 ms o tasa de error > 2% durante 3 minutos. |
| **[S3]** | Clúster `DBSORTER` (AlwaysOn) | Estado de replicación del nodo secundario (Réplica de lectura). | **P1**: Estado `NOT SYNCHRONIZING` o réplica inalcanzable (afecta tableros). |
| **[S4]** | Tópico Kafka `spp.alta-envio` | Consumer Lag de `spptovertical-suscriber`. | **P2**: Lag > 300 mensajes. Retraso en la preparación de bultos en Vertical. |
| **[S5]** | Resiliencia Rampa 6 (`job-spptovertical`) | Porcentaje de paquetes desviados a Rampa 6 respecto al total clasificado. | **P2**: Tasa de Rampa 6 > 5% en la última hora (indica fallas de pre-sincronización o etiquetas rotas). |
| **[S6]** | Software Proveedor y Hardware (Optisoft + Siemens S7-400) | Actividad de polling en `tb_evento`, ICMP Ping a `10.20.48.108` y SNMP a PLC. | **P1**: Sin actualización en `tb_evento` con bultos en cola > 5 min, o Host inalcanzable. |
| **[S7]** | Publicador de Retorno (`verticaltoSpp-publisher`) | Estado del Pod en K8s, conectividad a Redis (`DBSORTERPROD`) y tasa de eventos emitidos. | **P1**: Pod caído o 0 bultos emitidos durante 10 min en franja operativa ("Tablero en Cero"). |
| **[S8]** | Tableros Operativos (`spp-dashboard-ui`) | Disponibilidad HTTP 200 y tiempo de carga de vistas de supervisor. | **P2**: UI no accesible o `reportes-api` devolviendo errores de timeout. |
| **[S9]** | Tópico de Custodia (`spp.asignacion-custodia`) | Lag de consumo de sorters regionales e in-house (Giops). | **P3**: Lag elevado en sucursales particulares (aislamiento de red en planta remota). |
| **[S10]** | Sincronización de Modificaciones (`spp.cambio-destino`) | Latencia de impacto de redirecciones solicitadas por clientes. | **P3**: Demora en la actualización de paquetes que cambiaron de sucursal. |

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
+------------------------------------+-------------------------------------------+----------------------------------------------+
```
