# Form Controls

**Imports:**
```tsx
import {
  Checkbox,
  Radio,
  Switch,
  Pills,
  Search,
  InputQuantity,
  ListControl,
} from "@architecture-it/stylesystem";
```

---

## Checkbox

Standard checkbox extending MUI `Checkbox` + `FormControlLabel`.

### Checkbox Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `label` | `string \| ReactNode` | | Label text next to checkbox |
| `checked` | `boolean` | | Controlled checked state |
| `onChange` | `(event, checked: boolean) => void` | | Change handler |
| `disabled` | `boolean` | | Disables the control |
| `indeterminate` | `boolean` | | Shows indeterminate (−) state |
| `color` | `"primary" \| "secondary" \| "default"` | `"primary"` | Checkbox color |
| `classes` | `{ root?, label? }` | | CSS slot overrides |

### Checkbox Usage

```tsx
// Uncontrolled
<Checkbox label="Acepto los términos y condiciones" />

// Controlled
const [checked, setChecked] = React.useState(false);
<Checkbox
  label="Enviarme novedades"
  checked={checked}
  onChange={(_, val) => setChecked(val)}
/>

// Indeterminate (select-all pattern)
<Checkbox
  label="Seleccionar todos"
  checked={allSelected}
  indeterminate={someSelected && !allSelected}
  onChange={(_, val) => toggleAll(val)}
/>
```

#### React Hook Form

```tsx
import { Controller } from "react-hook-form";

<Controller
  name="terms"
  control={control}
  rules={{ required: "Debés aceptar los términos" }}
  render={({ field }) => (
    <Checkbox
      label="Acepto los términos"
      checked={field.value}
      onChange={(_, val) => field.onChange(val)}
    />
  )}
/>
```

---

## Radio

Radio button. Use with MUI `RadioGroup` + `FormControlLabel` to create groups.

### Radio Props

| Prop | Type | Description |
|------|------|-------------|
| `value` | `string \| number` | Value of this radio option |
| `label` | `string` | Label text (when used as standalone `FormControlLabel`) |
| `disabled` | `boolean` | Disables this option |
| `color` | `"primary" \| "secondary"` | Accent color |

### Radio Group Usage

```tsx
import { Radio } from "@architecture-it/stylesystem";
import { RadioGroup, FormControlLabel, FormControl, FormLabel } from "@mui/material";

const [value, setValue] = React.useState("express");

<FormControl>
  <FormLabel>Tipo de envío</FormLabel>
  <RadioGroup value={value} onChange={(e) => setValue(e.target.value)}>
    <FormControlLabel value="express" label="Express" control={<Radio />} />
    <FormControlLabel value="standard" label="Estándar" control={<Radio />} />
    <FormControlLabel value="economy" label="Económico" control={<Radio />} disabled />
  </RadioGroup>
</FormControl>
```

#### React Hook Form

```tsx
<Controller
  name="deliveryType"
  control={control}
  render={({ field }) => (
    <RadioGroup {...field}>
      <FormControlLabel value="express" label="Express" control={<Radio />} />
      <FormControlLabel value="standard" label="Estándar" control={<Radio />} />
    </RadioGroup>
  )}
/>
```

---

## Switch

Toggle control extending MUI `Switch` + `FormControlLabel`.

### Switch Props

| Prop | Type | Description |
|------|------|-------------|
| `label` | `string` | Label next to the switch |
| `checked` | `boolean` | Controlled state |
| `onChange` | `(event, checked: boolean) => void` | Change handler |
| `disabled` | `boolean` | Disables the control |
| `color` | `"primary" \| "secondary"` | Accent color |

### Switch Usage

```tsx
const [enabled, setEnabled] = React.useState(false);

<Switch
  label="Notificaciones por email"
  checked={enabled}
  onChange={(_, val) => setEnabled(val)}
/>

// Settings list pattern:
const settings = [
  { id: "email", label: "Email" },
  { id: "sms", label: "SMS" },
  { id: "push", label: "Push notifications" },
];
const [enabled, setEnabled] = React.useState<Record<string, boolean>>({});

{settings.map((s) => (
  <Switch
    key={s.id}
    label={s.label}
    checked={enabled[s.id] ?? false}
    onChange={(_, val) => setEnabled((prev) => ({ ...prev, [s.id]: val }))}
  />
))}
```

