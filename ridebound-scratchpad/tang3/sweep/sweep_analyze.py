"""Sweep analysis, metrics M1-M8 and the paired table P of SWEEP-PLAN.md (read-only on the sweep outputs).

Reuses the independently verified tools: evidence/audit_vep.py (signed v/e/p rows, oracle totals, E2, CVaR95),
evidence/choice_metrics.py (choice after the gate) and pilot/pilot_frozen.py (forced vehicles). New here, and
tested in test_sweep_analyze.py:
  actual drop time  = simTimeMs of the adapter eventBatch that carries the rider's passengerAlighted event (the
                      same rule gives the Runner's actualPickupTimeMs for boardings: checked 102/102 on a pilot run)
  A_r               = actual drop time - first promised drop ETA (initialPromise ledger entry), completed riders
  C_r               = sum |p - e| over the rider's drop revisions (as in pilot_analyze; row sums == oracle sumDropC)
Promise kept, per arm family at level x: M⁺-x promises A_r <= x; C-x promises C_r <= x. Both shares are computed
for EVERY arm, so each rule is also scored by the other rule's promise.

Usage: python -B sweep_analyze.py jobs <jobs.tsv> | paired <paired.tsv>   (outputs created with mode "x")
"""
from __future__ import annotations

import base64
import json
import pathlib
import statistics
import sys

HERE = pathlib.Path(__file__).resolve().parent
TANG3 = HERE.parent
sys.path.insert(0, str(TANG3 / "evidence"))
sys.path.insert(0, str(TANG3 / "pilot"))

import audit_vep  # noqa: E402
import choice_metrics  # noqa: E402
import pilot_frozen  # noqa: E402
from run_sweep import ARMS, CELLS, LEVELS, OUT_ROOT, WORLD_IDS, effective, state_of  # noqa: E402

THRESHOLDS_S = (60, 300, 900)


def level_of(arm: str):
    return None if arm == "U" else int(arm.split("-")[1])


def event_times(transcript: pathlib.Path):
    """requestId -> simTimeMs of the first adapter batch with its passengerBoarded / passengerAlighted event."""
    boarded, alighted = {}, {}
    with open(transcript, encoding="utf-8") as handle:
        for line in handle:
            record = json.loads(line)
            if record["direction"] != "adapterToRunner":
                continue
            envelope = json.loads(base64.b64decode(record["frameBase64"]))
            if envelope.get("messageType") != "eventBatch":
                continue
            for event in envelope["payload"].get("events", []):
                kind = event.get("eventType")
                if kind == "passengerBoarded":
                    boarded.setdefault(event["payload"]["requestId"], envelope["simTimeMs"])
                elif kind == "passengerAlighted":
                    alighted.setdefault(event["payload"]["requestId"], envelope["simTimeMs"])
    return boarded, alighted


def rider_values(table):
    """Per rider: first promised drop ETA, and C_r (sum |c| over drop revisions)."""
    first, c = {}, {}
    for request, coordinate, _, kind, _, _, _, p, _, cv, _, closed in table:
        if coordinate != "drop":
            continue
        if kind == "initialPromise":
            first[request] = p
            c.setdefault(request, 0)
        elif not closed:
            c[request] = c.get(request, 0) + abs(cv)
    return first, c


def share(numerator, denominator):
    return numerator / denominator if denominator else None


