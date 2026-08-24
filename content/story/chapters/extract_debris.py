with open('chapter-arc6-01.md.bak', 'r') as f:
    lines = f.readlines()

# Check the exact content at each debris line number (1-based from regions.json)
debris_lines = [123, 197, 313, 439, 443, 485, 810, 905, 963, 1042]

for ln in debris_lines:
    idx = ln - 1
    if idx < len(lines):
        content = lines[idx].rstrip('\n')
        print(f"Line {ln}: {content[:120]}")
    else:
        print(f"Line {ln}: OUT OF BOUNDS (file has {len(lines)} lines)")

# Also check a few lines around each for context
print("\n=== Context around L439 ===")
for i in range(425, 445):
    print(f"{i+1:4d}: {lines[i].rstrip()}")

print("\n=== Context around L443 ===")
for i in range(440, 450):
    print(f"{i+1:4d}: {lines[i].rstrip()}")

print("\n=== Context around L485 ===")
for i in range(480, 495):
    print(f"{i+1:4d}: {lines[i].rstrip()}")

print("\n=== Context around L963 ===")
for i in range(958, 970):
    print(f"{i+1:4d}: {lines[i].rstrip()}")

print("\n=== Context around L1042 ===")
for i in range(1037, 1050):
    print(f"{i+1:4d}: {lines[i].rstrip()}")