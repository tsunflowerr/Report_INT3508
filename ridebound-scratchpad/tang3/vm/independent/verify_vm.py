"""Independent verifier for the Tier 3 V/M (task A) claims.

Written from scratch; does not import anything from ridebound-scratchpad.
Pass 1 (extract): parse every transcript once and store a compact per-run
extract in extract.json (created with mode "x"; re-used if already present).
Pass 2 (analyse): evaluate claims 1-7 and write verify_output-<stamp>.txt
(mode "x").
"""
import base64
import collections
import hashlib
import json
import os
import sys
import time
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT_A = r"C:\RideBoundData\research\tier3-vm-v11-a"
ROOT_B = r"C:\RideBoundData\research\tier3-vm-v11-b"
ROOT_C = r"E:\RideBoundData\research\tier3-sweep-v1"
WORLDS = ["W0", "W1", "W2", "W3", "W4", "W5"]
CELLS = ["d20181112-s10-r1-w08", "d20181112-s10-r1-w17"]
ARMS = ["V-30", "M-30"]
INV = "0da63eaf2b30ab332fba265a6b2b6e5c36b3ee78950cbac6d6267e60f81e4cbe"
FLEET_TYPES = {"vehiclePlanUpdated", "requestAccepted", "requestRejected"}


def run_dirs():
    out = []
    for w in WORLDS:
        for c in CELLS:
            cdir = os.path.join(ROOT_C, f"C-30-{w}-{c}")
            if w == "W4" and c.endswith("w17"):
                cdir = cdir + "-rerun1"
            out.append((f"C-30|{w}|{c}", cdir))
            for arm in ARMS:
                for var, root in (("a", ROOT_A), ("b", ROOT_B)):
                    out.append((f"{arm}{var}|{w}|{c}", os.path.join(root, f"{arm}-{w}-{c}")))
    return out


def canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def h(obj):
    return hashlib.sha256(canon(obj).encode("utf-8")).hexdigest()


