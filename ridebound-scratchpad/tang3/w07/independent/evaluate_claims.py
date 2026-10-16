# Evaluates claims 1-7 from runs-extracted.json (produced by verify_w07.py). Writes claims-output.txt (mode "x").
import json
import os
import statistics

OUT = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(OUT, "runs-extracted.json"), "r", encoding="utf-8"))
R = D["runs"]
L = D["logs"]
ARMS = ["U", "C-30", "C-60", "C-120", "C-300", "Mplus-30", "Mplus-60",
        "Mplus-120", "Mplus-300", "V-30", "M-30"]
CELLS = ["d201811%d-s10-r%d-w07" % (d, r) for d in (12, 13) for r in (1, 2, 3, 4)]
SHORT = {c: "%sr%s" % (c[7:9], c[15]) for c in CELLS}
assert sorted(SHORT.values()) == ["12r1", "12r2", "12r3", "12r4", "13r1", "13r2", "13r3", "13r4"], SHORT
INV = "0da63eaf2b30ab332fba265a6b2b6e5c36b3ee78950cbac6d6267e60f81e4cbe"
lines = []


def p(*a):
    s = " ".join(str(x) for x in a)
    lines.append(s)
    print(s)


def run(arm, cell):
    return R["%s-%s" % (arm, cell)]


verdict = {}

# ---------- integrity / anomalies
p("== Integrity")
p("runs:", len(R), "missing:", D["missing"], "extra:", D["extra"])
anom = []
for k, r in sorted(R.items()):
    if r["sha_bad"] or r["unacked"] or r["ack_without_decision"] or r["checkpoints_r2a"] != 1 \
            or r["missing_normal_field"] or r["alight_dupes"] or r["batch_without_sim"] \
            or r["alighted_not_completed"] or r["completed_no_promise"] or r["completed_no_alight"] \
            or r["decisions"] != r["acked"]:
        anom.append((k, {x: r[x] for x in ("sha_bad", "decisions", "acked", "unacked", "ack_without_decision",
                                             "checkpoints_r2a", "missing_normal_field", "alight_dupes",
                                             "batch_without_sim", "alighted_not_completed",
                                             "completed_no_promise", "completed_no_alight")}))
p("runs with any integrity anomaly:", len(anom))
for a in anom:
    p("  ", a)
p("total transcript lines:", sum(r["lines"] for r in R.values()),
  "frameSha256 mismatches:", sum(r["sha_bad"] for r in R.values()))
p("lifecycle sets seen:", sorted({tuple(sorted(r["lifecycles"].items())) for r in R.values()})[:3], "...")
lc_keys = sorted({k for r in R.values() for k in r["lifecycles"]})
p("lifecycle values seen across runs:", lc_keys)

# ---------- Claim 1
p("\n== Claim 1")
st = {k: r["summary"]["status"] for k, r in R.items()}
inv = {k: r["summary"]["repositoryInventorySha256"] for k, r in R.items()}
c1a = all(v == "pass" for v in st.values())
c1b = all(v == INV for v in inv.values())
p("status pass count:", sum(v == "pass" for v in st.values()), "/", len(st))
p("inventory match count:", sum(v == INV for v in inv.values()), "/", len(inv))
c1c = True
for c in CELLS:
    hs = {run(a, c)["summary"]["sourceScenarioContentSha256"] for a in ARMS}
    p("  %s distinct sourceScenarioContentSha256: %d  %s" % (SHORT[c], len(hs), sorted(hs)))
    c1c &= len(hs) == 1
allh = [run(ARMS[0], c)["summary"]["sourceScenarioContentSha256"] for c in CELLS]
p("  distinct across the 8 cells:", len(set(allh)))
verdict[1] = c1a and c1b and c1c

# ---------- Claim 2
p("\n== Claim 2")
c2 = True
maxdev = 0.0
nbins = 0
bmax = {}
for job, g in sorted(L.items()):
    ok = g["version_lines"] == 1 and g["version_v12"] == 1 and g["base_lines"] == 1 and g["base_ok"] == 1 \
        and not g["unparsed_t_lines"] and all(b["t_ok"] for b in g["bins"]) and all(b["f_ok"] for b in g["bins"])
    for b in g["bins"]:
        nbins += 1
        maxdev = max(maxdev, abs(b["x"] - b["exp"]), abs(b["y"] - b["exp"]))
    bmax[job] = max(b["b"] for b in g["bins"]) if g["bins"] else None
    if not ok:
        c2 = False
        p("  FAIL", job, {k: g[k] for k in ("version_lines", "version_v12", "base_lines", "base_ok")},
          "unparsed:", g["unparsed_t_lines"], [b for b in g["bins"] if not (b["t_ok"] and b["f_ok"])])
