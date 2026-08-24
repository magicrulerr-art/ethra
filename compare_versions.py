with open('C:/temp/arc6-01_current.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(f'Current (HEAD) lines: {len(lines)}')

with open('C:/temp/arc6-01_original.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(f'Baseline (ebbd6a8) lines: {len(lines)}')