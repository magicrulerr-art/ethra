# -*- coding: utf-8 -*-
"""serve_pages_test.py — serve _pages/ at the /ethra/ prefix on :8792,
mimicking https://magicrulerr-art.github.io/ethra/ for local verification."""
import http.server
import os
import socketserver
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.join(BASE, '_pages')
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8792


class Handler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        path = path.split('?', 1)[0].split('#', 1)[0]
        if path == '/' or path == '/ethra':
            path = '/ethra/'
        if path.startswith('/ethra/'):
            path = path[len('/ethra/'):]
        elif path.startswith('/ethra'):
            path = path[len('/ethra'):]
        path = path.lstrip('/')
        # directory -> index.html (GitHub Pages behaviour)
        full = os.path.join(ROOT, path.replace('/', os.sep))
        if os.path.isdir(full):
            path = (path.rstrip('/') + '/index.html').lstrip('/')
        return os.path.join(ROOT, path.replace('/', os.sep))

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def log_message(self, *a):
        pass


if __name__ == '__main__':
    with socketserver.ThreadingTCPServer(('127.0.0.1', PORT), Handler) as httpd:
        print('serving _pages at http://127.0.0.1:%d/ethra/' % PORT)
        httpd.serve_forever()
