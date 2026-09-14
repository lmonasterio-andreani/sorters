# 📁 Material de Relevamiento - Ecosistema Sorters

Esta carpeta centraliza todos los **documentos de trabajo, minutas, planillas y grabaciones** generados y recopilados durante las reuniones de relevamiento con los distintos equipos involucrados (Arquitectura, Desarrollo SPP, Operaciones, Infraestructura y Soporte).

Sirve como la **fuente de verdad histórica** y repositorio de evidencias a partir del cual se elaboró y estructuró la documentación oficial en el portal [Sorter.html](../Sorter.html) y en la carpeta [`docs/`](../docs/).

---

## 📋 Inventario de Documentos Relevados

| Archivo | Tipo de Archivo | Descripción y Contenido |
| :--- | :--- | :--- |
| **`Observabilidad integral de los Sorters 01.docx`** | Documento Word | Minuta técnica y notas detalladas de la sesión de relevamiento. Contiene la explicación de los flujos de negocio, el rol del middleware SPP, el comportamiento de la Rampa 6, la réplica de lectura AlwaysOn y las directivas de alarmado. |
| **`Toma_de_Servicio - Sorters.xlsx`** | Planilla Excel | Matriz exhaustiva de toma de servicio con el inventario de componentes: más de 50 microservicios, namespaces de Kubernetes (`TYD-SPP`, `TYD-SORTERS`), clústeres (CCE, AKS-BR, K3H, K3S), inventario de PCs industriales de cada sucursal con sus IPs y roles. |
| **`mapa de monitoreo sorter.drawio`** | Diagrama Draw.io | Archivo fuente editable en Draw.io que sirvió como base para modelar los sensores de monitoreo, tópicos de Kafka e interacciones de base de datos. |
| **`Diagrama01.png`** | Imagen PNG | Captura preliminar del flujo de bloques y componentes analizados durante las entrevistas iniciales. |
| **`Observabilidad integral de los Sorters-20260810_140911-Grabación de la reunión.mp4`** | Video MP4 | Grabación audiovisual completa de la sesión técnica de traspaso y arquitectura con los referentes del sistema (10 de agosto de 2026). Permite auditar explicaciones puntuales y contexto técnico directo. |

---

## 🧭 Relación con la Documentación Consolidada

A partir de los archivos de esta carpeta se consolidaron los documentos estructurados y diagramas interactivos:

- **Portal Principal:** [`Sorter.html`](../Sorter.html) (Home page con navegación completa).
- **Arquitectura:** [`docs/01-arquitectura-general.md`](../docs/01-arquitectura-general.md).
- **Flujo Vertical Sorter:** [`docs/02-flujo-end-to-end-vertical.md`](../docs/02-flujo-end-to-end-vertical.md).
- **Catálogo de Componentes:** [`docs/03-inventario-componentes.md`](../docs/03-inventario-componentes.md).
- **Estrategia de Observabilidad:** [`docs/04-estrategia-observabilidad.md`](../docs/04-estrategia-observabilidad.md).
- **Diagrama E2E:** [`docs/diagrama-flujo-observabilidad.md`](../docs/diagrama-flujo-observabilidad.md).
