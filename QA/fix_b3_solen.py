# -*- coding: utf-8 -*-
"""B3 surgery on chapter-03.md: remove Solen confrontation Takes 2+3,
bridge the aftermath to Take 1 (cold version). Ainz-approved recommendation."""
import pathlib

f = pathlib.Path('ethra_site/content/story/chapter-03.md')
t = f.read_text(encoding='utf-8')
before = (t.count('\n') + 1, len(t.split()))

a_start = "Solen's mouth snapped shut. The other Bright Paw elders"
a_fury_end = "The heat of his fury still radiated from him like the breath of the desert."
for a in (a_start, a_fury_end, "There is nothing to forgive",
          "Forgive me. Please. Forgive me.", "the dais was empty save for the king himself"):
    assert t.count(a) == 1, f"anchor count {t.count(a)} for: {a[:50]}"

i0 = t.index(a_start)
i1 = t.index(a_fury_end) + len(a_fury_end)
removed = t[i0:i1]
assert "There is nothing to forgive" in removed and "Forgive me. Please. Forgive me." in removed

bridge = ("In the space of three heartbeats, no one moved. The elders stood with their heads "
          "bowed and their claws retracted, and old Solen pressed one paw slowly to his chest, "
          "over his heart, where the king's claw had rested. No argument came. No protest "
          "followed. The silence was the surrender. The green fire still flickered along "
          "Ajani's claws, casting dancing shadows across the ancient stone\u2014dimmed, but not gone.")

# Replace the whole Take2+Take3+flight+fury span with the bridge, then tidy
# the exact seam whitespace (file uses "\n\n\n" paragraph separators).
head, tail = t[:i0], t[i1:]
head = head.rstrip('\n')
tail = tail.lstrip('\n')
t = head + "\n\n\n\n" + bridge + "\n\n\n\n" + tail

f.write_text(t, encoding='utf-8')
after = (t.count('\n') + 1, len(t.split()))
print(f"OK B3: cut {len(removed.split())} words (Takes 2+3 + flight + fury para); "
      f"bridged to Take 1. Lines {before[0]}->{after[0]}, words {before[1]}->{after[1]}")
