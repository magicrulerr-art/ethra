#!/usr/bin/env python3
"""
Remove debris regions from chapter-arc6-01.md with wrapper-aware deletion.
Debris lines (1-based from regions.json):
- L123: inside dialogue-block wrapper
- L197: inside dialogue-block wrapper
- L313: inside dialogue-block wrapper
- L439: bare asterisk line (NOT in wrapper)
- L443: inside dialogue-block wrapper
- L485: inside dialogue-block wrapper
- L810: bare asterisk line (NOT in wrapper)
- L905: bare asterisk line (NOT in wrapper)
- L963: inside dialogue-block wrapper
- L1042: inside dialogue-block wrapper
"""

import re

def find_dialogue_block_bounds(lines, target_line_idx):
    """Find the start and end of the dialogue-block wrapper containing target_line_idx.
    Returns (start_idx, end_idx) inclusive, or None if not in a wrapper."""
    # Look backward for opening <div class="dialogue-block">
    start_idx = None
    for i in range(target_line_idx, -1, -1):
        if '<div class="dialogue-block">' in lines[i]:
            start_idx = i
            break
    if start_idx is None:
        return None
    
    # Look forward for closing </div>
    end_idx = None
    depth = 0
    for i in range(start_idx, len(lines)):
        if '<div class="dialogue-block">' in lines[i]:
            depth += 1
        if '</div>' in lines[i]:
            depth -= 1
            if depth == 0:
                end_idx = i
                break
    
    if end_idx is None:
        return None
    
    return (start_idx, end_idx)

def remove_debris():
    file_path = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-01.md"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Debris lines (1-based) - convert to 0-based indices
    debris_lines_1based = [123, 197, 313, 439, 443, 485, 810, 905, 963, 1042]
    debris_lines_0based = [l - 1 for l in debris_lines_1based]
    
    # Determine which lines are in wrappers vs bare
    # Check each debris line
    to_remove_ranges = []  # list of (start, end) inclusive ranges to remove
    
    for idx in debris_lines_0based:
        if idx >= len(lines):
            print(f"WARNING: Line {idx+1} out of bounds (file has {len(lines)} lines)")
            continue
        
        line_content = lines[idx].rstrip('\n')
        print(f"Line {idx+1}: {line_content[:80]}")
        
        # Check if this line is inside a dialogue-block wrapper
        bounds = find_dialogue_block_bounds(lines, idx)
        
        if bounds:
            start, end = bounds
            print(f"  -> In dialogue-block wrapper: lines {start+1}-{end+1}")
            # Check if this range is already covered
            covered = False
            for (s, e) in to_remove_ranges:
                if s <= start and end <= e:
                    covered = True
                    break
            if not covered:
                to_remove_ranges.append((start, end))
        else:
            print(f"  -> Bare line (no wrapper)")
            to_remove_ranges.append((idx, idx))
    
    # Sort ranges by start line, descending (so we delete from bottom up)
    to_remove_ranges.sort(key=lambda x: x[0], reverse=True)
    
    print(f"\nRanges to remove (0-based, inclusive):")
    for s, e in to_remove_ranges:
        print(f"  Lines {s+1}-{e+1}")
    
    # Remove ranges
    for start, end in to_remove_ranges:
        del lines[start:end+1]
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"\nDone. File now has {len(lines)} lines.")

if __name__ == "__main__":
    remove_debris()