# -*- coding: utf-8 -*-
"""Script D1b: chapter-06.md — arc6-03 L'vat arrival stitch."""
import sys
sys.path.insert(0, 'ethra_site/QA')
from _fix_helpers import load, save, para_bounds, div_bounds

t = load()
L0 = len(t)

FOREG = "The Lament's limb touched Ajani's forehead, and a pulse of light passed between them"
assert t.count(FOREG) == 3, t.count(FOREG)
BRIDGE = '"It always is with you. Explain. Now."'
assert t.count(BRIDGE) == 1

# ── 1. extract Take B's "Of course I came" block (contains "To let twenty Quick go") ──
OC_ANCH = "They remember what the Hummans did. Twice."
assert t.count(OC_ANCH) == 1
i_oc = t.find(OC_ANCH)
oc_s, oc_e = div_bounds(t, i_oc)
OC_BLOCK = t[oc_s:oc_e]
assert OC_BLOCK.lstrip().startswith('<div class="dialogue-block">')
assert '"Of course I came."' in OC_BLOCK and "To let twenty Quick go" in OC_BLOCK
print("extracted Of-course-B block:", len(OC_BLOCK), "chars")

# ── 2. cut Take A (forehead occ2 .. A8 defiance div end) ──
i_bridge = t.find(BRIDGE)
i_occ2 = t.find(FOREG, i_bridge)
sA = para_bounds(t, i_occ2)[0]
DEFY = "If you cannot accept that, then you have come here for nothing."
assert t.count(DEFY) == 2, t.count(DEFY)
i_defyA = t.find(DEFY, i_occ2)
eA = t.find('</div>', i_defyA) + len('</div>')
print("--- Take A cut:", eA - sA, "chars ---")
print(t[sA:sA+200].replace('\n', ' '))
print("...")
print(t[eA-200:eA].replace('\n', ' '))
t = t[:sA] + t[eA:]
assert t.count(FOREG) == 2

# ── 3. cut Take B replay opening (forehead occ3 .. Of-course-B div end) ──
i_bridge = t.find(BRIDGE)
i_occ3 = t.find(FOREG, i_bridge)
sB = para_bounds(t, i_occ3)[0]
i_oc = t.find(OC_ANCH)
_, eB = div_bounds(t, i_oc)
print("--- Take B opening cut:", eB - sB, "chars ---")
print(t[sB:sB+200].replace('\n', ' '))
t = t[:sB] + t[eB:]
assert t.count(FOREG) == 1
assert t.count(OC_ANCH) == 0

# ── 4. insert stitch after bridge block ──
i_bridge = t.find(BRIDGE)
bs, be = div_bounds(t, i_bridge)
STITCH = (
    "\n\nAjani explained. The Hummans on the wall. The creature at the gate. The king who "
    "had unleashed the Plague and the soldiers who had paid for his ambition. He told it "
    "plainly, without decoration, and when he finished, the wind moved across the broken "
    "wall and L'vat simply looked at him for a long, unreadable moment."
    "\n\n<div class=\"dialogue-block\">\n<p class=\"speech-line\">Ajani met his teacher's "
    "ancient gaze. \"L'vat. You came.\"</p>\n</div>"
    "\n\n" + OC_BLOCK
)
t = t[:be] + STITCH + t[be:]
assert t.count(OC_ANCH) == 1
print("stitch inserted")

# ── 5. merge tribunal clause into Quick-unease-B staging ──
OLD5 = "taking in the Wengari soldiers, the Pyrinae engineers, the scorpion riders."
NEW5 = ("taking in the Wengari soldiers, the Pyrinae engineers, the scorpion riders who "
        "had been cleared by Seris's tribunal.")
assert t.count(OLD5) == 1, t.count(OLD5)
t = t.replace(OLD5, NEW5)

# ── 6. graft Take A's whisper accusation + wall reaction after unease staging ──
ANCH6 = ("They looked ready to strike. They looked ready to flee. They looked like "
         "creatures caught between an old terror and an unfamiliar command.")
assert t.count(ANCH6) == 1
i6 = t.find(ANCH6)
p6s, p6e = para_bounds(t, i6)
GRAFT = (
    "\n\n<div class=\"dialogue-block\">\n<span class=\"speech\">\"These are the ones,\""
    "</span> one of the Quick whispered, its voice a thin, reedy rasp. <span class=\"speech\">"
    "\"These are the ones who burned us. The First Tyrant's fire. The Fifth Tyrant's Plague. "
    "Twice. Twice the Hummans burned us. We remember. The network remembers. The Deep "
    "remembers. Why are they here? Why are they not dead?\"</span>\n</div>"
    "\n\nThe Hummans on the wall had gone very still. The young boy Ajani had been helping "
    "with the boulder was pale, his dark eyes wide. The scorpion riders had raised their "
    "hands, empty, showing they carried no weapons. The Wengari soldiers had tensed, unsure "
    "whether to intervene. Blackie and Reddy had positioned themselves between the Quick and "
    "the Hummans, their tails raised, their white-lacquered stingers gleaming. They did not "
    "attack. But they were ready."
)
t = t[:p6e] + GRAFT + t[p6e:]
print("whisper graft inserted")

# ── 7-9. cut three raw dictation blocks ──
for raw in ("Then without warning the lament extends a limb",
            "We see a humman mother and daughter",
            "Ajani very flustered says"):
    assert t.count(raw) == 1, (raw, t.count(raw))
    i = t.find(raw)
    s, e = div_bounds(t, i)
    print("--- cutting raw:", t[s:s+90].replace('\n', ' '))
    t = t[:s] + t[e:]

# ── 10. cut gaze Take B (thousand-years variant) ──
GAZE = "L'vat turned his ancient gaze toward the small girl, who was still waving over her mother's shoulder."
assert t.count(GAZE) == 2, t.count(GAZE)
i1 = t.find(GAZE)
i2 = t.find(GAZE, i1 + 1)
t2_s, t2_e = para_bounds(t, i2)
assert "a thousand years" in t[t2_s:t2_e]
print("--- cutting gaze Take B ---")
t = t[:t2_s] + t[t2_e:]
assert t.count(GAZE) == 1

save(t)
print(f"D1b DONE: {L0} -> {len(t)} chars")
