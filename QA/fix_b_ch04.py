# -*- coding: utf-8 -*-
"""Script B: chapter-04.md — arc4-01/arc4-03 dedup + gesture variation."""
import pathlib

P = pathlib.Path('ethra_site/content/story/chapter-04.md')
t = P.read_text(encoding='utf-8')
orig = t

def para_bounds(text, idx):
    """Expand idx to paragraph boundaries (blank-line separated)."""
    s = text.rfind('\n\n', 0, idx)
    s = 0 if s < 0 else s + 2
    e = text.find('\n\n', idx)
    e = len(text) if e < 0 else e
    return s, e

# ═══ 1. silence-of-shock second instance ═══
ANCH = "The silence that followed was not the silence of shock"
assert t.count(ANCH) == 2, f"silence-of-shock: expected 2, got {t.count(ANCH)}"
i1 = t.find(ANCH)
i2 = t.find(ANCH, i1 + 1)
print("silence#2 context:", t[i2:i2+220].replace('\n', ' ')[:220])
t = t[:i2] + "What followed was not the silence of shock" + t[i2+len(ANCH):]
assert t.count(ANCH) == 1

# ═══ 2. roots pulsed x3 ═══
ANCH = "The roots pulsed faster, brighter"
assert t.count(ANCH) == 3, f"roots: expected 3, got {t.count(ANCH)}"
i1 = t.find(ANCH)
i2 = t.find(ANCH, i1 + 1)
i3 = t.find(ANCH, i2 + 1)
t = t[:i3] + "The roots pulsed, faster and brighter" + t[i3+len(ANCH):]
i2 = t.find(ANCH, i1 + 1)
t = t[:i2] + "The roots pulsed brighter, faster" + t[i2+len(ANCH):]
assert t.count(ANCH) == 1

# ═══ 3. Golden Sun cluster ═══
# 3a. cut occ2 (early surge-of-belief take); keep the smile sentence for graft
OCC2 = "Below the plaza, in the ancient darkness, the lord of the desert felt the surge of belief ripple through the stone and settled back into its patient, hungry waiting."
assert t.count(OCC2) == 1
s, e = para_bounds(t, t.find(OCC2))
occ2_block = t[s:e]
assert "the faintest, most private of smiles" in occ2_block and occ2_block.rstrip().endswith("And the pilgrims would come.")
print("\n--- cutting occ2 block ---\n", occ2_block)
t = t[:s] + t[e:]

# 3b. cut staging-occ2 + eldersA block (abandoned take), keep occ3
STAGE = "Sylva stood motionless at Ajani's side, her silver-chased ceremonial armor gleaming in the noon light."
assert t.count(STAGE) == 2, f"staging: expected 2, got {t.count(STAGE)}"
s_st, e_st = para_bounds(t, t.find(STAGE, t.find(STAGE) + 1))
stage_block = t[s_st:e_st]
print("\n--- cutting staging block ---\n", stage_block)
ELDA = "The elders would hear of this. They would have questions. They would have objections. But by the time those objections reached the capital"
assert t.count(ELDA) == 1
s_a, e_a = para_bounds(t, t.find(ELDA))
elda_block = t[s_a:e_a]
print("\n--- cutting eldersA block ---\n", elda_block)
assert e_st <= s_a, "staging/eldersA blocks not adjacent as expected"
# cut both in one slice (from staging start to eldersA end)
t = t[:s_st] + t[e_a:]

# 3c. graft smile sentence after occ3's feast paragraph
GRAFT_ANCH = "began to plan which pilgrim it would choose first."
assert t.count(GRAFT_ANCH) == 1
gs, ge = para_bounds(t, t.find(GRAFT_ANCH))
smile = ("And the White Dawn, standing on his stone platform with the green fire "
         "flickering gently along his claws, allowed himself the faintest, most "
         "private of smiles. The old thing had come through. The Golden Sun was real now.")
t = t[:ge] + "\n\n" + smile + t[ge:]

# ═══ 4. Kareth gesture variation ═══
# 13 total gesture occurrences; 3 have comma-continuations (#4, #10 already varied
# forms, #1 is narrative prose). Vary 5 of the 10 period-form speech-openers.
KAR_ANY = "Kareth inclined his scarred head"
KAR_PER = "Kareth inclined his scarred head."
assert t.count(KAR_ANY) == 13, f"Kareth total: expected 13, got {t.count(KAR_ANY)}"
assert t.count(KAR_PER) == 10, f"Kareth period-form: expected 10, got {t.count(KAR_PER)}"
variants = {
    2: "Kareth dipped his scarred head.",
    6: "Kareth gave a slow, measured nod.",
    7: "The old Shadow Paw inclined his head.",
    8: "Kareth's scarred head dipped.",
    11: "Kareth nodded once, his scarred head dipping.",
}
pos = -1
positions = []
while True:
    pos = t.find(KAR_ANY, pos + 1)
    if pos < 0:
        break
    positions.append(pos)
for n in sorted(variants, reverse=True):
    p = positions[n - 1]
    assert t[p:p + len(KAR_PER)] == KAR_PER, f"occ {n} not period-form"
    t = t[:p] + variants[n] + t[p + len(KAR_PER):]
assert t.count(KAR_PER) == 5

# ═══ 5. Sylva flickered-gently census (no edit yet) ═══
print("\n=== flickered gently census (chapter-04) ===")
i = -1
n = 0
while True:
    i = t.find("flickered gently", i + 1)
    if i < 0:
        break
    n += 1
    print(f"--- occ {n} @ {i} ---")
    print(t[max(0, i-160):i+120].replace('\n', ' ')[:300])
    print()

P.write_text(t, encoding='utf-8')
print("Script B DONE:", len(orig), "->", len(t), "chars")
