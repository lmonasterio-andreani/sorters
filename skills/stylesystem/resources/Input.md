# Input

**Import:** `import { Input } from "@architecture-it/stylesystem";`  
**Type:** `import type { InputProps } from "@architecture-it/stylesystem";`

A styled form input that wraps MUI `InputBase` inside a `FormControl`. Handles label, helper text, error state, tooltip, optional indicator, dark mode, and an inline checkbox pattern.

## Props

Extends MUI `InputBaseProps` with additional props:

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `label` | `string` | — | Floating label above the field |
| `helperText` | `string` | — | Hint or error text below the field |
| `dark` | `boolean` | `false` | Dark background styling |
| `optional` | `boolean` | `false` | Appends *(opcional)* to the label |
| `tooltip` | `MUI TooltipProps` | — | Shows a `?` icon with tooltip on the label |
| `checkbox` | `{ text: string, checked?: boolean, onChange?: (e) => void, disabled?: boolean }` | — | Inline checkbox that disables the input when checked |
| `inputLabelProps` | `MUI InputLabelProps` | `{}` | Forwarded to the label element |
| `classes` | `{ formControl?, label?, input?, helperText? }` | — | CSS class overrides per slot |
| `error` | `boolean` | — | Shows error color and error icon |
| `required` | `boolean` | — | Marks field required |
| `disabled` | `boolean` | — | Disables the field |
| `multiline` | `boolean` | — | Makes the field a textarea |
| `value` | `string` | — | Controlled value |
| `onChange` | `ChangeEventHandler` | — | Change handler |
| `placeholder` | `string` | — | Placeholder text |
| `type` | `string` | — | HTML input type  |
| `fullWidth` | `boolean` | — | 100% container width |
| `endAdornment` | `ReactNode` | — | Element at the end of the input |
| `id` | `string` | `"input-stylesystem"` | Input/label id |
| `ref` | `ref` | — | Forwarded to the inner input element |

## Usage Examples

### Basic input

```tsx
<Input label="Nombre" />
```

### Required with helper text

```tsx
<Input label="Nombre" required helperText="Debe ingresar un nombre" />
```

### With error state

```tsx
<Input label="Nombre" error helperText="Este campo es requerido" />
```

### Optional field

```tsx
<Input label="Nombre" optional />
// renders: "Nombre (opcional)"
```

### With tooltip

```tsx
<Input label="Nombre" tooltip={{ title: "Ingresá tu nombre completo tal como figura en tu DNI" }} />
```

### Disabled

```tsx
<Input label="Nombre" disabled value="Pedro Pérez" />
```

### Textarea (multiline)

```tsx
<Input
  label="Comentarios"
  multiline
  fullWidth
  placeholder="Introduce acá tus comentarios"
/>
```

### Dark background (e.g., on dark header)

```tsx
<Input label="Búsqueda" dark />
```

### With end icon adornment

```tsx
<Input
  placeholder="Buscar envíos, acciones o lo que necesitas"
  endAdornment={<SearchIcon />}
  classes={{ formControl: styles.searchInput }}
/>
```

### Inline checkbox ("sin número")

```tsx
const [value, setValue] = React.useState("");

<Input
  label="Dirección"
  checkbox={{ text: "Sin número" }}
  value={value}
  onChange={(e) => setValue(e.target.value)}
/>
// When checkbox is checked, the input becomes disabled
```

### With React Hook Form

```tsx
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as yup from "yup";

const schema = yup.object({
  name: yup.string().required("Campo requerido"),
  email: yup.string().email("Formato inválido").required("Campo requerido"),
});

const { register, handleSubmit, formState: { errors } } = useForm({ resolver: yupResolver(schema) });

<form onSubmit={handleSubmit(onSubmit)}>
  <Input
    label="Nombre"
    placeholder="Nombre"
    {...register("name")}
    error={Boolean(errors.name)}
    helperText={errors.name?.message}
  />
  <Input
    label="Email"
    type="email"
    placeholder="Email"
    {...register("email")}
    error={Boolean(errors.email)}
    helperText={errors.email?.message}
  />
  <Button text="Enviar" type="submit" variant="contained" />
</form>
```

### With Formik

```tsx
import { useFormik } from "formik";

const formik = useFormik({
  initialValues: { name: "", email: "" },
  validationSchema: schema,
  onSubmit: (values) => console.log(values),
});

<form onSubmit={formik.handleSubmit}>
  <Input
    label="Nombre"
    name="name"
    value={formik.values.name}
    onChange={formik.handleChange}
    error={formik.touched.name && Boolean(formik.errors.name)}
    helperText={formik.touched.name ? formik.errors.name : ""}
  />
  <Input
    label="Email"
    name="email"
    type="email"
    value={formik.values.email}
    onChange={formik.handleChange}
    error={formik.touched.email && Boolean(formik.errors.email)}
    helperText={formik.touched.email ? formik.errors.email : ""}
  />
  <Button text="Enviar" type="submit" variant="contained" />
</form>
```

## CSS Class Slots

```tsx
<Input
  label="Nombre"
  classes={{
    formControl: styles.myFormControl,   // wrapping FormControl
    label: styles.myLabel,               // InputLabel
    input: styles.myInput,               // InputBase
    helperText: styles.myHelperText,     // FormHelperText below
  }}
/>
```

## Important Behavior Notes

- The `ref` is forwarded to the underlying `<input>` element — works with React Hook Form's `register`.
- When `checkbox` prop is provided: by default, checking the checkbox disables the input. If `checkbox.checked` is controlled externally, provide `checkbox.onChange`.
- `helperText` is rendered **outside** the `FormControl` (in a separate `FormHelperText` below). This means it has no visual gap issues.
- `error` state shows an `✕` icon at the right side of the input automatically.
