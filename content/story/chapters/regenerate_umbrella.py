#!/usr/bin/env python3
"""
Regenerate chapter-06.md (umbrella) by concatenating cleaned arc6-01 through arc6-05.
"""

import os

arc_files = [
    r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-01.md",
    r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-02.md",
    r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-03.md",
    r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-04.md",
    r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-05.md",
]

output_path = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapter-06.md"

combined = []
for arc_file in arc_files:
    with open(arc_file, 'r', encoding='utf-8') as f:
        content = f.read()
    combined.append(content)

# Join with double newline between arcs
umbrella_content = '\n\n'.join(combined)

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(umbrella_content)

total_lines = len(umbrella_content.splitlines())
print(f"Umbrella regenerated: {total_lines} lines from 5 arcs")
for i, arc_file in enumerate(arc_files):
    with open(arc_file, 'r', encoding='utf-8') as f:
        arc_lines = len(f.read().splitlines())
    print(f"  Arc6-0{i+1}: {arc_lines} lines")