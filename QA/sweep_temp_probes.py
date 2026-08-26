# -*- coding: utf-8 -*-
"""Sweep one-off QA probe files (delegated by Ainz 2026-08-25).
DELETES only the known temp patterns; durable QA tooling, reports,
fix scripts, baselines, and QA/_backup_pre_dedup2/ are preserved.
"""
import pathlib, re

WS = pathlib.Path(__file__).resolve().parent.parent.parent  # workspace root
QA = WS / 'ethra_site' / 'QA'

victims = []
# QA/_* probes
victims += list(QA.glob('_*.py')) + list(QA.glob('_*.txt'))
# live-page dumps + scan outputs + one-off probes
for name in ('live_arc1_05.html', 'live_arc2_02.html', 'live_arc2_03.html',
             'scan_arc5.txt', 'scan_arc6_7.txt', 'tmp_corpus_probe.py',
             'diff_2378dae_ch02.txt', 'k1_stitched_scene.txt'):
    p = QA / name
    if p.exists():
        victims.append(p)
# workspace-root strays
for name in ('_verify_v2.py', 'tmp_ch.html'):
    p = WS / name
    if p.exists():
        victims.append(p)

# SAFETY: never touch durable files (paranoia filter on patterns)
keep_pat = re.compile(r'(paraphrase|dupe_paragraph|live_vs_disk|fix_d5|fix_motted|motted_census|refresh_hash|chapter_hashes_baseline|_backup_pre_dedup)', re.I)
safe = [v for v in victims if not keep_pat.search(str(v))]
dropped = [v for v in victims if keep_pat.search(str(v))]

for v in safe:
    v.unlink()
print(f"deleted: {len(safe)} files")
if dropped:
    print(f"SAFETY-KEPT: {[str(d) for d in dropped]}")
# verify survivors
left = sorted(p.name for p in QA.iterdir() if p.name.startswith('_'))
print(f"QA/_* remaining: {left if left else 'none (except _backup_pre_dedup2 dir)'}")
