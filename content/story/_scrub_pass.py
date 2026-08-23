#!/usr/bin/env python3
"""Surgical meta-fragment scrub of chapter-05.md (umbrella source).
Strips lines 1018-1095 inclusive:  5 DM-analysis headers + bleed-in.
Anchor: Kira weeps -> (5 spacing blanks + meta) -> 7:55 AM scene.
Replacement: Kira weeps -> (2 spacing blanks) -> 7:55 AM scene.
"""
import io, os, hashlib

PATH = r"C:\Users\magic\.copaw\workspaces\default\ethra_site\content\story\chapter-05.md"

with io.open(PATH, "r", encoding="utf-8") as f:
    data = f.read()

before_len = len(data)
print(f"Loaded {before_len} bytes")

# --- anchor: Kira weeps paragraph ---
KIRA = "buried her face in Pearl's pale shell and wept."
# --- end anchor: real 7:55 AM prose ---
PROSE = "It was 7:55 in the morning, the seventh day of the Month of Storms, and the golden dome still shimmered over the capital."

# 1. Find Kira anchor (last prose paragraph)
kira_idx = data.find(KIRA)
assert kira_idx >= 0, "Kira anchor not found"
print(f"Kira anchor: byte {kira_idx}")
# Last character of "." after wept
kira_end = kira_idx + len(KIRA)

# 2. Find the user-planning block start via the unique header
PLANNING_HEADER = "<div class=\"dialogue-block\">\nLet's start the next scene"
plan_idx = data.find(PLANNING_HEADER)
assert plan_idx >= 0, "Planning header not found"
print(f"Planning block: byte {plan_idx}")

# 3. Find the close of user-planning block (the </div> after "the scene ends")
plan_close_idx = data.find("</div>", plan_idx)
assert plan_close_idx >= 0
plan_close_end = plan_close_idx + len("</div>")
print(f"Planning close: byte {plan_close_end}")

# 4. Find the prose AFTER the user-planning block (real 7:55 AM)
prose_idx = data.find(PROSE, plan_close_end)
assert prose_idx >= 0
print(f"7:55 prose starts: byte {prose_idx}")

# But — the user-planning block starts at <div> on a newline, and we don't want to absorb any blank lines that PRECEDE <div> either (those are part of the spacing inside the meta-section).

# Strategy: cut = data[kira_end : prose_idx]
#                       includes: ".\n\n" + (Pacing..Lore Reveals..Emotional Core..A Few Observations..Planning block contents..) + "\n\n\n" before 7:55 prose
# Replacement = "\n\n\n" (preserve three-blank-line spacing before real prose, OR just one blank line)

# Let me preserve: ".\n\n\n" + "It was 7:55...". That means I should replace everything from kira_end to prose_idx with just "\n\n\n"
REPLACEMENT = "\n\n\n"

new_data = data[:kira_end] + REPLACEMENT + data[prose_idx:]
after_len = len(new_data)
print(f"Reduction: {before_len - after_len} bytes ({(before_len - after_len) / before_len * 100:.2f}%)")

# Sanity checks
assert new_data.find(KIRA) == data.find(KIRA), "Kira anchor moved"
assert new_data.find(PROSE) != -1, "Lost 7:55 prose"
# Confirm no survivors of any of the 5 meta-headers
for header in ["**Pacing**", "**Strategy**", "**Lore Reveals**", "**Emotional Core**", "**A Few Observations**"]:
    assert new_data.find(header) == -1, f"{header} still present!"
# Confirm no user-planning bleed-in
assert new_data.find("Let's start the next scene") == -1, "User-planning still present!"

with io.open(PATH, "w", encoding="utf-8") as f:
    f.write(new_data)

print(f"Wrote {after_len} bytes to {PATH}")
print(f"  BEFORE:  {before_len} bytes")
print(f"  REMOVED: {before_len - after_len} bytes")
print(f"  AFTER:   {after_len} bytes")
