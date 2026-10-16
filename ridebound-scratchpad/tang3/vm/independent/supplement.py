"""Supplementary diagnostics (reads extract.json + two transcripts; writes supplement_output-<stamp>.txt, mode x)."""
import base64
import collections
import json
import os
import time

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "extract.json"), "r", encoding="utf-8") as f:
    R = json.load(f)
L = []
p = L.append
CELL = "d20181112-s10-r1-w08"


def acked(r):
    s = set(r["applied"])
    return [d for d in r["decisions"] if d["hash"] in s]


# 1. Timing of promise publications relative to the actual drop-off (W5 w08)
p("## Promise publications vs actual drop-off time, W5 w08")
for a in ("C-30", "V-30b"):
    r = R[f"{a}|W5|{CELL}"]
    seq = collections.defaultdict(list)  # rid -> [(pubTimeMs, dropEtaMs)]
    for d in acked(r):
        for rid, ver, drop, pick, reason, pid in d["pubs"]:
            seq[rid].append((d["simTimeMs"], drop))
    comp = r["ckpt"]["completed"]
    last_eq_actual = 0
    last_at_or_after = 0
    pubs_at_or_after = 0
    moved_pre = 0
    moved_all = 0
    for rid in comp:
        s = seq[rid]
        t_al = r["alight"][rid]
        if s[-1][1] == t_al:
            last_eq_actual += 1
        if s[-1][0] >= t_al:
            last_at_or_after += 1
        pubs_at_or_after += sum(1 for t, _ in s if t >= t_al)
        pre = [x for x in s if x[0] < t_al]
        tot_pre = sum(abs(pre[i][1] - pre[i - 1][1]) for i in range(1, len(pre)))
        tot_all = sum(abs(s[i][1] - s[i - 1][1]) for i in range(1, len(s)))
        moved_pre += tot_pre > 30000
        moved_all += tot_all > 30000
    n = len(comp)
    p(f"{a}: completed={n}; last promise dropEta == actual alight time: {last_eq_actual}; "
      f"last publication at/after alight: {last_at_or_after}; publications at/after alight: {pubs_at_or_after}; "
      f"moved>30s all pubs={moved_all}/{n}; moved>30s using only pubs strictly before alight={moved_pre}/{n} "
      f"({moved_pre / n:.4f})")

# 2. V-30b vs C-30 W4 w08 first divergence
p("")
p("## V-30b vs C-30 W4 w08 first divergent decision")
c = acked(R[f"C-30|W4|{CELL}"])
v = acked(R[f"V-30b|W4|{CELL}"])
first = None
ndiff = 0
for i, (x, y) in enumerate(zip(c, v)):
    if x["fleet_full"] != y["fleet_full"]:
        ndiff += 1
        if first is None:
            first = i
p(f"decisions compared={min(len(c), len(v))} differing per-decision fleet lists={ndiff} first index={first}")
for i in range(first, min(first + 3, len(c))):
    x, y = c[i], v[i]
    p(f"  idx {i}: C-30 simT={x['simTimeMs']} types={x['fleet_types']} | V-30b simT={y['simTimeMs']} "
      f"types={y['fleet_types']} normal={y['normal']} witnesses(stage,code)={collections.Counter((w[0], w[1]) for w in y['witnesses'])}")
nw = [i for i, d in enumerate(v) if any(w[0] == "forcedNoWorse" for w in d["witnesses"])]
p(f"  V-30b W4 w08 indices of acked decisions with forcedNoWorse witnesses: {nw}")
# for the other 9 V-30b cells, confirm forcedNoWorse decisions exist even though actions equal C-30
p("")
p("## forcedNoWorse decisions in V-30b cells whose fleet actions equal C-30")
for w in ("W1", "W2", "W3", "W4", "W5"):
    for cell in (CELL, "d20181112-s10-r1-w17"):
        vv = acked(R[f"V-30b|{w}|{cell}"])
        cc = acked(R[f"C-30|{w}|{cell}"])
        idx = [i for i, d in enumerate(vv) if any(x[0] == "forcedNoWorse" for x in d["witnesses"])]
        same_at = sum(1 for i in idx if i < len(cc) and cc[i]["fleet_full"] == vv[i]["fleet_full"])
        p(f"  {w} {cell[-3:]}: forcedNoWorse decisions={len(idx)}, of which per-decision fleet actions identical to C-30={same_at}")

# 3. Duplicate passengerAlighted / time consistency, two transcripts
p("")
p("## passengerAlighted multiplicity (raw rescan)")
for a, d in (("C-30", r"E:\RideBoundData\research\tier3-sweep-v1\C-30-W5-d20181112-s10-r1-w08"),
             ("V-30b", r"C:\RideBoundData\research\tier3-vm-v11-b\V-30-W5-d20181112-s10-r1-w08")):
    cnt = collections.Counter()
    with open(os.path.join(d, "transcript-00.ndjson"), "r", encoding="utf-8") as f:
        for line in f:
            rec = json.loads(line)
            if rec["direction"] != "adapterToRunner":
                continue
            raw = base64.b64decode(rec["frameBase64"])
            if b"passengerAlighted" not in raw:
                continue
            env = json.loads(raw)
            if env.get("messageType") != "eventBatch":
                continue
            for e in env["payload"]["events"]:
                if e.get("eventType") == "passengerAlighted":
                    cnt[e["payload"]["requestId"]] += 1
    p(f"{a}: requests with alight events={len(cnt)}, max events per request={max(cnt.values())}, "
      f"total={sum(cnt.values())}")

stamp = time.strftime("%Y%m%d-%H%M%S")
outp = os.path.join(HERE, f"supplement_output-{stamp}.txt")
with open(outp, "x", encoding="utf-8") as f:
    f.write("\n".join(L) + "\n")
print("\n".join(L))
print("wrote", outp)
