"""Independent claim checks 1-6 from the per-run extracts in ./runs (own code)."""
import glob
import json
import os
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = {}
for p in glob.glob(os.path.join(HERE, "runs", "*.json")):
    with open(p, "r", encoding="utf-8") as f:
        d = json.load(f)
    RUNS[(d["arm"], d["cell"])] = d

CELLS = ["d20181112-s10-r%d-w07" % i for i in range(1, 5)] + ["d20181113-s10-r%d-w07" % i for i in range(1, 5)]
SHORT = {c: c[7:9] + "r" + c[15] for c in CELLS}  # d20181112-s10-r1-w07 -> 12r1
NEW_ARMS = ["C-90", "C-150", "C-180", "C-240", "Mplus-90", "Mplus-150", "Mplus-180", "Mplus-240",
            "V-90", "V-120", "V-150", "V-180", "V-240"]
OLD_ARMS = ["U", "C-30", "C-60", "C-120", "C-300", "Mplus-30", "Mplus-60", "Mplus-120", "Mplus-300", "V-30"]
ALL_ARMS = NEW_ARMS + OLD_ARMS
LEVELS = [30, 60, 90, 120, 150, 180, 240, 300]

out = []


def P(*a):
    s = " ".join(str(x) for x in a)
    out.append(s)
    print(s)


def level(arm):
    return int(arm.split("-")[1])


P("runs loaded:", len(RUNS))
missing = [(a, c) for a in ALL_ARMS for c in CELLS if (a, c) not in RUNS]
P("missing runs:", missing)

# ---------------- integrity ----------------
P("\n== Integrity ==")
bad = []
for k, d in sorted(RUNS.items()):
    issues = []
    if d["frame_sha_mismatch"]:
        issues.append("frameSha mismatch %d" % d["frame_sha_mismatch"])
    if d["n_acked_decisions"] != d["n_decisions"]:
        issues.append("unacked decisions %d" % (d["n_decisions"] - d["n_acked_decisions"]))
    if not d["acked_equals_decision_order"]:
        issues.append("ack order differs")
    if d["n_normal_missing"]:
        issues.append("normalOperation missing %d" % d["n_normal_missing"])
    if d["n_checkpoints"] != 1:
        issues.append("checkpoints=%d" % d["n_checkpoints"])
    if d["ledger_chain_breaks"]:
        issues.append("ledger chain breaks %d" % d["ledger_chain_breaks"])
    if d["ledger_vs_actions_mismatch"] or d["actions_without_ledger"]:
        issues.append("ledger vs promisePublished mismatch %d/%d" % (d["ledger_vs_actions_mismatch"], d["actions_without_ledger"]))
    if d["completed_without_ledger"] or d["completed_without_alight"]:
        issues.append("completed w/o ledger %d, w/o alight %d" % (d["completed_without_ledger"], d["completed_without_alight"]))
    if d["alight_dupes"]:
        issues.append("duplicate alight events %d" % d["alight_dupes"])
    n_multi_init = sum(1 for r in d["riders"].values() if r["n_init"] != 1 or r["kinds0"] != "initialPromise")
    if n_multi_init:
        issues.append("riders with !=1 initialPromise or not first: %d" % n_multi_init)
    if issues:
        bad.append((k, issues))
P("runs with integrity issues:", len(bad))
for k, i in bad:
    P("  ", k, i)
tot_frames = sum(d["frames"] for d in RUNS.values())
P("total frames checked (sha256 of decoded frame == frameSha256):", tot_frames)

# ---------------- claim 1 ----------------
P("\n== Claim 1 ==")
new = [RUNS[(a, c)] for a in NEW_ARMS for c in CELLS]
st = defaultdict(int)
inv = defaultdict(int)
for d in new:
    st[d["summary_status"]] += 1
    inv[d["summary_inventory"]] += 1
