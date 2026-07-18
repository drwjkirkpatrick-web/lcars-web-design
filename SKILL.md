---
name: lcars-web-design
description: |-
  Build authentic Star Trek TNG LCARS (Library Computer Access/Retrieval System)
  websites and dashboards. Covers Okuda's design grammar (elbows, bars, pills),
  canon color palettes (2357/2369/2375/2379 + Picard/Lower Decks themes),
  Antonio/Swiss-911 typography, pure-CSS frame construction, LCARS animation
  vocabulary (boot sweep, blinks, sweeps, red alert), and procedural Web Audio
  beeps. Ships copy-paste templates: base page, component CSS library, and a
  full animated dashboard.
version: 1.0.0
license: MIT
---

# LCARS Web Design

Use this skill whenever the user wants a Star Trek TNG LCARS-style website,
dashboard, kiosk display, or control panel. The design language was engineered
by Michael Okuda in 1987 to be readable on cheap NTSC broadcast hardware —
bold color blocks, huge hit targets, zero decoration. That makes it ideal for
kiosks, sensor dashboards, and Pi displays today.

## Trigger Conditions

- User asks for an LCARS / Star Trek TNG interface, dashboard, or theme.
- User wants a sci-fi computer console aesthetic for a kiosk, Pi display,
  home automation panel, or monitoring dashboard.
- User mentions Okuda, "Star Trek computer", elbows, or LCARS colors.

## Core Design Grammar (Okuda Rules — Follow These Exactly)

1. **Everything implies function.** No decoration. Every colored block is a
   button, bar, or readout. If it does nothing, remove it.
2. **The elbow is the frame.** Every screen is framed by an L-shaped "elbow"
   (top-left is canon). Elbows have: a horizontal arm (the title-bar height),
   a vertical arm (the button-column width), one large outer radius, and one
   smaller inner radius. All radii derive from a single base unit.
3. **Color = category.** Colors are not accents, they are semantics:
   orange/gold = primary actions & frame, blue/teal = data & science,
   purple/lilac = secondary nav, red = alert/engineering only.
4. **Typography is ultra-condensed and uppercase.** Swiss 911 Ultra Compressed
   on screen; use **Antonio** (Google Fonts, OFL) on the web. All labels
   uppercase with slight letter-spacing. Numbers are right-aligned.
5. **Black background always.** LCARS never uses white/gray page backgrounds.
   Panels are black; the interface is the colored frame + text.
6. **Flat only.** No gradients, no shadows, no 3D, no rounded-content-cards.
   The only rounded geometry is the frame system (elbows, pills, bar ends).

## Canon Color Palettes

Quick reference — full tables with all 4 canon eras + Picard/Lower Decks/
Nemesis Blue themes are in `references/color-palettes.md`.

**TNG 2369 palette (the classic Enterprise-D look) — use these first:**

| Name | Hex | Role |
|------|-----|------|
| golden-tanoi | `#FFCC66` | primary frame/elbow |
| tanoi | `#FFCC99` | frame secondary |
| neon-carrot | `#FF9933` | primary buttons |
| atomic-tangerine | `#FF9900` | active state |
| anakiwa | `#99CCFF` | data buttons / science |
| periwinkle | `#CCDDFF` | data text highlights |
| danub | `#6688CC` | secondary data |
| blue-bell | `#9999CC` | tertiary buttons |
| lilac | `#CC99CC` | nav / secondary |
| hopbush | `#CC6699` | nav accent |
| chestnut-rose | `#CC6666` | warning-adjacent |
| red-damask | `#DD6644` | engineering |
| orange-peel | `#FF9966` | frame accents |

Background: `#000000`. Default text: `#FF9900` (orange) or `#99CCFF` (data).

**Never invent off-palette colors.** If a shade isn't in the palette tables,
it isn't LCARS.

## Typography

```css
@import url('https://fonts.googleapis.com/css2?family=Antonio:wght@300;400;600;700&display=swap');

font-family: 'Antonio', 'Liberation Sans Narrow', 'Arial Narrow', sans-serif;
text-transform: uppercase;
letter-spacing: 0.05em;
```

- Titles: Antonio 600–700, size ~2–3rem.
- Button labels: Antonio 400–600, right-aligned or centered.
- Readout numbers: Antonio 300–400 (light weight reads as "computer text").
- Body text: avoid long prose; LCARS is labels + numbers + status lines.

## The Frame: Pure-CSS Elbow Construction

The elbow is a rounded rectangle with an inner black cutout via `::after`:

```css
.lcars-elbow {
  position: absolute;
  top: 16px; left: 16px;
  width: calc(var(--col-w) + 90px);
  height: calc(var(--bar-h) + 160px);
  background: var(--golden-tanoi);
  border-top-left-radius: 70px 50px;   /* outer radius */
}
.lcars-elbow::after {
  content: "";
  position: absolute;
  left: var(--col-w);                  /* vertical arm width */
  top: var(--bar-h);                   /* horizontal arm height */
  right: 0; bottom: 0;
  background: #000;                    /* cutout = page bg */
  border-top-left-radius: 35px 25px;   /* inner radius ~ half outer */
}
```

Layout shell: page padded `left: col-w + gap`, `top: bar-h + gap`; the title
bar sits right of the elbow's horizontal arm; content fills below. Button
column continues under the elbow's vertical arm. Full working geometry
(including bottom elbows, right elbows, and footer bars) is implemented in
`templates/lcars-components.css` — copy it, don't re-derive it.

**Radii pitfalls:**
- The inner cutout radius must be *smaller* than the outer radius, and its
  origin is offset by (col-w, bar-h) — otherwise the inner corner kinks.
