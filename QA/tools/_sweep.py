import glob, re

print("=== DICTATION FRAGMENT ('voice booming') ===")
for f in sorted(glob.glob('content/story/chapter-0*.md') + glob.glob('content/story/chapters/chapter-arc*.md')):
    t = open(f, encoding='utf-8').read()
    for pat in ['says his voice booming', 'voice booming', 'turns his cape billowing and enters']:
        if pat in t:
            for i, ln in enumerate(t.splitlines(), 1):
                if pat in ln:
                    print(f"  {f}:{i} [{pat}]")

print("\n=== KIRA / GRANDDAUGHTER SWEEP ===")
for f in sorted(glob.glob('content/story/chapter-0*.md') + glob.glob('content/story/chapters/chapter-arc*.md')):
    t = open(f, encoding='utf-8').read()
    for i, ln in enumerate(t.splitlines(), 1):
        if re.search(r'granddaughter|grand-daughter|is my grand|named Kira|golden Bright Paw|her name is Kira', ln, re.I):
            print(f"  {f}:{i}: {ln.strip()[:90]}")

print("\n=== DONE ===")
