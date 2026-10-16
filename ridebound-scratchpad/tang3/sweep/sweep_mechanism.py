"""Why do C-x and M⁺-x serve different riders? (read-only, descriptive; added after sealing, see the report)

For each (world, cell, x) whose completed sets differ:
  onlyM = riders completed under M⁺-x but not under C-x; onlyC = the reverse.
  In the C-x run, for each rider in onlyM: the prune codes of candidates that would have served it (the rider is in
  the candidate's newRequestIds), counted once per code per rider. A COMMITMENT_BUDGET_EXCEEDED there means C's cap
  removed at least one way of serving that rider. Symmetrically, in the M⁺-x run for onlyC and
  COMMITMENT_DEADLINE_EXCEEDED.
  For the budget witnesses in the C-x run: the delta the candidate would have charged (ms), to show how large the
  blocked decision-caused change was.
Usage: python -B sweep_mechanism.py <jobs-sweep.tsv> <output.tsv>   (output created with mode "x")
"""
from __future__ import annotations

import base64
import collections
import csv
import json
import statistics
import sys

from run_sweep import OUT_ROOT, effective


def prunes_by_new_rider(name):
    """requestId -> Counter(code) over acknowledged decisions' pruned candidates; and budget deltas per rider."""
    sent, acknowledged = {}, set()
    with open(OUT_ROOT / name / "transcript-00.ndjson", encoding="utf-8") as handle:
        for line in handle:
            record = json.loads(line)
            envelope = json.loads(base64.b64decode(record["frameBase64"]))
            kind = envelope.get("messageType")
            if record["direction"] == "runnerToAdapter" and kind == "decision":
                payload = envelope["payload"]
                evidence = (payload.get("solver") or {}).get("executionEvidence") or {}
                sent.setdefault(payload["decisionHash"], evidence.get("prunedCandidates", []))
            elif record["direction"] == "adapterToRunner" and kind == "decisionApplied":
                acknowledged.add(envelope["payload"]["decisionHash"])
    codes, deltas = collections.defaultdict(set), collections.defaultdict(list)
    for key, pruned in sent.items():
        if key not in acknowledged:
            continue
        for prune in pruned:
            for rider in prune.get("newRequestIds", []):
                codes[rider].add(prune["code"])
                if prune["code"] == "COMMITMENT_BUDGET_EXCEEDED":
                    deltas[rider] += [w["delta"] for w in prune.get("commitmentWitnesses", [])
                                      if w.get("dimension") == "drop_eta_total_ms"]
    return codes, deltas


def completed_set(name):
    """Completed riders from the final checkpoint (the same set sweep_analyze uses via alighting events)."""
    final = None
    with open(OUT_ROOT / name / "transcript-00.ndjson", encoding="utf-8") as handle:
        for line in handle:
            record = json.loads(line)
            if record["direction"] != "runnerToAdapter":
                continue
            envelope = json.loads(base64.b64decode(record["frameBase64"]))
            if envelope.get("messageType") == "checkpoint":
                final = envelope["payload"]["content"]["onlineState"]
    return {q["requestId"] for q in final["requests"] if q["lifecycle"] == "completed"}


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    jobs = list(csv.DictReader(open(sys.argv[1], encoding="utf-8"), delimiter="\t"))
    keys = sorted({(r["world"], r["cell"], int(r["level"])) for r in jobs if r.get("level")})
    columns = ["world", "cell", "level", "onlyM", "onlyC", "onlyM_blockedByCBudget", "onlyM_otherCodesOnly",
               "onlyC_blockedByMDeadline", "onlyC_otherCodesOnly", "cBudgetDeltaMedianMs", "cBudgetDeltaMaxMs"]
    with open(sys.argv[2], "x", encoding="utf-8", newline="\n") as out:
        out.write("\t".join(columns) + "\n")
        for world, cell, x in keys:
            c_name, m_name = effective(f"C-{x}-{world}-{cell}"), effective(f"Mplus-{x}-{world}-{cell}")
            cs, ms = completed_set(c_name), completed_set(m_name)
            if cs == ms:
                continue
            only_m, only_c = ms - cs, cs - ms
            c_codes, c_deltas = prunes_by_new_rider(c_name)
            m_codes, _ = prunes_by_new_rider(m_name)
            blocked_c = [r for r in only_m if "COMMITMENT_BUDGET_EXCEEDED" in c_codes.get(r, set())]
            blocked_m = [r for r in only_c if "COMMITMENT_DEADLINE_EXCEEDED" in m_codes.get(r, set())]
            deltas = sorted(d for r in blocked_c for d in c_deltas[r])
            row = {"world": world, "cell": cell, "level": x, "onlyM": len(only_m), "onlyC": len(only_c),
                   "onlyM_blockedByCBudget": len(blocked_c), "onlyM_otherCodesOnly": len(only_m) - len(blocked_c),
                   "onlyC_blockedByMDeadline": len(blocked_m), "onlyC_otherCodesOnly": len(only_c) - len(blocked_m),
                   "cBudgetDeltaMedianMs": statistics.median(deltas) if deltas else "",
                   "cBudgetDeltaMaxMs": deltas[-1] if deltas else ""}
            out.write("\t".join(str(row[k]) for k in columns) + "\n")
            out.flush()
            print("  ".join(f"{k}={row[k]}" for k in columns), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
