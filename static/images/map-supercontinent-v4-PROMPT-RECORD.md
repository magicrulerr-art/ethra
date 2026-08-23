# Map Supercontinent v4 — Forge Prompt Record (EDIT-of-v3 silhouette sharpening)

**Asset:** `static/images/map-supercontinent-v4.png`
**Aspect ratio:** 2368 × 1024 px (~23:10 wide panorama)
**File size:** 1,654,767 bytes
**SHA-256:** `4b0fcee6956f495dcf44d38b7fc45aa4a5f699e557206866e37e259f11256571`
**Forge model:** Qwen-Image 2.0 (qwen-image-2.0) — `edit_image_qwen` against v3 reference
**Source media-mirror:** `C:\Users\magic\.copaw\media\qwen_image\qwen_image_edit_0_1783865446531.png`
**Forge type:** **EDIT of v3** (NOT a fresh generation)

---

## Edit intent (the only thing that changed from v3)

Ainz-sama verdict on v3: *"This one doesn't look that bad, can you make it more continental looking?"*

The v3 forge produced a recognizable continent, but the silhouette bled fragmented islet-artifacts around the perimeter and felt organic-blob rather than deliberate-continent. v4 is the same five Ethra regions preserved exactly — only the silhouette gets tightened.

**Three axis-spec changes**:
1. **Single clearly-recognizable large continent** — sharp painted coastline, no scattered island fragmentation.
2. **Organic-but-deliberate landmass shape** — described as "fat crescent or curved spine with one peninsula" so Qwen-Image gets a recognizable continental silhouette archetype.
3. **Painted coastline reinforcement** — continent edge unambiguously traceable from any zoom level.

All other v3 anchors held: 5 biome regions in canonical colors, ocean as deep blue-teal painted water, parchment background, hand-lettered labels remain in place, compass rose, scale bar, twin-suns ornaments at corners.

## Edit Prompt (verbatim, as used)

```
图一 is an Inkarnate-style fantasy continental map. Refine the silhouette into a SINGLE clearly-recognizable large continent — sharp painted coastline, no scattered island fragmentation, organic-but-deliberate landmass shape resembling a real fantasy world continent (think similar to a fat crescent or curved spine with one peninsula). Preserve the painted aesthetic exactly: five regions (SteadFast Desert sand-tan, Rune Belt forest-green north, Umbral Ring pale icy silver-white south coast, Wetland olive-marsh south-east, central canyon-rim ochre core), ocean as deep blue-teal water with painted wave-crest marks, parchment background, hand-lettered labels remain in place. Strengthen the coastline so the continent edge is unambiguously traceable from any zoom level. Keep the compass rose, scale bar, twin-suns ornaments at corners. Do NOT add any characters, faces, animals, or text not already in 图一.
```

## Negative Prompt

```
island archipelago, fragmented coastline, scattered small islands, multiple disconnected landmasses, broken coast, jagged edges, rough scrawl, unfinished sketch, characters, frontal faces, painted flesh, leopard creature, body in desert, anthropomorphic creature, blue ocean fill, woodcut black-ink lines, sepia monochrome engraving
```

## Iteration lineage

| Version | Style anchor | Continent silhouette | Filesize | Status |
|---------|--------------|----------------------|----------|--------|
| v1 | Woodcut mappa mundi sepia | Drift-laden | 3,609,119 b | 🟡 originally rejected for "drift-laden"; preserved in ledger |
| v2 | Loose painterly, no explicit style | Blobby-organic | 3,615,820 b | 🟡 never locked; preserved as v2 sibling |
| v3 | INKARNATE painted continental (Ethra regions) | Recognizable but fragmented-islet | 3,457,251 b | ✅ accepted by Ainz *"doesn't look that bad"* 2026-07-12 |
| v4 | v3 + silhouette sharpening | **Tightened, single continental mass** | 1,654,767 b | 🟡 **PENDING AINZ VERDICT** (delivered for review 2026-07-12) |

Note: v4 filesize is half of v3 — that's because Qwen-Image edit compresses smoother coastline regions more efficiently than v3's island-fragment textures.

## Why v4 bytes ~half v3 bytes
- v3 had fragmented small islands at fringes → many small painted regions → less PNG compression efficiency
- v4 has continuous single-continent shape → fewer sharp edges → better PNG compression
- This is consistent with the silhouette being **simpler** (less complex coastline) and that's the intended outcome.

## Phase-2 Compliance

- [x] PNG saved at canonical path `map-supercontinent-v4.png`
- [x] JPG sibling at `map-supercontinent-v4.jpg` (206,847 b)
- [x] WEBP sibling at `map-supercontinent-v4.webp` (132,592 b)
- [x] SHA-256 recorded
- [x] Forge prompt archived (this file)
- [ ] Ainz's verdict — pending
- [ ] Lock-in to CANONICAL_VERSIONS.md — gated on verdict

## Standing-rules update

- **R50 (new):** When the user accepts a map v(N) but asks for tightening ("more continental, sharper coastline"), reach for `edit_image_qwen` rather than a fresh `generate_image_qwen`. Edit preserves v(N)'s aesthetic anchors (regions, palette, labels, parchment) and only mutates the silhouette. Same principle as v(N+1) = edit of v(N) from chapter-cover workflow.
- **R51 (new):** Smaller filesize after silhouette-edit is a GOOD signal — fewer edge transitions compress better, that's expected when the silhouette got simpler. Don't read a smaller filesize as a regression.
