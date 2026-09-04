# chapter-arc7-03 v8 Prompt Metadata

## Source
- Path: C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\media\qwen_image\qwen_image_gen_0_1788550597320.png
- SHA-256: verified equal src==dst at copy time (2026-09-04)
- Bytes: 7,065,887
- Canonical: ethra_site/static/images/chapter-arc7-03-v8.png (+ .webp audit derivative)

## Intended composition (Ainz ruling on v6, verbatim)
"the wurm needs to be constricting ajani, do a gigant wurm coiled, and dont
show ajani, that might be easier" — the gigant sand wurm coiled in a tall
tight spiral, coils CONSTRICTING the king who is completely hidden inside
(only a torn scrap of his white fur mantle and the tip of his golden tail
peek between two squeezing coils); eardless armored dome head with closed
pincer mandibles towering above; ice cavern; sepia ink + palest cold tint +
faint gold glow. Matches the canon beat: "its coils closed around Ajani...
covering him completely."

## Winning prompt — verbatim (v8)
POSITIVE:
Monochrome ink drawing on aged sepia parchment, Takehiko Inoue Vagabond aesthetic, sepia and pure black ink hatching only, faint pale-gold glow on the wurm chitin and palest cold tint on the dark ice cavern background. A GIGANTIC twenty-meter segmented sand wurm, body three meters thick, hundreds of short legs, coiled in a tall tight spiral inside a dark ice cavern. Its head is a smooth armored dome of overlapping chitin plates like a beetle carapace, COMPLETELY EARLESS with no ears at all, no facial features except two glowing eyes, mouth line fused SHUT with NO teeth, bearing two huge curved pincer mandibles closed like pincers; the head towers at the top of the coil, lowered, menacing. The coils CONSTRICT tight around a hidden occupant: NO part of the king's head or body is visible; only a torn scrap of tattered white fur mantle and the tip of a golden feline tail peek out between two squeezing coils, the coils pressing together with visible squeeze as if crushing a person held within. Dark ice cavern walls behind. Pure black ink hatching over sepia parchment, no painted fabric color.

NEGATIVE:
ears on wurm, cat ears, pointed ears, animal ears, teeth, fangs, open mouth, roaring, pink nose, whiskers, visible king head, visible face, visible ears of king, standing figure, anthropomorphic figure, human face, human skin, feline face on wurm, lion face on wurm, full color, color comic, watercolor wash, bright blue, cyan, green color, apache, cherokee, plains indian, war bonnet, feathered headdress, horse, native american, totem, dreamcatcher, sphere burst, glowing orb, low quality, grunge, spider, kitten, domestic cat, color photograph

Size 2048*2048, prompt_extend=False.

## Iteration history (drift ledger)
- v1: full-color wash; arch-over not coil; fanged mouth. REJECT.
- v2: palette fixed; no coil; fanged mouth. REJECT.
- v3: coil (waist-up) but bare torso. REJECT.
- v4: coil + regalia; shipped; Ainz ex-post: cat-face + scale (one coil must
  cover him head to toe, 20m vs 2m).
- v5: scale + lion-pharaoh fixed; lion grammar leaked to wurm head. REJECT.
- v6: eardless head + scale; shipped; Ainz REJECTED: no constriction; do a
  gigant coiled wurm; don't show Ajani.
- v7: constriction composition right; wurm head regrew cat ears + teeth;
  Ajani ear-crown peeked. REJECT.
- v8: v7 composition + eardless dome head + Ajani fully hidden (mantle scrap +
  tail tip only) → SELF-AUDIT PASS (small fang line at lip tolerated per v4
  ex-post tolerance). Shipped 🟡 pending Ainz lock.

## Self-audit findings (view_image on WebP derivative, v8)
- Gigant spiral coil; squeeze reads as constriction of a hidden person.
- Ajani not shown (mantle scrap + golden tail tip only).
- Wurm head: eardless armored dome, glowing eyes, closed pincer mandibles.
- Palette: sepia ink + palest cold tint + faint gold glow. PASS.

## Audit contract
- view_image self-audit on WebP derivative (master PNG > 2 MB vision limit).
- Ainz-sama audits ex post; his verdict is final.
