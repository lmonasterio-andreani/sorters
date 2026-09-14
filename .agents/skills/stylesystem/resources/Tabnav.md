# Tabnav

**Import:** `import { Tabnav } from "@architecture-it/stylesystem";`  
**Type:** `import type { TabnavProps } from "@architecture-it/stylesystem";`

Tab navigation component based on MUI `Tabs` + `Tab`. Renders a list of tabs with associated panels. Supports both controlled and uncontrolled modes, and an optional icon.

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `data` | `TabAndPanel[]` | ✅ | Tab + panel definitions |
| `value` | `number` | | **Controlled mode:** active tab index |
| `onChange` | `(event, value: number) => void` | | Controlled change handler |
| `onClick` | `(value: number) => void` | | Additional click callback |
| `icon` | `ReactElement` | | Icon shown in all tab labels |
| `classes` | `{ root?, tabs?, tab?, panel? }` | | CSS slot overrides |

### `TabAndPanel` shape

```ts
interface TabAndPanel {
  label: string;          // Tab label text
  panel: ReactNode;       // Panel content rendered when tab is active
  disabled?: boolean;     // Disables this individual tab
  icon?: ReactElement;    // Per-tab icon (overrides shared icon prop)
}
```

## Usage Examples

### Basic (uncontrolled)

```tsx
import { Tabnav } from "@architecture-it/stylesystem";

<Tabnav
  data={[
    { label: "Envíos", panel: <EnviosPanel /> },
    { label: "Seguimiento", panel: <SeguimientoPanel /> },
    { label: "Reportes", panel: <ReportesPanel /> },
  ]}
/>
```

### Controlled mode

```tsx
const [tab, setTab] = React.useState(0);

<Tabnav
  value={tab}
  onChange={(_, newValue) => setTab(newValue)}
  data={[
    { label: "Resumen", panel: <ResumenTab /> },
    { label: "Detalle", panel: <DetalleTab /> },
    { label: "Historial", panel: <HistorialTab /> },
  ]}
/>
```

### Controlled + navigate on click

```tsx
const navigate = useNavigate();
const location = useLocation();
const tabs = ["/inicio", "/envios", "/reportes"];
const tab = tabs.indexOf(location.pathname);

<Tabnav
  value={tab === -1 ? 0 : tab}
  onChange={(_, i) => navigate(tabs[i])}
  data={[
    { label: "Inicio", panel: null },
    { label: "Envíos", panel: null },
    { label: "Reportes", panel: null },
  ]}
/>
```

### With shared icon

```tsx
<Tabnav
  icon={<InfoIcon />}
  data={[
    { label: "Información", panel: <InfoPanel /> },
    { label: "Contacto", panel: <ContactoPanel /> },
  ]}
/>
```

### With per-tab icons and disabled tab

```tsx
<Tabnav
  data={[
    { label: "Activos", icon: <CheckCircleIcon />, panel: <ActiveList /> },
    { label: "Pendientes", icon: <ClockIcon />, panel: <PendingList /> },
    { label: "Archivados", icon: <FolderIcon />, panel: <ArchivedList />, disabled: true },
  ]}
/>
```

## Notes

- If `value` and `onChange` are not provided, the component manages its own active state (uncontrolled).
- Tab panels are rendered conditionally based on the active index.
- `Tabnav` wraps `Tabs` with `variant="scrollable"` `scrollButtons="auto"` on smaller screens.
- Do not mix `icon` (global) with per-item `icon` — per-item overrides global.
