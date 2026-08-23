# MVP #2 — Frozen Restore Point (2026-08-21)

Approved direction: Ainz said "Let's do all" (7-item backlog) + added refinement #8 (Twin Suns banner).

## Frozen artifacts
- `static/ethra_map_standalone.mvp2.html` — exact copy of the live page at freeze time.
- `static/maps/ethra_canon_v1.svg` — unchanged canon SVG (3,658,828 bytes), shared with MVP #1.
- `static/maps/base_ethra_underground.png` — NEW painted underground plate (2,564,421 bytes, Qwen-Image 2048×854), referenced by the Peel view.
- `static/maps/ethra_canon_mvp1.svg` + `static/ethra_map_standalone.mvp1.html` — MVP #1, untouched.

## Restore instructions
- To MVP #2: copy `ethra_map_standalone.mvp2.html` over `ethra_map_standalone.html`.
- To MVP #1: copy `ethra_map_standalone.mvp1.html` over `ethra_map_standalone.html`.
Neither touches the canon SVG or the underground plate.

## What MVP #2 added (all verified 2026-08-21)
1. **Peel the Surface (underground view)** — toggle swaps the painted landmass `href` to `base_ethra_underground.png`, hides surface-only layers (biomes, routes, cities, races, creatures, faiths, labels, caption, legend), shows Deep Veins + Underground inset; unpeeling restores everything. Persisted across reload via localStorage.
2. **The Faiths overlay** — runtime `layer-faiths`: 6 star markers + labels (Testing Fire, Cosmic Calendar, Great Song, The Feast, The Shadow, The Abyss) with click dossiers.
3. **Search / jump** — seek box with 44-entry datalist (cities, races, creatures, faiths, biomes); Enter flies to the pin and opens its dossier (verified with "lament" → full canon dossier).
4. **Persistence + deep links** — localStorage key `ethraMapMvp2`; URL params `?on=`, `?off=` (short layer ids), `?peel=1`.
5. **Route lore** — all 6 routes have canon-flavored dossier text on click.
6. **Label declutter** — creature labels hidden below scale 0.8 (`#stage.declutter`), reappear on zoom-in.
7. **Pinch gestures** — two-pointer pinch zoom + pan via pointer-event map (kept drag/scroll/dblclick intact).
8. **Twin Suns banner** — top-center banner: Steadfast (gold) + Flicker (crimson) glyphs with lore lines and Convergence note.

## Verification evidence (headless browser probes)
- faithsLayer=1, deepLayer=1, 12 faith elements, 8 deep nodes, 12 legend rows, banner present.
- Peel: href → underground PNG, biomes/legend hidden, deep shown; restore returns data-URI href.
- Search: 'lament' → dossier with canon line "L'vat is a known Lament who trained Ajani…".
- Reload with peel on: state persisted from localStorage.
- All endpoints 200: /map/, underground PNG, canon SVG, creature API.

## Known sharp edges
- The underground plate is a new painting, not a traced silhouette of the surface continent; coasts differ by design (it is cavern-country).
- Deep veins/nodes are schematic placeholders in canon-flavored positions; if Ainz wants forged underground map art per region, that is the next step.
- `?on=`/`?off=` expect short ids (biomes, routes, faiths, deep, labels, caption, legend, underground, cities, races, creatures).
