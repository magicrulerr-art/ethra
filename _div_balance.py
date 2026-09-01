import io, glob, re, sys

files = sorted(glob.glob('content/story/chapters/*.md'))
bad = []
for f in files:
    t = io.open(f, encoding='utf-8').read()
    opens = len(re.findall(r'<div\b', t))
    closes = len(re.findall(r'</div>', t))
    if opens != closes:
        bad.append((f, opens, closes))
print(f'checked {len(files)} splits')
if bad:
    for f, o, c in bad:
        print(f'IMBALANCE {f}: {o} opens / {c} closes (delta {o-c})')
    sys.exit(1)
print('DIV-BALANCE OK: all splits balanced')
