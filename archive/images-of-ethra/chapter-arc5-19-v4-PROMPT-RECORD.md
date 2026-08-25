# chapter-arc5-19 v4 — PROMPT RECORD

> This is the **canonical** prompt-sidecar for `chapter-arc5-19-v4.png`.
> Ainz-sama lock-in: 2026-06-28.
> Path: `static/images/chapter-arc5-19-v4.png`
> Mirror: `static/images/arc5-med-arc5-ch19-v4.png` (medallion timeline slot)

## Origin
Ainz-sama pivot: *"ajani looks like a human, and he's supposed to be wearing an amor"* → *"Almost, proportions are wrong his head is too big, edit don't regenerate"* → *"substitute the cloaked figures for a wall and show the creature Infront of ajani not on his back also do a panoramic view isntead of a frontal one to get a sense of scale"* → *"Lock it!"*

## Iteration lineage

| Version | Date | Type | Outcome |
|---|---|---|---|
| v1 | 2026-06-27 | fresh generation | ❌ Ajani face read as human-male (5 o'clock shadow) instead of anthro-feline lion; armor unclear |
| v2 | 2026-06-28 | fresh generation | ✅ anthro-feline head + Lightbringer armor visible + golden wings + spear mid-throw; ❌ head too big relative to torso (proportion off) |
| v3 | 2026-06-28 | `edit_image_qwen` (ref=v2) | ✅ head shrunk to ~1/7 figure height, heroic proportion, torso broader; ❌ creature was behind Ajani, cloaked figures below felt crowded |
| v4 | 2026-06-28 | `edit_image_qwen` (ref=v3) | ✅ LOCKED: **panoramic** `2048×1152`, **wall of feline defenders on left, Ajani mid-throw center, creature looming on right**, no cloaked column, scale contrast 3–4× |

## v4 canonical
- **Path:** `static/images/chapter-arc5-19-v4.png`
- **Source path:** `C:\Users\magic\.copaw\media\qwen_image\qwen_image_edit_0_1782705976135.png` (edit of v3 path)
- **Size:** 2048 × 1152 (panoramic). WebP variant 415,966 B; JPG variant 566,296 B.
- **Reference:** `chapter-arc5-19-v3.png`
- **Tool:** `edit_image_qwen` (Qwen-Image-2.0)
- **Negative prompt:** explicit bans on human-male face / fix-fragment drift / pastel/glamour / watermark
- **Style anchor:** Atlas-Compendium sepia + black-ink engraving preserved across v1→v4

## Composition (v4 LOCKED)
- **Left third**: low pale-sandstone defensive wall, rammed faint feline Wengari defenders' silhouettes leaning over (heads, spears, banner standards)
- **Center**: Ajani Brightmane mid-throw in mid-distance, smaller-in-proportion (approximately half the creature's silhouette), golden wings spread wide, spear drawn back over right shoulder, feline anthro face with full lion-pharaoh mane, Lightbringer ceremonial armor clearly delineated
- **Right third**: the giant black-pillar creature, 3–4× Ajani's size, maw open, purple orb-eyes pulsing
- **Atmospheric**: vast desert plateau stretching across full width, two suns (gold-left / red-right) high in the sky, sepia engraving throughout

## Verification
- Bytes match (canonical PNG byte-identical to media-mirror under `arc5-med-arc5-ch19-v4.png`)
- Served HTML routes ch.19 to v4 (priority `int("4") > int("3") > int("2") > int("1")`)
- Ainz-sama lock-in instruction received: *"Lock it!"*

## Lessons logged
- **"Edit don't regenerate"** workflow is reliable for body-text edit fixes (proportions, composition shift) when v_N+1 already has the right anatomy. Skip the regeneration loop entirely on these passes.
- **Panoramic vs frontal**: When the user asks for *scale sense*, default to wide `2048×1152` (panoramic) in `edit_image_qwen`. The vertical scene `1024×1280` is for hero portraits; the horizontal scene is for battlefields.
- **Composition shift via edit**: Moving creature from behind to in-front, replacing cloaks with wall — these are composition shifts. Edit is the right tool here, not regeneration.

## Ainz-feedback translation table
| Verbatim | Interpretation |
|---|---|
| "ajani looks like a human, and he's supposed to be wearing an amor" | Face must read anthro-feline; armor must be visible pale engraved plate |
| "proportions are wrong his head is too big, edit don't regenerate" | Use `edit_image_qwen`, not fresh generation; shrink head 1/7th |
| "substitute the cloaked figures for a wall" | Replace any ascending column of figures with a defensive rampart |
| "creature Infront of ajani not on his back" | Recompose: creature on right side of frame, Ajani mid-throw toward it (which is on his "front") |
| "panoramic view instead of a frontal one to get a sense of scale" | Wide horizontal at 2048×1152; creature 3–4× Ajani's size |
