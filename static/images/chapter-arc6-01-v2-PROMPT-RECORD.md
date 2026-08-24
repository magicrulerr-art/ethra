# chapter-arc6-01 v2 Prompt Metadata

## Source
- Path: C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\media\qwen_image\qwen_image_gen_0_1787530194511.png
- Canonical: ethra_site/static/images/chapter-arc6-01-v2.png
- SHA-256: E2B653D7C5E42562CCBD9D5184C3F2EDEB62703C2521D8C9C0BB23DB69E5AA2B
- Bytes: 4070723
- Model: qwen-image-2.0, 1536x1536, prompt_extend=True
- Forged: 2026-08-24

## Delta from v1
Species-explicit fixes: lap creatures = two scorpions (Black Fire
dark-scaled, Red Fire rust-red); left figure = anthropomorphic
silver-furred Wengari woman; added lion-broad muzzle anchor.

## Self-audit findings (view_image on the WebP derivative)
- FIXED from v1: two scorpions present (dark + rust-red) ✅; left figure
  is feline with ears + tail, not human ✅; Ajani muzzle lion-broad ✅.
- DRIFT 1 (new): bed rendered as modern metal hospital frame; wall
  carries a modern control-panel/outlet plate with hook.
- DRIFT 2 (new): Yvaria rendered as gaunt nude hairless cat-person
  (sphynx-like), unclothed.
- DRIFT 3 (minor): scorpions awake and oversized; tails raised instead
  of curled asleep.
- Drift terms fed to v3: positive "simple wooden bed with stone base,
  no metal frame"; "Yvaria clothed in light leather armor, sword at
  hip"; "scorpions small, asleep, tails coiled"; negative adds
  `metal bed frame, hospital bed, iron bed, wall panel, electrical
  outlet, switch plate, hook panel, modern furniture, nude, hairless
  cat, sphynx cat`.

## Audit contract
- view_image self-audit restored 2026-08-24; audited the WebP derivative.
- NOT shipped (drifted); superseded by v3.
