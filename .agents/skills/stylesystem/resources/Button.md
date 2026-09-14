# Button

**Import:** `import { Button } from "@architecture-it/stylesystem";`  
**Type:** `import type { ButtonProps } from "@architecture-it/stylesystem";`

Wraps MUI `Button` with Andreani styles. Ripple effects are disabled by default. The label is always rendered via an inner `<Typography>` component.

## Props

| Prop | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| `text` | `string` | — | ✅ | Button label text |
| `variant` | `"contained" \| "outlined" \| "text"` | — | | Visual style |
| `icon` | `ReactNode` | — | | Sets MUI `startIcon`. Use library icons or FontAwesome |
| `link` | `boolean` | `false` | | Renders as a link-style text button; ignores `variant` |
| `typographyProps` | `TypographyProps` | `{ variant: "subtitle2" }` | | Forwarded to inner `<Typography>` |
| `color` | `"primary" \| "secondary" \| ...` | — | | MUI color token |
| `size` | `"small" \| "medium" \| "large"` | `"medium"` | | Button size |
| `disabled` | `boolean` | `false` | | Disabled state |
| `href` | `string` | — | | Turns button into an `<a>` |
| `type` | `"button" \| "submit" \| "reset"` | `"button"` | | HTML type |
| `onClick` | `() => void` | — | | Click handler |
| `fullWidth` | `boolean` | `false` | | 100% container width |
| `className` | `string` | — | | Extra CSS class |
| `sx` | `SxProps` | — | | MUI sx prop |
| `startIcon` | `ReactNode` | — | | MUI native startIcon (use `icon` instead — it maps to this) |
| `endIcon` | `ReactNode` | — | | MUI native endIcon |

## Variants

- **Contained** (`variant="contained"`) — Primary action, solid background
- **Outlined** (`variant="outlined"`) — Secondary action, border only
- **Text** (`variant="text"`) — Tertiary/back action, no border
- **Link** (`link={true}`) — Styled as inline link text

## Usage Examples

### Basic variants

```tsx
// Primary contained
<Button text="Buscar envíos" variant="contained" color="primary" />

// Secondary outlined
<Button text="Cancelar" variant="outlined" color="primary" />

// Tertiary text
<Button text="Atrás" variant="text" />
```

### With icon

```tsx
import { SearchIcon, ArrowLeftIcon, SpinnerThirdIcon } from "@architecture-it/stylesystem";

// Contained with icon
<Button
  text="Buscar envíos"
  variant="contained"
  icon={<SearchIcon primaryColor="var(--gray-000)" />}
/>

// Text with back arrow
<Button
  text="Atrás"
  variant="text"
  icon={<ArrowLeftIcon height={16} width={16} primaryColor="var(--primary)" />}
/>

// Loading state
<Button
  text="Procesando"
  variant="contained"
  disabled
  icon={
    <SpinnerThirdIcon
      spin
      height={16}
      width={16}
      primaryColor="var(--shadow-secondary)"
      secondaryColor="var(--secondary)"
    />
  }
/>
```

### Link button

```tsx
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faLink } from "@fortawesome/free-solid-svg-icons";

<Button
  text="Ver más"
  link
  href="https://www.andreani.com/?tab=seguir-envio"
  icon={<FontAwesomeIcon icon={faLink} />}
/>
```

### In a form

```tsx
<form onSubmit={handleSubmit(onSubmit)}>
  <Input label="Nombre" {...register("name")} />
  <Button text="Enviar" type="submit" variant="contained" color="primary" />
</form>
```

### Full width

```tsx
<Button text="Ingresar o crear cuenta" variant="outlined" color="primary" fullWidth />
```

### Small size (in table/chips context)

```tsx
<Button text="submit" size="small" type="submit" variant="contained" />
```

## CSS Variables Used

- `var(--gray-000)` — white icon on contained button
- `var(--primary)` — primary brand color
- `var(--secondary)` — secondary brand color
- `var(--shadow-secondary)` — for loading spinners

## Common Mistakes

- ❌ Don't use `children` — the Button ignores children. Always use `text` prop.
- ❌ Don't pass `startIcon` directly — use `icon` prop instead (it maps internally).
- ✅ When doing loading, combine `disabled` + `icon` with a spinning `SpinnerThirdIcon`.
- ✅ For link navigation, prefer `link` + `href` over `variant="text"` + `onClick`.
