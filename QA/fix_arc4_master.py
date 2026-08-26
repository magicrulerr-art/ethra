# -*- coding: utf-8 -*-
"""Arc IV master cleanup on chapter-04.md:
B6 essay, B7a Sylva dupe, B7b profit math, B13 refrains, Sylva staging,
B14 communion surgery, B8/B15 K1 scorpion stitch, champion rename, Maren."""
import pathlib

f = pathlib.Path('ethra_site/content/story/chapter-04.md')
t = f.read_text(encoding='utf-8')
before = (t.count('\n') + 1, len(t.split()))

def rep(old, new, count=1, label=''):
    global t
    n = t.count(old)
    assert n == count, f"[{label}] expected {count}, found {n}: {old[:70]!r}"
    t = t.replace(old, new)

# ---------- B13: refrain trims (keep final at offices paragraph only) ----------
rep("Ajani leaned back on the cold throne. The green fire flickered gently along his claws. The plan was set. The families were bound.",
    "The plan was set. The families were bound.", label='B13-1')
rep("Ajani leaned back on the cold throne. The green fire flickered gently along his claws. The plan was audacious.",
    "The plan was audacious.", label='B13-2')
rep("Ajani leaned back on the cold throne. The green fire flickered gently along his claws. The plan was set. The coin was spoken for.",
    "The coin was spoken for.", label='B13-3')

# ---------- B6: strategy essay excised ----------
e0 = t.index("The Stripe Paws are given logistics and trade")
e1 = t.index("which is not guaranteed.") + len("which is not guaranteed.")
essay = t[e0:e1]
assert "The weaknesses are real" in essay and len(essay.split()) > 500
t = t[:e0].rstrip('\n') + "\n\n\n" + t[e1:].lstrip('\n')
print(f"B6: essay excised ({len(essay.split())} words)")

# ---------- B7a: Sylva near-dupe (keep Flowing Water version) ----------
rep("<div class=\"dialogue-block\">\n<p class=\"speech-line\">Sylva's soft voice was the last to speak. "
    "\"The Motted Paws will study the other races as we have always studied. Their styles. Their techniques. "
    "Their philosophies. Flowing Water adapts to every vessel. We will learn from the Hummans, the Pyrinae, "
    "the Veylar, the Threx. We will take what is useful. We will discard what is not. And we will teach the "
    "other families what we have learned. This is the old way. This is the way of the jaguar\u2014hunt, learn, "
    "adapt, endure.\"</p>\n</div>",
    "", label='B7a')

# ---------- B7b: profit math — Version A block excised, participants 25->10 ----------
rep("<div class=\"dialogue-block\">\nAjani leaned forward on the cold stone. <span class=\"speech\">\"Then let the "
    "distribution be thirty to the crown, fifteen each to the Stripe Paws, the Shadow Paws, and the Motted Paws. "
    "The remaining twenty-five will be split among the participants and the helpers. And the Bright Paws\u2014\"</span> "
    "He paused, the green fire flickering gently along his claws. <span class=\"speech\">\"The Bright Paws will receive "
    "ten percent. Not a full share. Not yet. But enough to begin the long climb back.\"</span>\n</div>",
    "", label='B7b-versionA')
rep("the 25% left will be distributed among those helping and participating",
    "the 10% left will be distributed among those helping and participating", label='B7b-decree')
rep("Twenty-five percent for the participants and helpers.",
    "Ten percent for the participants and helpers.", label='B7b-1')
rep("and that is before the twenty-five for the participants.",
    "and that is before the ten for the participants.", label='B7b-2')
rep("The remaining twenty-five percent to the participants and the helpers.",
    "The remaining ten percent to the participants and the helpers.", label='B7b-3')
rep("The participants will take twenty-five.",
    "The participants will take ten.", label='B7b-4')

# ---------- Sylva staging rewording (break 12w shared prefixes) ----------
rep("Sylva's soft voice carried from beside the throne. \"The Motted Paws accept. We will train our envoys",
    "Beside the throne, Sylva's silver aura brightened. \"The Motted Paws accept. We will train our envoys",
    label='sylva-stage-1')
rep("Sylva's soft voice carried from beside the throne. <span class=\"speech\">\"The Motted Paws have observed Sera.",
    "Sylva spoke from the shadows beside the throne, her voice soft as ever. <span class=\"speech\">\"The Motted Paws have observed Sera.",
    label='sylva-stage-2')

