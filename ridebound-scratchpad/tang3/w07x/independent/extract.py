"""Independent per-run extractor (written from scratch for the W07X verification).

Parses one transcript-00.ndjson + summary.json and writes a compact JSON with
everything the claim checks need.  Read-only on the input; output opened "x".
"""
import base64
import hashlib
import json
import os
import sys
from multiprocessing import Pool

NEW_ROOT = r"C:\RideBoundData\research\tier3-w07x-v1"
OLD_ROOT = r"C:\RideBoundData\research\tier3-w07-v1"
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "runs")

CELLS = ["d20181112-s10-r%d-w07" % i for i in range(1, 5)] + ["d20181113-s10-r%d-w07" % i for i in range(1, 5)]
NEW_ARMS = ["C-90", "C-150", "C-180", "C-240", "Mplus-90", "Mplus-150", "Mplus-180", "Mplus-240",
            "V-90", "V-120", "V-150", "V-180", "V-240"]
OLD_ARMS = ["U", "C-30", "C-60", "C-120", "C-300", "Mplus-30", "Mplus-60", "Mplus-120", "Mplus-300", "V-30"]
FLEET_TYPES = {"vehiclePlanUpdated", "requestAccepted", "requestRejected", "requestDeferred"}


def canon(o):
    return json.dumps(o, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def action_key(a):
    t = a["decisionType"]
    p = a.get("payload", {})
    if t == "vehiclePlanUpdated":
        return "%s|%s|%s" % (t, p.get("vehicleId"), p.get("candidateId"))
    return "%s|%s" % (t, p.get("requestId"))


def process(job):
    arm, cell, root = job
    name = "%s-%s" % (arm, cell)
    out_path = os.path.join(OUT_DIR, name + ".json")
    if os.path.exists(out_path):
        return name, "skip"
    folder = os.path.join(root, name)
    res = {"name": name, "arm": arm, "cell": cell, "folder": folder}
    with open(os.path.join(folder, "summary.json"), "r", encoding="utf-8") as f:
        summ = json.load(f)
    res["summary_status"] = summ.get("status")
    res["summary_inventory"] = summ.get("repositoryInventorySha256")
    res["summary_label"] = summ.get("label")

    frames = 0
    sha_bad = 0
    decisions = []          # in transcript order
    acked_hashes = []
    alight = {}             # rid -> simTimeMs of first eventBatch containing passengerAlighted
    alight_dupes = 0
    last_ckpt = None
    n_ckpt = 0
    policy_hash = None
    run_id = None
    promise_actions_by_hash = {}  # decisionHash -> list of (rid, version, dropEta)
    with open(os.path.join(folder, "transcript-00.ndjson"), "r", encoding="utf-8") as f:
        for line in f:
            rec = json.loads(line)
            raw = base64.b64decode(rec["frameBase64"])
            frames += 1
            if hashlib.sha256(raw).hexdigest() != rec.get("frameSha256"):
                sha_bad += 1
            env = json.loads(raw)
            mt = env.get("messageType")
            d = rec["direction"]
            if d == "adapterToRunner" and mt == "initializeRun":
                policy_hash = env["payload"]["manifest"]["policyConfigurationHash"]
                run_id = env.get("runId")
            elif d == "runnerToAdapter" and mt == "decision":
                p = env["payload"]
                fleet = [a for a in p.get("actions", []) if a.get("decisionType") in FLEET_TYPES]
                body = p.get("certificate", {}).get("body", {})
                decisions.append({
                    "epochId": env.get("epochId"),
                    "simTimeMs": env.get("simTimeMs"),
                    "hash": p.get("decisionHash"),
                    "normal": body.get("normalOperation"),
                    "fa_full": sha(canon([{"decisionType": a["decisionType"], "payload": a.get("payload")} for a in fleet])),
                    "fa_keys": [action_key(a) for a in fleet],
                })
                promise_actions_by_hash[p.get("decisionHash")] = [
                    (a["payload"]["promise"]["requestId"], a["payload"]["promiseVersion"], a["payload"]["promise"]["dropEtaMs"])
                    for a in p.get("actions", []) if a.get("decisionType") == "promisePublished"]
            elif d == "adapterToRunner" and mt == "decisionApplied":
                acked_hashes.append(env["payload"]["decisionHash"])
            elif d == "adapterToRunner" and mt == "eventBatch":
                t = env.get("simTimeMs")
                for ev in env["payload"].get("events", []):
                    if ev.get("eventType") == "passengerAlighted":
                        rid = ev["payload"]["requestId"]
                        if rid in alight:
                            alight_dupes += 1
                        else:
                            alight[rid] = t
            elif d == "runnerToAdapter" and mt == "checkpoint":
                n_ckpt += 1
                last_ckpt = env
    res["frames"] = frames
    res["frame_sha_mismatch"] = sha_bad
    res["policyConfigurationHash"] = policy_hash
    res["runId"] = run_id
    res["n_decisions"] = len(decisions)
    res["n_acked_msgs"] = len(acked_hashes)
    acked_set = set(acked_hashes)
    ack = [x for x in decisions if x["hash"] in acked_set]
    res["n_acked_decisions"] = len(ack)
    res["acked_equals_decision_order"] = acked_hashes == [x["hash"] for x in decisions]
    res["decisions"] = ack
    res["n_nonnormal"] = sum(1 for x in ack if x["normal"] is False)
    res["n_normal_missing"] = sum(1 for x in ack if x["normal"] is None)
    res["alight_dupes"] = alight_dupes
    res["n_checkpoints"] = n_ckpt

    osr = last_ckpt["payload"]["content"]["onlineState"]
    life = {r["requestId"]: r["lifecycle"] for r in osr["requests"]}
    res["lifecycle_counts"] = {}
    for v in life.values():
        res["lifecycle_counts"][v] = res["lifecycle_counts"].get(v, 0) + 1
    completed = sorted(r for r, v in life.items() if v == "completed")
    res["served"] = len(completed)

    # ledger
    chain_breaks = 0
    riders = {}
    for L in osr.get("commitmentLedger", []):
        rid = L["requestId"]
        ents = L["entries"]
        first = None
        v_abs = 0
        v_dec_abs = 0
        v_exo_abs = 0
        n_rev = 0
        prev_pub = None
        kinds = []
        for e in ents:
            kinds.append(e["kind"])
            pub = e["publishedPromise"]
            if e["kind"] == "initialPromise":
                if first is None:
                    first = pub["projection"]["dropEtaMs"]
            else:
                vv = e["previousPromise"]["projection"]["dropEtaMs"]
                ee = e["exogenousProjection"]["dropEtaMs"]
                pp = pub["projection"]["dropEtaMs"]
                v_abs += abs(pp - vv)
                v_dec_abs += abs(pp - ee)
                v_exo_abs += abs(ee - vv)
                n_rev += 1
                if prev_pub is not None and canon(e["previousPromise"]) != canon(prev_pub):
                    chain_breaks += 1
            prev_pub = pub
        riders[rid] = {"first_drop": first, "V": v_abs, "Vdec": v_dec_abs, "Vexo": v_exo_abs,
                       "n_rev": n_rev, "kinds0": kinds[0] if kinds else None,
                       "n_init": kinds.count("initialPromise"),
                       "life": life.get(rid), "alight": alight.get(rid),
                       "ledger_versions": [e["publishedPromise"]["version"] for e in ents],
                       "ledger_drops": [e["publishedPromise"]["projection"]["dropEtaMs"] for e in ents]}
    res["ledger_chain_breaks"] = chain_breaks
    # cross-check ledger vs promisePublished actions of acknowledged decisions
    from collections import defaultdict
    act = defaultdict(list)
    for x in ack:
        for (rid, ver, drop) in promise_actions_by_hash.get(x["hash"], []):
            act[rid].append((ver, drop))
    mism = 0
    for rid, r in riders.items():
        if list(zip(r["ledger_versions"], r["ledger_drops"])) != act.get(rid, []):
            mism += 1
    extra = [rid for rid in act if rid not in riders]
    res["ledger_vs_actions_mismatch"] = mism
    res["actions_without_ledger"] = len(extra)
    for r in riders.values():
        del r["ledger_versions"]
        del r["ledger_drops"]
    # completed riders not in ledger / without alight
    res["completed_without_ledger"] = sum(1 for r in completed if r not in riders)
    res["completed_without_alight"] = sum(1 for r in completed if r not in alight)
    res["completed_alight_not_in_ledger"] = [r for r in completed if r not in riders]
    res["completed_extra"] = {r: {"alight": alight.get(r)} for r in completed if r not in riders}
    res["riders"] = riders
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(out_path, "x", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False)
    return name, "ok frames=%d dec=%d served=%d" % (frames, len(decisions), len(completed))


def jobs():
    js = []
    for arm in NEW_ARMS:
        for c in CELLS:
            js.append((arm, c, NEW_ROOT))
    for arm in OLD_ARMS:
        for c in CELLS:
            js.append((arm, c, OLD_ROOT))
    return js


if __name__ == "__main__":
    nproc = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    js = jobs()
    if len(sys.argv) > 2:
        js = js[: int(sys.argv[2])]
    os.makedirs(OUT_DIR, exist_ok=True)
    with Pool(nproc) as pool:
        for name, msg in pool.imap_unordered(process, js):
            print(name, msg, flush=True)
