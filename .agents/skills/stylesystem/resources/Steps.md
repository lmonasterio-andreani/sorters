# Steps Components

**Imports:**
```tsx
import { HorizontalSteps } from "@architecture-it/stylesystem";
import { VerticalSteps } from "@architecture-it/stylesystem";
import { InfoSteps } from "@architecture-it/stylesystem";
```

Three distinct step/timeline components for different UX patterns: wizard progress (horizontal), history/timeline (vertical), and informational guides (with images or enum).

---

## HorizontalSteps

Progress stepper for wizard/multi-step flows. Shows numbered steps with active/completed states.

### HorizontalSteps Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `steps` | `string[]` | ✅ | Step label text array |
| `activeSteps` | `number` | ✅ | Index of the current active step (0-based) |
| `primaryColor` | `string` | | Custom color for active step circle |
| `secondaryColor` | `string` | | Custom color for inactive/completed steps |
| `classes` | `{ root?, step?, label? }` | | CSS slot overrides |

### HorizontalSteps Usage

```tsx
import { HorizontalSteps } from "@architecture-it/stylesystem";

const steps = ["Datos del envío", "Información del paquete", "Confirmación"];
const [activeStep, setActiveStep] = React.useState(0);

<HorizontalSteps steps={steps} activeSteps={activeStep} />

// Navigation buttons:
<Button
  text="Anterior"
  variant="outlined"
  disabled={activeStep === 0}
  onClick={() => setActiveStep((s) => s - 1)}
/>
<Button
  text={activeStep === steps.length - 1 ? "Finalizar" : "Siguiente"}
  variant="contained"
  onClick={() => setActiveStep((s) => Math.min(s + 1, steps.length - 1))}
/>
```

With custom colors:

```tsx
<HorizontalSteps
  steps={["Paso 1", "Paso 2", "Paso 3"]}
  activeSteps={1}
  primaryColor="var(--secondary-green)"
  secondaryColor="var(--c-color-border-subtle)"
/>
```

---

## VerticalSteps

Timeline-style component. Each step can have a date, time, description, and rich content.

### VerticalSteps Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `steps` | `VerticalStep[]` | ✅ | Step definitions |
| `activeStep` | `number` | ✅ | Index of the highlighted/current step (0-based) |
| `primaryColor` | `string` | | Color for the active step indicator |
| `secondaryColor` | `string` | | Color for inactive step indicators |

### `VerticalStep` shape

```ts
interface VerticalStep {
  label: string;         // Main text (event name / status)
  date?: string;         // Date string shown next to label
  time?: string;         // Time string
  description?: string;  // Secondary text below label
  content?: ReactNode;   // Rich content slot (e.g., address, inner details)
}
```

### VerticalSteps Usage

```tsx
import { VerticalSteps } from "@architecture-it/stylesystem";

const steps = [
  {
    label: "Envío despachado",
    date: "12/01/2025",
    time: "09:30",
    description: "El paquete fue retirado por el transportista.",
  },
  {
    label: "En centro de distribución",
    date: "13/01/2025",
    time: "14:00",
    description: "Recibido en CABA.",
  },
  {
    label: "En camino al destino",
    date: "14/01/2025",
    time: "08:00",
    content: (
      <Typography variant="caption" color="secondary">
        Repartidor: Carlos G. — Tel: 11-1234-5678
      </Typography>
    ),
  },
  {
    label: "Entregado",
    date: "14/01/2025",
    time: "11:15",
  },
];

<VerticalSteps steps={steps} activeStep={2} />
```

---

## InfoSteps

Instructional step list. Supports two modes: `"enum"` (numbered) and `"images"` (with accompanying images).

### InfoSteps Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `steps` | `InfoStep[]` | ✅ | Step definitions |
| `mode` | `"enum" \| "images"` | `"enum"` | Layout mode |
| `classes` | `{ root?, step?, number?, image?, text? }` | | CSS slot overrides |

### `InfoStep` shape

```ts
interface InfoStep {
  label: string;                          // Step instruction text
  imgProps?: ImgHTMLAttributes<HTMLImageElement>;  // Image (required for "images" mode)
}
```

### InfoSteps Usage

Enum (numbered) mode:

```tsx
import { InfoSteps } from "@architecture-it/stylesystem";

<InfoSteps
  mode="enum"
  steps={[
    { label: "Descargá la app en tu celular." },
    { label: "Registrate con tu email y contraseña." },
    { label: "Completá tus datos personales." },
    { label: "¡Comenzá a enviar!" },
  ]}
/>
```

Images mode:

```tsx
<InfoSteps
  mode="images"
  steps={[
    {
      label: "Ingresá el código de tu envío.",
      imgProps: { src: "/guide/step1.svg", alt: "paso 1", width: 80, height: 80 },
    },
    {
      label: "Seleccioná el punto de entrega más cercano.",
      imgProps: { src: "/guide/step2.svg", alt: "paso 2", width: 80, height: 80 },
    },
    {
      label: "Confirmá y recibí en tu domicilio.",
      imgProps: { src: "/guide/step3.svg", alt: "paso 3", width: 80, height: 80 },
    },
  ]}
/>
```

## Notes

- `HorizontalSteps` is for form wizard navigation — track `activeStep` with local state.
- `VerticalSteps` suits tracking history, audit logs, or order timelines.
- `InfoSteps` is best for onboarding, help guides, or feature explanations.
- `activeStep` in `VerticalSteps` renders that step with the primary color highlight.
- For `InfoSteps mode="images"`, each `imgProps` is applied to an `<img>` element — `alt` is required for accessibility.
