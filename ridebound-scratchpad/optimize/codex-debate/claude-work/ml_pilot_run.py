"""ML pilot analysis exactly per ML-PILOT-SEALED.md (SHA-256 93f6b968..., sealed 2026-10-08 22:46:17). Run once.
Env: C:/RideBoundData/envs/ml-v1 (sklearn 1.7.2). Input: riders-causal-2026-10-08.csv (SHA-256 7075ad97...).
Lateness is A - F in seconds; rates are percent of the test cohort (all first drop promises = completed riders).
Usage: python -B ml_pilot_run.py <csv> <report-out> <rows-out> (both outputs mode x)."""
import csv
import math
import sys

import numpy as np
import sklearn
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.linear_model import QuantileRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

BASE = ["clock_min", "horizon_s", "pick_s", "fc_ext_s", "maxride_s", "room_s"]
STATE = ["other_assigned", "other_onboard"]


def hgb():
    return HistGradientBoostingRegressor(loss="quantile", quantile=0.90, learning_rate=0.05, max_iter=100,
                                         max_leaf_nodes=7, min_samples_leaf=20, l2_regularization=1.0,
                                         random_state=7, early_stopping=False)


def linqr():
    return make_pipeline(StandardScaler(), QuantileRegressor(quantile=0.90, alpha=1.0, solver="highs"))


MODELS = {"HGB": (hgb, BASE + STATE), "HGB-nostate": (hgb, BASE), "LinQR": (linqr, BASE + STATE)}


def X(rs, feats):
    return np.array([[r[f] for f in feats] for r in rs])


def metrics(lat, ext, hor):
    n = len(lat)
    s = sorted(ext)
    return dict(n=n, Y60=100 * float(np.sum(lat > 60)) / n, early60=100 * float(np.sum(lat < -60)) / n,
                sym=100 * float(np.sum(np.abs(lat) <= 60)) / n, ext=float(np.mean(ext)),
                p90=float(s[math.ceil(0.9 * n) - 1]), hor=float(np.mean(hor)))


def wins(m, c):
    return (m["Y60"] < c["Y60"] and m["ext"] <= c["ext"] + 1 and m["p90"] <= c["p90"] + 15
            and m["early60"] <= c["early60"] + 1)