p("logs checked:", len(L), "bin lines:", nbins, "max |printed - expected| factor:", "%.6f" % maxdev)
p("bin lines with b>8:", sum(1 for g in L.values() for b in g["bins"] if b["b"] > 8),
  "; max bin per log distribution:", {v: sum(1 for x in bmax.values() if x == v) for v in sorted(set(bmax.values()))})
for day in ("2018-11-12", "2018-11-13"):
    f = D["factors_used"][day]
    base = f["25200"]
    p("  %s expected factors b=0..8:" % day,
      ", ".join("%.4f" % (f[str(25200 + 900 * b)] / base) for b in range(9)),
      "| b>8: %.4f" % (f["32400"] / base), "| f(25200)=%.6f" % base)
p("returncode lines not 'returncode=0':", [j for j, g in L.items() if not (g["returncode_line"] or "").startswith("returncode=0 ")])
verdict[2] = c2

# ---------- Claim 3
p("\n== Claim 3 (served = completed in last checkpoint)")
claimed3 = {
    "12r1": [90, 87, 87, 90, 90, 87, 87, 89, 90, 87, 87],
    "12r2": [82] * 11,
    "12r3": [97] * 11,
    "12r4": [87, 86, 87, 87, 87, 86, 87, 87, 87, 86, 86],
    "13r1": [70, 68, 68, 71, 70, 68, 68, 70, 70, 68, 68],
    "13r2": [65] * 11,
    "13r3": [82, 83, 83, 82, 82, 83, 83, 82, 82, 83, 83],
    "13r4": [92] * 11,
}
p("cell | " + " | ".join(ARMS))
c3 = True
for c in CELLS:
    got = [run(a, c)["served"] for a in ARMS]
    exp = claimed3[SHORT[c]]
    diff = [ARMS[i] for i in range(11) if got[i] != exp[i]]
    c3 &= not diff
    p("%s | %s | %s" % (SHORT[c], " ".join(map(str, got)), "OK" if not diff else "DIFF " + str(diff)))
verdict[3] = c3

# ---------- Claim 4
p("\n== Claim 4 (non-normal acknowledged decisions)")
p("arm | " + " ".join(SHORT[c] for c in CELLS))
for a in ARMS:
    p("%-9s | %s" % (a, " ".join("%4d" % run(a, c)["nonnormal"] for c in CELLS)))
c4a = all(run(a, c)["nonnormal"] == 0 for a in ("C-30", "C-60", "C-120", "C-300") for c in CELLS)
c4b = all(run(a, c)["nonnormal"] > 0 for a in ("Mplus-30", "V-30") for c in CELLS)
c4c = all((run("Mplus-300", c)["nonnormal"] > 0) == (c == "d20181113-s10-r1-w07") for c in CELLS)
p("C-* all zero:", c4a, "| Mplus-30 & V-30 >=1 in all cells:", c4b, "| Mplus-300 only 13r1:", c4c)
verdict[4] = c4a and c4b and c4c


# ---------- Claim 5
def share(arm, cell, thr):
    v = list(run(arm, cell)["a_r"].values())
    return sum(x > thr for x in v) / len(v), sum(x > thr for x in v), len(v)


p("\n== Claim 5")
exp60 = [0.080, 0.061, 0.041, 0.023, 0.118, 0.077, 0.060, 0.120]
s60 = []
ok60 = True
for i, c in enumerate(CELLS):
    s, k, n = share("Mplus-60", c, 60.0)
    s60.append(s)
    ok = round(s, 3) == exp60[i]
    ok60 &= ok
    p("  Mplus-60 %s: %d/%d = %.4f (claim %.3f) %s" % (SHORT[c], k, n, s, exp60[i], "OK" if ok else "DIFF"))
m60 = statistics.mean(s60)
p("  Mplus-60 mean share(A_r>60s) = %.4f (claim 0.073) %s" % (m60, "OK" if round(m60, 3) == 0.073 else "DIFF"))
s30 = []
for c in CELLS:
    s, k, n = share("Mplus-30", c, 30.0)
    s30.append(s)
    p("  Mplus-30 %s: %d/%d = %.4f" % (SHORT[c], k, n, s))
