# -*- coding: utf-8 -*-
"""Arc II master cleanup on chapter-02.md (B1, B2, B11 + bleed/tag fixes).
B10 reclassified legitimate (sequential petal events, intentional parallel)."""
import pathlib

f = pathlib.Path('ethra_site/content/story/chapter-02.md')
t = f.read_text(encoding='utf-8')
before = (t.count('\n') + 1, len(t.split()))

def rep(old, new, count=1, label=''):
    global t
    n = t.count(old)
    assert n == count, f"[{label}] expected {count}, found {n}: {old[:70]!r}"
    t = t.replace(old, new)

# ---------- B1: Nyasha Take A excised (Take B is answered by Ajani's speech) ----------
takeA_end = ("What did it demand? And what did you give it, Ajani Brightmane, "
             "that your father could not?\"</span>\n</div>")
assert t.count(takeA_end) == 1
i0n = t.index("Nyasha, who had been silent since her last words, spoke again.")
i0 = t.rindex("<div class=\"dialogue-block\">", 0, i0n)
assert i0n - i0 < 60, "div opener too far from Nyasha text"
i1 = t.index(takeA_end) + len(takeA_end)
assert "What do you want" not in t[i0:i1], "would eat Take B"
t = t[:i0].rstrip('\n') + "\n\n\n" + t[i1:].lstrip('\n')
print("B1: Nyasha Take A excised (div boundary clean)")

# NOTE: the 'ok... So good, so far' aside is legitimate Ajani interiority — kept.

# ---------- malformed div tag (missing closing quote on class attr) ----------
rep("<div class=\"dialogue-block>\n", "<div class=\"dialogue-block\">\n", count=4, label='tag')

# ---------- B2/B11: departure two-take — cut Take A (pre-header draft) ----------
styxA = ("And through it all, the white male Styx circled the northern horizon, a constant "
         "reminder of the promise Ajani had made. The road. The corridor. The pact. Fifty "
         "years. It seemed like an eternity. It felt like a heartbeat.")
assert t.count(styxA) == 2
s0 = t.index(styxA)                       # first occurrence = Take A opener
hdr = t.index("**One Month After the Council**")
assert s0 < hdr
removed_dep = t[s0:hdr]
assert "The king exhaled slowly. The road would have to wait." in removed_dep
assert "One Month After" not in removed_dep
assert "Summon the elders" not in removed_dep   # Take B continuation preserved
t = t[:s0] + t[hdr:]
print(f"B2/B11: departure Take A excised ({len(removed_dep.split())} words)")

# splice Take A's unique details into Take B
rep("The Hummans have sent a full mercantile council. There's a Shell-Singer",
    "The Hummans have sent a full mercantile council, led by Ambassador Seris. "
    "There's a Shell-Singer", label='splice-seris')
rep("And the Blight. The watchmen on the northern ridge say the ground is stirring.",
    "And the Blight. The Chi'Thak have sent nothing. But the watchmen on the northern "
    "ridge say the ground is stirring.", label='splice-chithak')

# ---------- B2: mercenary kneeling two-take — cut Take A (tap/stillness version) ----------
brace = "The Stripe Paw mercenary braced for fire."
assert t.count(brace) == 2
m0 = t.index(brace)
tail = "The smile of a student who had just remembered a lesson his teacher had taught him long ago.</p>\n</div>"
m1 = t.index(tail, m0) + len(tail)
removed_merc = t[m0:m1]
assert removed_merc.count(brace) == 1          # only Take A
assert "She did not expect the touch." not in removed_merc  # Take B intact
assert "Guards, please remove our sister" not in removed_merc
t = t[:m0].rstrip('\n') + "\n\n\n" + t[m1:].lstrip('\n')
print(f"B2: mercenary Take A excised ({len(removed_merc.split())} words)")

# normalize newline piles
while '\n\n\n\n' in t:
    t = t.replace('\n\n\n\n', '\n\n\n')

f.write_text(t, encoding='utf-8')
after = (t.count('\n') + 1, len(t.split()))
print(f"OK chapter-02.md: lines {before[0]}->{after[0]}, words {before[1]}->{after[1]}")
print("Styx-circling count now:", t.count(styxA))
print("brace-for-fire count now:", t.count(brace))