P("new summaries:", len(new), "status counts:", dict(st))
P("inventory counts:", dict(inv))
arm_hash = {}
c1_ok = True
for a in ALL_ARMS:
    hs = set(RUNS[(a, c)]["policyConfigurationHash"] for c in CELLS)
    P("  %-10s distinct policy hashes over 8 cells: %d  %s" % (a, len(hs), sorted(hs)[0][:16]))
    if len(hs) != 1:
        c1_ok = False
    arm_hash[a] = sorted(hs)[0]
distinct = len(set(arm_hash.values()))
P("distinct arm-level policy hashes:", distinct, "of", len(ALL_ARMS))
c1 = (st.get("pass", 0) == 104 and inv.get("0da63eaf2b30ab332fba265a6b2b6e5c36b3ee78950cbac6d6267e60f81e4cbe", 0) == 104
      and c1_ok and distinct == 23)
P("CLAIM 1:", "MATCH" if c1 else "MISMATCH")
# also check reused summaries
old_st = defaultdict(int)
for a in OLD_ARMS:
    for c in CELLS:
        old_st[(RUNS[(a, c)]["summary_status"], RUNS[(a, c)]["summary_inventory"][:12])] += 1
P("(info) reused summaries status/inventory:", dict(old_st))

# ---------------- claim 2 ----------------
P("\n== Claim 2 (served) ==")
claimed = {
    "12r1": {"U": 90, 30: (87, 87, 87), 60: (87, 87), 90: (90, 89, 89), 120: (90, 89, 89), 150: (90, 90, 90),
             180: (90, 90, 90), 240: (90, 90, 90), 300: (90, 90)},
    "12r2": {"U": 82, "all": 82},
    "12r3": {"U": 97, "all": 97},
    "12r4": {"U": 87, 30: (86, 86, 86), "all": 87},
    "13r1": {"U": 70, 30: (68, 68, 68), 60: (68, 68), 90: (69, 69, 69), 120: (71, 70, 70), 150: (71, 71, 71),
             180: (71, 71, 71), 240: (70, 70, 70), 300: (70, 70)},
    "13r2": {"U": 65, "all": 65},
    "13r3": {"U": 82, 30: (83, 83, 83), 60: (83, 83), "all": 82},
    "13r4": {"U": 92, "all": 92},
}
c2_mism = []
for c in CELLS:
    s = SHORT[c]
    row = ["U %d" % RUNS[("U", c)]["served"]]
    if RUNS[("U", c)]["served"] != claimed[s]["U"]:
        c2_mism.append((s, "U", RUNS[("U", c)]["served"], claimed[s]["U"]))
    for L in LEVELS:
        vals = []
        for fam in ("C", "Mplus", "V"):
            a = "%s-%d" % (fam, L)
            if (a, c) in RUNS:
                vals.append(RUNS[(a, c)]["served"])
        row.append("%d: %s" % (L, "/".join(str(v) for v in vals)))
        exp = claimed[s].get(L)
        if exp is None:
            exp = tuple([claimed[s]["all"]] * len(vals))
        if tuple(vals) != tuple(exp):
            c2_mism.append((s, L, vals, exp))
    P("  %s: %s" % (s, " | ".join(row)))
P("claim-2 mismatches:", c2_mism)
P("CLAIM 2:", "MATCH" if not c2_mism else "MISMATCH")

# ---------------- claim 3 ----------------
P("\n== Claim 3 (fleet-action sequences) ==")


def seq_full(d):
    return [x["fa_full"] for x in d["decisions"]]


def seq_key(d):
    return [tuple(x["fa_keys"]) for x in d["decisions"]]


def first_diff(a, b):
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            return i
    if len(a) != len(b):
        return min(len(a), len(b))
    return None


cm_diff_full, cm_diff_key, vc_diff_full, vc_diff_key = [], [], [], []
for L in LEVELS:
    for c in CELLS:
        C = RUNS[("C-%d" % L, c)]
        M = RUNS[("Mplus-%d" % L, c)]
        ff = first_diff(seq_full(C), seq_full(M))
        fk = first_diff(seq_key(C), seq_key(M))
        if ff is not None:
            cm_diff_full.append((L, SHORT[c], ff, len(C["decisions"]), len(M["decisions"])))
        if fk is not None:
            cm_diff_key.append((L, SHORT[c], fk))
        if ("V-%d" % L, c) in RUNS:
            V = RUNS[("V-%d" % L, c)]
            ff = first_diff(seq_full(C), seq_full(V))
            fk = first_diff(seq_key(C), seq_key(V))
            if ff is not None:
                vc_diff_full.append((L, SHORT[c], ff, len(C["decisions"]), len(V["decisions"])))
            if fk is not None:
                vc_diff_key.append((L, SHORT[c], fk))
