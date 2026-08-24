#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dump +/-2 context around every single-line debris region (read-only)."""
import io, sys, os, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
cfg = json.load(open(os.path.join(TOOL_DIR, "arc6_regions.json"), encoding="utf-8"))
CH = os.path.join(os.path.dirname(os.path.dirname(TOOL_DIR)), "content", "story", "chapters")
for f, rs in cfg["regions"].items():
    lines = open(os.path.join(CH, f), encoding="utf-8").read().split("\n")
    print("=" * 70)
    print(f)
    for a, b, label in rs:
        if b > a:
            continue
        print("-" * 60)
        print("L%d %s" % (a, label))
        for i in range(max(0, a - 3), min(len(lines), a + 2)):
            print("  %sL%-4d %s" % (">" if i + 1 == a else " ", i + 1, lines[i][:130]))
