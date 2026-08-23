# -*- coding: utf-8 -*-
"""run_server.py — P2.4 single-instance management for the Ethra dev server.

Guarantees exactly ONE listener on the port:
  1. PID file (tools/server.pid) names the current instance.
  2. If absent/stale, the actual listener PID is discovered via netstat.
  3. The old instance is killed BY PID (taskkill /pid — never a blanket
     `taskkill /im python.exe`).
  4. A fresh detached `python server.py` is started; its PID is recorded.
  5. Health-checked before the script exits 0.

Usage:  python tools/run_server.py [port]     (default 8790)
"""
import os
import subprocess
import sys
import tempfile
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# machine-local state lives OUTSIDE the repo (a committed PID could name an
# unrelated process on another machine)
PIDFILE = os.path.join(tempfile.gettempdir(), 'ethra_server.pid')
LOG = os.path.join(ROOT, 'server_stdout.log')


def listener_pid(port):
    try:
        out = subprocess.run(['netstat', '-ano'], capture_output=True,
                             text=True).stdout
    except OSError:
        return None
    for line in out.splitlines():
        parts = line.split()
        if len(parts) >= 5 and parts[0] == 'TCP' and parts[3] == 'LISTENING' \
                and parts[1].endswith(':%d' % port):
            try:
                return int(parts[4])
            except ValueError:
                continue
    return None


def alive(pid):
    if not pid:
        return False
    r = subprocess.run(['tasklist', '/fi', 'PID eq %d' % pid, '/nh'],
                       capture_output=True, text=True)
    return str(pid) in r.stdout


def is_our_server(pid):
    """Only a PID whose command line is our server.py may be killed."""
    r = subprocess.run(['powershell', '-NoProfile', '-Command',
                        '(Get-CimInstance Win32_Process -Filter "ProcessId=%d").CommandLine' % pid],
                       capture_output=True, text=True)
    return 'server.py' in (r.stdout or '')


def kill(pid):
    subprocess.run(['taskkill', '/pid', str(pid), '/f'],
                   capture_output=True, text=True)


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else \
        int(os.environ.get('ETHRA_PORT', 8790))

    # ── who holds the port today? ──
    pid = None
    from_port = False
    if os.path.exists(PIDFILE):
        try:
            pid = int(open(PIDFILE).read().strip())
        except (OSError, ValueError):
            pid = None
    actual = listener_pid(port)
    if actual:
        from_port = True
        if actual != pid:
            pid = actual  # PID file stale; the netstat truth wins

    # kill BY PID only: the port holder, or a pidfile PID verified to be our
    # server. Never a blanket process kill.
    if alive(pid) and (from_port or is_our_server(pid)):
        print('killing old instance pid %d' % pid)
        kill(pid)
        for _ in range(20):
            if not listener_pid(port):
                break
            time.sleep(0.25)
        if listener_pid(port):
            print('ERROR: port %d still held after kill' % port)
            return 1
    elif pid:
        print('pidfile pid %d not running; port free' % pid)

    # ── start fresh, detached ──
    env = dict(os.environ, ETHRA_PORT=str(port))
    log = open(LOG, 'ab')
    flags = 0x08000000  # CREATE_NO_WINDOW — console hidden, handles inherited
    proc = subprocess.Popen([sys.executable, 'server.py'], cwd=ROOT,
                            stdout=log, stderr=log, env=env,
                            creationflags=flags)
    with open(PIDFILE, 'w') as f:
        f.write(str(proc.pid))
    print('started server pid %d on port %d' % (proc.pid, port))

    # ── health check ──
    url = 'http://127.0.0.1:%d/api/health' % port
    ok = False
    for _ in range(40):
        time.sleep(0.25)
        try:
            with urllib.request.urlopen(url, timeout=3) as r:
                if r.status == 200:
                    ok = True
                    break
        except OSError:
            pass
    if not ok:
        print('ERROR: server did not become healthy')
        return 1
    # record the ACTUAL listener PID: venv python.exe may be a shim whose
    # child (the real interpreter) holds the port — killing only the shim
    # would orphan the server.
    real = listener_pid(port) or proc.pid
    with open(PIDFILE, 'w') as f:
        f.write(str(real))
    print('health OK (listener pid %d)' % real)
    return 0


if __name__ == '__main__':
    sys.exit(main())