def job_row(name, arm, world, cell):
    used = effective(name)
    row = {"job": name, "arm": arm, "family": arm.split("-")[0], "level": level_of(arm), "world": world,
           "cell": cell, "state": state_of(used), "output": used}
    output = OUT_ROOT / used
    transcript = output / "transcript-00.ndjson"
    if not transcript.exists():
        return row
    summary_file = output / "summary.json"
    if summary_file.exists():
        summary_json = json.loads(summary_file.read_text(encoding="utf-8"))
        row["scenarioSha256"] = summary_json.get("sourceScenarioContentSha256")
        runs = summary_json.get("runs") or [{}]
        row["wallSeconds"] = round(runs[0].get("resources", {}).get("wallMilliseconds", 0) / 1000)
    try:
        table, summary = audit_vep.audit(transcript)
    except audit_vep.EvidenceError as error:
        row["audit"] = f"EVIDENCE-ERROR: {error}"
        return row
    if table is None:
        row["audit"] = "no-final-checkpoint"
        return row
    row["audit"] = "ok"
    first, c = rider_values(table)
    if sum(c.values()) != summary["sumDropC"]:
        row["audit"] = "ROW-ORACLE-MISMATCH"
    boarded, alighted = event_times(transcript)
    completed = {r for r in first if r in alighted}
    lateness = sorted(alighted[r] - first[r] for r in completed)
    x_ms = None if row["level"] is None else row["level"] * 1000
    row.update({
        "requests": summary["requests"],
        "M1_completed": summary["lifecycle"].get("completed", 0),
        "M1_E1": summary["E1ServedShare"],
        "M2_E2": summary["E2ShareDropVAbove60s"],
        "M2_cvar95V_ms": summary["dropVCvar95Ms"],
        "M3_riders": len(lateness),
        "M3_meanA_ms": statistics.mean(lateness) if lateness else None,
        "M3_p95A_ms": lateness[(95 * len(lateness)) // 100] if lateness else None,
        "M3_maxA_ms": lateness[-1] if lateness else None,
        "M4_maxC_ms": max(c.values(), default=0),
        "M5_nonNormalShare": share(summary["nonNormalCertificates"], summary["decisionsAcknowledged"]),
        "M5_forcedRiderShare": share(summary["ridersWithForcedBreach"], summary["promisedRiders"]),
        "M5_forcedBreaches": (summary.get("breaches") or {}).get("forcedReference", 0),
        "M6_latePickups": summary["latePickups"],
        "M6_latePickupMax_ms": summary["latePickupMaxMs"],
        "decisions": summary["decisionsAcknowledged"],
    })
    for t in THRESHOLDS_S:
        row[f"M3_shareA_gt_{t}s"] = share(sum(1 for a in lateness if a > t * 1000), len(lateness))
    if x_ms is not None:
        # Each rule scored by its own promise AND by the other rule's promise, at the arm's level x.
        row["M3_shareA_gt_x"] = share(sum(1 for a in lateness if a > x_ms), len(lateness))
        # C's promise covers every promised rider (completed or not).
        row["M4_shareC_gt_x"] = share(sum(1 for value in c.values() if value > x_ms), len(c))
    choice = choice_metrics.measure(transcript)
    row["M7_gatedMultiShare"] = choice["gatedMultiInsertionShare"]
    row["M7_gatePrunes"] = sum(choice["gatePrunes"].values())
    frozen = pilot_frozen.measure(transcript)
    row["M5_meanForcedFleetShare"] = frozen["meanForcedFleetShare"]
    row["M5_pendingAllForcedShare"] = frozen["pendingAllForcedShare"]
    row["_completedSet"] = sorted(completed)
    row["_A"] = {r: alighted[r] - first[r] for r in completed}
    row["_C"] = {r: c[r] for r in completed}
    return row


def write_tsv(path, rows):
    columns = sorted({k for r in rows for k in r if not k.startswith("_")},
                     key=lambda k: (k not in ("job", "arm", "family", "level", "world", "cell", "state", "audit"), k))
    with open(path, "x", encoding="utf-8", newline="\n") as handle:
        handle.write("\t".join(columns) + "\n")
        for r in rows:
            handle.write("\t".join("" if r.get(c) is None else str(r.get(c)) for c in columns) + "\n")


def selected_worlds():
    """Optional SWEEP_WORLDS=W0,W1 restricts a run (for partial checks while the sweep runs); default all."""
    import os
    chosen = [w for w in os.environ.get("SWEEP_WORLDS", "").split(",") if w]
    unknown = set(chosen) - set(WORLD_IDS)
    if unknown:
        raise SystemExit(f"unknown worlds {sorted(unknown)}")
    return [w for w in WORLD_IDS if not chosen or w in chosen]


def all_rows():
    for world in selected_worlds():
        for cell in CELLS:
            for arm in ARMS:
                yield job_row(f"{arm}-{world}-{cell}", arm, world, cell)


def paired(rows):
    by = {(r["arm"], r["world"], r["cell"]): r for r in rows}
    out = []
    for world in selected_worlds():
        for cell in CELLS:
            u = by.get(("U", world, cell), {})
            for x in LEVELS:
                c, m = by.get((f"C-{x}", world, cell), {}), by.get((f"Mplus-{x}", world, cell), {})
                if "_completedSet" not in c or "_completedSet" not in m:
                    out.append({"world": world, "cell": cell, "level": x, "note": "missing"})
                    continue
                cs, ms = set(c["_completedSet"]), set(m["_completedSet"])
                common = cs & ms
                row = {"world": world, "cell": cell, "level": x, "completedC": len(cs), "completedMplus": len(ms),
                       "identicalSets": cs == ms, "common": len(common), "onlyC": len(cs - ms), "onlyMplus": len(ms - cs),
                       "sameAsU_C": "_completedSet" in u and cs == set(u["_completedSet"]),
                       "sameAsU_Mplus": "_completedSet" in u and ms == set(u["_completedSet"])}
                for label, arm_row in (("C", c), ("Mplus", m)):
                    row[f"common_A_gt_x_{label}"] = sum(1 for r in common if arm_row["_A"][r] > x * 1000)
                    row[f"common_C_gt_x_{label}"] = sum(1 for r in common if arm_row["_C"][r] > x * 1000)
                    row[f"common_maxA_ms_{label}"] = max((arm_row["_A"][r] for r in common), default=None)
                out.append(row)
    return out


def main() -> int:
    both = len(sys.argv) == 4 and sys.argv[1] == "both"
    if not both and (len(sys.argv) != 3 or sys.argv[1] not in ("jobs", "paired")):
        print(__doc__ + "\n       python -B sweep_analyze.py both <jobs.tsv> <paired.tsv>   (one pass)")
        return 2
    rows = list(all_rows())
    if both:
        write_tsv(sys.argv[2], rows)
        write_tsv(sys.argv[3], paired(rows))
        print(f"written {sys.argv[2]} and {sys.argv[3]}")
    elif sys.argv[1] == "jobs":
        write_tsv(sys.argv[2], rows)
        print(f"written {sys.argv[2]}")
    else:
        write_tsv(sys.argv[2], paired(rows))
        print(f"written {sys.argv[2]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
