"""Deep scan for residual meta-comment contamination patterns in umbrella + all Arc 5 slices."""
import re, io, os

ROOT = r"C:\Users\magic\.copaw\workspaces\default\ethra_site\content\story"
targets = [
    'chapter-05.md',
    'chapters/chapter-arc5-01.md',
    'chapters/chapter-arc5-02.md',
    'chapters/chapter-arc5-03.md',
    'chapters/chapter-arc5-04.md',
]

# Wider banned patterns - including user-quoted example
banned_patterns = [
    "**Pacing**", "**Strategy**", "**Lore Reveals**", "**Emotional Core**",
    "**A Few Observations**", "**Notes on**", "**Themes**", "**Tone**",
    "**Final Beat**",
    "battle logic holds", "correct dramatic structure", "anchored to a character",
    "classic tension-release structure", "the timing is correct", "this single",
    "the reader has been waiting", "this validates his strategy", "this serves the battle",
    "this is the correct", "this is the kind", "this is felt", "this single beat",
    "the pacing", "the strategy", "the lore reveals",
    "These moments ground", "these are the consequences", "this will be tested",
    "this is significant", "this is the cost", "this is tragedy", "is tragedy",
    "this is something", "this is true", "both things can be true",
    "I will retire", "dream optimization", "Let me verify my context",
    "can you quantify", "Begin chapter",
    "Let's start", "planning essay", "Let's keep going", "we should",
    "this is happening", "I think the", "I think we",
    "this is", "works because", "this works",
]

for path in targets:
    fp = os.path.join(ROOT, path)
    if not os.path.exists(fp):
        continue
    d = open(fp, encoding='utf-8').read()
    hits = []
    for pat in banned_patterns:
        if pat.lower() in d.lower():
            # Find context line numbers
            lc = 0
            for line in d.split('\n'):
                if pat.lower() in line.lower():
                    hits.append((pat, lc+1, line.strip()[:120]))
                lc += 1
    if not hits:
        print(f"CLEAN  {path}  ({len(d)} b)")
    else:
        print(f"DIRTY  {path}  ({len(d)} b):")
        seen=set()
        for pat,line,txt in hits:
            if txt in seen: continue
            seen.add(txt)
            print(f"   L{line:>5}: [{pat}] {txt}")
