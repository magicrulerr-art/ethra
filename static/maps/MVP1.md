# ETHRA MAP — MVP #1 (frozen 2026-08-21)

Ainz-sama approved this state with "I love it". It is the reference baseline;
refinements must never regress it. Restore by copying the .mvp1 files back over
the live ones.

## Frozen artifacts
- `static/ethra_map_standalone.mvp1.html`  (22,085 B) — the live /map/ page as approved
- `static/maps/ethra_canon_mvp1.svg`       (3,658,828 B) — canon map v3 (painted base, self-contained)
- also on disk: `ethra_map_standalone.html.bak.before-ux-rev` (pre-UX-revamp backup)

## What MVP #1 contains (verified by probes + Ainz's eyes)
- Painted base plate + ocean are PERMANENT (no toggles); 9 overlay toggles:
  Biome Tints (default off) · Routes · Underground inset · Cities · Races ·
  Creatures · Labels · Caption · Legend — all flip cleanly.
- Pan/zoom: drag, wheel-to-cursor, double-click, +/−/⌂ buttons.
- Hover: cities/races mini tooltip; creatures & races show bestiary plate image.
- Click: cities → canon dossier w/ plate image; races & creatures → full fetched
  bestiary entry (`/api/creature/<biome>/<slug>`) + plate; Wengari falls back to
  embedded canon text. Name labels and 24-unit invisible hit zones are interactive.
- Technical canon: SVG injected via DOMParser('image/svg+xml') + importNode
  (innerHTML would rewrite <image>→<img> and drop the painted plate).

## Refinement backlog (candidates for post-MVP work)
1. Underground "peel the surface" view (landmass swap) — Ainz's earlier conditional.
2. Faiths overlay layer (5 faiths: Testing Fire · Cosmic Calendar · Great Song ·
   The Feast · The Shadow) — present in dossiers only, not yet a map layer.
3. Search / jump-to box (creature, city, biome).
4. Toggle-state persistence (localStorage) + deep links (?layer=…).
5. Route dossiers with real lore (currently one-line).
6. Label declutter / zoom-dependent label density at fit zoom.
7. Touch / mobile gestures.
