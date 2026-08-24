with open('C:/Users/magic_new.BETOS-AIO.000/.qwenpaw/workspaces/default/ethra_site/content/story/chapters/chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped.startswith('*') and not stripped.startswith('**'):
        print(f'Line {i+1}: {line.rstrip()}')