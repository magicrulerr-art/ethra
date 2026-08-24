with open(r'content\story\chapters\chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    content = f.read()
print('Current Humman count:', content.count('Humman'))
print('Current Human count:', content.count('Human'))
print('Current King count:', content.count('King'))
print('Current king count:', content.count('king'))

# Check for asterisk debris
import re
lines = content.split('\n')
for i, line in enumerate(lines, 1):
    if line.lstrip().startswith('*') and not line.lstrip().startswith('**'):
        print(f'  Line {i}: {line.rstrip()[:100]}')