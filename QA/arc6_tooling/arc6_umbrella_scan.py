#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arc VI — umbrella chapter-06.md draft-debris scan. Grep-style, read-only.
Outputs line numbers + context for: meta markers, Version A/B, Corrected,
Montage, pass1/pass2, scene-heading inventory (for duplicate heading detection),
author planning prose patterns, and a heading-level structure dump.
"""
import re, io, sys, os, collections
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(os.path.dirname(TOOL_DIR))
UMB = os.path.join(BASE, "content", "story", "chapter-06.md")
out = open(os.path.join(TOOL_DIR, "arc6_umbrella_debris.txt"), "w", encoding="utf-8")
def p(*a):
    print(*a); out.write(" ".join(str(x) for x in a) + "\n")

lines = open(UMB, encoding="utf-8").read().split("\n")
p("UMBRELLA: %s" % UMB)
p("TOTAL LINES: %d" % len(lines))

MARKERS = [
    ("META-rewrite", r"\b[Ll]et me (rewrite|try|rework|redo|adjust)\b"),
    ("META-here-is", r"^[*\s]*Here (?:is|are) the\b"),
    ("META-correction", r"\b[Hh]ere is the correction\b|\bcorrection:\b"),
    ("META-corrected", r"\bCorrected\b"),
    ("META-versionAB", r"\bVersion [AB]\b|\bVariant [AB]\b"),
    ("META-montage", r"\bMontage\b"),
    ("META-pass", r"\bpass\s?[12]\b|\bPass [12]\b"),
    ("META-note", r"\bNote to self\b|\bI need to\b|\bI'll (try|rewrite|redo)\b|\bLet's try\b"),
    ("META-alt", r"\bAlternative (version|take|draft)\b|\bAlt version\b"),
    ("META-option", r"\bOption [AB12]\b"),
    ("META-draft", r"\bfirst draft\b|\brough draft\b|\bplaceholder\b|\bTBD\b|\bTODO\b"),
    ("META-craft-note", r"\b(craft note|craft-wise|tonally|pacing-wise)\b"),
    ("META-numbered-note", r"^\s*\d+\.\s+(Rewrite|Note|Fix|Change|Add)\b"),
    ("META-scaffold-bold", r"^\s*\*\*[^*]{0,60}(Corrected|Montage|Version|Scene \d|Take \d)[^*]{0,60}\*\*"),
]
hits = collections.defaultdict(list)
for i, l in enumerate(lines, 1):
    for label, pat in MARKERS:
        if re.search(pat, l):
            hits[label].append((i, l.strip()[:150]))
for label, _ in MARKERS:
    hs = hits.get(label, [])
    p("\n### %s: %d hits" % (label, len(hs)))
    for ln, t in hs[:80]:
        p("  L%-5d %s" % (ln, t))
    if len(hs) > 80:
        p("  ... +%d more (see JSON)" % (len(hs) - 80))

import json
with open(os.path.join(TOOL_DIR, "arc6_umbrella_debris.json"), "w", encoding="utf-8") as fh:
    json.dump({k: v for k, v in hits.items()}, fh, indent=1, ensure_ascii=False)

# heading inventory (duplicate detection)
p("\n### HEADING INVENTORY (lines starting with # or '**') ###")
headings = collections.defaultdict(list)
for i, l in enumerate(lines, 1):
    s = l.strip()
    if s.startswith("#") or (s.startswith("**") and s.endswith("**") and len(s) < 120):
        headings[re.sub(r"\s+", " ", s.lower())].append(i)
for h, ls in sorted(headings.items()):
    dup = "  <<DUPLICATE x%d>>" % len(ls) if len(ls) > 1 else ""
    p("  L%s :: %s%s" % (",".join(map(str, ls)), h[:100], dup))

# chapter split markers inside umbrella
p("\n### CHAPTER SPLIT MARKERS (Chapter N headings) ###")
for i, l in enumerate(lines, 1):
    if re.search(r"^#+\s*Chapter\s", l.strip()) or re.search(r"^\*\*Chapter\s", l.strip()):
        p("  L%-5d %s" % (i, l.strip()[:100]))
out.close()
print("written: arc6_umbrella_debris.txt")
