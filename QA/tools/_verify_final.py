import re

def full_div_balance(path):
    t = open(path, encoding='utf-8').read()
    lines = t.splitlines()
    depth = 0
    unclosed = []
    stray_closes = []
    
    for i, ln in enumerate(lines, 1):
        opens = len(re.findall(r'<div[^>]*>', ln))
        closes = ln.count('</div>')
        if opens:
            if depth == 0:
                unclosed.append((i, opens))
            depth += opens
        if closes:
            depth -= closes
            if depth < 0:
                stray_closes.append(i)
                depth = 0
    
    return unclosed, stray_closes, depth

print("=== MASTER CHAPTERS DIV BALANCE ===")
for f in ['content/story/chapter-04.md', 'content/story/chapter-05.md', 
          'content/story/chapter-06.md']:
    try:
        unc, sc, term = full_div_balance(f)
        if unc or sc or term:
            print(f"\n{f}: term_depth={term}")
            print(f"  unclosed opens: {unc[:5]}")
            print(f"  stray closes: {sc[:5]}")
        else:
            print(f"{f}: BALANCED")
    except FileNotFoundError:
        print(f"{f}: NOT FOUND")

print("\n=== ALL SPLITS DIV BALANCE ===")
import glob
for f in sorted(glob.glob('content/story/chapters/chapter-arc*.md')):
    try:
        unc, sc, term = full_div_balance(f)
        if unc or sc or term != 0:
            name = f.split('\\')[-1]
            print(f"  {name}: term_depth={term}, unclosed={unc[:3]}, stray_closes={sc[:3]}")
    except:
        pass

print("\n=== ARC6-02 DICTATION FRAGMENT CHECK ===")
try:
    t = open('content/story/chapters/chapter-arc6-02.md', encoding='utf-8').read()
    for pat in ['Ajani says his voice booming', 'says his voice booming', 'dictation', 'scene description', 'blockquote']:
        idx = t.find(pat)
        if idx >= 0:
            snippet = t[max(0,idx-50):idx+len(pat)+50]
            print(f"  FOUND '{pat}' at offset {idx}: ...{snippet}...")
except Exception as e:
    print(f"  Error: {e}")

print("\n=== MIRA MENTIONS IN ARC6-04 AND ARC6-05 ===")
for f in ['content/story/chapters/chapter-arc6-04.md', 'content/story/chapters/chapter-arc6-05.md']:
    try:
        t = open(f, encoding='utf-8').read()
        lines = t.splitlines()
        for i, ln in enumerate(lines, 1):
            if 'Mira' in ln:
                print(f"  {f.split(chr(92))[-1]}:{i}: ...{ln.strip()[:80]}...")
    except:
        pass
