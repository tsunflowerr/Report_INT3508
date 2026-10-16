"""Compact views of sweep_analyze.py outputs (read-only).

Usage: python -B show_sweep.py <jobs.tsv> [<paired.tsv>]
Per (world, cell) and level x: completed riders of U / C-x / M⁺-x; each rule's own promise broken share
(C: share C_r > x; M⁺: share A > x) and the other rule's promise on the same arm; forced (M5); E2.
"""
import csv
import sys

rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8"), delimiter="\t"))
by = {(r["arm"], r["world"], r["cell"]): r for r in rows}
bad = [r["job"] for r in rows if r.get("state") != "status-pass" or r.get("audit") != "ok"]
print(f"jobs {len(rows)}; not pass/ok: {len(bad)} {bad[:10]}")


def f(r, k, scale=1.0, digits=3):
    v = r.get(k, "")
    return "-" if v in ("", None) else f"{float(v) / scale:.{digits}f}"


levels = sorted({int(r["level"]) for r in rows if r.get("level")})
for world in sorted({r["world"] for r in rows}):
    for cell in sorted({r["cell"] for r in rows}):
        u = by.get(("U", world, cell))
        if not u:
            continue
        print(f"\n== {world} {cell[-3:]}  U completed {u.get('M1_completed')}  U A>60s {f(u, 'M3_shareA_gt_60s')}  "
              f"U maxA {f(u, 'M3_maxA_ms', 1000, 0)}s")
        print("   x   | done C  M+ | C: C>x  A>x  | M+: A>x  C>x | forced C  M+ | nonNorm M+ | E2 C   M+   | maxA C  M+")
        for x in levels:
            c, m = by.get((f"C-{x}", world, cell)), by.get((f"Mplus-{x}", world, cell))
            if not c or not m:
                continue
            print(f"  {x:>4} | {c.get('M1_completed'):>6} {m.get('M1_completed'):>3} | {f(c, 'M4_shareC_gt_x')} {f(c, 'M3_shareA_gt_x')} | "
                  f"{f(m, 'M3_shareA_gt_x')} {f(m, 'M4_shareC_gt_x')} | {c.get('M5_forcedBreaches'):>5} {m.get('M5_forcedBreaches'):>4} | "
                  f"{f(m, 'M5_nonNormalShare')}      | {f(c, 'M2_E2')} {f(m, 'M2_E2')} | {f(c, 'M3_maxA_ms', 1000, 0):>5} {f(m, 'M3_maxA_ms', 1000, 0):>4}")
if len(sys.argv) > 2:
    pairs = list(csv.DictReader(open(sys.argv[2], encoding="utf-8"), delimiter="\t"))
    print("\npaired C-x vs M+-x: identical completed sets / total, by level")
    for x in levels:
        at = [p for p in pairs if p.get("level") == str(x) and p.get("identicalSets")]
        print(f"  x={x:>4}: identical {sum(p['identicalSets'] == 'True' for p in at)}/{len(at)}; "
              f"both same as U {sum(p['sameAsU_C'] == 'True' and p['sameAsU_Mplus'] == 'True' for p in at)}/{len(at)}")
