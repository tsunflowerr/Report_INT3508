"""Round 26: read primary C-120 transcripts; write only one exclusive-created report.
No project imports, simulation, builds, installs, or edits to input files.
"""
from __future__ import annotations
import base64
import collections
import hashlib
import json
from pathlib import Path

ROOT = Path("C:/RideBoundData/research/tier3-t38c120-v1")
SPLIT = Path("E:/Code/Report_INT3508/ridebound-scratchpad/tang3/t38/split-t38-v1.json")
WORK = Path("E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work")
OUT = WORK / "round26-trace-rider.txt"
ROUND_CELL = "d20181114-s10-r3-w08"
CAP_MS = 120_000


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def decode(raw):
    data = base64.b64decode(raw["frameBase64"], validate=True)
    require(len(data) == raw["frameLengthBytes"], "frame length mismatch")
    require(hashlib.sha256(data).hexdigest() == raw["frameSha256"], "frame digest mismatch")
    return json.loads(data)


def final_checkpoint(path):
    size = path.stat().st_size
    span = 262_144
    with path.open("rb") as stream:
        while True:
            start = max(0, size - span)
            stream.seek(start)
            lines = stream.read().splitlines()
            complete = lines if start == 0 else lines[1:]
            if len(complete) >= 2:
                for line in reversed(complete):
                    raw = json.loads(line)
                    prefix = base64.b64decode(raw["frameBase64"][:1600])
                    if b'"checkpoint"' not in prefix:
                        continue
                    env = decode(raw)
                    content = (env.get("payload") or {}).get("content")
                    if env["messageType"] == "checkpoint" and content is not None:
                        return raw, content
            require(start > 0, "no final checkpoint: " + str(path))
            span *= 2


def rider_rows(ledger):
    running = 0
    previous_p = None
    rows = []
    for index, entry in enumerate(ledger["entries"]):
        pub = entry["publishedPromise"]
        p = pub["projection"]["dropEtaMs"]
        e = entry["exogenousProjection"]["dropEtaMs"]
        require(p is not None and e is not None, "missing drop projection")
        if entry["kind"] == "initialPromise":
            require(index == 0, "late initial promise")
            v = p
            require(v == e, "initial drop projection differs")
        else:
            require(entry["kind"] == "revision", "unknown ledger entry kind")
            v = entry["previousPromise"]["projection"]["dropEtaMs"]
            require(v == previous_p, "promise chain mismatch")
        x, c, z = e - v, p - e, p - v
        require(x + c == z, "signed decomposition mismatch")
        require(entry["deltas"]["exogenous"]["dropEtaTotalMs"] == abs(x), "x delta mismatch")
        require(entry["deltas"]["decisionInduced"]["dropEtaTotalMs"] == abs(c), "c delta mismatch")
        require(entry["deltas"]["visible"]["dropEtaTotalMs"] == abs(z), "z delta mismatch")
        require(entry["budgetBefore"]["dropEtaTotalMs"] == running, "before ledger mismatch")
        running += abs(c)
        require(entry["budgetAfter"]["dropEtaTotalMs"] == running, "after ledger mismatch")
        require(running <= CAP_MS, "C-120 cap overshoot")
        rows.append({
            "entry": index, "kind": entry["kind"],
            "time_ms": pub["publishedAtMs"], "epoch": pub["publishedEpoch"],
            "event_seq": entry["sourceEventSeq"], "version": pub["version"],
            "v": v, "e": e, "p": p, "x": x, "c": c, "z": z,
            "sum_abs_c": running, "remaining": CAP_MS - running,
            "publication_id": entry["publicationId"],
        })
        previous_p = p
    return rows


def seconds(ms):
    return f"{ms / 1000:.3f}"


def clock(ms, cell):
    total_ms = int(cell[-2:]) * 3_600_000 + ms
    whole_s, millisecond = divmod(total_ms, 1000)
    hour, rest = divmod(whole_s, 3600)
    minute, second = divmod(rest, 60)
    return f"{hour:02d}:{minute:02d}:{second:02d}.{millisecond:03d}"