def main():
    rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8")))
    for r in rows:
        for k in BASE + STATE + ["resid_s"]:
            r[k] = float(r[k])
    out = [f"# ml_pilot_run.py (sealed plan 93f6b968...; sklearn {sklearn.__version__}); lateness = A - F (s); rates in %"]
    table, res = [], {}
    for world, arms, tests in (("measured", ("U", "C-30"), ("test15", "test16")),
                               ("static", ("FREE", "LOCKS", "C-120", "C-60", "C-30"), ("test13",))):
        for arm in arms:
            sub = [r for r in rows if r["world"] == world and r["arm"] == arm]
            fit = [r for r in sub if r["role"] == "fit"]
            cal = [r for r in sub if r["role"] == "cal"]
            fitted = {}
            for name, (mk, feats) in MODELS.items():
                m = mk()
                m.fit(X(fit, feats), np.array([r["resid_s"] for r in fit]))
                fitted[name] = (m, feats)
            mdelta = float(np.mean([r["fc_ext_s"] for r in cal]))
            out.append(f"\n== {world} {arm}: fit {len(fit)}, cal {len(cal)}, cal mean delta (D0-P0) {mdelta:.2f} s")
            for E in (15, 30, 60):
                rules = {}
                for name, (m, feats) in fitted.items():
                    w = np.maximum(0, m.predict(X(cal, feats)))
                    mw = float(np.mean(w))
                    if E < mdelta:
                        rules[name] = None
                    elif mw > 0:
                        rules[name] = ("rho", (E - mdelta) / mw)
                    else:
                        rules[name] = ("flat", E - mdelta)
                for test in tests:
                    tr = [r for r in sub if r["role"] == test]
                    for wtag in (("all", "w08", "w17") if world == "static" else ("all",)):
                        trw = tr if wtag == "all" else [r for r in tr if r["window"] == wtag]
                        resid = np.array([r["resid_s"] for r in trw])
                        dlt = np.array([r["fc_ext_s"] for r in trw])
                        hor = np.array([r["horizon_s"] for r in trw])
                        M = {"uniform": metrics(resid + dlt - E, np.full(len(trw), float(E)), hor + E)}
                        if E >= mdelta:
                            extra = E - mdelta
                            M["fc+uniform"] = metrics(resid - extra, dlt + extra, hor + dlt + extra)
                        for name, (m, feats) in fitted.items():
                            rule = rules[name]
                            if rule is None:
                                continue
                            wt = np.maximum(0, m.predict(X(trw, feats)))
                            add = rule[1] * wt if rule[0] == "rho" else np.full(len(trw), rule[1])
                            M[name] = metrics(resid - add, dlt + add, hor + dlt + add)
                        for meth, mm in M.items():
                            table.append((world, arm, test, wtag, E, meth, mm))
                            res[(world, arm, test, wtag, E, meth)] = mm
                        if wtag == "all":
                            out.append(f"  E {E:>2d} {test} (n {len(trw)}): " + " | ".join(
                                f"{k} Y60 {v['Y60']:.2f} sym {v['sym']:.1f} early {v['early60']:.1f} ext {v['ext']:.1f} p90 {v['p90']:.1f}"
                                for k, v in M.items()))

    def g(*k):
        return res.get(k)

    out.append("\n== Sealed predictions (E = 30)")
    ml1 = []
    for d in ("test15", "test16"):
        a, b = g("measured", "C-30", d, "all", 30, "fc+uniform"), g("measured", "C-30", d, "all", 30, "HGB")
        if a and b:
            ml1.append(a["Y60"] - b["Y60"] < 1)
            out.append(f"  ML1 {d}: C-30 gain of HGB over fc+uniform = {a['Y60'] - b['Y60']:+.2f} pp")
        else:
            ml1.append(False)
            out.append(f"  ML1 {d}: infeasible")
    out.append(f"  ML1 {'TRUE' if all(ml1) else 'FALSE'}")
    ml2 = []
    for d in ("test15", "test16"):
        h = g("measured", "U", d, "all", 30, "HGB")
        for ctl in ("uniform", "fc+uniform"):
            c = g("measured", "U", d, "all", 30, ctl)
            if h and c:
                ok = c["Y60"] - h["Y60"] >= 1 and wins(h, c)
                out.append(f"  ML2 {d} vs {ctl}: gain {c['Y60'] - h['Y60']:+.2f} pp, guards {'pass' if wins(h, c) else 'fail'} -> {'ok' if ok else 'no'}")
            else:
                ok = False
                out.append(f"  ML2 {d} vs {ctl}: infeasible")
            ml2.append(ok)
    out.append(f"  ML2 {'TRUE' if all(ml2) else 'FALSE'}")
    h, c = g("static", "FREE", "test13", "all", 30, "HGB"), g("static", "FREE", "test13", "all", 30, "uniform")
    pos = all(g("static", "FREE", "test13", w, 30, "uniform")["Y60"] - g("static", "FREE", "test13", w, 30, "HGB")["Y60"] > 0
              for w in ("w08", "w17"))
    ml3 = c["Y60"] - h["Y60"] >= 3 and pos and wins(h, c)
    out.append(f"  ML3 static FREE: gain {c['Y60'] - h['Y60']:+.2f} pp; positive in w08 and w17: {pos}; "
               f"guards {'pass' if wins(h, c) else 'fail'} -> {'TRUE' if ml3 else 'FALSE'}")
    hits = []
    for world, arms, tests, ref in (("static", ("FREE", "LOCKS"), ("test13",), "uniform"),
                                    ("measured", ("U",), ("test15", "test16"), "fc+uniform")):
        for arm in arms:
            for d in tests:
                cref = g(world, "C-30", d, "all", 30, ref)
                for name in MODELS:
                    m = g(world, arm, d, "all", 30, name)
                    if m is None or cref is None:
                        continue
                    match = m["Y60"] <= cref["Y60"] and m["sym"] >= cref["sym"]
                    if match:
                        hits.append((world, arm, d, name))
                    out.append(f"  ML4 {world} {arm} {d} {name}: Y60 {m['Y60']:.2f} vs C-30 {cref['Y60']:.2f}; "
                               f"sym {m['sym']:.1f} vs {cref['sym']:.1f} -> {'MATCH' if match else 'no'}")
    out.append(f"  ML4 {'TRUE' if not hits else 'FALSE'} (matches: {hits})")
    ml5 = []
    for world, arm, d, ctl in (("measured", "U", "test15", "fc+uniform"), ("measured", "U", "test16", "fc+uniform"),
                               ("static", "FREE", "test13", "uniform")):
        c = g(world, arm, d, "all", 30, ctl)
        gf = c["Y60"] - g(world, arm, d, "all", 30, "HGB")["Y60"]
        gn = c["Y60"] - g(world, arm, d, "all", 30, "HGB-nostate")["Y60"]
        if gf > 0:
            ml5.append(gf - gn >= gf / 2)
        out.append(f"  ML5 {world} {arm} {d}: G_full {gf:+.2f}, G_nostate {gn:+.2f}"
                   + (f" -> {'ok' if gf - gn >= gf / 2 else 'no'}" if gf > 0 else " (G_full <= 0: not applicable)"))
    out.append(f"  ML5 {'not applicable' if not ml5 else ('TRUE' if all(ml5) else 'FALSE')}")
    out.append(f"  KILL (ML2 and ML3 both fail): {'YES' if (not all(ml2)) and (not ml3) else 'no'}")
    text = "\n".join(out) + "\n"
    open(sys.argv[2], "x", encoding="utf-8", newline="\n").write(text)
    print(text)
    with open(sys.argv[3], "x", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["world", "arm", "test", "window", "E", "method", "n", "Y60", "early60", "sym", "ext", "p90", "hor"])
        for world, arm, test, wtag, E, meth, mm in table:
            w.writerow([world, arm, test, wtag, E, meth, mm["n"], round(mm["Y60"], 3), round(mm["early60"], 3),
                        round(mm["sym"], 3), round(mm["ext"], 3), round(mm["p90"], 3), round(mm["hor"], 3)])


if __name__ == "__main__":
    main()
