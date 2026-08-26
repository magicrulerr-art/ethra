# -*- coding: utf-8 -*-
"""Script D1c: chapter-06.md — arc6-03 cut duplicated Sultan closer + essay tail + raw scene-direction."""
import sys
sys.path.insert(0, 'ethra_site/QA')
from _fix_helpers import load, save, div_bounds

t = load()
L0 = len(t)

SULT = '<span class="speech">"Then we negotiate,"</span> the Sultan said.'
assert t.count(SULT) == 2, t.count(SULT)
RESUME = "The Sunraptor banked low over the endless sand"
assert t.count(RESUME) == 1

i1 = t.find(SULT)
i2 = t.find(SULT, i1 + 1)
s, _ = div_bounds(t, i2)
e = t.find(RESUME)
cut = t[s:e]
print("--- cut range:", len(cut), "chars ---")
assert "The Council murmured its assent" in cut
assert "The chapter's core achievement" in cut
assert "Let's now follow Cefiro and Kira" in cut
print(cut[:300].replace('\n', ' '))
print("...")
print(cut[-300:].replace('\n', ' '))
t = t[:s] + t[e:]
assert t.count(SULT) == 1
assert t.count("The chapter's core achievement") == 0

save(t)
print(f"D1c DONE: {L0} -> {len(t)} chars")
