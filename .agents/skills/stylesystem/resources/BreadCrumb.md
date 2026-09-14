# BreadCrumb

**Import:** `import { BreadCrumb } from "@architecture-it/stylesystem";`  
**Type:** `import type { BreadCrumbProps } from "@architecture-it/stylesystem";`

Breadcrumb navigation bar based on MUI `Breadcrumbs`. Works with the `getRoutes` and `getReturnRoute` utility functions for automatic React Router integration.

## Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `routes` | `RouteItem[]` | ✅ | Array of breadcrumb segments |
| `onClick` | `(index: number) => void` | | Callback when a breadcrumb segment is clicked. Receives segment index |
| `classes` | `{ root?, link?, separator?, text? }` | | CSS slot overrides |

### `RouteItem` shape

```ts
interface RouteItem {
  label: string;  // Display text for the breadcrumb
  path: string;   // URL path for the segment
}
```

## Utility Functions

### `getRoutes(pathname: string): RouteItem[]`

Splits a URL path string into an array of `RouteItem` breadcrumb segments.

```ts
getRoutes("/envios/nacional/crear")
// => [
//   { label: "envios",    path: "/envios" },
//   { label: "nacional",  path: "/envios/nacional" },
//   { label: "crear",     path: "/envios/nacional/crear" },
// ]
```

### `getReturnRoute(routes: RouteItem[], index: number): string`

Returns the `path` from `routes[index]`, used as the navigation target when a breadcrumb is clicked.

```ts
getReturnRoute(routes, 0)  // "/envios"
getReturnRoute(routes, 1)  // "/envios/nacional"
```

## Usage Examples

### Full React Router integration

```tsx
import {
  BreadCrumb,
  getRoutes,
  getReturnRoute
} from "@architecture-it/stylesystem";
import { useLocation, useNavigate } from "react-router-dom";

function AppBreadCrumb() {
  const location = useLocation();
  const navigate = useNavigate();
  const routes = getRoutes(location.pathname);

  return (
    <BreadCrumb
      routes={routes}
      onClick={(index) => navigate(getReturnRoute(routes, index))}
    />
  );
}
```

### Inside Header (common pattern)

```tsx
<Header onClickButton={handleSidebarOpen}>
  <BreadCrumb
    routes={getRoutes(location.pathname)}
    onClick={(index) => navigate(getReturnRoute(routes, index))}
  />
</Header>
```

### Static breadcrumb (no navigation)

```tsx
const routes = [
  { label: "Inicio", path: "/" },
  { label: "Envíos", path: "/envios" },
  { label: "Detalle", path: "/envios/detalle" },
];

<BreadCrumb routes={routes} />
```

### Custom click handler

```tsx
<BreadCrumb
  routes={routes}
  onClick={(index) => {
    if (index === 0) {
      router.push("/");
    } else {
      router.push(routes[index].path);
    }
  }}
/>
```

## Notes

- The last segment (current page) is not clickable and renders as plain text.
- All previous segments are rendered as `Link` elements.
- `getRoutes` strips leading slash and creates cumulative paths automatically.
- `BreadCrumb` is often placed inside `Header` as a child, but can be used standalone (e.g., below a `Header`).
- The `label` returned by `getRoutes` is the raw path segment (e.g., `"envios"`). You may want to map IDs to human-readable names for dynamic routes like `/envios/123`.
