# chapter-arc5-01 v2 Prompt Metadata (EDIT of v1 — NO REGENERATION)

> This is an **edit** iteration, not a fresh generation. v2 was derived
> from v1 via `edit_image_qwen` with v1 as the reference image, per
> Ainz-sama's instruction "edit don't regenerate".
> Per the `view_image` bug class, the v2 edit was **viewed** for audit
> because Ainz-sama granted explicit permission (2026-06-23) to do so.
> The v2 audit was limited to confirming the edit region (added
> scorpions) without redlining other areas.

## Source files
- **v1 canonical**: `static/images/chapter-arc5-01-v1.png` (2,629,368 b,
  sha `29C9D5AE7BAD0883848855D21E66DCCAC6F84C367C6D497A072C4BE24ECC926F`)
- **v1 mirror**: `C:\Users\magic\.copaw\media\qwen_image\qwen_image_gen_0_1782257693281.png`
- **v2 edit source**: `C:\Users\magic\.copaw\media\qwen_image\qwen_image_edit_0_1782258313588.png`
- **v2 canonical**: `static/images/chapter-arc5-01-v2.png`
- **v2 sha-256**: `C7CD90FD0A4C4D35CF2BAE97069C6ED5990E278F4ED1D9863F38C41027180E5D`
- **v2 bytes**: 6,845,766

## Edit delta from v1
- **v1**: ~3 scorpion silhouettes in the lower-right/mid-ground.
- **v2**: 6–8 additional scorpion silhouettes spread across lower-right
  desert (horizon haze, mid-distance charging forms, tumbling
  foreground shadows). Dust and ash wisps behind the vanguard lines.

## Preserved from v1 (audit confirmed)
- Irek — 3/4 from-behind, spear, single-arm grip, no frontal face.
- Elite unit — lower-left cluster unchanged.
- Rune burst — three green-gold impact diamonds lower-right unchanged.
- Twin suns — Steadfast gold-left, Flicker red-right unchanged.
- Sepia + black + green-gold style anchor unchanged.
- No frontal feline face, no second elbow, no painted flesh.

## Tool used
- `edit_image_qwen` (qwen-image-2.0)
- Reference image: v1 canonical path
- Prompt focused on "ADD more scorpions" with explicit preservation
  of all other compositional elements
- Negative prompt: universal drift-bans + extra anti-new-character
  guards (`second Irek`, `second spear`, `Ember mount`, `ajani`)

## Audit notes (visual self-look performed with permission)
- ✅ Added scorpions correctly layered in depth (horizon → mid-ground
  → near-foreground)
- ✅ Silhouette style preserved (pure-black ink, no iridescent shells)
- ✅ Dust/ash trails read as pure-black ink wisps behind the added
  silhouettes
- ⚠️ Slight micro-shift in ink-edge crispness between the preserved
  upper-left (Irek) and the edited lower-right (added scorpions).
  The added forms read ~5% cleaner. Subtle and acceptable.
- ⚠️ Largest scorpion at far right edge may read as slightly oversized
  relative to the original three. Intentional per "much more". Fine
  unless flagged by Ainz-sama.

## Awaiting verdict
This is a v2 **edit**, not a v2 **re-generation**. If Ainz-sama approves
→ lock-in is identical to the v1 lock-in protocol but with `v2` row.
If Ainz-sama rejects the edit → further edits can be layered on top of
v2 (v3 edit), or a full v2 regeneration can be attempted (losing the
editability of the v1 base). A v3-edit may be cheaper than a v2-regen.
