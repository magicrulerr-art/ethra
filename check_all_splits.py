for fname in ['chapter-arc6-01.md', 'chapter-arc6-02.md', 'chapter-arc6-03.md', 'chapter-arc6-04.md', 'chapter-arc6-05.md']:
    with open(f'content\\story\\chapters\\{fname}', 'r', encoding='utf-8') as f:
        content = f.read()
    print(f'{fname}:')
    print(f'  Humman: {content.count("Humman")}, Human: {content.count("Human")}')
    print(f'  King: {content.count("King")}, king: {content.count("king")}')
    # Check asterisk debris
    import re
    lines = content.split('\n')
    asterisk_lines = []
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith('*') and not line.lstrip().startswith('**'):
            asterisk_lines.append((i, line.rstrip()[:80]))
    if asterisk_lines:
        print(f'  Asterisk debris: {len(asterisk_lines)} lines')
        for ln, txt in asterisk_lines:
            print(f'    Line {ln}: {txt}')
    else:
        print(f'  Asterisk debris: none')
    print()