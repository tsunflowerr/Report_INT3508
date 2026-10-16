"""Independent verifier for the T3.7 pilot report (tang3/T3.7-BAO-CAO-THI-DIEM.md), claims 1-8.

Written from scratch. Reads ONLY raw outputs:
  * E:/RideBoundData/research/tier3-pilot-v1/<job>/summary.json
  * E:/RideBoundData/research/tier3-pilot-v1/<job>/transcript-00.ndjson  (streamed line by line)
  * tang3/pilot/logs/<job>.log                                           (world bin lines)
It imports none of the author's modules (audit_vep, choice_metrics, run_pilot, pilot_*).
Definitions follow tang3/evidence/METRICS-SPEC.md v1.1 and the verification brief.

Usage (python -B, PYTHONDONTWRITEBYTECODE=1):
  python -B verify_pilot.py            compute and print; writes nothing
  python -B verify_pilot.py --write    also writes RESULT.md, jobs.tsv, paired.tsv, world-switch.tsv next to
                                       this script, each opened with mode "x" (never overwrites)
"""
from __future__ import annotations

import base64
import collections
import hashlib
import json
import pathlib
import platform
import re
import sys
import time

OUT_ROOT = pathlib.Path(r"E:/RideBoundData/research/tier3-pilot-v1")
LOG_ROOT = pathlib.Path(r"E:/Code/Report_INT3508/ridebound-scratchpad/tang3/pilot/logs")
HERE = pathlib.Path(__file__).resolve().parent

ARMS = ("U", "C-30", "V-30", "Mplus-30", "M-30")
WORLDS = ("W0", "W1", "W2", "W3", "W4", "W5")
CELLS = ("d20181112-s10-r1-w08", "d20181112-s10-r1-w17")
SHORT = {CELLS[0]: "w08", CELLS[1]: "w17"}
BIN_S = 900
E2_LIMIT_MS = 60_000

# ---------------------------------------------------------------- expected values, copied from the report
# Section 2.6: served (completed) per arm U, C-30, V-30, Mplus-30, M-30; E2 C-30 (num, den); E2 V-30 (num, den)
EXPECTED_SERVED = {
    ("W0", "w08"): ((102, 97, 97, 97, 97), (0, 97), (0, 97)),
    ("W1", "w08"): ((87, 82, 80, 82, 79), (15, 82), (15, 80)),
    ("W2", "w08"): ((85, 86, 79, 85, 79), (32, 86), (24, 79)),
    ("W3", "w08"): ((108, 108, 108, 108, 108), (1, 108), (1, 108)),
    ("W4", "w08"): ((96, 94, 90, 92, 92), (12, 94), (5, 90)),
    ("W5", "w08"): ((92, 90, 87, 90, 89), (2, 90), (2, 87)),
    ("W0", "w17"): ((99, 95, 95, 95, 95), (0, 95), (0, 95)),
    ("W1", "w17"): ((83, 81, 78, 81, 78), (15, 81), (14, 78)),
    ("W2", "w17"): ((79, 79, 69, 78, 69), (36, 79), (29, 69)),
    ("W3", "w17"): ((107, 107, 103, 107, 102), (6, 107), (7, 103)),
    ("W4", "w17"): ((92, 87, 86, 86, 85), (12, 87), (8, 86)),
    ("W5", "w17"): ((100, 99, 97, 99, 97), (2, 99), (1, 97)),
}
# Section 2.8: (common, commonAbove60 C, commonAbove60 V, onlyC, onlyC above 60, onlyV, onlyV above 60)
EXPECTED_PAIRED = {
    ("W1", "w08"): (70, 15, 15, 12, 0, 10, 0),
    ("W2", "w08"): (74, 28, 21, 12, 4, 5, 3),
    ("W4", "w08"): (82, 11, 5, 12, 1, 8, 0),
    ("W5", "w08"): (81, 2, 2, 9, 0, 6, 0),
    ("W1", "w17"): (75, 15, 14, 6, 0, 3, 0),
    ("W2", "w17"): (66, 26, 26, 13, 10, 3, 3),
    ("W3", "w17"): (103, 6, 7, 4, 0, 0, 0),
    ("W4", "w17"): (75, 12, 7, 12, 0, 11, 1),
    ("W5", "w17"): (95, 2, 1, 4, 0, 2, 0),
}
EXPECTED_IDENTICAL_SETS = (("W0", "w08"), ("W0", "w17"), ("W3", "w08"))
EXPECTED_MAJORITY = {"C-30": 0, "V-30": 5, "Mplus-30": 2, "M-30": 5}


def job_name(arm, world, cell):
    return f"{arm}-{world}-{cell}"


def all_jobs():
    for cell in CELLS:
        for world in WORLDS:
            for arm in ARMS:
                yield job_name(arm, world, cell), arm, world, cell


# ---------------------------------------------------------------- transcript scan
def summarize_decision(payload):
    body = (payload.get("certificate") or {}).get("body") or {}
    non_normal = body.get("normalOperation") is False          # spec v1.1 item 5
    forced = frozenset(w.get("vehicleId") for w in (body.get("witnesses") or [])
                       if w.get("stage") == "forcedReference")
    evidence = (payload.get("solver") or {}).get("executionEvidence")
    if evidence:
        generation = evidence["generation"]
        fleet = tuple(loss.get("vehicleId") for loss in generation["vehicleLosses"])
        pending = generation["totalPendingRequestCount"]
    else:
        fleet, pending = None, None
    return non_normal, forced, fleet, pending


