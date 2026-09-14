# Toast

**Import:** `import { Toast } from "@architecture-it/stylesystem";`  
**Type:** `import type { ToastProps } from "@architecture-it/stylesystem";`

A self-contained dismissible notification. Manages its own open/closed state internally — no external state management needed. Uses `Collapse` for animation and renders a styled MUI `Alert` with `variant="filled"`.

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `message` | `string` | — | **Required.** Notification text |
| `severity` | `"success" \| "info" \| "warning" \| "error"` | `"info"` | Color scheme |
| `emphasis` | `"high" \| "normal"` | `"high"` | `"high"` = strong filled, `"normal"` = softer fill |

## Variants by severity

| Severity | High | Normal |
|----------|------|--------|
| `success` | Green filled | Light green |
| `info` | Blue filled | Light blue |
| `warning` | Yellow filled | Light yellow (close icon is dark) |
| `error` | Red filled | Light red |

> Note: For `warning` or `emphasis="normal"`, the close icon uses `var(--c-color-icon-subtle)` (dark). Otherwise it uses `var(--c-color-icon-neutral-inverse)` (light/white).

## Usage Examples

### All severity types

```tsx
<Toast message="Esta es una alerta de éxito." severity="success" />
<Toast message="Esta es una alerta de error." severity="error" />
<Toast message="Esta es una advertencia." severity="warning" />
<Toast message="Esta es información." severity="info" />
```

### Emphasis variations

```tsx
// High emphasis (default — strongly filled)
<Toast message="Operación exitosa." severity="success" emphasis="high" />

// Normal emphasis (softer, background is lighter)
<Toast message="Nota informativa." severity="info" emphasis="normal" />
```

### Conditionally rendered (mount/unmount pattern)

Because `Toast` manages its own open state, mount-based rendering is common:

```tsx
const [showToast, setShowToast] = React.useState(false);

// Trigger
<Button text="Guardar" variant="contained" onClick={handleSave} />

// Conditionally rendered toast
{showToast && <Toast message="Guardado con éxito." severity="success" />}
```

> Once dismissed, the component collapses via animation. If you need to re-show it, unmount and remount the component (set `showToast` to `false` then `true`).

### In a notification system

```tsx
const notifications = [
  { id: 1, message: "Envío procesado.", severity: "success" as const },
  { id: 2, message: "Error al procesar.", severity: "error" as const },
];

{notifications.map((notif) => (
  <Toast key={notif.id} message={notif.message} severity={notif.severity} />
))}
```

## Notes

- Toast is **self-closing** — the user clicks ✕ and it disappears. You cannot force-close it from outside.
- To re-show a dismissed toast, unmount and remount the component.
- `Toast` is distinct from `Alert` — `Alert` requires external `open` state, `Toast` manages its own.
- Do not use both `Alert` and `Toast` for the same notification — choose one based on whether you need external control.
