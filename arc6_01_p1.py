with open(r'content\story\chapters\chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Remove the debris dialogue-block at lines 879-881 (1-based)
# The block is:
# Line 879: <div class="dialogue-block">
# Line 880: <p class="speech-line">It's morning now, ajani has bathed...
# Line 881: </div>

# Convert to 0-based indices
start_idx = 878  # line 879
end_idx = 880    # line 881 (inclusive)

print(f"Removing lines {start_idx+1} to {end_idx+1}:")
for i in range(start_idx, end_idx+1):
    print(f"  {i+1}: {lines[i].rstrip()}")

# Remove the lines
del lines[start_idx:end_idx+1]

# Also clean up any resulting double blank lines
# Join and split to normalize
content = ''.join(lines)
# Write back
with open(r'content\story\chapters\chapter-arc6-01.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done. File updated.")