def scan_transcript(path):
    decisions, order = {}, []
    acknowledged = set()
    stats = collections.Counter()
    last_checkpoint = None
    with open(path, "rb") as handle:
        for raw in handle:
            if not raw.strip():
                stats["blankLines"] += 1
                continue
            stats["lines"] += 1
            record = json.loads(raw)
            frame = base64.b64decode(record["frameBase64"], validate=True)
            if hashlib.sha256(frame).hexdigest() != record.get("frameSha256"):
                stats["frameShaMismatch"] += 1
            if "frameLengthBytes" in record and record["frameLengthBytes"] != len(frame):
                stats["frameLengthMismatch"] += 1
            envelope = json.loads(frame)
            kind, direction = envelope.get("messageType"), record.get("direction")
            if direction == "runnerToAdapter" and kind == "decision":
                payload = envelope["payload"]
                key = payload["decisionHash"]
                summary = summarize_decision(payload)
                if key in decisions:
                    stats["duplicateDecisionFrames"] += 1
                    if decisions[key] != summary:
                        stats["duplicateDecisionConflicts"] += 1
                else:
                    decisions[key] = summary
                    order.append(key)
            elif direction == "adapterToRunner" and kind == "decisionApplied":
                key = envelope["payload"]["decisionHash"]
                if key in decisions:            # counts only after its decision (spec v1.1 item 4)
                    if key in acknowledged:
                        stats["duplicateAcks"] += 1
                    acknowledged.add(key)
                else:
                    stats["ackWithoutPriorDecision"] += 1
            elif direction == "runnerToAdapter" and kind == "checkpoint":
                last_checkpoint = envelope
    return decisions, order, acknowledged, stats, last_checkpoint


# ---------------------------------------------------------------- per-rider promise history
def riders_from_ledger(ledger, anomalies):
    """requestId -> (C, X, V) of the DROP coordinate over revision entries (initialPromise contributes 0)."""
    riders = {}
    for history in ledger:
        rid = history["requestId"]
        if rid in riders:
            anomalies["duplicateLedgerRequestId"] += 1
        entries = history.get("entries") or []
        if not entries:
            anomalies["emptyHistory"] += 1
            continue
        big_c = big_x = big_v = 0
        previous_p = None
        has_drop = False
        for index, entry in enumerate(entries):
            kind = entry.get("kind")
            if index == 0 and kind != "initialPromise":
                anomalies["firstEntryNotInitial"] += 1
            if index > 0 and kind != "revision":
                anomalies["laterEntryNotRevision"] += 1
            p = entry["publishedPromise"]["projection"]["dropEtaMs"]
            if p is not None:
                has_drop = True
            if kind == "revision":
                v = entry["previousPromise"]["projection"]["dropEtaMs"]
                e = entry["exogenousProjection"]["dropEtaMs"]
                c, x, z = p - e, e - v, p - v
                big_c += abs(c)
                big_x += abs(x)
                big_v += abs(z)
                if v != previous_p:
                    anomalies["dropChainBreak"] += 1
                deltas = entry.get("deltas") or {}
                if (deltas.get("exogenous", {}).get("dropEtaTotalMs") != abs(x)
                        or deltas.get("decisionInduced", {}).get("dropEtaTotalMs") != abs(c)
                        or deltas.get("visible", {}).get("dropEtaTotalMs") != abs(z)):
                    anomalies["dropDeltaMismatch"] += 1
            previous_p = p
        if not has_drop:
            anomalies["historyWithoutDrop"] += 1
            continue
        riders[rid] = (big_c, big_x, big_v)
    return riders


