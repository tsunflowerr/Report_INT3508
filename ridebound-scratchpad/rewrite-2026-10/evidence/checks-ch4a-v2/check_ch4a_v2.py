"""Read-only checks for Chapter 4 part A, version 2 (2026-10-12).

Inputs (read only, nothing is modified):
  IVC   tang3/t38/independent/cache/<arm>-<cell>[-rerun1].json  (per-run extraction of the independent verifier,
        iv_extract.py; fields served, alight{requestId: ms}, riders{requestId: {p0_drop, rev[...]}})
  SPLIT tang3/t38/split-t38-v1.json  (the 34 test cells)
  TSV   optimize/codex-debate/claude-work/r21-stage1a/stage1a-2026-10-10-riders.tsv  (second reader; U, C-30, C-120)
Definitions (same as iv_analyze.py section 6 and sweep_analyze): late > T = alighted rider with
  alight - p0_drop > T * 1000 ms (strict); p0 = first drop promise without forecast. Cell mean = unweighted mean over the
  34 test cells of (late riders / alighted riders of the cell). timely T = served - late T, counted on 3.672 requests.
Every registered value is printed next to the recomputed one with OK / FAIL.
Usage: python -B -I check_ch4a_v2.py <out.txt>   (the output file is opened in mode "x")
"""
import csv
import json
import os
import sys

SCR = r"E:\Code\Report_INT3508\ridebound-scratchpad"
CACHE = os.path.join(SCR, r"tang3\t38\independent\cache")
SPLIT = os.path.join(SCR, r"tang3\t38\split-t38-v1.json")
TSV = os.path.join(SCR, r"optimize\codex-debate\claude-work\r21-stage1a\stage1a-2026-10-10-riders.tsv")
ARMS = ("U", "C-30", "Mplus-30", "Mplus-60", "V-30")
THRESH = (30, 60, 120, 300)
out = []
fails = 0


def P(*a):
    out.append(" ".join(str(x) for x in a))


def check(label, got, want):
    global fails
    ok = got == want
    fails += (not ok)
    P(f"  check {label}: got {got} want {want} -> {'OK' if ok else 'FAIL'}")


def load(arm, cell):
    for cand in (f"{arm}-{cell}", f"{arm}-{cell}-rerun1"):
        p = os.path.join(CACHE, cand + ".json")
        if os.path.exists(p):
            with open(p, encoding="utf-8") as fh:
                return cand, json.load(fh)
    raise SystemExit("missing " + arm + " " + cell)


test = json.load(open(SPLIT, encoding="utf-8"))["test"]
P("# check_ch4a_v2.py: lateness vs first promise p0 (no forecast) on the 34 test cells")
P("test cells:", len(test), "| windows:", {w: sum(1 for c in test if c.endswith(w)) for w in ("w07", "w08", "w17")})

res = {}
for arm in ARMS:
    served = alighted = 0
    late = {t: 0 for t in THRESH}
    shares = {t: [] for t in THRESH}
    win_shares = {t: {"w07": [], "w08": [], "w17": []} for t in THRESH}
    pos = {t: 0 for t in THRESH}
    folders = []
    for cell in test:
        name, r = load(arm, cell)
        folders.append(name)
        served += r["served"]
        al = {rid: q for rid, q in r["riders"].items() if rid in r["alight"]}
        alighted += len(al)
        for t in THRESH:
            n = sum(1 for rid, q in al.items() if r["alight"][rid] - q["p0_drop"] > t * 1000)
            late[t] += n
            sh = n / len(al) if al else 0.0
            shares[t].append(sh)
            win_shares[t][cell[-3:]].append(sh)
            pos[t] += (n > 0)
    res[arm] = dict(served=served, alighted=alighted, late=late,
                    mean={t: sum(shares[t]) / len(shares[t]) for t in THRESH}, pos=pos,
                    win={t: {w: (sum(v) / len(v) if v else 0.0) for w, v in win_shares[t].items()} for t in THRESH})
    P(f"\n## {arm}: served {served}; alighted riders with a promise {alighted}; rerun folders "
      f"{[f for f in folders if f.endswith('rerun1')]}")
    for t in THRESH:
        P(f"  late > {t:>3} s: pooled {late[t]}/{alighted} = {100 * late[t] / alighted:.2f}% | cell mean "
          f"{100 * res[arm]['mean'][t]:.2f}% | cells >= 1: {pos[t]}/34 | cell mean by window w07/w08/w17: "
          + " / ".join(f"{100 * res[arm]['win'][t][w]:.2f}%" for w in ('w07', 'w08', 'w17'))
          + f" | timely = served - late = {served - late[t]} of 3672")

