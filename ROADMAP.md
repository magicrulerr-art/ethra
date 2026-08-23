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

- The LIVE server (port 8790) was restarted on current code 2026-08-23
  (PID-specific kill authorized by Ainz-sama; zombies 8791–8793 cleaned in
  the same pass). Live and mirror now run identical code.
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

## Round 24 (2026-08-23) — ribbon dispensed with; P2 executed

Ainz-sama: "the ribbon is again separated from the book — dispense with it and
suggest a better way; work on P2 in parallel."

**R24 design (ribbon replaced, zero runtime geometry):**
- The silk ribbon is GONE. The book keeps its own marker: a red notch drawn
  as `::after` ON the fallen tab — pure CSS, rotates/travels with the tome
  through FLIP and fall, can never separate (commit e6fad3b).
- Chapter nav is now a horizontal **chapter rail** sewn across the folio's top
  edge (sticky, small-caps "Chapters" label, roman numerals, gold underline on
  active, hover title below). Flow layout only — identical on every viewport.
- JS silk machinery deleted; the proven `whenTomeLanded` gate remains solely
  to hold the folio veiled until the tome lies flat.
- probe_r24.py: 23 checks (fresh/switch/mobile + chapter-body-loaded +
  hygiene) — ALL PASS on live and public.

**P2 executed:**
- P2.1 monolith split: index.html 3191 → ~165 lines; extracted to
  `static/css/ethra_core.css`, `static/css/ethra_story.css`,
  `static/js/ethra_core.js`, `static/js/ethra_story.js`, cache-busted `?v=`
  (now 25). tools/split_monolith.py is the one-shot slicer.
- P2.2 viewers: dead `Ethra_viewer.html` + 10 scratch previews archived to
  `static/_archive/` + `static/maps/_archive/`; canon viewer + dev twin kept
  (patch-both protocol still stands).
- P2.3 asset diet (~52 MB archived): superseded -vN covers (arc4-01/04/05 v0,
  arc5-11 v1–v100), map v1/v3/v4 + sidecars, `$null` junk →
  `static/images/_archive/` (gitignored, export-skipped). veylar.md `<picture>`
  repointed to real `shell-singer.*` files. The "56 missing arc5-med" are the
  timeline's intentional 404-probe discovery, documented not "fixed".
  tools/link_check_assets.py now reports 0 referenced-but-missing.
  Report: tools/asset_diet_report.md.
- P2.4 server hygiene: tools/run_server.py — single-instance, PID-file in
  %TEMP% (machine-local, never in-repo), PID-specific kill only after
  command-line verification, health-checked start. `__main__` guard already
  existed; ROADMAP's "dead flat code" note was stale (flat is live).

**Pages chapter regression (user-reported) — root cause + fix (341709e):**
the P2a split externalized the inline JS; the bake rewrites `/api/`→
`/ethra/api/` only inside rendered HTML, so the bare `fetch('/api/chapter/')`
shipped to Pages un-rewritten and 404'd. Fixed at source (fetchChapter now
uses `/ethra/api/chapter/` like every other fetch; PrefixMiddleware strips it
locally) + bake hardening (export_static now rootifies copied static .js/.html
string literals) + cache-bust v25 + probe now asserts `data-loaded` on all
paths. Verified 23/23 on live AND public.

Commits: e6fad3b (R24), d285f90 (P2a+diet), 2f9d575 (Pages fix), 341709e
(run_server hardening).
