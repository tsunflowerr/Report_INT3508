"""R16 (2026-10-10) rider replay v2: adds an OUTCOME-FEEDBACK recalibration (a split-conformal-style rolling quantile,
NOT the exact Gibbs-Candes ACI recursion) on top of HIST and BLEND-in. RETROSPECTIVE AND EXPLORATORY (all runs seen
before); parameters fixed before this script was first run: quantile q in {0.8, 0.9}, at least 5 completed riders.
For rider i quoted at t0_i in a cell: completed set J = {j in the same run: A_j <= t0_i} (alights already observed by
the operator); r_j = (A_j - B_j) / (B_j - t0_j) with B = the base method's displayed first drop promise (B_j > t0_j);
rho_i = q-quantile of r_j (nearest rank) if |J| >= 5 else 0; displayed D_i = B_i + max(0, rho_i) * (P0_i - t0_i).
Same populations, reader and metrics as rider_nowcast_replay.py (v1 output kept unchanged). Output mode "x".
Usage: python -B rider_nowcast_replay_v2.py <out-file>
"""
from __future__ import annotations

import pathlib
import statistics
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import rider_nowcast_replay as rv1  # noqa: E402

fa, dl, v1 = rv1.fa, rv1.dl, rv1.v1
BASES = ("HIST", "BLEND-in", "REGB-1.3")
QS = (0.8, 0.9)


def nearest_rank(values, q):
    v = sorted(values)
    return v[max(0, min(len(v) - 1, -(-int(q * 1000) * len(v) // 1000) - 1))]


def main(out):
    sse, alpha, beta, phi = v1.fit_dt()
    params = (alpha, beta, phi)
    lines = ["# rider_nowcast_replay_v2.py (R16; RETROSPECTIVE; outcome-feedback recalibration; unsealed)"]
    data = {}
    for pop, members in rv1.cells().items():
        for cell, run in members:
            day, window = fa.day_of(cell), cell[-3:]
            rs = fa.riders(run, cell, dl.profile(day, window, "causal-no15"))
            for r in rs:
                r["B"] = {b: rv1.displayed(b, day, window, r["t0"], r["P0"], params) for b in BASES}
            for b in BASES:
                for q in QS:
                    key = f"FB{int(q * 100)}@{b}"
                    for r in rs:
                        done = [(x["A"] - x["B"][b]) / (x["B"][b] - x["t0"]) for x in rs
                                if x["A"] <= r["t0"] and x["B"][b] > x["t0"]]
                        rho = nearest_rank(done, q) if len(done) >= 5 else 0.0
                        r.setdefault("D", {})[key] = r["B"][b] + max(0.0, rho) * max(0, r["P0"] - r["t0"])
                for r in rs:
                    r["D"][b] = r["B"][b]
            data[(pop, cell)] = rs
    names = [n for b in BASES for n in [b] + [f"FB{int(q * 100)}@{b}" for q in QS]]
    for pop in ("SNOW", "WEEKDAY"):
        members = [c for (p, c) in data if p == pop]
        lines.append(f"\n## {pop}: {len(members)} cells, {sum(len(data[(pop, c)]) for c in members)} served riders")
        for name in names:
            ys, es, xs, late = [], [], [], 0
            for c in members:
                rs = data[(pop, c)]
                ys.append(sum(r["A"] - r["D"][name] > 60_000 for r in rs) / len(rs))
                es.append(sum(r["A"] - r["D"][name] < -60_000 for r in rs) / len(rs))
                xs.append(statistics.mean(r["D"][name] - r["P0"] for r in rs) / 1000)
                late += sum(r["A"] - r["D"][name] > 60_000 for r in rs)
            lines.append(f"{name:<14} Y60 {100 * statistics.mean(ys):6.2f}% | E60 {100 * statistics.mean(es):5.2f}% | "
                         f"ext {statistics.mean(xs):6.1f} s | late riders {late:>3}")
    text = "\n".join(lines) + "\n"
    with open(out, "x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    raise SystemExit(main(sys.argv[1]))