def analyze_job(name):
    out = {"job": name}
    summary_path = OUT_ROOT / name / "summary.json"
    out["summaryExists"] = summary_path.exists()
    out["status"] = json.loads(summary_path.read_text(encoding="utf-8")).get("status") if out["summaryExists"] else None
    out["runExists"] = (OUT_ROOT / name / "run-00.json").exists()
    transcript = OUT_ROOT / name / "transcript-00.ndjson"
    if not transcript.exists():
        out["finalCheckpoint"] = False
        return out, None
    decisions, order, acknowledged, stats, checkpoint = scan_transcript(transcript)
    out.update({k: stats.get(k, 0) for k in ("lines", "frameShaMismatch", "frameLengthMismatch",
                                             "duplicateDecisionFrames", "duplicateDecisionConflicts",
                                             "duplicateAcks", "ackWithoutPriorDecision")})
    out["decisionsSent"] = len(order)
    out["decisionsAcknowledged"] = len(acknowledged)
    out["decisionsUnacknowledged"] = len(order) - len(acknowledged)
    acked = [decisions[k] for k in order if k in acknowledged]
    out["nonNormal"] = sum(1 for d in acked if d[0])
    out["nonNormalShare"] = out["nonNormal"] / len(acked) if acked else None

    # frozen vehicles (claim 5)
    with_evidence = [d for d in acked if d[2] is not None]
    out["decisionsWithEvidence"] = len(with_evidence)
    out["fleetSizes"] = ",".join(str(s) for s in sorted({len(d[2]) for d in with_evidence}))
    out["forcedNotInFleet"] = sum(1 for d in with_evidence if not d[1] <= set(d[2]))
    out["forcedNoneVehicleId"] = sum(1 for d in acked if None in d[1])
    shares = [len(d[1]) / len(d[2]) for d in with_evidence if d[2]]
    out["meanForcedFleetShare"] = sum(shares) / len(shares) if shares else None
    pend = [d for d in with_evidence if d[3] and d[3] > 0]
    out["pendingDecisions"] = len(pend)
    out["pendingAllForced"] = sum(1 for d in pend if d[2] and set(d[2]) <= d[1])
    out["pendingHalfForced"] = sum(1 for d in pend if d[2] and 2 * len(d[1] & set(d[2])) >= len(d[2]))
    out["pendingAllForcedShare"] = out["pendingAllForced"] / len(pend) if pend else None
    out["pendingHalfForcedShare"] = out["pendingHalfForced"] / len(pend) if pend else None

    out["finalCheckpoint"] = bool(checkpoint and ((checkpoint.get("payload") or {}).get("content") or {})
                                  .get("onlineState") is not None)
    if not out["finalCheckpoint"]:
        return out, None
    state = checkpoint["payload"]["content"]["onlineState"]
    requests = state.get("requests") or []
    lifecycle = collections.Counter(r.get("lifecycle") for r in requests)
    out["requests"] = len(requests)
    out["distinctRequestIds"] = len({r.get("requestId") for r in requests})
    out["completed"] = lifecycle.get("completed", 0)
    out["lifecycle"] = ";".join(f"{k}={v}" for k, v in sorted(lifecycle.items(), key=lambda kv: str(kv[0])))
    anomalies = collections.Counter()
    ledger = state.get("commitmentLedger") or []
    riders = riders_from_ledger(ledger, anomalies)
    out["ledgerHistories"] = len(ledger)
    out["promisedRiders"] = len(riders)
    out["E2num"] = sum(1 for (_, _, v) in riders.values() if v > E2_LIMIT_MS)
    out["maxRiderDropCMs"] = max((c for (c, _, _) in riders.values()), default=0)
    out["sumDropC"] = sum(c for (c, _, _) in riders.values())
    out["sumDropX"] = sum(x for (_, x, _) in riders.values())
    out["sumDropV"] = sum(v for (_, _, v) in riders.values())
    completed_ids = {r.get("requestId") for r in requests if r.get("lifecycle") == "completed"}
    out["promisedNotCompleted"] = len(set(riders) - completed_ids)
    out["completedNotPromised"] = len(completed_ids - set(riders))
    for key in ("duplicateLedgerRequestId", "emptyHistory", "firstEntryNotInitial", "laterEntryNotRevision",
                "dropChainBreak", "dropDeltaMismatch", "historyWithoutDrop"):
        out[key] = anomalies.get(key, 0)
    incident = state.get("incidentLedger") or {}
    breaches = incident.get("breaches") or []
    kinds = collections.Counter(b.get("kind") or "operationalIncident" for b in breaches)
    out["breaches"] = ";".join(f"{k}={v}" for k, v in sorted(kinds.items()))
    out["forcedBreaches"] = kinds.get("forcedReference", 0)
    out["ridersWithForcedBreach"] = len({b.get("requestId") for b in breaches if b.get("kind") == "forcedReference"})
    late = incident.get("latePickups") or []
    out["latePickups"] = len(late)
    lateness = [lp["actualPickupMs"] - lp["latestPickupMs"] for lp in late]
    out["latePickupMaxMs"] = max(lateness, default=0)
    out["latePickupNonPositive"] = sum(1 for d in lateness if d <= 0)
    return out, riders


# ---------------------------------------------------------------- logs (claim 7)
BIN_LINE = re.compile(r"^\[world\] t=\s*(?P<t>-?\d+)s bin=(?P<bin>\d+) edges=(?P<edges>\d+) "
                      r"factor=\[(?P<lo>[^,\]]+), (?P<hi>[^\]]+)\]\s*$")
APPLIED_LINE = re.compile(r"^\[world\] bin changes applied: (?P<n>\d+)\s*$")


def parse_log(path):
    text = path.read_text(encoding="utf-8", errors="replace").splitlines()
    first = text[0] if text else ""
    match = re.match(r"^returncode=(-?\d+)", first)
    bins, applied, candidates = [], None, 0
    for line in text:
        if line.startswith("[world] t="):
            candidates += 1
        m = BIN_LINE.match(line)
        if m:
            bins.append((int(m["bin"]), int(m["t"]), int(m["edges"]), m["lo"].strip(), m["hi"].strip()))
        m = APPLIED_LINE.match(line)
        if m:
            applied = int(m["n"])
    return {"returncode": int(match.group(1)) if match else None, "bins": bins, "applied": applied,
            "binLineCandidates": candidates}


