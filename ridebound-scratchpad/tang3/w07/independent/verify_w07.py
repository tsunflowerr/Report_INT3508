# Independent verifier for the tier3-w07-v1 claims.
# Written from scratch; imports nothing from the ridebound-scratchpad analysis scripts.
# Read-only on all inputs. Writes only new files (mode "x") in this script's folder.
import base64
import csv
import hashlib
import json
import os
import re
import sys
import time
from multiprocessing import Pool

DATA = r"C:\RideBoundData\research\tier3-w07-v1"
LOGS = r"E:\Code\Report_INT3508\ridebound-scratchpad\tang3\w07\logs"
TTDIR = (r"E:\RideBoundData\wp6\extracted\sha256\d9"
         r"\d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e"
         r"\FleetPy_Manhattan\networks\Manhattan_2019_corrected")
OUT = os.path.dirname(os.path.abspath(__file__))

ARMS = ["U", "C-30", "C-60", "C-120", "C-300", "Mplus-30", "Mplus-60",
        "Mplus-120", "Mplus-300", "V-30", "M-30"]
CELLS = ["d201811%d-s10-r%d-w07" % (d, r) for d in (12, 13) for r in (1, 2, 3, 4)]
FLEET_TYPES = {"vehiclePlanUpdated", "requestAccepted", "requestRejected"}
INV = "0da63eaf2b30ab332fba265a6b2b6e5c36b3ee78950cbac6d6267e60f81e4cbe"


def canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def strip_candidate(obj):
    if isinstance(obj, dict):
        return {k: strip_candidate(v) for k, v in obj.items() if k != "candidateId"}
    if isinstance(obj, list):
        return [strip_candidate(x) for x in obj]
    return obj


