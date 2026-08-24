with open(r'content\story\chapters\chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the "King" occurrence
import re
matches = list(re.finditer(r'\bKing\b', content))
for m in matches:
    start = max(0, m.start()-50)
    end = min(len(content), m.end()+50)
    line_num = content[:m.start()].count('\n')+1
    print('Line {}: ...{}...'.format(line_num, content[start:end]))