with open('chapter-arc6-04.md', 'r') as f:
    content = f.read()

# Search for Shadow Paw text
idx = content.find('Shadow Paw')
if idx != -1:
    print(f"Found at {idx}: {content[max(0,idx-100):idx+200]}")
else:
    print("Not found")

# Search for "You are a"
idx = content.find('You are a')
if idx != -1:
    print(f"'You are a' at {idx}: {content[max(0,idx-100):idx+200]}")