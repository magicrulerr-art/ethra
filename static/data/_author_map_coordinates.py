"""Author map-coordinates.json — single source of truth for the bestiary map.

Run once. Re-run only when adding new creatures or repositioning dots.
Coordinates (x_pct, y_pct) are hand-curated against lore localization
on the 24:10 panorama map. y grows downward (top of map = 0).

Layout summary:
  Rune Belt    -> temperate central-west  (x ≈ 28..48, y ≈ 35..60)
  Steadfast    -> hot south-central plain (x ≈ 38..62, y ≈ 60..80)
  Umbral Ring  -> coastal/twilight SSW    (x ≈ 12..28, y ≈ 65..88)
  Flickermarch -> marshland NE           (x ≈ 60..82, y ≈ 18..38)
  Tidepools    -> intertidal S coast     (x ≈ 60..80, y ≈ 80..92)
  Underground  -> cave glyph bottom-R    (x ≈ 84..96, y ≈ 78..95)
"""
import json
import os

OUT = r"C:\Users\magic\.copaw\workspaces\default\ethra_site\static\data\map-coordinates.json"

data = {
    "schema_version": 1,
    "comment": (
        "Hand-curated creature placement on the Ethra supercontinent panorama. "
        "x_pct/y_pct are 0..100 along the map's aspect-ratio 24:10 canvas. "
        "To add a creature: append an entry with the next free slot. "
        "To add a city_pin (future culture/society revamp): append to city_pins."
    ),
    "biomes": [
        {"slug": "rune-belt",      "name": "Rune Belt",       "region_x": 38, "region_y": 47},
        {"slug": "steadfast-desert","name": "Steadfast Desert","region_x": 50, "region_y": 70},
        {"slug": "umbral-ring",    "name": "Umbral Ring",     "region_x": 20, "region_y": 76},
        {"slug": "flickermarch",   "name": "Flickermarch",    "region_x": 71, "region_y": 28},
        {"slug": "tidepools",      "name": "Tidepools",       "region_x": 70, "region_y": 86},
        {"slug": "underground",    "name": "Underground",     "region_x": 90, "region_y": 86}
    ],
    "creatures": [
        # ─── Rune Belt ───────────────────────────────────────────────
        {"kind": "race",   "biome": "rune-belt", "slug": "wengari",     "name": "Wengari (Anchor Race)",
         "x_pct": 32, "y_pct": 44, "image_full": "/static/images/tide-wolf.png",
         "subtitle": "Bright Paws / Shadow Paws / Mottled Paws / Stripe Paws / Snow Paws"},
        {"kind": "creature","biome": "rune-belt", "slug": "tide-wolf",  "name": "Tide Wolf",
         "x_pct": 36, "y_pct": 50, "image_full": "/static/images/tide-wolf.png"},
        {"kind": "creature","biome": "rune-belt", "slug": "black-fire-tide-wolf","name": "Black-Fire Tide Wolf",
         "x_pct": 33, "y_pct": 55, "image_full": "/static/images/black-fire-tide-wolf.png"},
        {"kind": "creature","biome": "rune-belt", "slug": "amuk",       "name": "Amuk",
         "x_pct": 41, "y_pct": 42, "image_full": "/static/images/amuk-v10.png"},
        {"kind": "creature","biome": "rune-belt", "slug": "ghost",      "name": "Ghost",
         "x_pct": 44, "y_pct": 48, "image_full": "/static/images/ghost-v3.png"},
        {"kind": "creature","biome": "rune-belt", "slug": "lotus-bloom","name": "Lotus Bloom",
         "x_pct": 47, "y_pct": 55, "image_full": "/static/images/lotus-bloom.png"},
        {"kind": "creature","biome": "rune-belt", "slug": "woh",        "name": "Woh",
         "x_pct": 39, "y_pct": 58, "image_full": "/static/images/woh.png"},
        {"kind": "race",   "biome": "rune-belt", "slug": "humann",      "name": "Humman",
         "x_pct": 45, "y_pct": 53, "image_full": "/static/images/humann.png",
         "subtitle": "Youngest sentient race — mercantile empire"},
        # ─── Steadfast Desert ────────────────────────────────────────
        {"kind": "race",   "biome": "steadfast-desert","slug": "pyrinae","name": "Pyrinae",
         "x_pct": 50, "y_pct": 67, "image_full": "/static/images/pyrinae.png",
         "subtitle": "Rune-glass artisans, Hydromancers"},
        {"kind": "creature","biome": "steadfast-desert","slug": "styx","name": "Styx",
         "x_pct": 48, "y_pct": 70, "image_full": "/static/images/styx.png"},
        {"kind": "creature","biome": "steadfast-desert","slug": "bright-paw","name": "Bright Paw",
         "x_pct": 53, "y_pct": 64, "image_full": "/static/images/bright-paw.png"},
        {"kind": "creature","biome": "steadfast-desert","slug": "stripe-paw","name": "Stripe Paw",
         "x_pct": 44, "y_pct": 62, "image_full": "/static/images/stripe-paw.png"},
        {"kind": "creature","biome": "steadfast-desert","slug": "shadow-paw","name": "Shadow Paw",
         "x_pct": 40, "y_pct": 65, "image_full": "/static/images/shadow-paw.png"},
        {"kind": "creature","biome": "steadfast-desert","slug": "mottled-paw","name": "Mottled Paw",
         "x_pct": 56, "y_pct": 70, "image_full": "/static/images/mottled-paw.png"},
        {"kind": "creature","biome": "steadfast-desert","slug": "kyre-tree","name": "The Kyre Tree",
         "x_pct": 60, "y_pct": 76, "image_full": "/static/images/kyre-tree.png",
         "subtitle": "Ancient predator-god; bargainer"},
        {"kind": "creature","biome": "steadfast-desert","slug": "desert-woh","name": "Desert Woh",
         "x_pct": 47, "y_pct": 76, "image_full": "/static/images/desert-woh.png"},
        {"kind": "creature","biome": "steadfast-desert","slug": "fire-beetle","name": "Fire Beetle",
         "x_pct": 51, "y_pct": 80, "image_full": "/static/images/fire-beetle.png"},
        {"kind": "creature","biome": "steadfast-desert","slug": "razor-hare","name": "Razor Hare",
         "x_pct": 56, "y_pct": 80, "image_full": "/static/images/razor-hare.png"},
        # ─── Umbral Ring ─────────────────────────────────────────────
        {"kind": "race",   "biome": "umbral-ring","slug": "dragari","name": "Dragari",
         "x_pct": 18, "y_pct": 72, "image_full": "/static/images/dragari.png",
         "subtitle": "Ancient gentle sea-singers; one of Ethra's oldest races"},
        {"kind": "creature","biome": "umbral-ring","slug": "auruch","name": "Auruch",
         "x_pct": 14, "y_pct": 80, "image_full": "/static/images/auruch.png",
         "subtitle": "Giant sea-creatures revered by the Dragari"},
        {"kind": "creature","biome": "umbral-ring","slug": "sea-marsh-dragari","name": "Sea Marsh (Dragari cultivar)",
         "x_pct": 24, "y_pct": 84, "image_full": "/static/images/sea-marsh.png"},
        {"kind": "creature","biome": "umbral-ring","slug": "sea-marsh-veylar","name": "Sea Marsh (Veylar cultivar)",
         "x_pct": 27, "y_pct": 78, "image_full": "/static/images/sea-marsh.png"},
        # ─── Flickermarch ────────────────────────────────────────────
        {"kind": "race",   "biome": "flickermarch","slug": "threx","name": "Threx",
         "x_pct": 70, "y_pct": 26, "image_full": "/static/images/lament.png",
         "subtitle": "Mycelial beings, connected to the Deep"},
        {"kind": "creature","biome": "flickermarch","slug": "lament","name": "The Lament",
         "x_pct": 73, "y_pct": 28, "image_full": "/static/images/lament.png"},
        {"kind": "creature","biome": "flickermarch","slug": "iris-serpent","name": "Iris Serpent",
         "x_pct": 64, "y_pct": 32, "image_full": "/static/images/iris-serpent.png"},
        {"kind": "creature","biome": "flickermarch","slug": "mycelial-deep","name": "The Mycelial Deep",
         "x_pct": 78, "y_pct": 32, "image_full": "/static/images/mycelial-deep.png"},
        {"kind": "creature","biome": "flickermarch","slug": "pearly-scorpion","name": "Pearly Scorpion",
         "x_pct": 68, "y_pct": 22, "image_full": "/static/images/pearly-scorpion.png"},
        {"kind": "creature","biome": "flickermarch","slug": "quick-threx","name": "Quick Threx",
         "x_pct": 64, "y_pct": 26, "image_full": "/static/images/quick-threx.png"},
        {"kind": "creature","biome": "flickermarch","slug": "rooted-threx","name": "Rooted Threx",
         "x_pct": 76, "y_pct": 22, "image_full": "/static/images/rooted-threx.png"},
        # ─── Tidepools ───────────────────────────────────────────────
        {"kind": "race",   "biome": "tidepools","slug": "veylar","name": "Veylar",
         "x_pct": 70, "y_pct": 84, "image_full": "/static/images/shell-singer.png",
         "subtitle": "Aquatic patient Shell-Singers; 20,000-year civilization"},
        {"kind": "creature","biome": "tidepools","slug": "shell-singer","name": "Shell-Singer",
         "x_pct": 66, "y_pct": 88, "image_full": "/static/images/shell-singer.png"},
        {"kind": "creature","biome": "tidepools","slug": "abyssal-heart","name": "Abyssal Heart",
         "x_pct": 74, "y_pct": 90, "image_full": "/static/images/abyssal-heart.png"},
        {"kind": "creature","biome": "tidepools","slug": "coral-citadel","name": "Coral Citadel",
         "x_pct": 78, "y_pct": 86, "image_full": "/static/images/coral-citadel.png"}
    ],
    "underground_cave": {
        "kind": "cave",
        "biome": "underground",
        "slug": "underground-cave",
        "name": "The Underground (cave)",
        "x_pct": 90,
        "y_pct": 90,
        "subtitle": "2 creatures available",
        "constituents": [
            {"slug": "chithak",         "name": "The Chi'Thak (Blight)",
             "image_full": "/static/images/lament.png"},
            {"slug": "super-organism",  "name": "Super-Organism",
             "image_full": "/static/images/mycelial-deep.png"}
        ]
    },
    "city_pins": []
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Verify
with open(OUT, "r", encoding="utf-8") as f:
    parsed = json.load(f)
print(f"WROTE {OUT}")
print(f"  biomes:           {len(parsed['biomes'])}")
print(f"  creatures:        {len(parsed['creatures'])}")
print(f"  underground cave: {len(parsed['underground_cave']['constituents'])}")
print(f"  city_pins:        {len(parsed['city_pins'])} (placeholder for later)")