def spread_analysis(logs, arms, require_all):
    """Per (world, cell, bin): spread of switch time across `arms`. require_all: only bins every arm reached."""
    worst, rows, factor_diff = None, [], []
    for cell in CELLS:
        for world in WORLDS:
            by_arm = {arm: {b[0]: b for b in logs[job_name(arm, world, cell)]["bins"]} for arm in arms}
            all_bins = sorted(set().union(*[set(v) for v in by_arm.values()]))
            for k in all_bins:
                reached = {arm: by_arm[arm][k] for arm in arms if k in by_arm[arm]}
                if require_all and len(reached) != len(arms):
                    continue
                if len(reached) < 2:
                    continue
                times = [b[1] for b in reached.values()]
                spread = max(times) - min(times)
                factors = {(b[3], b[4]) for b in reached.values()}
                if len(factors) != 1:
                    factor_diff.append((world, SHORT[cell], k, sorted(factors)))
                rows.append((world, SHORT[cell], k, spread))
                if worst is None or spread > worst[0]:
                    worst = (spread, [(world, SHORT[cell], k)])
                elif spread == worst[0]:
                    worst[1].append((world, SHORT[cell], k))
    return worst, rows, factor_diff


# ---------------------------------------------------------------- claims
class Claim:
    def __init__(self, number, text):
        self.number, self.text, self.checks, self.not_verified, self.notes = number, text, [], [], []

    def check(self, label, expected, actual, ok=None):
        self.checks.append((label, expected, actual, (expected == actual) if ok is None else ok))

    def verdict(self):
        if self.not_verified:
            return "NOT VERIFIED"
        return "MATCH" if all(c[3] for c in self.checks) else "MISMATCH"


def fmt3(x):
    return "None" if x is None else f"{x:.3f}"


