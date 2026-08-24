with open(r'content\story\chapters\chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    content = f.read()

# M1: Humman -> Human (case-sensitive, 52 occurrences total across all splits)
# M2: King -> king (but not in "Ice King", "Shadow King" etc.) - arc6-01 has 0 King already
# M3: arc6-01 L641 -> add missing closing quote on speech line (need to check)
# M4: debris -> wreckage (in 350-400 line band, verify each)

# Apply M1: Humman -> Human
import re
# Count before
humman_before = content.count('Humman')
content = content.replace('Humman', 'Human')
humman_after = content.count('Humman')
print('M1: Humman -> Human: {} -> {} (changed {})'.format(humman_before, humman_after, humman_before - humman_after))

# M2: King -> king (not in proper names)
# Check for "King" occurrences
king_matches = list(re.finditer(r'\bKing\b', content))
print('M2: Found {} "King" occurrences:'.format(len(king_matches)))
for m in king_matches:
    start = max(0, m.start()-30)
    end = min(len(content), m.end()+30)
    line_num = content[:m.start()].count('\n')+1
    print('  Line {}: ...{}...'.format(line_num, content[start:end]))

# M3: Check line 641 area for missing closing quote
lines = content.split('\n')
if len(lines) >= 641:
    print('\nM3: Line 641 area:')
    for i in range(635, min(650, len(lines))):
        print('  {}: {}'.format(i+1, lines[i]))

# M4: Check debris -> wreckage in 350-400 line band
print('\nM4: "debris" in lines 350-400:')
for i in range(349, min(400, len(lines))):
    if 'debris' in lines[i].lower():
        print('  {}: {}'.format(i+1, lines[i].rstrip()))

# Write back
with open(r'content\story\chapters\chapter-arc6-01.md', 'w', encoding='utf-8') as f:
    f.write(content)

print('\nDone.')