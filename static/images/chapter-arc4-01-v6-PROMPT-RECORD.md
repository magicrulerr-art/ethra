# chapter-arc4-01 v6 Prompt Metadata

## Source
- Path: C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\media\qwen_image\qwen_image_gen_0_1787546741512.png
- SHA-256: verified equal src/dst at copy time (2026-08-24)
- Bytes: 7,357,449
- Model: qwen-image-2.0, 2048*2048

## Intended composition (doctrine reforge of wolf-pup v2)
- Scene anchor (chapter-arc4-01.md "Bureaucracy"): Ajani "settled onto the cold
  stone" throne, green fire steady along his claws; Sylva "at the foot of the
  throne... a silent, silver-furred reminder that the regent was watching."
- Composition: both figures from behind — lion king seated upright, silver jaguar
  regent standing upright beside the throne; EMPTY hall (doctrine: no crowds).

## Species-table check (pre-forge)
- Bright Paws = lion → golden mane. ✔
- Mottled Paws = jaguar → silver fur, rosettes, NO mane. ✔

## Iteration history (all retained on disk)
- v3: figures correct (both bipedal, backs) BUT model drew background elders as
  robed HUMANS with faces → rejected (doctrine: max one frontal face, no crowds).
- v4: hall empty, Ajani frontal perfect, BUT Sylva quadruped → rejected.
- v5: Sylva still quadruped despite upright anchors → rejected.
- v6: combined v3's back-view figure handling with v4/v5's empty hall → PASS.
- Lesson reinforced: the model renders a second feline bipedal reliably only from
  BEHIND; frontal/standing second figures regress to quadruped. Back-view is the
  safe composition for two-feline scenes.

## Self-audit findings (view_image on the 895 KB WebP derivative)
- PASS: two upright bipedal felines, backs to viewer; one tail each; no faces;
  no crowd; empty benches; green claw-flame + gold light shafts only accents.
- Accepted minor drift: Sylva's rosettes tinted pink rather than dark — cosmetic,
  within sepia+accent tolerance.
- Supersedes ✅ LOCKED v2 per Ainz's 2026-08-24 green light on the reforge queue.

## Audit contract
- view_image self-audit on WebP derivative; Ainz-sama audits ex post, verdict final.
