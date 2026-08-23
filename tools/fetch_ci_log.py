# -*- coding: utf-8 -*-
"""Fetch CI step log + Pages status using the git-stored credential.
The token is never printed."""
import subprocess
import sys
import urllib.request

inp = "protocol=https\nhost=github.com\n\n"
out = subprocess.run(
    ['git', 'credential', 'fill'], input=inp, capture_output=True, text=True)
tok = ''
for line in out.stdout.splitlines():
    if line.startswith('password='):
        tok = line[len('password='):]
if not tok:
    print('NO STORED CREDENTIAL')
    sys.exit(1)

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None

def get(url, auth=True):
    req = urllib.request.Request(url, headers={
        'Accept': 'application/vnd.github+json'})
    if auth:
        req.add_header('Authorization', 'Bearer ' + tok)
    opener = urllib.request.build_opener(NoRedirect)
    try:
        with opener.open(req) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        if e.code in (301, 302, 303, 307) and not auth is False:
            return get(e.headers['Location'], auth=False)
        return e.code, e.read()

st, body = get('https://api.github.com/repos/magicrulerr-art/ethra/actions/jobs/97254791197/logs')
print('logs status:', st)
if st == 200:
    text = body.decode('utf-8', 'replace')
    with open('ci_log.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    print('saved ci_log.txt', len(text), 'bytes')
else:
    print(body[:400])

st2, body2 = get('https://api.github.com/repos/magicrulerr-art/ethra/pages')
print('\npages status:', st2)
print(body2.decode('utf-8', 'replace')[:600])
