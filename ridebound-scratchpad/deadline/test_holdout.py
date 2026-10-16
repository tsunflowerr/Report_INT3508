"""Independent check of holdout_predict.trajectory on a real transcript. Read-only.

For every rider: V from the reconstructed chain (sum |p_t - p_{t-1}|) must equal the sum of the
runner's own visibleDelta.dropEtaTotalMs; and the total C from the chain reader must equal the
sum of decisionDelta.dropEtaTotalMs read separately. Usage: test_holdout.py <run-dir> [...]
"""
from __future__ import annotations

import base64
import json
import sys
from collections import defaultdict
from pathlib import Path

import holdout_predict as hp

failures = 0
for arg in sys.argv[1:]:
    directory = Path(arg)
    chains, last, total_c = hp.trajectory(directory)
    visible = defaultdict(int)
    decision = 0
    with open(directory / "transcript-00.ndjson", encoding="utf-8") as handle:
        for line in handle:
            frame = json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
            if frame.get("messageType") != "decision":
                continue
            for action in frame["payload"].get("actions", []):
                if action["decisionType"] != "promisePublished":
                    continue
                payload = action["payload"]
                rider = payload["promise"]["requestId"]
                visible[rider] += (payload.get("visibleDelta") or {}).get("dropEtaTotalMs", 0)
                decision += (payload.get("decisionDelta") or {}).get("dropEtaTotalMs", 0)
    bad = 0
    for rider, chain in chains.items():
        v_chain = sum(abs(b[1] - a[1]) for a, b in zip(chain, chain[1:]))
        if v_chain != visible[rider]:
            bad += 1
    if total_c != decision:
        bad += 1
    failures += bad
    print(f"{directory.name}: riders {len(chains)}, last frame {last} ms, C {total_c} ms, "
          f"sum V {sum(visible.values())} ms, mismatches {bad}")
print(f"{failures} failure(s)")
raise SystemExit(1 if failures else 0)
