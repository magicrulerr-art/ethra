#!/usr/bin/env python3
"""Ethra editorial sweep — reusable review battery (canon reference companion).

    python canon/editorial_sweep.py

Scans the published MASTERS only (content/story/chapter-0*.md — raw/ excluded)
for known defect classes, and runs the div-balance gate across all splits.
Read-only: it reports, never edits. Fixes route through the umbrella pipeline.

Pattern classes:
  DEBRIS  — dictation/collaboration residue that must not survive into prose
  DRIFT   — spellings/terms adjudicated out of canon
  TIC     — image-reuse tics (Phase 2/3 triage — counts only, NO cutting
            without Ainz's scope ruling)
  CANON   — open adjudication items (tracked, expected non-zero until ruled)

2026-09-01 additions (Ainz rulings of that date):
  - 'humman king' drift regex (Hummans have SULTANS not kings)
  - wine moved to zero-tolerance word-boundary regex (no wine in Ethra;
    substitutes: frostfire / rune berry juice / Bitter Ale by speaker)
  - montage debris signatures ('private ceremon', 'The Veylar came first',
    'obsidian dagger', 'first gift-giving') — the excised ch04 gift montage
  - gift-uniqueness check: 'offer this gift' / 'I accept this gift' must
    appear exactly once (water-hole race scene is the only gift-giving)
"""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORY = os.path.join(ROOT, 'content', 'story')

DEBRIS = [
    'the scene ends', 'we cut to', 'we zoom out', 'we switch back',
    "Let's start the next", "Let's continue", 'Ok next', 'next one is',
    'agree with these beats', 'You understand that', 'voice booming',
    'I overcomplicated', 'You are right, and I apologize',
    'my narrative mistake', 'the next pov',
    # Excised ch04 gift-montage signatures (Ainz 2026-09-01: never wrote it)
    'private ceremon', 'The Veylar came first', 'obsidian dagger',
    'first gift-giving',
]
# Family-name signature only: the generic adjective "mottled" (fur patterns)
# is legitimate English; the ruling covers the family name "MOTTED Paws".
DRIFT = [
    'Mottled Paw', 'Styxiancus', "T'vat", 'Your Immensity', 'immensity',
]
# case-sensitive patterns (exact case as written)
DRIFT_CASE = [
    ('lowercase humman(s)', re.compile(r'\bhumman\b')),
]
# word-boundary regexes adjudicated to ZERO (exact case-insensitive)
DRIFT_RE = [
    # no wine in Ethra (Ainz ruling; substring scan false-counts "intertwined")
    ('wine (\\bwine\\b)', re.compile(r'\bwine\b', re.I)),
    # Hummans have Sultans, not kings (Ainz 2026-09-01)
    ('humman king(s)', re.compile(r'humman\s+king', re.I)),
    ('king of the Hummans', re.compile(r'king of the hummans', re.I)),
]
# exact-count checks: (label, pattern, expected_count)
EXACT_COUNT = [
    ('gift: offer this gift', 'The Stripe Paws offer this gift', 1),
    ('gift: I accept this gift', 'I accept this gift', 1),
]
TIC = [
    'might have been', 'green fire', 'patient as the stars',
    'for a long, breathless moment', 'slow, rhythmic',
]
# word-boundary regexes (avoid substring false positives like "intertwined")
CANON_RE = [
    ('super-organism', re.compile(r'super-organism', re.I)),
    ('buried two', re.compile(r'buried two', re.I)),
    ('buried three', re.compile(r'buried three', re.I)),
]


def scan(masters):
    results = {}
    for name, patterns in (('DEBRIS', DEBRIS), ('DRIFT', DRIFT),
                           ('TIC', TIC)):
        # TIC counts OCCURRENCES (triage-ledger metric: one line may carry
        # several instances of a construction); DEBRIS/DRIFT count lines.
        per_occurrence = (name == 'TIC')
        for p in patterns:
            hits = []
            for f in masters:
                fn = os.path.basename(f)
                for i, line in enumerate(open(f, encoding='utf-8'), 1):
                    if p.lower() in line.lower():
                        if per_occurrence:
                            hits.extend(
                                ['%s:%d' % (fn, i)] *
                                line.lower().count(p.lower()))
                        else:
                            hits.append('%s:%d' % (fn, i))
            results.setdefault(name, []).append((p, hits))
    for label, rx in DRIFT_CASE:
        hits = []
        for f in masters:
            fn = os.path.basename(f)
            for i, line in enumerate(open(f, encoding='utf-8'), 1):
                if rx.search(line):
                    hits.append('%s:%d' % (fn, i))
        results.setdefault('DRIFT', []).append((label, hits))
    for label, rx in DRIFT_RE:
        hits = []
        for f in masters:
            fn = os.path.basename(f)
            for i, line in enumerate(open(f, encoding='utf-8'), 1):
                if rx.search(line):
                    hits.append('%s:%d' % (fn, i))
        results.setdefault('DRIFT', []).append((label, hits))
    for label, pat, expected in EXACT_COUNT:
        total = 0
        for f in masters:
            total += open(f, encoding='utf-8').read().count(pat)
        status = 'OK' if total == expected else 'VIOLATION (expected %d)' % expected
        results.setdefault('EXACT-COUNT', []).append(
            ('%s [%s]' % (label, status), total))
    for label, rx in CANON_RE:
        hits = []
        for f in masters:
            fn = os.path.basename(f)
            for i, line in enumerate(open(f, encoding='utf-8'), 1):
                if rx.search(line):
                    hits.append('%s:%d' % (fn, i))
        results.setdefault('CANON', []).append((label, hits))
    return results


def div_balance():
    bad, n = [], 0
    for f in sorted(glob.glob(os.path.join(STORY, 'chapters', 'chapter-arc*.md'))):
        t = open(f, encoding='utf-8').read()
        n += 1
        if t.count('<div') != t.count('</div>'):
            bad.append(os.path.basename(f))
    return n, bad


def main():
    masters = sorted(glob.glob(os.path.join(STORY, 'chapter-0*.md')))
    results = scan(masters)
    print('masters scanned: %d' % len(masters))
    for cls in ('DEBRIS', 'DRIFT', 'TIC', 'EXACT-COUNT', 'CANON'):
        print('\n== %s ==' % cls)
        for p, hits in results[cls]:
            if isinstance(hits, int):
                print('  %-52s %3d' % (p, hits))
            else:
                loc = ', '.join(hits[:5]) + (' ...' if len(hits) > 5 else '')
                print('  %-32s %3d  %s' % (p, len(hits), loc))
    n, bad = div_balance()
    print('\n== DIV-BALANCE ==')
    print('  splits checked: %d, unbalanced: %d%s' %
          (n, len(bad), (' -> ' + ', '.join(bad)) if bad else ''))


if __name__ == '__main__':
    main()
