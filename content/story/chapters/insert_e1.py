#!/usr/bin/env python3
"""
Insert E1 rewrite for Arc6-01 after Cefiro's introduction.
"""

file_path = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-01.md"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the line after Cefiro's dialogue-block closing </div>
# Cefiro's block ends with "</div>" then blank lines then "M'rak straightened"
insert_idx = None
for i, line in enumerate(lines):
    if "M'rak straightened at the sound of his own name" in line:
        insert_idx = i
        break

if insert_idx is None:
    print("ERROR: Could not find insertion point")
else:
    print(f"Inserting before line {insert_idx+1}: {lines[insert_idx].strip()[:80]}")
    
    # E1 rewrite: Natural Ajani voice, same beat, keep dialogue wrapper
    new_lines = [
        '\n',
        '<div class="dialogue-block">\n',
        '<p class="speech-line">"Right. Now that\'s settled. Talk to me, M\'rak—that\'s your name, yeah? How many did we lose? Wengari, resident Humans, Pyrinae—and what\'s the state of the north wall?"</p>\n',
        '</div>\n',
        '\n'
    ]
    
    # Insert
    for j, new_line in enumerate(new_lines):
        lines.insert(insert_idx + j, new_line)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"Done. File now has {len(lines)} lines.")

# Verify
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(insert_idx-2, insert_idx+6):
    if 0 <= i < len(lines):
        print(f"  L{i+1}: {lines[i].rstrip()}")