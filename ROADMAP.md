# ETHRA — Future-Proofing Roadmap (audit of 2026-08-23)

Commissioned by Ainz-sama: audit backend + design; make adding content as safe
as the creature drop-in; never risk breaking everything again.
Full findings were presented in chat; this file is the actionable plan.

## Status (updated 2026-08-23, round 22)

- **P0 — DONE** (commits `ebbd6a8`, `d608a9f`): git baseline + remote push;
  smoke suite (now 36 checks); regenerate_chapters.py repaired (script-relative
  paths, manifest-driven, non-destructive).
- **P1 — DONE** (commit `ef82fbb`): places drop-in live — six canonical city
  files in `content/places/` drive `/api/places`, `/api/place/<slug>`, the
  gold city diamonds + gazetteer overlay on the main site, and the dossier
  layer of the canon viewer; creature map coords moved into creature-file
  frontmatter (36 files; JSON demoted to override-only, regression-verified
  byte-identical); arcs manifest + world auto-discovery.
- **P1.5 — DONE** (this round): `tools/export_static.py` bakes the whole site
  (119 documents: landing, viewer, every API response, static tree) into
  `_pages/` rooted at `/ethra/`; verified locally via
  `tools/serve_pages_test.py` + `probe_pages.py` (11/11). GitHub Actions
  workflow `.github/workflows/pages.yml` bakes + deploys on push to main;
  `actions/configure-pages` enables the Pages source automatically.
- **P2 — pending**: monolith split, viewer consolidation, asset diet, server
  hygiene.

### Adding a city today (the friction test)

Drop ONE file: `content/places/<slug>.md` with frontmatter
(name/kind/biome/x_pct/y_pct/race/faction/region/image/blurb) + a gazetteer
body. It appears in `/api/places`, as a gold diamond on the bestiary map, in
the canon viewer's dossier layer, and — after the next push — on the public
Pages mirror. Zero code edits.

### Known caveats

- The LIVE server (port 8790) still runs pre-P1 code; it needs one manual
  restart (my session cannot kill processes). Test instances on 8791/8792/8793
  are zombies until killed or reboot.
- Pages mirror is read-only; `/api/map/upload` stays local-Flask exclusive.

## Today's drop-in matrix (friction = how easy it is to break something)

| Content type | How it's added today | Friction |
|---|---|---|
| Chapter in existing arc | drop `content/story/chapters/chapter-arcX-YY.md` | none (auto-discovered) |
| Chapter cover art | drop `static/images/chapter-arcX-YY-vN.png` (highest v wins) | none |
| Creature | drop `content/creatures/<biome>/<slug>.md` → bestiary + APIs | medium — map dot needs a SECOND manual edit in `static/data/map-coordinates.json` |
| World section | drop `content/world/<key>.md` | medium — key must exist in hardcoded `section_order` in server.py |
| Umbrella rewrite / new arc | edit `chapter-0X.md`, run `regenerate_chapters.py` | HIGH — script has wrong hardcoded path (`C:\Users\magic\.copaw\...`), hardcoded ARCS dict, and DELETES all split chapters first |
| City / settlement / landmark | edit JS object literals inside up to 3 HTML files (`static/ethra_map_standalone.html` live, `static/ethra_map_dev.html` copy, dead `templates/ethra_map.html`) | HIGH — 3 places, 2 coordinate spaces |
| Arc title | `ARC_TITLES` dict in server.py + regenerate dict | HIGH — code edit |

## Phase 0 — Safety nets (do first; everything else is safer with these)

1. **git init** in `ethra_site/` + baseline commit of code + content + ledger.
   Commit per finished round. `.gitignore` the heavy superseded art (or archive
   it, see P2). *Needs Ainz-sama's go-ahead.*
2. **Smoke suite** `ethra_site/tools/smoke.py`: hits `/`, `/api/health`,
   `/api/chapters`, every `/api/chapter/<id>`, `/api/bestiary`, `/api/world*`,
   `/api/biomes`, `/api/map/coordinates`, `/map/`; asserts 200 + key markers;
   plus the Playwright shelf probes (moved from workspace root into
   `ethra_site/tools/`). Run after every edit.
3. **regenerate_chapters.py repair**: BASE = script-relative; read arc meta
   from a manifest (P1-3); NON-destructive (write to temp dir, verify counts,
   then swap; keep `.bak` of previous split).

## Phase 1 — Drop-in everything (the "cities like creatures" request)

1. **Places**: `content/places/<slug>.md` with frontmatter
   (`name, kind: city|ruin|landmark, biome, x_pct, y_pct, race, faction, blurb`).
   Server gains `/api/places` + `/api/place/<slug>`; `/api/map/coordinates`
   merges `city_pins` from this dir; world geography/culture sections and the
   map dossier layer render from it. One file per city, zero code edits.
   Migrate the 6 canonical cities (Styxian, Verdantis, Vey'sul, RiverSong,
   Xhilva, Ice City) + wengari-settlements dossier as the first drop-ins.
2. **Creature coords into the creature file**: frontmatter `x_pct/y_pct`
   in each `content/creatures/*/*.md`; server builds the creatures array;
   `map-coordinates.json` demoted to override-only. Creature = ONE file.
3. **Arc manifest**: `content/story/arcs.json` (title, sub_titles,
   split_anchors, source). server.py `ARC_TITLES` and regenerate script both
   read it. New arc = one manifest entry + one umbrella file.
4. **World sections auto-discovery**: `section_order` becomes "known labels +
   any extra *.md found on disk", so a new lore file appears without code edits.

## Phase 2 — Structure & hygiene (reduces break-radius of every future edit)

1. **Split the monolith**: `templates/index.html` (2990 lines) →
   `static/css/ethra.css` + `static/js/ethra.js`, loaded with `?v=` busting.
   HTML edits can no longer break JS/CSS and vice versa; CSS/JS become cacheable.
2. **Consolidate map viewers**: canonical = `static/ethra_map_standalone.html`
   (served at /map/). Archive dead `templates/ethra_map.html`,
   `static/Ethra_viewer.html`, `static/ethra_map_dev.html`,
   `static/maps/*_preview*.html` into `static/_archive/` (ledger row).
3. **Asset diet**: move superseded map PNGs / duplicate bases (the v1–v190
   lineage, ~300 MB) to `static/_archive/`; served tree stays lean.
4. **Server hygiene**: `app.run()` under `if __name__ == "__main__"` guard;
   delete the dead `flat = [...]` comprehension in `get_arcs_and_chapters`;
   single-instance management (`tools/run_server.py` with PID file; kill the
   current duplicate PIDs).

## Ordering rule

P0 → P1 → P2. Each item lands as its own round: implement + live-verify
(smoke suite) + ledger/daily-note, per the standing workflow.
