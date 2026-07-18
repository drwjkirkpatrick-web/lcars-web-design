# LCARS Design System — Okuda's Grammar

Michael Okuda designed LCARS in 1987 under hard constraints: backlit film
panels (not screens), NTSC broadcast readability, and a tiny per-episode
budget. Every rule below traces back to those constraints — which is why
LCARS translates perfectly to cheap kiosks and dashboards today.

## 1. The Five Inviolable Rules

1. **Everything implies function.** No ornament. A colored rectangle must
   read as a button, a bar, or a data block. Okuda's actors were told to
   touch panels *meaningfully* — the design must support that illusion.
2. **The frame is the interface.** Content sits in black negative space;
   the colored L-shaped frame (elbows + bars + button column) IS the UI.
3. **Color is semantic, not decorative.** Departments and functions own
   color families (see Semantic Assignment in color-palettes.md).
4. **Type is ultra-condensed, uppercase, and sparse.** Swiss 911 Ultra
   Compressed. Labels, numbers, status — never paragraphs.
5. **Flat light.** The original panels were evenly backlit film. No
   gradients, shadows, bevels, or glass effects. Flat color on black.

## 2. Geometry Math

The entire frame derives from two measurements:

```
--bar-h   (horizontal arm height)   default 90px
--col-w   (vertical arm width)      default 150px
--gap     (frame-to-frame spacing)  default 8px
--r-outer (outer elbow radius)      70px 50px   (elliptical x y)
--r-inner (inner cutout radius)     35px 25px   (~ half of outer)
```

The elbow is an L-shape built from a rounded rect minus a rounded cutout:

- Outer: `border-top-left-radius: var(--r-outer)` on a colored rect.
- Cutout: `::after` positioned at `left: col-w; top: bar-h`, black,
  `border-top-left-radius: var(--r-inner)`.

**Why elliptical radii?** `70px 50px` (wider than tall) matches the
on-screen proportions — circular radii look "webby", elliptical reads canon.

**Thickness floor:** bar-h ≥ 48px and col-w ≥ 96px at any display size,
or the frame looks spindly. For a 7" Pi kiosk: bar-h 48–56, col-w 96–120.
For desktop: bar-h 80–100, col-w 140–180.

## 3. Layout Patterns

### Pattern A — Bridge Console / Main Screen (default)

```
┌─(elbow TL)─────────[ TITLE BAR ················ pill-R ]─┐
│ ELBOW-V  ┌───────────────────────────────────────────────┐
│ (arm)    │                                               │
│ [BTN 1]  │              CONTENT PANELS                   │
│ [BTN 2]  │         (black, thin colored frames)          │
│ [BTN 3]  │                                               │
│ [BTN 4]  │                                               │
└─(elbow BL)────────[ STATUS BAR ······················ ]──┘
```

### Pattern B — PADD (handheld)

No left elbow. Top bar with rounded-left cap, stacked full-width buttons,
content list below, thin bottom bar. Use Lower Decks PADD or 2369 palette.

### Pattern C — Wall Panel / Kiosk

Single large elbow TL + title bar, one giant readout grid, status footer.
This is the weather-station / sensor-dashboard pattern. Maximize number
size: readouts at 3–6rem Antonio Light.

## 4. Typography Scale

| Element | Weight | Size (desktop) | Notes |
|---------|--------|---------------|-------|
| Screen title | 600–700 | 2.2–3rem | in title bar, black-on-color or color-on-black |
| Button labels | 400–600 | 1.1–1.4rem | uppercase, right-aligned in column |
| Readout numbers | 300 | 3–6rem | light weight = "computer voice" |
| Readout labels | 400 | 0.85rem | uppercase, letter-spacing 0.1em |
| Status/footer | 400 | 1rem | blinking elements allowed |
| Body/status text | 400 | 1–1.2rem | short lines only |

Always: `text-transform: uppercase; letter-spacing: 0.04–0.1em;`
Numbers: right-aligned, tabular feel (Antonio is naturally tabular-ish).

## 5. Component Anatomy

**Button (column block):** colored rect, height ≥ 40px, black uppercase
label right-aligned with 12px padding. Rounded variants: `pill-l`
(radius left), `pill-r` (radius right), `block` (square — most common
in the vertical column).

**Title bar:** colored horizontal bar, `border-radius: 0 40px 40px 0`
on the right end (pill-R). Title text black, left-aligned, vertically
centered. Optional right-side segment in a second color (two-tone bars
are very canon).

**Readout block:** label strip (small colored bar with black label) above
a black number field with colored text. Or inline: `LABEL .......... 47.2`
with dotted leader — acceptable and very Okuda.

**Panel:** black rect with 2px colored border. No radius. Title strip
across the top in the border color with black text.

**Status dot:** 10–14px circle or square, hard blinking via steps().

## 6. Color Semantics by Department (Canon)

- Command/bridge primary: golds (golden-tanoi, tanoi)
- Ops/engineering: reds (red-damask, chestnut-rose), husk
- Science/medical: blues (anakiwa, danub, blue-bell)
- Navigation/comms accents: purples (lilac, hopbush, melrose)
- Security/tactical: neon-carrot → red-damask range

A "clinic dashboard" in LCARS would lean science-blue frames; a "machine
shop console" would lean engineering red-orange. Keep ONE frame family
per screen; mixing gold frame + red frame on one screen reads as two
departments fighting.

## 7. Motion Principles

- **Instant > eased.** Computers in TNG don't ease-out; they snap.
  Use `linear` or `steps()`, 100–300ms.
- **Staggered boot.** Panels light up in sequence (frame first, then
  buttons, then content), 40–80ms stagger.
- **Blinks are hard.** `steps(1)` or `steps(2)`. No opacity fades.
- **Data ticks, doesn't tween.** Numbers change instantly on update.

## 8. Accessibility & Readability (the Okuda Test)

Okuda's bar: readable across a set on 480i broadcast. Your bar: readable
from 2 meters on the target display. Check:

- Contrast: black-on-orange ≈ 9:1 (excellent); orange-on-black ≈ 8:1.
- Minimum 32px hit targets (LCARS buttons are huge by design).
- Don't put long text in narrow columns; break into label + readout.
- Colorblind note: gold vs red-damask and anakiwa vs lilac are the risky
  pairs — separate them by position/label, not color alone.

## 9. Historical Notes (for authenticity decisions)

- Season 1–2 TNG panels are sparser and more golden (2357 palette).
- Later seasons add more blue/purple data blocks (2369).
- Films (Generations→Nemesis) go cooler and denser (2375/2379).
- Voyager uses the same grammar with slightly more blue-gray.
- DS9's station UI is Cardassian — different grammar entirely (ovals,
  brown/copper). Don't mix grammars on one page.
- Lower Decks (2020s) is a deliberate throwback: brighter, chunkier,
  orange-forward — great for playful kiosks.
