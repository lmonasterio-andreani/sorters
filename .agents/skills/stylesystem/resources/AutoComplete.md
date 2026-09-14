# AutoComplete

**Import:** `import { AutoComplete } from "@architecture-it/stylesystem";`  
**Type:** `import type { AutoCompleteProps } from "@architecture-it/stylesystem";`

Extends MUI `Autocomplete` with a custom `Option` type supporting descriptions, groups, and secondary text. Styled to match the design system tokens.

## Props

Extends MUI `AutocompleteProps<Option, Multiple, DisableClearable, FreeSolo>`:

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `options` | `Option[]` | ✅ | Available options |
| `label` | `{ text: string; icon?: ReactElement }` | | Text field label with optional prefix icon |
| `placeholder` | `string` | | Input placeholder |
| `textfieldprops` | `TextFieldProps` | | Forwarded to the internal `TextField` (error, helperText, etc.) |
| `classesprop` | `string` | | Extra CSS class on the root |
| `multiple` | `boolean` | | Allow multi-select |
| `loading` | `boolean` | | Shows loading spinner in the dropdown |
| `disabled` | `boolean` | | Disables the whole control |
| `onChange` | `(event, value: Option \| Option[] \| null) => void` | | Change handler |
| `value` | `Option \| Option[] \| null` | | Controlled value |

### `Option` shape

```ts
interface Option {
  value: string;           // ✅ Required — unique identifier
  title?: string;          // Primary display text
  description?: string;    // Secondary line in the dropdown item
  group?: string;          // Groups options under headers
  secondaryText?: string;  // Trailing text (right-aligned) in the item
}
```

> If `title` is omitted, `value` is used as the display string.

## Usage Examples

### Basic single select

```tsx
import { AutoComplete } from "@architecture-it/stylesystem";

const options = [
  { value: "1", title: "Envío estándar" },
  { value: "2", title: "Envío express" },
  { value: "3", title: "Envío económico" },
];

<AutoComplete
  options={options}
  label={{ text: "Tipo de envío" }}
  placeholder="Seleccioná una opción"
  onChange={(_, value) => console.log(value)}
/>
```

### With description and secondary text

```tsx
const options = [
  {
    value: "suc-1",
    title: "Sucursal Palermo",
    description: "Av. Santa Fe 2345, Buenos Aires",
    secondaryText: "8 km",
  },
  {
    value: "suc-2",
    title: "Sucursal Belgrano",
    description: "Av. Cabildo 1234, Buenos Aires",
    secondaryText: "12 km",
  },
];

<AutoComplete
  options={options}
  label={{ text: "Sucursal más cercana" }}
  placeholder="Buscá por nombre o dirección"
/>
```

### Grouped options

```tsx
const options = [
  { value: "ar-ba", title: "Buenos Aires", group: "Argentina" },
  { value: "ar-cor", title: "Córdoba", group: "Argentina" },
  { value: "uy-mvd", title: "Montevideo", group: "Uruguay" },
];

<AutoComplete
  options={options}
  label={{ text: "Ciudad" }}
  groupBy={(opt) => opt.group ?? ""}
/>
```

### With label icon

```tsx
<AutoComplete
  options={options}
  label={{ text: "Destinatario", icon: <UserIcon primaryColor="var(--primary)" /> }}
  placeholder="Buscar cliente"
/>
```

### Error state with helper text

```tsx
<AutoComplete
  options={options}
  label={{ text: "Código postal" }}
  textfieldprops={{
    error: !!errors.postalCode,
    helperText: errors.postalCode?.message,
  }}
/>
```

### React Hook Form integration

```tsx
import { Controller } from "react-hook-form";

<Controller
  name="service"
  control={control}
  rules={{ required: "Seleccioná un servicio" }}
  render={({ field, fieldState }) => (
    <AutoComplete
      options={serviceOptions}
      label={{ text: "Servicio" }}
      value={serviceOptions.find((o) => o.value === field.value) ?? null}
      onChange={(_, opt) => field.onChange(opt?.value ?? null)}
      textfieldprops={{
        error: !!fieldState.error,
        helperText: fieldState.error?.message,
      }}
    />
  )}
/>
```

### Multi-select

```tsx
const [selected, setSelected] = React.useState<Option[]>([]);

<AutoComplete
  multiple
  options={options}
  label={{ text: "Zonas de cobertura" }}
  value={selected}
  onChange={(_, value) => setSelected(value as Option[])}
/>
```

### Async options with loading state

```tsx
const [input, setInput] = React.useState("");
const [options, setOptions] = React.useState<Option[]>([]);
const [loading, setLoading] = React.useState(false);

const handleInputChange = async (_: unknown, value: string) => {
  setInput(value);
  setLoading(true);
  const results = await searchAPI(value);
  setOptions(results.map((r) => ({ value: r.id, title: r.name })));
  setLoading(false);
};

<AutoComplete
  options={options}
  loading={loading}
  label={{ text: "Buscar producto" }}
  onInputChange={handleInputChange}
  filterOptions={(x) => x} // disable client-side filtering for server search
/>
```

## Notes

- `AutoComplete` filters by `title` (falls back to `value`) by default.
- For server-side search, pass `filterOptions={(x) => x}` to disable client filtering.
- When used with `react-hook-form`, store the `value` string (not the full `Option`) in the form, and look up the matching option in `value` prop.
- `textfieldprops` is the main escape hatch for validation states, adornments, sizes, etc.
