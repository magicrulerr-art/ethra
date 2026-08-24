#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chapter-boundary check — Arc V (NEW, bonus check).
1. Re-split umbrella chapter-05.md using arcs.json line anchors with the SAME
   algorithm as regenerate_chapters.py; compare byte-for-byte against the 22
   published split files (consistency: published == regenerated).
2. For every boundary, inspect the last prose line of chapter N and first prose
   line of chapter N+1 for mid-sentence/mid-clause cuts and unclosed markup.
Read-only. Output: QA/arc5_tooling/a5_boundary.txt"""
import re, io, os, json, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STORY = os.path.join(BASE, "content", "story")
CH = os.path.join(STORY, "chapters")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "a5_boundary.txt")
out = open(OUT, "w", encoding="utf-8")
def P(*a):
    print(*a); out.write(" ".join(str(x) for x in a) + "\n")

arcs = json.load(open(os.path.join(STORY, "arcs.json"), encoding="utf-8"))["arcs"]
a5 = arcs["5"]
content = open(os.path.join(STORY, a5["source"]), encoding="utf-8").read()
umb_lines = content.split("\n")
anchors = a5["split_anchors"]
sub_titles = a5["sub_titles"]

def line_to_offset(content, line_no):
    if line_no <= 1:
        return 0
    offset = 0
    for _ in range(line_no - 1):
        nl = content.find("\n", offset)
        if nl == -1:
            return len(content)
        offset = nl + 1
    return offset

split_points = [line_to_offset(content, ln) for ln in anchors]
chunks = []
prev = 0
for i in range(len(sub_titles)):
    end = split_points[i] if i < len(split_points) else len(content)
    chunks.append(content[prev:end].strip())
    prev = end

P("=" * 100)
P("PART 1 — REGENERATION CONSISTENCY (rebuild splits in-memory, diff vs published)")
P("=" * 100)
all_match = True
for i, chunk in enumerate(chunks):
    ch_num = i + 1
    canonical_title = None
    first_nl = None
    m = re.match(r"^(#{1,2})\s+Chapter\s+(\d+)\s*:\s*([^\n]+?)\s*(?:\n|$)", chunk)
    if m:
        _lvl, src_ch_num, src_title = m.group(1), m.group(2), m.group(3).strip()
        if str(ch_num) == str(src_ch_num):
            canonical_title = src_title
            first_nl = chunk.find("\n")
    title = canonical_title if canonical_title is not None else sub_titles[i]
    if first_nl is not None:
        rest = chunk[first_nl:].lstrip("\n")
        sub_content = "## Chapter %d: %s\n\n%s" % (ch_num, title, rest)
    else:
        sub_content = "## Chapter %d: %s\n\n%s" % (ch_num, title, chunk)
    dedup_lines = []
    seen = False
    for line in sub_content.split("\n"):
        if re.match(r"^##\s+Chapter\s+\d+\s*:", line):
            if seen:
                continue
            seen = True
            dedup_lines.append(line)
            continue
        if re.match(r"^#\s+Chapter\s+\d+\s*:", line):
            continue
        dedup_lines.append(line)
    sub_content = "\n".join(dedup_lines).lstrip("\n")
    fname = "chapter-arc5-%02d.md" % ch_num
    published = open(os.path.join(CH, fname), encoding="utf-8").read()
    if published == sub_content:
        P("  %-24s MATCH  (title=%s)" % (fname, title))
    else:
        all_match = False
        P("  %-24s DIFFERS (title=%s)" % (fname, title))
        pl = published.split("\n"); sl = sub_content.split("\n")
        P("     published lines=%d regenerated lines=%d" % (len(pl), len(sl)))
        shown = 0
        for j in range(max(len(pl), len(sl))):
            a = pl[j] if j < len(pl) else "<EOF>"
            b = sl[j] if j < len(sl) else "<EOF>"
            if a != b:
                P("     first diff at line %d:" % (j + 1))
                P("       published:   %s" % repr(a[:150]))
                P("       regenerated: %s" % repr(b[:150]))
                shown += 1
                if shown >= 3:
                    break
P("ALL MATCH: %s" % all_match)

P("")
P("=" * 100)
P("PART 2 — BOUNDARY INTEGRITY (last prose line of ch N / first prose line of ch N+1)")
P("=" * 100)
TAG = re.compile(r"<[^>]+>")

def prose_lines(path):
    raw = open(path, encoding="utf-8").read().split("\n")
    res = []
    for i, l in enumerate(raw, 1):
        t = TAG.sub("", l).strip()
        if t and not l.startswith("## Chapter"):
            res.append((i, l, t))
    return raw, res

for i in range(22):
    fname = "chapter-arc5-%02d.md" % (i + 1)
    raw, pl = prose_lines(os.path.join(CH, fname))
    last_ln, last_raw, last_txt = pl[-1]
    # div balance
    opens = len(re.findall(r"<div\b", "\n".join(raw)))
    closes = len(re.findall(r"</div>", "\n".join(raw)))
    div_note = "" if opens == closes else "  <<DIV IMBALANCE open=%d close=%d>>" % (opens, closes)
    endch = last_txt.rstrip()[-1] if last_txt.rstrip() else "?"
    ends_sentence = endch in ".!?\"\u201d"
    P("--- ch %02d (%s)%s" % (i + 1, fname, div_note))
    P("    LAST  L%-4d [%s] %s" % (last_ln, "SENTENCE-END" if ends_sentence else "NO-FINAL-STOP", last_txt[:150]))
    if i + 1 < 22:
        nraw, npl = prose_lines(os.path.join(CH, "chapter-arc5-%02d.md" % (i + 2)))
        first_ln, first_raw, first_txt = npl[0]
        P("    FIRST L%-4d %s" % (first_ln, first_txt[:150]))
        # verdict heuristics
        notes = []
        if not ends_sentence:
            notes.append("tail lacks sentence-final punctuation (possible mid-clause cut or dash cutoff)")
        if re.search(r"[,;:]$", last_txt.rstrip()):
            notes.append("tail ends with comma/semicolon/colon — likely MID-CLAUSE cut")
        if last_txt.rstrip().endswith("\u2014"):
            notes.append("tail ends with em dash (suspended)")
        if not re.match(r'^[A-Z"\'<\u201c*]', first_raw.strip()) and not first_raw.strip().startswith("<"):
            notes.append("next chapter starts lowercase")
        if notes:
            for n in notes:
                P("    NOTE: %s" % n)
out.close()
print("done -> a5_boundary.txt")
