#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arc VI remediation infra — READ-ONLY.
1) arc6_regions.py  -> arc6_regions.json : canonical debris line-ranges per chapter (split line numbers).
2) arc6_extract_regions.py               : writes arc6_craft_notes_archive.md (blocks only),
                                           prints ALL ranges' text for review, counts debris lines.
3) arc6_verify.py                        : post-pass verifier (debris markers, hum tokens, quote parity,
                                           dup blocks, thought unification, golden text presence).
"""
import re, io, sys, os, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(os.path.dirname(TOOL_DIR))
CH = os.path.join(BASE, "content", "story", "chapters")
UMB = os.path.join(BASE, "content", "story", "chapter-06.md")

# ---------------------------------------------------------------- regions
# (a, b) inclusive 1-based line ranges in the PUBLISHED SPLIT file.
REGIONS = {
 "chapter-arc6-01.md": [
    (123,123,"DRAFT-BEAT Next scene beats >...Lira speaks angrily"),
    (197,197,"DRAFT-LINE Ajani 'well now that's out of the way...' (J2-style reword? NO: E1 rewrite)"),
    (313,313,"DRAFT-HYBRID 'hmm the council worked as designed...'"),
    (439,439,"DRAFT-BEAT *The next scene is a couple of hours after ajani...*"),
    (443,443,"DRAFT-HYBRID 'so these are the ones'"),
    (485,485,"DRAFT-LINE 'Ambassador these are your people...'"),
    (810,810,"DRAFT-BEAT *Let's follow the rest of the cast...*"),
    (905,905,"DIRECTIVE *Now let's see Yvaria, Reva, lira and vex*"),
    (963,963,"DRAFT-HYBRID 'its worse than I thought'"),
    (1042,1042,"DRAFT-BEAT 'theyre brutes, brutes !' (twin arc6-02 L4)"),
 ],
 "chapter-arc6-02.md": [
    (176,176,"DRAFT-BEAT After the meeting ajani goes down... (twin L180)"),
    (352,352,"DRAFT-LINE promotion speech (E2 verify twin)"),
    (486,486,"DIRECTIVE *Let's look at the immediate aftermath...*"),
    (489,489,"SYNOPSIS We are in the gardens..."),
    (585,585,"DRAFT-BEAT after the war council ajani tells Cefiro..."),
    (672,672,"SYNOPSIS We are in the throne room the very next day..."),
    (779,790,"CRAFT-BLOCK The chapter is working on all three fronts..."),
    (895,895,"DIRECTIVE *You can write the next scene...*"),
    (898,898,"DRAFT-BEAT Seris goes to report to ajani..."),
    (948,990,"DUP-BLOCK Tree scene V1 + approval '*I like it, let's write it*' (canon V2 L992-1041)"),
    (1089,1089,"DRAFT-BEAT *Few more days pass...*"),
 ],
 "chapter-arc6-03.md": [
    (75,75,"DIRECTIVE *Let's have ajani exit to work the wall...*"),
    (78,78,"SYNOPSIS A few hours later ajani is helping everyone..."),
    (133,133,"DRAFT-BEAT Then without warning the lament..."),
    (137,228,"DUP-BLOCK L'vat strike V1+V2 (canon V3 L230-272)"),
    (277,277,"DRAFT-BEAT We see a humman mother and daughter..."),
    (318,318,"DRAFT-LINE Ajani very flustered says... (twin L323)"),
    (434,434,"DRAFT-BEAT *Ajani Leads the threx through the city...*"),
    (561,561,"DRAFT-BEAT *Ajani leads l'vat and only l'vat...*"),
    (610,610,"DRAFT-BEAT *Ajani has returned to the throne room...*"),
    (710,710,"DRAFT-LINE Ajani looks towards sylva and says..."),
    (765,765,"DRAFT-BEAT 'Ambassador please tell them Wich direction...'"),
    (866,891,"CRAFT-BLOCK The central achievement... (dup in arc6-04)"),
    (895,895,"SYNOPSIS Let's now follow Cefiro and Kira..."),
    (1047,1047,"DRAFT-BEAT *We still follow him...*"),
 ],
 "chapter-arc6-04.md": [
    (36,145,"DUP-BLOCK dinner V1 (canon V2 L149-313)"),
    (146,146,"DIRECTIVE *We follow them to the dinning room...*"),
    (315,315,"CORRECTIONS-NOTE */corrections 1) the snow paws...*"),
    (318,318,"DRAFT-BEAT Before they have taken ten paces Kira... (twin L323)"),
    (641,641,"DRAFT-BEAT Later at night Nikolai ask Cefiro... (twin L649)"),
    (715,715,"DRAFT-BEAT The next day at breakfast Nikolai announces... (twin L719)"),
    (1101,1101,"DIRECTIVE *Let's follow them in the journey...*"),
    (1105,1105,"DRAFT-BEAT The journey is uneventful..."),
    (1148,1190,"CRAFT-BLOCK Shadow Office copy + arc6 extras"),
    (1194,1194,"DRAFT-BEAT sparring run-on salute"),
    (1221,1221,"DUP-BLOCK Nikolai laugh V1 (canon L1226)"),
    (1230,1264,"SCAFFOLD-BLOCK Feedback on the Combat Choreography"),
    (1270,1270,"DRAFT-BEAT Everyone cheers for Ajani everyone but l'vat..."),
 ],
 "chapter-arc6-05.md": [
    (129,140,"PLANNING-BLOCK Now we enter a sub arc..."),
    (144,144,"SYNOPSIS It's the afternoon of the same day..."),
    (238,248,"DUP-FRAGMENT Maren report V2 (J1 splice: move Nikolai speech into V1)"),
    (253,253,"SYNOPSIS Ok next one is a MASSIVE scene..."),
    (295,316,"CRAFT-BLOCK funeral analysis"),
    (342,342,"SYNOPSIS *Ajani declared the day a mourning day...*"),
    (378,406,"CRAFT-BLOCK throne-room analysis"),
    (410,410,"DRAFT-BEAT Ajani stands and sylva passes him a scroll..."),
    (466,466,"DRAFT-CITATION M'rak lowercase version (canon L474)"),
    (493,511,"DUP-BLOCK M'rak reactions duplicate (canon L470-491)"),
    (515,515,"DRAFT-CITATION Reva (hope her/eveyeone; canon L524)"),
    (576,576,"DRAFT-PROCLAMATION lowercase (twin L584)"),
    (609,651,"DUP-BLOCK Tamsin V1 Sun's Mercy (canon V2 L653-681)"),
    (684,708,"CRAFT-BLOCK proclamation analysis"),
    (717,717,"DRAFT-BEAT Sylva hands another scroll... black..."),
    (771,771,"DRAFT-CITATION Mira (didn't knew; canon L781)"),
    (800,800,"SYNOPSIS As the spirits are high a war horn..."),
    (882,882,"SYNOPSIS Salahim had come to offer a veritable mother load..."),
    (1034,1034,"DRAFT-LINE Nikolai turns and says utterly defeated... (twin L1038)"),
    (1173,1173,"SYNOPSIS Ajani looks at Nikolai confused then to sulheim..."),
 ],
}
# craft blocks for the archive
ARCHIVE = [
 ("chapter-arc6-02.md", 779, 790, "arc6-02 chapter analysis"),
 ("chapter-arc6-03.md", 866, 891, "arc6-03 chapter analysis (duplicated into arc6-04)"),
 ("chapter-arc6-04.md", 1148, 1190, "arc6-04 chapter analysis (arc6-03 copy + extras)"),
 ("chapter-arc6-04.md", 1230, 1264, "arc6-04 combat choreography scaffold"),
 ("chapter-arc6-05.md", 129, 140, "arc6-05 Great Celebration planning"),
 ("chapter-arc6-05.md", 295, 316, "arc6-05 funeral analysis"),
 ("chapter-arc6-05.md", 378, 406, "arc6-05 throne-room analysis"),
 ("chapter-arc6-05.md", 684, 708, "arc6-05 proclamation analysis"),
]
with open(os.path.join(TOOL_DIR, "arc6_regions.json"), "w", encoding="utf-8") as fh:
    json.dump({"regions": REGIONS, "archive_blocks": ARCHIVE}, fh, indent=1, ensure_ascii=False)
print("wrote arc6_regions.json")

# ---------------------------------------------------------------- extract/archive
def read_lines(p):
    return open(p, encoding="utf-8").read().split("\n")

archive_txt = ["# Arc VI craft-notes & planning archive",
 "",
 "Extracted READ-ONLY from the published splits by arc6_extract_regions.py (Demiurge audit tooling)",
 "before deletion. These blocks are author meta-text, not story; preserved here per Ainz-sama's ruling.",
 ""]
for f, a, b, label in ARCHIVE:
    lines = read_lines(os.path.join(CH, f))
    archive_txt.append("---")
    archive_txt.append("## %s — %s L%d-%d" % (label, f, a, b))
    archive_txt.append("")
    archive_txt.extend(lines[a-1:b])
    archive_txt.append("")
with open(os.path.join(TOOL_DIR, "arc6_craft_notes_archive.md"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(archive_txt))
print("wrote arc6_craft_notes_archive.md")

# print all region contents for Demiurge's pre-flight review
out = open(os.path.join(TOOL_DIR, "arc6_regions_dump.txt"), "w", encoding="utf-8")
def p(*a):
    out.write(" ".join(str(x) for x in a) + "\n")
total = 0
for f, rs in REGIONS.items():
    lines = read_lines(os.path.join(CH, f))
    p("=" * 80); p(f)
    for a, b, label in rs:
        n = b - a + 1
        total += n
        p("-" * 70)
        p("L%d-%d (%d lines) %s" % (a, b, n, label))
        for i in range(a, b + 1):
            t = lines[i-1]
            p("  L%-4d %s" % (i, t[:160]))
p("=" * 80)
p("TOTAL DEBRIS LINES: %d" % total)
out.close()
print("wrote arc6_regions_dump.txt")
