"""POST-HOC, descriptive (not in T38-PLAN.md): what riders experience under each arm on the 34 T3.8 test cells.

Written 2026-10-05 after the results were known, to answer the advisor's question "is this system-side or UX?". It
introduces no pass rule. Read-only on the outputs; output files are created with mode "x".
Per run (arms U, C-30, Mplus-30, Mplus-60, V-30), from the final checkpoint (requests, commitmentLedger) and the
adapter's passengerAlighted events:
  demand        requests; served = lifecycle completed; promised = riders with a drop promise (initialPromise row)
  wait          actualPickupTimeMs - arrivalTimeMs (request time), served riders
  ride          alight - actualPickup; door-to-door = alight - arrivalTimeMs
  late drop     alight - first promised drop ETA > 60 s / > 300 s (share of served riders)
  late pickup   actualPickup - first promised pickup ETA > 60 s (share of served riders)
  visible       V_r = sum |z| over drop revisions (z = p - v), share > 60 s (= E2) and > 120 s, promised riders
  jumps         revisions (pickup rows before boarding + drop rows) with |z| >= 60 s; share of promised riders with >= 1
  switches      riders whose ledger records a vehicle switch (visible vehicleSwitchCount > 0 on some revision)
Then per-cell means, totals, and paired cell-bootstrap 95% intervals (B = 10000, random.Random(20261005)) of the
per-cell differences C-30 - U, C-30 - Mplus-30, C-30 - V-30 for the rider metrics. Same riders are NOT compared
(each arm serves its own set); a common-rider check is printed for C-30 vs Mplus-30.
Usage: python -B t38_rider_experience.py <out-prefix>
"""
from __future__ import annotations

import json
import pathlib
import random
import statistics
import sys

HERE = pathlib.Path(__file__).resolve().parent
TANG3 = HERE.parent
for sub in ("sweep", "evidence"):
    sys.path.insert(0, str(TANG3 / sub))
sys.path.insert(0, str(HERE))

import audit_vep  # noqa: E402
import run_t38  # noqa: E402
import sweep_analyze  # noqa: E402
import t38_calibrate  # noqa: E402

ARMS = ("U", "C-30", "Mplus-30", "Mplus-60", "V-30")
CELLS = run_t38.PHASES["test"][1]
METRICS = ("served_share", "wait_mean_s", "wait_p90_s", "ride_mean_s", "door_mean_s", "late_drop60", "late_drop300",
           "late_pick60", "visible60", "visible120", "jump_share", "switch_share")


