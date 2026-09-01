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
TIC = [
    'might have been', 'green fire', 'patient as the stars',
    'for a long, breathless moment', 'slow, rhythmic',
]
# word-boundary regexes (avoid substring false positives like "intertwined")
CANON_RE = [
    ('super-organism', re.compile(r'super-organism', re.I)),
    ('wine', re.compile(r'\bwine\b', re.I)),
    ('buried two', re.compile(r'buried two', re.I)),
    ('buried three', re.compile(r'buried three', re.I)),
]


def scan(masters):
    results = {}
    for name, patterns in (('DEBRIS', DEBRIS), ('DRIFT', DRIFT),
                           ('TIC', TIC)):
        for p in patterns:
            hits = []
            for f in masters:
                fn = os.path.basename(f)
                for i, line in enumerate(open(f, encoding='utf-8'), 1):
                    if p.lower() in line.lower():
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
    for cls in ('DEBRIS', 'DRIFT', 'TIC', 'CANON'):
        print('\n== %s ==' % cls)
        for p, hits in results[cls]:
            loc = ', '.join(hits[:5]) + (' ...' if len(hits) > 5 else '')
            print('  %-32s %3d  %s' % (p, len(hits), loc))
    n, bad = div_balance()
    print('\n== DIV-BALANCE ==')
    print('  splits checked: %d, unbalanced: %d%s' %
          (n, len(bad), (' -> ' + ', '.join(bad)) if bad else ''))


if __name__ == '__main__':
    main()
