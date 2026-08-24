# chapter-arc6-01 v1 Prompt Metadata

## Source
- Path: C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\media\qwen_image\qwen_image_gen_0_1787529154636.png
- Canonical: ethra_site/static/images/chapter-arc6-01-v1.png
- SHA-256: 7D457C0EF97329610A3DA7C3C2FCC84A4C7ED9B5F6C90BA1C0DC686357A1A38B
- Bytes: 4081214
- Model: qwen-image-2.0, 1536x1536, prompt_extend=True
- Forged: 2026-08-23

## Intended composition
Chapter "The Cost" — Ajani sits on the edge of a stone bed in the throne room
converted to a hospital ward, three-quarter from-behind, head bowed with
exhaustion, tangled golden mane, dented Lightbringer armor, crown of white
Styx feathers glowing faintly, two small sleeping creatures (Black Fire, Red
Fire) curled on his lap. Morning golden light through tall arched windows at
left, dust motes, shattered wall edge beyond. One silver-furred female guard
silhouette (Yvaria) at 50% strength, far left. Somber aftermath mood.
Sepia parchment + pure black ink, Vagabond aesthetic.

## Drift-bans applied
- universal negative set (Apache/Plains-Indian, watercolor, painted skin,
  cyan/bright blue, sphere-burst, frontal face, modern clothing, extra limbs)
- bare-chested / exposed torso added as armor-drift insurance

## Known waives (deliberate choices to NOT include)
- twin-suns standing arrangement: indoor scene, morning window light only
- Ember block: mount not featured in this scene
- clothing-only regalia delta: character is armored; only nude-ban terms kept

## Self-audit findings (view_image on the WebP derivative, 2026-08-24)
- MATCHED: sepia parchment + black ink Vagabond style; Ajani feline king
  on bed's edge, bowed head, golden mane, ornate armor, white feather
  crown; arched window with shattered wall beyond; morning light shaft;
  somber aftermath mood.
- DRIFT 1: "two small curled sleeping creatures" collapsed to ONE
  kitten. Canon: Black Fire + Red Fire, two small scorpions.
- DRIFT 2: "silver-furred woman" rendered as a HUMAN woman with silver
  hair. Canon: Yvaria, anthropomorphic silver-furred Wengari.
- Drift terms fed to v2: positive species-explicit (two scorpions;
  anthro feline woman with ears/tail/silver fur); negative adds
  `kitten, cat cub, sleeping cat, domestic cat, human woman, human
  face, human skin`.

## Audit contract
- view_image self-audit restored 2026-08-24; audited the WebP derivative
  (master PNG exceeds the 2 MB vision-transport limit).
- Ainz-sama audits ex post and his verdict is final.
