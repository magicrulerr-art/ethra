#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pass 2: exact contexts, cross-line quote state, single-quote classification,
lowercase race names, typo sweep, meta-marker sweep. Read-only."""
import re, os, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHDIR = os.path.join(BASE, "content", "story", "chapters")
FILES = ["chapter-arc%d-%02d.md" % (a, c) for a in (1, 2) for c in range(1, 7)]
TAG_RE = re.compile(r"<[^>]+>")

CONTRACTIONS = ["wasnt","cant","dont","wont","thats","ive","ill","id","im","whos",
 "didnt","couldnt","wouldnt","shouldnt","isnt","arent","youre","theyre","weve",
 "youve","hasnt","havent","doesnt","hed","shes","hes","lets","mustnt","wheres",
 "heres","theres","yall","hadnt","aint","hell"]

def strip_tags(s): return TAG_RE.sub("", s)
def ctx(txt, m, w=38):
    a = max(0, m.start()-w); b = min(len(txt), m.end()+w)
    return ("..." if a>0 else "") + txt[a:b].replace("\n"," ") + ("..." if b<len(txt) else "")

out = open(os.path.join(BASE, "QA", "lint_pass2.txt"), "w", encoding="utf-8")
def P(*a): out.write(" ".join(str(x) for x in a) + "\n")

for fname in FILES:
    raw = open(os.path.join(CHDIR, fname), encoding="utf-8").read().split("\n")
    P("="*90); P("FILE:", fname); P("="*90)

    # ---- contractions with context ----
    P("--- CONTRACTIONS (word, line, context) ---")
    for i, rline in enumerate(raw, 1):
        t = strip_tags(rline)
        for w in CONTRACTIONS:
            for m in re.finditer(r"\b%s\b" % w, t, re.IGNORECASE):
                P("L%-4d %-8s %s" % (i, m.group(0), ctx(t, m)))
    # lowercase i'll/i've/i'd/i'm
    for i, rline in enumerate(raw, 1):
        t = strip_tags(rline)
        for m in re.finditer(r"\bi['\u2019](?:ll|ve|d|m)\b", t):
            P("L%-4d i-apos   %s" % (i, ctx(t, m)))

    # ---- standalone lowercase i ----
    P("--- LOWERCASE STANDALONE i ---")
    for i, rline in enumerate(raw, 1):
        t = strip_tags(rline)
        for m in re.finditer(r"\bi\b", t):
            P("L%-4d %s" % (i, ctx(t, m)))

    # ---- hum variants with context ----
    P("--- HUM VARIANTS ---")
    for i, rline in enumerate(raw, 1):
        t = strip_tags(rline)
        for m in re.finditer(r"\b[Hh]u+m+ans?\b", t):
            P("L%-4d %-9s %s" % (i, m.group(0), ctx(t, m)))

    # ---- cross-line double-quote state ----
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
            open_line = None; inside = False  # resync after blank line
    if inside: problems.append("UNBALANCED: still open at EOF (opened L%s)" % open_line)
    if not problems: P("OK: all double quotes balanced within line groups")
    for p in problems: P("CHECK:", p)

    # ---- single-quote classification ----
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
            else: O += 1  # isolated quote, treat as open
        if O or C:
            if O != C:
                P("L%-4d O=%d C=%d M=%d  %s" % (i, O, C, M, t.strip()[:150]))

    # ---- lowercase race/proper names ----
    P("--- LOWERCASE PROPER-NOUN TOKENS ---")
    names = ["wengari","veylar","veylara","pyrina","pyrinae","styx","threx","lightbringer",
             "chi'thak","humman","humans","human","bright paw","shadow paw","stripe paw",
             "motted paw","white dawn","black fire","kyre tree","bright paws","shadow paws",
             "stripe paws","motted paws"]
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

    # ---- typo sweep ----
    P("--- TYPO SWEEP ---")
    typos = [("handt", r"\bhandt\b"), ("appropiate", r"\bappropiate\b"),
             ("assasins", r"\bassasins?\b"), ("dessert", r"\bdessert\b"),
             ("three thousands", r"\bthree thousands\b"), ("kyrie", r"\bkyrie\b"),
             ("t'vat", r"\bt'vat\b", re.I), ("my father son", r"\bmy father son\b"),
             ("Raise and eyebrow", r"Raise and eyebrow"), ("stripes paw", r"\bstripes paw\b", re.I),
             ("hell (he'll)", r"\bhell\b"), ("styx plumage", None)]
    for entry in typos:
        label, pat = entry[0], entry[1]
        flags = entry[2] if len(entry) > 2 else 0
        if pat is None: continue
        for i, rline in enumerate(raw, 1):
            t = strip_tags(rline)
            for m in re.finditer(pat, t, flags):
                P("L%-4d %-18s %s" % (i, label, ctx(t, m)))

    # ---- King contexts ----
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

    # ---- meta markers ----
    P("--- META / SCAFFOLD MARKERS ---")
    markers = [r"^\s*Let me\b", r"^Here is the\b", r"^Yes\.\s", r"\bIt also fits the\b",
               r"\bshould be grounded\b", r"\bThe Montage\b", r"\bMontage, Corrected\b",
               r"\bOutside the Chamber\b", r"\bOne Month After the Council\b",
               r"\bThe Bright Paw Capital\b", r"\bperfectly calibrated\b",
               r"\bI'll take the seed\b", r"\bThe Tree is not a mentor\b",
               r"\bCorrected exchange\b"]
    for i, rline in enumerate(raw, 1):
        t = strip_tags(rline)
        for mk in markers:
            if re.search(mk, t, re.I):
                P("L%-4d [%s] %s" % (i, mk.replace("\\b",""), t.strip()[:120]))
                break
    P()

# full text of key lines for the report
P("="*90); P("KEY LINES FULL TEXT"); P("="*90)
keys = [("chapter-arc1-01.md",[4,26,37,74,114]), ("chapter-arc1-06.md",[16]),
        ("chapter-arc2-01.md",[6,54,97,120,192,234]), ("chapter-arc2-04.md",[26,188])]
for fname, lines in keys:
    raw = open(os.path.join(CHDIR, fname), encoding="utf-8").read().split("\n")
    for ln in lines:
        P("%s L%d:" % (fname, ln)); P("   " + strip_tags(raw[ln-1]).strip()); P()

out.close()
print("done")
