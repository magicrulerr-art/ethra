#!/usr/bin/env python3
"""
Properly convert multiline asterisk blocks in Arc6-04 to single quotes.
Remove ALL asterisk delimiters from thought blocks.
"""

import re

file_path = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-04.md"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.splitlines(keepends=True)

# Step 1: Remove debris lines (146, 315, 1101)
debris_1based = [146, 315, 1101]
debris_0based = sorted([l - 1 for l in debris_1based], reverse=True)
for idx in debris_0based:
    if idx < len(lines):
        print(f"Removing debris line {idx+1}: {lines[idx].strip()[:80]}")
        del lines[idx]

content = ''.join(lines)

# Step 2: Convert multiline asterisk blocks to single quotes
# Pattern: blocks that start with *" and end with ."* (or similar)
# Block 1: lines around 526-528 (now shifted)
# Block 2: line 534 (now shifted)

# The pattern is: *"text"* (with possible internal *"text"* inside)
# We need to find blocks that start with *" and end with ."*
# But internal quotes also have this pattern.

# Better approach: Find the specific golden text blocks by content
# Block 1: Contains "Most people think the saber is like a tide wolf"
# Block 2: Contains "You are a Shadow Paw"

# Let's work with the content directly
# Block 1 pattern: *"Most people think the saber..."*"It bites... save you."*
# Block 2 pattern: *"You are a Shadow Paw."* Lira's voice... *"The Eight Points... Remember that."*

# For block 1: Replace the entire span from *"Most people... to ...save you."*
# with single-quoted version where ALL *" and "* are removed

# Find block 1
block1_start = content.find('*"Most people think the saber is like a tide wolf')
if block1_start != -1:
    # Find the end: look for the last ."* in this vicinity
    # The block ends with: *"It bites. This is my fifth form. Serpent's Fang. It's the one that saved me against Sylva. It's the one that will save you."*
    block1_end = content.find('It\'s the one that will save you."', block1_start)
    if block1_end != -1:
        block1_end += len('It\'s the one that will save you."')
        # Include the closing *"
        # Find the next *" after that
        next_star = content.find('*"', block1_end)
        if next_star != -1 and next_star - block1_end < 50:
            block1_end = next_star + 2  # include *"
        
        block1_text = content[block1_start:block1_end]
        print(f"Block 1 found ({len(block1_text)} chars)")
        print(f"  Start: {block1_text[:80]}")
        print(f"  End: {block1_text[-80:]}")
        
        # Remove all *" and "* from the block
        cleaned = block1_text.replace('*"', '"').replace('"*', '"')
        # Also remove any standalone * at start/end of lines within
        cleaned = re.sub(r'^\s*\*', '', cleaned, flags=re.MULTILINE)
        cleaned = re.sub(r'\*\s*$', '', cleaned, flags=re.MULTILINE)
        # Wrap in single quotes
        cleaned = f"'{cleaned}'"
        
        content = content[:block1_start] + cleaned + content[block1_end:]
        print("  Block 1 converted")

# Find block 2
block2_start = content.find('*"You are a Shadow Paw."')
if block2_start != -1:
    # Find end: ...Remember that."*
    block2_end = content.find('Remember that."', block2_start)
    if block2_end != -1:
        block2_end += len('Remember that."')
        # Include closing *"
        next_star = content.find('*"', block2_end)
        if next_star != -1 and next_star - block2_end < 50:
            block2_end = next_star + 2
        
        block2_text = content[block2_start:block2_end]
        print(f"Block 2 found ({len(block2_text)} chars)")
        print(f"  Start: {block2_text[:80]}")
        print(f"  End: {block2_text[-80:]}")
        
        # Remove all *" and "* 
        cleaned = block2_text.replace('*"', '"').replace('"*', '"')
        cleaned = re.sub(r'^\s*\*', '', cleaned, flags=re.MULTILINE)
        cleaned = re.sub(r'\*\s*$', '', cleaned, flags=re.MULTILINE)
        cleaned = f"'{cleaned}'"
        
        content = content[:block2_start] + cleaned + content[block2_end:]
        print("  Block 2 converted")

# Step 3: Also convert any remaining single-line asterisk thoughts
lines = content.splitlines(keepends=True)
new_lines = []
for line in lines:
    stripped = line.strip()
    if stripped.startswith('*') and stripped.endswith('*') and not stripped.startswith('**'):
        inner = stripped[1:-1]
        # Remove any internal *" "* patterns
        inner = inner.replace('*"', '"').replace('"*', '"')
        leading = line[:len(line) - len(line.lstrip())]
        trailing = line[len(line.rstrip()):]
        new_lines.append(leading + f"'{inner}'" + trailing)
        print(f"Converted single-line: {stripped[:80]}")
    else:
        new_lines.append(line)

content = ''.join(new_lines)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nDone. File now has {len(content.splitlines())} lines.")