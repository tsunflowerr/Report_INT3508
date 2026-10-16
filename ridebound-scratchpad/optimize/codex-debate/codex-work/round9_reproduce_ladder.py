"""Independent Round-9 raw-transcript reproduction; no Claude code imported.
Stream/hash-check every frame, decode only events and the final checkpoint.
New outputs only, directly inside codex-work; run with Python -B.
"""
from __future__ import annotations
import base64
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
DATA = Path("E:/RideBoundData/wp14r/development-v6-ledger")
ARMS = {"b1-ref": "FREE", "c1-nobudget": "LOCKS",
        "c1-budget120": "C-120", "c1-budget60": "C-60", "c1-h6ref": "C-30"}
CAPS = {"C-120": 120000, "C-60": 60000, "C-30": 30000}
EXPECTED = {
    "FREE": ["94.3", "53.1", "23.8", "16.82", "10.07", "1.29"],
    "LOCKS": ["91.7", "21.8", "3.9", "2.97", "1.70", "0.13"],
    "C-120": ["90.5", "19.4", "2.6", "1.47", "0.00", "0.00"],
    "C-60": ["89.1", "17.3", "1.3", "0.00", "0.00", "0.00"],
    "C-30": ["88.8", "15.7", "0.4", "0.00", "0.00", "0.00"],
}
KIND = re.compile(rb'"messageType"\s*:\s*"([^"]+)"')
VERSION = re.compile(rb'"travelSnapshotVersion"\s*:\s*(\d+)')

