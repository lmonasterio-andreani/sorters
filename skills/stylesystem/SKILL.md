---
name: stylesystem
description: Expert guide for the @architecture-it/stylesystem React component library (v7+). Covers installation, setup, all components with TypeScript props, usage examples, icons, hooks, utilities, multi-brand theming, dark mode, and migration from v1/v2.
---

# @architecture-it/stylesystem — Developer Skill Guide

This document is the authoritative reference for developers using `@architecture-it/stylesystem`. Read it when you need to:
- Implement any component from the library
- Set up the provider / theme correctly
- Handle multi-brand theming or dark mode
- Use icons, hooks, or utilities from the library
- Migrate from older versions (v1 → v2 → v3+)

---

## Table of Contents

1. [Installation & Peer Dependencies](#installation--peer-dependencies)
2. [Provider Setup (REQUIRED)](#provider-setup-required)
3. [Multi-Brand Theming](#multi-brand-theming)
4. [Dark Mode](#dark-mode)
5. [Icons](#icons)
6. [Hooks — `useToggle`](#hooks--usetoggle)
7. [Utilities](#utilities)
8. [Components Reference](#components-reference)
   - [Primary/Form Components](#primaryform-components)
     - [Button](#button)
     - [Input](#input)
     - [Select](#select)
     - [Checkbox](#checkbox)
     - [Radio](#radio)
     - [Switch](#switch)
     - [Search](#search)
     - [Pills](#pills)
     - [InputQuantity](#inputquantity)
     - [ListControl](#listcontrol)
   - [Feedback Components](#feedback-components)
     - [Alert](#alert)
     - [Toast](#toast)
     - [Loading](#loading)
     - [Tooltip](#tooltip)
   - [Navigation & Layout](#navigation--layout)
     - [Header](#header)
     - [Footer](#footer)
     - [Sidebar](#sidebar)
     - [SidebarItem](#sidebaritem)
     - [SidebarAvatar](#sidebaravatar)
     - [SidebarMini](#sidebarmini)
     - [BreadCrumb](#breadcrumb)
     - [Tabnav](#tabnav)
     - [NavbarItem](#navbaritem)
   - [Cards](#cards)
     - [Card](#card)
     - [CardButton](#cardbutton)
     - [Skeletons](#skeletons)
   - [Data Display](#data-display)
     - [Table / TableHead / TableRow / TableFooter / TablePagination](#table-components)
     - [DescriptionItem](#descriptionitem)
     - [ListItem](#listitem)
     - [ListTexts](#listtexts)
   - [Steps Components](#steps-components)
     - [HorizontalSteps](#horizontalsteps)
     - [VerticalSteps](#verticalsteps)
     - [InfoSteps](#infosteps)
   - [Overlay & Dialogs](#overlay--dialogs)
     - [Modal](#modal)
     - [CustomPopover](#custompopover)
   - [AutoComplete & Dropdown](#autocomplete--dropdown)
     - [AutoComplete](#autocomplete)
     - [Dropdown](#dropdown)
   - [Interactive](#interactive)
     - [ButtonMob](#buttonmob)
     - [FabButton](#fabbutton)
     - [IconButton](#iconbutton)
     - [LikeDislike](#likedislike)
     - [BaseChip](#basechip)
   - [Miscellaneous](#miscellaneous)
     - [Miscellaneous (decorative)](#miscellaneous-decorative)
     - [SocialMedia](#socialmedia)
     - [Speaker](#speaker)
     - [Logos](#logos)
     - [CustomSection](#customsection)
     - [ThemeToggle](#themetoggle)
   - [Error Handling](#error-handling)
     - [ErrorBoundary](#errorboundary)
     - [FallbackComponent](#fallbackcomponent)
   - [ServicesStatus](#servicesstatus)
9. [Full Component Index (exports)](#full-component-index-exports)
10. [Migration Guide](#migration-guide)
    - [v1 → v2](#v1--v2)
    - [v2 → v3](#v2--v3)
11. [Resources (detailed per-component files)](#resources)

---

## Installation & Peer Dependencies

```bash
pnpm add @architecture-it/stylesystem
# Required peer dependencies:
pnpm add @architecture-it/cartesian @emotion/react @emotion/styled @mui/material
```

- **Node**: >= 20
- **MUI**: >= 7.1.2
- **cartesian**: >= 7

> FontAwesome icons (`@fortawesome/*`) are **no longer required** peer dependencies since v3. You can still use them for custom icons if needed.

---

## Provider Setup (REQUIRED)

Every application using this library **must** wrap its root with `StyleSystemProvider`. It sets up:
- MUI `ThemeProvider` with the custom theme
- CSS variables from `@architecture-it/cartesian`
- CSS injection order via `StyledEngineProvider`

```tsx
import { StyleSystemProvider } from "@architecture-it/stylesystem";

// app root
function App() {
  return (
    <StyleSystemProvider defaultThemeMode="light">
      {/* your app */}
    </StyleSystemProvider>
  );
}
```

### `IStyleSystemProviderProps`

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` | — | Extra class applied to the wrapper `div` |
| `disableInjectFirst` | `boolean` | `false` | Disables `StyledEngineProvider injectFirst`. Set to `true` if you manage CSS order elsewhere |
| `defaultThemeMode` | `"light" \| "dark"` | `"light"` | Initial color scheme |

### Testing with `StyleSystemProvider`

When using `renderWithProviders` in Jest tests you may see warnings about missing theme. Fix by passing a custom theme:

```typescript
import getTheme from "@architecture-it/stylesystem/Theme";

const colors = { primary: "#d71920" };
const theme = getTheme(false, colors);
// pass to your test wrapper's ThemeProvider
```

---

## Multi-Brand Theming

The library ships three brand themes: `cds`, `hop`, and `witwot`. Apply a brand theme by adding the brand's CSS class to the wrapper element.

```tsx
import { cds, hop, witwot, StyleSystemProvider } from "@architecture-it/stylesystem";

// Wrap with the brand styles class:
  <StyleSystemProvider className={cds.styles}>
    {/* components will use CDS brand tokens */}
  </StyleSystemProvider>
```

Each theme object exposes:
- `.styles` — the CSS class name string (apply to a wrapper div)
- `.css` — the raw CSS string if you need to inject it manually

### `getImagePropsLogoByBrand` utility

Returns the correct logo `img` props for each brand: `"cds" | "hop" | "witwot" | "andreani" | undefined`.

```tsx
import { getImagePropsLogoByBrand } from "@architecture-it/stylesystem";

const logo = getImagePropsLogoByBrand("cds"); // { alt: "CDS", src: "...", style: { height: 24 } }
<Header logo={logo} />
```

---

## Dark Mode

Dark mode is controlled via MUI's `useColorScheme`. The library provides `ThemeToggle` and `useThemeMode` to manage it.

```tsx
import { ThemeToggle, useThemeMode } from "@architecture-it/stylesystem";

// Simple toggle button:
<ThemeToggle />

// Programmatic control:
const { mode, toggleMode, setMode } = useThemeMode();
```

The `data-theme-mode` attribute is set on `:root` when mode changes, so you can scope CSS based on it.

---

## Icons

Since v3, the library has its own icon set. **Do NOT use FontAwesome** as required icons; use the built-in ones instead.

### Import pattern

Icons have two flavours:
1. **Deprecated shorthand** (still works): `import { Icon as CheckCircle } from "@architecture-it/stylesystem/icons/CheckCircle"`
2. **Preferred named exports** (suffix `Icon`): `import { CheckCircleIcon } from "@architecture-it/stylesystem"`

```tsx
import {
  CheckCircleIcon,
  SearchIcon,
  ChevronDownIcon,
  ArrowLeftIcon,
  SpinnerThirdIcon,
  CloseIcon,
  TimesIcon,
  MoonIcon,
  SunIcon,
  // ... many more
} from "@architecture-it/stylesystem";
```

### Icon props

All icons accept:
| Prop | Type | Description |
|------|------|-------------|
| `primaryColor` | `string` | Main fill/stroke color (CSS variable or hex) |
| `secondaryColor` | `string` | Secondary color (used in duotone-like icons) |
| `width` | `number` | Icon width in px |
| `height` | `number` | Icon height in px |
| `spin` | `boolean` | Enables CSS rotation animation (e.g. for `SpinnerThird`) |
| `className` | `string` | Extra CSS class |
| `cursor` | `string` | CSS cursor value |

### Full exported icon list

`AngleRightIcon`, `ArrowLeftIcon`, `ArrowRightIcon`, `ArrowRightFromBracketIcon`, `ArrowRightToBracketIcon`, `BarsIcon`, `CalendarIcon`, `CheckCircleIcon`, `CheckIcon`, `ChevronDownIcon`, `ChevronLeftIcon`, `ChevronRightIcon`, `ChevronUpIcon`, `CircleXmarkIcon`, `CloseIcon`, `CopyIcon`, `CssIcon`, `EditIcon`, `EnvelopeIcon`, `FacebookIcon`, `HouseIcon`, `InstagramIcon`, `JsIcon`, `LinkedinIcon`, `LockIcon`, `MoonIcon`, `QuestionCircleIcon`, `SearchIcon`, `SpinnerThirdIcon`, `SunIcon`, `ThumbsDownIcon`, `ThumbsUpIcon`, `TimesIcon`, `TwitterIcon`, `UserCircleIcon`, `UserIcon`, `YoutubeIcon`

> For icons not in the list, use FontAwesome manually: `import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"`.

---

## Hooks — `useToggle`

```tsx
import { useToggle } from "@architecture-it/stylesystem";

const [open, { toggle, handleOpen, handleClose }] = useToggle(false);
// toggle()      — flip open/closed
// handleOpen()  — set true
// handleClose() — set false
```

This hook is used extensively for modals, sidebars, dropdowns, etc.

---

## Utilities

```tsx
import { joinClasses, getFormatedDate, prepareViewport, getImagePropsLogoByBrand } from "@architecture-it/stylesystem";

// Merge class names, filtering out undefined/false:
const cls = joinClasses("base", condition && "extra", undefined); // "base extra"

// Format a date:
getFormatedDate(new Date(), "-"); // "1-1-2025"

// In tests — mock matchMedia:
prepareViewport("(max-width: 768px)", true);
```

Also exported:
- `RepeatElementHOC` — HOC to repeat a child element N times
- `getRoutes(path: string)` — splits a URL path into breadcrumb segments
- `getReturnRoute(routes: string[], index: number)` — computes the back-navigation target from breadcrumbs

---

## Components Reference

> For every component: import from `@architecture-it/stylesystem` unless noted.

---

### Primary/Form Components

#### Button

```tsx
import { Button } from "@architecture-it/stylesystem";
```

**Props (`ButtonProps`):**

| Prop | Type | Description |
|------|------|-------------|
| `text` | `string` | **Required.** Button label |
| `variant` | `"contained" \| "outlined" \| "text"` | Visual style |
| `icon` | `ReactNode` | Placed in `startIcon` |
| `link` | `boolean` | Renders as a text-style link button, ignores `variant` |
| `typographyProps` | `TypographyProps` | Props forwarded to the inner `<Typography>` |
| + all MUI `ButtonProps` | | `color`, `size`, `disabled`, `href`, `type`, `onClick`, `fullWidth`, etc. |

**Examples:**

```tsx
// Contained (primary)
<Button text="Buscar envíos" variant="contained" color="primary" />

// Outlined (secondary)
<Button text="Buscar envíos" variant="outlined" color="primary" />

// Text (tertiary / back)
<Button text="Atrás" variant="text" />

// With icon
<Button
  text="Buscar envíos"
  variant="contained"
  icon={<SearchIcon primaryColor="var(--gray-000)" />}
/>

// Link style
<Button
  text="Ver más"
  link
  href="https://www.andreani.com"
  icon={<ArrowRightIcon />}
/>

// Loading state
<Button
  text="Loading"
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

---

#### Input

```tsx
import { Input } from "@architecture-it/stylesystem";
import type { InputProps } from "@architecture-it/stylesystem";
```

**Props (`InputProps`)** — extends MUI `InputBaseProps`:

| Prop | Type | Description |
|------|------|-------------|
| `label` | `string` | Field label (uses shrink `InputLabel`) |
| `helperText` | `string` | Text below the field |
| `dark` | `boolean` | Dark background variant |
| `optional` | `boolean` | Shows *(opcional)* suffix on label |
| `tooltip` | `TooltipProps (MUI)` | Tooltip icon on the label |
| `checkbox` | `{ text, checked?, onChange?, disabled? }` | Inline checkbox that disables the input when checked |
| `inputLabelProps` | `InputLabelProps` | Forwarded to the inner `InputLabel` |
| `classes` | `{ formControl?, label?, input?, helperText? }` | CSS overrides per slot |
| + all MUI `InputBaseProps` | | `value`, `onChange`, `error`, `disabled`, `required`, `multiline`, `placeholder`, `endAdornment`, `type`, `fullWidth`, `id`, etc. |

**Examples:**

```tsx
// Basic
<Input label="Nombre" />

// Required with helper text
<Input label="Nombre" required helperText="Debe ingresar un nombre" />

// With error
<Input label="Nombre" error helperText="Debe ingresar un nombre" />

// With tooltip
<Input label="Nombre" tooltip={{ title: "Ingresa tu nombre completo" }} />

// Optional field
<Input label="Nombre" optional />

// Textarea
<Input label="Comentarios" multiline fullWidth placeholder="Introduce acá tus comentarios" />

// Dark background
<Input label="Comentarios" dark />

// With end icon adornment
<Input
  placeholder="Buscar envíos"
  endAdornment={<SearchIcon />}
  classes={{ formControl: "myClass" }}
/>

// With inline checkbox (common for "sin número" address field)
<Input
  label="Dirección"
  checkbox={{ text: "Sin número" }}
  onChange={handleChange}
  value={value}
/>
```

**With React Hook Form:**

```tsx
const schema = yup.object({ name: yup.string().required("Campo requerido") });
const { register, handleSubmit, formState: { errors } } = useForm({ resolver: yupResolver(schema) });

<Input
  label="Nombre"
  {...register("name")}
  error={Boolean(errors.name)}
  helperText={errors.name?.message}
/>
```

**With Formik:**

```tsx
<Input
  label="Nombre"
  name="name"
  value={formik.values.name}
  onChange={formik.handleChange}
  error={formik.touched.name && Boolean(formik.errors.name)}
  helperText={formik.touched.name ? formik.errors.name : ""}
/>
```

---

#### Select

```tsx
import { Select } from "@architecture-it/stylesystem";
import MenuItem from "@mui/material/MenuItem";
```

**Props (`SelectProps`)** — extends MUI `SelectProps` (omits `variant`, `classes`, `size`):

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `label` | `string` | | Field label |
| `dark` | `boolean` | | Dark variant |
| `helperText` | `string` | | Text below |
| `size` | `"small" \| "large"` | | Field height |
| `display` | `"default" \| "chips" \| "checkbox"` | `"default"` | Multi-select display mode |
| `multiple` | `boolean` | | Enables multi-select |
| `inputLabelProps` | `InputLabelProps` | | Label props |
| `classes` | `{ formControl?, select? }` | | Slot overrides |
| + MUI SelectProps | | | `value`, `onChange`, `error`, `required`, `disabled`, `fullWidth`, etc. |

**Examples:**

```tsx
// Basic single select — always deselect by clicking the same item
const [value, setValue] = React.useState("");

<Select label="¿Qué querés enviar?" value={value} size="large" onChange={(e) => setValue(e.target.value as string)}>
  {["Encomienda 1", "Encomienda 2"].map((opt) => (
    <MenuItem
      key={opt}
      value={opt}
      onClick={(e) => {
        if (value === opt) { e.preventDefault(); e.stopPropagation(); setValue(""); }
      }}
    >
      {opt}
    </MenuItem>
  ))}
</Select>

// Multi-select with chips
const [value, setValue] = React.useState<string[]>([]);

<Select multiple display="chips" label="Colores" size="large" value={value} onChange={(e) => setValue(e.target.value as string[])}>
  <MenuItem value="Rojo">Rojo</MenuItem>
  <MenuItem value="Azul">Azul</MenuItem>
</Select>

// Multi-select with checkboxes
<Select multiple display="checkbox" label="Colores" size="large" value={value} onChange={(e) => setValue(e.target.value as string[])}>
  <MenuItem value="Rojo">Rojo</MenuItem>
  <MenuItem value="Azul">Azul</MenuItem>
</Select>
```

**With React Hook Form (Controller pattern):**

```tsx
<Controller
  control={control}
  name="colors"
  defaultValue=""
  render={({ field }) => (
    <Select
      label="¿Qué querés enviar?"
      value={field.value}
      onChange={(e) => {
        const toggled = e.target.value === field.value ? "" : e.target.value;
        field.onChange(toggled);
      }}
      error={Boolean(errors.colors)}
      helperText={errors.colors?.message}
      size="large"
    >
      {options.map((opt) => <MenuItem key={opt} value={opt}>{opt}</MenuItem>)}
    </Select>
  )}
/>
```

---

#### Checkbox

```tsx
import { Checkbox } from "@architecture-it/stylesystem";
import type { CheckboxProps } from "@architecture-it/stylesystem";
```

Extends MUI `CheckboxProps`. The props `disableRipple`, `disableTouchRipple`, `disableFocusRipple` are always applied and cannot be overridden.

```tsx
<Checkbox />
<Checkbox checked />
<Checkbox disabled />
<Checkbox indeterminate />

// With React Hook Form
<Checkbox {...register("myField")} />

// With Formik
<Checkbox name="options" value="andreani" onChange={formik.handleChange} />

// With label
import { FormControlLabel } from "@mui/material";
<FormControlLabel control={<Checkbox />} label="Acepto términos y condiciones" />
```

---

#### Radio

```tsx
import { Radio } from "@architecture-it/stylesystem";
```

Extends MUI `RadioProps`. Disabled props: `disableRipple`, `disableTouchRipple`, `disableFocusRipple`, `focusRipple`.

```tsx
// Standalone
<Radio />
<Radio checked />
<Radio disabled />

// In a RadioGroup (typical pattern)
import { FormControl, RadioGroup, FormControlLabel } from "@mui/material";

<FormControl>
  <RadioGroup defaultValue="opcion1" name="option">
    <FormControlLabel value="opcion1" control={<Radio />} label="Opción 1" />
    <FormControlLabel value="opcion2" control={<Radio />} label="Opción 2" />
    <FormControlLabel value="opcion3" control={<Radio />} label="Opción 3" />
  </RadioGroup>
</FormControl>

// With React Hook Form
<FormControlLabel
  control={<Radio />}
  label="Opción 1"
  value="opcion1"
  {...register("option")}
/>

// With Formik
<FormControlLabel
  control={<Radio />}
  label="Opción 1"
  name="option"
  value="option1"
  onChange={formik.handleChange}
/>
```

---

#### Switch

```tsx
import { Switch } from "@architecture-it/stylesystem";
```

Extends MUI `SwitchProps`, with extra `icon` prop:

| Prop | Type | Description |
|------|------|-------------|
| `icon` | `() => JSX.Element` | Optional icon rendered next to the switch |
| + all MUI `SwitchProps` | | `checked`, `onChange`, `disabled`, etc. |

```tsx
<Switch />
<Switch checked />
<Switch disabled />
<Switch icon={() => <LockIcon primaryColor="var(--color-text-base)" />} />

// With React Hook Form
<Switch {...register("mySwitch")} />
```

---

#### Search

```tsx
import { Search } from "@architecture-it/stylesystem";
```

**Props (`SearchProps`)** — extends MUI `InputBaseProps`:

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `size` | `"small" \| "default" \| "large"` | `"default"` | Field height |
| `variant` | `"primary" \| "secondary"` | `"primary"` | Shows a divider before the icon when `"secondary"` |
| `onClick` | `() => void` | | Called on button click and Enter key |
| `onClear` | `() => void` | | Called when input is cleared |
| `buttonId` | `string` | | `id` on the icon wrapper |

```tsx
<Search placeholder="Ingresá el número de seguimiento" fullWidth />

// Small secondary
<Search placeholder="Buscar..." size="small" variant="secondary" />

// Large
<Search size="large" placeholder="..." fullWidth onClick={handleSearch} />

// With clear callback
<Search
  placeholder="..."
  fullWidth
  onClick={handleSearch}
  onClear={() => setQuery("")}
  onChange={(e) => setQuery(e.target.value)}
/>
```

---

#### Pills

```tsx
import { Pills } from "@architecture-it/stylesystem";
```

**Props (`PillsProps`):**

| Prop | Type | Description |
|------|------|-------------|
| `text` | `string` | **Required.** Label |
| `variant` | `"info" \| "success" \| "error" \| "warning" \| "default"` | **Required.** Color scheme |
| `size` | `"large" \| "medium" \| "small"` | **Required.** Size |
| `icon` | `ReactNode` | Optional icon before text |
| `width` | `string` | Custom width override |
| `typographyProps` | `TypographyProps` | Props forwarded to inner `Typography` |

```tsx
<Pills text="Ingrese su texto" variant="info" size="large" />
<Pills text="Exito" variant="success" size="large" />
<Pills text="Error" variant="error" size="medium" />
<Pills text="Advertencia" variant="warning" size="small" />
<Pills text="Default" variant="default" size="large" />
<Pills
  text="Entregado"
  variant="success"
  size="large"
  icon={<CheckCircleIcon height={15} width={14} primaryColor="var(--c-color-text-neutral-strong)" />}
/>
```

---

#### InputQuantity

```tsx
import { InputQuantity } from "@architecture-it/stylesystem";
```

A numeric quantity selector with increment/decrement buttons.

```tsx
const [quantity, setQuantity] = React.useState(1);
<InputQuantity value={quantity} onChange={setQuantity} min={1} max={10} />
```

---

#### ListControl

```tsx
import { ListControl } from "@architecture-it/stylesystem";
import type { ListControlItem } from "@architecture-it/stylesystem";
```

A controlled list with move/remove operations.

---

### Feedback Components

#### Alert

```tsx
import { Alert } from "@architecture-it/stylesystem";
import type { AlertProps } from "@architecture-it/stylesystem";
```

**Props (`AlertProps`)** — extends MUI `AlertProps`:

| Prop | Type | Description |
|------|------|-------------|
| `open` | `boolean` | **Required.** Controls visibility via `Collapse` |
| `onCloseProp` | `() => void` | **Required.** Close handler |
| `color` | `"success" \| "error" \| "info" \| "warning"` | Alert color |
| `variant` | `"outlined" \| "standard"` | MUI variant |
| `icon` | `ReactNode` | Custom icon element (replaces default) |
| `title` | `string` | Bold title above children |
| `button` | `{ text: string, href?: string, onClick?: () => void }` | Action button |
| `info` | `{ text: string, href?: string, onClick?: () => void }` | Info link |
| `intent` | `"default" \| "information"` | `"information"` uses a simpler info style |
| `children` | `ReactNode` | Message content |

**Examples:**

```tsx
// Success
<Alert color="success" variant="outlined" open={open} onCloseProp={() => setOpen(false)}
  icon={<CheckCircleIcon primaryColor="var(--secondary-green)" />}
>
  <Typography variant="subtitle2">Tu mensaje fue enviado con éxito.</Typography>
</Alert>

// Error
<Alert color="error" variant="outlined" open={open} onCloseProp={() => setOpen(false)}
  icon={<TimesIcon primaryColor="var(--primary)" />}
>
  <Typography>Tu mensaje <strong>no</strong> pudo ser enviado.</Typography>
</Alert>

// Info with title and action button
<Alert
  color="info"
  variant="standard"
  title="Información"
  open={open}
  onCloseProp={() => setOpen(false)}
  icon={<SearchIcon primaryColor="var(--primary)" />}
  button={{ text: "Entendido", onClick: handleClose }}
>
  <Typography color="secondary">Utilizamos cookies propias y de terceros...</Typography>
</Alert>

// Cookie banner (no title, info and button links)
<Alert color="info" variant="standard" open={open} onCloseProp={() => setOpen(false)}
  button={{ text: "Entendido" }}
  info={{ text: "Más información" }}
>
  <Typography>Al navegar en este sitio aceptás las cookies...</Typography>
</Alert>

// Simple information intent (no icon, blue border)
<Alert color="info" variant="outlined" intent="information" open={open} onCloseProp={() => setOpen(false)}>
  <Typography><strong>Mensaje informativo simple</strong></Typography>
</Alert>
```

---

#### Toast

```tsx
import { Toast } from "@architecture-it/stylesystem";
import type { ToastProps } from "@architecture-it/stylesystem";
```

A self-managed dismissible notification. **No external open/close state needed.**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `message` | `string` | **Required** | Notification text |
| `severity` | `"success" \| "info" \| "warning" \| "error"` | `"info"` | Color |
| `emphasis` | `"high" \| "normal"` | `"high"` | High = filled strongly, normal = softer |

```tsx
<Toast message="Esta es una alerta de éxito." severity="success" />
<Toast message="Esta es una alerta de error." severity="error" />
<Toast message="Esta es una advertencia." severity="warning" />
<Toast message="Esta es información." severity="info" />
<Toast message="Nota suave." severity="info" emphasis="normal" />
```

---

#### Loading

```tsx
import { Loading } from "@architecture-it/stylesystem";
import type { LoadingProps } from "@architecture-it/stylesystem";
```

Full-overlay loading indicator.

| Prop | Type | Description |
|------|------|-------------|
| `text` | `string` | Text shown below the animation |
| `variant` | `"base" \| "andreani"` | `"andreani"` uses the Andreani branded GIF; `"base"` uses the spinner |
| `srcImage` | `string` | URL for a custom gif (overrides both variants) |
| `className` | `string` | Added to root overlay |

```tsx
<Loading text="Cargando..." variant="base" />
<Loading text="Subiendo info..." variant="andreani" />
<Loading text="Procesando..." srcImage="https://example.com/my-loader.gif" />
```

---

#### Tooltip

```tsx
import { Tooltip } from "@architecture-it/stylesystem";
import type { TooltipProps } from "@architecture-it/stylesystem";
```

An accessible inline tooltip. Shown on hover and focus. Associates with trigger via `aria-describedby`.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `text` | `string` | **Required** | Tooltip content |
| `variant` | `"default" \| "info" \| "error" \| "success"` | `"default"` | Color |
| `placement` | `"top" \| "bottom" \| "left" \| "right"` | `"top"` | Position |
| `id` | `string` | auto | `id` for aria-describedby |
| `children` | `ReactNode` | **Required** | The trigger element |

```tsx
<Tooltip text="Texto de información adicional." variant="default" placement="top">
  Pasa el cursor aquí
</Tooltip>

<Tooltip text="Información adicional importante." variant="info" placement="bottom">
  <Button text="Info" variant="text" />
</Tooltip>

<Tooltip text="Ha ocurrido un error." variant="error" placement="right">
  <span>Error</span>
</Tooltip>
```

---

### Navigation & Layout

#### Header

```tsx
import { Header } from "@architecture-it/stylesystem";
import type { HeaderProps } from "@architecture-it/stylesystem";
```

Top application bar based on MUI `AppBar`.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `onClickButton` | `() => void` | | Menu hamburger click handler |
| `logo` | `img HTML props` | Andreani logo | Custom logo `<img>` props |
| `position` | `"absolute" \| "fixed" \| "sticky" \| "static" \| "relative"` | `"static"` | AppBar position |
| `disableMenuButton` | `boolean` | `false` | Hides the hamburger icon |
| `moduleName` | `string` | | Shows a module name (e.g. `"DMS"`) after a title divider |
| `children` | `ReactNode` | | Right-side content (buttons, avatar, etc.) |

```tsx
// Basic with children
<Header onClickButton={handleOpenSidebar}>
  <Button text="Ingresar" variant="outlined" />
</Header>

// With breadcrumbs (inside header children)
<Header logo={logo}>
  <BreadCrumb breadCrumbs={["usuarios", "perfil"]} handleNavigate={handleNavigate} disableBackButton />
  <Button text="Ingresar" variant="outlined" />
</Header>

// With NavbarItems
<Header logo={logo}>
  <NavbarItem id="menu-servicios" text="Servicios"
    links={[{ id: "s1", title: "Logística", href: "#" }, { id: "s2", title: "Ecommerce", href: "#" }]}
  />
  <Button text="Ingresar" variant="outlined" />
</Header>

// With module name (DMS style)
<Header logo={logo} moduleName="DMS">
  <Avatar sx={{ bgcolor: "var(--c-color-fill-primary)" }}>NA</Avatar>
</Header>
```

---

#### Footer

```tsx
import { Footer } from "@architecture-it/stylesystem";
import type { FooterProps } from "@architecture-it/stylesystem";
```

Two variants: full Andreani footer and internal footer.

```tsx
// Internal (minimal)
<Footer type="internal" name="ANDREANI" />

// Institutional (with sections)
<Footer
  sections={[
    {
      title: "Personas",
      items: [
        { text: "Seguí tu envío", href: "#" },
        { text: "Sucursales", href: "#" },
      ]
    }
  ]}
/>

// Institutional with references slot
<Footer
  type="institutional"
  references={<SocialMedia media={[...]} text="" />}
  links={[
    { text: "Política de Privacidad", href: "#" },
    { text: "Términos", onClick: handleClick },
  ]}
/>
```

---

#### Sidebar

```tsx
import { Sidebar } from "@architecture-it/stylesystem";
import type { SidebarProps } from "@architecture-it/stylesystem";
```

Left swipeable drawer built on MUI `SwipeableDrawer`.

| Prop | Type | Description |
|------|------|-------------|
| `open` | `boolean` | **Required** |
| `onClose` | `() => void` | **Required** |
| `onOpen` | `() => void` | **Required** |
| `routes` | `SidebarItemProps[]` | **Required.** Array of menu items |
| `sidebarItemClassName` | `string` | Class applied to every `SidebarItem` |

```tsx
const [open, { handleOpen, handleClose }] = useToggle();

<Sidebar
  open={open}
  onClose={handleClose}
  onOpen={handleOpen}
  routes={[
    {
      item: "Inicio",
      icon: <HouseIcon />,
      selected: true,
    },
    {
      item: "Ver mis envíos",
      icon: <ArrowRightIcon />,
      href: "/envios",
    },
    {
      item: "Más opciones",
      icon: <ChevronDownIcon />,
      childrens: [
        { item: "Sustentabilidad", href: "/sustentabilidad" },
        { item: "Trabaja con nosotros", href: "/empleos" },
      ]
    },
    {
      item: <Button text="Ingresar" variant="outlined" fullWidth />,
      button: false, // disables SidebarItem wrapper behavior
    },
  ]}
/>
```

---

#### SidebarItem

```tsx
import { SidebarItem } from "@architecture-it/stylesystem";
import type { SidebarItemProps } from "@architecture-it/stylesystem";
```

Individual row inside a Sidebar (or standalone).

| Prop | Type | Description |
|------|------|-------------|
| `item` | `ReactNode \| string` | Content or label |
| `icon` | `ReactNode` | Leading icon |
| `href` | `string` | Navigation destination |
| `selected` | `boolean` | Active state highlight |
| `divider` | `boolean` | Adds a bottom divider |
| `button` | `boolean` | Whether to render as a button-like item |
| `childrens` | `BaseRoute[]` | Sub-menu items |
| `handleClick` | `() => void` | Click handler |
| `style` | `CSSProperties` | Inline styles |
| `className` | `string` | CSS class |

---

#### SidebarAvatar

```tsx
import { SidebarAvatar } from "@architecture-it/stylesystem";
import type { SidebarAvatarProps } from "@architecture-it/stylesystem";
```

User avatar header inside a Sidebar.

```tsx
<SidebarAvatar name="Pedro Perez" subtitle="Ver mi perfil" />
```

---

#### SidebarMini

```tsx
import { SidebarMini } from "@architecture-it/stylesystem";
```

A compact mini sidebar variant.

---

#### BreadCrumb

```tsx
import { BreadCrumb, getRoutes, getReturnRoute } from "@architecture-it/stylesystem";
import type { IBreadCrumbProps } from "@architecture-it/stylesystem";
```

| Prop | Type | Description |
|------|------|-------------|
| `breadCrumbs` | `string[]` | **Required.** Array of path segment names |
| `handleNavigate` | `(index: number) => void` | **Required.** Navigation callback |
| `disableBackButton` | `boolean` | Hides the "Volver" back button |

**Full implementation pattern (with React Router):**

```tsx
import { useNavigate, useLocation } from "react-router-dom";
import { BreadCrumb, getRoutes, getReturnRoute, useToggle } from "@architecture-it/stylesystem";

const Layout = ({ children }) => {
  const navigate = useNavigate();
  const { pathname } = useLocation();
  const [breadCrumbs, setBreadCrumbs] = React.useState(getRoutes(pathname));

  const handleNavigate = (index: number) => {
    const clone = [...breadCrumbs];
    const { routes, routeToNavigate } = getReturnRoute(clone, index);
    setBreadCrumbs(routes);
    navigate(routeToNavigate);
  };

  return (
    <div>
      <Header onClickButton={handleOpen} />
      <main>
        {pathname !== "/" && (
          <BreadCrumb breadCrumbs={breadCrumbs} handleNavigate={handleNavigate} />
        )}
        {children}
      </main>
    </div>
  );
};
```

---

#### Tabnav

```tsx
import { Tabnav } from "@architecture-it/stylesystem";
import type { TabnavProps, TabAndPanel } from "@architecture-it/stylesystem";
```

| Prop | Type | Description |
|------|------|-------------|
| `data` | `TabAndPanel[]` | **Required.** Each item: `{ title, content?, id?, disabled? }` |
| `icon` | `ReactElement` | Icon applied to all tabs |
| `value` | `number` | Controlled active tab index |
| `onChange` | `(value: number) => void` | Called when tab changes |
| `onClick` | `() => void` | Additional click handler |
| `classes` | `{ root?, tabs?, tab?, panel? }` | Slot overrides |

```tsx
// Uncontrolled (self-manages state)
<Tabnav
  data={[
    { title: "Pestaña 1", content: <div>Contenido 1</div> },
    { title: "Pestaña 2", content: <div>Contenido 2</div> },
  ]}
/>

// Tabs only (no content panels)
<Tabnav
  data={[{ title: "Pestaña 1" }, { title: "Pestaña 2" }]}
/>

// Controlled
<Tabnav
  data={data}
  value={activeTab}
  onChange={(val) => setActiveTab(val)}
/>

// With icon
<Tabnav
  icon={<CheckCircleIcon />}
  data={[{ title: "Título check 1" }, { title: "Título check 2" }]}
/>

// With disabled tab
<Tabnav
  data={[
    { title: "Habilitada" },
    { title: "Deshabilitada", disabled: true },
    { title: "Habilitada" },
  ]}
/>
```

---

#### NavbarItem

```tsx
import { NavbarItem } from "@architecture-it/stylesystem";
import type { NavbarItemProps } from "@architecture-it/stylesystem";
```

Dropdown menu item for use in the `Header`.

```tsx
<NavbarItem
  id="menu-servicios"
  text="Servicios"
  links={[
    { id: "s1", title: "Logística", href: "#" },
    { id: "s2", title: "Ecommerce", href: "#" },
  ]}
/>
```

---

### Cards

#### Card

```tsx
import { Card } from "@architecture-it/stylesystem";
import type { CardProps } from "@architecture-it/stylesystem";
```

| Prop | Type | Description |
|------|------|-------------|
| `cardMediaIcon` | `CardMediaIcon` | **Required.** Image `{src, alt, ...}` **or** ReactElement SVG/component |
| `cardContent` | `ReactNode` | **Required.** Card body |
| `cardActions` | `ReactNode` | Optional actions area |
| `classes` | `{ container?, cardMUI?, cardMedia?, cardContent? }` | Slot CSS overrides |
| `containerGridProps` | `GridProps` | Forwarded to wrapping `Grid` |
| + MUI `CardProps` | | `onClick`, `raised`, etc. |

> **Note:** Styles for Card layouts (sizes, typography) are the **responsibility of the consuming application**. The library provides the structure and base classes only.

```tsx
// Base card (video-like)
<Card
  cardMediaIcon={{ src: "https://placehold.co/380x320", alt: "tutoriales" }}
  cardContent={
    <Typography color="primary" variant="h5">¿Cómo cambiar entrega?</Typography>
  }
  cardActions={
    <Typography color="secondary">ver vídeo <ChevronRightIcon /></Typography>
  }
  classes={{ container: styles.containerCard, cardMUI: styles.rootCard }}
/>

// With ReactElement as media (SVG)
<Card
  cardMediaIcon={<svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="50" fill="blue" /></svg>}
  cardContent={<Typography>Contenido</Typography>}
/>
```

---

#### CardButton

```tsx
import { CardButton } from "@architecture-it/stylesystem";
import type { CardButtonProps } from "@architecture-it/stylesystem";
```

Clickable card variant.

| Prop | Type | Description |
|------|------|-------------|
| `cardMediaIcon` | `CardMediaIcon` | Image or ReactElement |
| `cardContent` | `ReactNode` | Card body |
| `active` | `boolean` | Shows focused/selected state |
| `onClick` | `() => void` | Click handler |
| `id` | `string` | Card id |
| `role` | `string` | ARIA role |
| `classes` | `{ cardContainer?, cardMedia?, cardContent? }` | CSS overrides |

```tsx
<CardButton
  cardMediaIcon={{ src: "/icons/box.svg", alt: "Encomienda" }}
  cardContent={<Typography>Encomienda</Typography>}
  active={selected === "encomienda"}
  onClick={() => setSelected("encomienda")}
/>
```

---

#### Skeletons

```tsx
import {
  CardSkeleton,
  CardButtonSkeleton,
  DescriptionCardSkeleton,
  MainCardSkeleton,
} from "@architecture-it/stylesystem";
```

```tsx
<CardSkeleton />
<CardButtonSkeleton />
<DescriptionCardSkeleton imageHeight={300} width={360} />
<MainCardSkeleton imageWidth={400} width={958} />
```

---

### Data Display

#### Table Components

```tsx
import { Table, TableHead, TableRow, TableFooter, TablePagination } from "@architecture-it/stylesystem";
import { Paper, TableBody, TableCell, TableContainer } from "@mui/material";
```

These are styled wrappers around MUI's Table family.

```tsx
<TableContainer component={Paper}>
  <Table aria-label="simple table">
    <TableHead>
      <TableRow>
        <TableCell>Id</TableCell>
        <TableCell>Nombre</TableCell>
        <TableCell>Apellido</TableCell>
      </TableRow>
    </TableHead>
    <TableBody>
      {rows.map((row) => (
        <TableRow key={row.id}>
          <TableCell>{row.id}</TableCell>
          <TableCell>{row.name}</TableCell>
          <TableCell>{row.surname}</TableCell>
        </TableRow>
      ))}
    </TableBody>
  </Table>
  <TableFooter>
    <TableRow>
      <TablePagination
        count={100}
        page={page}
        rowsPerPage={10}
        rowsPerPageOptions={[]}
        onPageChange={(_, newPage) => setPage(newPage)}
        onRowsPerPageChange={() => {}}
      />
    </TableRow>
  </TableFooter>
</TableContainer>
```

---

#### DescriptionItem

```tsx
import { DescriptionItem } from "@architecture-it/stylesystem";
import type { DescriptionItemProps } from "@architecture-it/stylesystem";
```

Label + value pair for institutional data display.

---

#### ListItem

```tsx
import { ListItem } from "@architecture-it/stylesystem";
import type { ListItemProps } from "@architecture-it/stylesystem";
```

---

#### ListTexts

```tsx
import { ListTexts } from "@architecture-it/stylesystem";
import type { ListTextsProps } from "@architecture-it/stylesystem";
```

---

### Steps Components

#### HorizontalSteps

```tsx
import { HorizontalSteps } from "@architecture-it/stylesystem";
import type { HorizontalStepsProps, HorizontalStepListItem } from "@architecture-it/stylesystem";
```

| Prop | Type | Description |
|------|------|-------------|
| `steps` | `HorizontalStepListItem[]` | Array of steps: `{ icon?, content?: { title?, subtitle? }, isLatest? }` |
| `activeSteps` | `number` | 0-based index of the current active step |
| `primaryColor` | `string` | Color for completed/active steps |
| `secondaryColor` | `string` | Background color for future steps |

```tsx
<HorizontalSteps
  activeSteps={1}
  primaryColor="var(--primary)"
  secondaryColor="var(--gray-300)"
  steps={[
    { content: { title: "Ingresado", subtitle: "10/01/2025" }, icon: <CheckCircleIcon /> },
    { content: { title: "En tránsito", subtitle: "11/01/2025" } },
    { content: { title: "Entregado" } },
  ]}
/>
```

---

#### VerticalSteps

```tsx
import { VerticalSteps } from "@architecture-it/stylesystem";
import type { VerticalStepsProps } from "@architecture-it/stylesystem";
```

| Prop | Type | Description |
|------|------|-------------|
| `steps` | `Array<{ title, icon?, contents: { date?, time?, description? }[] }>` | **Required** |
| `activeStep` | `number` | 0-based step index (0 = last in list = most recent) |
| `primaryColor` | `string` | Active/past step color |
| `secondaryColor` | `string` | Future step color |

```tsx
<VerticalSteps
  activeStep={0}
  primaryColor="var(--primary)"
  secondaryColor="var(--gray-200)"
  steps={[
    {
      title: "En tránsito",
      contents: [{ date: "10/01/2025", time: "14:30", description: "Salió del centro de distribución" }],
    },
    {
      title: "Ingresado",
      contents: [{ date: "09/01/2025", description: "Recibido en origen" }],
    },
  ]}
/>
```

---

#### InfoSteps

```tsx
import { InfoSteps } from "@architecture-it/stylesystem";
import type { InfoStepsProps } from "@architecture-it/stylesystem";
```

Numbered/bulleted step list with optional images.

```tsx
// Enum (numbered, straight lines)
<InfoSteps
  regular
  items={[
    { title: "Paso 1", description: "Descripción del paso uno." },
    { title: "Paso 2", description: "Descripción del **paso dos**.", button: { text: "Ver más", variant: "outlined" } },
  ]}
/>

// With images
<InfoSteps
  items={[
    {
      title: "Empaquetá",
      description: "Usá una caja resistente.",
      image: { src: "/img/step1.png", alt: "empaquetar" },
    },
    {
      title: "Etiquetá",
      description: "Imprimí y pegá la etiqueta.",
      image: { src: "/img/step2.png", alt: "etiquetar" },
    },
  ]}
/>
```

---

### Overlay & Dialogs

#### Modal

```tsx
import { Modal } from "@architecture-it/stylesystem";
import type { ModalProps } from "@architecture-it/stylesystem";
```

Based on MUI `Dialog`.

| Prop | Type | Description |
|------|------|-------------|
| `open` | `boolean` | **Required** |
| `handleClose` | `() => void` | **Required** |
| `title` | `string` | **Required.** Dialog title |
| `subtitle` | `string` | Text below title |
| `content` | `ReactNode` | Scrollable dialog body |
| `buttons` | `[ReactNode, ReactNode?, ReactNode?]` | 1–3 action buttons (tuple) |
| `imgProps` | `img props \| { icon: () => JSX.Element }` | Illustration above title |
| `disableCloseOnBackdrop` | `boolean` | Prevents closing on backdrop click |
| `classes` | `{ dialogTitle?, dialogsubTitle?, modalHeader?, modalPaper?, modalContent?, actions? }` | Slot overrides |

```tsx
const [open, { handleOpen, handleClose }] = useToggle();

<Button text="Abrir Modal" variant="contained" onClick={handleOpen} />

<Modal
  open={open}
  handleClose={handleClose}
  title="Título de modal"
  subtitle="Mensaje explicativo del modal."
  buttons={[
    <Button key="2" text="Cancelar" variant="outlined" />,
    <Button key="1" text="Aceptar" variant="contained" />,
  ]}
/>

// With image
<Modal
  open={open}
  handleClose={handleClose}
  title="¡Atención!"
  imgProps={{ src: "https://example.com/icon.svg", alt: "icono", height: 80, width: 80 }}
  buttons={[<Button key="1" text="Entendido" variant="contained" />]}
/>

// With scroll content
<Modal
  open={open}
  handleClose={handleClose}
  title="Artículos prohibidos"
  imgProps={{ icon: () => <ExclamationCircleIcon /> }}
  content={
    <>
      {items.map((item, i) => (
        <Typography key={i}>{item.description}</Typography>
      ))}
    </>
  }
  buttons={[<Button key="1" text="Cerrar" variant="outlined" />]}
/>
```

---

#### CustomPopover

```tsx
import { CustomPopover } from "@architecture-it/stylesystem";
import type { CustomPopoverProps } from "@architecture-it/stylesystem";
```

---

### AutoComplete & Dropdown

#### AutoComplete

```tsx
import { AutoComplete } from "@architecture-it/stylesystem";
import type { AutoCompleteProps, Option } from "@architecture-it/stylesystem";
```

> **Important:** This component has no default width. Set width via `style` or a custom `className`.

`Option` shape:

```typescript
interface Option {
  value: string;      // Required - internal value and default display text
  title?: string;     // Display name in the dropdown list
  description?: string; // Subtitle in the dropdown list
  group?: string;     // Group header
  secondaryText?: string; // Right-aligned text (e.g. "Turno online")
}
```

**Props (`AutoCompleteProps`):** extends MUI `AutocompleteProps<Option, false, false, false>`.

Key additional props:
- `placeholder` — input placeholder
- `label` — `{ text: string, icon?: ReactNode }` — floating label with optional icon
- `textfieldprops` — forwarded to the inner `TextField`
- `classesprop` — `{ listBox?, paper?, groupLabel?, TextField?, title?, description?, gridItem?, secondaryText?, itemList? }` — CSS overrides per slot

```tsx
// Basic
<AutoComplete
  options={[
    { value: "Sucursal Victoria", title: "Sucursal Victoria", description: "Av. Pres. Perón 2880, Victoria", secondaryText: "Turno online" },
    { value: "Sucursal San Antonio Oeste", title: "Sucursal San Antonio Oeste", description: "Yrigoyen 565, San Antonio Oeste" },
  ]}
  placeholder="Buscá por provincia, localidad o sucursal."
  style={{ width: "500px" }}
/>

// With grouped options
<AutoComplete
  options={[
    { value: "Mesita", title: "Mesita", description: "Mi categoría", group: "Mis Productos" },
    { value: "Heladera", title: "Heladera", description: "Grandes electrodomésticos", group: "Mis Productos" },
    { value: "Bicicleta", title: "Bicicleta", description: "Bicicletas", group: "Productos sugeridos" },
  ]}
  placeholder="Ej: heladera, colchón, tv, etc."
  style={{ width: "400px" }}
/>

// With icon label
<AutoComplete
  options={[...]}
  placeholder="Ej: 1824, Lanús Oeste"
  label={{ icon: <SearchIcon primaryColor="var(--color-base-text)" />, text: "Selecciona una categoría" }}
  style={{ width: "400px" }}
/>
```

**With React Hook Form:**

```tsx
<AutoComplete
  {...register("option")}
  options={options}
  isOptionEqualToValue={(option, value) => option.value === value.value}
  style={{ width: "500px" }}
  placeholder="Buscá una sucursal."
  onChange={(_, data) => setValue("option", data?.value)}
/>
```

**With Formik:**

```tsx
<AutoComplete
  componentName="option"
  options={options}
  isOptionEqualToValue={(option, value) => option.value === value.value}
  style={{ width: "500px" }}
  placeholder="Buscá una sucursal."
  onChange={(_e, value) => formik.setFieldValue("option", value?.value)}
/>
```

---

#### Dropdown

```tsx
import { Dropdown } from "@architecture-it/stylesystem";
import type { DropdownProps } from "@architecture-it/stylesystem";
```

Collapsible accordion-style component.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `title` | `string \| ReactNode` | **Required** | Header text or element |
| `children` | `ReactNode` | | Collapsible content |
| `toggleOnTitle` | `boolean` | `true` | Opens/closes when clicking the title row |
| `initialState` | `boolean` | `false` | Starts open if true |
| `startIcon` | `ReactNode` | | Icon before the title |
| `typographyProps` | `TypographyProps` | | Typography props for the title |
| `unmountOnExit` | `boolean` | `true` | Unmounts content when collapsed |
| `id` | `string` | | DOM id |
| `onClick` | `(e) => void` | | Click handler for title/icon |
| `classes` | `{ container?, titleContainer?, dropdownBox?, icon?, collapseContainer? }` | | Overrides |

```tsx
// Basic FAQ
<Dropdown
  title="¿Cuándo voy a recibir mi envío?"
  typographyProps={{ color: "secondary" }}
>
  <p>El plazo de entrega estándar es de 2 a 3 días hábiles...</p>
</Dropdown>

// With start icon
<Dropdown
  title="Dirección de email"
  startIcon={<EnvelopeIcon primaryColor="var(--primary)" width={15} />}
  typographyProps={{ color: "secondary" }}
>
  <List>
    {emails.map((email) => <ListItem key={email} divider>{email}</ListItem>)}
  </List>
</Dropdown>

// Initially open
<Dropdown title="Mis opciones" initialState>
  <div>contenido</div>
</Dropdown>
```

---

### Interactive

#### ButtonMob

```tsx
import { ButtonMob } from "@architecture-it/stylesystem";
import type { ButtonMobProps } from "@architecture-it/stylesystem";
```

Mobile-optimized button variant.

---

#### FabButton

```tsx
import { FabButton } from "@architecture-it/stylesystem";
import type { FabButtonProps } from "@architecture-it/stylesystem";
```

Floating action button.

---

#### IconButton

```tsx
import { IconButton } from "@architecture-it/stylesystem";
import type { IconButtonProps } from "@architecture-it/stylesystem";
```

```tsx
<IconButton
  icon={<SearchIcon />}
  TooltipText="Buscar"
  onClick={handleSearch}
/>
```

---

#### LikeDislike

```tsx
import { LikeDislike } from "@architecture-it/stylesystem";
import type { LikeDislikeProps } from "@architecture-it/stylesystem";
```

Thumbs-up / thumbs-down interaction component.

---

#### BaseChip

```tsx
import { BaseChip } from "@architecture-it/stylesystem";
import type { BaseChipProps } from "@architecture-it/stylesystem";
```

Extends MUI `Chip`. Used internally in `Select` with `display="chips"`.

```tsx
<BaseChip label="Rojo" size="small" variant="filled" onDelete={() => handleDelete("Rojo")} />
```

---

### Miscellaneous

#### Miscellaneous (decorative)

```tsx
import { Miscellaneous } from "@architecture-it/stylesystem";
import type { MiscellaneousProps, Size } from "@architecture-it/stylesystem";
```

Decorative geometric shape repeater. Used for visual accents on hero cards.

```tsx
<Miscellaneous cant={3} color="red" size="small" type="triangle" />
<Miscellaneous cant={5} color="gray" size="small" type="parallel-filled" />
```

---

#### SocialMedia

```tsx
import { SocialMedia } from "@architecture-it/stylesystem";
import type { SocialMediaProps, Media } from "@architecture-it/stylesystem";
```

```tsx
<SocialMedia
  text="Seguinos en"
  media={[
    { icon: () => <LinkedinIcon />, href: "https://linkedin.com/...", title: "LinkedIn" },
    { icon: () => <YoutubeIcon />, href: "https://youtube.com/...", title: "YouTube" },
    { icon: () => <InstagramIcon />, href: "https://instagram.com/...", title: "Instagram" },
  ]}
/>
```

---

#### Speaker

```tsx
import { Speaker } from "@architecture-it/stylesystem";
import type { SpeakerProps } from "@architecture-it/stylesystem";
```

---

#### Logos

```tsx
import { Logos } from "@architecture-it/stylesystem";
import type { LogosProps } from "@architecture-it/stylesystem";
```

---

#### CustomSection

```tsx
import { CustomSection } from "@architecture-it/stylesystem";
import type { CustomSectionProps } from "@architecture-it/stylesystem";
```

---

#### ThemeToggle

```tsx
import { ThemeToggle, useThemeMode } from "@architecture-it/stylesystem";
import type { IThemeToggleProps, IUseThemeModeProps } from "@architecture-it/stylesystem";
```

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `lightText` | `string` | `"Light Mode"` | Label when switching to light mode |
| `darkText` | `string` | `"Dark Mode"` | Label when switching to dark mode |
| `disableLabelText` | `boolean` | `false` | Hides the text label, shows only the icon |
| `wrapper` | `Element \| null` | `:root` | DOM element to set `data-theme-mode` attribute on |

```tsx
// Full toggle with label
<ThemeToggle />

// Icon only
<ThemeToggle disableLabelText />

// Programmatic
const { mode, toggleMode, setMode } = useThemeMode();
setMode("dark");
toggleMode();
```

---

### Error Handling

#### ErrorBoundary

```tsx
import { ErrorBoundary } from "@architecture-it/stylesystem";
import type { ErrorBoundaryProps } from "@architecture-it/stylesystem";
```

```tsx
<ErrorBoundary fallback={<FallbackComponent />}>
  <MyRiskyComponent />
</ErrorBoundary>
```

---

#### FallbackComponent

```tsx
import { FallbackComponent } from "@architecture-it/stylesystem";
import type { FallbackProps } from "@architecture-it/stylesystem";
```

---

### ServicesStatus

```tsx
import { ServicesStatus } from "@architecture-it/stylesystem";
import type { IServicesStatusProps, IService } from "@architecture-it/stylesystem";
```

Displays a grid of service health/status indicators.

---

## Full Component Index (exports)

```typescript
// Form / Primary
Button, Checkbox, IconButton, Input, InputQuantity, Pills, Radio, Search, Select, Switch, ListControl

// Components
Alert, AutoComplete, BreadCrumb, ButtonMob, BaseChip, CustomSection, Dropdown,
ErrorBoundary, FallbackComponent, HorizontalSteps, InfoSteps, InputFile, LikeDislike,
Loading, ListItem, ListTexts, NavbarItem, Miscellaneous, Modal, SocialMedia, Speaker,
Table, TableFooter, TableRow, TableHead, Tabnav, Toast, VerticalSteps, FabButton,
Tooltip, CustomPopover

// Cards
Card, CardButton
CardSkeleton, CardButtonSkeleton, DescriptionCardSkeleton, MainCardSkeleton

// Institutional
DescriptionItem

// Layout
Footer, FooterList, Header, Logos, Sidebar, SidebarAvatar, SidebarItem, SidebarMini

// Theme / Dark mode
ThemeToggle, useThemeMode

// Services
ServicesStatus

// Theme
ThemeDefault (default export from "./Theme")

// HOC
RepeatElementHOC, StyleSystemProvider

// Hooks
useToggle

// Utils
joinClasses, getFormatedDate, prepareViewport, getImagePropsLogoByBrand, getRoutes, getReturnRoute

// Icons
SearchIcon, CheckCircleIcon, ArrowLeftIcon, ArrowRightIcon, ChevronDownIcon, ChevronUpIcon,
ChevronLeftIcon, ChevronRightIcon, TimesIcon, CloseIcon, SpinnerThirdIcon, MoonIcon, SunIcon,
EditIcon, EnvelopeIcon, BarsIcon, CalendarIcon, ... (see Icons section for full list)

// Themes
cds, hop, witwot
```

---

## Migration Guide

### v1 → v2

Key changes:
- **MUI peer deps**: `@emotion/react` and `@emotion/styled` are now required separately.
- **Import paths**: `material-ui/*` → `@mui/*`
- **`Input` renamed to `InputBase`** (the old `Input` still exists but will be removed in future versions)
- **`Select` extracted** from `Input` into its own component `Select`

```bash
# Run MUI v4→v5 codemods
npx @mui/codemod v5.0.0/preset-safe src
```

---

### v2 → v3

Key changes:

#### Icons — FontAwesome decoupled

FontAwesome is **no longer a required peer dependency**. Remove these from your app's dependencies if you don't use them elsewhere:
- `@fortawesome/react-fontawesome`
- `@fortawesome/free-brands-svg-icons`
- `@fortawesome/pro-light-svg-icons`
- `@fortawesome/pro-regular-svg-icons`
- `@fortawesome/pro-solid-svg-icons`

**Update all icon usages in stylesystem components:**

```tsx
// BEFORE (v2)
<Alert
  color="success"
  iconProps={{ icon: faCheckCircle }}
  open={open}
  variant="outlined"
  onCloseProp={() => dispatch(hide())}
>
  {message}
</Alert>

// AFTER (v3+)
import { Alert, CheckCircleIcon } from "@architecture-it/stylesystem";

<Alert
  color="success"
  icon={<CheckCircleIcon />}
  open={open}
  variant="outlined"
  onCloseProp={() => dispatch(hide())}
>
  {message}
</Alert>
```

For icons **not** in the built-in set, continue using FontAwesome directly:

```tsx
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faXmark } from "@fortawesome/free-solid-svg-icons";

<Button
  text="Eliminar filtros"
  variant="text"
  size="small"
  startIcon={<FontAwesomeIcon icon={faXmark} />}
/>
```

#### Unit Testing

When using `renderWithProviders` you may see provider warnings. Fix:

```typescript
import getTheme from "@architecture-it/stylesystem/Theme";

const colors = { primary: "#d71920" };
// Use getTheme(isDark, colors) inside your test ThemeProvider wrapper
```

---

## Resources

Use and CSS variables available in the file [resources/cartesian.md](resources/cartesian.md)

Detailed per-component resource files are available in the `resources/` subfolder:

- [resources/Button.md](resources/Button.md)
- [resources/Input.md](resources/Input.md)
- [resources/Select.md](resources/Select.md)
- [resources/Alert.md](resources/Alert.md)
- [resources/Modal.md](resources/Modal.md)
- [resources/Toast.md](resources/Toast.md)
- [resources/Sidebar.md](resources/Sidebar.md)
- [resources/Header.md](resources/Header.md)
- [resources/Footer.md](resources/Footer.md)
- [resources/Tabnav.md](resources/Tabnav.md)
- [resources/Table.md](resources/Table.md)
- [resources/AutoComplete.md](resources/AutoComplete.md)
- [resources/Dropdown.md](resources/Dropdown.md)
- [resources/BreadCrumb.md](resources/BreadCrumb.md)
- [resources/Cards.md](resources/Cards.md)
- [resources/Steps.md](resources/Steps.md)
- [resources/FormControls.md](resources/FormControls.md)
- [resources/Icons.md](resources/Icons.md)
- [resources/ThemeAndProvider.md](resources/ThemeAndProvider.md)
- [resources/Migration.md](resources/Migration.md)
