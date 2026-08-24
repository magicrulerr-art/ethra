import re

with open('C:/Users/magic_new.BETOS-AIO.000/.qwenpaw/workspaces/default/ethra_site/content/story/chapters/chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Check for remaining debris markers
patterns = ['DRAFT', 'DIRECTIVE', 'SYNOPSIS', 'CRAFT-BLOCK', 'SCAFFOLD-BLOCK', 'PLANNING-BLOCK', 'DUP-', 'CORRECTIONS-', 'Humman', 'King']
for pattern in patterns:
    matches = list(re.finditer(pattern, content, re.IGNORECASE))
    if matches:
        print(f'Found {len(matches)} occurrences of "{pattern}":')
        for m in matches[:5]:
            line_num = content[:m.start()].count('\n') + 1
            context = content[max(0,m.start()-40):m.end()+40].replace('\n', ' ')
            print(f'  Line ~{line_num}: ...{context}...')
    else:
        print(f'NOT FOUND: "{pattern}"')

# Check for asterisk thoughts (J3)
print("\n--- Asterisk thoughts (J3) ---")
asterisk_matches = list(re.finditer(r'^\s*\*[^*]+\*\s*$', content, re.MULTILINE))
for m in asterisk_matches[:20]:
    line_num = content[:m.start()].count('\n') + 1
    print(f'  Line {line_num}: {m.group()[:100]}')
print(f'Total asterisk thoughts: {len(asterisk_matches)}')

# Check for bare asterisk lines
print("\n--- Bare asterisk lines ---")
bare_asterisk = list(re.finditer(r'^\s*\*.+\*\s*$', content, re.MULTILINE))
for m in bare_asterisk[:20]:
    line_num = content[:m.start()].count('\n') + 1
    print(f'  Line {line_num}: {m.group()[:100]}')
print(f'Total bare asterisk lines: {len(bare_asterisk)}')