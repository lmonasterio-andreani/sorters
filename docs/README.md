# 📚 Documentación Oficial del Proyecto: Ecosistema de Sorters

Bienvenido al directorio central de documentación técnica del proyecto de **Observabilidad y Arquitectura de Sorters** de **Andreani Logística**.

En esta carpeta se consolida todo el trabajo de modelado, inventario, diseño de resiliencia y especificaciones de observabilidad para el ecosistema de clasificadores automáticos de la compañía.

---

## 🧭 Mapa de Documentos del Proyecto

| Orden | Documento | Enfoque Principal | Audiencia Objetivo |
| :---: | :--- | :--- | :--- |
| **01** | [**`01-arquitectura-general.md`**](./01-arquitectura-general.md) | Visión macro de negocio, tipología de los 5 tipos de Sorters y las 5 capas tecnológicas de la plataforma. | Arquitectura, Líderes Técnicos, Operaciones |
| **02** | [**`02-flujo-end-to-end-vertical.md`**](./02-flujo-end-to-end-vertical.md) | Recorrido secuencial paso a paso (6 fases) del Vertical Sorter (CIT 1° Piso) y diseño del loop de resiliencia de Rampa 6. | Desarrolladores, SysAdmins, Observabilidad |
| **03** | [**`03-inventario-componentes.md`**](./03-inventario-componentes.md) | Catálogo unificado de más de 50 microservicios, tópicos Kafka, bases AlwaysOn SQL Server, Redis y 20 PCs industriales de Sorters. | DevOps, SRE, DBA, Soporte L2/L3 |
| **04** | [**`04-estrategia-observabilidad.md`**](./04-estrategia-observabilidad.md) | Los 4 pilares de monitoreo, matriz de SLIs/SLOs, clasificación de alarmas P1 a P3 y runbooks operativos ante incidentes críticos. | Equipos de Observabilidad, Centro de Control (NOC), Guardias |
| **05** | [**`05-flujo-observabilidad.md`**](./05-flujo-observabilidad.md) | Mapa integral de flujo de datos con la especificación de los 10 sensores de monitoreo (S1 a S10) y diagramas interactivos. | Todos los equipos técnicos |

---

## 🎨 Subdirectorios y Recursos Internos

- [**`diagramas/`**](./diagramas/README.md): Repositorio centralizado con todos los diagramas vectoriales SVG, gráficos PNG y visores interactivos HTML.
- **`assets/`**: Hojas de estilo corporativas ([`cartesian.css`](./assets/cartesian.css)) y recursos visuales.
- [**`guia-estilos-cartesian.md`**](./guia-estilos-cartesian.md): **Guía interna** del sistema de diseño Andreani Cartesian y tokens de estilo para desarrolladores. *(No visible en el menú principal del portal)*.

---

## 🔗 Fuentes y Evidencias de Relevamiento

Los datos de origen que dieron sustento a esta documentación formal se encuentran resguardados y clasificados por sección en:
- [**`relevamiento/reuniones/`**](../relevamiento/reuniones/README.md): Minutas y grabaciones de audio/video.
- [**`relevamiento/diagramas/`**](../relevamiento/diagramas/README.md): Fuentes editables Draw.io y bocetos iniciales.
- [**`relevamiento/planillas/`**](../relevamiento/planillas/README.md): Toma de servicio técnica en formato Excel.

> 🌐 **Portal Interactivo:** Para visualizar toda la documentación navegable con buscador integrado, zoom de diagramas y selector de temas, abre el archivo [**`Sorters.html`**](../Sorters.html) en tu navegador.
