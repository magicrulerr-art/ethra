#!/usr/bin/env python3
"""
Fix multiline asterisk block in Arc6-02 (lines 205-222).
"""

file_path = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-02.md"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# The multiline block starts at line 205 (1-based) with "*You burned yourself..."
# and ends at line 222 (1-based) with "But today—today you have won.*"
# Convert: remove leading * from first line, remove trailing * from last line, wrap whole block in single quotes

start_idx = 204  # 0-based
end_idx = 221    # 0-based

print("Original block:")
for i in range(start_idx, end_idx + 1):
    print(f"  L{i+1}: {lines[i].rstrip()}")

# Extract content
block_lines = [lines[i].rstrip('\n') for i in range(start_idx, end_idx + 1)]
# Remove leading * from first line
block_lines[0] = block_lines[0][1:] if block_lines[0].startswith('*') else block_lines[0]
# Remove trailing * from last line
block_lines[-1] = block_lines[-1][:-1] if block_lines[-1].endswith('*') else block_lines[-1]

# Join with spaces (single paragraph) or keep line breaks
joined = ' '.join(block_lines)

# Replace with single-quoted version
new_line = f"'{joined}'\n"

# Replace the block
del lines[start_idx:end_idx+1]
lines.insert(start_idx, new_line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"\nReplaced with single-quoted block:")
print(f"  L{start_idx+1}: {lines[start_idx].strip()[:150]}...")
print(f"\nFile now has {len(lines)} lines.")