P("C vs Mplus differing (level, cell, first diff index, nC, nM) [full payload]:", cm_diff_full)
P("C vs Mplus differing [key: type+vehicle+candidate / type+request]:", cm_diff_key)
P("V vs C differing [full payload] (level, cell, idx, nC, nV):", vc_diff_full)
P("V vs C differing [key]:", vc_diff_key)
exp_set = {(90, "12r1"), (120, "12r1"), (120, "13r1")}
c3 = (set((a, b) for a, b, *_ in cm_diff_full) == exp_set and set((a, b) for a, b, *_ in vc_diff_full) == exp_set
      and set((a, b) for a, b, _ in cm_diff_key) == exp_set and set((a, b) for a, b, _ in vc_diff_key) == exp_set)
P("V levels present:", sorted(set(L for L in LEVELS for c in CELLS if ("V-%d" % L, c) in RUNS)))
P("CLAIM 3:", "MATCH" if c3 else "MISMATCH")

# ---------------- claim 4 ----------------
P("\n== Claim 4 ==")
c4 = []
for a in ["C-90", "C-150", "C-180", "C-240"]:
    for c in CELLS:
        c4.append(RUNS[(a, c)]["n_nonnormal"])
P("non-normal counts in 32 new C runs:", c4, "sum", sum(c4))
P("(info) non-normal in reused C runs:", {a: sum(RUNS[(a, c)]["n_nonnormal"] for c in CELLS) for a in ["C-30", "C-60", "C-120", "C-300"]})
P("CLAIM 4:", "MATCH" if len(c4) == 32 and sum(c4) == 0 else "MISMATCH")

# ---------------- claim 5 ----------------
P("\n== Claim 5 ==")


def a_share(d, x, strict=True):
    n = 0
    k = 0
    for rid, r in d["riders"].items():
        if r["life"] != "completed":
            continue
        n += 1
        A = r["alight"] - r["first_drop"]
        if (A > x * 1000) if strict else (A >= x * 1000):
            k += 1
    # completed riders without ledger would be excluded; checked in integrity
    return k / n if n else float("nan"), k, n


def nn_share(d):
    return d["n_nonnormal"] / d["n_acked_decisions"]


def mean(v):
    return sum(v) / len(v)


claim5_A = {90: 0.0212, 150: 0.0051, 180: 0.0051, 240: 0.0018}
claim5_NN = {90: (0.130, 0.174), 150: (0.068, 0.086), 180: (0.028, 0.028), 240: (0.017, 0.017)}
c5_ok = True
P("Level | mean share A_r > x (Mplus-x) | per-cell k/n")
for L in LEVELS:
    a = "Mplus-%d" % L
    vals = [a_share(RUNS[(a, c)], L) for c in CELLS]
    m = mean([v[0] for v in vals])
    m_ge = mean([a_share(RUNS[(a, c)], L, strict=False)[0] for c in CELLS])
    tag = ""
    if L in claim5_A:
        ok = round(m, 4) == claim5_A[L]
        c5_ok &= ok
        tag = "claimed %.4f -> %s" % (claim5_A[L], "MATCH" if ok else "MISMATCH")
    P("  %3d  %.6f  (>=: %.6f)  %s  %s" % (L, m, m_ge, " ".join("%d/%d" % (v[1], v[2]) for v in vals), tag))
P("(info) same metric under C-x and V-x:")
for L in LEVELS:
    row = []
    for fam in ("C", "V"):
        a = "%s-%d" % (fam, L)
        if all((a, c) in RUNS for c in CELLS):
            row.append("%s %.6f" % (fam, mean([a_share(RUNS[(a, c)], L)[0] for c in CELLS])))
    P("  %3d  %s" % (L, "  ".join(row)))
