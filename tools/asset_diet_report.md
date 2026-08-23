# P2 Asset Diet Report — 2026-08-23

Scope: `static/` assets + references from templates, static html/css/js/json,
content markdown. Tool: `tools/link_check_assets.py` (report in
`tools/linkcheck.json`).

## Referenced-but-missing: 3 → 0

- `static/images/veylar-shell-singer.{png,jpg,webp}` — referenced only by the
  inline `<picture>` in `content/creatures/tidepools/veylar.md`; the real files
  on disk are `shell-singer.*` (the frontmatter `image_full` was already
  correct). **Fixed** by repointing the `<picture>` to `shell-singer.*`.
  Nothing was recoverable from git history — the `veylar-` prefixed names
  never existed.

## The "56 missing arc5-med-*.png" — not broken refs

`static/arc5_timeline.js` discovers its artwork at runtime by probing
`/static/images/arc5-med-arc5-chNN-v{X}.png` (16 versions × 5 chapters = 80
paths; first on-disk hit wins, 404s are the discovery mechanism). The missing
paths are intentional probes, not broken references. Exactly one file per
chapter exists and is served: ch01→v1, ch05→v2, ch11→v101, ch19→v4, ch22→v1.
No action needed; documented so nobody "fixes" the 404s.

## Superseded art archived: 38 files (~52 MB) → `static/images/_archive/`

Keep-set rule: highest `-vN` per chapter cover (server picker), canonical map
v2, active arc5-med probe hit per chapter, docs belonging to kept art.

- `chapter-arc4-01/04/05.{png,jpg,webp}` (v0, superseded by -v2 / -v2 / -v8)
- `chapter-arc5-11-v{1,2,3,4,5,99,100}.{png,jpg,webp}` (superseded by v101)
- `map-supercontinent-v{1,3,4}.png` + their PROMPT-RECORD / VISUAL-AUDIT
  sidecars (canonical is v2, served by `static/js/ethra_story.js`)
- `$null` (0-byte Windows redirect junk)

## Legacy viewers archived: 11 files

- `static/_archive/`: `Ethra_viewer.html` (dead legacy viewer; server refuses
  to serve text/html statics; its only asset ref was the archived map v4),
  `_fitprobe.html`
- `static/maps/_archive/`: `base_preview.html`, `base_preview2.html`,
  `canon_preview2..6.html`, `_canon_preview.html`, `_tmp.html`
- Kept live: `ethra_map_standalone.html` (canonical /map/) + `ethra_map_dev.html`
  (dev twin, patch-both protocol).

## Shipping guards

- `.gitignore`: `_archive/` (any depth) — archives stay local, never pushed.
- `tools/export_static.py`: `_archive` in `IGNORED_STATIC_DIRS` — never baked
  into the Pages mirror.
- `tools/link_check_assets.py`: skips `_archive` dirs (historical refs).
- Git: archived files are recorded as deletions on push; history retains them.

## Kept by design (referenced docs, not assets)

`CANONICAL_VERSIONS.md`, `chapter-arc5-11-lineage.md`,
`chapter-arc5-01-v2-PROMPT-RECORD.md`, `chapter-arc5-19-v4-PROMPT-RECORD.md`,
`three-creatures-v1-PROMPT-RECORD.md` — documentation sidecars mandated by the
cover-forge skill or indexing kept art.

## Final state

`link_check_assets.py`: **0 referenced-but-missing**, 238 referenced &
existing. Smoke 36/36, probe_r24 20/20 on local and public mirror.
