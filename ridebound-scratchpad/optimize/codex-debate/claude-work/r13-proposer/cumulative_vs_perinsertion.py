"""R13 proposer helper (zero-run, read-only on transcripts): when would a CUMULATIVE per-rider dispatch budget
(rule C: sum_j |c_j| <= B) and a PER-INSERTION cap (max_j |c_j| <= B) disagree?

For every accepted rider (drop initialPromise exists) the drop-coordinate dispatch parts c_j = p - e of all later
revisions are collected with the same reader as budget_use_check.py (forecast_family_a.audit_vep.audit; unchanged).
Per population and B in {30, 60, 120, 300} s it reports:
  k2      = riders with >= 2 nonzero c_j;
  cum     = riders with sum |c_j| > B           (a cumulative cap would have been hit at some point);
  per     = riders with max |c_j| > B           (a per-insertion cap would have been hit);
  cumonly = riders with max |c_j| <= B < sum    (ONLY the cumulative rule binds; per-insertion would not).
This is EXPOSURE in arms that did not enforce the cap; under an enforced cap the decisions would differ, so the
numbers are an upper-bound-style screen of how often the cumulative property could matter, not a policy result.

Populations (existing runs only):
  wp14r FREE (b1-ref), LOCKS (c1-nobudget): fixed traffic, 16 cells, 8 vehicles   (E:/RideBoundData/wp14r/development-v6-ledger)
  t38 U: measured traffic, 34 test cells, 8 vehicles                              (C:/RideBoundData/research/tier3-t38-v1)
  wp9 panel B b1 / c1 (4 vehicles), panel A b1 / c1 (8 vehicles): older runner, fixed traffic (E:/RideBoundData/wp9/*-v2)
Usage: python -B cumulative_vs_perinsertion.py <out.txt>   (output opened with mode "x")."""
import collections
import pathlib
import sys
import time
import traceback

OPT = pathlib.Path(r"E:/Code/Report_INT3508/ridebound-scratchpad/optimize")
sys.path.insert(0, str(OPT))
import forecast_family_a as fa  # noqa: E402

BS = (30, 60, 120, 300)
WP14R = pathlib.Path("E:/RideBoundData/wp14r/development-v6-ledger")
WP9 = pathlib.Path("E:/RideBoundData/wp9")


def rider_changes(transcript):
    table, _ = fa.audit_vep.audit(transcript)
    accepted, changes = set(), collections.defaultdict(list)
    for r, coord, seq, kind, pub, v, e, p, x, cc, z, closed in table:
        if coord != "drop":
            continue
        if kind == "initialPromise":
            accepted.add(r)
            continue
        if cc != 0:
            changes[r].append(abs(cc) / 1000.0)
    return accepted, changes


def summarize(label, runs):
    n = 0
    k2 = 0
    exposed = 0
    cum = collections.Counter()
    per = collections.Counter()
    cumonly = collections.Counter()
    k2_sums = []
    failed = 0
    for t in runs:
        try:
            accepted, changes = rider_changes(t)
        except Exception:  # keep going, report
            failed += 1
            sys.stderr.write(f"FAILED {t}\n{traceback.format_exc()}\n")
            continue
        for r in accepted:
            n += 1
            cs = changes.get(r, [])
            if cs:
                exposed += 1
            if len(cs) >= 2:
                k2 += 1
                k2_sums.append(sum(cs))
            s, m = sum(cs), max(cs) if cs else 0.0
            for b in BS:
                cum[b] += s > b
                per[b] += m > b
                cumonly[b] += (m <= b < s)
    lines = [f"## {label}: runs {len(runs)} (failed {failed}); accepted riders n={n}; drop-exposed {exposed} "
             f"({100 * exposed / n if n else float('nan'):.2f}%); >=2 nonzero changes {k2} "
             f"({100 * k2 / n if n else float('nan'):.2f}%)"
             + (f"; sum|c| among k>=2: min {min(k2_sums):.1f} / median {sorted(k2_sums)[len(k2_sums) // 2]:.1f} / "
                f"max {max(k2_sums):.1f} s" if k2_sums else "")]
    for b in BS:
        lines.append(f"  B={b:>3d} s: cumulative-exceed {cum[b]:>4d} ({100 * cum[b] / n:.2f}%) | per-insertion-exceed "
                     f"{per[b]:>4d} ({100 * per[b] / n:.2f}%) | cumulative-ONLY {cumonly[b]:>3d} "
                     f"({100 * cumonly[b] / n:.2f}%)")
    return lines


def wp14r(arm):
    return [r / "attempt-01" / "output" / "transcript-00.ndjson" for r in sorted(WP14R.glob(f"w14-*-{arm}-s7"))
            if (r / "attempt-01" / "output" / "transcript-00.ndjson").exists()]


def wp9(folder, arm):
    return [r / "transcript-00.ndjson" for r in sorted((WP9 / folder).glob(f"*-{arm}"))
            if (r / "transcript-00.ndjson").exists()]


def main(out):
    t0 = time.time()
    pops = [
        ("wp14r FREE b1-ref (8 veh, fixed traffic)", wp14r("b1-ref")),
        ("wp14r LOCKS c1-nobudget (8 veh, fixed traffic)", wp14r("c1-nobudget")),
        ("t38 U (8 veh, measured traffic)", [fa.run_dir("test", "U", c) / "transcript-00.ndjson"
                                            for c in fa.run_t38.PHASES["test"][1]]),
        ("wp9 panel B b1-tight-s7 (4 veh, older runner)", wp9("confirmatory-h6-panelb-v2", "b1-tight-s7")),
        ("wp9 panel B c1-tight-s7 (4 veh, older runner)", wp9("confirmatory-h6-panelb-v2", "c1-tight-s7")),
        ("wp9 panel A b1-tight-s7 (8 veh, older runner)", wp9("confirmatory-h6-panela-v2", "b1-tight-s7")),
        ("wp9 panel A c1-tight-s7 (8 veh, older runner)", wp9("confirmatory-h6-panela-v2", "c1-tight-s7")),
    ]
    text = ["# cumulative_vs_perinsertion.py: when do a cumulative and a per-insertion dispatch cap disagree?",
            "# exposure in arms that did NOT enforce the cap (except c1 arms, which enforce 30 s); descriptive", ""]
    for label, runs in pops:
        text += summarize(label, runs)
        sys.stderr.write(f"done {label} at {time.time() - t0:.0f} s\n")
    text.append(f"\n# elapsed {time.time() - t0:.0f} s")
    body = "\n".join(text) + "\n"
    with open(out, "x", encoding="utf-8", newline="\n") as fh:
        fh.write(body)
    print(body)


if __name__ == "__main__":
    main(sys.argv[1])
