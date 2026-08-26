# -*- coding: utf-8 -*-
"""Script A: chapter-03.md — vary 2 of 3 identical Sylva speech attributions in arc3-05."""
import pathlib, sys

P = pathlib.Path('ethra_site/content/story/chapter-03.md')
t = P.read_text(encoding='utf-8')

PROBE = "she said quietly, her soft voice carrying across the silent platform"
assert t.count(PROBE) == 3, f"expected 3, found {t.count(PROBE)}"

# Occurrence 1: keep. Occurrence 2: vary phrasing. Occurrence 3: attribution-first form.
i1 = t.find(PROBE)
i2 = t.find(PROBE, i1 + 1)
i3 = t.find(PROBE, i2 + 1)

# Show contexts for the record
for n, i in ((1, i1), (2, i2), (3, i3)):
    print(f"--- occ {n} @ {i} ---")
    print(t[max(0, i-200):i+120].replace('\n', ' ')[:340])
    print()

t2 = (t[:i2] +
      "she said, her quiet voice carrying across the silent platform" +
      t[i2+len(PROBE):])
i3b = t2.find(PROBE, i2)  # occ 3 shifted
t3 = (t2[:i3b] +
      "Her soft voice carried across the hush of the platform" +
      t2[i3b+len(PROBE):])

assert t3.count(PROBE) == 1, "post-edit count wrong"
P.write_text(t3, encoding='utf-8')
print("Script A DONE: 3 -> 1 occurrence; two varied.")
