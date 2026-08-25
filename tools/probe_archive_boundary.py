import urllib.request as u
import urllib.error

for p in ['/archive/images-of-ethra/README.md',
          '/static/images/chapter-arc7-01-v4.png',
          '/static/images/chapter-arc7-01-v8.png',
          '/static/images/chapter-arc6-01-v1.png']:
    try:
        print(p, u.urlopen('http://localhost:8790' + p).getcode())
    except urllib.error.HTTPError as e:
        print(p, e.code)
