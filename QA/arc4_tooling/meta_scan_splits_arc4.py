# -*- coding: utf-8 -*-
"""Arc IV split-file author-voice/meta scan — broad marker net. Read-only."""
import re, os, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(os.path.dirname(TOOL_DIR))
CH = os.path.join(BASE, "content", "story", "chapters") + os.sep
files = ["chapter-arc4-%02d.md" % c for c in range(1, 7)]
TAG = re.compile(r"<[^>]+>")
markers = [
    (r"\blet'?s continue\b", "lets-continue"),
    (r"\bare we ready to\b", "are-we-ready"),
    (r"\bcontinue the\b", "continue-the"),
    (r"\bwalking exposition\b", "walking-exposition"),
    (r"\baudience surrogate\b", "audience-surrogate"),
    (r"\bstoryteller'?s kit\b", "storytellers-kit"),
    (r"\byou designed\b", "you-designed"),
    (r"\byou deployed\b", "you-deployed"),
    (r"\bwe'?ve built\b", "weve-built"),
    (r"\bI need to either\b", "i-need-to-either"),
    (r"\bretroactively\b", "retroactively"),
    (r"\bI should have noticed\b", "i-should-have-noticed"),
    (r"\bfill a crucial gap\b", "fill-crucial-gap"),
    (r"\bemotional engine\b", "emotional-engine"),
    (r"\bperforming competence\b", "performing-competence"),
    (r"\bvignettes?\b", "vignette"),
    (r"\bcraft\b", "craft-word"),
    (r"\bLet me\b", "let-me"),
    (r"\bHere is the\b", "here-is-the"),
    (r"\bCorrected\b", "corrected"),
    (r"\bMontage\b", "montage"),
    (r"\bVersion [AB]\b", "version-ab"),
    (r"\bpass ?[123]\b", "pass-n"),
    (r"\bscaffold\b", "scaffold"),
    (r"\bworldbuilding\b", "worldbuilding"),
    (r"\bbackstory\b", "backstory"),
    (r"\bnarrative(?:ly)?\b", "narrative-word"),
    (r"\bcharacteriz\w+", "characterize"),
    (r"\bsymbolic gesture\b", "symbolic-gesture"),
    (r"\beco(?:system|logy)\b", "ecosystem"),
    (r"\bfood web\b", "food-web"),
    (r"\bterrestrial apex\b", "terrestrial-apex"),
    (r"\bwe feel because\b", "we-feel-because"),
    (r"\boldest and most effective trick\b", "oldest-trick"),
    (r"\bgrimoire\b", "grimoire"),
]
for f in files:
    lines = open(CH + f, encoding="utf-8").read().split("\n")
    hits = []
    for ln, l in enumerate(lines, 1):
        t = TAG.sub("", l)
        if not t.strip():
            continue
        for rx, label in markers:
            if re.search(rx, t, re.I):
                hits.append((ln, label, t.strip()))
                break
    print("=" * 80); print(f, "hits:", len(hits))
    for ln, label, t in hits:
        print("  L%-4d [%s] %s" % (ln, label, t[:170]))