def extract(args):
    key, d = args
    res = {"key": key, "dir": d}
    sp = os.path.join(d, "summary.json")
    if os.path.exists(sp):
        with open(sp, "r", encoding="utf-8") as f:
            s = json.load(f)
        res["summary"] = {"status": s.get("status"), "inv": s.get("repositoryInventorySha256"),
                          "label": s.get("label"), "semanticHash": s.get("semanticHash")}
    else:
        res["summary"] = None
    tp = os.path.join(d, "transcript-00.ndjson")
    msg_counts = collections.Counter()
    decisions = []
    applied = []
    alight = {}
    board = {}
    last_ckpt = None
    sha_bad = 0
    prev_ord = None
    ord_gaps = 0
    nlines = 0
    run_id = None
    with open(tp, "r", encoding="utf-8") as f:
        for line in f:
            nlines += 1
            rec = json.loads(line)
            raw = base64.b64decode(rec["frameBase64"])
            if "frameSha256" in rec and hashlib.sha256(raw).hexdigest() != rec["frameSha256"]:
                sha_bad += 1
            o = rec.get("ordinal")
            if prev_ord is not None and o is not None and o != prev_ord + 1:
                ord_gaps += 1
            prev_ord = o
            env = json.loads(raw)
            mt = env.get("messageType")
            dr = rec["direction"]
            msg_counts[f"{dr}:{mt}"] += 1
            if run_id is None and env.get("runId"):
                run_id = env["runId"]
            if dr == "runnerToAdapter" and mt == "decision":
                p = env["payload"]
                body = p["certificate"]["body"]
                fleet_full = []
                fleet_nocand = []
                fleet_types = []
                pubs = []
                other_types = []
                for a in p["actions"]:
                    t = a["decisionType"]
                    if t == "promisePublished":
                        pp = a["payload"]
                        pr = pp["promise"]
                        pubs.append([pr["requestId"], pp.get("promiseVersion"), pr.get("dropEtaMs"),
                                     pr.get("pickupEtaMs"), pp.get("reasonCode"), pp.get("publicationId")])
                    elif t in FLEET_TYPES:
                        fleet_full.append(h(a))
                        a2 = json.loads(canon(a))
                        a2["payload"].pop("candidateId", None)
                        fleet_nocand.append(h(a2))
                        fleet_types.append(t)
                    else:
                        other_types.append(t)
                decisions.append({
                    "hash": p.get("decisionHash"),
                    "simTimeMs": env.get("simTimeMs"),
                    "epochId": env.get("epochId"),
                    "status": p.get("status"),
                    "reasonCode": p.get("reasonCode"),
                    "certStatus": p["certificate"].get("status"),
                    "normal": body.get("normalOperation"),
                    "witnesses": [[w.get("stage"), w.get("code"), w.get("requestId"), w.get("vehicleId")]
                                  for w in body.get("witnesses", [])],
                    "fleet_full": fleet_full,
                    "fleet_nocand": fleet_nocand,
                    "fleet_types": fleet_types,
                    "other_types": other_types,
                    "pubs": pubs,
                })
            elif dr == "adapterToRunner" and mt == "decisionApplied":
                applied.append(env["payload"].get("decisionHash"))
            elif dr == "adapterToRunner" and mt == "eventBatch":
                t_ms = env.get("simTimeMs")
                if b"passengerAlighted" in raw or b"passengerBoarded" in raw:
                    for e in env["payload"]["events"]:
                        et = e.get("eventType")
                        if et == "passengerAlighted":
                            rid = e["payload"]["requestId"]
                            if rid not in alight:
                                alight[rid] = t_ms
                        elif et == "passengerBoarded":
                            rid = e["payload"]["requestId"]
                            if rid not in board:
                                board[rid] = t_ms
            elif dr == "runnerToAdapter" and mt == "checkpoint":
                last_ckpt = env
    res["msg_counts"] = dict(msg_counts)
    res["nlines"] = nlines
    res["sha_bad"] = sha_bad
    res["ord_gaps"] = ord_gaps
    res["runId"] = run_id
    res["decisions"] = decisions
    res["applied"] = applied
    res["alight"] = alight
    res["board"] = board
    if last_ckpt is not None:
        content = last_ckpt["payload"]["content"]
        os_ = content["onlineState"]
        reqs = os_["requests"]
        res["ckpt"] = {
            "simTimeMs": content.get("simTimeMs"),
            "appliedEpoch": content.get("appliedEpoch"),
            "lifecycle": dict(collections.Counter(r.get("lifecycle") for r in reqs)),
            "completed": sorted(r["requestId"] for r in reqs if r.get("lifecycle") == "completed"),
            "request_keys": sorted({k for r in reqs for k in r.keys()}),
            "n_requests": len(reqs),
            "ledger": {x["requestId"]: [[e.get("kind"), e.get("reasonCode"), e.get("publicationId"),
                                          (e.get("publishedPromise") or {}).get("version"),
                                          ((e.get("publishedPromise") or {}).get("projection") or {}).get("dropEtaMs"),
                                          (e.get("publishedPromise") or {}).get("publishedAtMs")]
                                         for e in x["entries"]]
                       for x in os_.get("commitmentLedger", [])},
            "incident_counts": {k: (len(v) if isinstance(v, list) else v)
                                for k, v in os_.get("incidentLedger", {}).items()},
        }
    else:
        res["ckpt"] = None
    return res


def do_extract(path):
    jobs = run_dirs()
    t0 = time.time()
    out = {}
    with Pool(6) as pool:
        for r in pool.imap_unordered(extract, jobs):
            out[r["key"]] = r
            print(f"[{time.time() - t0:7.1f}s] extracted {r['key']}", flush=True)
    with open(path, "x", encoding="utf-8") as f:
        json.dump(out, f)
    return out


# ---------------------------------------------------------------- analysis

def acked(run):
    s = set(run["applied"])
    return [d for d in run["decisions"] if d["hash"] in s]


def served(run):
    return run["ckpt"]["lifecycle"].get("completed", 0)


def pub_sequences(run):
    """requestId -> list of (promiseVersion, dropEtaMs, reason, pubId) from acknowledged decisions,
    in transcript order."""
    seq = collections.OrderedDict()
    for d in acked(run):
        for rid, ver, drop, pick, reason, pid in d["pubs"]:
            seq.setdefault(rid, []).append((ver, drop, reason, pid))
    return seq


def movement_share(seqs, thr_ms=30000):
    n = 0
    moved = 0
    for rid, s in seqs.items():
        n += 1
        tot = sum(abs(s[i][1] - s[i - 1][1]) for i in range(1, len(s)))
        if tot > thr_ms:
            moved += 1
    return moved, n


