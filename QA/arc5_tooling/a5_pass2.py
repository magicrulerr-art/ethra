#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pass 2 — Arc V (adapted from QA/lint_pass2.py): exact contexts, cross-line
quote state, single-quote classification, lowercase proper nouns, typo sweep,
meta-marker sweep. Read-only. Output: QA/arc5_tooling/a5_pass2.txt"""
import re, os, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CHDIR = os.path.join(BASE, "content", "story", "chapters")
OUTDIR = os.path.dirname(os.path.abspath(__file__))
FILES = ["chapter-arc5-%02d.md" % c for c in range(1, 23)]
TAG_RE = re.compile(r"<[^>]+>")

CONTRACTIONS = ["wasnt","cant","dont","wont","thats","ive","ill","id","im","whos",
 "didnt","couldnt","wouldnt","shouldnt","isnt","arent","youre","theyre","weve",
 "youve","hasnt","havent","doesnt","hed","shes","hes","lets","mustnt","wheres",
 "heres","theres","yall","hadnt","aint","hell"]

def strip_tags(s): return TAG_RE.sub("", s)
def ctx(txt, m, w=38):
    a = max(0, m.start()-w); b = min(len(txt), m.end()+w)
    return ("..." if a>0 else "") + txt[a:b].replace("\n"," ") + ("..." if b<len(txt) else "")

out = open(os.path.join(OUTDIR, "a5_pass2.txt"), "w", encoding="utf-8")
def P(*a):
    print(*a); out.write(" ".join(str(x) for x in a) + "\n")

for fname in FILES:
    raw = open(os.path.join(CHDIR, fname), encoding="utf-8").read().split("\n")
    P("="*90); P("FILE:", fname); P("="*90)

    P("--- CONTRACTIONS (word, line, context) ---")
    for i, rline in enumerate(raw, 1):
        t = strip_tags(rline)
        for w in CONTRACTIONS:
            for m in re.finditer(r"\b%s\b" % w, t, re.IGNORECASE):
                P("L%-4d %-8s %s" % (i, m.group(0), ctx(t, m)))
    for i, rline in enumerate(raw, 1):
        t = strip_tags(rline)
        for m in re.finditer(r"\bi['\u2019](?:ll|ve|d|m)\b", t):
            P("L%-4d i-apos   %s" % (i, ctx(t, m)))

    P("--- LOWERCASE STANDALONE i ---")
    for i, rline in enumerate(raw, 1):
        t = strip_tags(rline)
        for m in re.finditer(r"\bi\b", t):
            P("L%-4d %s" % (i, ctx(t, m)))

    P("--- HUM VARIANTS ---")
    for i, rline in enumerate(raw, 1):
        t = strip_tags(rline)
        for m in re.finditer(r"\b[Hh]u+m+ans?\b", t):
            P("L%-4d %-9s %s" % (i, m.group(0), ctx(t, m)))

    P("--- DOUBLE-QUOTE STATE (cross-line walk) ---")
    inside = False; open_line = None; problems = []
    for i, rline in enumerate(raw, 1):
        t = strip_tags(rline)
        for ch in t:
            if ch == '"':
                inside = not inside
                if inside: open_line = i
                else: open_line = None
        if inside and rline.strip() == "" and open_line is not None:
            problems.append("quote opened L%d still open across blank line L%d" % (open_line, i))
            open_line = None; inside = False
    if inside: problems.append("UNBALANCED: still open at EOF (opened L%s)" % open_line)
    if not problems: P("OK: all double quotes balanced within line groups")
    for p in problems: P("CHECK:", p)

    P("--- SINGLE-QUOTE CLASSIFICATION (O=open C=close-ish M=mid-word) ---")
    for i, rline in enumerate(raw, 1):
        t = strip_tags(rline)
        O=C=M=0
        for m in re.finditer("'", t):
            p = t[m.start()-1] if m.start()>0 else " "
            n = t[m.end()] if m.end()<len(t) else " "
            if p.isalpha() and n.isalpha(): M += 1
            elif n.isalpha(): O += 1
            elif p.isalpha(): C += 1
            else: O += 1
        if O or C:
            if O != C:
                P("L%-4d O=%d C=%d M=%d  %s" % (i, O, C, M, t.strip()[:150]))

    P("--- LOWERCASE PROPER-NOUN TOKENS ---")
    names = ["wengari","veylar","veylara","lightbringer","white dawn","bright paw",
             "shadow paw","stripe paw","motted paw","pyrina","pyrinae","styx",
             "humman","hummans","human","humans","kyrie tree","kyre tree",
             "bright paws","shadow paws","stripe paws","motted paws","kyrie",
             "t'vat","t'van","l'vat","chi'thak","cefiro","zephyr"]
    counts = {}
    for i, rline in enumerate(raw, 1):
        t = strip_tags(rline)
        for nm in names:
            for m in re.finditer(r"\b%s\b" % re.escape(nm), t):
                counts.setdefault(nm, []).append(i)
                if len(counts[nm]) <= 6:
                    P("L%-4d %-13s %s" % (i, nm, ctx(t, m, 30)))
    for nm, ls in sorted(counts.items()):
        P("SUMMARY %-13s x%d lines %s" % (nm, len(ls), ls))

    P("--- TYPO SWEEP ---")
    typos = [("gratious", r"\bgratious\b", re.I), ("payed", r"\bpayed\b", re.I),
             ("producy", r"\bproducy\b", re.I), ("assasins", r"\bassasins?\b", re.I),
             ("appropiate", r"\bappropiate\b", re.I), ("handt", r"\bhandt\b", re.I),
             ("wanning", r"\bwanning\b", re.I), ("kyrie", r"\bkyrie\b", re.I),
             ("dessert sun", r"\bdessert sun\b", re.I), ("three thousands", r"\bthree thousands\b", re.I),
             ("Raise and eyebrow", r"Raise and eyebrow", 0), ("my father son", r"\bmy father son\b", re.I),
             # arc5-specific observed suspects
             ("trough(through)", r"\btrough\b", re.I), ("tores(tore)", r"\btores\b", re.I),
             ("visibily", r"\bvisibily\b", re.I), ("it's body/it's own", r"\bit's (?:body|own)\b", re.I),
             ("cleaves", r"\bcleaves\b", re.I), ("yells", r"\byells?\b", re.I),
             (" Bright Mane ", r"\bBright Mane\b", 0), ("Brightmane", r"\bBrightmane\b", 0)]
    for entry in typos:
        label, pat, flags = entry
        for i, rline in enumerate(raw, 1):
            t = strip_tags(rline)
            for m in re.finditer(pat, t, flags):
                P("L%-4d %-18s %s" % (i, label, ctx(t, m)))

    P("--- 'King' CAPITALIZED CONTEXTS ---")
    for i, rline in enumerate(raw, 1):
        t = strip_tags(rline)
        for m in re.finditer(r"\bKing\b", t):
            P("L%-4d %s" % (i, ctx(t, m, 30)))
    P("--- 'king <Name>' lowercase-before-name check ---")
    for i, rline in enumerate(raw, 1):
        t = strip_tags(rline)
        for m in re.finditer(r"\bking [A-Z][a-z]+", t):
            P("L%-4d %s" % (i, ctx(t, m, 30)))

    P("--- META / SCAFFOLD / DRAFT-INSTRUCTION MARKERS ---")
    markers = [r"^\s*Let me\b", r"^Here is the\b", r"\bVersion [AB]\b", r"\bCorrected\b",
               r"\bMontage\b", r"\brewrite\b", r"\bHere'?s? (?:a |the )?(?:better|revised|new) version\b",
               r"^\*\*[A-Z][^*]{3,60}\*\*\s*$", r"\byells\b", r"\bsays\b"]
    for i, rline in enumerate(raw, 1):
        t = strip_tags(rline)
        for mk in markers:
            if re.search(mk, t, re.I):
                P("L%-4d [%s] %s" % (i, mk.replace("\\b",""), t.strip()[:140]))
                break
    P()

out.close()
print("done -> a5_pass2.txt")
