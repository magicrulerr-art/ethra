# -*- coding: utf-8 -*-
"""List every distinct non-ASCII run in the two files Mare edited this session."""
import re, collections

out = []
for p in ['templates/index.html', 'static/css/ethra_core.css']:
    txt = open(p, encoding='utf-8').read()
    runs = re.findall(r'[^\x00-\x7f]+', txt)
    c = collections.Counter(runs)
    out.append('== ' + p)
    for run, n in c.most_common(60):
        out.append(f'  {n:4d}  {run!r}')
open('tools/mojibake_report.txt', 'w', encoding='utf-8').write('\n'.join(out))
print('written')
