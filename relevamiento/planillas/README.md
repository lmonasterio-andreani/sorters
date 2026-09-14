# 📊 Relevamiento: Planillas y Tomas de Servicio

Esta sección resguarda las planillas de cálculo, matrices técnicas y relevamientos de inventario provistos por los equipos de desarrollo e infraestructura para el ecosistema de Sorters.

---

## 📂 Archivos en esta Sección

| Archivo | Tipo | Tamaño | Descripción |
| :--- | :---: | :---: | :--- |
| [**`Toma_de_Servicio - Sorters.xlsx`**](./Toma_de_Servicio%20-%20Sorters.xlsx) | Excel (XLSX) | ~32 KB | **Matriz integral de toma de servicio.** Planilla técnica oficial con el relevamiento pormenorizado de componentes, clusters, namespaces, repositorios Git, dependencias de red e inventario de PCs industriales de clasificación. |

---

## 📑 Estructura y Contenido de la Planilla

La matriz maestra `Toma_de_Servicio - Sorters.xlsx` se organiza en las siguientes dimensiones técnicas:

1. **Microservicios y Workers:**
   - Detalle de más de 50 servicios en Kubernetes (clústeres CCE, AKS-BR, K3H y K3S).
   - Namespaces operados: `TYD-SPP` (lógica de negocio y procesamiento) y `TYD-SORTERS` (clasificadores de paquetería).
   - Enlaces directos a los repositorios de Azure DevOps y pipelines de CI/CD.
2. **Mensajería Apache Kafka:**
   - Tópicos de ingesta de envíos (`orden-envio-solicitada`, `orden-envio-creada`).
   - Tópicos de SPP (`spp.alta-envio`, `spp.asignacion-custodia`, `spp.cambio-destino`).
   - Tópicos de balanza y consolidación (`bulto-informado`, `bulto-pesado-y-medido`, `apto-para-consolidar`).
3. **Bases de Datos y Caching:**
   - Instancias Microsoft SQL Server AlwaysOn (`DBSORTER` e `Integración Vertical`).
   - Instancia Redis (`DBSORTERPROD`) para offset y cursores de lectura.
4. **Hardware Industrial y PCs en Planta:**
   - Relevamiento de 20 puestos de Sorters a lo largo del país (CIT, Córdoba, Bariloche, Tucumán, CTC, Pacheco, Avellaneda, Mendoza, Salta, etc.).
   - Direcciones IP estáticas y asignación en dominio corporativo.

---

## 🔗 Consolidación en la Documentación Oficial

El contenido de esta planilla se encuentra normalizado y documentado en:
- [**`docs/03-inventario-componentes.md`**](../../docs/03-inventario-componentes.md): Catálogo completo estructurado en tablas Markdown.