def main():
    write = "--write" in sys.argv[1:]
    started = time.time()
    expected_jobs = [j[0] for j in all_jobs()]
    present = sorted(p.name for p in OUT_ROOT.iterdir() if p.is_dir())
    jobs, riders = {}, {}
    for name, arm, world, cell in all_jobs():
        t0 = time.time()
        row, rider_map = analyze_job(name)
        row.update({"arm": arm, "world": world, "cell": SHORT[cell]})
        jobs[name], riders[name] = row, rider_map
        print(f"{name:<34} {time.time() - t0:5.1f}s acked={row.get('decisionsAcknowledged')} "
              f"nn={row.get('nonNormal')} completed={row.get('completed')} promised={row.get('promisedRiders')} "
              f"E2={row.get('E2num')} late={row.get('latePickups')}", flush=True)
    logs = {name: parse_log(LOG_ROOT / f"{name}.log") for name in expected_jobs if (LOG_ROOT / f"{name}.log").exists()}

    claims = []
    # ---- claim 1
    c1 = Claim(1, 'All 60 summary.json have status "pass"; all 60 have a final checkpoint.')
    c1.check("job directories present (expected 60 named jobs)", 60, sum(1 for j in expected_jobs if j in present))
    c1.check("extra directories in output root", [], sorted(set(present) - set(expected_jobs)))
    c1.check('summary.json status == "pass"', 60, sum(1 for j in jobs.values() if j.get("status") == "pass"))
    c1.check("final runnerToAdapter checkpoint with onlineState", 60,
             sum(1 for j in jobs.values() if j.get("finalCheckpoint")))
    claims.append(c1)

    # ---- claim 2
    c2 = Claim(2, "Each cell has 108 requests; served (completed) per arm/world/cell = table 2.6; "
                  "E2 numerators/denominators of C-30 and V-30 = table 2.6.")
    c2.check("jobs with exactly 108 requests (and 108 distinct requestIds)", 60,
             sum(1 for j in jobs.values() if j.get("requests") == 108 and j.get("distinctRequestIds") == 108))
    served_mismatch, e2_mismatch = [], []
    for (world, short), (served, e2c, e2v) in EXPECTED_SERVED.items():
        cell = CELLS[0] if short == "w08" else CELLS[1]
        for arm, want in zip(ARMS, served):
            got = jobs[job_name(arm, world, cell)].get("completed")
            if got != want:
                served_mismatch.append(f"{arm} {world} {short}: report {want}, raw {got}")
        for arm, want in (("C-30", e2c), ("V-30", e2v)):
            j = jobs[job_name(arm, world, cell)]
            got = (j.get("E2num"), j.get("promisedRiders"))
            if got != want:
                e2_mismatch.append(f"{arm} {world} {short}: report {want[0]}/{want[1]}, raw {got[0]}/{got[1]}")
    c2.check("served cells differing from table 2.6 (60 cells)", [], served_mismatch)
    c2.check("E2 num/den differing from table 2.6 (24 cells)", [], e2_mismatch)
    claims.append(c2)

    # ---- claim 3
    c30 = [j for j in jobs.values() if j["arm"] == "C-30"]
    c3 = Claim(3, "C-30: 0 non-normal decisions and 0 forcedReference breaches in 12/12; "
                  "largest per-rider drop C = 19118 ms (<= 30000).")
    c3.check("C-30 jobs", 12, len(c30))
    c3.check("C-30 acknowledged decisions with normalOperation=false (sum over 12)", 0, sum(j["nonNormal"] for j in c30))
    c3.check("C-30 forcedReference breaches (sum over 12)", 0, sum(j["forcedBreaches"] for j in c30))
    top = max(c30, key=lambda j: j["maxRiderDropCMs"])
    c3.check(f"largest per-rider drop C over C-30 (at {top['job']})", 19118, top["maxRiderDropCMs"])
    c3.check("that value <= 30000", True, top["maxRiderDropCMs"] <= 30000)
    claims.append(c3)

    # ---- claim 4
    c4 = Claim(4, "Episodes (of 12) with non-normal share > 0.5: C-30 0, V-30 5, Mplus-30 2, M-30 5; "
                  "max V-30 share 0.835 at V-30-W4-...-w17.")
    for arm, want in EXPECTED_MAJORITY.items():
        rows = [j for j in jobs.values() if j["arm"] == arm]
        c4.check(f"{arm} episodes with share > 0.5", want, sum(1 for j in rows if j["nonNormalShare"] > 0.5))
    v30 = [j for j in jobs.values() if j["arm"] == "V-30"]
    vmax = max(v30, key=lambda j: j["nonNormalShare"])
    c4.check(f"max V-30 share (3 dp; exact {vmax['nonNormal']}/{vmax['decisionsAcknowledged']} = "
             f"{vmax['nonNormalShare']!r})", "0.835", fmt3(vmax["nonNormalShare"]))
    c4.check("job with max V-30 share", job_name("V-30", "W4", CELLS[1]), vmax["job"])
    claims.append(c4)

    # ---- claim 5
    c5 = Claim(5, "Mean forced/fleet: max over V-30 is 0.298 at V-30-W2-...-w17; share of pending decisions "
                  "with every vehicle forced: 0 for V-30-W2-...-w17, max 0.056 over all jobs (Mplus-30-W2-...-w17).")
    vfz = max(v30, key=lambda j: j["meanForcedFleetShare"])
    c5.check(f"max V-30 meanForcedFleetShare (3 dp; exact {vfz['meanForcedFleetShare']!r})", "0.298",
             fmt3(vfz["meanForcedFleetShare"]))
    c5.check("job with that max", job_name("V-30", "W2", CELLS[1]), vfz["job"])
    target = jobs[job_name("V-30", "W2", CELLS[1])]
    c5.check("V-30-W2-w17 pending decisions with every vehicle forced (count, exact)", 0, target["pendingAllForced"])
    allmax = max(jobs.values(), key=lambda j: j["pendingAllForcedShare"] or 0)
    ties = sorted(j["job"] for j in jobs.values() if j["pendingAllForcedShare"] == allmax["pendingAllForcedShare"])
    c5.check(f"max pendingAllForcedShare over all 60 jobs (3 dp; exact {allmax['pendingAllForced']}/"
             f"{allmax['pendingDecisions']})", "0.056", fmt3(allmax["pendingAllForcedShare"]))
    c5.check("job(s) with that max", [job_name("Mplus-30", "W2", CELLS[1])], ties)
    c5.check("decisions whose forced vehicles are not all in vehicleLosses (all jobs)", 0,
             sum(j["forcedNotInFleet"] for j in jobs.values()))
    claims.append(c5)

    # ---- claim 6
    c6 = Claim(6, "Paired C-30 vs V-30 by requestId: common/onlyC/onlyV and '>60 s' counts = table 2.8; W0 (both "
                  "cells) and W3 morning have identical rider sets (and equal >60 s counts).")
    paired_rows, paired_mismatch = [], []
    for cell in CELLS:
        for world in WORLDS:
            rc, rv = riders[job_name("C-30", world, cell)], riders[job_name("V-30", world, cell)]
            common = set(rc) & set(rv)
            only_c, only_v = set(rc) - set(rv), set(rv) - set(rc)
            got = (len(common), sum(1 for r in common if rc[r][2] > E2_LIMIT_MS),
                   sum(1 for r in common if rv[r][2] > E2_LIMIT_MS), len(only_c),
                   sum(1 for r in only_c if rc[r][2] > E2_LIMIT_MS), len(only_v),
                   sum(1 for r in only_v if rv[r][2] > E2_LIMIT_MS))
            key = (world, SHORT[cell])
            paired_rows.append((world, SHORT[cell], len(rc), len(rv)) + got)
            if key in EXPECTED_PAIRED:
                if got != EXPECTED_PAIRED[key]:
                    paired_mismatch.append(f"{world} {SHORT[cell]}: report {EXPECTED_PAIRED[key]}, raw {got}")
            elif key in EXPECTED_IDENTICAL_SETS:
                if not (got[3] == 0 and got[5] == 0 and got[1] == got[2]):
                    paired_mismatch.append(f"{world} {SHORT[cell]}: report identical sets & equal >60 counts, raw {got}")
            else:
                paired_mismatch.append(f"{world} {SHORT[cell]}: not covered by the report table, raw {got}")
    c6.check("(world, cell) rows differing from table 2.8 / identical-set statement (12 rows)", [], paired_mismatch)
    claims.append(c6)

    # ---- claim 7
    c7 = Claim(7, "World switch: max lag 149 s (W4 w08 bin 3); max cross-arm spread 131 s (W5 w17 bin 8); "
                  "C-30/V-30 only 130 s; factor ranges identical across arms on bins all arms reached.")
    missing_logs = [j for j in expected_jobs if j not in logs]
    if missing_logs:
        c7.not_verified.append(f"missing logs: {missing_logs}")
    else:
        lag_worst, lag_where = None, []
        for name, arm, world, cell in all_jobs():
            for k, t, *_ in logs[name]["bins"]:
                if k == 0:
                    continue
                lag = t - k * BIN_S
                if lag_worst is None or lag > lag_worst:
                    lag_worst, lag_where = lag, [(arm, world, SHORT[cell], k)]
                elif lag == lag_worst:
                    lag_where.append((arm, world, SHORT[cell], k))
        c7.check("max lag over all bins >= 1 of all 60 logs (s)", 149, lag_worst)
        c7.check("where (arm, world, cell, bin)", "W4 w08 bin 3",
                 ", ".join(f"{a} {w} {c} bin {k}" for a, w, c, k in lag_where),
                 ok=all((w, c, k) == ("W4", "w08", 3) for _, w, c, k in lag_where))
        # Same lag, restricted to bins that all 5 arms reached in that (world, cell).
        common_lag, common_where, beyond = None, [], []
        for cell in CELLS:
            for world in WORLDS:
                seqs = {arm: {b[0]: b[1] for b in logs[job_name(arm, world, cell)]["bins"]} for arm in ARMS}
                common_bins = set.intersection(*[set(s) for s in seqs.values()])
                for arm in ARMS:
                    for k, t in sorted(seqs[arm].items()):
                        if k == 0:
                            continue
                        lag = t - k * BIN_S
                        if lag > 149:
                            beyond.append(f"{arm} {world} {SHORT[cell]} bin {k}: t={t}s lag={lag}s "
                                          f"({'bin reached by all 5 arms' if k in common_bins else 'bin NOT reached by all 5 arms'})")
                        if k not in common_bins:
                            continue
                        if common_lag is None or lag > common_lag:
                            common_lag, common_where = lag, [(arm, world, SHORT[cell], k)]
                        elif lag == common_lag:
                            common_where.append((arm, world, SHORT[cell], k))
        c7.check("max lag restricted to bins all 5 arms reached (s) [scope of the author's pilot_worlds.py]", 149,
                 common_lag, ok=common_lag == 149)
        c7.check("where, restricted scope", "W4 w08 bin 3",
                 ", ".join(f"{a} {w} {c} bin {k}" for a, w, c, k in common_where),
                 ok=all((w, c, k) == ("W4", "w08", 3) for _, w, c, k in common_where))
        c7.notes.append("bins (any arm) with lag > 149 s: " + ("; ".join(beyond) or "none"))
        c7.notes.append("The report text (section 2.1, 'Trễ lớn nhất 149 s') does not state the restriction to "
                        "bins every arm reached; over all bins of all 60 logs the maximum is larger (see above).")
        worst_all, spread_rows, factor_diff_all = spread_analysis(logs, ARMS, require_all=True)
        c7.check("max spread across the 5 arms, bins all 5 arms reached (s)", 131, worst_all[0])
        c7.check("where", [("W5", "w17", 8)], worst_all[1])
        worst_any, _, factor_diff_any = spread_analysis(logs, ARMS, require_all=False)
        c7.check("max spread across arms, bins reached by >= 2 arms (s) [robustness]", 131, worst_any[0])
        worst_cv, _, _ = spread_analysis(logs, ("C-30", "V-30"), require_all=True)
        c7.check("max spread C-30 vs V-30, bins both reached (s)", 130, worst_cv[0])
        c7.check("bins (all arms reached) whose factor range differs across arms", [], factor_diff_all)
        c7.check("bins (>= 2 arms reached) whose factor range differs across arms [robustness]", [], factor_diff_any)
        c7.check("logs with returncode=0 [context]", 60, sum(1 for l in logs.values() if l["returncode"] == 0))
        c7.check("logs whose bins are exactly 0..k and bin 0 at t=0 with factor [1.0000, 1.0000] [context]", 60,
                 sum(1 for l in logs.values() if [b[0] for b in l["bins"]] == list(range(len(l["bins"])))
                     and l["bins"] and l["bins"][0][1] == 0 and l["bins"][0][3:] == ("1.0000", "1.0000")))
        c7.check("'[world] t=' lines that failed the bin regex [parser sanity]", 0,
                 sum(l["binLineCandidates"] - len(l["bins"]) for l in logs.values()))
    claims.append(c7)

    # ---- claim 8
    c8 = Claim(8, "Late pickups: 71 over 60 jobs, at most 4 per job, largest lateness 207156 ms.")
    c8.check("total late pickups", 71, sum(j["latePickups"] for j in jobs.values()))
    c8.check("max late pickups in one job", 4, max(j["latePickups"] for j in jobs.values()))
    c8.check("max actualPickupMs - latestPickupMs (ms)", 207156, max(j["latePickupMaxMs"] for j in jobs.values()))
    claims.append(c8)

    # ---- integrity (not a report claim, reported for transparency)
    integrity = []
    for key in ("frameShaMismatch", "frameLengthMismatch", "duplicateDecisionConflicts", "ackWithoutPriorDecision",
                "duplicateAcks", "decisionsUnacknowledged", "forcedNoneVehicleId", "duplicateLedgerRequestId",
                "emptyHistory", "firstEntryNotInitial", "laterEntryNotRevision", "dropChainBreak",
                "dropDeltaMismatch", "historyWithoutDrop", "latePickupNonPositive"):
        integrity.append((key, sum(j.get(key) or 0 for j in jobs.values())))
    integrity.append(("jobs where decisionsWithEvidence != decisionsAcknowledged",
                      sum(1 for j in jobs.values() if j["decisionsWithEvidence"] != j["decisionsAcknowledged"])))
    integrity.append(("jobs where promisedRiders != ledgerHistories",
                      sum(1 for j in jobs.values() if j["promisedRiders"] != j["ledgerHistories"])))
    integrity.append(("fleet sizes seen", sorted({j["fleetSizes"] for j in jobs.values()})))
    integrity.append(("jobs where promised riders != completed riders (as sets)",
                      sorted(j["job"] for j in jobs.values() if j["promisedNotCompleted"] or j["completedNotPromised"])))

    # ---- additional report statements checked on the side (not in the 1-8 list)
    extra = []

    def arm_rows(arm, skip_w0=False):
        return [j for j in jobs.values() if j["arm"] == arm and not (skip_w0 and j["world"] == "W0")]

    for arm in ("C-30", "V-30", "Mplus-30", "M-30"):
        nn = [j["nonNormalShare"] for j in arm_rows(arm, True)]
        fr = [j["ridersWithForcedBreach"] / j["promisedRiders"] for j in arm_rows(arm, True)]
        fr_all = [j["ridersWithForcedBreach"] / j["promisedRiders"] for j in arm_rows(arm)]
        mf = [j["meanForcedFleetShare"] for j in arm_rows(arm, True)]
        mf_all = [j["meanForcedFleetShare"] for j in arm_rows(arm)]
        extra.append((f"table 2.7 {arm}: non-normal share range excl. W0", f"{fmt3(min(nn))}-{fmt3(max(nn))}"))
        extra.append((f"table 2.7 {arm}: forced-breach rider share range excl. W0 / all 12",
                      f"{fmt3(min(fr))}-{fmt3(max(fr))} / {fmt3(min(fr_all))}-{fmt3(max(fr_all))}"))
        extra.append((f"table 2.7 {arm}: mean forced fleet share range excl. W0 / all 12",
                      f"{fmt3(min(mf))}-{fmt3(max(mf))} / {fmt3(min(mf_all))}-{fmt3(max(mf_all))}"))
    extra.append(("U episodes with non-normal share > 0.5", sum(1 for j in arm_rows("U") if j["nonNormalShare"] > 0.5)))
    extra.append(("V-30-W2-w17 pending decisions with >= half the fleet forced (report 36.4%)",
                  f"{target['pendingHalfForced']}/{target['pendingDecisions']} = {fmt3(target['pendingHalfForcedShare'])}"))
    extra.append(("V-30-W2-w17 forced-breach rider share (report 52.2%)",
                  f"{target['ridersWithForcedBreach']}/{target['promisedRiders']}"))
    for world, cell in (("W0", CELLS[0]), ("W0", CELLS[1])):
        u = jobs[job_name("U", world, cell)]
        extra.append((f"U {world} {SHORT[cell]} E2 (report 3/102 sáng, 5/99 tối)", f"{u['E2num']}/{u['promisedRiders']}"))
    v4 = jobs[job_name("V-30", "W4", CELLS[1])]
    extra.append(("V-30-W4-w17 largest per-rider drop C (report: one rider with 129 s)", v4["maxRiderDropCMs"]))
    diffs = [jobs[job_name("C-30", w, c)]["completed"] - jobs[job_name("V-30", w, c)]["completed"]
             for c in CELLS for w in WORLDS]
    extra.append(("C-30 served - V-30 served: >=0 count / >0 count / range (report 12/12, 9/12, 1-10)",
                  f"{sum(d >= 0 for d in diffs)}/12, {sum(d > 0 for d in diffs)}/12, "
                  f"{min(d for d in diffs if d > 0)}-{max(diffs)}"))
    extra.append(("C-30 served - U served range (report -5..+1)",
                  f"{min(jobs[job_name('C-30', w, c)]['completed'] - jobs[job_name('U', w, c)]['completed'] for c in CELLS for w in WORLDS)}.."
                  f"{max(jobs[job_name('C-30', w, c)]['completed'] - jobs[job_name('U', w, c)]['completed'] for c in CELLS for w in WORLDS)}"))
    if not missing_logs:
        extra.append(("bin counts per log (report: 9 or 10)", sorted({len(l["bins"]) for l in logs.values()})))
        extra.append(("logs where 'bin changes applied' != number of bin lines",
                      sum(1 for l in logs.values() if l["applied"] != len(l["bins"]))))
        extra.append(("logs whose edge count changes between bins",
                      sum(1 for l in logs.values() if len({b[2] for b in l["bins"]}) > 1)))

    # ---- print
    elapsed = time.time() - started
    lines = render(claims, integrity, extra, elapsed)
    print("\n".join(lines))
    if write:
        write_outputs(lines, jobs, paired_rows, logs)
    return 0


