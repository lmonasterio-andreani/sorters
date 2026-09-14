# Header

**Import:** `import { Header } from "@architecture-it/stylesystem";`  
**Type:** `import type { HeaderProps } from "@architecture-it/stylesystem";`

Top application bar (AppBar). Shows an optional hamburger menu button, a logo, an optional module name, and children slots for navigation / user tools.

## Props

Extends MUI `AppBarProps`:

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `onClickButton` | `() => void` | | Handler for the hamburger (☰) icon. If omitted, no button renders |
| `logo` | `ReactElement` | | Custom logo element. If omitted, uses default brand logo |
| `position` | `"static" \| "fixed" \| "sticky" \| "absolute" \| "relative"` | `"static"` | MUI AppBar position |
| `disableMenuButton` | `boolean` | | Hides the hamburger button completely |
| `moduleName` | `string` | | Renders a `Typography` label next to the logo |
| `children` | `ReactNode` | | Rendered in the right side of the AppBar |
| `classes` | `{ root?, toolbar?, logo? }` | | CSS slot overrides |

## Usage Examples

### Basic header (Sidebar toggle)

```tsx
const [open, { handleOpen, handleClose }] = useToggle();

<Header onClickButton={handleOpen} />
<Sidebar open={open} onOpen={handleOpen} onClose={handleClose} routes={routes} />
```

### Header with BreadCrumb

```tsx
import { Header, BreadCrumb, getRoutes, getReturnRoute } from "@architecture-it/stylesystem";
import { useLocation, useNavigate } from "react-router-dom";

function AppHeader() {
  const location = useLocation();
  const navigate = useNavigate();
  const routes = getRoutes(location.pathname);

  return (
    <Header onClickButton={() => setSidebarOpen(true)}>
      <BreadCrumb
        routes={routes}
        onClick={(index) => navigate(getReturnRoute(routes, index))}
      />
    </Header>
  );
}
```

### Header with Dropdown menu and NavbarItem

```tsx
import { Header, Dropdown, NavbarItem } from "@architecture-it/stylesystem";

<Header onClickButton={handleOpen} disableMenuButton={false}>
  <Dropdown title="Soporte" startIcon={<HelpIcon />}>
    <NavbarItem text="Base de conocimiento" href="/knowledge" />
    <NavbarItem text="Reportar un problema" href="/issues" />
  </Dropdown>
</Header>
```

### Header with user info (logged-in state)

```tsx
<Header onClickButton={handleOpen}>
  <Box display="flex" alignItems="center" gap={1}>
    <Avatar src={user.avatarUrl} />
    <Typography variant="body2">{user.name}</Typography>
    <IconButton onClick={handleLogout}><ExitToAppIcon /></IconButton>
  </Box>
</Header>
```

### Header with custom logo

```tsx
import { getImagePropsLogoByBrand } from "@architecture-it/stylesystem";

const logoProps = getImagePropsLogoByBrand("hop");

<Header
  logo={<img {...logoProps} style={{ height: 40 }} />}
  onClickButton={handleOpen}
/>
```

### DMS-style header with module name

```tsx
<Header moduleName="Gestión de Envíos" position="sticky">
  {/* children render in top-right */}
  <Button text="Nueva solicitud" variant="contained" size="small" />
</Header>
```

## Notes

- If `onClickButton` is not provided, the hamburger button does not render.
- `position="sticky"` keeps the header visible on scroll — pair with `top: 0` in CSS if needed.
- Children are rendered right-aligned inside the `Toolbar` via `Box flex={1}`.
- For multi-brand theming, wrap header content inside a `<div className={cds.styles}>` or use `StyleSystemProvider` brand tokens.
