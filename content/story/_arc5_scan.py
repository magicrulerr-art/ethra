"""Comprehensive meta-fragment inventory across Arc 5 umbrella + all 4 slices.
Goal: produce an exhaustive categorized list of contamination, line-numbered, with context, so Pass-2 can be surgical.
"""
import re, os
from io import open as iopen

ROOT = r"C:\Users\magic\.copaw\workspaces\default\ethra_site\content\story"
files = ['chapter-05.md',
         'chapters/chapter-arc5-01.md',
         'chapters/chapter-arc5-02.md',
         'chapters/chapter-arc5-03.md',
         'chapters/chapter-arc5-04.md']

META_HEADERS = re.compile(r'^\*\*(Pacing|Strategy|Lore Reveals|Emotional Core|A Few Observations|Tone|Themes|Author Note|Author note|Background Note|Notes On|Notes on|Final Beat|This single|This is the classic|This is the|This validates|This serves|The lore reveals|The pacing|The strategy|The emotional|The cost|The Humman|The Wengari|The next Humman|The common|The battle|The shield|The lights|The first|One observation|One note|One thought)\*\*', re.M)

# Author-commentary patterns (philosophical, present-tense evaluative statements)
META_PHRASES = [
    r'\bthis is the correct\b', r'\bthis is properly\b', r'\bthis is felt\b',
    r'\bthis single (turn|beat|moment)\b', r'\bthis is because\b', r'\bthis validates\b',
    r'\bthis serves\b', r'\bthis is felt\b', r'\bthis is significant\b', r'\bthis is the cost\b',
    r'\bthis is tragedy\b', r'\bis tragedy\b', r'\bthis is unfair\b',
    r'\bthis is what war costs\b', r'\bthis is what\b',
    r'\bThis kind of (small|tender|quiet)\b', r'\bThe (small|tender)\b',
    r'\bthese moments ground\b', r'\bthis single motion\b',
    r'\bThe reader (is|has|knows|will|feels)\b',
    r'\bThe deflation\b', r'\bthe timing is correct\b',
    r'\bclassic tension-release\b', r'\btension-release structure\b',
    r'\bproperly delayed\b', r'\bproperly devastating\b',
    r'\bbecause it has been\b',
    r'\bnot merely casualties\b',
    r'\bThe lore reveals are working\b', r'\bThe lore reveals have been\b',
    r'\bThe pacing of the (\w+ )?(scene|death|moment|cut|chapter)\b',
    r'\bThe pacing is\b', r'\bThe pacing\b',
    r'\banchored to a character\b',
    r'\bdrama that is (logical|earned|fair)\b',
    r'\blogical consequence\b', r'\bfelt consequence\b',
    r'\bBoth things can be true\b',
    r'\bThis is exactly that\b',
    r'\bThe works well\b',
    r"\bLet's start\b(?!\sthe battle)",
    r'\bHere is the next pov\b', r'\bnext pov\b',
    r'^\s*For the next pov\b', r'\bwe switch to (mekhmed|Mekhmed|the young|the humman|the wengari|the tent|the healers|the generals|the priests|the ritualists|the people|the cultists|M\'rak|Reva|Yvaria|Zephyr)\b',
    r'\bGood,?\s*I (like|love|want)\b',
    r'\bWe jump to\b', r'\bfor the next pov\b', r'\bswitch to mekhmet\b', r'\bwe cut to\b', r'\bwe see\b',
    r"\bI like it\b", r"\bwe are in the\b", r"\bLet.s go back to\b",
]

for path in files:
    fp = os.path.join(ROOT, path)
    if not os.path.exists(fp):
        continue
    d = iopen(fp, encoding='utf-8').read()
    lines = d.split('\n')
    print()
    print('#'*78)
    print(f'### {path}  ({len(d)} b, {len(lines)} lines)')
    print('#'*78)

    # Headers
    headers = []
    for i,line in enumerate(lines):
        if META_HEADERS.match(line.strip()):
            headers.append((i+1, line.strip()))
    if headers:
        print(f'  META-HEADERS ({len(headers)}):')
        for ln,t in headers:
            print(f'    L{ln:>5}: {t}')

    # Phrase matches
    seen_lines = set()
    phrase_hits = []
    for i,line in enumerate(lines):
        if (i+1) in seen_lines: continue
        for pat in META_PHRASES:
            if re.search(pat, line, re.IGNORECASE):
                phrase_hits.append((i+1, line.strip()[:160]))
                seen_lines.add(i+1)
                break
    if phrase_hits:
        print(f'  META-PHRASES ({len(phrase_hits)}):')
        for ln,t in phrase_hits:
            print(f'    L{ln:>5}: {t}')
    if not headers and not phrase_hits:
        print('  CLEAN')