def main():
    cache = os.path.join(HERE, "extract.json")
    if os.path.exists(cache):
        with open(cache, "r", encoding="utf-8") as f:
            R = json.load(f)
        print("loaded cache", cache)
    else:
        R = do_extract(cache)

    L = []
    p = L.append
    p("# Independent verification output")
    p("")
    p("## Integrity per run")
    for k in sorted(R):
        r = R[k]
        acks = acked(r)
        nd = len(r["decisions"])
        unacked = nd - len(acks)
        dup_hash = nd - len({d["hash"] for d in r["decisions"]})
        appl_not_dec = len(set(r["applied"]) - {d["hash"] for d in r["decisions"]})
        other = collections.Counter(t for d in r["decisions"] for t in d["other_types"])
        st = collections.Counter((d["status"], d["certStatus"]) for d in r["decisions"])
        p(f"- {k}: dir={r['dir']} lines={r['nlines']} shaBad={r['sha_bad']} ordGaps={r['ord_gaps']} "
          f"decisions={nd} applied={len(r['applied'])} unacked={unacked} dupHash={dup_hash} "
          f"appliedNotInDecisions={appl_not_dec} otherActionTypes={dict(other)} decisionStatus={dict(st)} "
          f"ckptLifecycle={r['ckpt']['lifecycle'] if r['ckpt'] else None} runId={r['runId']} "
          f"summary={r['summary']}")

    # Claim 1
    p("")
    p("## Claim 1")
    n_ok = 0
    bad = []
    for k in sorted(R):
        if k.startswith("C-30"):
            continue
        s = R[k]["summary"]
        if s and s["status"] == "pass" and s["inv"] == INV:
            n_ok += 1
        else:
            bad.append((k, s))
    n_taskA = sum(1 for k in R if not k.startswith("C-30"))
    p(f"task A folders={n_taskA} pass+inventory ok={n_ok} bad={bad}")
    labels = collections.Counter()
    for k in sorted(R):
        if not k.startswith("C-30"):
            lab = R[k]["summary"]["label"]
            var = k.split("|")[0][-1]
            labels[(var, lab.split("-")[-1] if lab else None)] += 1
    p(f"variant vs label-suffix counts: {dict(labels)}")
    for k in sorted(R):
        if k.startswith("C-30"):
            p(f"C-30 summary {k}: {R[k]['summary']}")

    # Claim 2
    p("")
    p("## Claim 2 (served = completed in last checkpoint)")
    claimed2 = {
        ("W0", "w08"): (97, 97, 97, 97, 97), ("W0", "w17"): (95, 95, 95, 95, 95),
        ("W1", "w08"): (82, 80, 82, 79, 85), ("W1", "w17"): (79, 78, 79, 78, 79),
        ("W2", "w08"): (85, 77, 85, 77, 85), ("W2", "w17"): (79, 66, 79, 66, 79),
        ("W3", "w08"): (108, 108, 108, 108, 105), ("W3", "w17"): (107, 103, 107, 102, 107),
        ("W4", "w08"): (94, 92, 94, 89, 94), ("W4", "w17"): (89, 85, 89, 86, 89),
        ("W5", "w08"): (90, 92, 90, 87, 92), ("W5", "w17"): (99, 96, 99, 97, 99),
    }
    mism2 = 0
    for w in WORLDS:
        for c in CELLS:
            cs = c[-3:]
            got = (served(R[f"C-30|{w}|{c}"]), served(R[f"V-30a|{w}|{c}"]), served(R[f"V-30b|{w}|{c}"]),
                   served(R[f"M-30a|{w}|{c}"]), served(R[f"M-30b|{w}|{c}"]))
            exp = claimed2[(w, cs)]
            ok = got == exp
            mism2 += 0 if ok else 1
            # cross-check with alight events
            alc = tuple(len(R[f"{a}|{w}|{c}"]["alight"]) for a in ("C-30", "V-30a", "V-30b", "M-30a", "M-30b"))
            p(f"{w} {cs}: got {got[0]} | {got[1]}/{got[2]} | {got[3]}/{got[4]}  claimed {exp[0]} | {exp[1]}/{exp[2]} | "
              f"{exp[3]}/{exp[4]}  {'MATCH' if ok else 'MISMATCH'}  (alighted-event counts {alc})")
    p(f"claim 2 mismatching cells: {mism2}")

    # Claim 3
    p("")
    p("## Claim 3 (decisions with normalOperation == false; all decisions / acknowledged)")
    c3_ok = True
    for w in WORLDS:
        for c in CELLS:
            row = []
            for a in ("V-30a", "V-30b", "M-30a", "M-30b"):
                r = R[f"{a}|{w}|{c}"]
                n_all = sum(1 for d in r["decisions"] if d["normal"] is False)
                n_ack = sum(1 for d in acked(r) if d["normal"] is False)
                row.append(f"{a}={n_all}/{n_ack}")
                if w == "W0" and n_all != 0:
                    c3_ok = False
                if w != "W0" and a in ("V-30a", "M-30a") and n_ack < 1:
                    c3_ok = False
            cr = R[f"C-30|{w}|{c}"]
            row.append(f"C-30={sum(1 for d in cr['decisions'] if d['normal'] is False)}")
            p(f"{w} {c[-3:]}: " + " ".join(row))
    p(f"claim 3 holds: {c3_ok}")

    # Claim 4
    p("")
    p("## Claim 4 (fleet action sequence of acknowledged decisions vs C-30)")
    p("Fleet actions = actions with decisionType in {vehiclePlanUpdated, requestAccepted, requestRejected} "
      "(every non-promisePublished action; no other types were observed).")
    p("Tests: FLAT = flattened ordered list of action hashes; PERDEC = list of per-decision action lists "
      "(keeps decision boundaries, incl. empty ones); PERDEC_T = PERDEC plus simTimeMs of each decision; "
      "*_NC = same but candidateId removed from payloads; SORTED = per-decision sorted lists.")
    c4_b_equal = []
    for w in WORLDS:
        for c in CELLS:
            cr = acked(R[f"C-30|{w}|{c}"])
            ref = {
                "FLAT": [x for d in cr for x in d["fleet_full"]],
                "FLAT_NC": [x for d in cr for x in d["fleet_nocand"]],
                "PERDEC": [d["fleet_full"] for d in cr],
                "PERDEC_T": [(d["simTimeMs"], d["fleet_full"]) for d in cr],
                "PERDEC_NC": [d["fleet_nocand"] for d in cr],
                "SORTED": [sorted(d["fleet_full"]) for d in cr],
            }
            parts = []
            for a in ("V-30a", "V-30b", "M-30a", "M-30b"):
                ar = acked(R[f"{a}|{w}|{c}"])
                got = {
                    "FLAT": [x for d in ar for x in d["fleet_full"]],
                    "FLAT_NC": [x for d in ar for x in d["fleet_nocand"]],
                    "PERDEC": [d["fleet_full"] for d in ar],
                    "PERDEC_T": [(d["simTimeMs"], d["fleet_full"]) for d in ar],
                    "PERDEC_NC": [d["fleet_nocand"] for d in ar],
                    "SORTED": [sorted(d["fleet_full"]) for d in ar],
                }
                eq = {t: got[t] == ref[t] for t in ref}
                # first divergence on FLAT
                fd = None
                if not eq["PERDEC"]:
                    for i, (x, y) in enumerate(zip(got["PERDEC_T"], ref["PERDEC_T"])):
                        if x != y:
                            fd = (i, x[0], y[0])
                            break
                    if fd is None:
                        fd = ("len", len(got["PERDEC"]), len(ref["PERDEC"]))
                parts.append(f"{a}: " + ",".join(f"{t}={'EQ' if v else 'NE'}" for t, v in eq.items())
                             + (f" firstDiv(decIdx,simT,refSimT)={fd}" if fd else "")
                             + f" nAck={len(ar)} nFleet={len(got['FLAT'])}")
                if a == "V-30b":
                    c4_b_equal.append(((w, c[-3:]), eq))
            p(f"{w} {c[-3:]} (C-30 nAck={len(cr)} nFleet={len(ref['FLAT'])}):")
            for s in parts:
                p("    " + s)
    for t in ("FLAT", "FLAT_NC", "PERDEC", "PERDEC_T", "PERDEC_NC", "SORTED"):
        eqcells = [k for k, e in c4_b_equal if e[t]]
        necells = [k for k, e in c4_b_equal if not e[t]]
        p(f"V-30b vs C-30 [{t}]: equal in {len(eqcells)}/12; not equal: {necells}")

    # Claim 5
    p("")
    p("## Claim 5 (witnesses in acknowledged decisions)")
    tot_b = 0
    for w in WORLDS[1:]:
        for c in CELLS:
            r = R[f"V-30b|{w}|{c}"]
            n = sum(1 for d in acked(r) if any(x[0] == "forcedNoWorse" and x[1] == "COMMITMENT_BUDGET_EXCEEDED"
                                                for x in d["witnesses"]))
            n_all = sum(1 for d in r["decisions"] if any(x[0] == "forcedNoWorse" and x[1] == "COMMITMENT_BUDGET_EXCEEDED"
                                                         for x in d["witnesses"]))
            tot_b += n
            p(f"V-30b {w} {c[-3:]}: acked decisions with forcedNoWorse+COMMITMENT_BUDGET_EXCEEDED = {n} (all decisions {n_all})")
    p(f"V-30b total over W1..W5 x 2 = {tot_b}")
    m3 = 0
    for c in CELLS:
        r = R[f"M-30b|W3|{c}"]
        n = sum(1 for d in acked(r) if any(x[0] == "forcedNoWorse" for x in d["witnesses"]))
        n2 = sum(1 for d in acked(r) if any(x[0] == "forcedNoWorse" and x[1] == "COMMITMENT_BUDGET_EXCEEDED"
                                           for x in d["witnesses"]))
        m3 += n
        p(f"M-30b W3 {c[-3:]}: acked decisions with any forcedNoWorse witness = {n} (with COMMITMENT_BUDGET_EXCEEDED code {n2})")
    p(f"M-30b W3 both cells = {m3}")
    p("Witness (stage, code) inventory per run (count of witness entries, acknowledged decisions):")
    for k in sorted(R):
        cnt = collections.Counter((x[0], x[1]) for d in acked(R[k]) for x in d["witnesses"])
        p(f"    {k}: {dict(cnt)}")

    # Claims 6 and 7
    p("")
    p("## Claim 6 (W5 w08 total drop-promise movement > 30 s)")
    for a in ("C-30", "V-30a", "V-30b", "M-30a", "M-30b"):
        r = R[f"{a}|W5|d20181112-s10-r1-w08"]
        seqs = pub_sequences(r)
        moved, n = movement_share(seqs)
        # cross-check vs checkpoint commitment ledger
        led = r["ckpt"]["ledger"]
        led_seqs = {rid: [(e[3], e[4], e[1], e[2]) for e in ents] for rid, ents in led.items()}
        lm, ln = movement_share(led_seqs)
        same = all([x[3] for x in seqs.get(rid, [])] == [x[3] for x in led_seqs[rid]] for rid in led_seqs) \
            and set(seqs) == set(led_seqs)
        vers_ok = all([x[0] for x in s] == list(range(1, len(s) + 1)) for s in seqs.values())
        first_initial = all(s[0][2] == "INITIAL_BOOKING_CONFIRMATION" for s in seqs.values())
        # variant: movement only over publications at or before actual alight time? (diagnostic)
        p(f"{a}: decisions-based moved={moved}/{n} share={moved / n:.4f}; ledger-based moved={lm}/{ln} "
          f"share={lm / ln:.4f}; ledger and decision publications identical={same}; "
          f"versions 1..n contiguous={vers_ok}; first pub is INITIAL_BOOKING_CONFIRMATION={first_initial}")
        # sensitivity thresholds
        sens = []
        for thr in (0, 1000, 10000, 30000, 60000):
            m_, n_ = movement_share(seqs, thr)
            sens.append(f">{thr // 1000}s:{m_}")
        p(f"    sensitivity (moved counts): {' '.join(sens)}")
        # restricted to completed riders
        comp = set(r["ckpt"]["completed"])
        cs = {rid: s for rid, s in seqs.items() if rid in comp}
        mc, nc = movement_share(cs)
        p(f"    restricted to completed riders: {mc}/{nc} = {mc / nc:.4f}")
        # net movement |last-first|
        net = sum(1 for s in seqs.values() if abs(s[-1][1] - s[0][1]) > 30000)
        p(f"    net |last - first| > 30 s: {net}/{n} = {net / n:.4f}")

    p("")
    p("## Claim 7 (actual drop vs FIRST promised drop, completed riders, W5 w08)")
    for a in ("C-30", "V-30a", "V-30b", "M-30a", "M-30b"):
        r = R[f"{a}|W5|d20181112-s10-r1-w08"]
        seqs = pub_sequences(r)
        comp = r["ckpt"]["completed"]
        late = 0
        absd = 0
        early = 0
        missing = 0
        diffs = []
        for rid in comp:
            if rid not in r["alight"] or rid not in seqs:
                missing += 1
                continue
            dlt = r["alight"][rid] - seqs[rid][0][1]
            diffs.append(dlt)
            if dlt > 30000:
                late += 1
            if dlt < -30000:
                early += 1
            if abs(dlt) > 30000:
                absd += 1
        n = len(comp)
        p(f"{a}: completed={n} missing={missing} late>30s={late} ({late / n:.4f}) early<-30s={early} "
          f"|diff|>30s={absd} ({absd / n:.4f})")
        # last promise comparison, diagnostic
        lastd = sum(1 for rid in comp if rid in seqs and abs(r['alight'][rid] - seqs[rid][-1][1]) > 30000)
        p(f"    diagnostic: |actual - LAST promise| > 30 s: {lastd}")
        big = sorted(diffs, key=lambda x: -abs(x))[:10]
        p(f"    largest |diff| ms: {big}")

    stamp = time.strftime("%Y%m%d-%H%M%S")
    outp = os.path.join(HERE, f"verify_output-{stamp}.txt")
    with open(outp, "x", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L))
    print("wrote", outp)


if __name__ == "__main__":
    main()