P("Level | mean non-normal share Mplus / V")
for L in LEVELS:
    row = []
    res = {}
    for fam in ("Mplus", "V", "C"):
        a = "%s-%d" % (fam, L)
        if all((a, c) in RUNS for c in CELLS):
            res[fam] = mean([nn_share(RUNS[(a, c)]) for c in CELLS])
            row.append("%s %.6f" % (fam, res[fam]))
    tag = ""
    if L in claim5_NN:
        ok = round(res["Mplus"], 3) == claim5_NN[L][0] and round(res["V"], 3) == claim5_NN[L][1]
        c5_ok &= ok
        tag = "claimed %.3f / %.3f -> %s" % (claim5_NN[L][0], claim5_NN[L][1], "MATCH" if ok else "MISMATCH")
    if L == 120:
        ok = round(res["V"], 3) == 0.074 and round(res["Mplus"], 3) == 0.066
        c5_ok &= ok
        tag = "claimed V 0.074 / Mplus 0.066 -> %s" % ("MATCH" if ok else "MISMATCH")
    P("  %3d  %s  %s" % (L, "  ".join(row), tag))
P("per-cell non-normal shares:")
for a in ["Mplus-90", "V-90", "Mplus-120", "V-120", "Mplus-150", "V-150", "Mplus-180", "V-180", "Mplus-240", "V-240"]:
    P("  %-10s %s" % (a, " ".join("%d/%d" % (RUNS[(a, c)]["n_nonnormal"], RUNS[(a, c)]["n_acked_decisions"]) for c in CELLS)))
P("CLAIM 5:", "MATCH" if c5_ok else "MISMATCH")

# ---------------- claim 6 ----------------
P("\n== Claim 6 ==")


def v_share(d, x, field="V", denom="promised", strict=True):
    n = 0
    k = 0
    for rid, r in d["riders"].items():
        if r["first_drop"] is None:
            continue
        if denom == "completed" and r["life"] != "completed":
            continue
        n += 1
        v = r[field]
        if (v > x * 1000) if strict else (v >= x * 1000):
            k += 1
    return k / n if n else float("nan"), k, n


claim6 = {90: 0.0289, 120: 0.0101, 150: 0.0083, 180: 0.0051, 240: 0.0036}
c6_ok = True
for L in LEVELS:
    a = "V-%d" % L
    if not all((a, c) in RUNS for c in CELLS):
        continue
    vals = [v_share(RUNS[(a, c)], L) for c in CELLS]
    m = mean([v[0] for v in vals])
    m_comp = mean([v_share(RUNS[(a, c)], L, denom="completed")[0] for c in CELLS])
    m_dec = mean([v_share(RUNS[(a, c)], L, field="Vdec")[0] for c in CELLS])
    tag = ""
    if L in claim6:
        ok = round(m, 4) == claim6[L]
        c6_ok &= ok
        tag = "claimed %.4f -> %s" % (claim6[L], "MATCH" if ok else "MISMATCH")
    P("  V-%-3d mean share V_r > x: %.6f  cells %s  %s" % (L, m, " ".join("%d/%d" % (v[1], v[2]) for v in vals), tag))
    P("         (variants: completed-denominator %.6f; sum|p-e| only %.6f)" % (m_comp, m_dec))
P("(info) V_r > x share under C-x and Mplus-x:")
for L in LEVELS:
    row = []
    for fam in ("C", "Mplus"):
        a = "%s-%d" % (fam, L)
        row.append("%s %.6f" % (fam, mean([v_share(RUNS[(a, c)], L)[0] for c in CELLS])))
    P("  %3d  %s" % (L, "  ".join(row)))
P("CLAIM 6:", "MATCH" if c6_ok else "MISMATCH")

path = os.path.join(HERE, "analyze_output.txt")
if len(sys.argv) > 1 and sys.argv[1] == "--write":
    with open(path, "x", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
