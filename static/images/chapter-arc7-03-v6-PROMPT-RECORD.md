# chapter-arc7-03 v6 Prompt Metadata

## Source
- Path: C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\media\qwen_image\qwen_image_gen_0_1788550056079.png
- SHA-256: verified equal src==dst at copy time (2026-09-04)
- Bytes: 6,913,230
- Canonical: ethra_site/static/images/chapter-arc7-03-v6.png (+ .webp audit derivative)

## Intended composition (Step-2 brief, as corrected by Ainz)
Chapter 3 "The Ancient one" closing beat with Ainz's scale ruling: the
twenty-meter sand wurm dwarfs the two-meter king; ONE coil of its body, as
thick as the king is tall, encircles him from head to toe; the armored head
(eardless, plated, closed pincer mandibles, no teeth) towers above him,
lowered, menacing. Ajani = lion-pharaoh anthro (wide muzzle grammar), regalia,
profile. Sepia ink + palest cold tint + faint gold glow.

## Winning prompt — verbatim (v6)
POSITIVE:
Monochrome ink drawing on aged sepia parchment, Takehiko Inoue Vagabond aesthetic, sepia and pure black ink hatching only, faint pale-gold glow on the wurm chitin and palest cold tint on the dark ice cavern background. SCALE IS THE SUBJECT: a colossal twenty-meter segmented sand wurm whose body is three meters thick, hundreds of short legs. Its head is an armored insectoid plated head like a beetle-carapace: NO ears, NO cat face, NO pink nose, NO whiskers, mouth SHUT with no teeth visible, bearing two huge curved pincer mandibles closed like pincers. One single vertical loop of the wurm's immense body, the loop's band as thick as the king is tall, encircles the small two-meter king completely from head to toe like a standing ring of chitin, the king dwarfed inside that single coil's embrace; the wurm's armored head towers above him, lowered toward the king, menacing. The king is an anthropomorphic LION-pharaoh humanoid: wide muzzle the breadth of a male lion, broad nose-leather, broad canine arch, round-tipped ears, full golden mane, clad in tattered wengari royal regalia (hewn-fur half-mantle over the left shoulder, tightly-bound cloth sash, bark-cloth arm wraps), standing upright, face in profile. Pure black ink hatching over sepia parchment, no painted fabric color.

NEGATIVE:
cat ears on wurm, feline face on wurm, lion face on wurm, animal ears on wurm, pink nose, whiskers on wurm, teeth, open mouth, fangs, roaring, tabby cat face on king, slim domestic-cat muzzle, pointed cat ears on king, kitten, full color, color comic, watercolor wash, bright blue, cyan, green color, nude, naked, bare-chested, exposed torso, loincloth, frontal humanoid face, human face, human skin, apache, cherokee, plains indian, war bonnet, feathered headdress, horse, native american, totem, dreamcatcher, second elbow, twisted elbow, second paw, second hand, second arm, modern clothing, sphere burst, glowing orb, low quality, grunge, spider, color photograph

Size 2048*2048, prompt_extend=False.

## Iteration history (drift ledger)
- v1: full-color wash; arch-over not coil; fanged mouth. REJECT.
- v2: palette fixed; still no coil; fanged mouth. REJECT.
- v3: coil achieved (waist-up crop) but bare torso. REJECT.
- v4: coil + regalia PASS-then-shipped; Ainz ex-post: "almost — ajani looks
  like a cat; wurm massive, one coil should cover him head to toe (20m vs 2m)".
- v5: scale + lion-pharaoh Ajani fixed; lion grammar LEAKED onto wurm head
  (cat ears, pink nose, roaring fangs). REJECT.
- v6: v5 + strict wurm-head fix (eardless beetle-carapace, closed mandibles,
  no teeth) → SELF-AUDIT PASS. Shipped 🟡 pending Ainz lock.

## Self-audit findings (view_image on WebP derivative, v6)
- Scale reads: loop band ≈ king's height, encircles head-to-toe; head towers.
- Ajani: lion-pharaoh muzzle, mane, regalia; profile; no human drift.
- Wurm head: armored plated, eardless, mandibles closed, no teeth.
- Palette: sepia ink + palest cold tint + faint gold glow. PASS.

## Audit contract
- view_image self-audit on WebP derivative (master PNG > 2 MB vision limit).
- Ainz-sama audits ex post; his verdict is final.