P("\n## cross-checks against registered values (IVC reader)")
check("served U", res["U"]["served"], 2434)
check("served C-30", res["C-30"]["served"], 2338)
check("served Mplus-30", res["Mplus-30"]["served"], 2338)
check("served Mplus-60", res["Mplus-60"]["served"], 2347)
check("served V-30", res["V-30"]["served"], 2336)
for arm in ARMS:
    check(f"alighted == served {arm}", res[arm]["alighted"], res[arm]["served"])
check("late60 U (C06)", res["U"]["late"][60], 203)
check("late60 C-30 (C06)", res["C-30"]["late"][60], 76)
check("late60 Mplus-30 (C06)", res["Mplus-30"]["late"][60], 74)
check("late120 U (C07)", res["U"]["late"][120], 102)
check("late120 C-30 (C07)", res["C-30"]["late"][120], 11)
check("late120 Mplus-30 (C07)", res["Mplus-30"]["late"][120], 11)
check("late300 U (C07)", res["U"]["late"][300], 18)
check("late300 C-30 (C07)", res["C-30"]["late"][300], 0)
check("Mplus-30 own break pooled late30 (N-21)", res["Mplus-30"]["late"][30], 289)
check("Mplus-30 own break cell mean, 4 dp (N-21: 14,48%)", round(res["Mplus-30"]["mean"][30], 4), 0.1448)
check("Mplus-30 own break cells >= 1 (C13)", res["Mplus-30"]["pos"][30], 28)
check("Mplus-30 own break w07 cell mean, 4 dp (N-21: 36,53%)", round(res["Mplus-30"]["win"][30]["w07"], 4), 0.3653)
check("Mplus-60 own break pooled late60 (IV: 79/2347)", res["Mplus-60"]["late"][60], 79)
check("Mplus-60 own break cell mean, 4 dp (C13: 4,2%)", round(res["Mplus-60"]["mean"][60], 4), 0.0423)
check("Mplus-60 own break cells >= 1 (C13)", res["Mplus-60"]["pos"][60], 22)

P("\n## second reader: Claude stage-1a rider TSV (completed riders, A - p0 > T ms)")
tsv = {}
with open(TSV, encoding="utf-8", newline="") as fh:
    for row in csv.DictReader(fh, delimiter="\t"):
        if row["lifecycle"] != "completed":
            continue
        d = tsv.setdefault(row["arm"], {"served": 0, **{t: 0 for t in THRESH}, "cells": {}})
        d["served"] += 1
        lat = float(row["A"]) - float(row["p0"])
        cs = d["cells"].setdefault(row["cell"], [0, 0])
        cs[0] += 1
        if lat > 30000:
            cs[1] += 1
        for t in THRESH:
            d[t] += lat > t * 1000
for arm, d in sorted(tsv.items()):
    cm = sum(n / s for s, n in d["cells"].values()) / len(d["cells"])
    P(f"  {arm}: served {d['served']} cells {len(d['cells'])} | late30 {d[30]} late60 {d[60]} late120 {d[120]} "
      f"late300 {d[300]} | late30 cell mean {100 * cm:.2f}% | cells with late30 >= 1 "
      f"{sum(1 for s, n in d['cells'].values() if n > 0)}")
check("TSV served U", tsv["U"]["served"], 2434)
check("TSV served C-30", tsv["C-30"]["served"], 2338)
check("TSV served C-120 (N-06)", tsv["C-120"]["served"], 2387)
check("TSV late60 C-120 (N-06)", tsv["C-120"][60], 132)
check("TSV late60 C-30 == IVC", tsv["C-30"][60], res["C-30"]["late"][60])
check("TSV late30 C-30 == IVC", tsv["C-30"][30], res["C-30"]["late"][30])
check("TSV late30 U == IVC", tsv["U"][30], res["U"]["late"][30])

P(f"\nFAIL count: {fails}")
text = "\n".join(out) + "\n"
with open(sys.argv[1], "x", encoding="utf-8", newline="\n") as fh:
    fh.write(text)
print(text)
