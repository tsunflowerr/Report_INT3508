"""Answer (2026-10-06): (1) under 'free' pooling (U = no 30 s cap) how late are riders vs the first promise and how
much of it is caused by pooling decisions; (2) how much does one pooling decision move a rider's drop ETA (|c| per
revision, sum per rider); (3) which constraints prune candidates (codes in executionEvidence.prunedCandidates) and how
many requests end unserved. Arms U and C-30 on the 34 T3.8 test cells. Usage: python -B constraints_and_pooling.py <out>"""
import base64, collections, json, pathlib, statistics as st, sys
HERE = pathlib.Path(__file__).resolve().parents[1]
TANG3 = HERE.parent / "tang3"
for sub in ("sweep", "evidence", "t38"):
    sys.path.insert(0, str(TANG3 / sub))
import audit_vep, sweep_analyze, run_t38, t38_calibrate
CELLS = run_t38.PHASES["test"][1]
def q(xs, p):
    xs = sorted(xs); return xs[min(len(xs) - 1, int(p * len(xs)))] if xs else None
out = ["# constraints_and_pooling.py (34 T3.8 test cells)"]
for arm in ("U", "C-30"):
    codes, lifecycle = collections.Counter(), collections.Counter()
    late, c_rev, c_rider, disp_late, tot_late = [], [], [], 0, 0
    decisions = 0
    for cell in CELLS:
        t = run_t38.OUT_ROOT / t38_calibrate.effective(f"{arm}-{cell}") / "transcript-00.ndjson"
        _, _, state = audit_vep.load(t)
        lifecycle.update(r["lifecycle"] for r in state["requests"])
        table, _ = audit_vep.audit(t)
        _, alighted = sweep_analyze.event_times(t)
        first, csum = {}, {}
        for r, c, s, k, pub, v, e, p, x, cc, z, closed in table:
            if c != "drop":
                continue
            if k == "initialPromise":
                first[r] = p; csum[r] = 0
            else:
                csum[r] += cc
                if cc != 0:
                    c_rev.append(abs(cc))
        for r in first:
            if r in alighted:
                a = alighted[r] - first[r]; late.append(a)
                c_rider.append(sum(abs(cc) for rr, c, s, k, pub, v, e, p, x, cc, z, closed in table if rr == r and c == "drop" and k != "initialPromise"))
                if a > 60_000:
                    tot_late += a; disp_late += csum[r]
        with open(t, encoding="utf-8") as h:
            for line in h:
                rec = json.loads(line)
                env = json.loads(base64.b64decode(rec["frameBase64"]))
                if env.get("messageType") != "decision":
                    continue
                decisions += 1
                ev = ((env.get("payload") or {}).get("solver") or {}).get("executionEvidence") or {}
                for prune in ev.get("prunedCandidates", []):
                    codes[prune["code"]] += 1
    n = len(late)
    out.append(f"\n== {arm}: requests {sum(lifecycle.values())}, lifecycle {dict(lifecycle)}")
    out.append(f"  served riders {n}: late vs first drop promise > 60 s {sum(1 for a in late if a > 60000) / n:.4f}, > 120 s {sum(1 for a in late if a > 120000) / n:.4f}, "
               f"> 300 s {sum(1 for a in late if a > 300000) / n:.4f}; mean {st.mean(late) / 1000:+.1f} s; p90 {q(late, .9) / 1000:+.1f} s; max {max(late) / 1000:+.1f} s")
    out.append(f"  of the late seconds (riders late > 60 s), caused by pooling decisions (sum of p - e): {100 * disp_late / tot_late:.1f}%")
    out.append(f"  drop revisions with a pooling-caused change (c != 0): {len(c_rev)}; |c| median {q(c_rev, .5) / 1000:.1f} s, p90 {q(c_rev, .9) / 1000:.1f} s, max {max(c_rev) / 1000:.1f} s")
    out.append(f"  per rider total |c|: zero for {sum(1 for v in c_rider if v == 0) / n:.3f} of riders; > 30 s {sum(1 for v in c_rider if v > 30000) / n:.3f}; > 60 s {sum(1 for v in c_rider if v > 60000) / n:.3f}; > 120 s {sum(1 for v in c_rider if v > 120000) / n:.3f}; max {max(c_rider) / 1000:.1f} s")
    out.append(f"  decisions {decisions}; pruned candidates by code: {dict(codes.most_common())}")
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
