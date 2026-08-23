"""
Regenerate all sub-chapter files from the 6 clean chapter files.
Splits at logical scene boundaries and outputs to content/story/chapters/
with naming: chapter-arc{ARC}-{CH}.md

Also generates arc summary files in content/story/arcs/arc-{ARC}.md
"""

import os
import re
from pathlib import Path

BASE = Path(r'C:\Users\magic\.copaw\workspaces\default\ethra_site')
STORY = BASE / 'content' / 'story'
CHAPTERS_DIR = STORY / 'chapters'
ARCS_DIR = STORY / 'arcs'

# Ensure output directories exist
CHAPTERS_DIR.mkdir(parents=True, exist_ok=True)
ARCS_DIR.mkdir(parents=True, exist_ok=True)

# ── Delete old files ──────────────────────────────────────
print("Cleaning old files...")
for f in CHAPTERS_DIR.glob("chapter-arc*.md"):
    f.unlink()
    print(f"  Deleted: {f.name}")
for f in ARCS_DIR.glob("arc-*.md"):
    f.unlink()
    print(f"  Deleted: {f.name}")

# ── Arc metadata ──────────────────────────────────────────
ARCS = {
    1: {
        'source': 'chapter-01.md',
        'title': 'Arc I: The White Dawn',
        'sub_titles': [
            'The Return',
            'The Chamber',
            'The Pact',
            'The Styx',
            'The Four Pillars',
            'The Passing',
        ],
    },
    2: {
        'source': 'chapter-02.md',
        'title': 'Arc II: The Council',
        'sub_titles': [
            'The Summons',
            'The Confession',
            'The Shadow Paw',
            'The Tree\'s Judgment',
            'The Hydromancer',
            'Foreign Delegations',
        ],
    },
    3: {
        'source': 'chapter-03.md',
        'title': 'Arc III: The Tournament',
        'sub_titles': [
            'The Arena',
            'First Blood',
            'The Fire Feet',
            'The Tyrant Cycle',
            'The Hour Before',
        ],
    },
    4: {
        'source': 'chapter-04.md',
        'title': 'Arc IV: The Consolidation',
        'sub_titles': [
            'Bureaucracy',
            'The Caravans',
            'The Pyrinae Accord',
            'The Humman Delegation',
            'The Gifts',
            'Aftermath',
        ],
    },
    5: {
        'source': 'chapter-05.md',
        'title': 'Arc V: The Great War',
        'sub_titles': [
            '05:25 — Vasha Storms In',
            '06:55 — Sera Holds The Gate',
            '06:25 — The War Room Still Watches',
            '07:55 — The Dome Shimmers',
            '08:15 — The Second Shot',
            '08:20 — The Light Shield Falls',
            '08:40 — The Plague Comes',
            '08:45 — Scorpions Still Marching',
            '09:00 — The Truce Lasts An Hour',
            '09:30 — The Wall Breaks',
            '09:45 — The War Becomes Worse',
            '10:35 — The Wall Blanketed',
            '11:20 — The Shadow Figure Drinks',
            '11:35 — The Wall Learns Horror',
            '11:40 — M\'rak Yells Clear',
            '11:50 — Vows Are Absolved',
            '11:55 — The Legend Answers',
            '11:59 — Nefere Fires',
            '12:02 — Ajani Throws The Spear',
            '12:03 — Cefiro Arrives',
            '12:05 — The Light Cage Fades',
            '12:06 — The White Dawn Wakes',
        ],
        # Timestamp-aware split: each anchor is a 1-based line number in
        # chapter-05.md where the new sub-chapter/title boundary lands.
        # The first chapter always begins at the source's first line; the
        # anchors below mark the LAST line of each preceding chapter
        # (equivalently, the FIRST line of the next chapter).
        # Strategy: war-dispatch mode — every distinct prose timestamp is
        # a chapter boundary. 21 anchors produce 22 chapters from
        # 22 timestamps (5:25 → 12:06). The 12:04 timestamp is a one-sentence
        # beat (only 2 source lines) which has been collapsed into the
        # adjacent 12:03/12:05 chapter.
        # Source has been surgically cleaned across 12 cuts of all
        # DM-author-meta blocks before this splitter is run.
        'split_anchors': [410, 550, 728, 772, 792, 998, 1090, 1111, 1146, 1278, 1592, 1636, 1668, 1703, 1762, 1872, 1909, 2023, 2132, 2156, 2193],
    },
    6: {
        'source': 'chapter-06.md',
        'title': 'Arc VI: Aftermath & The Road',
        'sub_titles': [
            'The Cost',
            'Rebuilding',
            'The Vision',
            'The Road Begins',
            'Epilogue',
        ],
    },
}

