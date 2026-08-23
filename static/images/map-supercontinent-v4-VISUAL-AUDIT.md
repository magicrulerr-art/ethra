# Map Supercontinent v4 — Visual Audit (2026-07-22)

**Asset under audit:** `static/images/map-supercontinent-v4.png`
**Bytes:** 1,654,767 — **SHA-256:** `4b0fcee6956f495dcf44d38b7fc45aa4a5f699e557206866e37e259f11256571`
**Actual dimensions:** 1568 × 672 px (NOT the 2368×1024 stated in the v4 prompt-record — verify before any dossier re-pinning)
**Forge model:** Qwen-Image 2.0 via `edit_image_qwen` against v3 reference
**Ainz verdict status:** PENDING — last surfaced with "can i see the latest map?" 2026-07-22, after the prior "more stylized, try Inkarnate" pivot

---

## What v4 contains — element-by-element

| Element | Position (viewBox px) | Verified? | Notes |
|---|---|---|---|
| Continent silhouette | Entire landmass within (220,140)-(1380,500) | ✅ | Single crescent mass with one peninsula toward NE |
| Steadfast Desert | Center ~(420, 240) cartouche | ✅ | Sand-tan watercolor fill, single ridge relief at east edge |
| Rune Belt | North band ~(700, 110) cartouche | ✅ | Forest-green band, 4 small tree icons |
| Umbral Ring | South coast ~(580, 400) cartouche | ✅ | Pale silver-white crescent moon glyphs fill the south |
| Flickermarch | East ~(950, 360) cartouche | ✅ | Narrow olive-strip label box |
| Wetland | SE ~(1100, 380) cartouche | ✅ | Olive-marsh cluster |
| Steadfast sun | Top-left corner ~(85, 60) | ✅ | Gold disc + halo |
| Flicker sun | Top-left inner ~(135, 90) | ✅ | Smaller crimson disc |
| Compass rose | Top-right ~(1485, 60) | ✅ | 4-spoke star with cardinal N marker (simple, not ornate) |
| Scale bar | Bottom-right ~(1450, 615) | ✅ | 0–800 km marks |
| Parchment scroll frame | Edges (entire viewBox) | ✅ | Aged-paper roll borders, top + bottom curls |
| Hand-lettered cartouches | On each region label | ✅ | Cinzel-style serif text |

## Five regions — first-pass presence check (R45 checklist)

- [x] 5/5 region labels rendered
- [x] Twin suns visible (Steadfast + Flicker)
- [x] Compass rose complete (N at minimum — full 4-spoke cardinal present)
- [x] Scale bar 0–800 km matches the 800 km cell-distance-unit
- [x] All five biome palette colors present
- [ ] **Marine label** — NOT on the map as a 6th label (intentional: was per `marine` biome that's not in the canonical 5)
- [ ] **Ornamental flourishes** — NOT present (no ribbon banners, no sea-monster motifs, no city pins)
- [ ] **Hand-drawn mountain ranges** — minimal (only the Steadfast ridge at east-center)
- [ ] **Atmospheric coastal fog/mist** — absent (clean painted coastline)

## v3 → v4 deltas (what the edit actually achieved)

Per the v4 prompt-record, `edit_image_qwen` was used against v3 with the intent of:

1. "Single clearly-recognizable large continent" — **ACHIEVED**. v4 eliminated the fragmented small-island halo that v3 had around the perimeter. The landmass reads as one silhouette.
2. "Sharp painted coastline, no scattered island fragmentation" — **ACHIEVED**. Edges are continuous painted curves rather than dot-islet textures.
3. "Organic-but-deliberate landmass shape" — **ACHIEVED**. The crescent arc + small NE peninsula is recognizable as a continental archetype.

**What the edit *lost* or *didn't sharpen*:**
- All hand-lettered labels remained (good).
- Compass rose persisted but is the same simple 4-spoke as v3 (didn't sharpen to ornate Inkarnate style).
- Twin suns remained in same corner positions.
- Filesize ~half v3 (1.65 MB vs 3.46 MB) — **expected** per R51: smoother-contour image compresses better. Not a regression.

## Aesthetic gap — Ainz's "more stylized" request

The Inkarnate-*classic* aesthetic v4 delivers is the parchment-watercolor end of the spectrum. The Inkarnate-*modern fantasy* aesthetic, which Ainz signaled as preferred, includes:

- Hand-drawn mountain ranges drawn as small repeated chevron/V-stroke icons
- Atmospheric fog along coastlines (lighter blue-white band between painted water and continent edge)
- Ornate compass crest — multi-pointed with central fleur-de-lis motif
- Ribbon-banner labels rather than plain boxed cartouches
- Sea-monster or ship motifs in the open ocean zones
- City/settlement pin overlays
- Brushwork visible — directional strokes within biome fills rather than flat washes

v5 forge plan (when Ainz verdict lands):
- v5 = `edit_image_qwen` against v4 reference
- Edit prompt shifts the aesthetic axis from parchment-classic → Inkarnate-modern-fantasy
- Preserve: continent silhouette, 5 regions, parchment base, twin suns, scale bar
- Mutate: add mountain ranges, atmospheric coastal fog, ornate compass, ribbon labels, sea-monster ornaments in ocean

## Files in this lineage (audit trail)

| Version | Path | Bytes | Style anchor | Status |
|---|---|---|---|---|
| v1 | `map-supercontinent-v1.png` | 3,609,119 | Woodcut mappa mundi sepia | 🟡 rejected 2026-06-29 |
| v2 | `map-supercontinent-v2.png` | 3,615,820 | Loose painterly, no explicit style | 🟡 never locked |
| v3 | `map-supercontinent-v3.png` | 3,457,251 | INKARNATE painted continental | ✅ accepted by Ainz 2026-07-12 |
| v4 | `map-supercontinent-v4.png` | 1,654,767 | v3 + silhouette sharpening | 🟡 **PENDING AINZ VERDICT** 2026-07-22 |
| v5 | (planned) | — | v4 + modern-fantasy aesthetic | ⏳ not yet forged |

## Outstanding next-step options (Ainz verdict pending)

- **(a) Lock v4 as canonical** — finalize, update `CANONICAL_VERSIONS.md`, close the lineage; proceed to dossier overlay integration in `Ethra_viewer.html`
- **(b) Iterate to v5** — forge modern Inkarnate-fantasy aesthetic via `edit_image_qwen` against v4 with atmospheric fog, ornate compass, mountain ranges, ribbon labels
- **(c) Use authentic Inkarnate web editor** — requires Ainz credentials or signup authorization; ~30–60 min Playwright canvasing
- **(d) Hybrid** — keep v4 as canonical painted base; layer the modern-fantasy ornaments (compass crest, ribbon banners, mountain icons, sea-monster motifs) as a **separate SVG overlay** on top of v4 in the `Ethra_dossiers/` directory; toggle via `Ethra_viewer.html` layer controls (this delivers R50/R51-style architecture without burning another forge iteration)

## Reusable for rehydration

- R45 checklist: 5 region labels / twin suns / compass with N / scale bar / biome palette present → ALL PASS on v4
- R50: edit-of-prev preserves aesthetic anchors; v4 = edit of v3 confirms this
- R51: smaller filesize after silhouette simplification is a GOOD signal, not regression
- R46: pause-period gap audit — v4 was forged 2026-07-12, last surfaced 2026-07-22 = 10-day gap with no memory file. This audit is the backfill.
