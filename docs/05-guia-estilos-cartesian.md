# Guía de Identidad Visual Corporativa (Cartesian CSS)

Esta guía documenta la integración del **Sistema de Diseño Cartesian de Andreani** implementado a nivel de **estilos CSS nativos** en este repositorio y en el portal de observabilidad.

---

## 1. Fundamentos del Sistema

El sistema **Cartesian** estandariza tokens de diseño organizados jerárquicamente para garantizar una experiencia visual coherente, accesible y alineada a la marca Andreani:

1. **Tokens Primitivos**: Valores base puros (escalas cromáticas 50 a 900, fuentes, espaciados en px).
2. **Tokens Semánticos**: Asignación de intención funcional (superficie, fondo, texto, bordes, estados de interacción como hover, pressed o disabled).
3. **Soporte Bimodal**: Variables adaptativas automáticas para **Light Mode** y **Dark Mode**.

El archivo canonical de este repositorio es [`cartesian.css`](../cartesian.css), utilizable directamente en cualquier página HTML sin necesidad de empaquetadores ni dependencias externas.

---

## 2. Paleta Cromática Oficial

### Rojo Andreani (Primario Institucional)

Color emblema de la compañía. Se utiliza en barras de navegación, botones primarios, estados activos e indicadores críticos.

| Token | Valor Hex | Uso Principal |
| :--- | :---: | :--- |
| `--c-red-50` | `#fbe8e9` | Fondo sutil de selección / badges |
| `--c-red-500` | `#df474d` | Alertas / acentos secundarios |
| `--c-red-600` | `#d71920` | **Rojo oficial Andreani** |
| `--c-red-700` | `#b6040b` | Hover y estados de presión |
| `--c-red-900` | `#560a0d` | Tonos oscuros de contraste |

### Azul Institucional Andreani

Aporta sobriedad, alta legibilidad y jerarquía a títulos y estructura.

| Token | Valor Hex | Uso Principal |
| :--- | :---: | :--- |
| `--c-blue-50` | `#edeffb` | Fondos de información técnica y tags |
| `--c-blue-600` | `#4e63d7` | Hipervínculos e indicadores informativos |
| `--c-blue-900` | `#1f2856` | **Azul noche corporativo** para tipografía y topbars |

### Escalas de Soporte Operativo

- **Verde Éxito / Operación Normal**: `--c-green-600` (`#1f7e5a`), `--c-green-50` (`#ddf3ea`).
- **Amarillo / Ámbar Precaución / Señalética**: `--c-yellow-700` (`#d4a140`), `--c-yellow-50` (`#fff9ed`).
- **Naranja Advertencia / Rampa de Excepción**: `--c-orange-600` (`#e86427`), `--c-orange-50` (`#fdefe9`).
- **Grises Neutros**: `--c-gray-50` (`#fafafa` fondo general), `--c-gray-100` (`#dfe1e3` bordes), `--c-gray-800` (`#272a2f` texto principal).

---

## 3. Tipografía Oficial

El ecosistema digital Andreani utiliza dos tipografías maestras servidas vía Google Fonts:

### Rubik (Títulos, Headlines y Badges)
Utilizada en `h1` a `h6`, píldoras de marca y llamados a la acción destacados.
- Variable: `--c-font-family-headline` / `--c-font-family-title`
- Pesos: Medium (`500`), SemiBold (`600`), Bold (`700`), ExtraBold (`800`)

### Roboto (Cuerpo, Tablas y Formularios)
Optimizada para máxima legibilidad en diagramas técnicos, párrafos descriptivos y tablas operativas.
- Variable: `--c-font-family-body` / `--c-font-family-label`
- Pesos: Light (`300`), Regular (`400`), Medium (`500`), Bold (`700`)

---

## 4. Escala de Espaciados y Bordes

Para mantener armonía espacial en paneles y vistas de observabilidad:

### Espaciados
- `--c-spacing-1`: `4px`
- `--c-spacing-2`: `8px`
- `--c-spacing-3`: `12px`
- `--c-spacing-4`: `16px`
- `--c-spacing-5`: `24px`
- `--c-spacing-6`: `32px`
- `--c-spacing-7`: `48px`

### Radios de Borde
- `--c-border-radius-xsmall`: `4px` (tags y etiquetas compactas)
- `--c-border-radius-small`: `8px` (botones, inputs y tarjetas estándar)
- `--c-border-radius-medium`: `16px` (modales y contenedores principales)
- `--c-border-radius-large`: `24px` (tarjetas hero y banners)
- `--c-border-radius-xlarge`: `99px` (píldoras y badges redondeados)

---

## 5. Implementación en Código CSS Nativo

Para utilizar los estilos en cualquier componente o documento HTML:

```html
<!-- 1. Cargar fuentes oficiales -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Rubik:wght@500;600;700;800&display=swap" rel="stylesheet">

<!-- 2. Vincular la hoja de estilos Cartesian -->
<link rel="stylesheet" href="cartesian.css">
```

### Ejemplo de componente usando variables nativas:

```css
.tarjeta-sorter {
  background-color: var(--c-color-surface);
  border: var(--c-border-width-subtle) solid var(--c-color-border-neutral-soft);
  border-radius: var(--c-border-radius-small);
  padding: var(--c-spacing-5);
  box-shadow: var(--card-shadow);
}

.tarjeta-sorter h3 {
  font-family: var(--c-font-family-headline);
  color: var(--c-color-text-content-title);
  font-size: var(--c-font-size-headline5);
  margin-bottom: var(--c-spacing-3);
}

.tarjeta-sorter p {
  font-family: var(--c-font-family-body);
  color: var(--c-color-text-content-base);
  font-size: var(--c-font-size-bodymedium);
  line-height: var(--c-font-lineheight-bodymedium);
}

.boton-accion {
  background-color: var(--c-color-fill-primary);
  color: var(--c-color-text-inverse);
  border-radius: var(--c-border-radius-small);
  padding: var(--c-spacing-2) var(--c-spacing-4);
  font-family: var(--c-font-family-title);
  border: none;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.boton-accion:hover {
  background-color: var(--c-color-fill-primary-hover);
}
```

---

## 6. Soporte para Modo Oscuro

El sistema activa automáticamente los tokens de modo oscuro mediante el atributo `data-theme-mode="dark"` o `data-theme="dark"` en la etiqueta `<html>`:

```html
<html lang="es" data-theme-mode="dark">
  <!-- Todos los tokens --c-color-* se transforman a su variante nocturna con alto contraste -->
</html>
```