# ── Scene break detection ─────────────────────────────────
# When we can't find explicit markers, we split at the first
# paragraph break after roughly equal word counts.

SCENE_BREAK_MARKERS = [
    # Bold section titles
    r'^\*\*[A-Z][^*]{3,60}\*\*\s*$',
    # Time/location shifts
    r'^(The (morning|evening|night|sun|moon|next day|following))',
    r'^(Three|Four|Five|A few|Several) (days|weeks|months|hours)',
    # Character-focused scene starts
    r'^(Ajani|Kareth|Nyasha|T\'van|Seris|Sylara|L\'vat|Uthgard|Zara|Solen) (stood|sat|entered|stepped|walked|rose|woke|opened|looked|turned|arrived|left|departed|set)',
    # </div> followed by narrative paragraph (post-dialogue scene break)
]

def line_to_offset(content, line_no):
    """Convert a 1-based line number to a character offset in content.

    Returns the offset of the START of the given line. If line_no is past
    end-of-file, returns len(content).
    """
    if line_no <= 1:
        return 0
    # Find offsets of each newline up to line_no-1
    offset = 0
    for _ in range(line_no - 1):
        nl = content.find('\n', offset)
        if nl == -1:
            return len(content)
        offset = nl + 1  # start of next line
    return offset


def find_split_points(content, num_chunks):
    """
    Find logical split points in the content for num_chunks sub-chapters.
    Returns list of character offsets where splits should occur.
    """
    total_len = len(content)
    approx_chunk_size = total_len // num_chunks
    
    # Find paragraphs (split by double newline)
    para_positions = []
    for m in re.finditer(r'\n\n+', content):
        para_positions.append(m.start())
    
    if not para_positions:
        return []
    
    # Find split points near approximate boundaries
    split_points = []
    used_positions = set()
    
    for i in range(1, num_chunks):
        target = i * approx_chunk_size
        
        # Find paragraph break closest to target
        best_pos = None
        best_dist = float('inf')
        
        for pos in para_positions:
            if pos in used_positions:
                continue
            dist = abs(pos - target)
            if dist < best_dist and dist < approx_chunk_size * 0.5:
                best_dist = dist
                best_pos = pos
        
        if best_pos is not None:
            split_points.append(best_pos)
            used_positions.add(best_pos)
    
    split_points.sort()
    return split_points


