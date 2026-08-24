import re

with open('C:/Users/magic_new.BETOS-AIO.000/.qwenpaw/workspaces/default/ethra_site/content/story/chapter-06.md', 'r', encoding='utf-8') as f:
    content = f.read()

patterns = ['DRAFT', 'DIRECTIVE', 'SYNOPSIS', 'CRAFT-BLOCK', 'SCAFFOLD-BLOCK', 'PLANNING-BLOCK', 'DUP-', 'CORRECTIONS-']
for pattern in patterns:
    matches = list(re.finditer(pattern, content, re.IGNORECASE))
    if matches:
        for m in matches[:3]:
            line_num = content[:m.start()].count('\n') + 1
            context = content[max(0,m.start()-50):m.end()+50].replace('\n', ' ')
            print(f'Found "{pattern}" at line ~{line_num}: ...{context}...')
    else:
        print(f'NOT FOUND in chapter-06: "{pattern}"')