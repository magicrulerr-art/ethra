with open('chapter-arc6-01.md.bak', 'r') as f:
    lines = f.readlines()

# Check line 641 (1-based) in backup
idx = 640
if idx < len(lines):
    print(f"Backup L641: {lines[idx].rstrip()}")
    
# Check surrounding lines for speech-line with quote issues
print("\n=== Lines 630-650 in backup ===")
for i in range(629, 650):
    if i < len(lines):
        line = lines[i].rstrip()
        if '<p class="speech-line">' in line or '<span class="speech">' in line:
            quotes = line.count('"')
            print(f"  L{i+1} (quotes={quotes}): {line[:150]}")
        else:
            print(f"  L{i+1}: {line[:150]}")