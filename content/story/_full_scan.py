p=r'C:\Users\magic\.copaw\workspaces\default\ethra_site\content\story\chapter-05.md'
d=open(p,encoding='utf-8').read()
lines=d.split('\n')
print('Total lines:',len(lines))
# Test PASS4 grep pattern from MEMORY.md
banned = [
    'Will retire', 'Kira..s arc is the emotional backbone', 'dream optimization',
    'collaborative process', 'Let me verify my context', 'can you quantify',
    'Begin chapter', 'planning essay', 'hypergraph', 'A Few Observations',
    'Emotional Core', 'Lore Reveals', 'Strategic',
    'This is the correct', 'battle logic holds',
    'correct dramatic structure', 'anchored to a character',
    'The next Humman scene', 'The lore reveals are working',
    "Let's start the next scene",
    'I will retire']
print()
print('--- PASS4 full-scan ---')
for b in banned:
    c = d.count(b)
    if c > 0:
        print(f'  X  Has "{b}": {c}')
print('--- DONE ---')
