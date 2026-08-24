#!/usr/bin/env python3
"""
Insert canon promotion speech for E2 in Arc6-02.
"""

file_path = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-02.md"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find insertion point: after "We will fix it. Or we will not survive the next war." and before "The weight of the king's words"
insert_idx = None
for i, line in enumerate(lines):
    if 'The weight of the king\'s words settled over the great hall' in line:
        insert_idx = i
        break

if insert_idx is None:
    print("ERROR: Could not find insertion point")
else:
    print(f"Inserting before line {insert_idx+1}: {lines[insert_idx].strip()[:80]}")
    
    # Canon promotion speech from umbrella
    new_lines = [
        '\n',
        '<div class="dialogue-block">\n',
        '<p class="speech-line">"I am promoting these four to two star generals, and giving them full command of one legion. They will pick their garrisons and travel to Verdantis. They won\'t come back until the Humans understand what they brought upon themselves."</p>\n',
        '</div>\n',
        '\n'
    ]
    
    for j, new_line in enumerate(new_lines):
        lines.insert(insert_idx + j, new_line)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"Done. File now has {len(lines)} lines.")
    
    # Verify
    for i in range(insert_idx-2, insert_idx+6):
        if 0 <= i < len(lines):
            print(f"  L{i+1}: {lines[i].rstrip()}")