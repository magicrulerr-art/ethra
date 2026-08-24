import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
# usage: python peek.py <file> <start> <end>   (1-based inclusive)
p, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
mx = int(sys.argv[4]) if len(sys.argv) > 4 else 200
lines = open(p, encoding="utf-8").read().split("\n")
for i in range(max(0, a-1), min(len(lines), b)):
    t = re.sub(r"<[^>]+>", "", lines[i])
    print("L%-5d %s" % (i+1, t[:mx]))
