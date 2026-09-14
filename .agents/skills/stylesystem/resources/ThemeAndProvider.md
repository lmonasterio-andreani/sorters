# Theme & Provider

**Imports:**
```tsx
import { StyleSystemProvider } from "@architecture-it/stylesystem";
import { ThemeToggle, useThemeMode } from "@architecture-it/stylesystem";
import { cds, hop, witwot } from "@architecture-it/stylesystem";
import { getImagePropsLogoByBrand } from "@architecture-it/stylesystem";
```

---

## StyleSystemProvider

**Required** root wrapper for all apps using the stylesystem. Sets up MUI's `ThemeProvider`, `StyledEngineProvider`, CSS variable injection, and dark mode support.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `children` | `ReactNode` | — | App tree |
| `defaultThemeMode` | `"light" \| "dark"` | `"light"` | Initial color mode |
| `disableInjectFirst` | `boolean` | `false` | Disables `StyledEngineProvider injectFirst`. Only disable if you need CSS specificity control. |
| `className` | `string` | | Class applied to the provider wrapper div |

### Basic Setup

```tsx
// src/main.tsx or _app.tsx
import { StyleSystemProvider } from "@architecture-it/stylesystem";

function App() {
  return (
    <StyleSystemProvider defaultThemeMode="light">
      <YourRouter />
    </StyleSystemProvider>
  );
}
```

### With brand theme

```tsx
import { StyleSystemProvider, cds } from "@architecture-it/stylesystem";

<StyleSystemProvider className={cds.styles} defaultThemeMode="light">
  <App />
</StyleSystemProvider>
```

### With dark mode default

```tsx
<StyleSystemProvider defaultThemeMode="dark">
  <App />
</StyleSystemProvider>
```

---

## Brand Themes

Three brand themes available. Each exports:
- `.styles` — CSS class string to apply to a wrapper element (includes all CSS custom properties)
- `.css` — Raw CSS string (for SSR or injecting manually)

| Brand | Description |
|-------|-------------|
| `cds` | Andreani CDS brand (blue palette) |
| `hop` | HOP brand |
| `witwot` | Witwot brand |

### Brand Theme Usage

```tsx
import { cds, hop, witwot } from "@architecture-it/stylesystem";
import { StyleSystemProvider } from "@architecture-it/stylesystem";

// Apply via StyleSystemProvider className (recommended)
<StyleSystemProvider className={cds.styles}>
  <App />
</StyleSystemProvider>

// Or apply to any container to scope a brand section
<div className={hop.styles}>
  <HopComponents />
</div>

// Access raw CSS (e.g., SSR)
<style>{cds.css}</style>
```

### Multi-brand layout

```tsx
import { cds, hop } from "@architecture-it/stylesystem";

<Box>
  <div className={cds.styles}>
    <Header />
    <MainContent />
  </div>
  <div className={hop.styles}>
    <PartnerWidget />
  </div>
</Box>
```

---

## Dark Mode

Dark mode is controlled via MUI's `useColorScheme` system, exposed through two utilities:

### ThemeToggle Component

Renders a toggle switch (or button) that switches between light and dark mode:

```tsx
import { ThemeToggle } from "@architecture-it/stylesystem";

// Typically in Header children
<Header onClickButton={handleOpen}>
  <ThemeToggle />
</Header>
```

### useThemeMode Hook

```tsx
import { useThemeMode } from "@architecture-it/stylesystem";

const { mode, setMode } = useThemeMode();

// mode — "light" | "dark" | "system"
// setMode — (mode: "light" | "dark" | "system") => void

<Button
  text={mode === "dark" ? "Modo claro" : "Modo oscuro"}
  onClick={() => setMode(mode === "dark" ? "light" : "dark")}
/>
```

### Dark-aware components

The `Input` component accepts a `dark` prop to force dark-variant styles regardless of global theme mode:

```tsx
<Input label="Campo" dark />
```

---

## `getImagePropsLogoByBrand`

Returns `<img>` props for the correct brand logo.

```ts
function getImagePropsLogoByBrand(
  brand: "cds" | "hop" | "witwot" | "andreani" | undefined
): ImgHTMLAttributes<HTMLImageElement>
```

### Usage

```tsx
import { getImagePropsLogoByBrand } from "@architecture-it/stylesystem";

// Standard usage
const logoProps = getImagePropsLogoByBrand("cds");
<img {...logoProps} style={{ height: 40 }} />

// In Header
<Header logo={<img {...getImagePropsLogoByBrand("andreani")} height={36} />} />

// Dynamic brand from env
const brand = process.env.REACT_APP_BRAND as "cds" | "hop" | "witwot";
<img {...getImagePropsLogoByBrand(brand)} />
```

Returns `undefined` props if brand is `undefined` — safe to spread.

---

## Complete App Setup Example

```tsx
// src/main.tsx
import React from "react";
import ReactDOM from "react-dom/client";
import { StyleSystemProvider, cds } from "@architecture-it/stylesystem";
import { BrowserRouter } from "react-router-dom";
import App from "./App";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <StyleSystemProvider className={cds.styles} defaultThemeMode="light">
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </StyleSystemProvider>
  </React.StrictMode>
);
```

```tsx
// src/App.tsx
import {
  Header, Sidebar, useToggle,
  ThemeToggle, getImagePropsLogoByBrand
} from "@architecture-it/stylesystem";

function App() {
  const [open, { handleOpen, handleClose }] = useToggle();

  return (
    <>
      <Header
        onClickButton={handleOpen}
        logo={<img {...getImagePropsLogoByBrand("cds")} height={36} />}
      >
        <ThemeToggle />
      </Header>
      <Sidebar open={open} onOpen={handleOpen} onClose={handleClose} routes={routes} />
      <main>
        {/* page content */}
      </main>
    </>
  );
}
```

## Notes

- `StyleSystemProvider` **must** be at the root level — placing it inside a subtree will scope only that subtree's MUI theme context.
- `disableInjectFirst={true}` moves MUI styles lower in the CSS cascade — only use this if you have CSS specificity conflicts with custom stylesheets.
- Dark mode state persists via MUI's built-in `localStorage` mechanism when using `useColorScheme`.
- The brand theme CSS variables (from `cds.styles`, etc.) must be applied on a DOM element that wraps all components; applying them to `<body>` via `StyleSystemProvider className` is the simplest approach.
