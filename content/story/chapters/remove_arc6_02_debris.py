#!/usr/bin/env python3
"""
Remove Arc6-02 debris regions with wrapper-aware deletion.
Line numbers match regions.json exactly.
"""

file_path = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-02.md"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Debris regions (1-based, inclusive) from regions.json
# Format: (start, end, description)
debris_regions = [
    (176, 176, "L176 DRAFT-BEAT"),
    (352, 352, "L352 DRAFT-LINE promotion speech"),
    (486, 486, "L486 DIRECTIVE asterisk"),
    (489, 489, "L489 SYNOPSIS"),
    (585, 585, "L585 DRAFT-BEAT"),
    (672, 672, "L672 SYNOPSIS"),
    (779, 790, "L779-790 CRAFT-BLOCK"),
    (895, 895, "L895 DIRECTIVE asterisk"),
    (898, 898, "L898 DRAFT-BEAT"),
    (948, 990, "L948-990 DUP-BLOCK Tree scene V1"),
    (1089, 1089, "L1089 DRAFT-BEAT asterisk"),
]

def find_dialogue_block_bounds(lines, target_start, target_end):
    """Find dialogue-block wrapper containing the target range."""
    # Look backward from target_start for opening <div class="dialogue-block">
    start_idx = None
    for i in range(target_start - 1, -1, -1):
        if '<div class="dialogue-block">' in lines[i]:
            start_idx = i
            break
    if start_idx is None:
        return None
    
    # Verify target range is inside this block by scanning forward
    depth = 0
    for i in range(start_idx, len(lines)):
        if '<div class="dialogue-block">' in lines[i]:
            depth += 1
        if '</div>' in lines[i]:
            depth -= 1
            if depth == 0:
                if i >= target_end - 1:
                    return (start_idx, i)
                else:
                    return None
    return None

# Determine removal ranges
to_remove = []

for start, end, desc in debris_regions:
    start_idx = start - 1
    end_idx = end - 1
    
    print(f"{desc}: lines {start}-{end}")
    for i in range(start_idx, min(end_idx + 1, len(lines))):
        print(f"  {i+1}: {lines[i].strip()[:100]}")
    
    # Check if in dialogue-block wrapper
    bounds = find_dialogue_block_bounds(lines, start_idx, end_idx)
    if bounds:
        w_start, w_end = bounds
        print(f"  -> In dialogue-block wrapper: lines {w_start+1}-{w_end+1}")
        # Check if already covered
        covered = False
        for (s, e) in to_remove:
            if s <= w_start and w_end <= e:
                covered = True
                break
        if not covered:
            to_remove.append((w_start, w_end))
    else:
        print(f"  -> Bare lines")
        to_remove.append((start_idx, end_idx))

# Sort by start line descending (delete from bottom up)
to_remove.sort(key=lambda x: x[0], reverse=True)

print(f"\nRanges to remove (0-based, inclusive):")
for s, e in to_remove:
    print(f"  Lines {s+1}-{e+1}")

# Remove
for start, end in to_remove:
    del lines[start:end+1]

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"\nDone. File now has {len(lines)} lines.")