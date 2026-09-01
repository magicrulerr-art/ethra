import io

p = r"C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapter-06.md"
s = io.open(p, encoding="utf-8").read()

# Anchor: end of the FIRST M'rak block concatenated directly into the start of the SECOND copy.
anchor = "and prepared to speak again.M'rak rose from his knees."
si = s.find(anchor)
if si == -1:
    print("ANCHOR NOT FOUND"); raise SystemExit(1)

# The duplicate second-copy block runs from this "M'rak rose from his knees." up to the NEXT
# "prepared to speak again." that closes it (the second occurrence after si).
dup_start = si + anchor.find("M'rak rose from his knees.")
next_end_marker = "prepared to speak again."
ei = s.find(next_end_marker, dup_start + len("M'rak rose"))
if ei == -1:
    print("END MARKER NOT FOUND"); raise SystemExit(1)
dup_block_end = ei + len(next_end_marker)  # include the closing "prepared to speak again."

removed = s[dup_start:dup_block_end]
s2 = s[:dup_start] + s[dup_block_end:]
print("REMOVED BYTES:", len(removed))
print("snip head:", repr(removed[:120]))
print("snip tail:", repr(removed[-120:]))
print("Heavenly General of the Earth count after:", s2.count("Heavenly General of the Earth"))
print("M'rak rose from his knees count after:", s2.count("M'rak rose from his knees"))
io.open(p, "w", encoding="utf-8").write(s2)
print("WRITTEN")