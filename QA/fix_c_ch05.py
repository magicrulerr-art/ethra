# -*- coding: utf-8 -*-
"""Script C: chapter-05.md — cut arc5-01 Take B (duplicate arc-opener re-statement)."""
import pathlib

P = pathlib.Path('ethra_site/content/story/chapter-05.md')
t = P.read_text(encoding='utf-8')

ANCH = "It was 5:25 in the morning, the seventh day of the Month of Storms"
assert t.count(ANCH) == 1, f"expected 1, got {t.count(ANCH)}"
i = t.find(ANCH)
s = t.rfind('\n\n', 0, i) + 2
e = t.find('\n\n', i)
block = t[s:e]
print("--- context before ---")
print(t[max(0, s-400):s])
print("--- BLOCK TO CUT ---")
print(block)
print("--- context after ---")
print(t[e:e+300])
assert block.endswith("And the battle was not yet over.")
t = t[:s] + t[e:]
assert t.count(ANCH) == 0
P.write_text(t, encoding='utf-8')
print("\nScript C DONE")
