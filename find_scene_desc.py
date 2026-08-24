with open(r'content\story\chapters\chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the long asterisk scene description
idx = content.find('*The next scene is a couple of hours after ajani')
if idx >= 0:
    line_num = content[:idx].count('\n') + 1
    print(f'Found at line {line_num}')
    # Show surrounding lines
    lines = content.split('\n')
    for i in range(max(0, line_num-5), min(len(lines), line_num+5)):
        print(f'{i+1}: {lines[i]}')
else:
    print('NOT FOUND')