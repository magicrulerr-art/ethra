with open(r'content\story\chapters\chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix M2: King -> king (except in Ice King, Shadow King etc.)
# The occurrence is "King of the Wengari" - should become "king of the Wengari"
content = content.replace('King of the Wengari', 'king of the Wengari')

# Verify
import re
king_count = len(list(re.finditer(r'\bKing\b', content)))
print('Remaining King count:', king_count)

with open(r'content\story\chapters\chapter-arc6-01.md', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed.')