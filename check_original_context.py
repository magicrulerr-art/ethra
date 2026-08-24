with open('C:/temp/arc6-01_original.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

debris_lines = [123, 197, 313, 439, 443, 485, 810, 905, 963, 1042]

for ln in debris_lines:
    if ln <= len(lines):
        start = max(0, ln - 3)
        end = min(len(lines), ln + 2)
        print(f"=== Line {ln} (context {start+1}-{end}) ===")
        for i in range(start, end):
            marker = ">>> " if i == ln - 1 else "    "
            print(f"{marker}{i+1:4d}: {lines[i].rstrip()}")
        print()
    else:
        print(f"=== Line {ln}: OUT OF RANGE (max {len(lines)}) ===")
        print()