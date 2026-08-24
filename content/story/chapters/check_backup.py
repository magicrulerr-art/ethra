with open('chapter-arc6-01.md.bak', 'r') as f:
    lines = f.readlines()

# Check L439 area (1-based = index 438)
print('=== L439 area (backup) ===')
for i in range(425, 450):
    print(f'{i+1:4d}: {lines[i].rstrip()}')

print()
print('=== L810 area (backup) ===')
for i in range(800, 820):
    print(f'{i+1:4d}: {lines[i].rstrip()}')

print()
print('=== L905 area (backup) ===')
for i in range(895, 915):
    print(f'{i+1:4d}: {lines[i].rstrip()}')