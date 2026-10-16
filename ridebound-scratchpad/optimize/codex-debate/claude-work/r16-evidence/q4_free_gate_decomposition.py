"""R16 evidence, Q4 (zero-run, read-only): decompose the decisions of WP14r FREE (b1-ref, rolling-cost, no commitment
filter) that changed an accepted rider's promise into
  GATE   : the decision's published revisions include a change that LOCKS's hard gates forbid, i.e. a decision-induced
           vehicle switch, pickup-stop switch or drop-stop switch (hardLimit 0 in wp14-c1-nobudget-v1.json), or a
           decision-induced pickup-ETA change published before the rider boarded (finalConfirmationLocks pickupEta,
           CommitmentLockEvaluator.cs:55-58, lock compares candidate with the exogenous projection, :155-158, exact
           equality :204-207);
  RANK   : no gate-forbidden change, but a decision-induced drop-ETA change (allowed under LOCKS, which has no drop cap;
           LOCKS only ranks it lower through the revision levels);
  NONE   : no decision-induced change at all.
Source: the final checkpoint's commitmentLedger (entries: publicationId, publishedPromise.publishedAtMs,
deltas.decisionInduced.{vehicleSwitchCount, pickupStopSwitchCount, dropStopSwitchCount, pickupEtaTotalMs,
dropEtaTotalMs}) joined to decisions through promisePublished.publicationId; only acknowledged decisions.
The same classifier is run on LOCKS (c1-nobudget) as a control: it must find 0 GATE decisions there.
Caveat: the WaitingPickup lifecycle starts at a BookingConfirmed event (EventReducer.cs:204-205); a rider still in
'Accepted' carries only the vehicle lock (CommitmentLockEvaluator.cs:43,69), so pickup-ETA GATE counts are an upper
bound on what LOCKS would forbid. Counted on FREE's own path (first order): the LOCKS trajectory differs.
Usage: python -B q4_free_gate_decomposition.py <out.txt>   (out opened with mode "x"; <= 4 processes)."""
import base64
import collections
import json
import pathlib
import sys
from concurrent.futures import ProcessPoolExecutor

ROOT = pathlib.Path("E:/RideBoundData/wp14r/development-v6-ledger")
ARMS = ("b1-ref", "c1-nobudget")


def analyze(job):
    arm, path = job
    pub_to_dec, acked, final = {}, set(), None
    considered = {}
    with open(path, "rb") as fh:
        for line in fh:
            row = json.loads(line)
            frame = base64.b64decode(row["frameBase64"])
            head = frame[:160]
            if row["direction"] == "adapterToRunner":
                if b'"decisionApplied"' in head:
                    acked.add(json.loads(frame)["payload"]["decisionHash"])
                continue
            if b'"checkpoint"' in head:
                final = frame
                continue
            if b'"decision"' not in head:
                continue
            env = json.loads(frame)
            if env.get("messageType") != "decision":
                continue
            p = env["payload"]
            considered[p["decisionHash"]] = ((p.get("solver") or {}).get("executionEvidence") or {}).get(
                "generation", {}).get("consideredRequestCount", 0)
            for a in p.get("actions", []):
                if a.get("decisionType") == "promisePublished":
                    pub_to_dec[a["payload"]["publicationId"]] = p["decisionHash"]
    state = json.loads(final)["payload"]["content"]["onlineState"]
    boarded = {r["requestId"]: r.get("actualPickupTimeMs") for r in state["requests"]}
    per_dec = collections.defaultdict(lambda: collections.Counter())
    drop_s = collections.defaultdict(float)
    riders = collections.defaultdict(set)
    for hist in state["commitmentLedger"]:
        rid = hist["requestId"]
        for e in hist["entries"]:
            if e["kind"] == "initialPromise":
                continue
            h = pub_to_dec[e["publicationId"]]
            if h not in acked:
                continue
            di = e["deltas"]["decisionInduced"]
            t = e["publishedPromise"]["publishedAtMs"]
            b = boarded.get(rid)
            f = per_dec[h]
            f["veh"] += di["vehicleSwitchCount"] > 0
            f["pstop"] += di["pickupStopSwitchCount"] > 0
            f["dstop"] += di["dropStopSwitchCount"] > 0
            f["pick_pre"] += di["pickupEtaTotalMs"] > 0 and (b is None or t < b)
            f["drop"] += di["dropEtaTotalMs"] > 0
            if di["dropEtaTotalMs"] > 0:
                drop_s[h] += di["dropEtaTotalMs"] / 1000
                riders[h].add(rid)
    c = collections.Counter()
    sec = collections.Counter()
    nrid = collections.Counter()
    for h in acked:
        if h not in considered:
            continue
        c["acked_decisions"] += 1
        f = per_dec.get(h, collections.Counter())
        gate = f["veh"] or f["pstop"] or f["dstop"] or f["pick_pre"]
        cls = "GATE" if gate else "RANK" if f["drop"] else "NONE"
        c[cls] += 1
        sec[cls] += drop_s.get(h, 0.0)
        nrid[cls] += len(riders.get(h, ()))
        if gate:
            for k in ("veh", "pstop", "dstop", "pick_pre"):
                c["GATE_with_" + k] += f[k] > 0
            c["GATE_also_drop"] += f["drop"] > 0
            c["GATE_only_pick_pre"] += f["pick_pre"] > 0 and not (f["veh"] or f["pstop"] or f["dstop"])
        c[cls + "_with_new_request"] += considered[h] >= 1
    return arm, dict(c), dict(sec), dict(nrid)


def main():
    out = sys.argv[1]
    jobs = [(arm, r / "attempt-01" / "output" / "transcript-00.ndjson")
            for arm in ARMS for r in sorted(ROOT.glob(f"w14-*-{arm}-s7"))
            if (r / "attempt-01" / "output" / "transcript-00.ndjson").exists()]
    with ProcessPoolExecutor(max_workers=4) as pool:
        res = list(pool.map(analyze, jobs))
    lines = ["# q4_free_gate_decomposition.py: FREE decisions that changed accepted riders' promises, by what LOCKS would do",
             ""]
    for arm in ARMS:
        c, s, n = collections.Counter(), collections.Counter(), collections.Counter()
        runs = 0
        for a, cc, ss, nn in res:
            if a == arm:
                runs += 1
                c.update(cc)
                s.update(ss)
                n.update(nn)
        lines.append(f"## {arm}: runs {runs}; acknowledged decisions {c['acked_decisions']}")
        for cls in ("GATE", "RANK", "NONE"):
            lines.append(f"  {cls}: decisions {c[cls]} (with >=1 new request {c[cls + '_with_new_request']}); "
                         f"decision-induced drop-ETA seconds published {s[cls]:.1f}; riders whose drop ETA it moved (summed over decisions) {n[cls]}")
        lines.append(f"  GATE breakdown: vehicle switch {c['GATE_with_veh']}, pickup-stop switch {c['GATE_with_pstop']}, "
                     f"drop-stop switch {c['GATE_with_dstop']}, pre-boarding pickup-ETA change {c['GATE_with_pick_pre']} "
                     f"(only that: {c['GATE_only_pick_pre']}); GATE decisions that also moved a drop ETA {c['GATE_also_drop']}")
    text = "\n".join(lines) + "\n"
    with open(out, "x", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(text)


if __name__ == "__main__":
    main()
