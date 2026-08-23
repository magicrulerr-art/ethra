"""Regression diff: /api/map/coordinates old (8790) vs new (8791).

Creatures must be IDENTICAL (frontmatter merge reproduces the JSON).
city_pins must now carry the six canonical places.
"""
import json
import urllib.request

old = json.load(urllib.request.urlopen('http://127.0.0.1:8790/api/map/coordinates'))
new = json.load(urllib.request.urlopen('http://127.0.0.1:8791/api/map/coordinates'))

def key(c):
    return c.get('slug')

oc = sorted(old['creatures'], key=key)
nc = sorted(new['creatures'], key=key)
print('old creatures:', len(oc), ' new creatures:', len(nc))

diffs = 0
for a, b in zip(oc, nc):
    if a != b:
        diffs += 1
        print('DIFF at', a.get('slug'))
        for k in sorted(set(a) | set(b)):
            if a.get(k) != b.get(k):
                print('   ', k, ':', repr(a.get(k)), '->', repr(b.get(k)))
if len(oc) != len(nc):
    print('COUNT MISMATCH')
    diffs += 1
print('creature diffs:', diffs)

print('biomes identical:', old['biomes'] == new['biomes'])
print('underground identical:', old.get('underground_cave') == new.get('underground_cave'))

print('\ncity_pins (new):')
for p in new.get('city_pins', []):
    print('  ', p)

places = json.load(urllib.request.urlopen('http://127.0.0.1:8791/api/places'))
print('\n/api/places count:', len(places), '->', [p['name'] for p in places])

one = json.load(urllib.request.urlopen('http://127.0.0.1:8791/api/place/styxian'))
print('\n/api/place/styxian keys:', sorted(one.keys()))
print('content preview:', one['content'][:200].replace('\n', ' '))
