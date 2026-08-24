#!/usr/bin/env python3
"""
Insert E4: Lira→Maren sibling friction scene in Arc6-03.
Insert after Maren's early dialogue (around line 58).
"""

file_path = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-03.md"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find insertion point: after Maren's "The coin master notes..." line
insert_idx = None
for i, line in enumerate(lines):
    if 'The coin master notes that the Shadow Office' in line:
        insert_idx = i + 1
        break

if insert_idx is None:
    print("ERROR: Could not find insertion point")
else:
    print(f"Inserting after line {insert_idx}: {lines[insert_idx-1].strip()[:80]}")
    
    # E4: Lira-Maren sibling friction
    new_lines = [
        '\n',
        '<div class="dialogue-block">\n',
        '<p class="speech-line">Lira\'s ears flattened. She had been silent since the throne room, her lacquered claws retracted but her tail lashing slow and deliberate. "You knew."</p>\n',
        '</div>\n',
        '\n',
        '<div class="dialogue-block">\n',
        '<p class="speech-line">Maren didn\'t look up from her ledger. The stylus didn\'t pause. "I knew the numbers. I knew the risk. I did not know your White Dawn would tear the sky open."</p>\n',
        '</div>\n',
        '\n',
        '<div class="dialogue-block">\n',
        '<p class="speech-line">"You sent me to the Shadow Office. You sent me away from the fight. From *him*." Lira stepped closer, close enough that Maren could smell the desert dust on her fur. "Every report you buried. Every resource you diverted. You made sure I couldn\'t reach him."</p>\n',
        '</div>\n',
        '\n',
        '<div class="dialogue-block">\n',
        '<p class="speech-line">Maren\'s stylus finally stopped. She looked up, and her dark eyes held the cold precision of a coin master who had once been a sister. "I made sure *you* survived. The Shadow Office needed its claws. The White Dawn needed his. You are not the same weapon, Lira. You never were."</p>\n',
        '</div>\n',
        '\n',
        '<div class="dialogue-block">\n',
        '<p class="speech-line">The silence stretched. Then Lira\'s claws half-extended, catching the light. "And if he falls? If the pact breaks? What does your ledger say then, sister?"</p>\n',
        '</div>\n',
        '\n',
        '<div class="dialogue-block">\n',
        '<p class="speech-line">Maren returned to her numbers. "It says we prepare for the audit. As we always have."</p>\n',
        '</div>\n',
        '\n'
    ]
    
    for j, new_line in enumerate(new_lines):
        lines.insert(insert_idx + j, new_line)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"Done. File now has {len(lines)} lines.")
    
    # Verify
    for i in range(insert_idx-2, insert_idx+15):
        if 0 <= i < len(lines):
            print(f"  L{i+1}: {lines[i].rstrip()}")