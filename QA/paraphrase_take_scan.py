# -*- coding: utf-8 -*-
"""Paraphrase-take detector for Ethra chapters.
Catches what verbatim scanners miss:
  (a) SHARED-PREFIX pairs: two paragraphs whose first N words are identical
      but which diverge afterward (rewritten takes of the same beat).
  (b) NEAR-DUPLICATE pairs: high word-overlap (Jaccard >= 0.55) among
      paragraphs >= 20 words, excluding verbatim-equal (those are class 1).
  (c) REPEATED DIALOGUE: identical quoted speech (>= 8 words) in > 1 block.
Refrains (deliberate repetition) will appear; human classifies."""
import re, glob, pathlib

MINW = 12          # shared-prefix threshold in words
MINP = 20          # min paragraph words for near-dupe comparison
JACC = 0.55

def paras(text):
    out = []
    for blk in re.split(r'\n\s*\n', text):
        blk = blk.strip()
        if not blk:
            continue
        ps = re.findall(r'<p[^>]*>(.*?)</p>', blk, re.S)
        if ps:
            out.extend(ps)
        elif '<p' not in blk:
            out.append(blk)
    return out

def norm(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = re.sub(r'\s+', ' ', s).lower().strip(' .')
    return s

def words(s):
    return norm(s).split()

total_hits = 0
for f in sorted(glob.glob('ethra_site/content/story/chapters/chapter-arc[1-7]-*.md')):
    text = pathlib.Path(f).read_text(encoding='utf-8')
    plist = paras(text)
    pwords = [words(p) for p in plist]
    hits = []

    # (a) shared-prefix pairs
    for i in range(len(plist)):
        for j in range(i + 1, len(plist)):
            wi, wj = pwords[i], pwords[j]
            if len(wi) < MINW or len(wj) < MINW:
                continue
            if wi == wj:
                continue  # verbatim class 1, already known
            k = 0
            while k < min(len(wi), len(wj)) and wi[k] == wj[k]:
                k += 1
            if k >= MINW:
                hits.append(('PREFIX', k, plist[i], plist[j]))

    # (b) near-duplicate pairs (Jaccard on content words)
    sets = [set(w) for w in pwords]
    for i in range(len(plist)):
        if len(pwords[i]) < MINP:
            continue
        for j in range(i + 1, len(plist)):
            if len(pwords[j]) < MINP:
                continue
            if pwords[i] == pwords[j]:
                continue
            inter = len(sets[i] & sets[j])
            union = len(sets[i] | sets[j])
            if union and inter / union >= JACC:
                # skip if already a PREFIX hit for this pair
                if not any(h[2] is plist[i] and h[3] is plist[j] for h in hits):
                    hits.append(('NEAR', round(inter / union, 2), plist[i], plist[j]))

    # (c) repeated dialogue
    seen = {}
    for p in plist:
        for q in re.findall(r'["\u201c]([^"\u201d]{40,})["\u201d]', p):
            qn = norm(q)
            if len(qn.split()) >= 8:
                seen.setdefault(qn, 0)
                seen[qn] += 1
    for q, c in seen.items():
        if c > 1:
            hits.append(('SPEECH', c, q[:90], ''))

    if hits:
        print(f"\n===== {pathlib.Path(f).name} =====")
        for kind, score, a, b in hits:
            total_hits += 1
            na = norm(a)
            print(f"[{kind} {score}] {na[:105]}...")
            if b:
                print(f"        vs: {norm(b)[:105]}...")

print(f"\nTOTAL FLAGGED PAIRS/ITEMS: {total_hits}")
