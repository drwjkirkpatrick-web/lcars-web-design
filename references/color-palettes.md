# LCARS Canon Color Palettes

All palettes verified against the trekcolors canon set (leonawicz/trekcolors,
which encodes the established fan-canon LCARS color names) and thelcars.com
theme guide (updated 2026). Use these exact hex values — never approximate.

## Usage

Copy the CSS custom property block for your chosen era into your stylesheet
`:root`, or generate it with `scripts/build_palette.py <era>`.

---

## TNG 2357 (Early TNG / Season 1–2 look)

Fewer colors, simpler screens.

```css
:root {
  --lcars-pale-canary:  #FFFF99;
  --lcars-tanoi:        #FFCC99;
  --lcars-golden-tanoi: #FFCC66;
  --lcars-neon-carrot:  #FF9933;
  --lcars-eggplant:     #664466;
  --lcars-lilac:        #CC99CC;
  --lcars-anakiwa:      #99CCFF;
  --lcars-mariner:      #3366CC;
  --lcars-bahama-blue:  #006699;
}
```

## TNG 2369 (Classic Enterprise-D — THE DEFAULT)

The full canonical palette. This is the one to use unless the user asks
for a different era.

```css
:root {
  /* Golds & oranges — frames, primary actions */
  --lcars-pale-canary:      #FFFF99;
  --lcars-tanoi:            #FFCC99;
  --lcars-golden-tanoi:     #FFCC66;
  --lcars-neon-carrot:      #FF9933;
  --lcars-atomic-tangerine: #FF9900;
  --lcars-orange-peel:      #FF9966;

  /* Blues — data, science, information */
  --lcars-anakiwa:          #99CCFF;
  --lcars-periwinkle:       #CCDDFF;
  --lcars-dodger-pale:      #5599FF;
  --lcars-dodger-soft:      #3366FF;
  --lcars-danub:            #6688CC;
  --lcars-blue-bell:        #9999CC;
  --lcars-mariner:          #3366CC;
  --lcars-bahama-blue:      #006699;
  --lcars-indigo:           #4455BB;
  --lcars-near-blue:        #0011EE;
  --lcars-navy-blue:        #000088;

  /* Purples & pinks — navigation, secondary */
  --lcars-lilac:            #CC99CC;
  --lcars-melrose:          #9999FF;
  --lcars-hopbush:          #CC6699;
  --lcars-lavender-purple:  #9977AA;
  --lcars-cosmic:           #774466;
  --lcars-eggplant:         #664466;

  /* Reds & browns — engineering, alert, warning */
  --lcars-chestnut-rose:    #CC6666;
  --lcars-red-damask:       #DD6644;
  --lcars-medium-carmine:   #AA5533;
  --lcars-bourbon:          #BB6622;
  --lcars-sandy-brown:      #EE9955;
  --lcars-rust:             #BB4411;
  --lcars-tamarillo:        #882211;
  --lcars-husk:             #BBAA55;
}
```

## TNG 2375 (Later TNG films era)

Same names, plus wider blue/red usage — use the 2369 table; era difference
is compositional (more danub/blue-bell, less gold), not new colors.

## TNG 2379 (Nemesis era)

Cooler overall: favor anakiwa, danub, blue-bell, indigo for frames; gold
reserved for alerts/primary only.

---

## Picard Theme (ST:P modern look — darker, flatter)

```css
:root {
  --lcars-p-blue:             #37A6D1;
  --lcars-p-bright-blue:      #41C4F7;
  --lcars-p-dark-blue:        #1C3C55;
  --lcars-p-dark-gray:        #2F3749;
  --lcars-p-ghost-gray:       #D2D5DF;
  --lcars-p-light-gray:       #9EA5BA;
  --lcars-p-light-orange-red: #FF6753;
  --lcars-p-med-dark-blue:    #2A7193;
  --lcars-p-med-dark-gray:    #52596E;
  --lcars-p-orange-red:       #E7442A;
  --lcars-p-pale-orange-red:  #FF977B;
  --lcars-p-primary-gray:     #6D748C;
  --lcars-p-starlight:        #F3F4F7;
}
```

## Lower Decks Theme (bright, orange-forward, playful)

```css
:root {
  --lcars-ld-butter:         #FFEECC;
  --lcars-ld-daybreak:       #FF9911;
  --lcars-ld-harvestgold:    #FFAA44;
  --lcars-ld-honey:          #FFCC99;
  --lcars-ld-october-sunset: #FF4400;
  --lcars-ld-orange:         #FF7700;
  --lcars-ld-pumpkin-pie:    #CC5500;
}
```

## Lower Decks PADD Theme (blue-forward handheld look)

```css
:root {
  --lcars-ldp-alpha-blue:     #5588EE;
  --lcars-ldp-arctic-ice:     #66CCFF;
  --lcars-ldp-arctic-snow:    #99CCFF;
  --lcars-ldp-beta-blue:      #7799DD;
  --lcars-ldp-night-cloud:    #344470;
  --lcars-ldp-night-rain:     #455580;
  --lcars-ldp-radioactive:    #88EEFF;
  --lcars-ldp-starship-white: #F3F3FC;
  --lcars-ldp-sunset-red:     #FF3500;
}
```

## Nemesis Blue Theme (cool blue command variant)

```css
:root {
  --lcars-nb-bronze:         #B88B5C;
  --lcars-nb-cardinal:       #DA2537;
  --lcars-nb-cool:           #6699FF;
  --lcars-nb-copper:         #C16C3D;
  --lcars-nb-evening:        #2266FF;
  --lcars-nb-galaxy-gray:    #52526A;
  --lcars-nb-ghost:          #88BBFF;
  --lcars-nb-grape:          #9966CC;
  --lcars-nb-honey:          #FFCC99;
  --lcars-nb-martian:        #99CC33;
  --lcars-nb-midnight:       #0048F0;
  --lcars-nb-moonbeam:       #EBF0FF;
  --lcars-nb-pumpkin:        #E63D00;
  --lcars-nb-tangerine:      #FF8833;
  --lcars-nb-washed-pumpkin: #FF7744;
  --lcars-nb-wheat:          #D1A16C;
}
```

---

## Semantic Assignment Cheat-Sheet

| Function | Color family | Canon picks |
|----------|-------------|-------------|
| Main frame/elbow | gold | golden-tanoi, tanoi |
| Primary buttons | orange | neon-carrot, atomic-tangerine |
| Data display | light blue | anakiwa, periwinkle |
| Secondary data | medium blue | danub, blue-bell, dodger-pale |
| Navigation | purple/pink | lilac, hopbush, melrose |
| Engineering | red-orange | red-damask, chestnut-rose |
| Alert only | red/bright orange | red-damask, near-blue flash |
| Background | — | #000000 only |
| Default text | orange/blue | atomic-tangerine, anakiwa |

## Alert Palette Swap (Red Alert Mode)

```css
.lcars-alert-mode {
  --lcars-golden-tanoi: #DD6644;
  --lcars-tanoi:        #CC6666;
  --lcars-neon-carrot:  #DD6644;
  --lcars-anakiwa:      #CC99CC;
}
```
