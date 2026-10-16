"""R17 rebuttal: derived counts used in R17-REBUTTAL-CLAUDE.md, computed from this folder's JSON outputs only.
(1) T3.8 per-cell sign of late60 / served, U vs C-30, by window; (2) WP14r first-order cost-first details per arm.
Read-only; output mode "x". Usage: python -B r17_derived_counts.py <out.txt>"""
import collections, json, sys
dial = json.load(open("r17-verify-dial-2026-10-10.json", encoding="utf-8"))["rows"]
t = {(r["arm"], r["cell"]): r["m"] for r in dial if r["pop"] == "t38"}
g = collections.Counter()
for c in sorted({c for _, c in t}):
    u, k, w = t[("U", c)], t[("C-30", c)], c[-3:]
    for name in ("late60", "served"):
        d = u[name] - k[name]
        g[(w, name, ">" if d > 0 else "=" if d == 0 else "<")] += 1
lines = ["# r17_derived_counts.py", "## T3.8 per-cell sign U vs C-30 (window, metric, sign: cells)"]
lines += [f"{w} {m} U{s}C: {n}" for (w, m, s), n in sorted(g.items())]
wp = json.load(open("r17-wp14r-check-2026-10-10.json", encoding="utf-8"))
lines.append("## WP14r first-order cost-first (differing frames)")
for arm in ("LOCKS", "C-120", "C-60", "C-30"):
    det, cnt = wp[arm]["details"], wp[arm]["counts"]
    lines.append(f"{arm}: differ {len(det)}; extra drop >0 {sum(d['extra_drop_s'] > 0 for d in det)}; cost-first plan "
                 f"moves >=1 incumbent {sum(d['cf_vehicles_with_drop_move'] >= 1 for d in det)}; new request moved to "
                 f"another vehicle (2+ vehicles changed) {sum(d['changed_vehicles'] >= 2 for d in det)}; mean saving per "
                 f"new-request frame {100 * sum(d['rel_saving'] for d in det) / cnt['with_new']:.2f}%")
with open(sys.argv[1], "x", encoding="utf-8", newline="\n") as fh:
    fh.write("\n".join(lines) + "\n")
print("\n".join(lines))