def process_run(folder):
    t0 = time.time()
    path = os.path.join(DATA, folder, "transcript-00.ndjson")
    decisions = []          # in transcript order: dict(hash, sim, normal, has_normal, actions)
    acked = []              # acknowledged hashes in order
    alight = {}             # requestId -> simTimeMs of first eventBatch containing its passengerAlighted
    alight_dupes = 0
    last_checkpoint = None
    checkpoints = 0
    sha_bad = 0
    lines = 0
    batch_without_sim = 0
    msg_counts = {}
    with open(path, "rb") as fh:
        for raw in fh:
            lines += 1
            rec = json.loads(raw)
            frame = base64.b64decode(rec["frameBase64"])
            if hashlib.sha256(frame).hexdigest() != rec.get("frameSha256"):
                sha_bad += 1
            direction = rec["direction"]
            env = json.loads(frame)
            mt = env.get("messageType")
            msg_counts[direction + ":" + str(mt)] = msg_counts.get(direction + ":" + str(mt), 0) + 1
            if direction == "adapterToRunner":
                if mt == "eventBatch":
                    sim = env.get("simTimeMs")
                    if sim is None:
                        batch_without_sim += 1
                    for ev in env["payload"]["events"]:
                        if ev.get("eventType") == "passengerAlighted":
                            rid = ev["payload"]["requestId"]
                            if rid in alight:
                                alight_dupes += 1
                            else:
                                alight[rid] = sim
                elif mt == "decisionApplied":
                    acked.append(env["payload"]["decisionHash"])
            elif direction == "runnerToAdapter":
                if mt == "decision":
                    p = env["payload"]
                    body = ((p.get("certificate") or {}).get("body")) or {}
                    decisions.append({
                        "hash": p.get("decisionHash"),
                        "sim": env.get("simTimeMs"),
                        "has_normal": "normalOperation" in body,
                        "normal": body.get("normalOperation"),
                        "witnesses": len(body.get("witnesses") or []),
                        "actions": p.get("actions") or [],
                    })
                elif mt == "checkpoint":
                    checkpoints += 1
                    last_checkpoint = env["payload"]
    acked_set = set(acked)
    dec_hashes = [d["hash"] for d in decisions]
    unacked = [h for h in dec_hashes if h not in acked_set]
    ack_without_decision = [h for h in acked if h not in set(dec_hashes)]

    first_promise = {}
    promise_count = 0
    fleet_full = []
    fleet_nocand = []
    nonnormal = 0
    nonnormal_first_sim = None
    missing_normal_field = 0
    fleet_type_counts = {}
    for d in decisions:
        if d["hash"] not in acked_set:
            continue
        if not d["has_normal"]:
            missing_normal_field += 1
        if d["normal"] is False:
            nonnormal += 1
            if nonnormal_first_sim is None:
                nonnormal_first_sim = d["sim"]
        for a in d["actions"]:
            t = a.get("decisionType")
            if t == "promisePublished":
                promise_count += 1
                pr = a["payload"]["promise"]
                rid = pr["requestId"]
                if rid not in first_promise:
                    first_promise[rid] = pr["dropEtaMs"]
            elif t in FLEET_TYPES:
                fleet_type_counts[t] = fleet_type_counts.get(t, 0) + 1
                fleet_full.append(hashlib.sha256(canon(a).encode("utf-8")).hexdigest())
                fleet_nocand.append(hashlib.sha256(canon(strip_candidate(a)).encode("utf-8")).hexdigest())

    reqs = last_checkpoint["content"]["onlineState"]["requests"]
    lifecycles = {}
    completed = []
    for r in reqs:
        lifecycles[r["lifecycle"]] = lifecycles.get(r["lifecycle"], 0) + 1
        if r["lifecycle"] == "completed":
            completed.append(r["requestId"])
    a_r = {}
    no_promise = []
    no_alight = []
    for rid in completed:
        if rid not in first_promise:
            no_promise.append(rid)
            continue
        if rid not in alight or alight[rid] is None:
            no_alight.append(rid)
            continue
        a_r[rid] = (alight[rid] - first_promise[rid]) / 1000.0
    alighted_not_completed = [rid for rid in alight if rid not in set(completed)]

    with open(os.path.join(DATA, folder, "summary.json"), "r", encoding="utf-8") as fh:
        summ = json.load(fh)
    return {
        "folder": folder,
        "lines": lines,
        "msg_counts": msg_counts,
        "sha_bad": sha_bad,
        "decisions": len(decisions),
        "acked": len(acked),
        "unacked": len(unacked),
        "ack_without_decision": len(ack_without_decision),
        "checkpoints_r2a": checkpoints,
        "lifecycles": lifecycles,
        "served": len(completed),
        "nonnormal": nonnormal,
        "nonnormal_first_sim": nonnormal_first_sim,
        "missing_normal_field": missing_normal_field,
        "promise_actions": promise_count,
        "riders_with_promise": len(first_promise),
        "alight_riders": len(alight),
        "alight_dupes": alight_dupes,
        "batch_without_sim": batch_without_sim,
        "alighted_not_completed": len(alighted_not_completed),
        "completed_no_promise": len(no_promise),
        "completed_no_alight": len(no_alight),
        "a_r": a_r,
        "fleet_type_counts": fleet_type_counts,
        "fleet_full_digest": hashlib.sha256("\n".join(fleet_full).encode()).hexdigest(),
        "fleet_nocand_digest": hashlib.sha256("\n".join(fleet_nocand).encode()).hexdigest(),
        "fleet_full": fleet_full,
        "fleet_nocand": fleet_nocand,
        "summary": {
            "status": summ.get("status"),
            "repositoryInventorySha256": summ.get("repositoryInventorySha256"),
            "sourceScenarioContentSha256": summ.get("sourceScenarioContentSha256"),
            "label": summ.get("label"),
        },
        "seconds": round(time.time() - t0, 1),
    }