# ---------- B14: communion surgery ----------
# 1. excise Take A (Analysis#1 + razor-hare + near-acceptance)
ta_start = "The roots of the Kyre Tree pulsed in slow, rhythmic waves, the pale green light rippling through the ancient chamber like breath through a sleeping giant. The blossom stirred, its petals unfurling just enough to reveal the amber pool at its heart,"
ta_end = "Not warmth\u2014the Tree was incapable of warmth\u2014but recognition."
assert t.count(ta_start) == 1 and t.count(ta_end) == 1
c0, c1 = t.index(ta_start), t.index(ta_end) + len(ta_end)
communion_takeA = t[c0:c1]
assert "This is a pact worthy of the name." in communion_takeA
assert "you're right and wrong lord of the desert" not in communion_takeA
t = t[:c0].rstrip('\n') + "\n\n\n" + t[c1:].lstrip('\n')
print(f"B14: communion Take A excised ({len(communion_takeA.split())} words)")

# 2. bare blossom staging (post-excision) reworded
rep("That is a description of my nature.'\n\n"
    "The blossom leaned closer, its petals trembling with the intensity of the Tree's focus.\n\n"
    "'And then you ask the greatest thing.",
    "That is a description of my nature.'\n\n"
    "The blossom leaned closer still.\n\n"
    "'And then you ask the greatest thing.", label='B14-stage-bare')

# 3. duplicate blossom staging before pilgrims image reworded
rep("The blossom leaned closer, its petals trembling with the intensity of the Tree's focus. The amber pool swirled with images of pilgrims",
    "The blossom leaned closer. The amber pool swirled with images of pilgrims", label='B14-stage-pilgrims')

# 4. elegant-deception near-dupe reworded (keep first, vary second)
rep("This is elegant. This is sustainable. This is a deception that will endure for generations.'",
    "This is elegant. This is sustainable. The deception deepens with every choice I make.'",
    label='B14-deception')

# 5. essay-voice tail excised
tail0 = t.index("The deception itself is elegant. The Tree will sap the visitors")
tail1 = t.index("their ally.", tail0) + len("their ally.")
tail = t[tail0:tail1]
assert "The strong will come. The Tree will feast." in tail
assert "Ajani stepped onto the raised stone platform" not in tail
t = t[:tail0].rstrip('\n') + "\n\n\n" + t[tail1:].lstrip('\n')
print(f"B14: essay tail excised ({len(tail.split())} words)")

# ---------- B8/B15: K1 scorpion scene — full A->B->D->C stitch ----------
scene = pathlib.Path('ethra_site/QA/k1_stitched_scene.txt').read_text(encoding='utf-8-sig').strip('\n')
s_marker = "\"King Ajani.\"</span> She knelt in the damp sand"
assert t.count(s_marker) == 1
s0 = t.rindex("<div class=\"dialogue-block\">", 0, t.index(s_marker))
e_marker = "It was impossible to tell with Vasha.\n\nThe Bright Paws arrived"
assert t.count(e_marker) == 1
s1 = t.index(e_marker) + len("It was impossible to tell with Vasha.")
removed_k1 = t[s0:s1]
# sanity: all superseded takes must be inside the removed span
for probe in ("You can name it. You can train it. You can ride it through the Flickermarch. That is your right as the king's sister.",
              "What emerged was not a single Pearly Scorpion.",
              "The egg was whole in Ajani's paws",
              "Not a false alarm this time",
              "'Get them off!! Get them off!!'",
              "The Pearly Scorpion is the finest mount on Ethra."):
    assert probe in removed_k1, f"probe missing from removed span: {probe[:50]}"
# sanity: canon beats that must survive live OUTSIDE the removed span
for keep in ("The Bright Paws arrived", "Black Fire and Red Fire reacted as one"):
    assert keep in t[s1:] or keep in t[:s0], f"canon beat lost: {keep}"
t = t[:s0] + scene + t[s1:]
print(f"B8/B15: K1 stitched (removed {len(removed_k1.split())} words, inserted {len(scene.split())})")

# ---------- champion Solen -> Karn ----------
rep("The Bright Paw champion Solen\u2014no relation to the broken heir",
    "The Bright Paw champion Karn\u2014no relation to the broken heir", label='karn-1')
rep("whose name Solen had never learned", "whose name Karn had never learned", label='karn-2')
rep("Solen gritted his teeth and resumed his stance.",
    "Karn gritted his teeth and resumed his stance.", label='karn-3')

# ---------- Maren pronoun ----------
rep("Maren sounds like he'll fit right in",
    "Maren sounds like she'll fit right in", label='maren')

# normalize newline piles
while '\n\n\n\n' in t:
    t = t.replace('\n\n\n\n', '\n\n\n')

f.write_text(t, encoding='utf-8')
after = (t.count('\n') + 1, len(t.split()))
print(f"OK chapter-04.md: lines {before[0]}->{after[0]}, words {before[1]}->{after[1]}")
print("hatch-event check — 'cracked' count:", t.count("The egg cracked"))
print("Solen count (High Priest only):", t.count("Solen"))
