#!/usr/bin/env python3
"""
Remove debris from chapter-arc6-01.md by searching for content patterns
from regions.json, with wrapper-aware deletion.
"""

import re

# Debris patterns to search for (from regions.json descriptions)
DEBRIS_PATTERNS = [
    # L123: "Next scene beats >When all have said their piece Lira speaks angrily"
    r'Next scene beats >When all have said their piece Lira speaks angrily',
    
    # L197: "well now that's out of the way, I need the talky, M'rak"
    r'well now that\'s out of the way, I need the talky, M\'rak',
    
    # L313: "hmm the council worked as designed I'll need to reward them"
    r'hmm the council worked as designed I\'ll need to reward them',
    
    # L439: "*The next scene is a couple of hours after ajani..."
    r'\*The next scene is a couple of hours after ajani is sitting on the throne',
    
    # L443: "so these are the ones"
    r'\'so these are the ones\' - "So you are the ones who unleashed',
    
    # L485: "Ambassador these are your people"
    r'Ambassador these are your people, deal with them as you see fit',
    
    # L810: "*Let's follow the rest of the cast how is the city doing..."
    r'\*Let\'s follow the rest of the cast how is the city doing after the battle',
    
    # L905: "*Now let's see Yvaria, Reva, lira and vex*"
    r'\*Now let\'s see Yvaria, Reva, lira and vex\*',
    
    # L963: "its worse than I thought"
    r'\'its worse than I thought \' - "call for Maren please"',
    
    # L1042: "theyre brutes, brutes !"
    r'\'theyre brutes, brutes !\' - "Generals I meant from Verdantis',
]

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
    
    # Verify the target line is actually inside this block by scanning forward
    depth = 0
    for i in range(start_idx, len(lines)):
        if '<div class="dialogue-block">' in lines[i]:
            depth += 1
        if '</div>' in lines[i]:
            depth -= 1
            if depth == 0:
                # Found the matching closing tag
                if i >= target_line_idx:
                    return (start_idx, i)
                else:
                    # Target line is after this block - not inside
                    return None
    
    return None

def remove_debris():
    file_path = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-01.md"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.splitlines(keepends=True)
    original_line_count = len(lines)
    
    # Find all debris lines by pattern matching
    debris_line_indices = []
    for pattern in DEBRIS_PATTERNS:
        found = False
        for i, line in enumerate(lines):
            if re.search(pattern, line):
                debris_line_indices.append(i)
                print(f"Found debris pattern at line {i+1}: {line.strip()[:80]}")
                found = True
                break
        if not found:
            print(f"WARNING: Pattern not found: {pattern[:60]}...")
    
    # Determine removal ranges (wrapper-aware)
    to_remove_ranges = []
    
    for idx in debris_line_indices:
        bounds = find_dialogue_block_bounds(lines, idx)
        
        if bounds:
            start, end = bounds
            print(f"  Line {idx+1} -> In dialogue-block wrapper: lines {start+1}-{end+1}")
            # Check if already covered
            covered = False
            for (s, e) in to_remove_ranges:
                if s <= start and end <= e:
                    covered = True
                    break
            if not covered:
                to_remove_ranges.append((start, end))
        else:
            print(f"  Line {idx+1} -> Bare line (no wrapper)")
            to_remove_ranges.append((idx, idx))
    
    # Sort ranges by start line, descending (delete from bottom up)
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
    
    print(f"\nDone. File: {original_line_count} -> {len(lines)} lines ({original_line_count - len(lines)} removed)")

if __name__ == "__main__":
    remove_debris()