def generate_sub_chapters(arc_num, arc_data):
    """Read a clean chapter file and split into sub-chapters."""
    source_path = STORY / arc_data['source']
    
    if not source_path.exists():
        print(f"  ERROR: Source file not found: {source_path}")
        return []
    
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    sub_titles = arc_data['sub_titles']
    num_chunks = len(sub_titles)
    
    # Find the first line (chapter header)
    first_newline = content.find('\n')
    chapter_header = content[:first_newline].strip() if first_newline > 0 else ''
    
    # Find split points (timestamp-aware override for arcs that declare split_anchors)
    if arc_data.get('split_anchors'):
        anchors = arc_data['split_anchors']
        split_points = [line_to_offset(content, ln) for ln in anchors]
        print(f"  Using timestamp-aware split at lines: {anchors}")
    else:
        split_points = find_split_points(content, num_chunks)

    if len(split_points) != num_chunks - 1:
        print(f"  WARNING: Found {len(split_points)} splits for {num_chunks} chunks")
        # Fall back to equal character splits
        total = len(content)
        split_points = [total * (i+1) // num_chunks for i in range(num_chunks - 1)]
    
    # Build chunks
    chapters = []
    prev = 0
    for i in range(num_chunks):
        if i < len(split_points):
            end = split_points[i]
        else:
            end = len(content)
        
        chunk = content[prev:end].strip()

        # Detect pre-existing canonical heading inside this chunk.
        # If the source has its own "# Chapter N: <Canonical>" or "## Chapter N: <Canonical>"
        # we prefer that exact canonical title over the hardcoded sub_titles entry.
        canonical_title = None
        first_nl = None
        ch_num = i + 1
        m = re.match(
            r'^(#{1,2})\s+Chapter\s+(\d+)\s*:\s*([^\n]+?)\s*(?:\n|$)',
            chunk,
        )
        if m:
            heading_level, src_ch_num, src_title = m.group(1), m.group(2), m.group(3).strip()
            # Only adopt canonical title if chapter numbers match (avoid cross-pollination)
            if str(ch_num) == str(src_ch_num):
                canonical_title = src_title
                first_nl = chunk.find('\n')

        title = canonical_title if canonical_title is not None else sub_titles[i]

        # Build the sub-chapter content.
        # If the chunk already starts with a "# Chapter N: ..." heading we adopted, drop it —
        # otherwise we'd have a duplicate heading in the served HTML.
        if first_nl is not None:
            header_line = chunk[:first_nl]
            rest = chunk[first_nl:].lstrip('\n')
            sub_content = f"## Chapter {ch_num}: {title}\n\n{rest}"
        else:
            sub_content = f"## Chapter {ch_num}: {title}\n\n{chunk}"

        # Defensive: collapse duplicate "## Chapter N:" headings. Some umbrella files
        # carry the canonical heading mid-chunk; we keep the FIRST occurrence and
        # delete every subsequent line that matches "^## Chapter N:". This avoids the
        # double-heading pathology observed in chapter-arc4-05.md line 151/1.
        # Ainz-sama additionally flagged: every slot-1 file previously carried the
        # umbrella's leading "# Chapter N:" heading as a stale carry-forward. We
        # now delete any single-hash "# Chapter N:" header entirely (it should not
        # appear in a slot file — the canonical heading we wrote above is double-hash).
        dedup_lines = []
        seen_chapter_heading = False
        for line in sub_content.split('\n'):
            if re.match(r'^##\s+Chapter\s+\d+\s*:', line):
                if seen_chapter_heading:
                    continue  # skip duplicate
                seen_chapter_heading = True
                dedup_lines.append(line)
                continue
            if re.match(r'^#\s+Chapter\s+\d+\s*:', line):
                # Stale umbrella carry-forward (# Chapter N:) — discard entirely
                continue
            dedup_lines.append(line)
        sub_content = '\n'.join(dedup_lines).lstrip('\n')

        # Write to file
        filename = f"chapter-arc{arc_num}-{ch_num:02d}.md"
        filepath = CHAPTERS_DIR / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(sub_content)
        
        chapters.append({
            'filename': filename,
            'title': title,
            'ch_num': ch_num,
            'word_count': len(chunk.split()),
        })
        
        print(f"  {filename}: {title} ({len(chunk.split())} words)")
        
        prev = end
    
    return chapters


def generate_arc_summary(arc_num, arc_data, chapters):
    """Generate an arc summary markdown file."""
    source_path = STORY / arc_data['source']
    
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the chapter header
    first_nl = content.find('\n')
    header = content[:first_nl].strip() if first_nl > 0 else ''
    
    # Build summary
    total_words = sum(ch['word_count'] for ch in chapters)
    summary = f"{header}\n\n"
    summary += f"*{total_words:,} words across {len(chapters)} chapters*\n\n"
    
    for ch in chapters:
        # Get first paragraph of each chapter as preview
        ch_file = CHAPTERS_DIR / ch['filename']
        if ch_file.exists():
            with open(ch_file, 'r', encoding='utf-8') as f:
                ch_content = f.read()
            # Skip the chapter header, get first narrative paragraph
            lines = ch_content.split('\n')
            preview = ''
            in_narrative = False
            for line in lines:
                stripped = line.strip()
                if stripped.startswith('## Chapter'):
                    in_narrative = True
                    continue
                if in_narrative and stripped and not stripped.startswith('#'):
                    # Clean HTML tags for preview
                    clean = re.sub(r'<[^>]+>', '', stripped)
                    if len(clean) > 30:
                        preview = clean[:200] + '...'
                        break
            
            summary += f"### {ch['title']}\n\n{preview}\n\n"
    
    # Write arc summary
    arc_path = ARCS_DIR / f"arc-{arc_num:02d}.md"
    with open(arc_path, 'w', encoding='utf-8') as f:
        f.write(summary)
    
    print(f"  arc-{arc_num:02d}.md: {total_words:,} total words")


# ── Main ───────────────────────────────────────────────────
print("\nRegenerating sub-chapters from clean source files...\n")

all_chapters = []
for arc_num in sorted(ARCS.keys()):
    arc_data = ARCS[arc_num]
    print(f"Arc {arc_num}: {arc_data['title']}")
    chapters = generate_sub_chapters(arc_num, arc_data)
    generate_arc_summary(arc_num, arc_data, chapters)
    all_chapters.extend(chapters)
    print()

total = sum(ch['word_count'] for ch in all_chapters)
print(f"Done. {len(all_chapters)} sub-chapters generated.")
print(f"Total words: {total:,}")
