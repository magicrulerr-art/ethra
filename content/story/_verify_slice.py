p=r'C:\Users\magic\.copaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc5-02.md'
d=open(p,encoding='utf-8').read()
print(len(d),'bytes')
banned=[
    '**Pacing**','**Strategy**','**Lore Reveals**','**Emotional Core**','**A Few Observations**',
    'battle logic holds','correct dramatic structure',
    'anchored to a character','The next Humman scene','The lore reveals are working',
    "Let's start the next scene",'This is the correct',
    'Will retire',"Kira..s arc is the emotional",'dream optimization',
    'Let me verify my context','can you quantify','Begin chapter']
dirty=False
for b in banned:
    c=d.count(b)
    if c>0:
        print(' X Has',repr(b),':',c)
        dirty=True
if not dirty:
    print('PASS4 CLEAN: zero contamination.')
# Check Kira -> 7:55 transition integrity
k=d.find('buried her face in Pearl')
v=d.find('It was 7:55 in the morning')
print('Kira @',k,'  7:55 @',v,'  gap=',(v-k) if(v>k and k>=0) else 'NF')
print('--- TRANSITION CONTEXT ---')
if k>=0 and v>=0:
    print(repr(d[k:k+250]))
