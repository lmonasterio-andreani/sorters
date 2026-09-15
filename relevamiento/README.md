# 📁 Material de Relevamiento - Ecosistema Sorters

Esta carpeta centraliza todos los **documentos de trabajo, minutas, planillas, diagramas de diseño y grabaciones audiovisuales** recopilados durante las sesiones técnicas de relevamiento con los distintos equipos de Andreani (Arquitectura, Desarrollo SPP, Operaciones CIT, Infraestructura y Soporte).

Sirve como la **fuente de verdad histórica** y repositorio de evidencias a partir del cual se estructuró la documentación técnica oficial disponible en el portal [**`index.html`**](../index.html) y en la carpeta [**`docs/`**](../docs/).

---

## 🧭 Secciones de Relevamiento

El material se encuentra organizado por tipología de contenido:

```text
relevamiento/
├── reuniones/     # 🎙️ Minutas de reuniones y grabaciones de audio/video
├── diagramas/     # 📐 Diagramas preliminares y fuentes de diagramación (Draw.io)
└── planillas/     # 📊 Matrices maestras de toma de servicio e inventario (Excel)
```

---

### 1. 🎙️ [Reuniones Técnicas y Minutas](./reuniones/README.md)

Documentación testimonial y minutas detalladas de los encuentros con referentes del negocio:
- [**`reuniones/Observabilidad integral de los Sorters 01.docx`**](./reuniones/Observabilidad%20integral%20de%20los%20Sorters%2001.docx): Minuta técnica con la descripción funcional de SPP, Rampa 6, AlwaysOn y acuerdos de monitoreo.
- **`reuniones/Observabilidad integral de los Sorters-20260810_140911-Grabación de la reunión.mp4`**: Grabación audiovisual completa de la sesión técnica de traspaso (10 de agosto de 2026).

Más información en: [**Ver sección Reuniones**](./reuniones/README.md)

---

### 2. 📐 [Diagramas Preliminares y Fuentes](./diagramas/README.md)

Esquemas de trabajo y archivos de diseño gráfico preliminares:
- [**`diagramas/mapa de monitoreo sorter.drawio`**](./diagramas/mapa%20de%20monitoreo%20sorter.drawio): Archivo fuente editable en Draw.io con el modelado inicial de sensores y flujos.
- [**`diagramas/Diagrama01.png`**](./diagramas/Diagrama01.png): Esquema preliminar analizado durante las sesiones de trabajo.

Más información en: [**Ver sección Diagramas de Relevamiento**](./diagramas/README.md)

---

### 3. 📊 [Planillas y Tomas de Servicio](./planillas/README.md)

Matrices de inventario y relevamiento exhaustivo de infraestructura:
- [**`planillas/Toma_de_Servicio - Sorters.xlsx`**](./planillas/Toma_de_Servicio%20-%20Sorters.xlsx): Matriz consolidada de más de 50 microservicios, tópicos Kafka, bases SQL AlwaysOn, Redis e inventario de 20 PCs industriales de Sorters.

Más información en: [**Ver sección Planillas**](./planillas/README.md)

---

## 🔗 Relación con la Documentación Oficial Consolidada

Todo el material en bruto de esta carpeta ha sido normalizado y sintetizado en la documentación técnica del proyecto:

| Sección de Relevamiento | Documento Oficial Consolidado en `docs/` |
| :--- | :--- |
| **Minuta de Reunión** (`reuniones/`) | [**`docs/01-arquitectura-general.md`**](../docs/01-arquitectura-general.md) y [**`docs/02-flujo-end-to-end-vertical.md`**](../docs/02-flujo-end-to-end-vertical.md) |
| **Planilla Toma de Servicio** (`planillas/`) | [**`docs/03-inventario-componentes.md`**](../docs/03-inventario-componentes.md) |
| **Estrategia y Acuerdos de Monitoreo** | [**`docs/04-estrategia-observabilidad.md`**](../docs/04-estrategia-observabilidad.md) |
| **Diagrama Fuente Draw.io** (`diagramas/`) | [**`docs/05-flujo-observabilidad.md`**](../docs/05-flujo-observabilidad.md) y [**`docs/diagramas/`**](../docs/diagramas/) |
| **Identidad Visual Corporativa (Interna)** | [**`docs/guia-estilos-cartesian.md`**](../docs/guia-estilos-cartesian.md) |
| **Portal Unificado Interactivo** | [**`index.html`**](../index.html) |
