# -*- coding: utf-8 -*-
"""Script D1a: chapter-06.md — arc6-01 + arc6-02 fixes."""
import sys
sys.path.insert(0, 'ethra_site/QA')
from _fix_helpers import load, save, cut_unique

t = load()
L0 = len(t)

# ══ arc6-01: cut misplaced mist-beat #1 + Take A speech ══
MIST = "Cefiro flicked his wrist. A dense, cool mist erupted from the air around Ajani"
assert t.count(MIST) == 2, t.count(MIST)
i1 = t.find(MIST)
# the first mist paragraph + the following dialogue block with Take A's speech
s = t.rfind('\n\n', 0, i1) + 2
e_para = t.find('\n\n', i1)
assert "The Snow Paw prince did not look up from his notebook." in t[s:e_para]
# following div contains Take A speech
div_s = t.find('<div class=', e_para)
div_e = t.find('</div>', div_s) + len('</div>')
block = t[div_s:div_e]
assert "This one does not know the customs of the southern court" in block
print("--- cutting mist#1 + Take A speech ---")
print(t[s:div_e][:400].replace('\n', ' '))
t = t[:s] + t[div_e:]
assert t.count(MIST) == 1
assert t.count("This one does not know the customs of the southern court") == 0

# ══ arc6-01: repair Sylva contamination (dictation memo -> quoted dialogue) ══
OLD = ("but something in her posture shifted as Ajani spoke. The resignation is not "
       "accepted. You fought to be regent. Now bear the weight till it's taken from you. "
       "It's not a prize. It's a burden. No one should want it. I don't want it, which is "
       "why I dumped it on you. She had expected dismissal.")
NEW = ("but something in her posture shifted as Ajani spoke. <span class=\"speech\">"
       "\"The resignation is not accepted. You fought to be regent. Now bear the weight "
       "till it's taken from you. It's not a prize. It's a burden. No one should want it. "
       "I don't want it, which is why I dumped it on you.\"</span> She had expected dismissal.")
assert t.count(OLD) == 1
t = t.replace(OLD, NEW)
print("sylva contamination repaired")

# ══ arc6-01: vary guard-departure Take B opener ══
GUARD = "The guard at the door bowed and departed."
assert t.count(GUARD) == 2, t.count(GUARD)
i1 = t.find(GUARD)
i2 = t.find(GUARD, i1 + 1)
t = t[:i2] + "The guard bowed and withdrew." + t[i2 + len(GUARD):]
print("guard Take B varied")

# ══ arc6-02: rewrite Torek second intro (both scenes legit; vary the 2nd opener) ══
TOREK = ("General Torek, the old Bright Paw commander who had let M'rak ride without "
         "authorization, turned to his former subordinate.")
assert t.count(TOREK) == 2, t.count(TOREK)
i1 = t.find(TOREK)
i2 = t.find(TOREK, i1 + 1)
t = t[:i2] + "Torek turned to his former subordinate once more." + t[i2 + len(TOREK):]
print("torek intro rewritten")

save(t)
print(f"D1a DONE: {L0} -> {len(t)} chars")
