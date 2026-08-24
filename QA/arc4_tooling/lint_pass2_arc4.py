#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arc IV pass 2 — adapted from QA/lint_pass2.py (Arc I-II battery).
Exact contexts, cross-line quote state, single-quote classification,
lowercase proper nouns, typo sweep, meta-marker sweep. Read-only."""
import re, os

TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(os.path.dirname(TOOL_DIR))
CHDIR = os.path.join(BASE, "content", "story", "chapters")
FILES = ["chapter-arc4-%02d.md" % c for c in range(1, 7)]
TAG_RE = re.compile(r"<[^>]+>")

CONTRACTIONS = ["wasnt","cant","dont","wont","thats","ive","ill","id","im","whos",
 "didnt","couldnt","wouldnt","shouldnt","isnt","arent","youre","theyre","weve",
 "youve","hasnt","havent","doesnt","hed","shes","hes","lets","mustnt","wheres",
 "heres","theres","yall","hadnt","aint","hell"]

def strip_tags(s): return TAG_RE.sub("", s)
def ctx(txt, m, w=38):
    a = max(0, m.start()-w); b = min(len(txt), m.end()+w)
    return ("..." if a>0 else "") + txt[a:b].replace("\n"," ") + ("..." if b<len(txt) else "")

out = open(os.path.join(TOOL_DIR, "lint_pass2_arc4.txt"), "w", encoding="utf-8")
def P(*a): out.write(" ".join(str(x) for x in a) + "\n")

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
    names = ["wengari","veylar","veylara","pyrina","pyrinae","styx","threx","lightbringer",
             "chi'thak","humman","hummans","humans","human","bright paw","shadow paw",
             "stripe paw","motted paw","white dawn","black fire","kyre tree","kyrie tree",
             "bright paws","shadow paws","stripe paws","motted paws"]
    counts = {}
    for i, rline in enumerate(raw, 1):
        t = strip_tags(rline)
        for nm in names:
            for m in re.finditer(r"\b%s\b" % re.escape(nm), t):  # case-sensitive lowercase only
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
             ("Raise and eyebrow", r"Raise and eyebrow"), ("my father son", r"\bmy father son\b", re.I),
             ("stripes paw", r"\bstripes paw\b", re.I), ("t'vat", r"\bt'vat\b", re.I),
             ("hell (he'll)", r"\bhell\b", 0)]
    for entry in typos:
        label, pat = entry[0], entry[1]
        flags = entry[2] if len(entry) > 2 else 0
        for i, rline in enumerate(raw, 1):
            t = strip_tags(rline)
            for m in re.finditer(pat, t, flags):
                P("L%-4d %-18s %s" % (i, label, ctx(t, m)))

    P("--- 'King' CAPITALIZED CONTEXTS ---")
    for i, rline in enumerate(raw, 1):
        t = strip_tags(rline)
        for m in re.finditer(r"\bKing\b", t):
            P("L%-4d %s" % (i, ctx(t, m, 30)))
    P("--- 'king Ajani/Uthgard' lowercase-before-name check ---")
    for i, rline in enumerate(raw, 1):
        t = strip_tags(rline)
        for m in re.finditer(r"\bking (?:Ajani|Uthgard)", t):
            P("L%-4d %s" % (i, ctx(t, m, 30)))

    P("--- META / SCAFFOLD MARKERS ---")
    markers = [r"^\s*Let me\b", r"^Here is the\b", r"^Yes\.\s", r"\bIt also fits the\b",
               r"\bshould be grounded\b", r"\bThe Montage\b", r"\bMontage, Corrected\b",
               r"\bCorrected exchange\b", r"\bHere is the correction\b",
               r"\bHere is the corrected\b", r"\bI'll rewrite\b", r"\bLet me rewrite\b",
               r"\bLet me narrate\b", r"\bVersion A\b", r"\bVersion B\b",
               r"\bperfectly calibrated\b", r"\bcraft note\b"]
    for i, rline in enumerate(raw, 1):
        t = strip_tags(rline)
        for mk in markers:
            if re.search(mk, t, re.I):
                P("L%-4d [%s] %s" % (i, mk.replace("\\b",""), t.strip()[:120]))
                break
    P()

out.close()
print("done")
