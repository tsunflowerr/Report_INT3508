"""Task w07x mechanism (descriptive; W07X-PLAN.md §3), read-only; output with mode "x".

For every level x and cell where C-x and Mplus-x have different fleet-action sequences:
  1. the first acknowledged decision whose fleet actions differ (index, simulation time);
  2. at that decision, per vehicle: the candidate each rule selected (vehiclePlanUpdated.candidateId), and requests
     accepted / rejected by one rule only;
  3. for a candidate selected by one rule and not by the other: whether the other rule PRUNED it at that same decision
     (solver.executionEvidence.prunedCandidates: code, rule, the affected rider of each witness, the new riders it would
     have served) or kept it but did not select it;
  4. for every affected rider: the drift so far (sum of signed x = e - v) and the dispatch part so far (sum of signed
     c = p - e) over its drop revisions published before that decision, and p_last - p_first, in the C-x run.
Up to the first divergence both runs have the same state, so candidate ids are comparable at that decision.
Usage: python -B w07x_mechanism.py <new-log>
"""
from __future__ import annotations

import base64
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
TANG3 = HERE.parent
for sub in ("sweep", "pilot", "evidence", "w07"):
    sys.path.insert(0, str(TANG3 / sub))

import audit_vep  # noqa: E402
import run_w07  # noqa: E402
from pilot_analyze import FLEET_ACTIONS  # noqa: E402
from w07x_analyze import LEVELS, root_of  # noqa: E402


def decisions(transcript: pathlib.Path):
    sent, order, acknowledged = {}, [], set()
    with open(transcript, encoding="utf-8") as handle:
        for line in handle:
            record = json.loads(line)
            envelope = json.loads(base64.b64decode(record["frameBase64"]))
            kind = envelope.get("messageType")
            if record["direction"] == "runnerToAdapter" and kind == "decision":
                payload = envelope["payload"]
                if payload["decisionHash"] not in sent:
                    order.append(payload["decisionHash"])
                fleet = [a for a in payload.get("actions", []) if a.get("decisionType") in FLEET_ACTIONS]
                evidence = (payload.get("solver") or {}).get("executionEvidence") or {}
                body = (payload.get("certificate") or {}).get("body") or {}
                sent[payload["decisionHash"]] = {
                    "t": envelope.get("simTimeMs"),
                    "digest": hashlib.sha256("\n".join(sorted(json.dumps(a, sort_keys=True) for a in fleet)).encode()).hexdigest(),
                    "fleet": fleet,
                    "pruned": {p["candidateId"]: p for p in evidence.get("prunedCandidates", [])},
                    "forced": sorted({(w.get("stage"), w.get("code"), w.get("requestId", "")[:10]) for w in body.get("witnesses") or []}),
                }
            elif record["direction"] == "adapterToRunner" and kind == "decisionApplied":
                acknowledged.add(envelope["payload"]["decisionHash"])
    return [sent[h] for h in order if h in acknowledged]


def summary_of(decision):
    plans = {a["payload"]["vehicleId"]: a["payload"]["candidateId"] for a in decision["fleet"] if a["decisionType"] == "vehiclePlanUpdated"}
    accepted = {a["payload"].get("requestId") for a in decision["fleet"] if a["decisionType"] == "requestAccepted"}
    rejected = {a["payload"].get("requestId") for a in decision["fleet"] if a["decisionType"] == "requestRejected"}
    return plans, accepted, rejected


def rider_state(table, rider, before_ms):
    x = c = 0
    first = last = None
    for request, coordinate, _, kind, at, _, _, p, xv, cv, _, closed in table:
        if request != rider or coordinate != "drop" or at >= before_ms:
            continue
        if kind == "initialPromise":
            first = p
        elif not closed:
            x += xv
            c += cv
        last = p
    return x, c, (None if first is None or last is None else last - first)


def change_at(table, rider, at_ms):
    """Signed (x, c) of the rider's drop revision published at exactly this decision time in this run, if any."""
    found = [(xv, cv) for request, coordinate, _, kind, at, _, _, _, xv, cv, _, closed in table
             if request == rider and coordinate == "drop" and at == at_ms and kind != "initialPromise" and not closed]
    return found[0] if found else None


def main(log_path: str) -> int:
    lines = ["# w07x_mechanism.py (descriptive): first divergence of C-x and Mplus-x per level and cell"]
    for x in LEVELS:
        for cell in run_w07.CELLS:
            names = {rule: f"{rule}-{x}-{cell}" for rule in ("C", "Mplus")}
            paths = {rule: root_of(f"{rule}-{x}") / names[rule] / "transcript-00.ndjson" for rule in names}
            if not all(p.exists() for p in paths.values()):
                continue
            runs = {rule: decisions(p) for rule, p in paths.items()}
            index = next((i for i, (a, b) in enumerate(zip(runs["C"], runs["Mplus"])) if a["digest"] != b["digest"]), None)
            if index is None:
                if len(runs["C"]) != len(runs["Mplus"]):
                    lines.append(f"x={x} {cell}: same prefix but different lengths {len(runs['C'])}/{len(runs['Mplus'])}")
                continue
            dc, dm = runs["C"][index], runs["Mplus"][index]
            lines.append(f"x={x} {cell}: first divergence at acknowledged decision {index} (t = {dc['t'] / 1000:.0f} s)")
            table, _ = audit_vep.audit(paths["C"])
            (pc, ac, rc), (pm, am, rm) = summary_of(dc), summary_of(dm)
            if ac != am or rc != rm:
                lines.append(f"    accepted only by C {sorted(r[:10] for r in ac - am)}, only by Mplus {sorted(r[:10] for r in am - ac)}; "
                             f"rejected only by C {sorted(r[:10] for r in rc - rm)}, only by Mplus {sorted(r[:10] for r in rm - rc)}")
            lines.append(f"    certificate witnesses: C {dc['forced'] or 'none'}; Mplus {dm['forced'] or 'none'}")
            for vehicle in sorted(set(pc) | set(pm)):
                if pc.get(vehicle) == pm.get(vehicle):
                    continue
                for chooser, other, chosen, other_decision in (("C", "Mplus", pc.get(vehicle), dm), ("Mplus", "C", pm.get(vehicle), dc)):
                    if chosen is None:
                        continue
                    prune = other_decision["pruned"].get(chosen)
                    if prune is None:
                        lines.append(f"    vehicle {vehicle[:10]}: {chooser} selected {chosen[:18]}; {other} did not prune it (kept, not selected)")
                        continue
                    lines.append(f"    vehicle {vehicle[:10]}: {chooser} selected {chosen[:18]}, which {other} PRUNED with {prune['code']}; "
                                 f"new riders {[r[:10] for r in prune.get('newRequestIds', [])]}")
                    for witness in prune.get("commitmentWitnesses", []):
                        rider = witness.get("requestId")
                        drift, dispatch, net = rider_state(table, rider, dc["t"])
                        now = change_at(table, rider, dc["t"]) if chooser == "C" else None
                        lines.append(f"        witness {witness.get('rule') or witness.get('code')} on rider {str(rider)[:10]}: before this decision "
                                     f"sum x = {drift / 1000:.1f} s, sum c = {dispatch / 1000:.1f} s, p_last - p_first = "
                                     f"{'-' if net is None else f'{net / 1000:.1f} s'}; in the C run this decision changed the rider by "
                                     f"{'-' if now is None else f'x = {now[0] / 1000:.1f} s, c = {now[1] / 1000:.1f} s'}")
    text = "\n".join(lines) + "\n"
    with open(log_path, "x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    raise SystemExit(main(sys.argv[1]))