def render(claims, integrity, extra, elapsed):
    lines = ["# Independent verification of the T3.7 pilot report, claims 1-8", "",
             f"- Script: `{pathlib.Path(__file__).resolve()}` (written from scratch; imports no author module)",
             f"- Python: `{sys.executable}` {platform.python_version()}",
             f"- Inputs: `{OUT_ROOT}` (summary.json, transcript-00.ndjson streamed), `{LOG_ROOT}` (<job>.log)",
             f"- Run at: {time.strftime('%Y-%m-%d %H:%M:%S')} local, {elapsed:.0f} s",
             "- Only acknowledged decisions count (ack must follow its decision; distinct hashes). Final state = last "
             "runnerToAdapter checkpoint. Per-rider drop C/X/V summed over revision entries; E2 = drop V > 60000 ms "
             "(strict) over promised riders (histories with a drop promise).",
             "- Values stated rounded in the report (0.835, 0.298, 0.056) are compared at 3 decimals; every other "
             "value is compared exactly.", "", "## Summary", ""]
    for claim in claims:
        failing = [f"{label}: report `{expected}` vs raw `{actual}`" for label, expected, actual, ok in claim.checks
                   if not ok]
        lines.append(f"- Claim {claim.number}: **{claim.verdict()}**" + (" - " + "; ".join(failing) if failing else "")
                     + (" - " + "; ".join(claim.not_verified) if claim.not_verified else ""))
    lines += ["", "## Verdicts (detail)", ""]
    for claim in claims:
        lines.append(f"### Claim {claim.number}: {claim.verdict()}")
        lines.append("")
        lines.append(claim.text)
        lines.append("")
        for label, expected, actual, ok in claim.checks:
            lines.append(f"- [{'ok' if ok else 'MISMATCH'}] {label}: report/expected `{expected}`, raw `{actual}`")
        for reason in claim.not_verified:
            lines.append(f"- NOT VERIFIED: {reason}")
        for note in claim.notes:
            lines.append(f"- Note: {note}")
        lines.append("")
    lines += ["## Integrity checks on the raw data (sums over 60 jobs; expected 0 / empty unless noted)", ""]
    lines += [f"- {k}: `{v}`" for k, v in integrity]
    lines += ["", "## Other report statements recomputed on the side (not in the 1-8 list; informational)", ""]
    lines += [f"- {k}: `{v}`" for k, v in extra]
    lines.append("")
    return lines


