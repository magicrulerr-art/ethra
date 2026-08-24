with open(r'content\story\chapters\chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

target_lines = [123, 197, 313, 439, 443, 485, 810, 905, 963, 1042]
for ln in target_lines:
    if ln <= len(lines):
        print(f'{ln}: {repr(lines[ln-1])}')
    else:
        print(f'{ln}: (beyond file length {len(lines)})')