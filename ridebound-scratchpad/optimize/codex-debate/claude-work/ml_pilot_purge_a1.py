"""Amendment A1 (ML-PILOT-AMENDMENTS.md): write riders-causal-a1 = riders-causal minus static CALIBRATION riders whose
original FleetPy trip is in the 11-trip fit/calibration overlap set (provenance-overlap-check-2026-10-08.txt).
Mapping (as provenance_overlap_check.py): runtime id = 'rq-' + sha256(b's' + 8-byte length + fixture requestId);
fixture sourceRecordOrdinal -> demand CSV row -> request_id.
Usage: python -B ml_pilot_purge_a1.py <in.csv> <out.csv> (mode x)."""
import csv
import hashlib
import json
import pathlib
import sys

FIX = pathlib.Path("E:/Code/RideBound/benchmarks/fixtures/wp6/public/fleetpy-manhattan-v1/wp14-development-panel-v1")
DEMROOT = pathlib.Path("E:/RideBoundData/wp6/extracted/sha256/d9/d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e")
OVERLAP = {"3212940", "3218675", "3222010", "3228410", "3229318", "3229612", "3232267", "3233063", "3234082",
           "3346430", "3350441"}


def runtime_prefix(fixture_id):
    b = fixture_id.encode("utf-8")
    return ("rq-" + hashlib.sha256(b"s" + len(b).to_bytes(8, "big") + b).hexdigest())[:16]


def mapping(cell):
    fx = FIX / cell
    path = json.loads((fx / "normalizer-configuration.json").read_text(encoding="utf-8"))["demandMemberPath"]
    with (DEMROOT / path).open(encoding="utf-8") as fh:
        ids = [row["request_id"] for row in csv.DictReader(fh)]
    sc = json.loads((fx / "scenario-content.json").read_text(encoding="utf-8"))
    return {runtime_prefix(q["requestId"]): ids[q["sourceRecordOrdinal"]] for q in sc["requests"]}


def main():
    rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8")))
    maps, dropped, kept = {}, [], []
    for r in rows:
        if r["world"] == "static" and r["role"] == "cal":
            if r["cell"] not in maps:
                maps[r["cell"]] = mapping(r["cell"])
            if maps[r["cell"]][r["rider"]] in OVERLAP:
                dropped.append((r["arm"], r["cell"], r["rider"], maps[r["cell"]][r["rider"]]))
                continue
        kept.append(r)
    with open(sys.argv[2], "x", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(kept)
    by_arm = {}
    for arm, *_ in dropped:
        by_arm[arm] = by_arm.get(arm, 0) + 1
    print(f"input {len(rows)} rows; dropped {len(dropped)} static calibration rows; kept {len(kept)}; by arm {by_arm}")


if __name__ == "__main__":
    main()
