# -*- coding: utf-8 -*-
"""Editorial metrics for Arcs I-IV: pacing + expressiveness proxies."""
import re, glob, json
from pathlib import Path

def words(s):
    return len(re.findall(r"\w+", s))

files = sorted(glob.glob('ethra_site/content/story/chapters/chapter-arc[1-4]-*.md'))
rows = []
for f in files:
    text = Path(f).read_text(encoding='utf-8')

    # spoken words in <span class="speech">
    speech = sum(words(m.group(1)) for m in re.finditer(r'<span class="speech">(.*?)</span>', text, re.S))

    # speech-line blocks: mix of inner thought (single-quoted) and spoken (double-quoted or bare)
    sl_total = sl_inner = 0
    for m in re.finditer(r'<p class="speech-line">(.*?)</p>', text, re.S):
        c = m.group(1)
        sl_total += words(c)
        sl_inner += sum(words(i) for i in re.findall(r"'([^']*)'", c))
    sl_spoken = sl_total - sl_inner

    plain = re.sub(r'<[^>]+>', ' ', text)
    total = words(plain)
    narration = total - speech - sl_total

    headings = re.findall(r'^\*\*(.+?)\*\*\s*$', text, re.M)
    hr_breaks = len(re.findall(r'^\s*-{3,}\s*$', text, re.M))

    # narration-only text (strip dialogue divs) -> paragraphs
    nodiv = re.sub(r'<div class="dialogue-block">.*?</div>', '\n\n', text, flags=re.S)
    paras = [p.strip() for p in re.split(r'\n\s*\n', nodiv)
             if p.strip() and not p.strip().startswith('#') and not p.strip().startswith('**')]
    pw = [words(p) for p in paras]
    over120 = sum(1 for w in pw if w >= 120)
    over200 = sum(1 for w in pw if w >= 200)
    maxp = max(pw) if pw else 0

    # longest uninterrupted narration run (consecutive narration paragraphs, words)
    blocks = re.split(r'<div class="dialogue-block">', text)
    longest_run = 0
    for b in blocks:
        b = re.sub(r'</div>.*', '', b, flags=re.S) if '</div>' in b else b
        b = re.sub(r'<[^>]+>', ' ', b)
        b = re.sub(r'^\s*\*\*.+\*\*\s*$', '', b, flags=re.M)
        longest_run = max(longest_run, words(b))

    # thought-blocks (explicit)
    tb = len(re.findall(r'<div class="thought-block">', text))

    rows.append(dict(
        file=Path(f).name, total=total, spoken=speech + sl_spoken,
        inner=sl_inner, narration=narration,
        dlg_pct=round(100*(speech+sl_spoken)/total,1),
        inner_pct=round(100*sl_inner/total,1),
        narr_pct=round(100*narration/total,1),
        scenes=len(headings)+hr_breaks, headings=len(headings),
        paras=len(pw), over120=over120, over200=over200, max_para=maxp,
        longest_narr_run=longest_run, thought_blocks=tb,
    ))

# print table
hdr = ['file','total','dlg%','inner%','narr%','scenes','paras','p>=120','p>=200','maxP','longRun']
print('\t'.join(hdr))
for r in rows:
    print('\t'.join(str(r[k]) for k in
        ['file','total','dlg_pct','inner_pct','narr_pct','scenes','paras','over120','over200','max_para','longest_narr_run']))

# arc aggregates
arcs = {}
for r in rows:
    a = r['file'].split('-')[1]
    arcs.setdefault(a, []).append(r)
print()
for a in sorted(arcs):
    rs = arcs[a]
    tot = sum(r['total'] for r in rs)
    sp = sum(r['spoken'] for r in rs)
    inn = sum(r['inner'] for r in rs)
    nar = sum(r['narration'] for r in rs)
    print(f"ARC {a}: chapters={len(rs)} words={tot} spoken%={100*sp/tot:.1f} inner%={100*inn/tot:.1f} narr%={100*nar/tot:.1f} avg_ch={tot//len(rs)}")

Path('ethra_site/QA/editorial_metrics.json').write_text(json.dumps(rows, indent=1), encoding='utf-8')
