# LCARS Animation & Sound Library

Canon LCARS motion is mechanical: panels snap, lights hard-blink, data
ticks instantly, and full-screen transitions are fast linear wipes.
Nothing eases like a phone app. All timings below are calibrated to
match the on-screen feel.

## The Five Canon Moves

### 1. Boot Sweep (page load)

Frame lights first, then the button column top-to-bottom, then content
panels left-to-right. Stagger 40–80ms per element, each element wipes
in over 150–300ms, `linear`.

```css
@keyframes lcars-wipe {
  from { clip-path: inset(0 100% 0 0); opacity: 0.4; }
  to   { clip-path: inset(0 0% 0 0);   opacity: 1; }
}

.lcars-sweep-in {
  animation: lcars-wipe 280ms linear both;
  animation-delay: calc(var(--i, 0) * 60ms); /* set --i: 0,1,2... per element */
}
```

Usage: `<div class="lcars-sweep-in" style="--i:3">...</div>`

Variant — vertical wipe for the title bar:

```css
@keyframes lcars-wipe-down {
  from { clip-path: inset(0 0 100% 0); opacity: 0.4; }
  to   { clip-path: inset(0 0 0% 0);   opacity: 1; }
}
```

### 2. Status Blink (indicators)

Hard switching only — `steps()` timing. No opacity fades.

```css
@keyframes lcars-blink {
  0%, 49%  { opacity: 1; }
  50%, 100%{ opacity: 0.15; } /* dim, not fully off: reads as lit-LED */
}

.lcars-blink        { animation: lcars-blink 1s steps(1) infinite; }
.lcars-blink-fast   { animation: lcars-blink 0.5s steps(1) infinite; }
.lcars-blink-slow   { animation: lcars-blink 2s steps(1) infinite; }
```

For two-color status lights (e.g., green/amber alternating):

```css
@keyframes lcars-alt {
  0%, 49%  { background: var(--lcars-anakiwa); }
  50%, 100%{ background: var(--lcars-golden-tanoi); }
}
.lcars-alt { animation: lcars-alt 1.2s steps(1) infinite; }
```

### 3. Button Press Flash

Invert to bright on `:active` for ~120ms — the "panel chirp" visual half.

```css
.lcars-btn:active {
  background: var(--lcars-pale-canary) !important;
  color: #000 !important;
  transition: none; /* instant on */
}
```

For a programmatic flash (JS-triggered acknowledge):

```css
@keyframes lcars-flash {
  0% { filter: brightness(1.8); }
  100% { filter: brightness(1); }
}
.lcars-flash { animation: lcars-flash 150ms linear; }
```

### 4. Readout Tick

Numbers change **instantly** on update — no counting animation, no
transition. Smooth counting reads as a phone widget; instant change
reads as a computer refresh. If a value updates faster than ~2Hz, gate
it in JS to 1–2Hz (canon displays update at stately pace).

```js
// Canon-correct readout update: instant text swap, throttled
function tickReadout(el, value, decimals = 1) {
  el.textContent = value.toFixed(decimals); // no transition, ever
}
// caller: setInterval(() => tickReadout(el, readSensor()), 500);
```

For "scrolling" data columns (sensor logs), prepend rows and let the
column grow/shift instantly — or use a fast linear marquee:

```css
@keyframes lcars-scroll {
  from { transform: translateY(0); }
  to   { transform: translateY(-50%); }
}
.lcars-scroll-col {
  animation: lcars-scroll 20s linear infinite; /* duplicate content 2x */
}
```

### 5. Red Alert Mode

Palette swap + slow frame pulse. Apply `.lcars-alert-mode` (from
color-palettes.md) to the root element, then:

```css
@keyframes lcars-alert-pulse {
  0%, 49%  { filter: brightness(1); }
  50%, 100%{ filter: brightness(1.35); }
}
.lcars-alert-mode .lcars-elbow,
.lcars-alert-mode .lcars-bar {
  animation: lcars-alert-pulse 1s steps(2) infinite;
}
```

Optional klaxon (Web Audio, procedural — no files):

```js
function lcarsKlaxon(ctx) {
  // Two-tone sweep, ~0.8s, classic red-alert feel
  const o = ctx.createOscillator(), g = ctx.createGain();
  o.type = 'sawtooth';
  o.frequency.setValueAtTime(600, ctx.currentTime);
  o.frequency.linearRampToValueAtTime(900, ctx.currentTime + 0.4);
  o.frequency.linearRampToValueAtTime(600, ctx.currentTime + 0.8);
  g.gain.setValueAtTime(0.04, ctx.currentTime);
  g.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.8);
  o.connect(g).connect(ctx.destination);
  o.start(); o.stop(ctx.currentTime + 0.8);
}
```

## Procedural Panel Beeps (Web Audio — no audio files)

The authentic TNG panel chirp is a short sine burst with a fast downward
pitch drop. Generate it; never ship MP3s.

```js
let _lcarsAudioCtx = null;
function lcarsBeep(freq = 1600, dur = 0.06) {
  // Must be called from a user gesture at least once (browser autoplay policy)
  _lcarsAudioCtx = _lcarsAudioCtx || new (window.AudioContext || window.webkitAudioContext)();
  const ctx = _lcarsAudioCtx;
  const o = ctx.createOscillator(), g = ctx.createGain();
  o.type = 'sine';
  o.frequency.setValueAtTime(freq, ctx.currentTime);
  o.frequency.exponentialRampToValueAtTime(freq * 0.6, ctx.currentTime + dur);
  g.gain.setValueAtTime(0.06, ctx.currentTime);
  g.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + dur);
  o.connect(g).connect(ctx.destination);
  o.start(); o.stop(ctx.currentTime + dur);
}

// Canon variants:
//   lcarsBeep(1600, 0.05)  — standard button chirp
//   lcarsBeep(2200, 0.04)  — higher "confirm" chirp
//   lcarsBeep(900, 0.09)   — lower "denied/alert" bonk
//   Two beeps 60ms apart   — "acknowledged" double-chirp
```

Wire-up:

```js
document.querySelectorAll('.lcars-btn').forEach(b =>
  b.addEventListener('click', () => lcarsBeep(1600, 0.05)));
```

## Boot Sequence Orchestration (putting it together)

```js
// Assign stagger indices in DOM order, then release the sweep.
// Keep total boot under ~400ms + last element's 280ms wipe.
document.querySelectorAll('.lcars-boot').forEach((el, i) => {
  el.style.setProperty('--i', i);
  el.classList.add('lcars-sweep-in');
});
```

Order in markup: elbow → title bar → column buttons → panels → footer.
That DOM order IS the light-up order.

## Reduced Motion

Honor `prefers-reduced-motion`: keep blinks (functional status) but
kill sweeps and scrolls.

```css
@media (prefers-reduced-motion: reduce) {
  .lcars-sweep-in { animation: none; }
  .lcars-scroll-col { animation: none; }
  .lcars-alert-mode .lcars-elbow,
  .lcars-alert-mode .lcars-bar { animation: none; }
}
```

## Timing Reference Card

| Effect | Duration | Timing | Repeat |
|--------|----------|--------|--------|
| Boot wipe per element | 280ms | linear | once |
| Boot stagger | 60ms | — | — |
| Status blink | 500–2000ms | steps(1) | infinite |
| Press flash | 120–150ms | linear | once |
| Alert pulse | 1000ms | steps(2) | infinite |
| Data scroll | 15–30s | linear | infinite |
| Button chirp | 40–90ms | — | per press |
