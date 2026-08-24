# -*- coding: utf-8 -*-
"""
apply_arc3_fix_canon.py — Arc 3 umbrella remediation, canonical implementation.

Specs: QA/arc3_tooling/arc3_fix_plan.md + arc3_fix_plan_part2.md
Target: content/story/chapter-03.md (umbrella master, 2894 lines verified).

Modes:
  --dry-run   all assertions + full op-log, NO write (default)
  --write     apply and write umbrella in place

Any assertion failure => prints FAILED lines, 'ABORTED - NO WRITE', exit 1.
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
UMB = os.path.normpath(os.path.join(HERE, '..', '..', 'content', 'story', 'chapter-03.md'))

MODE = sys.argv[1] if len(sys.argv) > 1 else '--dry-run'
if MODE not in ('--dry-run', '--write'):
    print('usage: apply_arc3_fix_canon.py [--dry-run|--write]'); sys.exit(2)

raw = io.open(UMB, 'r', encoding='utf-8', newline='').read()
ends_nl = raw.endswith('\n')
L = raw.split('\n')
if ends_nl:
    assert L and L[-1] == '', 'unexpected trailing segment'
    L = L[:-1]
N0 = len(L)

errors = []
oplog = []
def err(id_, msg): errors.append('[%s] %s' % (id_, msg))
def ok(msg): oplog.append(msg)

def eq(a, b): return a.strip() == b.strip()

def a_line(n1, id_, contain=None, equal=None, start=None):
    if n1 < 1 or n1 > len(L):
        err(id_, 'line %d out of range' % n1); return ''
    s = L[n1 - 1]
    if equal is not None and not eq(s, equal):
        err(id_, 'line %d equal-check failed: %r' % (n1, s[:100]))
    if contain is not None and contain not in s:
        err(id_, 'line %d contain-check failed (%r): %r' % (n1, contain, s[:100]))
    if start is not None and not s.strip().startswith(start):
        err(id_, 'line %d start-check failed (%r): %r' % (n1, start, s[:100]))
    return s

def a_count(sub, want, id_, regex=False):
    if regex:
        hits = [(n + 1, l[:90]) for n, l in enumerate(L) if re.search(sub, l)]
    else:
        hits = [(n + 1, l[:90]) for n, l in enumerate(L) if sub in l]
    if len(hits) != want:
        err(id_, 'count %r = %d, want %d :: %s' % (sub, len(hits), want, hits[:6]))
    return hits

# =====================================================================
# PHASE 1 — captures (assert exact shapes on the original file)
# =====================================================================
a_line(896, 'CAP-joke-div', equal='<div class="dialogue-block">')
a_line(897, 'CAP-joke-line', contain='"Without even eating breakfast,"')
a_line(898, 'CAP-joke-end', equal='</div>')
JOKE = L[895:898]
ok('CAPTURE joke block L896-898: %r...' % JOKE[1][:60])

gr_hits = a_count("*'yes they would make good regents", 1, 'CAP-goodreg')
GOODREG_NORM = "'yes they would make good regents, two for two and they're unscathed'"
if gr_hits:
    ok('CAPTURE good-regents thought L%d' % gr_hits[0][0])

HALF_OLD = "*'half of it down, no one is engaging, it should end soon... They will want glory for their name'*"
HALF_NEW = "'half of it down, no one is engaging, it should end soon... They will want glory for their name'"
a_count(HALF_OLD, 1, 'CAP-half-thought')

# =====================================================================
# PHASE 2 — deletion anchor assertions (original 1-based line numbers)
# =====================================================================
# D1 J1 Torek version A + premature closing (318-327); keep version B at 329
a_line(318, 'D1', equal='<div class="dialogue-block">')
a_line(319, 'D1', contain='I have served four kings,')
a_line(320, 'D1', equal='</div>')
a_line(323, 'D1', start='The elders filed out of the chamber')
a_line(325, 'D1', start='The negotiations were complete.')
a_line(327, 'D1', equal='')
a_line(329, 'D1-KEEP', contain='I served your father,')

# D2 J2 Fire Feet scaffold (333-354); bullets already in QA/bestiary_notes.md
a_line(333, 'D2', equal='**The Fire Feet \u2014 Lore Confirmed**')
a_line(336, 'D2', start='- **Physical Description:**')
a_line(348, 'D2', start='- **Bond:**')
a_line(351, 'D2', contain="piecing together clues from Ajani's past")
a_line(354, 'D2', equal='')
a_line(355, 'D2-KEEP', start='The chamber had emptied.')

# D3 J4a Solen confrontation occ1 (883-908); occ2 kept from 909 heading
a_line(883, 'D3', start='The Bright Paw elders did not wait')
a_line(906, 'D3', start='The other Bright Paws fell silent')
a_line(908, 'D3', equal='')
a_line(909, 'D3-KEEP', equal='**The Hour Before the Tournament**')

# D4 J4b battle occ1 + stray (1536-1613); keep 1531 thought, 1533 basin, occ2 at 1614
a_line(1531, 'D4-KEEP-thought', equal=HALF_OLD)
a_line(1533, 'D4-KEEP-basin', equal='The basin erupted.')
a_line(1536, 'D4', start='Rask led the charge, her massive frame barreling toward the Motted Paws')
if 'auras blazing gold' in L[1535]: err('D4', 'occ1 unexpectedly contains blazing gold')
a_line(1611, 'D4', equal='*The basin erupted.*')
a_line(1614, 'D4-KEEP-occ2', start='Rask led the charge, her massive frame barreling toward the Motted Paws', contain='auras blazing gold')

# D5 duplicate incense closer + recap layers X/Y/Z (1657-1721); keep layer W at 1722
a_line(1654, 'D5-KEEP-champions', start='Two champions remained standing: Sylva of the Motted Paws')
a_line(1657, 'D5', equal='The incense stick crumbled into ash. The first phase was over.')
a_line(1660, 'D5', start='The Motted Paws had drawn first blood')
a_line(1719, 'D5', contain='And the desert would remember.')
a_line(1721, 'D5', equal='')
a_line(1722, 'D5-KEEP-layerW', equal='The incense stick crumbled into ash. The first phase was over.')

# D6 planning transition (1945-1947)
a_line(1945, 'D6', start="Let's follow the arena as the Styx feathers")
a_line(1948, 'D6-KEEP', start='The Pyrinae moved with the quiet efficiency')

# D7 J3 Zara Ember-gift beat occ2 (2452-2454); keep occ1 2386-2390 and Kareth 2455
a_line(2388, 'D7-KEEP-occ1', contain='fan of the fire feet')
a_line(2452, 'D7', start='Zara watched the exchange from the fence rail', contain='fan of the fire feet')
a_line(2455, 'D7-KEEP-kareth', start='Kareth leaned on his obsidian staff')

# D8 mounted version A (2278-2297); keep version B 2298+
INC = 'The incense flared to life, and the arena held its breath.'
a_line(2278, 'D8', start=INC)
a_line(2294, 'D8', contain='He dropped his paw, and the arena erupted.')
a_line(2295, 'D8', equal='</div>')
a_line(2296, 'D8', equal='')
a_line(2297, 'D8', equal='')
a_line(2298, 'D8-KEEP-vB', start=INC)

# D9 **Logic** craft block (2570-2622)
a_line(2570, 'D9', equal='**Logic**')
a_line(2620, 'D9', contain='The green fire is the mark of that year')
a_line(2622, 'D9', equal='')
a_line(2623, 'D9-KEEP', start='The third strike was the kill shot')

# D10 compressed feint dialogue block (2770-2772); keep canon 2791-2798
a_line(2770, 'D10', equal='<div class="dialogue-block">')
a_line(2771, 'D10', contain='"The feint,"', )
a_line(2771, 'D10', contain='I yield. The crown is yours.')
a_line(2772, 'D10', equal='</div>')
a_line(2792, 'D10-KEEP-canon1', contain='The crowd erupted. The Styx screamed.')
a_line(2797, 'D10-KEEP-canon2', contain='I yield. The crown is yours.')

DELETIONS = [
    ('D10', 2770, 2772), ('D9', 2570, 2622), ('D8', 2278, 2297),
    ('D7', 2452, 2454), ('D6', 1945, 1947), ('D5', 1657, 1721),
    ('D4', 1536, 1613), ('D3', 883, 908), ('D2', 333, 354), ('D1', 318, 327),
]
DELETIONS = sorted(DELETIONS, key=lambda d: -d[1])  # strict bottom-up by start index

if errors:
    print('\n'.join('FAILED ' + e for e in errors))
    print('ABORTED - NO WRITE (anchor phase)'); sys.exit(1)

# =====================================================================
# PHASE 3 — deletions bottom-up
# =====================================================================
DEL_EXPECT = {id_: (L[s - 1], L[e - 1]) for id_, s, e in DELETIONS}
for id_, s, e in DELETIONS:
    exp_first, exp_last = DEL_EXPECT[id_]
    if L[s - 1] != exp_first or L[e - 1] != exp_last:
        err(id_, 'content shifted at apply time (L%d/L%d)' % (s, e))
        continue
    first, last = L[s - 1][:60], L[e - 1][:60]
    del L[s - 1:e]
    ok('DELETE %s L%d-%d :: first=%r last=%r' % (id_, s, e, first, last))
if errors:
    print('\n'.join('FAILED ' + e for e in errors))
    print('ABORTED - NO WRITE (deletion phase)'); sys.exit(1)

# =====================================================================
# PHASE 4 — insertions (content-anchored on the post-deletion list)
# =====================================================================
def find_unique(sub, id_, equal=False):
    hits = [n for n, l in enumerate(L) if (eq(l, sub) if equal else sub in l)]
    if len(hits) != 1:
        err(id_, 'anchor %r found %d times' % (sub[:60], len(hits))); return -1
    return hits[0]

# I1 good-regents between champions paragraph and layer-W opener
tc = find_unique('Two champions remained standing: Sylva of the Motted Paws', 'I1-champions')
wline = find_unique('The incense stick crumbled into ash. The first phase was over.', 'I1-closer', equal=True)
if tc >= 0 and wline > tc >= 0:
    gap = L[tc + 1:wline]
    if any(g.strip() for g in gap):
        err('I1', 'non-blank gap between anchors: %r' % [g[:40] for g in gap if g.strip()][:3])
    else:
        L[tc + 1:wline] = ['', GOODREG_NORM, '']
        ok('INSERT I1 good-regents after L%d champions paragraph' % (tc + 1))

# I2 breakfast joke after Vasha block in occ2
v = find_unique('You just offered it as a prize. To anyone. Without consulting us.', 'I2-vasha')
if v >= 0:
    if not eq(L[v + 1], '</div>'):
        err('I2', 'expected </div> after Vasha line, got %r' % L[v + 1][:60])
    else:
        L[v + 2:v + 2] = ['', JOKE[0], JOKE[1], JOKE[2]]
        ok('INSERT I2 breakfast joke after Vasha </div>')

# I3 half-thought normalize in place
h = find_unique(HALF_OLD, 'I3-half')
if h >= 0:
    L[h] = HALF_NEW
    ok('REPLACE I3 half-thought delimiter normalize')

# =====================================================================
# PHASE 5 — mechanical replacements (exact substrings; assert >=1)
# =====================================================================
M = [
    ('M1',  'welcome to the wengari brothers!', 'welcome to the Wengari brothers!'),
    ('M2',  '"t\'vat call for the elder council of the striped paws, now please "',
            '"T\'vat call for the elder council of the Stripe Paws, now please "'),
    ('M3',  "'therye here, good...why do they seem mad?'", "'they're here, good...why do they seem mad?'"),
    ('M4',  'who rules the wengari?', 'who rules the Wengari?'),
    ('M5',  'news about the hummans as well', 'news about the Hummans as well'),
    ('M6',  '"the best of the humans here means...what Zara ? Tell me what do the humans do best ?"',
            '"the best of the Hummans here means...what Zara ? Tell me what do the Hummans do best ?"'),
    ('M7',  'the humans will send their best here', 'the Hummans will send their best here'),
    ('M8',  '"the stripe paws will become', '"the Stripe Paws will become'),
    ('M9',  'what did father always said ,', 'what did father always say ,'),
    ('M10a', "FRIEND'S!!", 'FRIENDS!!'),
    ('M10b', 'A KING CANT BE', "A KING CAN'T BE"),
    ('M11', '*The Bright Paw Elders (Closing Scene)*', '**The Bright Paw Elders**'),
    ('M12', '*The king has put his crown on the line. The tournament begins in an hour. The Wengari are choosing their champions. The other races are choosing theirs. What should I do?*',
            "'The king has put his crown on the line. The tournament begins in an hour. The Wengari are choosing their champions. The other races are choosing theirs. What should I do?'"),
    ('M13', '"tell me solen, who rules the wenfari ?"', '"tell me Solen, who rules the Wengari ?"'),
    ('M14a', "'fhe sun is up", "'the sun is up"),
    ('M14b', 'BROTHERS STEMMED GUESTS', 'BROTHERS ESTEEMED GUESTS'),
    ('M15', 'GUESTS RISED TO THE CHALLENGE, LETS HONOR', "GUESTS RISEN TO THE CHALLENGE, LET'S HONOR"),
    ('M16a', 'ESPECTACULAR, THIS', 'SPECTACULAR, THIS'),
    ('M16b', 'NO MORTAL WOUNDS ITS A TOURNAMENT', "NO MORTAL WOUNDS IT'S A TOURNAMENT"),
    ('M17', 'mycelial network: *The White Dawn does not ask for mercy. The White Dawn does not offer it. The tournament will be brutal. The tournament will be remembered.*',
            "mycelial network: 'The White Dawn does not ask for mercy. The White Dawn does not offer it. The tournament will be brutal. The tournament will be remembered.'"),
    ('M19', "*Let's begin!*", "'Let's begin!'"),
    ('M20a', 'LIVE NOT ONLY ON THE DESER BUT', 'LIVE NOT ONLY ON THE DESERT BUT'),
    ('M20b', 'ILL DEMONSTRATE, FRIENDS PYRANEI', "I'LL DEMONSTRATE, FRIENDS PYRINAE"),
    ('M21a', 'i havent seen one since i was a child', "I haven't seen one since I was a child"),
    ('M21b', 'care if i touched one?!', 'care if I touched one?!'),
    ('M21c', 'dont look too much, regal!', "don't look too much, regal!"),
    ('M22a', "'styx in heaven i blew it!!", "'Styx in heaven I blew it!!"),
    ('M22b', 'so good!!, i should make', 'so good!!, I should make'),
    ('M22c', 'definetly.. a yearly thing', 'definitely.. a yearly thing'),
    ('M23a', 'THEN I SHALL IS IT DONE, AFTER THE DUEL ENDS', 'THEN, WHEN IT IS DONE, AFTER THE DUEL ENDS'),
    ('M23b', 'AND THE PYRANEI, THIS', 'AND THE PYRINAE, THIS'),
    ('M23c', 'ill gauge their eyes out', "I'll gouge their eyes out"),
    ('M23d', 'i can already see', 'I can already see'),
    ('M24a', "*OH, ok, she has claws... spear then'", "'OH, ok, she has claws... spear then'"),
    ('M24b', 'should be, lets have the sun', "should be, let's have the sun"),
    ('M24c', 'dead in two moves*', "dead in two moves'"),
    ('M25a', "*What on....ok... calm, breathe, shes unarmed, sword then, lets see her try to catch a dual blade'-",
             "'What on....ok... calm, breathe, she's unarmed, sword then, let's see her try to catch a dual blades'-"),
    ('M25b', '"You\'re good, but im better!"', '"You\'re good, but I\'m better!"'),
    ('M25c', 'dont allow her openings', "don't allow her openings"),
    ('M25d', 'my fur is starting to bristle*', "my fur is starting to bristle'"),
    ('M26a', "*This is getting annoying!!!, why cant i reach her?!, im faster than her, im sure i am, im stronger than her, how is she still catching me?!'",
             "'This is getting annoying!!!, why can't I reach her?!, I'm faster than her, I'm sure I am, I'm stronger than her, how is she still catching me?!'"),
    ('M26b', 'but im still better!!', 'but I\'m still better!!'),
    ('M26c', "'Faint, open with the sword", "'Feint, open with the sword"),
    ('M26d', 'all i need is one good strike*', "all I need is one good strike'"),
    ('M26e', 'she wont be able to evade', "she won't be able to evade"),
    ('M27a', "*OK THIS ENDS NOW, SHE NEEDS TO GO DOWN, NOW'", "'OK THIS ENDS NOW, SHE NEEDS TO GO DOWN, NOW'"),
    ('M27b', 'youre good, i admit it', "you're good, I admit it"),
    ('M27c', 'but i am still the heir of the light, WITNESS', 'but I am still the heir of the Light, WITNESS'),
    ('M27d', 'i cant loose the crown!!!', "I can't lose the crown!!!"),
    ('M27e', 'i havent even made the road yet!!, ill be the laughing stock of the families for millenia',
             "I haven't even made the road yet!!, I'll be the laughing stock of the families for millennia"),
    ('M27f', 'lost in duel!!*', "lost in duel!!'"),
    ('M28a', "*what?'", "'what?'"),
    ('M28b', 'statecraft...*', "statecraft...'"),
    ('M28c', 'Infurating woman', 'Infuriating woman'),
    ('M29', "'im this close to skewering her..'", "'I'm this close to skewering her..'"),
]

# M18 special: 3-line pulse merge
m18_head = 'network: *The White Dawn has changed the rules.'
m18_tail = 'The tournament will be a battle. The desert will drink deep today.*'
hits = [n for n, l in enumerate(L) if l.strip().endswith(m18_head)]
if len(hits) != 1:
    err('M18', 'head anchor found %d times' % len(hits))
else:
    x = hits[0]
    if L[x + 1].strip() != '' or L[x + 2].strip() != m18_tail:
        err('M18', 'tail shape mismatch: %r / %r' % (L[x + 1][:40], L[x + 2][:40]))
    else:
        prefix = L[x][:L[x].index('network: ') + len('network: ')]
        L[x] = prefix + "'The White Dawn has changed the rules. The tournament will be a battle. The desert will drink deep today.'"
        del L[x + 1:x + 3]
        ok('REPLACE M18 pulse merged into one paragraph (3 lines -> 1)')

total_repl = 0
for id_, old, new in M:
    cnt = sum(l.count(old) for l in L)
    if cnt < 1:
        err(id_, 'substring not found: %r' % old[:80]); continue
    L = [l.replace(old, new) for l in L]
    total_repl += cnt
    ok('REPLACE %s x%d :: %r -> %r' % (id_, cnt, old[:44], new[:44]))

# =====================================================================
# PHASE 6 — residual self-checks
# =====================================================================
text2 = '\n'.join(L)
RES_ZERO = [
    ('wengari', r'\bwengari\b'), ('wenfari', r'\bwenfari\b'),
    ('humman-lower', r'\bhummans\b'), ('humans-lower', r'\bhumans\b'),
    ('therye', r'therye'), ('tvat-lower', r"\bt'vat\b"), ("FRIEND'S", re.escape("FRIEND'S")),
    ('fhe', r'\bfhe\b'), ('STEMMED', r'STEMMED'), ('RISED', r'\bRISED\b'),
    ('ESPECTACULAR', r'ESPECTACULAR'), ('DESER', r'\bDESER\b'), ('PYRANEI', r'PYRANEI'),
    ('definetly', r'definetly'), ('Infurating', r'Infurating'), ('millenia', r'millenial?\b|millenia'),
    ('gauge', r'\bgauge\b'), ('loose', r'\bloose\b'), ('Faint-open', r"'Faint,"),
    ('dual-blade-sg', r'\bdual blade\b'),
    ('cant', r'\bcant\b'), ('dont', r'\bdont\b'), ('havent', r'\bhavent\b'),
    ('shes', r'\bshes\b'), ('wont', r'\bwont\b'), ('youre', r'\byoure\b'),
    ('im-lower', r'\bim\b'), ('ill-lower', r'\bill\b'), ('lets', r'\blets\b'),
    ('styx-lower', r'\bstyx\b'),
    ('CANT', r'\bCANT\b'), ('LETS', r'\bLETS\b'), ('ILL', r'\bILL\b'),
    ('solen-lower', r'\bsolen\b'), ('heir-lower', r'heir of the light'),
    ('garble', r'THEN I SHALL IS IT DONE'), ('closing-scene', r'\(Closing Scene\)'),
    ('asterisk-quote', re.escape("*'")), ('quote-asterisk', re.escape("'*")),
    ('always-said', r'always said\b'),
]
for name, pat in RES_ZERO:
    m = re.findall(pat, text2)
    if m:
        err('RES-' + name, '%d residual: %s' % (len(m), m[:4]))
    else:
        ok('RESIDUAL-CLEAN %s' % name)

its_hits = [(n + 1, l.strip()[:70]) for n, l in enumerate(L) if re.search(r'\bITS\b', l)]
ok('RESIDUAL-INFO ITS-uppercase remaining=%d (out-of-scope per plan): %s' % (len(its_hits), its_hits))
i_hits = [(n + 1, l.strip()[:70]) for n, l in enumerate(L) if re.search(r'\bi\b', l)]
if i_hits:
    err('RES-i', 'standalone lowercase i remaining: %s' % i_hits)
else:
    ok('RESIDUAL-CLEAN standalone-i')

# =====================================================================
# REPORT + writeback
# =====================================================================
print('=== OPLOG (%d ops) ===' % len(oplog))
for o in oplog: print(' ', o)
print('original lines: %d -> final lines: %d' % (N0, len(L)))
print('mechanical replacements applied: %d' % total_repl)
if errors:
    print('\n'.join('FAILED ' + e for e in errors))
    print('ABORTED - NO WRITE'); sys.exit(1)

if MODE == '--write':
    out = '\n'.join(L) + ('\n' if ends_nl else '')
    io.open(UMB, 'w', encoding='utf-8', newline='').write(out)
    print('WRITTEN ->', UMB)
else:
    print('DRY-RUN OK - no write performed')
