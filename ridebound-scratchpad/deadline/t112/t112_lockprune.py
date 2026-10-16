"""T1.12 — timing of pickup-lock prunes and service effect of removing the lock.

Preregistration: T112-PREREGISTRATION.md (sealed before this script was run).
Read-only over E:/RideBoundData/wp14r/development-v6-ledger/.
"""
from __future__ import annotations

import base64
import json
import os
import statistics
from pathlib import Path

ROOT = Path(r"E:/RideBoundData/wp14r/development-v6-ledger")
CELLS = [f"d201811{day}-s10-r{rep}-w{win}"
         for day in (12, 13) for rep in (1, 2, 3, 4) for win in ("08", "17")]


def job_output(cell: str, arm: str) -> Path:
    job = ROOT / f"w14-{cell}-{arm}-s7"
    outs = [p / "output" for p in sorted(job.glob("attempt-*"))
            if (p / "output" / "summary.json").exists()]
    if len(outs) != 1:
        raise SystemExit(f"{job}: expected exactly one attempt with summary.json, got {outs}")
    return outs[0]


def frames(path: Path):
    with open(path / "transcript-00.ndjson", encoding="utf-8") as handle:
        for line in handle:
            frame = json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
            if frame.get("messageType") == "decision":
                yield frame


def accepted(path: Path) -> int:
    run = json.loads((path / "run-00.json").read_text(encoding="utf-8"))
    return len(run["semantic"]["acceptedRequestIds"])


def shares(values, cuts=(60, 120, 300, 600)):
    n = len(values)
    return {c: (sum(1 for v in values if v <= c * 1000) / n if n else float("nan")) for c in cuts}


def quantiles(values):
    if not values:
        return "n/a"
    s = sorted(values)
    q = lambda f: s[min(len(s) - 1, int(f * (len(s) - 1)))] / 1000
    return (f"min={s[0]/1000:.0f} p10={q(0.10):.0f} p25={q(0.25):.0f} p50={q(0.5):.0f} "
            f"p75={q(0.75):.0f} p90={q(0.9):.0f} max={s[-1]/1000:.0f} s")


lock_leads = []          # unique (cell, frame, request) lock events
exposure_leads = []      # every waiting-rider publication
negative_lock = 0        # lock events where the held pickup ETA is already in the past
lock_by_rule = {}
per_cell = []
for cell in CELLS:
    out = job_output(cell, "c1-h6ref")
    held = {}
    events = 0
    for frame in frames(out):
        now = frame["simTimeMs"]
        seen = set()
        evidence = frame["payload"].get("solver", {}).get("executionEvidence", {})
        for pruned in evidence.get("prunedCandidates", []) or []:
            for witness in pruned.get("commitmentWitnesses", []) or []:
                if (witness.get("code") != "COMMITMENT_PHASE_LOCK"
                        or witness.get("dimension") != "pickup_eta_ms"):
                    continue
                lock_by_rule[witness.get("rule")] = lock_by_rule.get(witness.get("rule"), 0) + 1
                key = witness["requestId"]
                if key in seen:
                    continue
                seen.add(key)
                if key not in held:
                    raise SystemExit(f"{cell}: lock witness for {key} with no prior promise")
                lead = held[key] - now
                if lead < 0:
                    negative_lock += 1
                lock_leads.append(lead)
                events += 1
        # promises published in this frame become the held promise for later frames
        for action in frame["payload"].get("actions", []):
            if action["decisionType"] != "promisePublished":
                continue
            promise = action["payload"]["promise"]
            held[promise["requestId"]] = promise["pickupEtaMs"]
            if promise["pickupEtaMs"] > now:
                exposure_leads.append(promise["pickupEtaMs"] - now)
    a_ref = accepted(out)
    a_nolock = accepted(job_output(cell, "c1-nopickuplock"))
    per_cell.append((cell, events, a_ref, a_nolock, a_nolock - a_ref))

print("T1.12 — c1-h6ref lock prunes on pickup_eta_ms, 16 development cells")
print(f"witness rules seen: {lock_by_rule}")
print(f"unique lock events (cell, frame, request): {len(lock_leads)}  "
      f"held pickup ETA already past at the frame: {negative_lock}")
print(f"lock lead quantiles     : {quantiles(lock_leads)}")
print(f"exposure lead quantiles : {quantiles(exposure_leads)}  (n={len(exposure_leads)})")
ls, es = shares(lock_leads), shares(exposure_leads)
for cut in ls:
    print(f"  share lead <= {cut:>3} s : lock {100*ls[cut]:5.1f}%   exposure {100*es[cut]:5.1f}%   "
          f"diff {100*(ls[cut]-es[cut]):+5.1f} pp")
print()
print(f"{'cell':<24}{'lock events':>12}{'h6ref':>8}{'nolock':>8}{'diff':>6}")
for cell, events, a_ref, a_nolock, diff in per_cell:
    print(f"{cell:<24}{events:>12}{a_ref:>8}{a_nolock:>8}{diff:>+6}")
total_ref = sum(r[2] for r in per_cell)
total_nolock = sum(r[3] for r in per_cell)
print(f"{'TOTAL':<24}{sum(r[1] for r in per_cell):>12}{total_ref:>8}{total_nolock:>8}"
      f"{total_nolock-total_ref:>+6}")
print(f"cells with nonzero difference: {sum(1 for r in per_cell if r[4] != 0)} / {len(per_cell)}")