def p90(values):
    ordered = sorted(values)
    return ordered[max(0, -(-9 * len(ordered) // 10) - 1)] if ordered else None


def run_metrics(run_dir: pathlib.Path):
    transcript = run_dir / "transcript-00.ndjson"
    _, _, state = audit_vep.load(transcript)
    table, summary = audit_vep.audit(transcript)
    _, alighted = sweep_analyze.event_times(transcript)
    requests = {r["requestId"]: r for r in state["requests"]}
    first_pick, first_drop, visible, jumps = {}, {}, {}, {}
    for request, coordinate, _, kind, _, _, _, p, _, _, z, closed in table:
        if kind == "initialPromise":
            (first_pick if coordinate == "pickup" else first_drop)[request] = p
            continue
        if closed:
            continue
        if coordinate == "drop":
            visible[request] = visible.get(request, 0) + abs(z)
        if abs(z) >= 60_000:
            jumps[request] = jumps.get(request, 0) + 1
    switched = set()
    for history in state["commitmentLedger"]:
        for entry in history["entries"]:
            if entry["kind"] != "initialPromise" and entry["deltas"]["visible"].get("vehicleSwitchCount", 0) > 0:
                switched.add(history["requestId"])
    promised = sorted(first_drop)
    served = [r for r in requests if requests[r]["lifecycle"] == "completed"]
    if sum(visible.get(r, 0) for r in promised) != summary["sumDropV"]:
        raise SystemExit(f"{run_dir}: visible drop change does not match the audit")
    waits = [(requests[r]["actualPickupTimeMs"] - requests[r]["arrivalTimeMs"]) / 1000 for r in served]
    rides = [(alighted[r] - requests[r]["actualPickupTimeMs"]) / 1000 for r in served]
    doors = [(alighted[r] - requests[r]["arrivalTimeMs"]) / 1000 for r in served]
    late_drop = [alighted[r] - first_drop[r] for r in served if r in first_drop]
    late_pick = [requests[r]["actualPickupTimeMs"] - first_pick[r] for r in served if r in first_pick]
    share = lambda xs, t: sum(1 for x in xs if x > t) / len(xs) if xs else 0.0  # noqa: E731
    return {
        "requests": len(requests), "served": len(served), "promised": len(promised),
        "served_share": len(served) / len(requests),
        "wait_mean_s": statistics.mean(waits), "wait_p90_s": p90(waits),
        "ride_mean_s": statistics.mean(rides), "door_mean_s": statistics.mean(doors),
        "late_drop60": share(late_drop, 60_000), "late_drop300": share(late_drop, 300_000),
        "late_pick60": share(late_pick, 60_000),
        "visible60": share([visible.get(r, 0) for r in promised], 60_000),
        "visible120": share([visible.get(r, 0) for r in promised], 120_000),
        "jump_share": sum(1 for r in promised if jumps.get(r)) / len(promised),
        "switch_share": len(switched & set(promised)) / len(promised),
        "_served_ids": set(served),
    }


def bootstrap(diffs: list[float]):
    rng = random.Random(20261005)
    m = len(diffs)
    means = sorted(sum(diffs[rng.randrange(m)] for _ in range(m)) / m for _ in range(10_000))
    return statistics.mean(diffs), means[249], means[9750]


def main(prefix: str) -> int:
    data = {}
    for cell in CELLS:
        for arm in ARMS:
            name = t38_calibrate.effective(f"{arm}-{cell}")
            if run_t38.state_of(name) != "status-pass":
                raise SystemExit(f"{name}: {run_t38.state_of(name)}")
            data[(arm, cell)] = run_metrics(run_t38.OUT_ROOT / name)
    out = ["# t38_rider_experience.py (POST-HOC, descriptive; not a pass rule of T38-PLAN.md); 34 test cells"]
    say = out.append
    say("\n== totals over 34 cells: requests / served / promised")
    for arm in ARMS:
        say(f"  {arm:<9} {sum(data[(arm, c)]['requests'] for c in CELLS)} / {sum(data[(arm, c)]['served'] for c in CELLS)}"
            f" / {sum(data[(arm, c)]['promised'] for c in CELLS)}")
    for group, cells in [("all", CELLS)] + [(w, [c for c in CELLS if c.endswith(w)]) for w in ("w07", "w08", "w17")]:
        say(f"\n== per-cell means, {group} ({len(cells)} cells)")
        say("  metric          " + "".join(f"{a:>11}" for a in ARMS))
        for metric in METRICS:
            say(f"  {metric:<15} " + "".join(f"{statistics.mean(data[(a, c)][metric] for c in cells):>11.4f}" for a in ARMS))
    say("\n== paired cell bootstrap of per-cell differences (mean, 95% interval), all 34 cells")
    for other in ("U", "Mplus-30", "V-30"):
        say(f"  C-30 minus {other}:")
        for metric in METRICS:
            mean, lo, hi = bootstrap([data[("C-30", c)][metric] - data[(other, c)][metric] for c in CELLS])
            say(f"    {metric:<15} {mean:+.4f} [{lo:+.4f}, {hi:+.4f}]")
    common = [len(data[("C-30", c)]["_served_ids"] & data[("Mplus-30", c)]["_served_ids"]) for c in CELLS]
    only_c = [len(data[("C-30", c)]["_served_ids"] - data[("Mplus-30", c)]["_served_ids"]) for c in CELLS]
    say(f"\n== C-30 vs Mplus-30 served riders: common {sum(common)}, only under C-30 {sum(only_c)}, "
        f"only under Mplus-30 {sum(len(data[('Mplus-30', c)]['_served_ids'] - data[('C-30', c)]['_served_ids']) for c in CELLS)}")
    with open(f"{prefix}-cells.tsv", "x", encoding="utf-8", newline="\n") as handle:
        keys = ["requests", "served", "promised"] + list(METRICS)
        handle.write("arm\tcell\t" + "\t".join(keys) + "\n")
        for (arm, cell), row in data.items():
            handle.write(f"{arm}\t{cell}\t" + "\t".join(str(row[k]) for k in keys) + "\n")
    text = "\n".join(out) + "\n"
    with open(f"{prefix}-report.txt", "x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    raise SystemExit(main(sys.argv[1]))
