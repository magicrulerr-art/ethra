import re
p=r'C:\Users\magic\.copaw\workspaces\default\ethra_site\content\story\chapter-05.md'
d=open(p,encoding='utf-8').read()
pat=re.compile(r'\b(?:[1-9]|1[0-2])\s*[:.]?\s*[0-5][0-9]\s*(?:am|pm|AM|PM|in the morning|in the afternoon)\b|^It was \d',re.M)
hits=[]
for i,line in enumerate(d.split('\n')):
    s=line.strip()
    if pat.search(s):
        hits.append((i+1,s[:160]))
print('Total timestamp-ish lines:', len(hits))
for ln,s in hits:
    if s.startswith('It was '):
        print(f'  L{ln:>5}: {s[:80]}')
print('--- AM/PM hits ---')
for ln,s in hits:
    if 'AM' in s or 'PM' in s:
        print(f'  L{ln:>5}: {s[:80]}')
