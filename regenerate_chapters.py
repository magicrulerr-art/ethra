"""
Regenerate all sub-chapter files from the clean umbrella chapter files.

R20 repair (roadmap P0):
  * BASE is now script-relative (the old hardcoded C:\\Users\\magic\\.copaw
    path was wrong on this machine).
  * Arc metadata (titles / sub_titles / split_anchors / source) is read from
    content/story/arcs.json — the single source of truth shared with
    server.py. Adding an arc no longer requires editing this script.
  * NON-DESTRUCTIVE: output is staged in chapters/_new + arcs/_new, verified
    (file counts per arc must match the manifest), and only then swapped in.
    The previous live splits are preserved under backups/splits-<timestamp>/.
    The old script deleted all live splits BEFORE regenerating — a single
    bad run could have destroyed content with no undo.
  * --check mode: stage + diff against live, report, touch nothing.

Splitting logic is unchanged from the proven R-era implementation.
Outputs: content/story/chapters/chapter-arc{ARC}-{CH}.md and
content/story/arcs/arc-{ARC}.md
"""

import json
import re
import shutil
import sys
import time
from pathlib import Path

BASE = Path(__file__).resolve().parent
STORY = BASE / 'content' / 'story'
CHAPTERS_DIR = STORY / 'chapters'
ARCS_DIR = STORY / 'arcs'
MANIFEST = STORY / 'arcs.json'

CHECK_ONLY = '--check' in sys.argv

ARCS = json.loads(MANIFEST.read_text(encoding='utf-8'))['arcs']

CHAPTERS_DIR.mkdir(parents=True, exist_ok=True)
ARCS_DIR.mkdir(parents=True, exist_ok=True)
CH_NEW = CHAPTERS_DIR / '_new'
AR_NEW = ARCS_DIR / '_new'
for _d in (CH_NEW, AR_NEW):
    if _d.exists():
        shutil.rmtree(_d)
    _d.mkdir(parents=True)

# ── Scene break detection ─────────────────────────────────
# When we can't find explicit markers, split at the first
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

    para_positions = [m.start() for m in re.finditer(r'\n\n+', content)]
    if not para_positions:
        return []

    split_points = []
    used_positions = set()
    for i in range(1, num_chunks):
        target = i * approx_chunk_size
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


