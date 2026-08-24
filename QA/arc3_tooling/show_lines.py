import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
# usage: python show_lines.py <path> <start> <end> [maxchars]
path, start, end = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
mx = int(sys.argv[4]) if len(sys.argv) > 4 else 140
lines = open(path, encoding="utf-8").read().split("\n")
for i in range(start - 1, min(end, len(lines))):
    t = lines[i]
    if t.strip() == "":
        print("%5d|" % (i + 1))
    else:
        print("%5d| %s" % (i + 1, t[:mx]))
