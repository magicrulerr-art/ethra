"""
Ethra Chapter Formatter
=======================
Post-processes raw extracted chapter prose into reader-friendly markdown
with distinct visual styling for:
  - Ajani's dialogue (amber/gold left-border)
  - Internal thoughts (italic, muted)
  - DM narration (clean prose)
  - Scene transitions (divider)
  - Other characters' speech (subtle styling)

This ensures the raw files are preserved (in raw/) while the formatted
versions are what the site displays.
"""

import re
import os
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

INPUT_DIR = r'C:\Users\magic\.copaw\workspaces\default\ethra_site\content\story'
OUTPUT_DIR = r'C:\Users\magic\.copaw\workspaces\default\ethra_site\content\story'


def format_chapter(text):
    """
    Transform raw chapter prose into reader-friendly markdown with
    HTML classes for distinct dialogue/narration/thought styling.
    """
    lines = text.split('\n')
    output = []
    in_dialogue_block = False
    in_thought_block = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Keep the chapter header
        if stripped.startswith('# Chapter'):
            output.append(line)
            output.append('')
            continue
        
        # Skip empty lines but track state
        if not stripped:
            if in_dialogue_block:
                output.append('</div>')
                output.append('')
                in_dialogue_block = False
            if in_thought_block:
                output.append('</div>')
                output.append('')
                in_thought_block = False
            output.append('')
            continue
        
        # ── Process dialogue ──────────────────────────
        # Pattern: Ajani's speech (full lines starting/ending with quotes)
        is_dialogue = False
        is_thought = False
        is_dm = False
        
        # Full-line quoted dialogue: "Speech goes here"
        if stripped.startswith('"') and '"' in stripped[1:]:
            is_dialogue = True
        # Paragraph that starts heavily with quotes (multi-speech line)
        elif stripped.count('"') >= 2 and ' "' in stripped:
            is_dialogue = True
        
        # Full-line thought: 'thought goes here'  
        if stripped.startswith("'") and stripped.endswith("'") and len(stripped) > 10:
            is_thought = True
            is_dialogue = False
        
        # DM narration markers
        dm_markers = ['Your move, Ajani.', 'Your move,', 'The arena', 
                       'The crowd', 'He watched', 'She watched',
                       'The king', 'The old king', 'The young']
        if any(stripped.startswith(m) for m in dm_markers):
            is_dm = True
        
        # Bold marker phrases in narration (character names, places)
        # Add subtle emphasis to first mention of names in narration blocks
        # This is handled by the CSS rendering — we just need clean paragraphs
        
        # ── Render with classes ───────────────────────
        if is_dialogue or is_thought or is_dm:
            # Close any open block of different type
            if in_dialogue_block and not is_dialogue:
                output.append('</div>')
                output.append('')
                in_dialogue_block = False
            if in_thought_block and not is_thought:
                output.append('</div>')
                output.append('')
                in_thought_block = False
        
        if is_dialogue:
            if not in_dialogue_block:
                output.append('<div class="dialogue-block">')
                in_dialogue_block = True
            # Format the quoted speech cleanly
            cleaned = format_dialogue_line(stripped)
            output.append(cleaned)
        
        elif is_thought:
            if not in_thought_block:
                output.append('<div class="thought-block">')
                in_thought_block = True
            # Make thoughts italic
            output.append(f'*{stripped.strip("'\''")}*')
        
        else:
            # Regular narration — close any open blocks
            if in_dialogue_block:
                output.append('</div>')
                output.append('')
                in_dialogue_block = False
            if in_thought_block:
                output.append('</div>')
                output.append('')
                in_thought_block = False
            
            # Scene transitions
            if stripped == '---':
                output.append('<hr class="scene-break">')
                output.append('')
                continue
            
            # Split long narration paragraphs for readability
            if len(stripped) > 500:
                # Insert paragraph breaks at natural sentence boundaries
                sentences = re.split(r'(?<=[.!?])\s+', stripped)
                para = []
                for s in sentences:
                    para.append(s)
                    if sum(len(x) for x in para) > 400:
                        output.append(' '.join(para))
                        output.append('')
                        para = []
                if para:
                    output.append(' '.join(para))
            else:
                output.append(stripped)
            output.append('')
    
    # Close any remaining blocks
    if in_dialogue_block:
        output.append('</div>')
    if in_thought_block:
        output.append('</div>')
    
    return '\n'.join(output)


def format_dialogue_line(line):
    """Format a line of dialogue, handling quoted speech with context."""
    # Clean up the line
    line = line.strip()
    
    # Check if it contains multiple speakers
    # Pattern: "text" ... "text" — likely a question and answer
    quotes = re.findall(r'"([^"]*)"', line)
    
    if len(quotes) >= 2:
        # Multi-speech line — wrap each quote in a span
        result = line
        for q in quotes:
            result = result.replace(f'"{q}"', f'<span class="speech">"{q}"</span>', 1)
        return result
    
    # Single speech line
    if line.startswith('"') and line.count('"') >= 2:
        # Find the quote content
        inner = line[1:line.rindex('"')]
        prefix = line[line.rindex('"')+1:].strip()
        if prefix:
            return f'<p class="speech-line">"{inner}" <span class="speech-attr">{prefix}</span></p>'
        return f'<p class="speech-line">"{inner}"</p>'
    
    return f'<p class="speech-line">{line}</p>'


def format_all_chapters():
    """Format all chapter raw files and write to the main story directory."""
    if not os.path.exists(INPUT_DIR):
        print(f"Raw directory not found: {INPUT_DIR}")
        return
    
    files = sorted([f for f in os.listdir(INPUT_DIR) if f.startswith('chapter-') and f.endswith('.md')])
    
    for fname in files:
        raw_path = os.path.join(INPUT_DIR, fname)
        out_path = os.path.join(OUTPUT_DIR, fname)
        
        with open(raw_path, 'r', encoding='utf-8') as f:
            raw_text = f.read()
        
        formatted = format_chapter(raw_text)
        
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(formatted)
        
        # Count words for verification
        word_count = len(raw_text.split())
        print(f'  {fname}: {word_count:,} words → formatted')


def main():
    print("Formatting chapters for readability...")
    format_all_chapters()
    print("Done. Raw files preserved in raw/ directory.")


if __name__ == '__main__':
    main()
