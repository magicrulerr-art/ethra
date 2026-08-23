p=r'C:\Users\magic\.copaw\workspaces\default\ethra_site\content\story\chapter-05.md'
d=open(p,encoding='utf-8').read()
ts_idx = d.find("the scene ends", 105105)
print('the scene ends idx:', ts_idx)
post = d[ts_idx:ts_idx+50]
print('post-repr:', repr(post))
div_idx = d.find('</div>', ts_idx)
print('</div> after:', div_idx)
print('post-div:', repr(d[div_idx:div_idx+30]))
