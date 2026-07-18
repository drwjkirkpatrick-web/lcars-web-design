#!/usr/bin/env python3
"""
build_palette.py — Emit LCARS CSS custom properties for any canon era.

Usage:
    python3 build_palette.py 2369            # TNG classic (default)
    python3 build_palette.py 2357            # early TNG
    python3 build_palette.py picard          # ST:P modern theme
    python3 build_palette.py lower-decks     # Lower Decks bright theme
    python3 build_palette.py nemesis-blue    # Nemesis blue variant
    python3 build_palette.py --list          # list available palettes

Output goes to stdout — redirect into your stylesheet:
    python3 build_palette.py 2369 > lcars-palette.css

Palettes verified against trekcolors (leonawicz) + thelcars.com theme guide.
"""

import sys

# Canon palettes: name -> hex. Keep in sync with references/color-palettes.md.
PALETTES = {
    "2357": {
        "pale-canary": "#FFFF99", "tanoi": "#FFCC99", "golden-tanoi": "#FFCC66",
        "neon-carrot": "#FF9933", "eggplant": "#664466", "lilac": "#CC99CC",
        "anakiwa": "#99CCFF", "mariner": "#3366CC", "bahama-blue": "#006699",
    },
    "2369": {
        "pale-canary": "#FFFF99", "tanoi": "#FFCC99", "golden-tanoi": "#FFCC66",
        "neon-carrot": "#FF9933", "atomic-tangerine": "#FF9900",
        "orange-peel": "#FF9966", "anakiwa": "#99CCFF", "periwinkle": "#CCDDFF",
        "dodger-pale": "#5599FF", "dodger-soft": "#3366FF", "danub": "#6688CC",
        "blue-bell": "#9999CC", "mariner": "#3366CC", "bahama-blue": "#006699",
        "indigo": "#4455BB", "near-blue": "#0011EE", "navy-blue": "#000088",
        "lilac": "#CC99CC", "melrose": "#9999FF", "hopbush": "#CC6699",
        "lavender-purple": "#9977AA", "cosmic": "#774466", "eggplant": "#664466",
        "chestnut-rose": "#CC6666", "red-damask": "#DD6644",
        "medium-carmine": "#AA5533", "bourbon": "#BB6622",
        "sandy-brown": "#EE9955", "rust": "#BB4411", "tamarillo": "#882211",
        "husk": "#BBAA55",
    },
    # 2375/2379 share 2369 names; composition differs (see color-palettes.md)
    "2375": None,  # alias -> 2369
    "2379": None,  # alias -> 2369
    "picard": {
        "blue": "#37A6D1", "bright-blue": "#41C4F7", "dark-blue": "#1C3C55",
        "dark-gray": "#2F3749", "ghost-gray": "#D2D5DF", "light-gray": "#9EA5BA",
        "light-orange-red": "#FF6753", "medium-dark-blue": "#2A7193",
        "medium-dark-gray": "#52596E", "orange-red": "#E7442A",
        "pale-orange-red": "#FF977B", "primary-gray": "#6D748C",
        "starlight": "#F3F4F7",
    },
    "lower-decks": {
        "butter": "#FFEECC", "daybreak": "#FF9911", "harvestgold": "#FFAA44",
        "honey": "#FFCC99", "october-sunset": "#FF4400", "orange": "#FF7700",
        "pumpkin-pie": "#CC5500",
    },
    "lower-decks-padd": {
        "alpha-blue": "#5588EE", "arctic-ice": "#66CCFF", "arctic-snow": "#99CCFF",
        "beta-blue": "#7799DD", "night-cloud": "#344470", "night-rain": "#455580",
        "radioactive": "#88EEFF", "starship-white": "#F3F3FC",
        "sunset-red": "#FF3500",
    },
    "nemesis-blue": {
        "bronze": "#B88B5C", "cardinal": "#DA2537", "cool": "#6699FF",
        "copper": "#C16C3D", "evening": "#2266FF", "galaxy-gray": "#52526A",
        "ghost": "#88BBFF", "grape": "#9966CC", "honey": "#FFCC99",
        "martian": "#99CC33", "midnight": "#0048F0", "moonbeam": "#EBF0FF",
        "pumpkin": "#E63D00", "tangerine": "#FF8833",
        "washed-pumpkin": "#FF7744", "wheat": "#D1A16C",
    },
}
PALETTES["2375"] = PALETTES["2369"]
PALETTES["2379"] = PALETTES["2369"]

# Geometry defaults emitted with every palette (design-system.md §2)
GEOMETRY = {
    "bar-h": "90px", "col-w": "150px", "gap": "8px",
    "r-outer": "70px 50px", "r-inner": "35px 25px",
}


def emit(era: str) -> str:
    pal = PALETTES[era]
    prefix = "lcars" if era in ("2357", "2369", "2375", "2379") else f"lcars-{era.split('-')[0]}"
    lines = [f":root {{ /* LCARS palette: {era} */"]
    for name, hexval in pal.items():
        lines.append(f"  --{prefix}-{name}: {hexval};")
    for name, val in GEOMETRY.items():
        lines.append(f"  --lcars-{name}: {val};")
    lines.append("}")
    return "\n".join(lines)


def main(argv):
    if len(argv) < 2 or argv[1] in ("--list", "-l"):
        print("Available palettes:", ", ".join(sorted(PALETTES)))
        return
    era = argv[1].lower()
    if era not in PALETTES:
        print(f"Unknown era '{era}'. Use --list.", file=sys.stderr)
        sys.exit(1)
    print(emit(era))


if __name__ == "__main__":
    main(sys.argv)
