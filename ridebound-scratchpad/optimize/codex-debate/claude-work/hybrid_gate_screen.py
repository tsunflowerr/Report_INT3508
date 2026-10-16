"""Zero-run screen for Codex idea 3 (C budget AND a customer deadline p - P0 <= S on the drop promise).
On the saved C-30 (and U) test runs, for each served rider: M = max over drop publications of (p - P0), P0 = first drop
promise. A deadline S would have been reached by the chosen plan for riders with M > S. Split: traffic-only riders
(every drop revision has c == 0) vs riders with some dispatch part. Retrospective only: it cannot tell what the
dispatcher would have done instead. Usage: python -B hybrid_gate_screen.py <out> (mode x)."""
import collections, pathlib, sys
OPT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(OPT))
import forecast_family_a as fa
CELLS = fa.run_t38.PHASES["test"][1]
out = ["# hybrid_gate_screen.py (34 T3.8 test cells; retrospective)"]
for arm in ("C-30", "U"):
    m, disp = {}, collections.defaultdict(bool)
    for cell in CELLS:
        t = fa.run_dir("test", arm, cell) / "transcript-00.ndjson"
        table, _ = fa.audit_vep.audit(t)
        _, alighted = fa.sweep_analyze.event_times(t)
        p0 = {}
        for r, c, s, k, pub, v, e, p, x, cc, z, closed in table:
            if c != "drop" or r not in alighted:
                continue
            key = (cell, r)
            if k == "initialPromise":
                p0[key] = p; m[key] = 0
            else:
                m[key] = max(m[key], p - p0[key]); disp[key] |= cc != 0
    n = len(m)
    out.append(f"\n== {arm}: {n} served riders")
    for S in (30, 60, 120, 180, 240):
        hit = [k for k, v in m.items() if v > S * 1000]
        tr = sum(1 for k in hit if not disp[k])
        out.append(f"  S = {S:>3d} s: riders whose drop promise exceeded P0 + S: {len(hit):4d} ({100 * len(hit) / n:5.2f}%); traffic-only {tr}, with dispatch part {len(hit) - tr}")
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
