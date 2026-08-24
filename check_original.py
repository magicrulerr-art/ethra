with open('C:/temp/arc6-01_original.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(f'Total lines: {len(lines)}')
for ln in [123, 197, 313, 439, 443, 485, 810, 905, 963, 1042]:
    if ln <= len(lines):
        print(f'Line {ln}: {lines[ln-1].rstrip()[:120]}')
    else:
        print(f'Line {ln}: OUT OF RANGE')