def load_factors(day):
    f = {}
    with open(os.path.join(TTDIR, "%s_tt_factors.csv" % day), "r", encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            f[int(float(row["simulation_time"]))] = float(row["travel_time_factor"])
    return f


def check_logs():
    out = {}
    re_ver = re.compile(r"^\[world\] version=(\S+) ")
    re_base = re.compile(r"^\[world\] measured base check: day=(\S+) windowStart=(\d+) matches the scenario\s*$")
    re_bin = re.compile(r"^\[world\] t=\s*(\d+)s bin=(\d+) edges=(\d+) factor=\[([0-9.]+), ([0-9.]+)\]\s*$")
    re_binloose = re.compile(r"^\[world\] t=")
    factors = {d: load_factors(d) for d in ("2018-11-12", "2018-11-13")}
    for arm in ARMS:
        for cell in CELLS:
            job = "%s-%s" % (arm, cell)
            day = "2018-11-%s" % cell[7:9]
            with open(os.path.join(LOGS, job + ".log"), "r", encoding="utf-8") as fh:
                lines = fh.read().splitlines()
            ver_lines = [l for l in lines if l.startswith("[world] version=")]
            ver_v12 = [l for l in ver_lines if (re_ver.match(l) and re_ver.match(l).group(1) == "v1.2")]
            base_lines = [l for l in lines if l.startswith("[world] measured base check:")]
            base_ok = [l for l in base_lines if re_base.match(l) and re_base.match(l).group(1) == day
                       and re_base.match(l).group(2) == "25200"]
            bins = []
            unparsed = []
            for l in lines:
                if re_binloose.match(l):
                    m = re_bin.match(l)
                    if not m:
                        unparsed.append(l)
                        continue
                    t, b = int(m.group(1)), int(m.group(2))
                    x, y = float(m.group(4)), float(m.group(5))
                    f = factors[day]
                    exp = (f[25200 + 900 * b] / f[25200]) if b <= 8 else (f[32400] / f[25200])
                    bins.append({"t": t, "b": b, "x": x, "y": y, "exp": exp,
                                 "t_ok": t == 900 * b,
                                 "f_ok": abs(x - exp) <= 1e-4 and abs(y - exp) <= 1e-4})
            out[job] = {
                "version_lines": len(ver_lines), "version_v12": len(ver_v12),
                "base_lines": len(base_lines), "base_ok": len(base_ok),
                "bins": bins, "unparsed_t_lines": unparsed,
                "returncode_line": lines[0] if lines else None,
            }
    return out, factors


def main():
    folders = ["%s-%s" % (a, c) for a in ARMS for c in CELLS]
    missing = [f for f in folders if not os.path.isdir(os.path.join(DATA, f))]
    extra = sorted(set(os.listdir(DATA)) - set(folders))
    t0 = time.time()
    with Pool(int(sys.argv[1]) if len(sys.argv) > 1 else 6) as pool:
        results = pool.map(process_run, folders, chunksize=1)
    runs = {r["folder"]: r for r in results}
    logs, factors = check_logs()
    with open(os.path.join(OUT, "runs-extracted.json"), "x", encoding="utf-8") as fh:
        json.dump({"missing": missing, "extra": extra, "runs": runs, "logs": logs,
                   "factors_used": {d: {str(k): v for k, v in f.items() if 25200 <= k <= 33300}
                                    for d, f in factors.items()},
                   "elapsed_s": round(time.time() - t0, 1)}, fh, indent=1)
    print("done", round(time.time() - t0, 1), "s; missing", missing, "extra", extra)


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "one":
        r = process_run(sys.argv[2])
        vals = sorted(r["a_r"].values())
        for k in ("fleet_full", "fleet_nocand", "a_r"):
            r.pop(k)
        print(json.dumps(r, indent=1))
        print("A_r n=%d min=%.1f max=%.1f >30:%d >60:%d" % (len(vals), vals[0], vals[-1],
              sum(v > 30 for v in vals), sum(v > 60 for v in vals)))
    else:
        main()
