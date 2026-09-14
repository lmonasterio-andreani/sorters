# 🎙️ Relevamiento: Reuniones Técnicas y Minutas

Esta sección resguarda el registro documental y audiovisual de las sesiones de relevamiento realizadas con los referentes de arquitectura, desarrollo y operaciones de Andreani.

---

## 📅 Sesión Principal: Traspaso de Arquitectura y Observabilidad Sorters

- **Fecha:** 10 de Agosto de 2026 (14:09 hs)
- **Objetivo:** Traspaso integral de la arquitectura del ecosistema de Sorters, identificación de dependencias de SPP, diseño del circuito de resiliencia de Rampa 6, esquemas de replicación AlwaysOn y acuerdos de instrumentación de observabilidad.
- **Participantes Relevados:** Referentes de Arquitectura, Líder Técnico de SPP/Sorters, Operaciones CIT y Equipo de Observabilidad.

---

## 📂 Archivos en esta Sección

| Archivo | Tipo | Tamaño | Descripción |
| :--- | :---: | :---: | :--- |
| [**`Observabilidad integral de los Sorters 01.docx`**](./Observabilidad%20integral%20de%20los%20Sorters%2001.docx) | Word (DOCX) | ~3.7 MB | **Minuta técnica detallada.** Contiene transcripción de definiciones operativas, rol del middleware SPP, detalle de latencias en enriquecimiento (NDD/Geo), funcionamiento de Rampa 6, criticidad de la réplica de lectura de `DBSORTER` y matriz de criticidad. |
| **`Observabilidad integral de los Sorters-20260810_140911-Grabación de la reunión.mp4`** | Video (MP4) | ~279 MB | **Grabación audiovisual completa de la sesión.** Permite auditar en detalle explicaciones sobre el terreno, consultas sobre la caja negra de proveedores (Optisoft) y demostraciones en vivo. *(Nota: Excluido de Git por peso).* |

---

## 📌 Principales Conclusiones de la Sesión

1. **Prioridad Vertical Sorter:** Se definió que el clasificador del 1° Piso de CIT es el caso testigo y prioritario por combinar microservicios en Kubernetes, eventos Kafka, bases AlwaysOn, Redis y software de terceros.
2. **Riesgo "Tablero en Cero":** Si el componente `verticaltoSpp-publisher` falla, la máquina sigue clasificando pero los tableros quedan en 0 bultos/hora. Debe catalogarse como alerta **P1 Crítica**.
3. **Mecanismo de Resiliencia Rampa 6:** Los bultos sin datos en la base local son derivados a Rampa 6; el job `job-spptovertical` los reinyecta desde `DBSORTER` para permitir su reclasificación exitosa en la segunda inducción.
4. **Réplica de Lectura AlwaysOn:** El frontend `spp-dashboard-ui` y las APIs de consulta dependen exclusivamente de la réplica de lectura de `DBSORTER`. Una desincronización deja ciega a la planta.
