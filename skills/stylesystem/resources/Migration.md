# Migration Guide

Migration notes for upgrading between major versions of `@architecture-it/stylesystem`.

---

## v1 → v2

### Summary

v2 replaced JSS (Material UI v4 style system) with Emotion (Material UI v5). All class name APIs changed.

### Breaking Changes

#### 1. MUI v4 → v5 + Emotion

**Before (v1):** `makeStyles`, `useStyles`, `createStyles` from `@material-ui/core`  
**After (v2):** Use `sx` prop, `styled()` from `@emotion/styled`, or CSS Modules

```tsx
// Before
import { makeStyles } from "@material-ui/core";
const useStyles = makeStyles({ root: { color: "red" } });
function MyComp() {
  const classes = useStyles();
  return <div className={classes.root} />;
}

// After
import { Box } from "@mui/material";
function MyComp() {
  return <Box sx={{ color: "red" }} />;
}
// Or with emotion:
import styled from "@emotion/styled";
const Root = styled("div")({ color: "red" });
```

#### 2. Peer dependency changes

**Before:** `@material-ui/core`, `@material-ui/icons`  
**After:** `@mui/material`, `@mui/icons-material`, `@emotion/react`, `@emotion/styled`

```bash
# Remove:
pnpm remove @material-ui/core @material-ui/icons

# Install:
pnpm add @mui/material @emotion/react @emotion/styled
```

#### 3. StyleSystemProvider is now required

**Before:** No provider required; styles were injected via JSS  
**After:** Wrap your app in `StyleSystemProvider`:

```tsx
import { StyleSystemProvider } from "@architecture-it/stylesystem";

<StyleSystemProvider>
  <App />
</StyleSystemProvider>
```

#### 4. `makeStyles` / `withStyles` class overrides

MUI v5 changed the `classes` prop structure on some components. Check individual component docs for updated `classes` key names.

#### 5. Component import paths

All components are now exported from the top-level package (no deep imports):

```tsx
// Before
import Button from "@architecture-it/stylesystem/Button";

// After
import { Button } from "@architecture-it/stylesystem";
```

---

## v2 → v3

### Summary

v3 removed the FontAwesome peer dependency and introduced the built-in icon set. All icon usage must be migrated.

### Breaking Changes

#### 1. Remove FontAwesome peer dependency

**Before:** Required peer deps for icons:
```json
"@fortawesome/fontawesome-svg-core": "^6.x",
"@fortawesome/pro-regular-svg-icons": "^6.x",
"@fortawesome/react-fontawesome": "^0.x"
```

**After:** No FontAwesome needed. Remove from `package.json` and `pnpm`.

```bash
pnpm remove @fortawesome/fontawesome-svg-core @fortawesome/pro-regular-svg-icons @fortawesome/react-fontawesome
```

#### 2. Replace icon usage

All icons previously used via FontAwesome now have direct replacements in the stylesystem:

```tsx
// Before (v2)
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTruck } from "@fortawesome/pro-regular-svg-icons";
<FontAwesomeIcon icon={faTruck} color="blue" size="lg" />

// After (v3)
import { TruckIcon } from "@architecture-it/stylesystem";
<TruckIcon primaryColor="blue" width={20} height={20} />
```

#### 3. Common icon migration table

| FontAwesome | v3 Icon |
|-------------|---------|
| `faTruck` | `TruckIcon` |
| `faCheckCircle` | `CheckCircleIcon` |
| `faTimes` | `TimesIcon` |
| `faTimesCircle` | `TimesCircleIcon` |
| `faSearch` | `SearchIcon` |
| `faFilter` | `FilterIcon` |
| `faDownload` | `DownloadIcon` |
| `faUpload` | `UploadIcon` |
| `faTrash` | `DeleteIcon` |
| `faPencil` / `faEdit` | `EditIcon` |
| `faInfoCircle` | `InfoCircleIcon` |
| `faExclamationCircle` | `ExclamationCircleIcon` |
| `faExclamationTriangle` | `ExclamationTriangleIcon` |
| `faChevronDown` | `ChevronDownIcon` |
| `faChevronUp` | `ChevronUpIcon` |
| `faChevronLeft` | `ChevronLeftIcon` |
| `faChevronRight` | `ChevronRightIcon` |
| `faAngleDown` | `AngleDownIcon` |
| `faBell` | `BellIcon` |
| `faCalendar` | `CalendarIcon` |
| `faHome` | `HomeIcon` |
| `faBox` | `BoxIcon` |
| `faPhone` | `PhoneIcon` |
| `faEnvelope` | `EnvelopeIcon` |
| `faLock` | `LockIcon` |
| `faUnlock` | `UnlockIcon` |
| `faUser` | `UserIcon` |
| `faUserCircle` | `UserCircleIcon` |
| `faInstagram` | `InstagramIcon` |
| `faFacebook` | `FacebookIcon` |
| `faLinkedin` | `LinkedInIcon` |
| `faTwitter` | `TwitterIcon` |
| `faYoutube` | `YoutubeIcon` |
| `faWhatsapp` | `WhatsAppIcon` |

#### 4. Icon size mapping

FontAwesome `size` prop vs stylesystem:

| FA size | stylesystem width/height |
|---------|--------------------------|
| `xs` | `12` |
| `sm` | `16` |
| (default) | `20` |
| `lg` | `24` |
| `xl` | `32` |
| `2x` | `40` |
| `3x` | `64` |

#### 5. Color mapping

FontAwesome icon colors were applied via `color` prop or inherited CSS color. Stylesystem icons use explicit `primaryColor`/`secondaryColor` props:

```tsx
// Before
<FontAwesomeIcon icon={faTruck} color="var(--primary)" />

// After
<TruckIcon primaryColor="var(--primary)" />
```

---

## v3 → v7 (current)

### Summary

v7 updated peer dependencies to MUI v7. No major API changes to component props. The main action is updating peer dependency versions.

### Peer Dependency Update

```json
{
  "peerDependencies": {
    "@architecture-it/cartesian": ">=7",
    "@emotion/react": ">=11",
    "@emotion/styled": ">=11",
    "@mui/material": ">=7.1.2"
  }
}
```

```bash
pnpm add @mui/material@^7 @architecture-it/cartesian@^7
```

### Node.js requirement

Node.js **>= 20** is required as of v7.

---

## General Migration Checklist

- [ ] Update `@architecture-it/stylesystem` to target version
- [ ] Update `@mui/material`, `@emotion/react`, `@emotion/styled` peer deps
- [ ] Update `@architecture-it/cartesian` if used
- [ ] Ensure Node.js >= 20
- [ ] Wrap app in `StyleSystemProvider`
- [ ] Apply brand theme class (`cds.styles`, `hop.styles`, or `witwot.styles`)
- [ ] Replace FontAwesome icons with stylesystem icons (v2→v3)
- [ ] Replace `@material-ui` imports with `@mui` (v1→v2)
- [ ] Replace `makeStyles`/`withStyles` with `sx` prop or `styled()` (v1→v2)
