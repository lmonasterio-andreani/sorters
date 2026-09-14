# Modal

**Import:** `import { Modal } from "@architecture-it/stylesystem";`  
**Type:** `import type { ModalProps } from "@architecture-it/stylesystem";`

Dialog component based on MUI `Dialog`. Has a fixed close button (×) at the top. Supports illustrations, scrollable content, and up to 3 action buttons.

## Props

Extends MUI `DialogProps` (omits `fullWidth`, `fullScreen`, `maxWidth`, `classes`, `content`):

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `open` | `boolean` | ✅ | Controls dialog visibility |
| `handleClose` | `() => void` | ✅ | Called when × is clicked or backdrop is clicked |
| `title` | `string` | ✅ | Dialog title text |
| `subtitle` | `string` | | Secondary text below title |
| `content` | `ReactNode` | | Scrollable body (`DialogContent`) |
| `buttons` | `[ReactNode, ReactNode?, ReactNode?]` | | 1–3 action buttons (first = primary) |
| `imgProps` | `img props \| { icon: () => JSX.Element }` | | Illustration above title. Pass `{ icon: () => <MyIcon /> }` for a ReactElement |
| `disableCloseOnBackdrop` | `boolean` | | Prevents `handleClose` on backdrop click |
| `PaperProps` | `PaperProps` | | Forwarded to the Dialog paper |
| `classes` | `{ dialogTitle?, dialogsubTitle?, modalHeader?, modalPaper?, modalContent?, actions? }` | | CSS slot overrides |

## Usage Examples

### Basic modal (title + subtitle + buttons)

```tsx
import { useToggle } from "@architecture-it/stylesystem";

const [open, { handleOpen, handleClose }] = useToggle();

<Button text="Abrir Modal" variant="contained" onClick={handleOpen} />

<Modal
  open={open}
  handleClose={handleClose}
  title="Título de modal"
  subtitle="Utilizamos cookies propias y de terceros para mejorar nuestros servicios."
  buttons={[
    <Button key="2" text="Acción 2" variant="outlined" size="medium" sx={{ maxWidth: "fit-content" }} />,
    <Button key="1" text="Acción 1" variant="contained" size="medium" sx={{ maxWidth: "fit-content" }} />,
  ]}
/>
```

### Warning modal with icon

```tsx
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faExclamationCircle } from "@fortawesome/pro-regular-svg-icons";

<Modal
  open={open}
  handleClose={handleClose}
  title="Título de modal"
  subtitle="Mensaje de advertencia."
  imgProps={{
    icon: () => <FontAwesomeIcon icon={faExclamationCircle} size="3x" className={styles.modalIcon} />,
  }}
  buttons={[
    <Button key="2" text="Cancelar" variant="outlined" />,
    <Button key="1" text="Confirmar" variant="contained" />,
  ]}
/>
```

### Modal with image illustration

```tsx
<Modal
  open={open}
  handleClose={handleClose}
  title="Sustentabilidad"
  imgProps={{
    src: "https://example.com/icon.svg",
    alt: "sustentabilidad-image",
    height: 80,
    width: 80,
    className: styles.modalImg,
  }}
  buttons={[
    <Button key="1" text="Más información" variant="outlined" />,
    <Button key="2" text="Entendido" variant="contained" />,
  ]}
/>
```

### Modal with scrollable content

```tsx
<Modal
  open={open}
  handleClose={handleClose}
  title="Artículos prohibidos"
  imgProps={{ src: "/icon.svg", alt: "icon", height: 80, width: 80 }}
  content={
    <>
      {items.map((item, i) => (
        <Box key={i} display="flex" alignItems="center">
          <TimesIcon color="primary" />
          <Typography color="secondary" fontSize="14px" paddingLeft="var(--spacing-2)">
            {item.description}
          </Typography>
        </Box>
      ))}
      <Typography color="#616161" component="i" marginTop="var(--spacing-4)" variant="body2">
        Nota adicional...
      </Typography>
    </>
  }
  buttons={[<Button key="1" text="Cerrar" variant="outlined" />]}
/>
```

### Disable backdrop close

```tsx
<Modal
  open={open}
  handleClose={handleClose}
  title="Confirmación requerida"
  disableCloseOnBackdrop
  buttons={[
    <Button key="no" text="No" variant="outlined" onClick={handleClose} />,
    <Button key="yes" text="Sí, confirmar" variant="contained" onClick={handleConfirm} />,
  ]}
/>
```

## Button Placement Rules

- `buttons` is a **tuple** of 1–3 elements.
- Buttons render in the `DialogActions` section at the bottom.
- Typical layout: `[secondary button, primary button]` — the first item is always on the left.
- All buttons inside `buttons` should have `sx={{ maxWidth: "fit-content" }}` for proper sizing.

## Notes

- There is always a close `×` button in the top-right corner; it calls `handleClose`.
- `content` renders inside `DialogContent` which has `scroll="paper"`, enabling vertical scrolling on long content.
- `subtitle` renders as `DialogContentText` (gray text).
- Pass `imgProps` as `{ icon: () => <MyElement /> }` for non-`<img>` illustrations.