def round_counts(path):
    times = []
    decisions, acks = {}, {}
    request_ids = set()
    arrivals = []
    types = collections.Counter()
    digest = hashlib.sha256()
    frames = 0
    with path.open("rb") as stream:
        for line in stream:
            digest.update(line)
            frames += 1
            raw = json.loads(line)
            env = decode(raw)
            typ = env["messageType"]
            if typ == "eventBatch":
                times.append((env["epochId"], env["simTimeMs"], raw["ordinal"]))
                for ev in env["payload"]["events"]:
                    types[ev["eventType"]] += 1
                    if ev["eventType"] == "requestArrived":
                        request_ids.add(ev["payload"]["request"]["requestId"])
                        arrivals.append(env["simTimeMs"])
            elif typ == "decision":
                decisions[env["epochId"]] = env["simTimeMs"]
            elif typ == "decisionApplied":
                acks[env["epochId"]] = env["simTimeMs"]
    require(len(times) == len(decisions) == len(acks), "batch/decision/ACK counts differ")
    require({ep: t for ep, t, _ in times} == decisions == acks, "round times differ")
    return {
        "batches": len(times), "decisions": len(decisions), "acknowledged": len(acks),
        "requests": len(request_ids), "first": times[0], "last": times[-1],
        "unique_round_times": len({t for _, t, _ in times}),
        "same_time_intervals": sum(b[1] == a[1] for a, b in zip(times, times[1:])),
        "max_interval_ms": max(b[1] - a[1] for a, b in zip(times, times[1:])),
        "first_request_ms": min(arrivals), "last_request_ms": max(arrivals),
        "distinct_request_arrival_times": len(set(arrivals)),
        "event_types": dict(types), "frames_verified": frames,
        "transcript_sha256": digest.hexdigest(),
    }


