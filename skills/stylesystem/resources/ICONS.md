# Icons

**Import:** Named exports from `@architecture-it/stylesystem`

Since v3 the library ships its own SVG icon set. FontAwesome peer dependency was removed. Icons are React components that accept CSS variable-based color props.

## Props (all icons share the same interface)

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `primaryColor` | `string` | CSS var | Main fill color. Pass any CSS color or CSS variable |
| `secondaryColor` | `string` | CSS var | Secondary/accent fill color (dual-tone icons) |
| `width` | `string \| number` | `24` | SVG width |
| `height` | `string \| number` | `24` | SVG height |
| `spin` | `boolean` | `false` | Rotates the icon (useful for loading states) |
| `className` | `string` | | Extra CSS class |
| `cursor` | `string` | | CSS cursor value |

## Naming Convention

Two export styles — **both work**:

| Style | Example | Status |
|-------|---------|--------|
| `XxxIcon` (preferred) | `CheckCircleIcon` | Current |
| `Icon as Xxx` (deprecated) | `import { Icon as CheckCircle }` | Deprecated, still works |

Always use the `XxxIcon` named export in new code.

## Full Icon List

```tsx
import {
  AlertIcon,
  AlertCircleIcon,
  AngleDownIcon,
  AngleLeftIcon,
  AngleRightIcon,
  AngleUpIcon,
  ArrowCircleLeftIcon,
  ArrowCircleRightIcon,
  ArrowDownIcon,
  ArrowLeftIcon,
  ArrowRightIcon,
  ArrowUpIcon,
  BellIcon,
  BoxIcon,
  CalendarCheckIcon,
  CalendarIcon,
  CallCenterIcon,
  CheckCircleIcon,
  CheckIcon,
  ChevronDoubleLeftIcon,
  ChevronDoubleRightIcon,
  ChevronDownIcon,
  ChevronLeftIcon,
  ChevronRightIcon,
  ChevronUpIcon,
  ClockIcon,
  CloseIcon,
  CloudUploadIcon,
  CopyIcon,
  DeleteIcon,
  DownloadIcon,
  EditIcon,
  EnvelopeIcon,
  ExclamationCircleIcon,
  ExclamationIcon,
  ExclamationTriangleIcon,
  EyeIcon,
  EyeSlashIcon,
  FacebookIcon,
  FilterIcon,
  FolderIcon,
  GlobeIcon,
  HelpIcon,
  HomeIcon,
  InfoCircleIcon,
  InstagramIcon,
  KeyIcon,
  LinkedInIcon,
  LocationIcon,
  LockIcon,
  LogoutIcon,
  MapMarkerIcon,
  MenuIcon,
  MinusIcon,
  MoreHorizIcon,
  MoreVertIcon,
  PackageIcon,
  PaperclipIcon,
  PhoneIcon,
  PlusIcon,
  PrintIcon,
  QrCodeIcon,
  RefreshIcon,
  SearchIcon,
  SettingsIcon,
  ShareIcon,
  ShoppingCartIcon,
  SortIcon,
  StarIcon,
  TimesCircleIcon,
  TimesIcon,
  TruckIcon,
  TwitterIcon,
  UnlockIcon,
  UploadIcon,
  UserCircleIcon,
  UserIcon,
  WhatsAppIcon,
  YoutubeIcon,
  ZoomInIcon,
  ZoomOutIcon,
} from "@architecture-it/stylesystem";
```

## Usage Examples

### Inline with text

```tsx
<Box display="flex" alignItems="center" gap={1}>
  <TruckIcon primaryColor="var(--primary)" width={20} height={20} />
  <Typography>En tránsito</Typography>
</Box>
```

### In a Button

```tsx
<Button
  text="Descargar"
  variant="outlined"
  icon={<DownloadIcon primaryColor="var(--primary)" />}
/>
```

### In a `Tooltip` trigger

```tsx
<Tooltip text="Más información" variant="info">
  <InfoCircleIcon primaryColor="var(--c-color-icon-info)" />
</Tooltip>
```

### Spinning loader icon

```tsx
<RefreshIcon spin primaryColor="var(--primary)" width={24} height={24} />
```

### Dual-tone icon

```tsx
<CheckCircleIcon
  primaryColor="var(--secondary-green)"
  secondaryColor="var(--c-color-surface-success)"
  width={48}
  height={48}
/>
```

### Using CSS variables for theming

```tsx
// Always prefer CSS variables over hardcoded colors:
<TimesIcon primaryColor="var(--primary)" />
<CheckIcon primaryColor="var(--secondary-green)" />
<ExclamationTriangleIcon primaryColor="var(--secondary-yellow)" />
<InfoCircleIcon primaryColor="var(--c-color-icon-info)" />
```

### Social media icons

```tsx
<Box display="flex" gap={2}>
  <a href="https://facebook.com"><FacebookIcon primaryColor="var(--primary)" /></a>
  <a href="https://instagram.com"><InstagramIcon primaryColor="var(--primary)" /></a>
  <a href="https://linkedin.com"><LinkedInIcon primaryColor="var(--primary)" /></a>
  <a href="https://twitter.com"><TwitterIcon primaryColor="var(--primary)" /></a>
  <a href="https://youtube.com"><YoutubeIcon primaryColor="var(--primary)" /></a>
  <a href="https://wa.me/549XXXXXXXXXX"><WhatsAppIcon primaryColor="#25D366" /></a>
</Box>
```

## Migration Note (v2 → v3)

**Before (v2):**
```tsx
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTruck } from "@fortawesome/pro-regular-svg-icons";

<FontAwesomeIcon icon={faTruck} />
```

**After (v3):**
```tsx
import { TruckIcon } from "@architecture-it/stylesystem";

<TruckIcon primaryColor="var(--primary)" />
```

`@fortawesome/fontawesome-svg-core` and `@fortawesome/pro-regular-svg-icons` are **no longer** required peer dependencies.
