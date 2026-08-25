# chapter-arc6-03 v3 Prompt Metadata

## Source
- Path: C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\media\qwen_image\qwen_image_gen_0_1787621411364.png
- SHA-256: 6C4E0B3EF33DCD0DDFF5DD8FD12274508A8155D80FF06E7D11944496B26FAD2A
- Bytes: 4,267,684
- Derivatives: .webp 590,214 b / .jpg 715,406 b (q88)

## Why v3 exists (Ainz corrective, 2026-08-24)
Ainz-sama: "L'Vat isnt an insect right? hes sort of a fungi entity per cannon? why do you keep
painting him as an insectoid?" — v1 and v2 rendered L'vat insectoid because the prompts anchored
to the insect-half vocabulary of the canon text ("chitin dark and gleaming", "multifaceted eyes"),
which forces beetle anatomy out of the model. Bestiary §4 says Threx are FUNGAL-insectoid hybrids
and the Lament is specifically "a rare avatar of the Deep itself" — fungal dominates. Ainz ruling:
L'vat = fungal entity. v3 reframes him accordingly; composition held from v2.

## Intended composition
Extreme-wide Kyre sanctum (held from v2): colossal root-pillars like cathedral columns, vaulted
dark, ENORMOUS blossom suspended in its root-web cupping the amber pool, amber lake below, pale
green root-light (canon: "roots pulsed with pale green light"). Two small figures from behind at
the lake's edge: Ajani (anthropomorphic feline king, layered fur regalia, one paw raised) and
L'vat as a FUNGAL entity — tall slender body woven of pale mycelial strands, layered dark lustrous
fungal plates/shelf-fungi mantling head and shoulders, spore-dust, soft green-gold bioluminescent
glow from within. Sacred scale: tiny figures, colossal organism.

## Drift-bans applied
- NEW insectoid ban set: beetle, insect, insectoid, bug, antennae, compound eyes, multifaceted
  eyes, segmented insect legs, carapace, exoskeleton, mandibles, insect wings, insect abdomen,
  crab, spider, crustacean
- universal negative set (Apache/plains-indian, watercolor, painted skin, cyan, extra limbs,
  frontal humanoid face, sphere-burst, modern clothing)
- clothing ban set for Ajani (nude/bare-chested etc.)
- text/caption/label/watermark ban

## Known waives
- Canon "chitin dark and gleaming" / "multifaceted eyes" descriptors deliberately NOT used in the
  positive prompt — superseded by Ainz's fungal ruling; the gloss is honored via lustrous fungal
  plates instead of beetle chitin.
- Amber pool rendered as a pouring cascade of light into the lake (interpretive, consistent with
  v2's amber lake).

## Self-audit findings (view_image on the WebP derivative)
- PASS first gen. L'vat reads unmistakably fungal: mycelial-weave body, dark glossy fungal caps
  on head/shoulders, green-gold glow, NO antennae/compound eyes/carapace. Sanctum scale holds;
  pale green root-light canon-correct; Ajani feline from behind with fur mantle and raised paw;
  sepia + black ink Vagabond brushwork; no text. Figures slightly larger than v2's but still
  dwarfed — scale contrast intact.

## Audit contract
- view_image self-audit on WebP derivative (master PNG 4.27 MB > 2 MB vision-transport limit).
- Ainz-sama audits ex post and his verdict is final.