def read_run(item):
    source_arm, path = item
    arm = ARMS[source_arm]
    final_frame, alights, versions = None, {}, set()
    event_types, frames, source_bytes = Counter(), 0, 0
    before = path.stat()
    transcript_hash = hashlib.sha256()
    with path.open("rb") as stream:
        for line in stream:
            source_bytes += len(line)
            transcript_hash.update(line)
            outer = json.loads(line)
            frame = base64.b64decode(outer["frameBase64"], validate=True)
            if hashlib.sha256(frame).hexdigest() != outer["frameSha256"]:
                raise ValueError(f"Frame hash mismatch: {path}")
            if len(frame) != outer["frameLengthBytes"]:
                raise ValueError(f"Frame length mismatch: {path}")
            frames += 1
            versions.update(int(m[1]) for m in VERSION.finditer(frame))
            match = KIND.search(frame[:2048])
            kind = match[1].decode() if match else json.loads(frame)["messageType"]
            if outer["direction"] == "runnerToAdapter" and kind == "checkpoint":
                final_frame = frame
            elif outer["direction"] == "adapterToRunner" and kind == "eventBatch":
                env = json.loads(frame)
                for event in env["payload"].get("events", []):
                    event_types[event["eventType"]] += 1
                    if event["eventType"] == "passengerAlighted":
                        rid = event["payload"]["requestId"]
                        if rid in alights:
                            raise ValueError(f"Duplicate alight event: {path}/{rid}")
                        alights[rid] = env["simTimeMs"]
    after = path.stat()
    if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
        raise ValueError(f"Source changed during read: {path}")
    if final_frame is None:
        raise ValueError(f"Missing final checkpoint: {path}")
    state = json.loads(final_frame)["payload"]["content"]["onlineState"]
    requests = {r["requestId"]: r for r in state["requests"]}
    completed = {rid for rid, r in requests.items() if r["lifecycle"] == "completed"}
    if completed != set(alights):
        raise ValueError(f"Completed/alight mismatch: {path}")
    unfinished = {rid: r["lifecycle"] for rid, r in requests.items()
                  if r["lifecycle"] not in ("completed", "rejected")}
    if unfinished:
        raise ValueError(f"Undrained run: {path}/{unfinished}")
    legs = defaultdict(list)
    for rid in alights:
        req = requests[rid]
        legs[req["assignedVehicleId"]].append((req["actualPickupTimeMs"], alights[rid], rid))
    shared = set()
    for vehicle_legs in legs.values():
        for start, end, rid in vehicle_legs:
            if any(other != rid and ostart < end and start < oend
                   for ostart, oend, other in vehicle_legs):
                shared.add(rid)
    rows, history_count, nonzero_x_all, c_violations_all = [], 0, 0, 0
    largest_c_all = 0
    for history in state["commitmentLedger"]:
        rid = history["requestId"]
        entries = history["entries"]
        if not entries or entries[0]["kind"] != "initialPromise":
            raise ValueError(f"Missing first initial promise: {path}/{rid}")
        first = entries[0]["publishedPromise"]["projection"]["dropEtaMs"]
        previous = first
        xs, cs, material_entries = [], [], 0
        for entry in entries[1:]:
            v = entry["previousPromise"]["projection"]["dropEtaMs"]
            e = entry["exogenousProjection"]["dropEtaMs"]
            p = entry["publishedPromise"]["projection"]["dropEtaMs"]
            if v != previous:
                raise ValueError(f"Discontinuous publication chain: {path}/{rid}")
            deltas = entry["deltas"]
            for key, expected in (("exogenous", abs(e-v)), ("decisionInduced", abs(p-e)),
                                  ("visible", abs(p-v))):
                if deltas[key]["drop_eta_total_ms"] != expected:
                    raise ValueError(f"Ledger delta mismatch: {path}/{rid}/{key}")
            xs.append(e-v)
            cs.append(p-e)
            previous = p
            material_entries += 1
        if previous != first + sum(xs) + sum(cs):
            raise ValueError(f"Telescoping mismatch: {path}/{rid}")
        cumulative_c = sum(abs(c) for c in cs)
        history_count += 1
        nonzero_x_all += sum(x != 0 for x in xs)
        largest_c_all = max(largest_c_all, cumulative_c)
        c_violations_all += arm in CAPS and cumulative_c > CAPS[arm]
        if rid not in alights:
            continue
        arrival = alights[rid]
        z = arrival - previous
        error = arrival - first
        if error != sum(xs) + sum(cs) + z:
            raise ValueError(f"Arrival decomposition mismatch: {path}/{rid}")
        rows.append({"arm": arm, "cell": path.parents[3].name.removesuffix("-"+source_arm+"-s7"),
                     "rider": rid, "shared": rid in shared, "exposed": any(cs),
                     "initial_drop": first, "arrival": arrival, "error_ms": error,
                     "signed_x_ms": sum(xs), "absolute_x_ms": sum(abs(x) for x in xs),
                     "signed_c_ms": sum(cs), "absolute_c_ms": cumulative_c,
                     "residual_z_ms": z, "revision_entries": material_entries,
                     "late_above_cap": arm in CAPS and error > CAPS[arm]})
    if {r["rider"] for r in rows} != set(alights):
        raise ValueError(f"Served rider without ledger: {path}")
    summary = {"arm": arm, "path": str(path), "frames": frames,
               "transcript_sha256": transcript_hash.hexdigest(), "bytes": source_bytes,
               "signature": [after.st_size, after.st_mtime_ns], "requests": len(requests),
               "served": len(rows), "shared": len(shared),
               "exposed": sum(r["exposed"] for r in rows),
               "late60": sum(r["error_ms"] > 60000 for r in rows),
               "late120": sum(r["error_ms"] > 120000 for r in rows),
               "late300": sum(r["error_ms"] > 300000 for r in rows),
               "travel_versions": sorted(versions), "ledger_histories": history_count,
               "nonzero_x_entries_all": nonzero_x_all, "max_C_all_ms": largest_c_all,
               "C_breaches_all": int(c_violations_all), "event_types": dict(event_types)}
    return summary, rows

