"""Evidence-register addendum 1: does the C-30 per-rider bound hold on the snow afternoon, and how many budget-prune
records do those 8 measured-traffic C-30 runs carry? (OUTLINE-V2 / REVIEW-DECISIONS-R20 section 8 item 4 and the
"132 runs" scope of the cumulative audit.)  Read-only, ONE process, no simulation/build/install; output mode "x".

Runs: the 8 C-30 forecast-off runs of 15/11/2018 14:00 and 15:00 used by optimize/family_snow.py
(run_forecast.SNOW = d20181115-s10-r{1..4}-{w14,w15}; run_forecast.OUT_ROOT = C:/RideBoundData/research/tier3-forecast-v1;
folder C-30-<cell>). The two constants are restated here instead of importing run_forecast.
Readers reused unchanged: audit_vep.load / audit, sweep_analyze.event_times (via forecast_family_a), and
cumulative_decisive_check.analyze (prune classes).
Usage: E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -B check_snow_c30.py
"""
from __future__ import annotations

import collections
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
OPT = pathlib.Path(r"E:/Code/Report_INT3508/ridebound-scratchpad/optimize")
sys.path.insert(0, str(OPT))
sys.path.insert(0, str(OPT / "codex-debate" / "claude-work" / "r13-final-judge"))
import forecast_family_a as fa  # noqa: E402
import cumulative_decisive_check as cdc  # noqa: E402

OUT = HERE / "check-snow-c30-2026-10-11.txt"
ROOT = pathlib.Path(r"C:/RideBoundData/research/tier3-forecast-v1")
SNOW = tuple(f"d20181115-s10-r{r}-{w}" for w in ("w14", "w15") for r in (1, 2, 3, 4))
B = 30_000


def main() -> int:
    out = ["# check_snow_c30.py: 8 C-30 runs of the snow afternoon 15/11/2018 (tier3-forecast-v1), measured traffic"]
    tot = collections.Counter()
    classes = collections.Counter()
    smax = 0
    for cell in SNOW:
        run = ROOT / f"C-30-{cell}"
        tr = run / "transcript-00.ndjson"
        status = json.loads((run / "summary.json").read_text(encoding="utf-8")).get("status")
        table, summary = fa.audit_vep.audit(tr)
        _, alighted = fa.sweep_analyze.event_times(tr)
        first, s = set(), collections.Counter()
        k = collections.Counter()
        for r, coord, seq, kind, pub, v, e, p, x, c, z, closed in table:
            if coord != "drop":
                continue
            if kind == "initialPromise":
                first.add(r)
            else:
                s[r] += abs(c)
                k[r] += c != 0
        judged = cdc.analyze(("snow", "C-30", tr))
        classes.update(judged["candidates"])
        served = sum(1 for r in first if r in alighted)
        m = max((s[r] for r in first), default=0)
        smax = max(smax, m)
        row = {"accepted": len(first), "served": served, "exposed": sum(1 for r in first if s[r] > 0),
               "k2": sum(1 for r in first if k[r] >= 2), "overshoot": sum(1 for r in first if s[r] > B),
               "forced": summary["nonNormalCertificates"], "acknowledged": summary["decisionsAcknowledged"],
               "cum_decisions": judged["decisions_with_cumulative_only"]}
        tot.update(row)
        out.append(f"{cell}: status {status}; {row}; max S {m} ms; prune classes {judged['candidates']}")
    out.append(f"all 8: {dict(tot)}; max S {smax} ms ({smax / 1000:.3f} s); prune classes {dict(classes)} "
               f"(total {sum(classes.values())})")
    text = "\n".join(out) + "\n"
    with open(OUT, "x", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
