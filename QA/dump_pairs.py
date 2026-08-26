# -*- coding: utf-8 -*-
"""Dump FULL text of every flagged duplicate pair for Ainz's judgment."""
import re, glob, pathlib, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

MINW=12; MINP=20; JACC=0.55
def paras(text):
    out=[]
    for blk in re.split(r'\n\s*\n', text):
        blk=blk.strip()
        if not blk: continue
        ps=re.findall(r'<p[^>]*>(.*?)</p>', blk, re.S)
        if ps: out.extend(ps)
        elif '<p' not in blk: out.append(blk)
    return out
def norm(s):
    s=re.sub(r'<[^>]+>',' ',s); return re.sub(r'\s+',' ',s).lower().strip(' .')
def words(s): return norm(s).split()
def display(s):
    s=re.sub(r'<[^>]+>','',s); return re.sub(r'\s+',' ',s).strip()

out=[]
for f in sorted(glob.glob('ethra_site/content/story/chapters/chapter-arc[1-7]-*.md')):
    text=pathlib.Path(f).read_text(encoding='utf-8')
    plist=paras(text); pw=[words(p) for p in plist]; sets=[set(w) for w in pw]
    pairs=[]
    for i in range(len(plist)):
        for j in range(i+1,len(plist)):
            wi,wj=pw[i],pw[j]
            if len(wi)<MINW or len(wj)<MINW: continue
            if wi==wj:
                pairs.append(('VERBATIM',1.0,i,j)); continue
            k=0
            while k<min(len(wi),len(wj)) and wi[k]==wj[k]: k+=1
            if k>=MINW: pairs.append(('PREFIX',k,i,j)); continue
            if len(wi)>=MINP and len(wj)>=MINP:
                u=len(sets[i]|sets[j]); inter=len(sets[i]&sets[j])
                if u and inter/u>=JACC: pairs.append(('NEAR',round(inter/u,2),i,j))
    seen={}
    for idx,p in enumerate(plist):
        for q in re.findall(r'["\u201c]([^"\u201d]{40,})["\u201d]', p):
            qn=norm(q)
            if len(qn.split())>=8: seen.setdefault(qn,[]).append(idx)
    speech=[(q,ixs) for q,ixs in seen.items() if len(ixs)>1]
    if not pairs and not speech: continue
    name=pathlib.Path(f).name
    out.append(f"\n\n{'='*70}\n## {name}\n{'='*70}")
    for n,(kind,score,i,j) in enumerate(pairs,1):
        out.append(f"\n--- [{name} #{n}] {kind} (score={score}) ---")
        out.append("VERSION A:\n  "+display(plist[i]))
        out.append("VERSION B:\n  "+display(plist[j]))
    for n,(q,ixs) in enumerate(speech,1):
        out.append(f"\n--- [{name} SPEECH #{n}] repeated x{len(ixs)} ---")
        out.append("  "+display(q))

doc="\n".join(out)
pathlib.Path('ethra_site/QA/duplicate_pairs_for_judgment.md').write_text(
    "# Ethra Duplicate Pairs — For Ainz's Judgment\n\nEach entry shows the two (or more) versions of a repeated beat. "+
    "Rule KEEP-A / KEEP-B / KEEP-BOTH for each.\n"+doc, encoding='utf-8')
print(f"Wrote {len(doc)} chars; pairs dumped.")
print("Chapters with flags:", re.findall(r'## (chapter-arc[0-9-]+\.md)', doc))
