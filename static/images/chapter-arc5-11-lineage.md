# Arc 5 ch.11 — illustration lineage

## v1 (legacy)
**File:** `chapter-arc5-11-v1.png` (1,967,988 B), `chapter-arc5-11-v1.webp` (213,184 B), `chapter-arc5-11-v1.jpg` (278,000 B)
**Type:** Generated from prompt (Reva + broken gate + slumped defenders).
**Status:** Rolled back after Ainz-sama's "I'm not sure what you're trying to show" feedback — the gate scene was ambiguous; the emblem beat was missed.

## v2 (regenerated)
**File:** `chapter-arc5-11-v2.png` (1,946,422 B), `chapter-arc5-11-v2.webp` (201,748 B), `chapter-arc5-11-v2.jpg` (260,272 B)
**Type:** Generated from a refined prompt (Ajani in a pearlescent cocoon + Cefiro + Kira).
**Status:** Reverted (not locked).
**Ainz feedback after v2:**
- Ajani's face reads as a cat, needs to read as a male lion.
- Kira reads too human, needs to read as a small Wengari girl with feline features.
- Cefiro is acceptable as-is.
- Action: **edit, do not regenerate.**

## v3 (edit of v2)
**File:** `chapter-arc5-11-v3.png`
**Type:** Edited from v2 PNG via `edit_image_qwen` (single-image input).
**Tool call lineage:**
- Source image: `chapter-arc5-11-v2.png`
- Tool: `edit_image_qwen`, model `qwen-image-2.0`
- Reference image: absolute path to v2 PNG
- Edit instructions: refine reclining figure with broader mane and lion-pharaoh silhouette; refine girl-scout with feline ears and small muzzle; keep Cefiro unchanged; preserve pearlescent cocoon; preserve style anchor (sepia + black ink).
- Output saved to: `C:\Users\magic\.copaw\media\qwen_image\qwen_image_edit_0_1782697716998.png` → copied to `static/images/chapter-arc5-11-v3.png`.

**Status:** Awaiting Ainz-sama's review.

## v3 (edit of v2) — REJECTED
**File:** `chapter-arc5-11-v3.png` (2,012,953 B)
**Type:** Edited from v2 PNG via `edit_image_qwen` (single-image input).
**Ainz feedback after v3:** "ajanis eyes look like blue marbles, he has no mane, Kira still looks human but now with a glowing pink nose ... iterate over v1 and not the failed v2"

## v4 (edit of v3) — REJECTED
**File:** `chapter-arc5-11-v4.png` (2,198,111 B)
**Type:** Edited from v3 via `edit_image_qwen`. Built on top of v3's already-broken state — wrong direction. The iteration chain stayed on v2 when v1 was the user's preferred base.

## v5 (edit of v1) — REJECTED
**File:** `chapter-arc5-11-v5.png` (1.9 MB)
**Type:** Edited from v1 PNG via `edit_image_qwen`.
**Ainz feedback after v5:** "The image you sent it's what was originally there." v5 visually resembles v1 to the point of indistinguishability — `edit_image_qwen` was too conservative.
**Lesson logged:** Sidecar note — edit-based iterations on Atlas-Compendium panel images produce sub-perceptual changes. **For visible iteration, fresh-generate with cumulative constraints baked in.**

## v99 (fresh generation) — superseded by v100
**File:** `chapter-arc5-11-v99.png`
**Status:** Pushed all four constraints — chamber + Snow Leopard + Kira + Ajani's full mane — but Ainz-feedback: heal the request by SYNTHESIZING the chamber of v2/v3 with the broader-mane/3-scorpions of v99. Single-fresh-generation approach was not enough; the synthesis brief required a wholly fresh synthesis.

## v100 (synthesis fresh generation) — current canonical
**File:** `chapter-arc5-11-v100.png`, `chapter-arc5-11-v100.webp` (242,708 B), `chapter-arc5-11-v100.jpg` (303,420 B)
**Type:** Fresh generation (NOT an edit) — `generate_image_qwen` invoked with comprehensive synthesis prompt.
**Source prompts anchored to:**
- Royal chamber / intact walls (from v2, v3 grammar)
- Snow Leopard Wengari figure (from v2, v3 grammar — Cefiro-like)
- Kira-like child-scout female Wengari (from v3 grammar)
- Ajani with full mane (from v99 grammar — broader mane)
- Three scorpions: red/black/white (from v99 grammar)
- Sepia + black-ink engraving style (ground)

**Why v100 vs v99:** Ainz feedback after v99 — "...Ajani needs to be in the royal chamber which is not in ruins, one figure needs to be a snow leopard wengari, the other figure needs to be Kira." v99 still had a courtyard ruin scene; the synthesis brief calls for chamber + Snow Leopard + Kira. v100 captures all three.
**Status:** Awaiting Ainz-sama's review.

## Naming convention
- `chapter-arc5-11-v{N}.png` for canonical chapter-end assets (v1–v5 reserved series, v6–v8 reserved for candidate variants, v9N reserved for canonical-override, v100+ reserved for cumulative-synthesis overrides).
- `arc5-med-arc5-ch11-v{N}.png` duplicates for the timeline med-slot — auto-resolved by JS probe which now reads `['v101','v100','v99','v98','v97','v96','v95','v9','v8','v7','v6','v5','v4','v3','v2','v1']` in order. **Always mirror v100+ assets into `arc5-med-*` filenames BEFORE locking, or the timeline hover will show a stale image.**