def main():
    require(Path(__file__).resolve().parent == WORK.resolve(), "script outside work directory")
    require(not OUT.exists(), "output already exists; no overwrite")
    cells = json.loads(SPLIT.read_text(encoding="utf-8"))["test"]
    require(len(cells) == len(set(cells)) == 34, "wrong test panel")
    candidates = []
    unchanged = []
    lengths = []
    riders_checked = revisions_checked = positive_candidates = 0
    for cell in cells:
        folder = ROOT / ("C-120-" + cell)
        summary = json.loads((folder / "summary.json").read_text(encoding="utf-8"))
        run = json.loads((folder / "run-00.json").read_text(encoding="utf-8"))
        require(summary["status"] == "pass" and run["status"] == "succeeded", "invalid run")
        raw, content = final_checkpoint(folder / "transcript-00.ndjson")
        state = content["onlineState"]
        require(content["simTimeMs"] == run["semantic"]["finalSimulationTimeMs"], "final time mismatch")
        lengths.append((cell, content["simTimeMs"], len(state["requests"])))
        for ledger in state["commitmentLedger"]:
            rows = rider_rows(ledger)
            riders_checked += 1
            revisions_checked += len(rows) - 1
            nonzero = [r for r in rows[1:] if r["c"]]
            if len(rows) >= 3 and nonzero:
                # Prefer meaningful positive moves; then fewest recorded revisions.
                meaningful = any(r["c"] >= 1000 for r in nonzero)
                positive_candidates += meaningful
                score = (not meaningful, len(rows) - 1,
                         min(abs(r["c"]) % 1000 for r in nonzero), cell, ledger["requestId"])
                candidates.append((score, cell, ledger["requestId"], raw["ordinal"],
                                   raw["frameSha256"], rows))
            for row in rows[1:]:
                if row["p"] == row["v"] and row["c"] != 0:
                    unchanged.append((cell, ledger["requestId"], raw["ordinal"],
                                      raw["frameSha256"], row))
    require(candidates, "no eligible revised rider")
    _, cell, rider, ordinal, checkpoint_hash, rows = min(candidates, key=lambda t: t[0])
    lines = [
        "# Round 26 primary transcript extraction",
        "# No simulation/build/install. All arithmetic uses integer milliseconds.",
        f"# Input panel: {ROOT}; test cells: {SPLIT}",
        f"Verified final checkpoint frames: {len(cells)}; riders: {riders_checked}; revisions: {revisions_checked}",
        f"Eligible riders (at least 2 revisions and nonzero c): {len(candidates)}; with c >= 1 s: {positive_candidates}",
        "",
        "Q3 SELECTED RIDER",
        f"Cell: {cell}", f"Request: {rider}",
        f"Transcript: {ROOT / ('C-120-' + cell) / 'transcript-00.ndjson'}",
        f"Final checkpoint transcript ordinal: {ordinal}; frame SHA-256: {checkpoint_hash}",
        f"Recorded revisions (initial excluded): {len(rows)-1}",
        "t is the publication's simulated time, not wall time. v/e/p are drop ETA projections.",
        "Exact columns below are ms; time/ETA clock is New York window start plus relative ms.",
        "entry kind t_ms t_clock epoch eventSeq version v_ms e_ms p_ms x_ms c_ms z_ms sumAbsC_ms remaining_ms",
    ]
    for r in rows:
        lines.append(" ".join(str(x) for x in [
            r["entry"], r["kind"], r["time_ms"], clock(r["time_ms"], cell),
            r["epoch"], r["event_seq"], r["version"], r["v"], r["e"], r["p"],
            r["x"], r["c"], r["z"], r["sum_abs_c"], r["remaining"]]))
    lines += ["", "SAME ROWS IN SECONDS",
              "entry t_s v_s e_s p_s x_s c_s z_s sumAbsC_s remaining_s"]
    for r in rows:
        lines.append(" ".join([str(r["entry"])] + [seconds(r[k]) for k in
            ["time_ms", "v", "e", "p", "x", "c", "z", "sum_abs_c", "remaining"]]))
    lines += ["", "Q3 UNCHANGED P WITH GROWING DROP ALLOWANCE USAGE"]
    if unchanged:
        case = min(unchanged, key=lambda z: (z[0], z[1], z[4]["entry"]))
        ccell, crider, cord, chash, row = case
        lines += [f"Cases found in 34 C-120 runs: {len(unchanged)}",
                  f"Cell: {ccell}; request: {crider}; checkpoint ordinal: {cord}; hash: {chash}",
                  json.dumps(row, sort_keys=True),
                  "This is an observed p==v, c!=0 entry. No physical cause is inferred."]
    else:
        lines += ["No p==v and c!=0 drop entry found in these 34 C-120 final ledgers.",
                  "This is a scoped negative result, not proof of impossibility in other configurations."]
    path = ROOT / ("C-120-" + ROUND_CELL) / "transcript-00.ndjson"
    counted = round_counts(path)
    require(counted["requests"] == 108, "wrong real-cell request count")
    lines += ["", "Q1 REAL-CELL ROUND COUNT", str(path),
              json.dumps(counted, sort_keys=True),
              "", "Q2 C-120 MAIN-PANEL SIMULATED LENGTHS",
              "cell finalTime_ms finalTime_min finalTime_hours inputRequests nominalWindow_s"]
    for ccell, ms, req in lengths:
        lines.append(f"{ccell} {ms} {ms/60000:.6f} {ms/3600000:.9f} {req} 7200")
    lines += [f"range_minutes: {min(t for _,t,_ in lengths)/60000:.6f}..{max(t for _,t,_ in lengths)/60000:.6f}",
              "Duration starts at simulated t=0 and ends when no requests or physical tasks remain.",
              "A run can finish before 7200 s when all selected demand and trips have already finished.",
              "All selected row delta fields, prior/after ledger counters, chain values, and caps checked."]
    text = "\n".join(lines) + "\n"
    with OUT.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(text)
    print(f"WROTE {OUT} ({len(text.encode('utf-8'))} bytes)")
    print(f"SELECTED {cell} {rider} revisions={len(rows)-1}; unchanged_p_cases={len(unchanged)}")
    print(f"ROUNDS {counted['batches']} requests={counted['requests']} first={counted['first']} last={counted['last']}")


if __name__ == "__main__":
    main()

