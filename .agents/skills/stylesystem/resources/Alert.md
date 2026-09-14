# Alert

**Import:** `import { Alert } from "@architecture-it/stylesystem";`  
**Type:** `import type { AlertProps } from "@architecture-it/stylesystem";`

Collapsible alert/notification bar. Uses MUI `Alert` inside a `Collapse` for animated show/hide. Supports icons, links, action buttons, and a cookie banner layout.

## Props

Extends MUI `AlertProps`:

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `open` | `boolean` | ✅ | Controls visibility via `Collapse` animation |
| `onCloseProp` | `() => void` | ✅ | Called when the close (×) button is clicked |
| `color` | `"success" \| "error" \| "info" \| "warning"` | | Alert color theme |
| `variant` | `"outlined" \| "standard"` | | MUI variant |
| `icon` | `ReactNode` | | Custom icon element. If omitted, no icon is shown |
| `title` | `string` | | Bold heading above children |
| `button` | `{ text: string, href?: string, onClick?: () => void }` | | Renders an outlined `Button` inside the alert |
| `info` | `{ text: string, href?: string, onClick?: () => void }` | | Renders a `Link` inside the alert |
| `intent` | `"default" \| "information"` | | `"information"` = simpler info blue style (no icon) |
| `children` | `ReactNode` | | Alert message body |

## Usage Examples

### Success (outlined)

```tsx
const [open, setOpen] = React.useState(true);

<Alert
  color="success"
  variant="outlined"
  open={open}
  onCloseProp={() => setOpen(false)}
  icon={<CheckCircleIcon primaryColor="var(--secondary-green)" />}
>
  <Typography component="h2" fontSize="var(--body-3)">
    Tu mensaje fue <strong>enviado con éxito, </strong>pronto nos comunicaremos. ¡Muchas Gracias!
  </Typography>
</Alert>
```

### Error (outlined)

```tsx
<Alert
  color="error"
  variant="outlined"
  open={open}
  onCloseProp={() => setOpen(false)}
  icon={<TimesIcon primaryColor="var(--primary)" />}
>
  <Typography component="h2" fontSize="var(--body-3)">
    Tu mensaje <strong>no </strong>pudo ser enviado.
  </Typography>
</Alert>
```

### Info with title and action button

```tsx
<Alert
  color="info"
  variant="standard"
  title="Información"
  open={open}
  onCloseProp={() => setOpen(false)}
  icon={<SearchIcon primaryColor="var(--primary)" />}
  button={{ text: "Entendido", onClick: () => setOpen(false) }}
>
  <Typography color="secondary" component="h2" fontSize="var(--body-3)">
    Utilizamos cookies propias y de terceros para mejorar nuestros servicios.
  </Typography>
</Alert>
```

### Cookie banner (no title, with info link + button)

```tsx
<Alert
  color="info"
  variant="standard"
  open={open}
  onCloseProp={() => setOpen(false)}
  button={{ text: "Entendido" }}
  info={{ text: "Más información", href: "/privacidad" }}
>
  <Typography color="secondary" component="h2" fontSize="var(--body-3)">
    Al navegar en este sitio aceptás las cookies que utilizamos para mejorar tu experiencia.
  </Typography>
</Alert>
```

### Simple information intent

```tsx
<Alert
  color="info"
  variant="outlined"
  intent="information"
  open={open}
  onCloseProp={() => setOpen(false)}
  icon={<SearchIcon primaryColor="var(--c-color-border-info)" />}
>
  <Typography component="h2" fontSize="var(--body-3)">
    <strong>Mensaje informativo simple </strong><br />
    ¡No te vayas! Olvidaste algo en tu carrito
  </Typography>
</Alert>
```

### Text only (no icon)

```tsx
<Alert
  color="success"
  variant="standard"
  open={open}
  onCloseProp={() => setOpen(false)}
>
  <Typography variant="subtitle2">Tu mensaje fue enviado con éxito.</Typography>
</Alert>
```

## Managing Open State

The typical pattern is to use local state or the `useToggle` hook:

```tsx
const [open, setOpen] = React.useState(true);

// Or with Storybook-style updates:
const [, updateArgs] = useArgs();
const handleClose = () => updateArgs({ open: false });
```

With Redux:

```tsx
import { useDispatch } from "react-redux";
import { hide } from "./alertSlice";

<Alert
  open={open}
  onCloseProp={() => dispatch(hide())}
  color="success"
  ...
>
  {message}
</Alert>
```

## Notes

- The close button (×) at the top-right is always present; it calls `onCloseProp`.
- Pass `icon={false}` explicitly to get the color-bar-only layout without any icon.
- Do not pass icon when `color="info"` with a title — the title block has its own icon positioning.
- `intent="information"` changes CSS classes in the internal class map.
