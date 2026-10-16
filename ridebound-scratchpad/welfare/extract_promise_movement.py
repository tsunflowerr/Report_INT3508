"""Extract, per sealed run, how much announced ETA actually moved under each rider.

The sealed transcripts carry every promisePublished decision with all three
anchors already computed by the runner:

    exogenousDelta  = previous -> exogenous   (physical drift, operator blameless)
    decisionDelta   = exogenous -> proposed   (the operator's own contribution)
    visibleDelta    = previous -> proposed    (everything the rider sees move)

This reads them back out and reduces them to per-request totals, so the price of
commitment measured in service rate can be set against the unexpected time that
commitment avoids. Nothing is written into the repository.

Usage:  extract_promise_movement.py <run-dir> [<run-dir> ...]
Writes  <out>/<label>.json  with per-request and aggregate totals.
"""

from __future__ import annotations

import base64
import json
import pathlib
import sys
from collections import defaultdict

DIMENSIONS = ("pickupEtaTotalMs", "dropEtaTotalMs")
ANCHORS = ("exogenousDelta", "decisionDelta", "visibleDelta")


def scan(run_dir: pathlib.Path) -> dict:
    transcript = run_dir / "transcript-00.ndjson"
    run = json.loads((run_dir / "run-00.json").read_text(encoding="utf-8"))

    # run-00.json reports semantic request ids ("req-<32 hex>"); the transcript
    # carries the runner's own ids ("rq-<64 hex>"). They are different hashings of
    # the same requests, so acceptance is read from the transcript's own
    # requestAccepted / requestRejected actions and cross-checked on cardinality
    # against run-00 below.
    accepted: set[str] = set()
    rejected: set[str] = set()

    per_request: dict[str, dict] = defaultdict(
        lambda: {
            "publications": 0,
            **{f"{a}.{d}": 0 for a in ANCHORS for d in DIMENSIONS},
        }
    )
    reason_codes: dict[str, int] = defaultdict(int)
    peak_budget: dict[str, int] = defaultdict(int)
    publications = 0

    with transcript.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                frame = json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
            except Exception:
                continue
            if frame.get("messageType") != "decision":
                continue
            for action in frame["payload"].get("actions", []):
                kind = action.get("decisionType")
                if kind == "requestAccepted":
                    accepted.add(action["payload"]["requestId"])
                    continue
                if kind == "requestRejected":
                    rejected.add(action["payload"]["requestId"])
                    continue
                if kind != "promisePublished":
                    continue
                payload = action["payload"]
                request_id = payload["promise"]["requestId"]
                bucket = per_request[request_id]
                bucket["publications"] += 1
                publications += 1
                reason_codes[payload.get("reasonCode", "?")] += 1
                for anchor in ANCHORS:
                    delta = payload.get(anchor) or {}
                    for dimension in DIMENSIONS:
                        bucket[f"{anchor}.{dimension}"] += int(delta.get(dimension, 0))
                # How much of each budget was ever actually consumed. If a limit
                # never approaches its cap it is slack, and the service loss must
                # be coming from some other constraint.
                for dimension, value in (payload.get("budgetAfter") or {}).items():
                    key = f"budget.{dimension}"
                    peak_budget[key] = max(peak_budget[key], int(value))

    totals = {f"{a}.{d}": 0 for a in ANCHORS for d in DIMENSIONS}
    served_totals = dict(totals)
    for request_id, bucket in per_request.items():
        for key in totals:
            totals[key] += bucket[key]
            if request_id in accepted:
                served_totals[key] += bucket[key]

    semantic = run["semantic"]
    return {
        "label": run_dir.name,
        "acceptedCount": len(accepted),
        "rejectedCount": len(rejected),
        "acceptedCountAgreesWithRun":
            len(accepted) == len(semantic["acceptedRequestIds"]),
        "rejectedCountAgreesWithRun":
            len(rejected) == len(semantic["rejectedRequestIds"]),
        "requestCount": semantic["requestCount"],
        "publications": publications,
        "publicationCountFromRun": run["semantic"]["publicationCount"],
        "requestsWithPromise": len(per_request),
        "reasonCodes": dict(sorted(reason_codes.items())),
        "peakBudgetConsumed": dict(sorted(peak_budget.items())),
        "totalsAllRequests": totals,
        "totalsAcceptedOnly": served_totals,
        "perRequest": {
            request_id: bucket
            for request_id, bucket in per_request.items()
            if request_id in accepted
        },
    }


def main() -> int:
    out_dir = pathlib.Path(__file__).resolve().parent / "out"
    out_dir.mkdir(parents=True, exist_ok=True)
    for raw in sys.argv[1:]:
        run_dir = pathlib.Path(raw)
        target = out_dir / f"{run_dir.name}.json"
        if target.exists():
            print(f"{run_dir.name}: reused", flush=True)
            continue
        result = scan(run_dir)
        target.write_text(
            json.dumps(result, indent=1, sort_keys=True) + "\n",
            encoding="utf-8", newline="\n",
        )
        agreed = result["publications"] == result["publicationCountFromRun"]
        print(
            f"{run_dir.name}: accepted={result['acceptedCount']} "
            f"publications={result['publications']} "
            f"(matches run-00: {agreed}) "
            f"visiblePickupMs={result['totalsAcceptedOnly']['visibleDelta.pickupEtaTotalMs']}",
            flush=True,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
