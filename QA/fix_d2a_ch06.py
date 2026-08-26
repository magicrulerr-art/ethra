# -*- coding: utf-8 -*-
"""Script D2a: chapter-06.md — arc6-04 dinner reconstruction.
Keep Take A's character beats + Take B's interactive report/Five Tyrants;
merge decisions; drop duplicated head/question/report/decision pieces."""
import sys
sys.path.insert(0, 'ethra_site/QA')
from _fix_helpers import load, save, div_bounds

t = load()
L0 = len(t)

# ── anchors ──
REPORT_OPEN = "Cefiro set down his cup of Frostfire."
assert t.count(REPORT_OPEN) == 2, t.count(REPORT_OPEN)
REPORT_A_END = "The military is stronger than it was before the war."
assert t.count(REPORT_A_END) == 1
EMOTION_END = "And we knew nothing of any of it."
assert t.count(EMOTION_END) == 1
DECISION_B = ("He rose from his chair, his massive form casting a long shadow across the "
              "frozen table. <span class=\"speech\">\"We will go south. I will bring my family. "
              "I will bring gifts. I will bring questions. And I will spar with this White Dawn. "
              "We will see if he is as strong as my son claims.\"</span>")
assert t.count(DECISION_B) == 1
THUNDER = "volunteer who held the wall while he was unconscious."
assert t.count(THUNDER) == 1

# ── 1. extract Report B interactive portion (report open .. thunderstorm div end) ──
i_r2 = t.find(REPORT_OPEN, t.find(REPORT_OPEN) + 1)
rb_s, _ = div_bounds(t, i_r2)
i_th = t.find(THUNDER, i_r2)
_, rb_e = div_bounds(t, i_th)
REPORT_B = t[rb_s:rb_e]
assert "What is an Amuk?" in REPORT_B and "Five Tyrants" in REPORT_B
print("Report B interactive portion:", len(REPORT_B), "chars")

# ── 2. extract emotional-speech div (immediately after Report B portion) ──
em_s, em_e = div_bounds(t, t.find(EMOTION_END))
assert em_s >= rb_e - 20  # adjacent
EMOTION_DIV = t[em_s:em_e]
assert DECISION_B in EMOTION_DIV
print("Emotional div:", len(EMOTION_DIV), "chars")

# ── 3. cut both extracted pieces from original location ──
t = t[:rb_s] + t[rb_e:]
em_s2 = t.find('<div class="dialogue-block">\nNikolai was silent for a long moment.')
assert em_s2 > 0
em_e2 = t.find('</div>', em_s2) + len('</div>')
assert DECISION_B in t[em_s2:em_e2]
t = t[:em_s2] + t[em_e2:]
print("extracted both pieces from Take B location")

# ── 4. cut Dining B head + question B (second dining description .. 2nd question end) ──
DIN = "The dining hall of the Ice Palace was a vast chamber"
assert t.count(DIN) == 2
i_din2 = t.find(DIN, t.find(DIN) + 1)
db_s = t.rfind('\n\n', 0, i_din2) + 2
QB_END = "Everything a king would need to know about a potential ally."
assert t.count(QB_END) == 2
i_qb2 = t.find(QB_END, t.find(QB_END) + 1)
_, db_e = div_bounds(t, i_qb2)
cut = t[db_s:db_e]
assert "Pearl was on the table beside her plate" in cut
print("--- cutting Dining B head+question:", len(cut), "chars ---")
t = t[:db_s] + t[db_e:]
assert t.count(DIN) == 1 and t.count(QB_END) == 1

# ── 5. cut Report A monologue ──
i_ra = t.find(REPORT_OPEN)
ra_s, _ = div_bounds(t, i_ra)
i_rae = t.find(REPORT_A_END)
_, ra_e = div_bounds(t, i_rae)
print("--- cutting Report A monologue:", ra_e - ra_s, "chars ---")
t = t[:ra_s] + t[ra_e:]
assert t.count(REPORT_OPEN) == 0  # both gone; B re-inserted next

# ── 6. insert Report B after question A div ──
QA_END = "Everything a king would need to know about a potential ally."
i_qa = t.find(QA_END)
_, qa_e = div_bounds(t, i_qa)
t = t[:qa_e] + "\n\n" + REPORT_B + t[qa_e:]
print("Report B inserted after question A")

# ── 7. fix Chapter 4 bridge + replace Chapter-4 decision with nothing (merged decision
#     lives in the emotional div, inserted after the invitation beat) ──
OLD_BR = ("Nikolai listened without interruption. When Cefiro finished, the Tsar was "
          "silent for a long moment.")
NEW_BR = "When Cefiro finished, the Tsar was silent for a long moment."
assert t.count(OLD_BR) == 1
t = t.replace(OLD_BR, NEW_BR)

CH4_DECISION = ("Nikolai nodded slowly. \"Then we will go. I will bring a delegation. "
                "I will bring gifts. I will bring my family. And I will spar with the "
                "White Dawn. We will see if he is as strong as you say.\"")
assert t.count(CH4_DECISION) == 1
i_cd = t.find(CH4_DECISION)
cd_s, cd_e = div_bounds(t, i_cd)
t = t[:cd_s] + t[cd_e:]
print("chapter-4 standalone decision cut")

# ── 8. rewrite decision inside emotional div, insert after invitation beat ──
EMOTION_NEW = EMOTION_DIV.replace(
    "He rose from his chair, his massive form casting a long shadow across the frozen "
    "table. <span class=\"speech\">\"We will go south. I will bring my family. I will bring "
    "gifts. I will bring questions.",
    "He rose from his chair, his massive form casting a long shadow across the frozen "
    "table. <span class=\"speech\">\"Then we will go south. I will bring a delegation. I will "
    "bring my family. I will bring gifts. I will bring questions.")
assert EMOTION_NEW != EMOTION_DIV
INVITE = "There will be a memorial celebration for the fallen. He wants us there."
assert t.count(INVITE) == 1
i_inv = t.find(INVITE)
_, inv_e = div_bounds(t, i_inv)
t = t[:inv_e] + "\n\n\n" + EMOTION_NEW + t[inv_e:]
print("emotional div (merged decision) inserted after invitation beat")

# ── 9. trim lap-beat verbatim overlap ──
LAP_OLD = ("Pearl is the smallest, but she's the bravest. She deflected the assassin's "
           "blade. She's the reason I'm alive.")
LAP_NEW = "Pearl is the smallest, but she's the bravest. She's the reason I'm alive."
assert t.count(LAP_OLD) == 1
t = t.replace(LAP_OLD, LAP_NEW)
print("lap beat trimmed")

save(t)
print(f"D2a DONE: {L0} -> {len(t)} chars")
