from pathlib import Path
import base64, hashlib, json, statistics
ROOT = Path(__file__).resolve().parent
TRANSCRIPT = Path("C:/RideBoundData/research/tier3-t38-v1/C-30-d20181114-s10-r3-w07/transcript-00.ndjson")
initial = None
frames = 0
records = []
seen_bins = {}
for line in TRANSCRIPT.open(encoding="utf-8"):
    row = json.loads(line)
    raw = base64.b64decode(row["frameBase64"], validate=True)
    assert hashlib.sha256(raw).hexdigest() == row["frameSha256"]
    frames += 1
    env = json.loads(raw)
    if env.get("messageType") != "eventBatch":
        continue
    for event in env["payload"]["events"]:
        if event.get("eventType") != "travelTimesUpdated":
            continue
        snapshot = event["payload"]["snapshot"]
        arcs = {(a["fromNodeId"], a["toNodeId"]): a["travelTimeMs"] for a in snapshot["arcs"]}
        assert len(arcs) == len(snapshot["arcs"])
        if initial is None:
            assert env["simTimeMs"] == 0
            initial = {k: v for k, v in arcs.items() if v > 0}
        assert all(k in arcs and arcs[k] > 0 for k in initial)
        b = env["simTimeMs"] // 900_000
        if b in seen_bins:
            assert arcs == seen_bins[b]
        seen_bins[b] = arcs
        ratios = [arcs[k] / initial[k] for k in sorted(initial)]
        records.append({"ordinal": row["ordinal"], "sim_time_ms": env["simTimeMs"], "bin": b,
                        "version": snapshot["version"], "positive_initial_pairs": len(initial),
                        "missing_initial_pairs": 0, "median_ratio": statistics.median(ratios),
                        "min_ratio": min(ratios), "max_ratio": max(ratios)})
assert records and records[0]["median_ratio"] == 1.0
result = {"scope": "One C-30 calibration run, snapshot observability only; no fitting or simulation; no factor CSV read.",
          "transcript": str(TRANSCRIPT), "transcript_sha256": hashlib.sha256(TRANSCRIPT.read_bytes()).hexdigest(),
          "verified_frames": frames, "snapshots": records,
          "all_initial_pairs_present": True, "initial_snapshot_time_ms": 0,
          "same_bin_matrices_identical": True}
with (ROOT / "round12-snapshot-proxy-check.json").open("x", encoding="utf-8", newline="\n") as out:
    json.dump(result, out, indent=2)
    out.write("\n")
with (ROOT / "round12-snapshot-proxy-check.txt").open("x", encoding="utf-8", newline="\n") as out:
    out.write("# Round 12 snapshot-input feasibility spot check\n")
    out.write(result["scope"] + "\n")
    out.write(f"Verified frames: {frames}; snapshot updates: {len(records)}; fixed positive OD pairs: {len(initial)}; initial snapshot time: 0 ms.\n")
    out.write("All fixed pairs exist at every update; repeated within-bin matrices, if any, agree.\n")
    out.write("This certifies the inspected run only; full-panel/provenance gates remain in the proposed protocol.\n")
print(json.dumps({"verified_frames": frames, "snapshots": len(records), "positive_pairs": len(initial)}))
