"""Verify the old snapshot.version schema against the independently hash-checked cache."""
import base64
import hashlib
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
cache = json.loads((HERE / "round9-ladder-records-2026-10-08.json").read_text())
output = HERE / "round9-static-snapshot-verification-2026-10-08.txt"
if output.exists():
    raise FileExistsError(output)
lines = ["# Independent static snapshot verification; legacy field is event.payload.snapshot.version.",
         "# v2 report versions=[] reflects an absent legacy field name, not absence of a travel snapshot.",
         "# Full cached event counts are from all 189071 hash-checked frames; first travel event read again directly."]
for source in cache["sources"]:
    path = Path(source["path"])
    stat = path.stat()
    if [stat.st_size, stat.st_mtime_ns] != source["signature"]:
        raise ValueError(f"Source changed: {path}")
    if source["event_types"].get("travelTimesUpdated") != 1:
        raise ValueError(f"Not exactly one travel update: {path}")
    snapshot = None
    with path.open("rb") as handle:
        for raw in handle:
            outer = json.loads(raw)
            if outer["direction"] != "adapterToRunner":
                continue
            frame = base64.b64decode(outer["frameBase64"], validate=True)
            if hashlib.sha256(frame).hexdigest() != outer["frameSha256"]:
                raise ValueError(f"Frame hash mismatch: {path}")
            env = json.loads(frame)
            if env["messageType"] != "eventBatch":
                continue
            snapshots = [e["payload"]["snapshot"] for e in env["payload"]["events"]
                         if e["eventType"] == "travelTimesUpdated"]
            if snapshots:
                if len(snapshots) != 1:
                    raise ValueError(f"Multiple snapshots in first travel event: {path}")
                snapshot = snapshots[0]
                break
    if snapshot is None or snapshot["version"] != 1:
        raise ValueError(f"Missing initial version 1: {path}")
    lines.append(f"{source['arm']} {path.parents[2].name}: travel_updates=1 snapshot.version=1 "
                 f"snapshotHash={snapshot['snapshotHash']}")
lines.append("RESULT: all 80 runs have exactly one travel update, snapshot.version=1; no later updates.")
lines.append("COMMAND: E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -B round9_verify_static_snapshot.py")
with output.open("x", encoding="utf-8", newline="\n") as handle:
    handle.write("\n".join(lines)+"\n")
print(lines[-2], flush=True)
