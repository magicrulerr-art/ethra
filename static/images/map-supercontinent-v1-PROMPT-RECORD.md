# Map Supercontinent v1 — Forge Prompt Record

**Asset:** `static/images/map-supercontinent-v1.png`
**Aspect ratio:** 2368 × 1024 px (≈ 23:10 ≈ "wide panorama")
**File size:** 3,609,119 bytes
**SHA-256:** `45639e8ce3b6cb3c1eeec22391415c6181b99f671ee5ffc9e566dafd5fe8576f`
**Siblings:** `map-supercontinent-v1.jpg`, `map-supercontinent-v1.webp` (duplicated fallback copies)
**Forge model:** Qwen-Image 2.0 (qwen-image-2.0)

---

## Final Forge Prompt (iteration 4 of allowed 3)

> Pure black-ink line drawing on plain aged-paper tan color (#c4a882) ONLY.
>
> Drawing is a wide horizontally-rectangular mappa mundi (roughly double-width-to-height, like an unfurled parchment scroll). FRAYED PARCHMENT EDGES with small inward curls that cast no shadow shapes.
>
> The drawing shows a single round continent occupying most of the parchment, surrounded by a thin parchment margin. The continent has six clearly-labelled regions, separated by hand-drawn ink lines. Each region is labelled with a small rectangular cartouche containing the region's name written as if hand-calligraphed:
>
> - THE RUNE BELT (north-center, large temperate forest region with small tree sketch-icons)
> - STEADFAST DESERT (central-south, mostly blank with hatched sand-ridge line streaks and one large tree silhouette on its eastern edge labelled "KYRE")
> - UMBRAL RING (southwest coastal strip, lotus sketch-icons along the coast)
> - FLICKERMARCH (northeast, mushroom sketch-icons and small standing stones)
> - TIDEPOOLS (southeast coast, wave-pattern hatching)
> - UNDERGROUND (southeast corner, a dark cross-section of a cave mouth drawn with dense parallel ink hatching)
>
> Top-left corner parchment margin has a small text "MAPPA MUNDI ETHRAE". Top-right corner margin has a tiny compass rose with an "N" letter at the top. Bottom edge has a thin inked scale-line with tick marks.
>
> STRICT rules:
> - NO characters in the picture at all, no people, no animals, no faces, no frontal portraits
> - Continent land interior is plain parchment tan with only ink-line icons, never painted with any color
> - Ocean surrounding the continent is plain parchment tan (negative space), never painted blue or any colored fill
> - Drawing style is exactly like a 1500s woodcart map: clean black ink lines of varying weight on warm tan paper

## Negative Prompt

> frontal faces, characters, villagers, portrait, full-color painted flesh, watercolor, painterly dunes, pastel, cyan blob, plastic look, 3D render, anime, gradient mesh, neon, urban, Asian characters, temples, Buddhist symbols, generic fantasy, blue ocean fill, painted ocean, leopard creature, body in desert, anthropomorphic creature, frontal face, painted colored regions

---

## Iteration Log

| # | Drift Failure | Strategy Change for Next Iteration |
|---|---|---|
| v1 | Underwater creatures replaced continent. Continent vanished into ocean pattern. | Added stronger "continent is single visible oval" instruction + explicit parchment-tan ocean rule. |
| v2 | Image drifted to Buddha-temple ink style with strong ocean motifs. No biome labels. | Specified "no characters, no Asian symbols, no temples". Required labelled regions. |
| v3 | Cross-hatch blue ocean took ~40% of frame; desert rendered as reclining leopard-body creature. | Tightened "ocean is parchment tan negative space, never painted blue"; banned painted flesh + painted ocean. |
| v4 | Final committed candidate. Capture remained sepia-tonal but identity drift persisted (compass label -> "compass nose", labelled cartouches -> partial fragments). Acceptable for v1. |

**Drift trade-off acknowledged:** Qwen-Image 2.0 with `prompt_extend:false` reduced but did not eliminate drift toward CGI/symbolism and away from Renaissance ink-line. The committed candidate still requires Ainz's judgement whether to (a) accept v1 and proceed, (b) try a fresh forge with a different anchor strategy (e.g. emissive-on-ink overlay guidance), or (c) composite parchment background onto a structurally-cleaner base map.

---

## Phase 2 Compliance

- [x] PNG saved at canonical path
- [x] JPG sibling exists
- [x] WEBP sibling exists
- [x] SHA-256 recorded
- [x] Forge prompt archived
- [x] Iteration history preserved
- [ ] Ainz's verdict received — pending
