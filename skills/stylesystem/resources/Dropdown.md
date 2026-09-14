# Dropdown

**Import:** `import { Dropdown } from "@architecture-it/stylesystem";`  
**Type:** `import type { DropdownProps } from "@architecture-it/stylesystem";`

Collapsible accordion-style section. Uses MUI `Collapse` for animation. Useful for FAQ sections, expandable menu items, or grouped content.

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `title` | `string` | — | **Required.** Accordion header label |
| `children` | `ReactNode` | | Content revealed when expanded |
| `toggleOnTitle` | `boolean` | `true` | If `true`, clicking the title text also toggles open/closed |
| `initialState` | `boolean` | `false` | Start expanded |
| `startIcon` | `ReactElement` | | Icon shown left of the title |
| `typographyProps` | `TypographyProps` | | MUI Typography props for the title text |
| `unmountOnExit` | `boolean` | `true` | If `true`, children are unmounted when collapsed |
| `id` | `string` | | HTML `id` for the container |
| `onClick` | `() => void` | | Extra callback on toggle |
| `classes` | `{ root?, header?, title?, icon?, content? }` | | CSS slot overrides |

## Usage Examples

### Basic FAQ accordion

```tsx
import { Dropdown } from "@architecture-it/stylesystem";

<Dropdown title="¿Cuánto tarda mi envío?">
  <Typography variant="body2" color="secondary">
    Los envíos estándar demoran entre 3 y 5 días hábiles. Los envíos express
    llegan al día siguiente antes de las 10 AM.
  </Typography>
</Dropdown>
```

### Start open by default

```tsx
<Dropdown title="Preguntas frecuentes" initialState={true}>
  <Typography>Aquí encontrarás las respuestas más comunes...</Typography>
</Dropdown>
```

### With start icon

```tsx
import { HelpIcon } from "@architecture-it/stylesystem";

<Dropdown
  title="Soporte"
  startIcon={<HelpIcon primaryColor="var(--primary)" />}
>
  <NavbarItem text="Base de conocimiento" href="/docs" />
  <NavbarItem text="Reportar un problema" href="/issues" />
  <NavbarItem text="Contactar soporte" href="/soporte" />
</Dropdown>
```

### List of links inside Dropdown (menu-style)

```tsx
<Dropdown title="Mis envíos" startIcon={<TruckIcon />}>
  <NavbarItem text="Envíos activos" href="/envios/activos" />
  <NavbarItem text="Historial" href="/envios/historial" />
  <NavbarItem text="Programados" href="/envios/programados" />
</Dropdown>
```

### FAQ list (multiple dropdowns)

```tsx
const faqs = [
  {
    question: "¿Puedo cambiar el destinatario?",
    answer: "Sí, podés modificarlo hasta que el envío sea despachado.",
  },
  {
    question: "¿Cómo hago el seguimiento?",
    answer: "Ingresá tu número de tracking en el portal de seguimiento.",
  },
];

{faqs.map((faq, i) => (
  <Dropdown key={i} title={faq.question}>
    <Typography variant="body2" color="secondary">{faq.answer}</Typography>
  </Dropdown>
))}
```

### Controlled externally

Dropdown has no exposed `open` prop — use `initialState` for initial state. For full external control, use the `onClick` callback and conditional rendering:

```tsx
const [expanded, setExpanded] = React.useState(false);

<Dropdown
  title="Filtros avanzados"
  initialState={expanded}
  onClick={() => setExpanded((prev) => !prev)}
>
  {/* filter form */}
</Dropdown>
```

### Header nav with Dropdown

```tsx
<Header onClickButton={handleSidebarOpen}>
  <Dropdown
    title="Mis servicios"
    typographyProps={{ variant: "body2", fontWeight: 600 }}
  >
    <NavbarItem text="Correo" href="/correo" />
    <NavbarItem text="Encomiendas" href="/encomiendas" />
  </Dropdown>
</Header>
```

## Notes

- `unmountOnExit={true}` (default) means children are destroyed when collapsed — useful for form resets or lazy data loading.
- Set `unmountOnExit={false}` if you need children to retain state between collapses.
- `toggleOnTitle={false}` means only the chevron icon toggles the accordion. Use when the title itself should be a link.
- For nested Dropdowns, each manages its own open state independently.