- Keep arm thickness ≥ 32px or the elbow looks spindly at kiosk sizes.
- `border-radius: 70px 50px` (elliptical) looks more canon than circular.

## Animation Vocabulary

LCARS motion is *mechanical and instant-feeling* — panels snap, lights blink
in steps, sweeps are fast linear wipes. Full keyframes in
`references/animations.md`; the five canon moves:

1. **Boot sweep** — frame + panels wipe in left→right, staggered 40–80ms,
   `animation: lcars-wipe 300ms linear both` with `--i` stagger index.
2. **Status blink** — `steps(1)` hard blinking (no fade!) for indicators.
3. **Button press flash** — invert to white/bright for 120ms on `:active`.
4. **Readout tick** — numbers update via JS; no transition (instant change
   reads as computer-refresh; smooth counting looks wrong).
5. **Red alert** — swap palette CSS vars to reds + slow pulse on the frame
   (`animation: lcars-alert 1s steps(2) infinite`).

**Sound (optional but high-value):** procedural Web Audio beeps — no audio
files needed. A 1400–1800Hz sine burst, 40–80ms, with a fast pitch drop
reads as an authentic panel chirp. Snippet in `references/animations.md`.

## Workflow

1. **Pick the era/palette** — default to TNG 2369 (golden-tanoi frame).
   Use `scripts/build_palette.py <era>` to emit CSS custom properties for
   any canon era (2357, 2369, 2375, 2379, picard, lower-decks, nemesis-blue).
2. **Copy `templates/lcars-base.html`** for a minimal page, or
   **`templates/lcars-dashboard.html`** for a full animated sensor-style
   dashboard (boot sweep, blinking status, ticking readouts, beeps).
3. **Structure the screen**: top-left elbow + title bar → left button column
   → content panels → optional bottom elbow + status footer.
4. **Assign colors by function** (see grammar rule 3), not by taste.
5. **Add motion last**: boot sweep on load, blinks for live status, press
   flashes on buttons. Keep it under ~400ms total boot.
6. **Verify with the checklist below**, ideally with a browser screenshot.

## Component Recipes (all in templates/lcars-components.css)

- `.lcars-elbow` + `.elbow-tl/.elbow-tr/.elbow-bl/.elbow-br` — frame elbows
- `.lcars-bar` / `.bar-pill-l/.bar-pill-r` — title & footer bars
- `.lcars-btn` + `.btn-block/.btn-pill-l/.btn-pill-r` — buttons
- `.lcars-readout` — right-aligned numeric blocks with label strip
- `.lcars-panel` — black content panel with 2px colored frame
- `.lcars-status-dot` — blinking status indicators
- `.lcars-bg-*` / `.lcars-fg-*` — every canon color as utility classes
- `.lcars-sweep-in`, `.lcars-blink`, `.lcars-alert` — animation classes

## Pitfalls (Learned from Real LCARS Builds)

- **Don't use gradients/shadows** — instant canon-break. Okuda's panels were
  backlit film: flat light, flat color.
- **Don't round content panels** — only frame geometry is rounded. Content
  areas are sharp rectangles.
- **Don't smooth-fade blinks** — LCARS lights hard-switch. `steps(1)` or
  `steps(2)` only.
- **Don't center long text** — labels are right-aligned in elbows/columns,
  left-aligned in panels. Numbers always right-aligned.
- **Don't use white text on orange** at small sizes — use black text on
  orange/gold buttons (canon), orange text on black for readouts.
- **Mobile**: keep the elbow but shrink `--col-w`/`--bar-h` proportionally;
  the button column becomes a horizontal scroll row under the title bar.
- **Fonts**: if Google Fonts is unavailable (offline kiosk), Liberation Sans
  Narrow / Arial Narrow holds up; never fall back to a normal-width font —
  condensation is 50% of the LCARS look.

## Verification Checklist

- [ ] Black page background, no gradients/shadows anywhere
- [ ] Elbow radii: outer elliptical radius + smaller offset inner cutout
- [ ] All colors from canon palette tables (no invented hex values)
- [ ] Antonio (or narrow fallback) loaded; all labels uppercase
- [ ] Buttons have black text on colored bg; ≥32px hit targets
- [ ] Blinks use steps(), boot sweep < 400ms, no smooth fades
- [ ] Numbers right-aligned; labels uppercase with letter-spacing
- [ ] Screenshot at target display size: reads clearly from 2m away
  (Okuda's original NTSC readability test)

## Linked Files

- `references/color-palettes.md` — all canon palettes: 2357/2369/2375/2379
  full named tables, plus Picard, Lower Decks, Lower Decks PADD, Nemesis Blue,
  and Classic (thelcars.com) themes, as CSS custom properties.
- `references/design-system.md` — deep dive on Okuda's grammar: geometry math,
  layout patterns (bridge console, PADD, wall panel), typography scale,
  color semantics by department.
- `references/animations.md` — full keyframes library: boot sweep variants,
  blinks, sweeps, alert modes, readout patterns, Web Audio beep snippets.
- `templates/lcars-base.html` — minimal single-file starter (elbow + bar +
  buttons + one panel), embedded CSS, no dependencies beyond the font.
- `templates/lcars-components.css` — the full component library with all
  color utility classes and animation classes.
- `templates/lcars-dashboard.html` — complete animated dashboard: boot sweep,
  live-ticking readouts, blinking status, CSS bar chart, procedural beeps.
- `scripts/build_palette.py` — emit CSS custom properties for any canon era:
  `python3 build_palette.py 2369 > palette.css`