---

## Pills

Status badge / tag component.

### Pills Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `text` | `string` | ✅ | Badge label |
| `variant` | `"info" \| "success" \| "error" \| "warning" \| "default"` | ✅ | Color scheme |
| `size` | `"large" \| "medium" \| "small"` | ✅ | Size variant |
| `icon` | `ReactElement` | | Icon before text |
| `width` | `string \| number` | | Custom width |

### Pills Usage

```tsx
// Status indicators
<Pills text="Entregado" variant="success" size="medium" />
<Pills text="En tránsito" variant="info" size="medium" />
<Pills text="Demorado" variant="warning" size="medium" />
<Pills text="Error" variant="error" size="medium" />
<Pills text="Pendiente" variant="default" size="small" />

// With icon
<Pills
  text="Nuevo"
  variant="info"
  size="large"
  icon={<StarIcon primaryColor="var(--c-color-icon-info)" width={14} />}
/>

// In a table cell
<TableCell>
  <Pills text={row.status} variant={statusVariantMap[row.status]} size="small" />
</TableCell>
```

---

## Search

Standalone search input with submit button and clear action.

### Search Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `size` | `"small" \| "default" \| "large"` | `"default"` | Input size |
| `variant` | `"primary" \| "secondary"` | `"primary"` | Style variant |
| `placeholder` | `string` | | Placeholder text |
| `value` | `string` | | Controlled value |
| `onChange` | `(event) => void` | | Input change handler |
| `onClick` | `() => void` | | Submit/search button handler |
| `onClear` | `() => void` | | Clear (✕) button handler |
| `buttonId` | `string` | | HTML id for the search button |
| `disabled` | `boolean` | | Disables the control |

### Search Usage

```tsx
const [query, setQuery] = React.useState("");
const [results, setResults] = React.useState([]);

const handleSearch = async () => {
  const data = await searchAPI(query);
  setResults(data);
};

<Search
  value={query}
  onChange={(e) => setQuery(e.target.value)}
  onClick={handleSearch}
  onClear={() => { setQuery(""); setResults([]); }}
  placeholder="Buscar por número de guía..."
/>
```

---

## InputQuantity

Number input with increment/decrement buttons (+/−). Useful for quantity selectors.

### InputQuantity Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` | `number` | | Controlled value |
| `onChange` | `(value: number) => void` | | Change handler |
| `min` | `number` | `0` | Minimum value |
| `max` | `number` | | Maximum value |
| `step` | `number` | `1` | Increment/decrement step |
| `disabled` | `boolean` | | Disables the control |
| `label` | `string` | | Label text above the input |

### InputQuantity Usage

```tsx
const [qty, setQty] = React.useState(1);

<InputQuantity
  label="Cantidad"
  value={qty}
  onChange={setQty}
  min={1}
  max={99}
/>
```

---

## ListControl

Checkbox list with built-in select-all support.

### ListControl Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `items` | `ListItem[]` | ✅ | Checkbox item definitions |
| `onChange` | `(selected: string[]) => void` | ✅ | Called with array of selected values |
| `value` | `string[]` | | Controlled selected values |
| `selectAll` | `boolean` | | Show a "select all" checkbox at top |
| `classes` | `{ root?, item? }` | | CSS slot overrides |

### `ListItem` shape

```ts
interface ListItem {
  value: string;
  label: string;
  disabled?: boolean;
}
```

### ListControl Usage

```tsx
const [selected, setSelected] = React.useState<string[]>([]);

<ListControl
  selectAll
  value={selected}
  onChange={setSelected}
  items={[
    { value: "email", label: "Email" },
    { value: "sms", label: "SMS" },
    { value: "push", label: "Push notifications" },
    { value: "whatsapp", label: "WhatsApp", disabled: true },
  ]}
/>
```