def write_outputs(lines, jobs, paired_rows, logs):
    with open(HERE / "RESULT.md", "x", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(lines) + "\n")
    columns = ["job", "arm", "world", "cell", "status", "finalCheckpoint", "lines", "decisionsSent",
               "decisionsAcknowledged", "nonNormal", "nonNormalShare", "decisionsWithEvidence", "fleetSizes",
               "meanForcedFleetShare", "pendingDecisions", "pendingAllForced", "pendingAllForcedShare",
               "pendingHalfForced", "pendingHalfForcedShare", "requests", "lifecycle", "completed", "ledgerHistories",
               "promisedRiders", "E2num", "maxRiderDropCMs", "sumDropC", "sumDropX", "sumDropV", "breaches",
               "forcedBreaches", "ridersWithForcedBreach", "latePickups", "latePickupMaxMs"]
    with open(HERE / "jobs.tsv", "x", encoding="utf-8", newline="\n") as handle:
        handle.write("\t".join(columns) + "\n")
        for name, *_ in all_jobs():
            handle.write("\t".join("" if jobs[name].get(c) is None else str(jobs[name].get(c)) for c in columns) + "\n")
    with open(HERE / "paired.tsv", "x", encoding="utf-8", newline="\n") as handle:
        handle.write("world\tcell\tpromisedC\tpromisedV\tcommon\tcommonAbove60C\tcommonAbove60V\tonlyC\t"
                     "onlyCAbove60\tonlyV\tonlyVAbove60\n")
        for row in paired_rows:
            handle.write("\t".join(map(str, row)) + "\n")
    with open(HERE / "world-switch.tsv", "x", encoding="utf-8", newline="\n") as handle:
        handle.write("world\tcell\tbin\t" + "\t".join(f"t_{a}" for a in ARMS) + "\tfactors\n")
        for cell in CELLS:
            for world in WORLDS:
                by_arm = {a: {b[0]: b for b in logs[job_name(a, world, cell)]["bins"]} for a in ARMS}
                for k in sorted(set().union(*[set(v) for v in by_arm.values()])):
                    times = [str(by_arm[a][k][1]) if k in by_arm[a] else "" for a in ARMS]
                    factors = sorted({f"[{by_arm[a][k][3]},{by_arm[a][k][4]}]" for a in ARMS if k in by_arm[a]})
                    handle.write(f"{world}\t{SHORT[cell]}\t{k}\t" + "\t".join(times) + "\t" + " ".join(factors) + "\n")


if __name__ == "__main__":
    raise SystemExit(main())
