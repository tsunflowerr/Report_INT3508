"""Per-cell predictions for the deadline families (plan T2.8), from conduct-30 trajectories.

For each cell, read the conduct-30 transcript at the same drift level (complete, or partial
if that run died) and, for every rider, the chain of published drop ETAs:
  M+_r(t) = running max of max(0, p_t - p_0)      -> predicts dl-<l>   (one-sided deadline)
  M_r(t)  = running max of |p_t - p_0|            -> predicts dl2-<l>  (two-sided deadline)
  V_r(t)  = running sum of |p_t - p_{t-1}|        -> predicts visible-<l> (outcome ledger)
tau = first frame time at which ANY rider's quantity exceeds l (strictly).
T   = time of the last decision frame of the conduct-30 run if it died, else infinity.
Prediction:  tau <= T            -> commitment-infeasible
             no tau, completed   -> not-commitment-infeasible
             no tau, died        -> window-wall (weak prediction: the deadline did not bite
                                    before the vehicle was late)
Validity flag: reference behavioural total C (sum of decision-induced drop deltas) > 60 s
marks the cell "far-from-fallback" (the prediction assumes a near-fallback trajectory).

Read-only. Usage: holdout_predict.py <out.csv>
"""
from __future__ import annotations

import base64
import csv
import json
import math
import sys
from pathlib import Path

import run_deadline as rd

OUT_ROOT = rd.OUT_ROOT
THRESHOLDS_S = (30, 60, 120)


def trajectory(output: Path):
    """(per-rider list of (t_ms, drop_eta_ms), last frame t_ms, total C ms)."""
    path = output / "transcript-00.ndjson"
    chains: dict[str, list[tuple[int, int]]] = {}
    last = None
    total_c = 0
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            frame = json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
            if frame.get("messageType") != "decision":
                continue
            now = frame["simTimeMs"]
            last = now
            for action in frame["payload"].get("actions", []):
                if action["decisionType"] != "promisePublished":
                    continue
                payload = action["payload"]
                rider = payload["promise"]["requestId"]
                chains.setdefault(rider, []).append((now, payload["promise"]["dropEtaMs"]))
                total_c += (payload.get("decisionDelta") or {}).get("dropEtaTotalMs", 0)
    return chains, last, total_c


def first_exceed(chains, threshold_ms):
    """First time any rider's M+, M, V exceeds threshold (strictly)."""
    first = {"M+": math.inf, "M": math.inf, "V": math.inf}
    for chain in chains.values():
        p0 = chain[0][1]
        previous = p0
        running_v = 0
        for t, p in chain[1:]:
            running_v += abs(p - previous)
            previous = p
            if p - p0 > threshold_ms:
                first["M+"] = min(first["M+"], t)
            if abs(p - p0) > threshold_ms:
                first["M"] = min(first["M"], t)
            if running_v > threshold_ms:
                first["V"] = min(first["V"], t)
    return first


def predict(tau, died_at):
    # No exceedance at all must never count as "tau <= T": inf <= inf is True in Python, which
    # in the unsealed v0 of predictions.csv turned every completed reference into a false
    # "commitment-infeasible" (kept as predictions-v0-BUGGY-tau-inf.csv, never sealed).
    if tau != math.inf and tau <= died_at:
        return "commitment-infeasible", False
    if died_at == math.inf:
        return "not-commitment-infeasible", False
    return "window-wall", True


PREDICTED = [
    # (stage label, panel, k, arms with (family, threshold))
    ("2a", rd.PANEL_A, 0, [("dl-30", "M+", 30), ("dl-60", "M+", 60), ("dl-120", "M+", 120)]),
    ("2a", rd.PANEL_A, 1, [("dl-30", "M+", 30), ("dl-60", "M+", 60), ("dl-120", "M+", 120)]),
    ("2b", rd.PANEL_DEV, 1, [("visible-30", "V", 30), ("dl-30", "M+", 30), ("dl-60", "M+", 60),
                             ("dl-120", "M+", 120), ("dl2-30", "M", 30)]),
]


def reference_output(panel, k, cell):
    if panel is rd.PANEL_A and k == 0:
        return OUT_ROOT / f"ctl-conduct-k0-{cell}-s7"
    return OUT_ROOT / f"conduct-30-k{k}-{cell}-s7"


def main() -> int:
    target = Path(sys.argv[1])
    rows = []
    for stage, panel, k, arms in PREDICTED:
        for cell in panel["cells"]:
            reference = reference_output(panel, k, cell)
            label = __import__("classify").classify_output(reference)
            if label == "no-artifact" or not (reference / "transcript-00.ndjson").exists():
                raise SystemExit(f"missing reference trajectory {reference}")
            chains, last, total_c = trajectory(reference)
            died_at = math.inf if label == "completed" else last
            window = "w17" if cell.endswith("w17") else "w08"
            exceed = {s: first_exceed(chains, s * 1000) for s in THRESHOLDS_S}
            for arm, family, threshold in arms:
                tau = exceed[threshold][family]
                prediction, weak = predict(tau, died_at)
                rows.append({
                    "stage": stage, "window": window, "cell": cell, "k": k, "arm": arm,
                    "family": family, "threshold_s": threshold,
                    "tau_s": "" if tau == math.inf else f"{tau / 1000:.3f}",
                    "reference_label": label,
                    "reference_T_s": "inf" if died_at == math.inf else f"{died_at / 1000:.3f}",
                    "reference_C_s": f"{total_c / 1000:.3f}",
                    "far_from_fallback": total_c > 60_000,
                    "prediction": prediction, "weak": weak,
                })
    with open(target, "x", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} predictions to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
