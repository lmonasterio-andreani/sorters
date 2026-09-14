# Cards

**Imports:**
```tsx
import { Card, CardButton } from "@architecture-it/stylesystem";
import {
  CardSkeleton,
  DescriptionCardSkeleton,
  MainCardSkeleton,
  ContentSkeleton,
} from "@architecture-it/stylesystem";
```

## Card

Flexible MUI-based card with three slots: media (image/icon/SVG), content, and actions.

### Card Props

| Prop | Type | Description |
|------|------|-------------|
| `cardMediaIcon` | `ImgHTMLAttributes<HTMLImageElement> \| { icon: ReactElement }` | Media slot: pass img props or `{ icon: <MyComponent /> }` for a React element |
| `cardContent` | `ReactNode` | Main body of the card |
| `cardActions` | `ReactNode` | Bottom actions slot (buttons, links) |
| `containerGridProps` | `GridProps` | MUI Grid props applied to the outer container |
| `classes` | `{ root?, media?, content?, actions? }` | CSS slot overrides |

### Card Usage Examples

#### Base card with image

```tsx
import { Card } from "@architecture-it/stylesystem";

<Card
  cardMediaIcon={{ src: "/images/envio.png", alt: "envío", height: 80, width: 80 }}
  cardContent={
    <Box>
      <Typography variant="h6">Envío estándar</Typography>
      <Typography variant="body2" color="secondary">
        Entrega en 3 a 5 días hábiles.
      </Typography>
    </Box>
  }
  cardActions={
    <Button text="Ver detalle" variant="outlined" size="small" />
  }
/>
```

#### Card with SVG / ReactElement icon

```tsx
<Card
  cardMediaIcon={{ icon: () => <TruckIcon width={64} height={64} primaryColor="var(--primary)" /> }}
  cardContent={
    <DescriptionItem
      title="Seguimiento"
      description="Rastreá tu paquete en tiempo real."
    />
  }
  cardActions={
    <Button text="Rastrear" variant="contained" size="small" />
  }
/>
```

#### Main card (prominent, full-width)

```tsx
<Card
  containerGridProps={{ xs: 12 }}
  cardContent={
    <Typography variant="h5" fontWeight={600}>
      Panel de control
    </Typography>
  }
/>
```

---

## CardButton

A clickable card styled as a large button. Used for navigation tiles or feature selection screens.

### CardButton Props

| Prop | Type | Description |
|------|------|-------------|
| `title` | `string` | Card label |
| `description` | `string` | Secondary text |
| `icon` | `ReactElement` | Icon displayed in the card |
| `onClick` | `() => void` | Click handler (makes the entire card clickable) |
| `active` | `boolean` | Highlights card as selected (checked state) |
| `disabled` | `boolean` | Disables the card |
| `classes` | `{ root?, icon?, text?, active? }` | CSS slot overrides |

### CardButton Usage Examples

```tsx
const [selected, setSelected] = React.useState<string | null>(null);

const options = [
  { id: "express", title: "Express", description: "Entrega en 24 hs", icon: <BoltIcon /> },
  { id: "standard", title: "Estándar", description: "3-5 días hábiles", icon: <TruckIcon /> },
];

{options.map((opt) => (
  <CardButton
    key={opt.id}
    title={opt.title}
    description={opt.description}
    icon={opt.icon}
    active={selected === opt.id}
    onClick={() => setSelected(opt.id)}
  />
))}
```

---

## Card Skeletons

Loading placeholder variants. Each skeleton matches the visual layout of the corresponding card type.

### Available Skeletons

| Component | Use case |
|-----------|----------|
| `CardSkeleton` | Matches `Card` layout (media + content + actions) |
| `DescriptionCardSkeleton` | Card with a title + description body |
| `MainCardSkeleton` | Large prominent card variant |
| `ContentSkeleton` | Generic content block skeleton |

### Props (all skeletons)

| Prop | Type | Description |
|------|------|-------------|
| `className` | `string` | Extra CSS class |
| `classes` | `{ root?, ... }` | CSS slot overrides |

### Skeleton Usage Example

```tsx
import { CardSkeleton, DescriptionCardSkeleton } from "@architecture-it/stylesystem";

// Show while loading
{loading ? (
  <Grid container spacing={2}>
    {Array.from({ length: 3 }).map((_, i) => (
      <Grid item xs={12} md={4} key={i}>
        <CardSkeleton />
      </Grid>
    ))}
  </Grid>
) : (
  cards.map((card) => <Card key={card.id} {...card} />)
)}
```

## Notes

- `cardMediaIcon` accepts either standard HTML `<img>` props or `{ icon: ReactElement }` — not both.
- `CardButton` is typically used in a grid for feature selection (e.g., "choose delivery type").
- Place skeletons at the same Grid hierarchy level as the real cards they replace.