m30 = statistics.mean(s30)
p("  Mplus-30 mean share(A_r>30s) = %.4f (claim 0.240) %s" % (m30, "OK" if round(m30, 3) == 0.240 else "DIFF"))
expmax = [109.1, 102.9, 99.7, 148.7, 99.1, 194.0, 88.2, 106.3]
okmax = True
for i, c in enumerate(CELLS):
    mx = max(run("C-30", c)["a_r"].values())
    ok = round(mx, 1) == expmax[i]
    okmax &= ok
    p("  C-30 %s max A_r = %.3f s (claim %.1f) %s" % (SHORT[c], mx, expmax[i], "OK" if ok else "DIFF"))
verdict[5] = ok60 and round(m60, 3) == 0.073 and round(m30, 3) == 0.240 and okmax
p("  (context) min A_r over all 88 runs: %.3f s" % min(min(r["a_r"].values()) for r in R.values()))

# ---------- Claim 6
p("\n== Claim 6 (fleet-action sequences)")


def first_div(a, b):
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            return i
    return None if len(a) == len(b) else min(len(a), len(b))


c6 = True
for x in ("30", "60", "120", "300"):
    eq = []
    eqnc = []
    for c in CELLS:
        A, B = run("Mplus-" + x, c), run("C-" + x, c)
        same = A["fleet_full"] == B["fleet_full"]
        same_nc = A["fleet_nocand"] == B["fleet_nocand"]
        eq.append(same)
        eqnc.append(same_nc)
        if not same:
            p("   Mplus-%s vs C-%s %s differ: lens %d/%d, first divergence at action #%s; ignoring candidateId equal: %s"
              % (x, x, SHORT[c], len(A["fleet_full"]), len(B["fleet_full"]), first_div(A["fleet_full"], B["fleet_full"]), same_nc))
    p("  Mplus-%s == C-%s in %d/8 cells (%s); ignoring candidateId: %d/8"
      % (x, x, sum(eq), ",".join(SHORT[c] for c, e in zip(CELLS, eq) if e), sum(eqnc)))
    need = 6 if x == "120" else 8
    c6 &= sum(eq) == need
eqv = []
for c in CELLS:
    A, B = run("V-30", c), run("C-30", c)
    eqv.append(A["fleet_full"] == B["fleet_full"])
    if not eqv[-1]:
        p("   V-30 vs C-30 %s differ: first divergence at action #%s" % (SHORT[c], first_div(A["fleet_full"], B["fleet_full"])))
p("  V-30 == C-30 in %d/8 cells" % sum(eqv))
c6 &= all(eqv)
# context: other pairs
for a1, a2 in (("M-30", "C-30"), ("M-30", "V-30"), ("M-30", "Mplus-30"), ("U", "C-30")):
    n = sum(run(a1, c)["fleet_full"] == run(a2, c)["fleet_full"] for c in CELLS)
    p("  (context) %s == %s in %d/8 cells" % (a1, a2, n))
verdict[6] = c6

# ---------- Claim 7
p("\n== Claim 7 (13r1, A_r > 300 s)")
c7 = True
for a in ARMS:
    v = run(a, "d20181113-s10-r1-w07")["a_r"]
    big = sorted((val, rid) for rid, val in v.items() if val > 300)
    p("  %-9s riders with A_r>300: %d %s" % (a, len(big), ["%s %.3f" % (rid[:14], val) for val, rid in big]))
    if a in ("C-300", "Mplus-300"):
        c7 &= len(big) == 1 and round(big[0][0], 1) == 307.3
bigC = [rid for rid, val in run("C-300", "d20181113-s10-r1-w07")["a_r"].items() if val > 300]
bigM = [rid for rid, val in run("Mplus-300", "d20181113-s10-r1-w07")["a_r"].items() if val > 300]
p("  same rider in C-300 and Mplus-300:", bigC == bigM)
verdict[7] = c7

p("\n== Verdicts")
for k in sorted(verdict):
    p("Claim %d: %s" % (k, "MATCH" if verdict[k] else "MISMATCH"))

with open(os.path.join(OUT, "claims-output.txt"), "x", encoding="utf-8") as fh:
    fh.write("\n".join(lines) + "\n")
