# 06. Ecosistema SPP (Sistema de Paquetería y Procesamiento)

El **SPP (`tyd-spp`)** es la plataforma troncal de Andreani responsable de orquestar la paquetería, las altas de envíos, los aforos dinámicos, la consolidación en contenedores y la interfaz bidireccional con los clasificadores automáticos (**Sorters**).

> 📁 **Fuente Oficial:** Sincronizado automáticamente desde la plataforma de arquitectura [**GitOps Andreani**](https://ui-gitops-prod.apps.andreani.com.ar/aplicaciones?view=table&section=detalles&projectId=51) | Proyecto: `tyd-spp` (ID: 51) | Owner Técnico: `sbecerra@andreani.com`.

---

## 🗺️ Arquitectura de Integración: ¿Cómo interactúan SPP y los Sorters?

Los Sorters físicos (Vertical, Wayzim, etc.) no toman decisiones de ruteo de forma aislada. Dependen de SPP para saber hacia qué rampa expulsar cada bulto y para notificar la confirmación del pesaje y la clasificación:

```mermaid
graph TD
    subgraph Ingesta y Preparación en SPP
        K1["Kafka: OrdenEnvioCreada"] --> AS["spp-altas-suscriber"]
        AS --> AA["spp-altas-api"]
        AA --> DB[("DBSORTER (SQL Server)")]
    end

    subgraph Despacho hacia Sorter
        DB --> SVS["spptovertical-suscriber"]
        SVS --> IV[("Integración Vertical")]
        IV --> HW["Software Proveedor / PLC Sorter"]
    end

    subgraph Ciclo de Clasificación y Retorno
        HW -- "Clasificado Exitoso" --> VTP["verticaltospp-publisher"]
        VTP --> SVA["sortervertical-api"]
        SVA --> EAF["eventosdeaforo-api"]
        EAF --> PES["publisher-events-spp"]
        PES --> K2["Kafka: Eventos SPP / Trazabilidad"]
    end

    subgraph Loop de Resiliencia (Rampa 6)
        HW -- "Rechazo / Sin Destino" --> R6["Expulsión a Rampa 6"]
        R6 --> JOB["job-spptovertical"]
        JOB -- "Reinyecta para re-clasificación" --> IV
    end
```

---

## 📊 Resumen Ejecutivo del Parque de Aplicaciones

| Métrica | Valor | Observaciones |
| :--- | :---: | :--- |
| **Total de Aplicaciones Registradas** | **42** | Catálogo oficial en `operations-innovation` |
| **Aplicaciones Activas en Producción** | **31** | Servicios productivos operando en planta |
| **En Desarrollo / Modernización** | **9** | Módulos en construcción o evolución |
| **Desactivadas / Legadas** | **2** | Servicios retirados |
| **Stack Tecnológico Principal** | **.NET (38) / React (3)** | C# (APIs/Workers) y JavaScript/TypeScript (Frontends) |

---

## 1. Integración con Sorters (Clasificación Automatizada)

| Aplicación | Tipo / Plantilla | Estado | Cobertura | Calidad | Repositorio GitHub |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **[`job-spptovertical`](https://github.com/operations-innovation/job-spptovertical)** | NET (platform-worker) | 🟢 Activa | 100,00% | ✅ OK | [Ver Repositorio ↗](https://github.com/operations-innovation/job-spptovertical) |
| **[`sortervertical-api`](https://github.com/operations-innovation/dotnet-SorterVertical-SPP-API)** | NET (platform-worker) | 🟢 Activa | 81,80% | ✅ OK | [Ver Repositorio ↗](https://github.com/operations-innovation/dotnet-SorterVertical-SPP-API) |
| **[`spptovertical-suscriber`](https://github.com/operations-innovation/dotnet-spptovertical-suscriber)** | NET (platform-worker) | 🟢 Activa | 91,70% | ✅ OK | [Ver Repositorio ↗](https://github.com/operations-innovation/dotnet-spptovertical-suscriber) |
| **[`vertical-sorter-worker`](https://github.com/operations-innovation/tyd-spp-vertical-sorter-worker)** | NET (platform-worker) | 🟡 En Desarrollo | 98,10% | ✅ OK | [Ver Repositorio ↗](https://github.com/operations-innovation/tyd-spp-vertical-sorter-worker) |
| **[`verticaltospp-publisher`](https://github.com/operations-innovation/dotnet-verticaltospp-publisher)** | NET (platform-Web-api) | 🟢 Activa | 100,00% | ✅ OK | [Ver Repositorio ↗](https://github.com/operations-innovation/dotnet-verticaltospp-publisher) |
| **[`integration-sorters-api`](https://github.com/operations-innovation/tyd-spp-integration-sorters-api)** | NET (platform-Web-api) | 🟢 Activa | 0,00% | ❌ ERROR | [Ver Repositorio ↗](https://github.com/operations-innovation/tyd-spp-integration-sorters-api) |

---

## 2. Ingesta, Altas y Procesamiento Core

| Aplicación | Tipo / Plantilla | Estado | Cobertura | Calidad | Repositorio GitHub |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **[`spp-altas-api`](https://github.com/operations-innovation/dotnet-spp-altas-api)** | NET (platform-Web-api) | 🟢 Activa | 69,30% | ❌ ERROR | [Ver Repositorio ↗](https://github.com/operations-innovation/dotnet-spp-altas-api) |
| **[`spp-altas-suscriber`](https://github.com/operations-innovation/dotnet-spp-altas-suscriber)** | NET (platform-Web-api) | 🟢 Activa | 80,00% | ✅ OK | [Ver Repositorio ↗](https://github.com/operations-innovation/dotnet-spp-altas-suscriber) |
| **[`procesamiento-api`](https://github.com/operations-innovation/dotnet-Procesamiento-SPP-API)** | NET (platform-Web-api) | 🟢 Activa | 77,60% | ❌ ERROR | [Ver Repositorio ↗](https://github.com/operations-innovation/dotnet-Procesamiento-SPP-API) |
| **[`publisher-events-spp`](https://github.com/operations-innovation/publisher-events-spp)** | NET (platform-Web-api) | 🟢 Activa | 96,50% | ✅ OK | [Ver Repositorio ↗](https://github.com/operations-innovation/publisher-events-spp) |
| **[`bulto-informado-worker`](https://github.com/operations-innovation/tyd-spp-bulto-informado-worker)** | NET (platform-worker) | 🟡 En Desarrollo | 0,00% | ❌ ERROR | [Ver Repositorio ↗](https://github.com/operations-innovation/tyd-spp-bulto-informado-worker) |
| **[`oneclick-api`](https://github.com/operations-innovation/dotnet-OneClick-SPP-API)** | NET (platform-Web-api) | 🟢 Activa | 70,90% | ❌ ERROR | [Ver Repositorio ↗](https://github.com/operations-innovation/dotnet-OneClick-SPP-API) |

---

## 3. Consolidación de Bultos y Contenedores

| Aplicación | Tipo / Plantilla | Estado | Cobertura | Calidad | Repositorio GitHub |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **[`consolidacion-api`](https://github.com/operations-innovation/dotnet-consolidacion-spp-api)** | NET (platform-Web-api) | 🟢 Activa | 93,20% | ❌ ERROR | [Ver Repositorio ↗](https://github.com/operations-innovation/dotnet-consolidacion-spp-api) |
| **[`consolidacionautomatica-api`](https://github.com/operations-innovation/dotnet-consolidacion-automatica-spp-api)** | NET (platform-Web-api) | 🟢 Activa | 81,60% | ✅ OK | [Ver Repositorio ↗](https://github.com/operations-innovation/dotnet-consolidacion-automatica-spp-api) |
| **[`consolidacion-bultos-worker`](https://github.com/operations-innovation/tyd-spp-consolidacion-bultos-worker)** | NET (platform-worker) | 🟡 En Desarrollo | 0,00% | ❌ ERROR | [Ver Repositorio ↗](https://github.com/operations-innovation/tyd-spp-consolidacion-bultos-worker) |
| **[`contenedores-suscriber`](https://github.com/operations-innovation/spp-contenedores-suscriber)** | NET (platform-Web-api) | 🟡 En Desarrollo | 84,30% | ✅ OK | [Ver Repositorio ↗](https://github.com/operations-innovation/spp-contenedores-suscriber) |
| **[`contenedores-to-integra`](https://github.com/operations-innovation/spp-contenedores-to-integra)** | NET (platform-Web-api) | 🟢 Activa | 91,40% | ✅ OK | [Ver Repositorio ↗](https://github.com/operations-innovation/spp-contenedores-to-integra) |
| **[`cierredecontendorspp-worker`](https://github.com/operations-innovation/tyd-spp-cierredecontendorspp-worker)** | NET (platform-worker) | 🟡 En Desarrollo | - | ⚪ Sin datos | [Ver Repositorio ↗](https://github.com/operations-innovation/tyd-spp-cierredecontendorspp-worker) |
| **[`cierredecontenedorspp-worker`](https://github.com/operations-innovation/tyd-spp-cierredecontenedorspp-worker)** | NET (platform-worker) | 🟡 En Desarrollo | - | ⚪ Sin datos | [Ver Repositorio ↗](https://github.com/operations-innovation/tyd-spp-cierredecontenedorspp-worker) |

---

## 4. Medición, Aforo y Geocercas

| Aplicación | Tipo / Plantilla | Estado | Cobertura | Calidad | Repositorio GitHub |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **[`eventosdeaforo-api`](https://github.com/operations-innovation/dotnet-EventosDeAforo-SPP-API)** | NET (platform-Web-api) | 🟢 Activa | 89,30% | ✅ OK | [Ver Repositorio ↗](https://github.com/operations-innovation/dotnet-EventosDeAforo-SPP-API) |
| **[`geocerca-consumer`](https://github.com/operations-innovation/dotnet-geocerca-consumer)** | NET (platform-Web-api) | 🟢 Activa | 48,50% | ❌ ERROR | [Ver Repositorio ↗](https://github.com/operations-innovation/dotnet-geocerca-consumer) |

---

## 5. Distribución y Abastecimiento a Sucursales

| Aplicación | Tipo / Plantilla | Estado | Cobertura | Calidad | Repositorio GitHub |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **[`spp-sucursal-abastecedora-worker`](https://github.com/operations-innovation/tyd-spp-spp-sucursal-abastecedora-worker)** | NET (platform-worker) | 🟡 En Desarrollo | - | ⚪ Sin datos | [Ver Repositorio ↗](https://github.com/operations-innovation/tyd-spp-spp-sucursal-abastecedora-worker) |
| **[`sucursal-abastecedora-spp-worker`](https://github.com/operations-innovation/tyd-spp-sucursal-abastecedora-spp-worker)** | NET (platform-worker) | 🟢 Activa | - | ⚪ Sin datos | [Ver Repositorio ↗](https://github.com/operations-innovation/tyd-spp-sucursal-abastecedora-spp-worker) |

---

## 6. Interfaces de Usuario y Aplicaciones Web (React)

| Aplicación | Tipo / Plantilla | Estado | Cobertura | Calidad | Repositorio GitHub |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **[`spp-ui`](https://github.com/operations-innovation/react-spp-ui)** | REACT (template-rsbuild) | 🟢 Activa | 7,80% | ❌ ERROR | [Ver Repositorio ↗](https://github.com/operations-innovation/react-spp-ui) |
| **[`spp-dashboard-ui`](https://github.com/operations-innovation/react-spp-dashboard-ui)** | REACT (cra-template) | 🟢 Activa | 18,20% | ❌ ERROR | [Ver Repositorio ↗](https://github.com/operations-innovation/react-spp-dashboard-ui) |
| **[`trackinginternoui`](https://github.com/operations-innovation/MobileTrackingInternoApp)** | REACT (cra-template) | 🟢 Activa | - | ⚪ Sin datos | [Ver Repositorio ↗](https://github.com/operations-innovation/MobileTrackingInternoApp) |

---

## 7. Trazabilidad Interna, Reportes y Archivos

| Aplicación | Tipo / Plantilla | Estado | Cobertura | Calidad | Repositorio GitHub |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **[`tracking-api`](https://github.com/operations-innovation/tyd-spp-tracking-api)** | NET (platform-Web-api) | 🟢 Activa | 98,40% | ✅ OK | [Ver Repositorio ↗](https://github.com/operations-innovation/tyd-spp-tracking-api) |
| **[`reportes-api`](https://github.com/operations-innovation/dotnet-reportes-spp-api)** | NET (platform-Web-api) | 🟢 Activa | 54,20% | ❌ ERROR | [Ver Repositorio ↗](https://github.com/operations-innovation/dotnet-reportes-spp-api) |
| **[`generador-de-archivo-worker`](https://github.com/operations-innovation/spp-generador-de-archivo-worker)** | NET (platform-worker) | 🟢 Activa | 93,20% | ✅ OK | [Ver Repositorio ↗](https://github.com/operations-innovation/spp-generador-de-archivo-worker) |

---

## 8. Gateways, Puentes e Integraciones de Negocio

| Aplicación | Tipo / Plantilla | Estado | Cobertura | Calidad | Repositorio GitHub |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **[`gateway-hop-api`](https://github.com/operations-innovation/tyd-spp-gateway-hop-api)** | NET (platform-Web-api) | 🟡 En Desarrollo | 0,00% | ❌ ERROR | [Ver Repositorio ↗](https://github.com/operations-innovation/tyd-spp-gateway-hop-api) |
| **[`mq-bridge-api`](https://github.com/operations-innovation/dotnet-mq-bridge)** | NET (platform-Web-api) | 🟡 En Desarrollo | 0,00% | ❌ ERROR | [Ver Repositorio ↗](https://github.com/operations-innovation/dotnet-mq-bridge) |
| **[`natura-spp-publisher`](https://github.com/operations-innovation/dotnet-natura-spp-publisher)** | NET (platform-Web-api) | ⚪ Desactivada | 79,20% | ❌ ERROR | [Ver Repositorio ↗](https://github.com/operations-innovation/dotnet-natura-spp-publisher) |

---

## 9. Otras Aplicaciones y Servicios

| Aplicación | Tipo / Plantilla | Estado | Cobertura | Calidad | Repositorio GitHub |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **[`acciones-api`](https://github.com/operations-innovation/spp-acciones-api)** | NET (platform-Web-api) | 🟢 Activa | 82,20% | ❌ ERROR | [Ver Repositorio ↗](https://github.com/operations-innovation/spp-acciones-api) |
| **[`acciones-suscriber`](https://github.com/operations-innovation/spp-acciones-suscriber)** | NET (platform-worker) | 🟢 Activa | 82,10% | ❌ ERROR | [Ver Repositorio ↗](https://github.com/operations-innovation/spp-acciones-suscriber) |
| **[`actualizacion-destino-integra`](https://github.com/operations-innovation/job-actualizacion-destino-integra)** | NET (platform-worker) | 🟢 Activa | 84,30% | ✅ OK | [Ver Repositorio ↗](https://github.com/operations-innovation/job-actualizacion-destino-integra) |
| **[`actualizadorsucursales-worker`](https://github.com/operations-innovation/tyd-spp-actualizadorsucursales-worker)** | NET (platform-worker) | 🟢 Activa | - | ⚪ Sin datos | [Ver Repositorio ↗](https://github.com/operations-innovation/tyd-spp-actualizadorsucursales-worker) |
| **[`administracion-api`](https://github.com/operations-innovation/dotnet-AdministracionSpp-SPP-API)** | NET (platform-Web-api) | 🟢 Activa | 31,30% | ❌ ERROR | [Ver Repositorio ↗](https://github.com/operations-innovation/dotnet-AdministracionSpp-SPP-API) |
| **[`alta-unidad-ope-sus`](https://github.com/operations-innovation/spp-alta-unidad-operativa-suscriber)** | NET (platform-Web-api) | 🟢 Activa | 90,60% | ✅ OK | [Ver Repositorio ↗](https://github.com/operations-innovation/spp-alta-unidad-operativa-suscriber) |
| **[`altas-boq`](https://github.com/operations-innovation/dotnet-spp-altas-suscriber-boq)** | NET (platform-worker) | ⚪ Desactivada | - | ⚪ Sin datos | [Ver Repositorio ↗](https://github.com/operations-innovation/dotnet-spp-altas-suscriber-boq) |
| **[`app-spp`](https://github.com/operations-innovation/tyd-spp-app-spp)** | React Native (TemplatePlatformMobile) | 🟢 Activa | 71,40% | ❌ ERROR | [Ver Repositorio ↗](https://github.com/operations-innovation/tyd-spp-app-spp) |
| **[`archivos-excepciones-worker`](https://github.com/operations-innovation/spp-generador-de-archivo-excepciones-worker)** | NET (platform-worker) | 🟢 Activa | 92,60% | ✅ OK | [Ver Repositorio ↗](https://github.com/operations-innovation/spp-generador-de-archivo-excepciones-worker) |
| **[`archivos-pendientes-job`](https://github.com/operations-innovation/spp-generador-de-archivo-job)** | NET (platform-worker) | 🟢 Activa | 90,50% | ✅ OK | [Ver Repositorio ↗](https://github.com/operations-innovation/spp-generador-de-archivo-job) |

---
