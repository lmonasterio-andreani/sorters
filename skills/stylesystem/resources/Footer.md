# Footer

**Import:** `import { Footer, FooterList } from "@architecture-it/stylesystem";`

Application footer available in two layout modes via the `variant` prop.

## Footer Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `variant` | `"internal" \| "institutional"` | `"internal"` | Layout style (see below) |
| `logo` | `ReactElement` | | Custom logo element |
| `sections` | `FooterSection[]` | | Column groups of links |
| `references` | `ReactNode` | | Bottom-bar content (copyright, legal links) |
| `socialMedia` | `SocialMediaProps[]` | | Social icon links |
| `classes` | `{ root?, container?, logo?, sections?, references?, social? }` | | CSS slot overrides |

### `FooterSection` shape

```ts
interface FooterSection {
  title: string;
  links: Array<{
    text: string;
    href?: string;
    onClick?: () => void;
  }>;
}
```

## Variants

| Variant | Description |
|---------|-------------|
| `"internal"` | Compact footer — typically logo + copyright. Used inside authenticated/private pages. |
| `"institutional"` | Full footer with columns grid, section links, social icons, and references bar. Used on public/marketing pages. |

## FooterList Props

Standalone list of footer links (used internally and can be composed):

| Prop | Type | Description |
|------|------|-------------|
| `title` | `string` | Section heading |
| `links` | `Array<{ text: string; href?: string; onClick?: () => void }>` | Link items |

## Usage Examples

### Internal footer (private app pages)

```tsx
import { Footer } from "@architecture-it/stylesystem";

<Footer
  variant="internal"
  references={
    <Typography variant="caption" color="secondary">
      © 2025 Andreani. Todos los derechos reservados.
    </Typography>
  }
/>
```

### Institutional footer (public/marketing)

```tsx
import { Footer, InstagramIcon, LinkedInIcon } from "@architecture-it/stylesystem";

<Footer
  variant="institutional"
  sections={[
    {
      title: "Empresa",
      links: [
        { text: "Quiénes somos", href: "/nosotros" },
        { text: "Trabaja con nosotros", href: "/empleos" },
      ],
    },
    {
      title: "Soporte",
      links: [
        { text: "Centro de ayuda", href: "/ayuda" },
        { text: "Contacto", href: "/contacto" },
      ],
    },
  ]}
  socialMedia={[
    { icon: <InstagramIcon />, url: "https://instagram.com/andreani" },
    { icon: <LinkedInIcon />, url: "https://linkedin.com/company/andreani" },
  ]}
  references={
    <Box display="flex" gap={2}>
      <Link href="/privacidad">Política de privacidad</Link>
      <Link href="/terminos">Términos y condiciones</Link>
    </Box>
  }
/>
```

### With custom logo

```tsx
import { Footer, getImagePropsLogoByBrand } from "@architecture-it/stylesystem";

<Footer
  variant="internal"
  logo={<img {...getImagePropsLogoByBrand("andreani")} height={32} />}
  references={<Typography variant="caption">© 2025 Andreani</Typography>}
/>
```

### FooterList standalone

```tsx
import { FooterList } from "@architecture-it/stylesystem";

<FooterList
  title="Herramientas"
  links={[
    { text: "Calculadora de envío", onClick: () => openCalc() },
    { text: "Mapa de sucursales", href: "/mapa" },
  ]}
/>
```

## Notes

- `variant="institutional"` renders `sections` as a CSS grid of columns — each section becomes a `FooterList`.
- The `references` slot appears at the very bottom, full-width, typically for copyright and legal links.
- Social icons accept `SocialMediaProps` — same type used in `SidebarAvatar`.