def generate_sub_chapters(arc_num, arc_data, out_dir):
    """Read a clean chapter file and split into sub-chapters (staged)."""
    source_path = STORY / arc_data['source']

    if not source_path.exists():
        print(f"  ERROR: Source file not found: {source_path}")
        return []

    content = source_path.read_text(encoding='utf-8')

    sub_titles = arc_data['sub_titles']
    num_chunks = len(sub_titles)

    first_newline = content.find('\n')
    chapter_header = content[:first_newline].strip() if first_newline > 0 else ''

    if arc_data.get('split_anchors'):
        anchors = arc_data['split_anchors']
        split_points = [line_to_offset(content, ln) for ln in anchors]
        print(f"  Using timestamp-aware split at lines: {anchors}")
    else:
        split_points = find_split_points(content, num_chunks)

    if len(split_points) != num_chunks - 1:
        print(f"  WARNING: Found {len(split_points)} splits for {num_chunks} chunks")
        total = len(content)
        split_points = [total * (i + 1) // num_chunks for i in range(num_chunks - 1)]

    chapters = []
    prev = 0
    for i in range(num_chunks):
        end = split_points[i] if i < len(split_points) else len(content)
        chunk = content[prev:end].strip()

        # Detect pre-existing canonical heading inside this chunk.
        canonical_title = None
        first_nl = None
        ch_num = i + 1
        m = re.match(
            r'^(#{1,2})\s+Chapter\s+(\d+)\s*:\s*([^\n]+?)\s*(?:\n|$)',
            chunk,
        )
        if m:
            _lvl, src_ch_num, src_title = m.group(1), m.group(2), m.group(3).strip()
            if str(ch_num) == str(src_ch_num):
                canonical_title = src_title
                first_nl = chunk.find('\n')

        title = canonical_title if canonical_title is not None else sub_titles[i]

        if first_nl is not None:
            rest = chunk[first_nl:].lstrip('\n')
            sub_content = f"## Chapter {ch_num}: {title}\n\n{rest}"
        else:
            sub_content = f"## Chapter {ch_num}: {title}\n\n{chunk}"

        # Defensive: collapse duplicate "## Chapter N:" headings and drop
        # stale single-hash "# Chapter N:" umbrella carry-forwards.
        dedup_lines = []
        seen_chapter_heading = False
        for line in sub_content.split('\n'):
            if re.match(r'^##\s+Chapter\s+\d+\s*:', line):
                if seen_chapter_heading:
                    continue
                seen_chapter_heading = True
                dedup_lines.append(line)
                continue
            if re.match(r'^#\s+Chapter\s+\d+\s*:', line):
                continue
            dedup_lines.append(line)
        sub_content = '\n'.join(dedup_lines).lstrip('\n')

        filename = f"chapter-arc{arc_num}-{ch_num:02d}.md"
        (out_dir / filename).write_text(sub_content, encoding='utf-8')

        chapters.append({
            'filename': filename,
            'title': title,
            'ch_num': ch_num,
            'word_count': len(chunk.split()),
        })
        print(f"  {filename}: {title} ({len(chunk.split())} words)")
        prev = end

    return chapters


def generate_arc_summary(arc_num, arc_data, chapters, ch_dir, ar_dir):
    """Generate an arc summary markdown file (staged)."""
    source_path = STORY / arc_data['source']
    content = source_path.read_text(encoding='utf-8')

    first_nl = content.find('\n')
    header = content[:first_nl].strip() if first_nl > 0 else ''

    total_words = sum(ch['word_count'] for ch in chapters)
    summary = f"{header}\n\n*{total_words:,} words across {len(chapters)} chapters*\n\n"

    for ch in chapters:
        ch_file = ch_dir / ch['filename']
        if ch_file.exists():
            ch_content = ch_file.read_text(encoding='utf-8')
            in_narrative = False
            preview = ''
            for line in ch_content.split('\n'):
                stripped = line.strip()
                if stripped.startswith('## Chapter'):
                    in_narrative = True
                    continue
                if in_narrative and stripped and not stripped.startswith('#'):
                    clean = re.sub(r'<[^>]+>', '', stripped)
                    if len(clean) > 30:
                        preview = clean[:200] + '...'
                        break
            summary += f"### {ch['title']}\n\n{preview}\n\n"

    (ar_dir / f"arc-{arc_num:02d}.md").write_text(summary, encoding='utf-8')
    print(f"  arc-{arc_num:02d}.md: {total_words:,} total words")


# ── Main ───────────────────────────────────────────────────
print(f"\nRegenerating sub-chapters ({'--check' if CHECK_ONLY else 'live swap'})...\n")

all_chapters = []
for arc_str in sorted(ARCS, key=int):
    arc_num = int(arc_str)
    arc_data = ARCS[arc_str]
    print(f"Arc {arc_num}: {arc_data['title']}")
    chapters = generate_sub_chapters(arc_num, arc_data, CH_NEW)
    generate_arc_summary(arc_num, arc_data, chapters, CH_NEW, AR_NEW)
    all_chapters.extend(chapters)
    print()

# ── Verify staged output BEFORE touching live files ───────
problems = []
for arc_str in ARCS:
    expect = len(ARCS[arc_str]['sub_titles'])
    got = len(list(CH_NEW.glob(f"chapter-arc{arc_str}-*.md")))
    if got != expect:
        problems.append(f"arc {arc_str}: staged {got} files, manifest expects {expect}")
if problems:
    print("VERIFICATION FAILED — live files untouched:")
    for p in problems:
        print("  ", p)
    sys.exit(1)

staged = sorted(CH_NEW.glob("chapter-arc*.md"))

if CHECK_ONLY:
    diffs = [f.name for f in staged
             if not (CHAPTERS_DIR / f.name).exists()
             or (CHAPTERS_DIR / f.name).read_text(encoding='utf-8') != f.read_text(encoding='utf-8')]
    print(f"--check: {len(diffs)} of {len(staged)} staged files differ from live.")
    for d in diffs:
        print("   DIFFERS:", d)
    print("Live files untouched.")
    shutil.rmtree(CH_NEW)
    shutil.rmtree(AR_NEW)
    sys.exit(0)

# ── Backup live splits, then swap staged in ───────────────
ts = time.strftime('%Y%m%d-%H%M%S')
BAK = BASE / 'backups' / f'splits-{ts}'
(BAK / 'chapters').mkdir(parents=True)
(BAK / 'arcs').mkdir(parents=True)
for f in CHAPTERS_DIR.glob("chapter-arc*.md"):
    shutil.move(str(f), str(BAK / 'chapters' / f.name))
for f in ARCS_DIR.glob("arc-*.md"):
    shutil.move(str(f), str(BAK / 'arcs' / f.name))
for f in staged:
    shutil.move(str(f), str(CHAPTERS_DIR / f.name))
for f in AR_NEW.glob("arc-*.md"):
    shutil.move(str(f), str(ARCS_DIR / f.name))
shutil.rmtree(CH_NEW)
shutil.rmtree(AR_NEW)

total = sum(ch['word_count'] for ch in all_chapters)
print(f"Done. {len(all_chapters)} sub-chapters swapped in.")
print(f"Total words: {total:,}")
print(f"Previous splits preserved in: {BAK}")
