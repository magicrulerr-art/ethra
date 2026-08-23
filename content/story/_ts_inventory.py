import re
p=r'C:\Users\magic\.copaw\workspaces\default\ethra_site\content\story\chapter-05.md'
d=open(p,encoding='utf-8').read()
lines=d.split('\n')
# Find It-was-X-morning/and..., and identify the immediate preceding 80 chars
pat=re.compile(r'^It was (\d+:\d+)')
beats=[]
buf=[]
prev=''
for i,line in enumerate(lines):
    if pat.search(line.strip()):
        ts=pat.match(line.strip()).group(1)
        beats.append((i+1, ts, prev.strip()[-120:] if prev else '', line.strip()[:120]))
    prev=line
print('Beat inventory (timestamp anchor):')
for ln,ts,leading,ltxt in beats:
    print()
    print(f'  L{ln:>5} [{ts:>5}]')
    print(f'    PREV: {leading}')
    print(f'    LINE: {ltxt}')
