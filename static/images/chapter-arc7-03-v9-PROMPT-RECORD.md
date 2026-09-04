# chapter-arc7-03 v9 Prompt Metadata

## Source
- Base: chapter-arc7-03-v8.png (forge qwen_image_gen_0_1788550597320.png)
- v9 = PIXEL EDIT of v8, NOT a regeneration (Ainz: "can you edit the image
  and not regenerate it, without too much effort?")
- Edit: the hidden king's bare crown dome (read as a bald head) at
  (915,1030)-(1100,1130) dissolved into the dark coil hatch: mirrored texture
  patch copied from the hatched coil at (730,1030)-(915,1130), gaussian-
  feathered mask (8px). King now fully hidden: fur-mantle scrap + golden
  tail-tip only.
- Bytes: 6,763,680
- Canonical: ethra_site/static/images/chapter-arc7-03-v9.png (+ .webp)

## Composition (inherited from v8, Ainz-approved direction)
Gigant twenty-meter sand wurm coiled in a tall tight spiral, coils
CONSTRICTING the hidden king; eardless armored dome head with closed pincer
mandibles towering above; ice cavern; sepia ink + palest cold tint + faint
gold glow.

## Winning forge prompt (v8, verbatim — v9 inherits)
POSITIVE:
Monochrome ink drawing on aged sepia parchment, Takehiko Inoue Vagabond aesthetic, sepia and pure black ink hatching only, faint pale-gold glow on the wurm chitin and palest cold tint on the dark ice cavern background. A GIGANTIC twenty-meter segmented sand wurm, body three meters thick, hundreds of short legs, coiled in a tall tight spiral inside a dark ice cavern. Its head is a smooth armored dome of overlapping chitin plates like a beetle carapace, COMPLETELY EARLESS with no ears at all, no facial features except two glowing eyes, mouth line fused SHUT with NO teeth, bearing two huge curved pincer mandibles closed like pincers; the head towers at the top of the coil, lowered, menacing. The coils CONSTRICT tight around a hidden occupant: NO part of the king's head or body is visible; only a torn scrap of tattered white fur mantle and the tip of a golden feline tail peek out between two squeezing coils, the coils pressing together with visible squeeze as if crushing a person held within. Dark ice cavern walls behind. Pure black ink hatching over sepia parchment, no painted fabric color.

NEGATIVE:
ears on wurm, cat ears, pointed ears, animal ears, teeth, fangs, open mouth, roaring, pink nose, whiskers, visible king head, visible face, visible ears of king, standing figure, anthropomorphic figure, human face, human skin, feline face on wurm, lion face on wurm, full color, color comic, watercolor wash, bright blue, cyan, green color, apache, cherokee, plains indian, war bonnet, feathered headdress, horse, native american, totem, dreamcatcher, sphere burst, glowing orb, low quality, grunge, spider, kitten, domestic cat, color photograph

## Self-audit (view_image on region crop + full WebP)
- Bald dome gone; region reads as dark coil hatch; faint fur-glow highlight
  at mantle top tolerated at cover scale.
- Rest of image identical to v8; band crop (0.35,0.05,0.80,0.45) outside the
  patch → title-arc7-ch03.webp byte-identical (sha 647c1fdf5e8f before/after
  rollout re-cut) → no cache bust needed; css stays v41.
- PASS → shipped 🟡 pending Ainz lock.

## Audit contract
- view_image self-audit on WebP derivative; Ainz-sama audits ex post; his
  verdict is final.
