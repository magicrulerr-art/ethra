# -*- coding: utf-8 -*-
"""One-shot: create the Pages site with build_type=workflow using the
git-stored credential. Token never printed."""
import json
import subprocess
import sys
import urllib.request

inp = "protocol=https\nhost=github.com\n\n"
out = subprocess.run(['git', 'credential', 'fill'], input=inp,
                     capture_output=True, text=True)
tok = ''
for line in out.stdout.splitlines():
    if line.startswith('password='):
        tok = line[len('password='):]
if not tok:
    print('NO STORED CREDENTIAL')
    sys.exit(1)

req = urllib.request.Request(
    'https://api.github.com/repos/magicrulerr-art/ethra/pages',
    data=json.dumps({'build_type': 'workflow'}).encode(),
    headers={'Authorization': 'Bearer ' + tok,
             'Accept': 'application/vnd.github+json',
             'Content-Type': 'application/json'},
    method='POST')
try:
    with urllib.request.urlopen(req) as r:
        print('created:', r.status, r.read().decode()[:300])
except urllib.error.HTTPError as e:
    print('HTTP', e.code, e.read().decode()[:300])
