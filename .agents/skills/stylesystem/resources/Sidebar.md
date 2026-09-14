# Sidebar

**Import:** `import { Sidebar, SidebarAvatar, SidebarItem, SidebarMini } from "@architecture-it/stylesystem";`

Full navigation sidebar with an `SwipeableDrawer` base. Supports grouped navigation, user avatar with logout, social media links, and MUI theme variants.

## Sidebar Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `open` | `boolean` | ✅ | Controls drawer open state |
| `onClose` | `() => void` | ✅ | Callback to close the drawer |
| `onOpen` | `() => void` | ✅ | Callback to open the drawer (swipe-to-open) |
| `routes` | `SidebarItemProps[]` | | Navigation item list |
| `sidebarItemClassName` | `string` | | Extra CSS class applied to each `SidebarItem` |

## SidebarItemProps

| Prop | Type | Description |
|------|------|-------------|
| `name` | `string` | Label text |
| `path` | `string` | Navigation URL |
| `description` | `string` | Optional secondary text |
| `icon` | `ReactElement` | Icon displayed left of the label |
| `isActive` | `boolean` | Highlights as the current page |
| `badge` | `number` | Badge count shown on the icon |
| `onClick` | `() => void` | Custom click handler (overrides default router navigation) |

## SidebarAvatar Props

| Prop | Type | Description |
|------|------|-------------|
| `name` | `string` | User display name |
| `description` | `string` | Secondary text (role, email, etc.) |
| `avatarSrc` | `string` | Optional avatar image URL |
| `socialMedia` | `SocialMediaProps[]` | Social icons (see SocialMedia component) |
| `onLogout` | `() => void` | Logout callback; renders a logout icon button |
| `classes` | `{ root?, avatar?, texts?, name?, description? }` | CSS slot overrides |

## SidebarMini Props

Compact sidebar variant (icon-only, expands on hover):

| Prop | Type | Description |
|------|------|-------------|
| `routes` | `SidebarItemProps[]` | Navigation items |
| `position` | `"left" \| "right"` | Side the drawer appears on |

## Usage Examples

### Basic sidebar with routes

```tsx
import {
  Sidebar, SidebarItem,
  useToggle, HomeIcon, BoxIcon, TruckIcon
} from "@architecture-it/stylesystem";
import { useLocation, useNavigate } from "react-router-dom";

const routes = [
  { name: "Inicio", path: "/", icon: <HomeIcon /> },
  { name: "Envíos", path: "/envios", icon: <TruckIcon /> },
  { name: "Paquetes", path: "/paquetes", icon: <BoxIcon /> },
];

function App() {
  const [open, { handleOpen, handleClose }] = useToggle();
  const location = useLocation();
  const navigate = useNavigate();

  return (
    <Sidebar
      open={open}
      onOpen={handleOpen}
      onClose={handleClose}
      routes={routes.map((r) => ({
        ...r,
        isActive: location.pathname === r.path,
        onClick: () => { navigate(r.path); handleClose(); },
      }))}
    />
  );
}
```

### Sidebar with avatar and social media

```tsx
import {
  Sidebar, SidebarAvatar,
  InstagramIcon, FacebookIcon
} from "@architecture-it/stylesystem";

<Sidebar open={open} onOpen={handleOpen} onClose={handleClose} routes={routes}>
  <SidebarAvatar
    name="Juan Pérez"
    description="juanperez@email.com"
    onLogout={() => auth.logout()}
    socialMedia={[
      { icon: <InstagramIcon />, url: "https://instagram.com/brand" },
      { icon: <FacebookIcon />, url: "https://facebook.com/brand" },
    ]}
  />
</Sidebar>
```

### SidebarMini (icon-only compact)

```tsx
import { SidebarMini } from "@architecture-it/stylesystem";

<SidebarMini
  position="left"
  routes={[
    { name: "Inicio", path: "/", icon: <HomeIcon />, isActive: true },
    { name: "Envíos", path: "/envios", icon: <TruckIcon /> },
  ]}
/>
```

### Toggling from a Header

```tsx
const [open, { handleOpen, handleClose }] = useToggle();

<Header onClickButton={handleOpen} />
<Sidebar open={open} onOpen={handleOpen} onClose={handleClose} routes={routes} />
```

## Notes

- `Sidebar` uses MUI `SwipeableDrawer` — on mobile the user can swipe to open/close.
- `SidebarItem` is exported and can be used standalone inside `Sidebar` children or custom menus.
- Children passed to `Sidebar` render **above** the routes list.
- Use `sidebarItemClassName` to style all route items uniformly (e.g., adjust padding for dense mode).
