# Map Supercontinent v3 — Forge Prompt Record (INKARNATE-style pivot)

**Asset:** `static/images/map-supercontinent-v3.png`
**Aspect ratio:** 2368 × 1024 px (~23:10 wide panorama)
**File size:** 3,457,251 bytes
**SHA-256:** `6ec0c8a03122b63229ca70479fe353dec535f15cc5b00d0841fb485120aff1d1`
**Forge model:** Qwen-Image 2.0 (qwen-image-2.0)
**Source media-mirror:** `C:\Users\magic\.copaw\media\qwen_image\qwen_image_gen_0_1783833328028.png`

---

## Pivot justification (why v3)

The previous two forges (v1 woodcut mappa mundi, v2 painterly-without-explicit-style) failed to satisfy Ainz-sama's "look like a map" criterion. The 2026-07-11 audit revealed the whole biome-rectangles SVG-painter path was wrong-direction — biome rectangles painted from cells.biome never produce a continent silhouette.

v3 is a **deliberate Inkarnate-style pivot** per Ainz-sama's 2026-07-12 directive ("try incarnate"). The aesthetic is explicitly:
- Painted-illustration (NOT woodcut, NOT sepia engraving)
- Top-down 2D fantasy continental map
- 5 painted biome regions ON a continental silhouette
- Hand-lettered labels with elegant serif typography
- Ocean surrounding the continent
- Compass rose, scale bar, parchment texture

## Final Forge Prompt

```
A wide horizontally-elongated Inkarnate-style fantasy continent map, painted illustration, top-down 2D perspective. Parchment-textured background with subtle aged-cream color and faint foxing stains. A SINGLE continental landmass occupies most of the parchment, surrounded by painted ocean water with subtle wave patterns.

CONTINENT DETAIL — five distinct regions painted with smooth flat watercolor-like color fills (no harsh outlines):
- STEADFAST DESERT: largest central region, warm sand-tan filled with subtle yellow-gold gradient, faint sand-ridge brushmarks
- RUNE BELT: north temperate region, deep forest green with scattered tiny tree icons hand-painted
- UMBRAL RING: south coast, pale icy silver-white with faint crescent-moon glyphs scattered
- WETLAND: south-east, olive-marsh green with reed icons
- (Continental core shows as canyon-rim ochre)

OCEAN: deep blue-teal water with subtle horizon gradient, hand-painted wave-crest brush marks along the continent edges, NOT blank parchment.

LABELS: Eleven hand-lettered serif-font labels in black ink, each with a small rectangular cartouche backing: MAPPA MUNDI ETHRAE, N (compass rose top-right), STEADFAST DESERT (center), RUNE BELT (north), UMBRAL RING (south coast), WETLAND (south-east), FLICKERMARCH (small region marker on the wetland boundary), THE PACT (small marker near central mesa), DRIFTARI (small marker in the rune-belt forest), THE LAMENT (small marker in umbral ring), THE KYRE TREE (landmark marker with small tree silhouette).

COMPASS ROSE: top-right corner, classical 8-point with N at apex, gold-and-cream painted colors.
SCALE BAR: bottom-right, ink rule with km tick marks "0 — 800 km".
PARCHMENT: edges softly curled inward with faint warm-cream shadow suggesting aged paper.
TWIN SUNS: small decorative disc motifs on the parchment margin (gold + crimson) — NOT in the sky.

STYLE: Inkarnate-style painted continental map illustration. Soft painterly brushwork, watercolor-like flat fills, clean hand-lettered labels, traditional fantasy-cartography aesthetic. NOT woodcut, NOT sepia engraving, NOT cyan-blob, NOT generic RPG dungeon map.

HARD BAN: NO characters, NO people, NO animals, NO anthropomorphic creatures, NO frontal faces, NO painted flesh, NO blue-painted ocean, NO woodcut black-ink lines, NO sepia monochrome, NO 3D, NO anime, NO neon, NO Asian temple motifs, NO leopard creatures.
```

## Negative Prompt

```
frontal faces, characters, villagers, portrait, painted flesh, watercolor smears, cyan blob, plastic look, 3D render, anime, gradient mesh, neon, urban, Asian characters, temples, Buddhist symbols, blue painted entire ocean, leopard creature, body in desert, anthropomorphic creature, frontal face, woodcut sepia, engraving crosshatch
```

## Iteration lineage

| Version | Style anchor | Filesize | Status |
|---------|--------------|----------|--------|
| v1 | Atlas-Compendium mappa mundi woodcut sepia | 3,609,119 b | 🟡 Drift-laden per original commit; rejected by Ainz on "compass rose → compass nose" verdict |
| v2 | Painterly without explicit style guide | 3,615,820 b | 🟡 Visually closest to a real continent but never locked as canonical |
| v3 | INKARNATE-style painted continental with explicit Ethra region labels | 3,457,251 b | 🟡 **PENDING AINZ VERDICT** (delivered 2026-07-12) |

## Standing-rules update

- **R47 (new):** "Continental maps require a CONTINENT SILHOUETTE, not biome rectangles." Biome-painted cells never read as continents.
- **R48 (new):** Inkarnate-style = painted continental illustration with hand-lettered labels, NOT woodcut sepia engraving. Don't conflate aesthetics.
- **R49 (new):** When user names a specific tool ("Inkarnate"), that is an AESTHETIC directive for AI to forge, NOT a hand-painting workflow for the user.

## Phase-2 Compliance

- [x] PNG saved at canonical path `map-supercontinent-v3.png`
- [ ] JPG sibling — pending (forge-thumbnail script `gen_thumbs.py` should be run by lock-in)
- [ ] WEBP sibling — pending
- [x] SHA-256 recorded
- [x] Forge prompt archived (this file)
- [ ] Ainz's verdict — pending
- [ ] Lock-in to CANONICAL_VERSIONS.md — gated on verdict