def main():
    report = HERE / "round9-ladder-reproduction-2026-10-08.txt"
    cache = HERE / "round9-ladder-records-2026-10-08.json"
    if report.exists() or cache.exists():
        raise FileExistsError("Round-9 outputs must be new")
    inventory = []
    for source_arm in ARMS:
        paths = sorted(DATA.glob(f"w14-*-{source_arm}-s7/attempt-01/output/transcript-00.ndjson"))
        if len(paths) != 16:
            raise ValueError(f"{source_arm}: expected 16 runs, got {len(paths)}")
        inventory.extend((source_arm, p) for p in paths)
    summaries, rows = [], []
    # Two independent streaming readers; no simulation process is launched.
    with ThreadPoolExecutor(max_workers=2) as pool:
        for index, (summary, riders) in enumerate(pool.map(read_run, inventory), 1):
            summaries.append(summary)
            rows.extend(riders)
            if index % 4 == 0:
                print(f"Hash-checked and reproduced {index}/{len(inventory)} transcripts", flush=True)
    lines = ["# Independent Round-9 reproduction; raw source frames and complete transcript SHA256 checked.",
             "# Coverage denominator=all requests; sharing, exposure and lateness denominator=completed riders.",
             "# Sharing=positive-duration onboard overlap; exposure=any nonzero dispatch drop component.",
             "# Strict > thresholds; pooled rider counts, not averages of per-cell rates.",
             "arm runs requests served shared exposed late60 late120 late300 | percentages"]
    mismatches = []
    for arm in ARMS.values():
        episodes = [s for s in summaries if s["arm"] == arm]
        rider_rows = [r for r in rows if r["arm"] == arm]
        totals = {k: sum(s[k] for s in episodes)
                  for k in ("requests", "served", "shared", "exposed", "late60", "late120", "late300")}
        fields = [f"{100*totals['served']/totals['requests']:.1f}"]
        fields.extend(f"{100*totals[k]/totals['served']:.1f}" for k in ("shared", "exposed"))
        fields.extend(f"{100*totals[k]/totals['served']:.2f}" for k in ("late60", "late120", "late300"))
        lines.append(arm+" "+str(len(episodes))+" "+" ".join(str(totals[k]) for k in
                     ("requests", "served", "shared", "exposed", "late60", "late120", "late300"))
                     +" | "+" ".join(fields))
        for column, actual, expected in zip(("served", "shared", "exposed", "late60", "late120", "late300"),
                                             fields, EXPECTED[arm]):
            if actual != expected:
                mismatches.append({"arm": arm, "column": column, "expected": expected, "actual": actual})
        versions = sorted({v for s in episodes for v in s["travel_versions"]})
        lines.append(f"{arm} STATIC/BOUND: versions={versions}; "
                     f"nonzero_x_entries_all={sum(s['nonzero_x_entries_all'] for s in episodes)}; "
                     f"completed_nonzero_signed_X={sum(r['signed_x_ms']!=0 for r in rider_rows)}; "
                     f"X_signed_range_ms=[{min(r['signed_x_ms'] for r in rider_rows)},"
                     f"{max(r['signed_x_ms'] for r in rider_rows)}]; "
                     f"completed_nonzero_z={sum(r['residual_z_ms']!=0 for r in rider_rows)}; "
                     f"z_range_ms=[{min(r['residual_z_ms'] for r in rider_rows)},"
                     f"{max(r['residual_z_ms'] for r in rider_rows)}]; "
                     f"max_actual_lateness_ms={max(r['error_ms'] for r in rider_rows)}; "
                     f"max_C_all_ms={max(s['max_C_all_ms'] for s in episodes)}; "
                     f"C_breaches_all={sum(s['C_breaches_all'] for s in episodes)}; "
                     f"completed_late_above_cap={sum(r['late_above_cap'] for r in rider_rows)}; "
                     f"max_X_plus_z_ms={max(r['signed_x_ms']+r['residual_z_ms'] for r in rider_rows)}")
    lines.append("TABLE_MISMATCHES="+json.dumps(mismatches, separators=(",", ":")))
    lines.append(f"Verified {len(summaries)} runs, {sum(s['frames'] for s in summaries)} frames, "
                 f"{sum(s['bytes'] for s in summaries)} raw bytes; no original files modified.")
    lines.append("COMMAND: E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -B round9_reproduce_ladder.py")
    lines.append("No dispatch/simulation jobs; new output files opened exclusively with mode x.")
    with cache.open("x", encoding="utf-8", newline="\n") as out:
        json.dump({"sources": summaries, "riders": rows}, out, separators=(",", ":"))
    with report.open("x", encoding="utf-8", newline="\n") as out:
        out.write("\n".join(lines)+"\n")
    print("\n".join(lines), flush=True)

if __name__ == "__main__":
    main()
