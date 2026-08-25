# lament-v2 Prompt Metadata (bestiary species portrait rework)

## Source
- Path: C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\media\qwen_image\qwen_image_gen_0_1787622160142.png
- SHA-256: 814777AB5BD99A2F549922BD1F9212AE967152BC99DCFACDC11EC4FB4BCE7D7C
- Bytes: 1,720,909 (png) / 176,476 (webp q88) / 242,927 (jpg q88)
- Supersedes: lament.png (v1 — multi-eyed clawed horror-demon drift)

## Why v2 exists (Ainz directive, 2026-08-24)
Ainz-sama: "yes, lets rework the bestiary portrait to make it more fungal" — following the
arc6-03 ruling that L'vat / the Lament is a FUNGAL entity (avatar of the Mycelial Deep), never
insectoid. The v1 portrait read as a muscular multi-eyed horror demon with claws — the opposite
of "ancient and patient, radiating the quiet, inexorable presence of the Deep."

## Intended composition
Bestiary field-sketch plate in the established register: monochrome black ink on sepia parchment,
fine hatching, aged naturalist's codex. Full-body standing Lament: tall slender fungal entity,
broad dark mushroom cap crowning the head like a cowl, layered dark lustrous shelf-fungi plates
mantling the shoulders, body woven of pale mycelial strands like a living robe, face a smooth
featureless pale fungal mask with two small faint softly-glowing eyes, blunt rounded hands and
feet (NO claws/talons), mycelial threads trailing into the ground, small mushrooms at the feet,
faint spore-dust, marsh grass, serene and patient.

## Iteration history
- attempt 1 (qwen_image_gen_0_1787622101560.png): fungal read correct but drift — dark talon
  tips on hands/feet and a feline-leaning face. Not installed; drift terms fed to attempt 2.
- attempt 2 = THIS FILE: talons and feline face eliminated; audit PASS.

## Drift-bans applied
- insectoid ban set (beetle, antennae, compound eyes, carapace, mandibles…) per species doctrine
- horror ban set (many eyes, demon, fangs, claws, talons, muscular, menacing)
- feline/human face bans (cat face, cat nose, whiskers, human face)
- color/watercolor bans to hold the sepia-ink plate register
- text/caption/watermark bans

## Known waives
- Faint warm brown tint on the cap and gold spore-glow accepted as harmonious with the sepia
  parchment (register holds; not a full-color painterly plate).

## Self-audit findings (view_image on the WebP derivative)
- PASS. Fungal cowl + shelf-fungi shoulders + mycelial robe + mushrooms at feet; featureless
  mask face with two glowing eyes; blunt clawless hands/feet; patient posture; sepia-ink register.

## Rewiring performed (same work block)
- content/creatures/flickermarch/lament.md frontmatter + picture → lament-v2
- content/creatures/flickermarch/threx.md frontmatter + picture → lament-v2
- content/bestiary.md Lament Threx picture → lament-v2
- static/data/map-coordinates.json: threx race + lament creature → lament-v2.png; latent bug
  fixed: underground chithak constituent was borrowing lament.png → now /static/images/chithak.png
- lament.png retained on disk as historical v1 (unreferenced after rewiring).

## Audit contract
- view_image self-audit on WebP derivative; Ainz-sama audits ex post and his verdict is final.
