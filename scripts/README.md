# 🛠️ Scripts y Herramientas de Automatización

Este directorio centraliza todos los scripts de soporte operativo y sincronización del portal de **Sorters Andreani**.

---

## 📋 Catálogo de Scripts

| Script | Lenguaje / Tipo | Finalidad | Modo de Uso |
| :--- | :--- | :--- | :--- |
| [**`preview.bat`**](./preview.bat) | Batch (`.bat`) | Inicia un servidor web local en `http://localhost:3000` y abre el navegador automáticamente. | Doble clic o `.\scripts\preview.bat` |
| [**`push.bat`**](./push.bat) | Batch (`.bat`) | Empuja commits pendientes en simultáneo a los dos repositorios de GitHub (`infrastructure-services` y `lmonasterio-andreani`). | Doble clic o `.\scripts\push.bat` |
| [**`sync.bat`**](./sync.bat) | Batch (`.bat`) | Acceso rápido de 1 clic para ejecutar la sincronización de aplicaciones SPP desde la última exportación de GitOps. | Doble clic o `.\scripts\sync.bat` |
| [**`sync-gitops.py`**](./sync-gitops.py) | Python 3 | Motor inteligente de sincronización con la plataforma **GitOps Andreani** (vía API REST o exportación Excel). | Ver detalle abajo |

---

## ⚙️ Uso Avanzado: `sync-gitops.py`

### 1. Sincronización Automática por Archivo (Offline)
Toma automáticamente la exportación más reciente de la plataforma GitOps ubicada en `relevamiento/planillas/` y regenera la documentación:
```powershell
python scripts/sync-gitops.py
```

### 2. Sincronización en Vivo vía API REST
Si dispones de un token Bearer de sesión corporativo:
```powershell
python scripts/sync-gitops.py --token "<tu-bearer-token>"
```

### 📦 Archivos generados / actualizados automáticamente:
- `docs/06-ecosistema-spp.md`: Catálogo en Markdown con diseño Cartesian, métricas y enlaces a GitHub.
- `docs/assets/spp-apps.json`: Base de datos estructurada en JSON con todas las aplicaciones y metadatos.
