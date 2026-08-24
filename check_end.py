with open(r'content\story\chapters\chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    content = f.read()

print(f'Total length: {len(content)}')
print(f'Total lines: {content.count(chr(10))}')
# Show last 50 lines
lines = content.split('\n')
for i, line in enumerate(lines[-50:], len(lines)-49):
    print(f'{i}: {line}')