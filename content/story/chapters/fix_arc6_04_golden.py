#!/usr/bin/env python3
"""
Convert multiline asterisk blocks in Arc6-04 to single quotes.
Block 1: lines 526-528 (Ajani memory - Serpent's Fang)
Block 2: line 534 (Lira - Shadow Paw)
"""

file_path = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-04.md"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Block 1: lines 526-528 (1-based) -> indices 525-527
# Block starts with *"Most people think..." and ends with ...right—"* 
# Actually line 528 ends with *"It bites. This is my fifth form... save you."*
# So block is lines 526-528

start1, end1 = 525, 527
block1_lines = [lines[i].rstrip('\n') for i in range(start1, end1 + 1)]
# Remove leading * from first, trailing * from last
block1_lines[0] = block1_lines[0][1:] if block1_lines[0].startswith('*') else block1_lines[0]
block1_lines[-1] = block1_lines[-1][:-1] if block1_lines[-1].endswith('*') else block1_lines[-1]
joined1 = ' '.join(block1_lines)
new1 = f"'{joined1}'\n"

print("Block 1 (Ajani memory):")
for i in range(start1, end1 + 1):
    print(f"  L{i+1}: {lines[i].rstrip()[:100]}")
print(f"  -> '{joined1[:100]}...'")

# Block 2: line 534 (1-based) -> index 533
# Starts with '"You are a Shadow Paw."* and ends with ...Remember that."'
start2, end2 = 533, 533
block2 = lines[start2].rstrip('\n')
if block2.startswith('*') and block2.endswith('*'):
    block2 = block2[1:-1]
elif block2.startswith('*"') and block2.endswith('."'):
    # Pattern: *"text."
    block2 = block2[2:-2]  # Remove *" and ."
    # Actually let's just strip * from both ends
    block2 = block2.strip('*')
elif block2.startswith('*"') and block2.endswith('."*'):
    block2 = block2[2:-3]

leading = lines[start2][:len(lines[start2]) - len(lines[start2].lstrip())]
trailing = lines[start2][len(lines[start2].rstrip()):]
new2 = leading + f"'{block2}'" + trailing + '\n'

print(f"\nBlock 2 (Lira):")
print(f"  L{start2+1}: {lines[start2].rstrip()[:100]}")
print(f"  -> '{block2[:100]}...'")

# Replace blocks
# Delete block 1 lines
del lines[start1:end1+1]
# Block 2 index shifts by (end1 - start1 + 1) = 3
new_start2 = start2 - 3
lines.insert(start1, new1)
lines[new_start2] = new2

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"\nDone. File now has {len(lines)} lines.")