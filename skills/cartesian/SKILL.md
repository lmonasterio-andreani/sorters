---
name: cartesian
description: A comprehensive guide to CSS variables in with the design system of the company, covering colors, typography, spacing, and usage guidelines for frontend agents.
---

# CSS Variables Skill Guide

This document provides a comprehensive reference for all CSS variables available in the Cartesian design system. Frontend agents should reference this guide when styling components to ensure consistency and adherence to the design system.

## Table of Contents

1. [Color Variables](#color-variables)
   - [Color Primitives](#color-primitives)
   - [Semantic Colors](#semantic-colors)
   - [Text Colors](#text-colors)
   - [Border Colors](#border-colors)
   - [Icon Colors](#icon-colors)
   - [Partner Brand Colors](#partner-brand-colors)
2. [Border Variables](#border-variables)
   - [Border Width](#border-width)
   - [Border Radius](#border-radius)
3. [Typography Variables](#typography-variables)
   - [Font Family](#font-family)
   - [Font Size](#font-size)
   - [Font Weight](#font-weight)
   - [Line Height](#line-height)
   - [Mobile Typography](#mobile-typography)
4. [Spacing Variables](#spacing-variables)

---

## Color Variables

### Color Primitives

Base color palette used throughout the system. These include hue variations (50-900) for each color family.

#### Red Scale
- `--c-red-50`: #fbe8e9
- `--c-red-100`: #f7d1d2
- `--c-red-200`: #f3babc
- `--c-red-300`: #efa3a6
- `--c-red-400`: #e77579
- `--c-red-500`: #df474d
- `--c-red-600`: #d71920
- `--c-red-700`: #b6040b
- `--c-red-800`: #810f13
- `--c-red-900`: #560a0d

#### Orange Scale
- `--c-orange-50`: #fdefe9
- `--c-orange-100`: #fae0d4
- `--c-orange-200`: #f8d0be
- `--c-orange-300`: #f6c1a9
- `--c-orange-400`: #f1a27d
- `--c-orange-500`: #ed8352
- `--c-orange-600`: #e86427
- `--c-orange-700`: #ba501f
- `--c-orange-800`: #8b3c17
- `--c-orange-900`: #5d2810

#### Yellow Scale
- `--c-yellow-50`: #fff9ed
- `--c-yellow-100`: #fff3dc
- `--c-yellow-200`: #ffedca
- `--c-yellow-300`: #ffe7b9
- `--c-yellow-400`: #ffdb96
- `--c-yellow-500`: #ffcf73
- `--c-yellow-600`: #ffc350
- `--c-yellow-700`: #d4a140
- `--c-yellow-800`: #a97f30
- `--c-yellow-900`: #684d18

#### Green Scale
- `--c-green-50`: #ddf3ea
- `--c-green-100`: #bfe8d9
- `--c-green-200`: #9cd1bd
- `--c-green-300`: #8ac5af
- `--c-green-400`: #66ad92
- `--c-green-500`: #439676
- `--c-green-600`: #1f7e5a
- `--c-green-700`: #196548
- `--c-green-800`: #134c36
- `--c-green-900`: #0c3224

#### Blue Scale
- `--c-blue-50`: #edeffb
- `--c-blue-100`: #dce0f7
- `--c-blue-200`: #cad0f3
- `--c-blue-300`: #b8c1ef
- `--c-blue-400`: #95a1e7
- `--c-blue-500`: #7182df
- `--c-blue-600`: #4e63d7
- `--c-blue-700`: #3e4fac
- `--c-blue-800`: #2f3b81
- `--c-blue-900`: #1f2856

#### Gray Scale
- `--c-gray-50`: #fafafa
- `--c-gray-100`: #dfe1e3
- `--c-gray-200`: #c0c3c8
- `--c-gray-300`: #a0a6ac
- `--c-gray-400`: #818891
- `--c-gray-500`: #616a75
- `--c-gray-600`: #4e555e
- `--c-gray-700`: #3a4046
- `--c-gray-800`: #272a2f
- `--c-gray-900`: #1d2023
- `--c-gray-000`: #fff

#### Dark Gray Scale
- `--c-darkgray-50`: #1d2023
- `--c-darkgray-100`: #272a2f
- `--c-darkgray-200`: #3a4046
- `--c-darkgray-300`: #4e555e
- `--c-darkgray-400`: #616a75
- `--c-darkgray-500`: #818891
- `--c-darkgray-600`: #4e555e
- `--c-darkgray-700`: #3a4046
- `--c-darkgray-800`: #272a2f
- `--c-darkgray-900`: #1d2023
- `--c-darkgray-00`: #ffffff

#### Base Colors
- `--c-base-black`: #000000
- `--c-base-white`: #ffffff

#### Opacity
- `--c-opacity-opacity`: #1d2023b2
- `--c-opacity-backdrop`: #1d2023

### Semantic Colors

Semantic colors for UI surfaces and components.

#### Background Colors
- `--c-color-bg`: #fafafa (light mode) / #1d2023 (dark mode)
- `--c-color-bg-white`: #ffffff
- `--c-color-bg-backdrop`: #1d2023b2
- `--c-color-bg-black`: #000000

#### Surface Colors
- `--c-color-surface`: #ffffff (light) / #272a2f (dark)
- `--c-color-surface-hover`: #fafafa (light) / #272a2f (dark)
- `--c-color-surface-disabled`: #dfe1e3 (light) / #a0a6ac (dark)
- `--c-color-surface-primary`: #d71920 (light) / #810f13 (dark)
- `--c-color-surface-primary-subtle`: #fbe8e9 (light) / #e77579 (dark)
- `--c-color-surface-neutral`: #dfe1e3 (light) / #272a2f (dark)
- `--c-color-surface-neutral-strong`: #616a75
- `--c-color-surface-neutral-subtle`: #fafafa (light) / #1d2023 (dark)
- `--c-color-surface-success`: #1f7e5a (light) / #134c36 (dark)
- `--c-color-surface-success-subtle`: #ddf3ea (light) / #66ad92 (dark)
- `--c-color-surface-info`: #4e63d7 (light) / #2f3b81 (dark)
- `--c-color-surface-info-subtle`: #edeffb (light) / #95a1e7 (dark)
- `--c-color-surface-caution`: #ffc350 (light) / #a97f30 (dark)
- `--c-color-surface-caution-subtle`: #fff9ed (light) / #ffdb96 (dark)
- `--c-color-surface-warning`: #e86427 (light) / #8b3c17 (dark)
- `--c-color-surface-warning-subtle`: #fdefe9 (light) / #f1a27d (dark)
- `--c-color-surface-error`: #df474d (light) / #810f13 (dark)
- `--c-color-surface-error-subtle`: #fbe8e9 (light) / #e77579 (dark)

#### Fill Colors
- `--c-color-fill`: #ffffff (light) / #1d2023 (dark)
- `--c-color-fill-hover`: #fafafa (light) / #c0c3c8 (dark)
- `--c-color-fill-disabled`: #dfe1e3
- `--c-color-fill-pressed`: #fafafa (light) / #616a75 (dark)
- `--c-color-fill-selected`: #fafafa (light) / #818891 (dark)
- `--c-color-fill-transparent`: transparent
- `--c-color-fill-transparent-hover`: #fafafa

**Primary Fill**
- `--c-color-fill-primary`: #d71920 (light) / #df474d (dark)
- `--c-color-fill-primary-hover`: #b6040b (light) / #d71920 (dark)
- `--c-color-fill-primary-pressed`: #810f13 (light) / #e77579 (dark)
- `--c-color-fill-primary-subtle`: #fbe8e9 (light) / #560a0d (dark)

**Neutral Fill**
- `--c-color-fill-neutral`: #dfe1e3 (light) / #272a2f (dark)
- `--c-color-fill-neutral-strong`: #4e555e
- `--c-color-fill-neutral-subtle`: #fafafa (light) / #1d2023 (dark)
- `--c-color-fill-neutral-hover`: #a0a6ac (light) / #3a4046 (dark)
- `--c-color-fill-neutral-pressed`: #3a4046 (light) / #c0c3c8 (dark)
- `--c-color-fill-neutral-stronge`: #4e555e / #616a75 (dark)

**Success Fill**
- `--c-color-fill-success`: #1f7e5a (light) / #439676 (dark)
- `--c-color-fill-success-hover`: #196548 (light) / #1f7e5a (dark)
- `--c-color-fill-success-pressed`: #134c36 (light) / #66ad92 (dark)
- `--c-color-fill-success-subtle`: #ddf3ea (light) / #0c3224 (dark)

**Info Fill**
- `--c-color-fill-info`: #4e63d7 (light) / #7182df (dark)
- `--c-color-fill-info-hover`: #3e4fac (light) / #4e63d7 (dark)
- `--c-color-fill-info-pressed`: #2f3b81 (light) / #95a1e7 (dark)
- `--c-color-fill-info-subtle`: #edeffb (light) / #1f2856 (dark)

**Caution Fill**
- `--c-color-fill-caution`: #ffc350 (light) / #ffcf73 (dark)
- `--c-color-fill-caution-hover`: #d4a140 (light) / #ffc350 (dark)
- `--c-color-fill-caution-pressed`: #a97f30 (light) / #ffdb96 (dark)
- `--c-color-fill-caution-subtle`: #fff9ed (light) / #684d18 (dark)

**Warning Fill**
- `--c-color-fill-warning`: #e86427 (light) / #ed8352 (dark)
- `--c-color-fill-warning-hover`: #ba501f (light) / #e86427 (dark)
- `--c-color-fill-warning-pressed`: #8b3c17 (light) / #f1a27d (dark)
- `--c-color-fill-warning-subtle`: #fdefe9 (light) / #5d2810 (dark)

**Error Fill**
- `--c-color-fill-error`: #df474d (light) / #df474d (dark)
- `--c-color-fill-error-hover`: #b6040b (light) / #d71920 (dark)
- `--c-color-fill-error-pressed`: #810f13 (light) / #e77579 (dark)
- `--c-color-fill-error-subtle`: #fbe8e9 (light) / #f7d1d2 (dark)

### Text Colors

#### Strong & Base Text
- `--c-color-text-strong`: #272a2f
- `--c-color-text`: #4e555e
- `--c-color-text-hover`: #3a4046
- `--c-color-text-pressed`: #272a2f
- `--c-color-text-subtle`: #818891
- `--c-color-text-disabled`: #818891
- `--c-color-text-inverse`: #fff

#### Primary Text
- `--c-color-text-primary-primary`: #d71920
- `--c-color-text-primary-hover`: #b6040b (light) / #dfe1e3 (dark)
- `--c-color-text-primary-pressed`: #810f13 (light) / #818891 (dark)
- `--c-color-text-primary`: #d71920 (light) / #4e555e (dark)

#### Success Text
- `--c-color-text-success`: #1f7e5a (light) / #439676 (dark)
- `--c-color-text-success-subtle`: #ddf3ea
- `--c-color-text-success-strong`: #0c3224

#### Info Text
- `--c-color-text-info`: #4e63d7 (light) / #7182df (dark)
- `--c-color-text-info-subtle`: #edeffb
- `--c-color-text-info-strong`: #1f2856

#### Caution Text
- `--c-color-text-caution`: #e86427 (light) / #ed8352 (dark)
- `--c-color-text-caution-inverse`: #684d18
- `--c-color-text-caution-subtle`: #fdefe9
- `--c-color-text-caution-strong`: #5d2810

#### Warning Text
- `--c-color-text-warning`: #ffc350 (light) / #ffcf73 (dark)
- `--c-color-text-warning-inverse`: #5d2810
- `--c-color-text-warning-subtle`: #fff9ed
- `--c-color-text-warning-strong`: #684d18

#### Error Text
- `--c-color-text-error`: #d71920 (light) / #df474d (dark)
- `--c-color-text-error-inverse`: #560a0d
- `--c-color-text-error-subtle`: #fbe8e9
- `--c-color-text-error-strong`: #560a0d

#### Link Text
- `--c-color-text-link`: #4e63d7
- `--c-color-text-link-hover`: #3e4fac
- `--c-color-text-link-visited`: #2f3b81

#### Content Hierarchy
- `--c-color-text-content-base`: #4e555e
- `--c-color-text-content-subtitle`: #3a4046
- `--c-color-text-content-title`: #272a2f

#### Neutral Text
- `--c-color-text-neutral-strong`: #272a2f (light) / #c0c3c8 (dark)
- `--c-color-text-neutral-hover`: #3a4046 (light) / #dfe1e3 (dark)
- `--c-color-text-neutral-pressed`: #272a2f (light) / #818891 (dark)
- `--c-color-text-neutral-subtle`: #a0a6ac (light) / #3a4046 (dark)
- `--c-color-text-neutral-disabled`: #818891 (light) / #a0a6ac (dark)
- `--c-color-text-neutral-inverse`: #ffffff (light) / #fafafa (dark)

### Border Colors

#### Base Border
- `--c-color-border`: #4e555e
- `--c-color-border-strong`: #818891
- `--c-color-border-subtle`: #c0c3c8

#### Semantic Border
- `--c-color-border-negative`: #d71920 (light) / #efa3a6 (dark)
- `--c-color-border-positive`: #1f7e5a (light) / #8ac5af (dark)

#### Primary Border
- `--c-color-border-primary`: #d71920 (light) / #dfe1e3 (dark)
- `--c-color-border-primary-hover`: #b6040b (light) / #a0a6ac (dark)
- `--c-color-border-primary-selected`: #f3babc (light) / #4e555e (dark)

#### Success Border
- `--c-color-border-success`: #1f7e5a (light) / #66ad92 (dark)
- `--c-color-border-success-strong`: #196548 (light) / #8ac5af (dark)
- `--c-color-border-success-subtle`: #9cd1bd (light) / #196548 (dark)

#### Info Border
- `--c-color-border-info`: #4e63d7 (light) / #b8c1ef (dark)

#### Caution Border
- `--c-color-border-caution`: #ffc350 (light) / #ffdb96 (dark)
- `--c-color-border-caution-strong`: #d4a140 (light) / #ffe7b9 (dark)
- `--c-color-border-caution-subtle`: #ffedca (light) / #d4a140 (dark)

#### Warning Border
- `--c-color-border-warning`: #ffc350 (light) / #ffe7b9 (dark)

#### Error Border
- `--c-color-border-error`: #df474d (light) / #e77579 (dark)
- `--c-color-border-error-subtle`: #f3babc (light) / #b6040b (dark)
- `--c-color-border-error-strong`: #810f13

#### Neutral Border
- `--c-color-border-neutral-soft`: #dfe1e3 (light) / #272a2f (dark)
- `--c-color-border-neutral-subtle`: #a0a6ac (light) / #3a4046 (dark)
- `--c-color-border-neutral`: #818891
- `--c-color-border-neutral-strong`: #4e555e
- `--c-color-border-neutral-focus`: #c0c3c8
- `--c-color-border-neutral-hover`: #3a4046
- `--c-color-border-neutral-black`: #000000 (light) / #fafafa (dark)
- `--c-color-border-neutral-white`: #ffffff (light) / #fafafa (dark)

### Icon Colors

#### Base Icon
- `--c-color-icon-strong`: #272a2f
- `--c-color-icon-hover`: #3a4046
- `--c-color-icon-pressed`: #272a2f
- `--c-color-icon-subtle`: #818891
- `--c-color-icon-inverse`: #fff
- `--c-color-icon-disabled`: #818891

#### Primary Icon
- `--c-color-icon-primary`: #d71920 (light) / #df474d (dark)
- `--c-color-icon-primary-hover`: #b6040b (light) / #d71920 (dark)
- `--c-color-icon-primary-inverse`: #560a0d
- `--c-color-icon-primary-pressed`: #810f13 (light) / #e77579 (dark)
- `--c-color-icon-primary-subtle`: #efa3a6

#### Success Icon
- `--c-color-icon-success`: #1f7e5a (light) / #439676 (dark)
- `--c-color-icon-success-hover`: #196548 (light) / #1f7e5a (dark)
- `--c-color-icon-success-inverse`: #0c3224
- `--c-color-icon-success-pressed`: #134c36 (light) / #66ad92 (dark)

#### Info Icon
- `--c-color-icon-info`: #4e63d7 (light) / #7182df (dark)
- `--c-color-icon-info-hover`: #3e4fac (light) / #4e63d7 (dark)
- `--c-color-icon-info-inverse`: #1f2856
- `--c-color-icon-info-pressed`: #2f3b81 (light) / #95a1e7 (dark)

#### Caution Icon
- `--c-color-icon-caution`: #ffc350 (light) / #ffcf73 (dark)
- `--c-color-icon-caution-hover`: #d4a140 (light) / #ffc350 (dark)
- `--c-color-icon-caution-inverse`: #684d18
- `--c-color-icon-caution-pressed`: #a97f30 (light) / #ffdb96 (dark)

#### Warning Icon
- `--c-color-icon-warning`: #e86427 (light) / #ed8352 (dark)
- `--c-color-icon-warning-hover`: #ba501f (light) / #e86427 (dark)
- `--c-color-icon-warning-inverse`: #5d2810
- `--c-color-icon-warning-pressed`: #8b3c17 (light) / #f1a27d (dark)

#### Error Icon
- `--c-color-icon-error`: #d71920 (light) / #df474d (dark)
- `--c-color-icon-error-hover`: #b6040b (light) / #d71920 (dark)
- `--c-color-icon-error-inverse`: #560a0d
- `--c-color-icon-error-pressed`: #810f13 (light) / #e77579 (dark)

#### Link Icon
- `--c-color-icon-link`: #4e63d7
- `--c-color-icon-link-hover`: #3e4fac
- `--c-color-icon-link-visited`: #2f3b81

#### Neutral Icon
- `--c-color-icon-neutral`: #4e555e (light) / #616a75 (dark)
- `--c-color-icon-neutral-hover`: #3a4046 (light) / #4e555e (dark)
- `--c-color-icon-neutral-subtle`: #a0a6ac (light) / #3a4046 (dark)
- `--c-color-icon-neutral-pressed`: #272a2f (light) / #818891 (dark)
- `--c-color-icon-neutral-strong`: #272a2f (light) / #a0a6ac (dark)
- `--c-color-icon-neutral-inverse`: #ffffff
- `--c-color-icon-neutral-disabled`: #818891

### Partner Brand Colors

#### Modo
- `--c-color-partners-modo-primary`: #008859
- `--c-color-partners-modo-inverse`: #ffffff

#### MercadoPago (MPago)
- `--c-color-partners-mpago-primary`: #00b1ea
- `--c-color-partners-mpago-secondary`: #1d2647
- `--c-color-partners-mpago-inverse`: #ffffff

#### Nube
- `--c-color-partners-nube-primary`: #172363
- `--c-color-partners-nube-inverse`: #ffffff

### Additional Colors
- `--c-color-opacity-backdrop`: #1d2023
- `--c-nube-primary`: #172363
- `--c-nube-white`: #ffffff
- `--c-mpago-primary`: #00b1ea
- `--c-mpago-skyBlue`: #1d2647
- `--c-mpago-white`: #ffffff
- `--c-modo-primary`: #008859
- `--c-modo-white`: #ffffff

---

## Border Variables

### Border Width

- `--c-border-width-regular`: 2px
- `--c-border-width-strong`: 3px
- `--c-border-width-subtle`: 1px

### Border Radius

- `--c-border-radius-none`: 0
- `--c-border-radius-xsmall`: 4px
- `--c-border-radius-small`: 8px
- `--c-border-radius-medium`: 16px
- `--c-border-radius-large`: 24px
- `--c-border-radius-xlarge`: 99px

---

## Typography Variables

### Font Family

- `--c-font-family-headline`: Rubik
- `--c-font-family-title`: Rubik
- `--c-font-family-body`: Roboto
- `--c-font-family-label`: Roboto
- `--c-font-family-caption`: Roboto
- `--c-font-family-overline`: Roboto

### Font Size

#### Desktop Font Sizes
- `--c-font-size-headline1`: 38px
- `--c-font-size-headline2`: 40px
- `--c-font-size-headline3`: 32px
- `--c-font-size-headline4`: 24px
- `--c-font-size-headline5`: 20px
- `--c-font-size-headline6`: 18px
- `--c-font-size-titlesmall`: 14px
- `--c-font-size-titlemedium`: 16px
- `--c-font-size-titlelarge`: 18px
- `--c-font-size-bodysmall`: 14px
- `--c-font-size-bodymedium`: 16px
- `--c-font-size-bodylarge`: 18px
- `--c-font-size-labelsmall`: 14px
- `--c-font-size-labelmedium`: 16px
- `--c-font-size-labellarge`: 18px
- `--c-font-size-caption`: 12px
- `--c-font-size-overline`: 10px

#### Mobile Font Sizes
- `--c-mobile-font-size-headline1`: 32px
- `--c-mobile-font-size-headline2`: 28px
- `--c-mobile-font-size-headline3`: 24px
- `--c-mobile-font-size-headline4`: 20px
- `--c-mobile-font-size-headline5`: 18px
- `--c-mobile-font-size-headline6`: 16px
- `--c-mobile-font-size-titlesmall`: 14px
- `--c-mobile-font-size-titlemedium`: 16px
- `--c-mobile-font-size-titlelarge`: 18px
- `--c-mobile-font-size-bodysmall`: 14px
- `--c-mobile-font-size-bodymedium`: 16px
- `--c-mobile-font-size-bodylarge`: 18px
- `--c-mobile-font-size-labelsmall`: 14px
- `--c-mobile-font-size-labelmedium`: 16px
- `--c-mobile-font-size-labellarge`: 18px
- `--c-mobile-font-size-caption`: 12px
- `--c-mobile-font-size-overline`: 10px

### Font Weight

#### Desktop Font Weights
- `--c-font-weight-light`: 300
- `--c-font-weight-regular`: 400
- `--c-font-weight-regularunderline`: 400
- `--c-font-weight-medium`: 500
- `--c-font-weight-mediumundeline`: 500
- `--c-font-weight-bold`: 700
- `--c-font-weight-extrabold`: 900
- `--c-font-weight-italic`: italic

#### Mobile Font Weights
- `--c-mobile-font-weight-light`: 300
- `--c-mobile-font-weight-regular`: 400
- `--c-mobile-font-weight-regularunderline`: 400
- `--c-mobile-font-weight-medium`: 500
- `--c-mobile-font-weight-mediumundeline`: 500
- `--c-mobile-font-weight-bold`: 700
- `--c-mobile-font-weight-extrabold`: 900
- `--c-mobile-font-weight-italic`: italic

### Line Height

#### Desktop Line Heights
- `--c-font-lineheight-headline1`: 54px
- `--c-font-lineheight-headline2`: 44px
- `--c-font-lineheight-headline3`: 36px
- `--c-font-lineheight-headline4`: 28px
- `--c-font-lineheight-headline5`: 24px
- `--c-font-lineheight-headline6`: 22px
- `--c-font-lineheight-titlesmall`: 20px
- `--c-font-lineheight-titlemedium`: 24px
- `--c-font-lineheight-titlelarge`: 28px
- `--c-font-lineheight-bodysmall`: 20px
- `--c-font-lineheight-bodymedium`: 24px
- `--c-font-lineheight-bodylarge`: 28px
- `--c-font-lineheight-labelsmall`: 20px
- `--c-font-lineheight-labelmedium`: 24px
- `--c-font-lineheight-labellarge`: 28px
- `--c-font-lineheight-caption`: 16px
- `--c-font-lineheight-overline`: 14px

#### Mobile Line Heights
- `--c-mobile-font-lineheight-headline1`: 36px
- `--c-mobile-font-lineheight-headline2`: 32px
- `--c-mobile-font-lineheight-headline3`: 28px
- `--c-mobile-font-lineheight-headline4`: 24px
- `--c-mobile-font-lineheight-headline5`: 22px
- `--c-mobile-font-lineheight-headline6`: 20px
- `--c-mobile-font-lineheight-titlesmall`: 20px
- `--c-mobile-font-lineheight-titlemedium`: 24px
- `--c-mobile-font-lineheight-titlelarge`: 28px
- `--c-mobile-font-lineheight-bodysmall`: 20px
- `--c-mobile-font-lineheight-bodymedium`: 24px
- `--c-mobile-font-lineheight-bodylarge`: 28px
- `--c-mobile-font-lineheight-labelsmall`: 20px
- `--c-mobile-font-lineheight-labelmedium`: 24px
- `--c-mobile-font-lineheight-labellarge`: 28px
- `--c-mobile-font-lineheight-caption`: 16px
- `--c-mobile-font-lineheight-overline`: 14px

---

## Spacing Variables

Spacing scale for consistent margins, padding, and gaps throughout the design system.

- `--c-spacing-0`: 0px
- `--c-spacing-1`: 4px
- `--c-spacing-2`: 8px
- `--c-spacing-3`: 12px
- `--c-spacing-4`: 16px
- `--c-spacing-5`: 24px
- `--c-spacing-6`: 32px
- `--c-spacing-7`: 48px
- `--c-spacing-8`: 64px
- `--c-spacing-9`: 80px

---

## Usage Guidelines

### Dark Mode Support

Most color variables have both light and dark mode variants. The dark mode values are defined in the `[data-theme-mode="dark"]` selector. When using colors, ensure you:

1. Use the semantic color variables (e.g., `--c-color-text-primary`) rather than primitive color variables (e.g., `--c-red-500`)
2. Do not hardcode hex values in your CSS - always reference CSS variables
3. Test components in both light and dark modes

### Typography Combinations

Use typography variables in combination with spacing variables. Example:

```css
.heading {
  font-family: var(--c-font-family-headline);
  font-size: var(--c-font-size-headline1);
  line-height: var(--c-font-lineheight-headline1);
  font-weight: var(--c-font-weight-bold);
  margin-bottom: var(--c-spacing-4);
}
```

### Mobile Responsiveness

For responsive typography, use mobile variants on smaller breakpoints:

```css
.heading {
  font-size: var(--c-mobile-font-size-headline1);
  line-height: var(--c-mobile-font-lineheight-headline1);
}

@media (min-width: 1024px) {
  .heading {
    font-size: var(--c-font-size-headline1);
    line-height: var(--c-font-lineheight-headline1);
  }
}
```

### Spacing Best Practices

Use the spacing scale consistently:

```css
.component {
  padding: var(--c-spacing-4);
  margin-bottom: var(--c-spacing-5);
  gap: var(--c-spacing-3);
}
```

---

## Color Naming Convention

The color variables follow a consistent naming pattern: `--c-[category]-[subcategory]-[state]`

- **Color**: `c` prefix indicates a color variable
- **Category**: Primary categorization (e.g., `color`, `red`, `blue`)
- **Subcategory**: Specific usage (e.g., `text`, `surface`, `border`, `icon`)
- **State**: Optional state modifier (e.g., `hover`, `pressed`, `disabled`, `subtle`)

Understanding this pattern helps in finding and using the correct variable for your needs.

---

## Summary

This comprehensive CSS variables system ensures:

- **Consistency**: All colors, typography, and spacing follow the same scale
- **Maintainability**: Centralized variable definitions make updates easy
- **Accessibility**: Theme awareness with light/dark mode support
- **Flexibility**: Semantic naming allows intuitive variable selection
- **Scalability**: Organized structure supports future additions

Frontend agents should reference this guide when styling components to leverage the full power of the design system.
