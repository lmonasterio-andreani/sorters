# Select

**Import:** `import { Select } from "@architecture-it/stylesystem";`  
**Type:** `import type { SelectProps } from "@architecture-it/stylesystem";`

Wraps MUI `Select` inside a `FormControl` with custom styling. Supports single-select, multi-select with chips display, and multi-select with checkbox display. Always import `MenuItem` from `@mui/material`.

## Props

Extends MUI `SelectProps` (omits `variant`, `classes`, `size`):

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `label` | `string` | — | Floating label |
| `dark` | `boolean` | — | Dark variant |
| `helperText` | `string` | — | Text below the select |
| `size` | `"small" \| "large"` | — | Field height |
| `display` | `"default" \| "chips" \| "checkbox"` | `"default"` | How multi-selections are shown |
| `multiple` | `boolean` | — | Enables multi-select mode |
| `inputLabelProps` | `InputLabelProps` | `{}` | Label element props |
| `classes` | `{ formControl?, select? }` | — | CSS overrides |
| `error` | `boolean` | — | Error state |
| `required` | `boolean` | — | Marks field required |
| `disabled` | `boolean` | — | Disables select |
| `fullWidth` | `boolean` | — | 100% width |
| `value` | `string \| string[]` | — | Controlled value |
| `onChange` | `SelectChangeEvent handler` | — | Change handler |
| `displayEmpty` | `boolean` | — | Show empty option |
| `ref` | `ref` | — | Forwarded ref |

## Deselect Pattern

A selected item can be deselected by clicking it again. This requires explicit `onClick` handling on `MenuItem`:

```tsx
<MenuItem
  value={opt}
  onClick={(e) => {
    if (value === opt) {
      e.preventDefault();
      e.stopPropagation();
      setValue("");
    }
  }}
  onKeyDown={(e) => {
    if ((e.key === "Enter" || e.key === " ") && value === opt) {
      e.preventDefault();
      e.stopPropagation();
      setValue("");
    }
  }}
>
  {opt}
</MenuItem>
```

## Usage Examples

### Basic single select

```tsx
import MenuItem from "@mui/material/MenuItem";

const [value, setValue] = React.useState("");

<Select
  label="¿Qué querés enviar?"
  value={value}
  size="large"
  displayEmpty
  onChange={(e) => setValue(e.target.value as string)}
>
  {["Encomienda 1", "Encomienda 2", "Encomienda 3"].map((opt) => (
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
```

### With error and helper text

```tsx
<Select
  label="Colores"
  value={value}
  error
  helperText="Seleccioná una opción"
  onChange={(e) => setValue(e.target.value as string)}
>
  <MenuItem value="Rojo">Rojo</MenuItem>
  <MenuItem value="Azul">Azul</MenuItem>
</Select>
```

### Multi-select with chips

```tsx
const [value, setValue] = React.useState<string[]>([]);

<Select
  multiple
  display="chips"
  label="¿Qué querés enviar?"
  size="large"
  value={value}
  onChange={(e) => setValue(e.target.value as string[])}
>
  <MenuItem value="Rojo">Rojo</MenuItem>
  <MenuItem value="Blanco">Blanco</MenuItem>
  <MenuItem value="Azul">Azul</MenuItem>
  <MenuItem value="Verde">Verde</MenuItem>
</Select>
```

### Multi-select with checkboxes

```tsx
const [value, setValue] = React.useState<string[]>([]);

<Select
  multiple
  display="checkbox"
  label="Colores"
  size="large"
  value={value}
  onChange={(e) => setValue(e.target.value as string[])}
>
  <MenuItem value="Rojo">Rojo</MenuItem>
  <MenuItem value="Blanco">Blanco</MenuItem>
  <MenuItem value="Azul">Azul</MenuItem>
</Select>
```

### With React Hook Form (Controller pattern)

```tsx
import { Controller, useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as yup from "yup";
import MenuItem from "@mui/material/MenuItem";

const schema = yup.object({ colors: yup.string().required("* Campo requerido") });
const { control, setValue, handleSubmit, formState: { errors } } = useForm({ resolver: yupResolver(schema) });

<form onSubmit={handleSubmit(onSubmit)}>
  <Controller
    control={control}
    defaultValue=""
    name="colors"
    render={({ field }) => (
      <Select
        label="¿Qué querés enviar?"
        value={field.value}
        size="large"
        error={Boolean(errors.colors)}
        helperText={errors.colors?.message ?? " "}
        onBlur={field.onBlur}
        onChange={(e) => {
          const next = e.target.value as string;
          // deselect pattern
          const toggled = next === field.value ? "" : next;
          field.onChange(toggled);
          setValue("colors", toggled, { shouldValidate: true });
        }}
      >
        {["Rojo", "Blanco", "Azul"].map((opt) => (
          <MenuItem
            key={opt}
            value={opt}
            onClick={(e) => {
              if (field.value === opt) {
                e.preventDefault(); e.stopPropagation();
                field.onChange(""); setValue("colors", "", { shouldValidate: true });
              }
            }}
          >
            {opt}
          </MenuItem>
        ))}
      </Select>
    )}
  />
  <Button text="Enviar" type="submit" variant="contained" />
</form>
```

### With Formik

```tsx
import { useFormik } from "formik";
import MenuItem from "@mui/material/MenuItem";

const formik = useFormik({
  initialValues: { color: "" },
  validationSchema: yup.object({ color: yup.string().required("* Campo requerido") }),
  onSubmit: (values) => console.log(values),
});

<form onSubmit={formik.handleSubmit}>
  <Select
    label="¿Qué querés enviar?"
    name="color"
    value={formik.values.color}
    size="large"
    helperText={formik.touched.color ? formik.errors.color : ""}
    onBlur={formik.handleBlur}
    onChange={formik.handleChange}
  >
    {["Rojo", "Blanco", "Azul"].map((opt) => (
      <MenuItem
        key={opt}
        value={opt}
        onClick={(e) => {
          if (formik.values.color === opt) {
            e.preventDefault(); e.stopPropagation();
            formik.setFieldTouched("color", true, true);
            formik.setFieldValue("color", "", true);
          }
        }}
      >
        {opt}
      </MenuItem>
    ))}
  </Select>
  <Button text="Enviar" type="submit" variant="contained" />
</form>
```

## Notes

- `Select` always uses `variant="outlined"` internally — do not attempt to override this.
- For multi-select `display="chips"`, individual chips can be deleted by the user; the delete action triggers `onChange` with the filtered array.
- The dropdown arrow icon is always `ChevronDownIcon` from the library — it cannot be replaced via props.
- `MenuProps.disablePortal = true` is hardcoded, meaning the dropdown renders inside the component tree, not in a portal.
