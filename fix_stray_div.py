with open(r'content\story\chapters\chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Remove the stray </div> at line 879 (0-based: 878)
# Check what's there
print(f"Line 879: {repr(lines[878])}")
print(f"Line 880: {repr(lines[879])}")
print(f"Line 881: {repr(lines[880])}")

# Remove the stray </div> if it's just that
if '</div>' in lines[878] and lines[878].strip() == '</div>':
    del lines[878]
    print("Removed stray </div>")

# Also check for double blank lines
content = ''.join(lines)
with open(r'content\story\chapters\chapter-arc6-01.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done.")