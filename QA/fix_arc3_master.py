# -*- coding: utf-8 -*-
"""Arc III master cleanup on chapter-03.md (B4, B5, B12, B9 minors, Solen->Karn).
All ops assertion-guarded. B3 already applied."""
import pathlib

f = pathlib.Path('ethra_site/content/story/chapter-03.md')
t = f.read_text(encoding='utf-8')
before = (t.count('\n') + 1, len(t.split()))

def rep(old, new, count=1, label=''):
    global t
    n = t.count(old)
    assert n == count, f"[{label}] expected {count}, found {n}: {old[:70]!r}"
    t = t.replace(old, new)

# ---------- B4: melee contradictions ----------
rep("He slid to the sand, unconscious but alive. The Shadow Paws had lost their champion.",
    "He slid to the sand, unconscious but alive. For three heartbeats he lay still. Then his "
    "claws scraped against stone, and with the terrible, grinding slowness of a predator that "
    "refuses to die, Thane dragged himself upright, one shoulder hanging wrong, his eyes empty "
    "of everything but the fight.",
    label='B4a')

rep("The basin fell silent.",
    "The basin fell silent. But the mountain did not stay fallen. Rask's great body shuddered, "
    "her foreclaws found the sand, and inch by inch, fighting the poison with every heartbeat, "
    "she rose\u2014swaying, trembling, but standing.",
    label='B4b')

rep("Two champions remained standing: Sylva of the Motted Paws, her silver aura flickering "
    "faintly, her claws stained with Vex's blood. And Sera of the Shadow Paws, her face a ruin, "
    "her dark pelt matted with her own gore, her one good eye blazing with defiance.",
    "Four champions remained standing: Sylva of the Motted Paws, her silver aura flickering "
    "faintly, her claws stained with Vex's blood. Sera of the Shadow Paws, her face a ruin, her "
    "dark pelt matted with her own gore, her one good eye blazing with defiance. Thane of the "
    "Shadow Paws, upright by will alone, his shoulder hanging wrong. And Rask of the Stripe "
    "Paws, swaying with the poison in her blood, but on her feet.",
    label='B4c')

# ---------- B5 + cluster consolidation ----------
rep("Other elders noticed too. Kareth, leaning on his obsidian staff, filed the observation "
    "away for the Shadow Paw council. A king who loved spectacle could be honored with a "
    "demonstration of the Eight Points, a private exhibition of the art's most secret "
    "techniques. Hakar, the old watchman, thought of the northern wall and the weapons stored "
    "there. A king who craved combat might appreciate a blade forged in the old style.",
    "", label='B12-kareth-hakar-1')

rep("And Sylva, still mounted on her war-mount, silver aura flickering, looked down at the "
    "king who had shouted himself hoarse for her victory. The Motted Paws had been silent for "
    "five thousand years. They would not be silent when they chose the gift for the king who "
    "had finally heard them.",
    "", label='B12-sylva-1')

rep("The final pass was a blur of black scales and silver light. Thane was already "
    "out\u2014his injured shoulder had betrayed him on the second turn, and Sylva had guided his "
    "mount to the rail with the same gentle inevitability she had shown in every phase. The "
    "Shadow Paw dismounted without protest, cradling his arm, and the crowd roared as the two "
    "Motted Paws wheeled to face each other.",
    "Across the enclosure, the two Motted Paws wheeled their fire feet to face each other. "
    "Sylva and Torin. Silver against silver.",
    label='B5')

rep("Hakar, the old watchman, thought of the northern wall and the young soldiers who would "
    "flock to the capital to study under the masters.",
    "And Hakar, the old watchman, saw what it would mean: young soldiers flocking to the "
    "capital to study under the masters.",
    label='B12-hakar-epilogue')

# ---------- B9 minors ----------
rep("The arena absorbed the second rule like a blade sinking into flesh.",
    "The arena absorbed the king's words like a blade sinking into flesh.", label='B9-rule2')

rep("his golden mane still dusty from his earlier prostration",
    "his golden mane still dusty from the morning", label='B9-prostration')

# ---------- champion Solen -> Karn (High Priest & broken heir keep their name) ----------
renames = [
    ("a young golden-maned warrior named Solen, no relation to the broken heir",
     "a young golden-maned warrior named Karn, no relation to the broken heir"),
    ("The young warrior Solen murmured", "The young warrior Karn murmured"),
    ("made the young champion Solen go pale", "made the young champion Karn go pale"),
    ("Solen's golden eyes flicked to the throne", "Karn's golden eyes flicked to the throne"),
    ("Rask's blow was swift and merciful. Solen crumpled",
     "Rask's blow was swift and merciful. Karn crumpled"),
    ("Their three champions\u2014Solen and his two companions\u2014",
     "Their three champions\u2014Karn and his two companions\u2014"),
    ("Solen walked on his own feet", "Karn walked on his own feet"),
    ("Solen fell to his knees before the throne", "Karn fell to his knees before the throne"),
    ("She looked at Solen, still kneeling", "She looked at Karn, still kneeling"),
    ("Solen, the broken champion", "Karn, the broken champion"),
]
for old, new in renames:
    rep(old, new, label='rename')

# normalize newline piles created by paragraph deletions (file convention: max 2 blank lines)
while '\n\n\n\n' in t:
    t = t.replace('\n\n\n\n', '\n\n\n')

f.write_text(t, encoding='utf-8')
after = (t.count('\n') + 1, len(t.split()))
print(f"OK: chapter-03.md ops applied. Lines {before[0]}->{after[0]}, "
      f"words {before[1]}->{after[1]}")
# residual checks
import re
assert "The final pass was a blur" in t and t.count("The final pass was a blur") == 1
print("final-pass count:", t.count("The final pass was a blur"))
print("remaining Solen occurrences (should all be High Priest):", t.count("Solen"))
