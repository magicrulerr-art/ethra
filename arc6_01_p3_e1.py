with open(r'content\story\chapters\chapter-arc6-01.md', 'r', encoding='utf-8') as f:
    content = f.read()

# E1: Rewrite the Ajani introduction line (around line 144)
# Current messy text:
# 'well that's understandable, he is odd' - "right, let me make the proper presentation, this Ajani brightmane first of his name, defender of the realm, heir to the black fire and the lightbringer, brother of the deep, caller of spirits, holder of Luxor, king of the wengari salutes Cefiro Silverpelt,   caller of ice, killer of the bho, heir of the great ice city in the North, crown prince of the snow paws our long lost cousins, the crown welcomes you to Styxian cus"

# Replace with natural Ajani voice - formal introduction
old_text = '''<div class="dialogue-block">
<p class="speech-line">'well that's understandable, he is odd' - "right, let me make the proper presentation, this Ajani brightmane first of his name, defender of the realm, heir to the black fire and the lightbringer, brother of the deep, caller of spirits, holder of Luxor, king of the wengari salutes Cefiro Silverpelt,   caller of ice, killer of the bho, heir of the great ice city in the North, crown prince of the snow paws our long lost cousins, the crown welcomes you to Styxian cus"</p>
</div>'''

new_text = '''<div class="dialogue-block">
<p class="speech-line">"Well. That's understandable—he is odd. Right, then. Let me make the proper presentation." He drew himself up. "This is Ajani Brightmane, First of His Name, Defender of the Realm, Heir to the Black Fire and the Lightbringer, Brother of the Deep, Caller of Spirits, Holder of Luxor, King of the Wengari. He salutes Cefiro Silverpelt—Caller of Ice, Killer of the Bho, Heir of the Great Ice City in the North, Crown Prince of the Snow Paws, our long-lost cousins. The Crown welcomes you to Styxiancus."</p>
</div>'''

if old_text in content:
    content = content.replace(old_text, new_text)
    print("E1 rewrite applied successfully")
else:
    print("ERROR: Could not find exact text to replace")
    # Try to find it with more flexible matching
    import re
    match = re.search(r'<div class="dialogue-block">\s*<p class="speech-line">\'well that', content)
    if match:
        print("Found at position:", match.start())
        # Show context
        start = max(0, match.start()-50)
        end = min(len(content), match.start()+500)
        print("Context:", content[start:end])

# Write back
with open(r'content\story\chapters\chapter-arc6-01.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done.")