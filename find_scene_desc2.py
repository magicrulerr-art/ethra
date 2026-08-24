with open(r'content\story\chapters\chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Find "next scene" 
idx = content.find('next scene')
if idx >= 0:
    line_num = content[:idx].count('\n') + 1
    print(f'Found "next scene" at line {line_num}')
    lines = content.split('\n')
    for i in range(max(0, line_num-5), min(len(lines), line_num+5)):
        print(f'{i+1}: {lines[i]}')
else:
    print('NOT FOUND')

# Also search for "healers still checking"
idx2 = content.find('healers still checking')
if idx2 >= 0:
    line_num2 = content[:idx2].count('\n') + 1
    print(f'\nFound "healers still checking" at line {line_num2}')
    lines = content.split('\n')
    for i in range(max(0, line_num2-5), min(len(lines), line_num2+5)):
        print(f'{i+1}: {lines[i]}')
else:
    print('\n"healers still checking" NOT FOUND')