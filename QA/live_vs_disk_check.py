# -*- coding: utf-8 -*-
"""Fetch every chapter (Arcs I-VII) from the LIVE server, strip tags, and
diff word-for-word against the on-disk .md (tags + markdown heading markers
stripped). Proves the site serves exactly what is on disk.

v2 (2026-08-25): normalizes markdown '#' heading markers on the disk side
(the server renders them as <h2> etc., so the literal '##' token is a
known render artifact, not a content mismatch). Extended coverage from
Arcs I-IV (23 ch) to all seven arcs (52 ch). Run from WORKSPACE ROOT.
"""
import re, urllib.request, pathlib

BASE = "http://localhost:8790"
chapters = []
for arc, n in [(1,6),(2,6),(3,5),(4,6),(5,22),(6,5),(7,2)]:
    for ch in range(1, n+1):
        chapters.append((arc, ch))

def strip_tags(s):
    # inline tags leave no whitespace when rendered — remove without trace
    s = re.sub(r'</?(em|strong|b|i|u|span|a|code|small)[^>]*>', '', s, flags=re.I)
    # block tags render as whitespace
    s = re.sub(r'<[^>]+>', ' ', s)
    s = s.replace('&amp;','&').replace('&lt;','<').replace('&gt;','>').replace('&quot;','"').replace('&#39;',"'").replace('&nbsp;',' ')
    return re.sub(r'\s+', ' ', s).strip()

def normalize_md(s):
    # drop markdown heading markers ('## Chapter N:' -> 'Chapter N:')
    s = re.sub(r'(?m)^#{1,6}\s+', '', s)
    # drop emphasis markers (*italics*, **bold**) — the renderer consumes
    # them outside raw HTML blocks; INSIDE divs they pass through as
    # literal '*', so strip them on BOTH sides for a fair comparison.
    s = s.replace('**', '').replace('*', '')
    # drop horizontal-rule scene markers ('---' renders as <hr>/decoration)
    s = re.sub(r'(?m)^-{3,}\s*$', '', s)
    return re.sub(r'\s+', ' ', s).strip()

mismatches = []
for arc, ch in chapters:
    cid = f"arc{arc}-ch{ch:02d}"
    url = f"{BASE}/api/chapter/{cid}"
    try:
        html = urllib.request.urlopen(url, timeout=15).read().decode('utf-8')
    except Exception as e:
        print(f"{cid}: FETCH FAIL {e}")
        mismatches.append(cid)
        continue
    live_words = strip_tags(normalize_md(html)).split()
    disk = pathlib.Path(f"ethra_site/content/story/chapters/chapter-arc{arc}-{ch:02d}.md").read_text(encoding='utf-8')
    disk_words = strip_tags(normalize_md(disk)).split()
    if live_words == disk_words:
        print(f"{cid}: IDENTICAL ({len(live_words)} words)")
    else:
        n = min(len(live_words), len(disk_words))
        i = next((k for k in range(n) if live_words[k] != disk_words[k]), n)
        print(f"{cid}: DIFFERS live={len(live_words)}w disk={len(disk_words)}w first@{i}: live={' '.join(live_words[i:i+8])!r} disk={' '.join(disk_words[i:i+8])!r}")
        mismatches.append(cid)

print()
print("RESULT:", f"ALL {len(chapters)} CHAPTERS IDENTICAL LIVE vs DISK" if not mismatches else f"MISMATCHES ({len(mismatches)}): {mismatches}")
