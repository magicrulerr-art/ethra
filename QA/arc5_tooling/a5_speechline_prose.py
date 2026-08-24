# -*- coding: utf-8 -*-
"""Find <p class="speech-line"> paragraphs containing ZERO double quotes
(narrative prose wrongly wrapped in dialogue markup). Read-only."""
import io, os, re, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CH = os.path.join(BASE, "content", "story", "chapters")
files = ["chapter-arc5-%02d.md" % c for c in range(1, 23)]
for f in files:
    lines = open(os.path.join(CH, f), encoding="utf-8").read().split("\n")
    for i, l in enumerate(lines, 1):
        if '<p class="speech-line">' in l and '"' not in l.replace('<p class="speech-line">', ""):
            t = re.sub(r"<[^>]+>", "", l).strip()
            print("%s L%d: %s" % (f, i, t[:150]))
