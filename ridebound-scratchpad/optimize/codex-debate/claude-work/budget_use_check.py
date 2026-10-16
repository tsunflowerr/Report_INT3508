"""How much of the per-rider dispatch budget do riders actually use? Descriptive, zero-run, existing transcripts only.

For every accepted rider (has an initialPromise ledger entry) and every completed rider (alighted):
  S_drop = sum over later drop-promise revisions of |c|, c = p - e (dispatch part), seconds;
  S_pick = same for the pickup promise, revisions published before boarding only (closed rows excluded);
  k_drop = number of drop revisions with c != 0.
Reported per arm: share with S_drop > 0, distribution of S_drop among exposed riders, share of riders using
>= 50% / >= 90% of the budget B, net signed sum of c among exposed riders.
For U (no budget) the same S_drop is reported, plus the share that would exceed 30/60/120/300 s.

Populations:
  w07  = tier3-w07-v1  (8 cells, 07:00-09:00, measured traffic only): U, C-30, C-60, C-120, C-300
  w07x = tier3-w07x-v1 (same 8 cells): C-90, C-150, C-180, C-240
  t38  = tier3-t38-v1  (34 T3.8 test cells): U, C-30
Usage: python -B budget_use_check.py <out.txt> (mode x)."""
import collections
import pathlib
import statistics
import sys

OPT = pathlib.Path(r"E:/Code/Report_INT3508/ridebound-scratchpad/optimize")
sys.path.insert(0, str(OPT))
import forecast_family_a as fa  # noqa: E402

W07 = pathlib.Path(r"C:/RideBoundData/research/tier3-w07-v1")
W07X = pathlib.Path(r"C:/RideBoundData/research/tier3-w07x-v1")
CELLS_W07 = [f"d201811{d}-s10-r{r}-w07" for d in ("12", "13") for r in (1, 2, 3, 4)]
CELLS_T38 = list(fa.run_t38.PHASES["test"][1])


def q(xs, p):
    """Nearest-rank percentile."""
    if not xs:
        return float("nan")
    xs = sorted(xs)
    k = max(1, min(len(xs), int(-(-p * len(xs) // 1))))
    return xs[k - 1]


def rider_sums(transcript):
    _, _, state = fa.audit_vep.load(transcript)
    table, _ = fa.audit_vep.audit(transcript)
    _, alighted = fa.sweep_analyze.event_times(transcript)
    accepted = set()
    s_drop, s_pick, k_drop, net_drop = (collections.defaultdict(float), collections.defaultdict(float),
                                        collections.defaultdict(int), collections.defaultdict(float))
    for r, coord, seq, kind, pub, v, e, p, x, cc, z, closed in table:
        if kind == "initialPromise":
            if coord == "drop":
                accepted.add(r)
            continue
        if coord == "drop":
            s_drop[r] += abs(cc) / 1000
            net_drop[r] += cc / 1000
            k_drop[r] += cc != 0
        elif coord == "pickup" and not closed:
            s_pick[r] += abs(cc) / 1000
    return accepted, set(alighted), s_drop, s_pick, k_drop, net_drop


def summarize(label, budget, runs):
    acc_all, done_all = [], []
    for run in runs:
        accepted, done, s_drop, s_pick, k_drop, net = rider_sums(run / "transcript-00.ndjson")
        for r in accepted:
            row = (s_drop[r], s_pick[r], k_drop[r], net[r])
            acc_all.append(row)
            if r in done:
                done_all.append(row)
    lines = [f"## {label} (runs {len(runs)}; budget {budget if budget else 'none'})"]
    for pop_name, rows in (("accepted", acc_all), ("completed", done_all)):
        n = len(rows)
        exp = [s for s, _, _, _ in rows if s > 0]
        netexp = [nt for s, _, _, nt in rows if s > 0]
        ks = [k for _, _, k, _ in rows if k > 0]
        pexp = [sp for _, sp, _, _ in rows if sp > 0]
        line = (f"- {pop_name}: n={n}; drop-exposed {len(exp)} ({100 * len(exp) / n:.2f}%); "
                f"S_drop among exposed: mean {statistics.mean(exp) if exp else float('nan'):.1f} s, "
                f"median {q(exp, 0.5):.1f}, p90 {q(exp, 0.9):.1f}, max {max(exp) if exp else float('nan'):.1f}; "
                f"mean S_drop over all riders {sum(exp) / n:.2f} s; "
                f"revisions with c!=0 per exposed rider: max {max(ks) if ks else 0}, "
                f"share with >=2: {100 * sum(k >= 2 for k in ks) / n:.2f}% of all; "
                f"net signed c among exposed: mean {statistics.mean(netexp) if netexp else float('nan'):.1f} s, "
                f"negative (earlier) {sum(nt < 0 for nt in netexp)}; "
                f"pickup-exposed {len(pexp)} ({100 * len(pexp) / n:.2f}%)")
        if budget:
            line += (f"; use >=50% of B: {sum(s >= 0.5 * budget for s, *_ in rows)} "
                     f"({100 * sum(s >= 0.5 * budget for s, *_ in rows) / n:.2f}%), "
                     f">=90% of B: {sum(s >= 0.9 * budget for s, *_ in rows)} "
                     f"({100 * sum(s >= 0.9 * budget for s, *_ in rows) / n:.2f}%), "
                     f"over B (+1 ms tolerance): {sum(s > budget + 0.001 for s, *_ in rows)}")
        else:
            line += "; would exceed " + ", ".join(
                f"{b} s: {100 * sum(s > b for s, *_ in rows) / n:.2f}%" for b in (30, 60, 120, 300))
        lines.append(line)
    return lines


def main(out):
    text = ["# budget_use_check.py: per-rider dispatch-budget use (drop promise), existing runs only", ""]
    text.append("# w07 / w07x: 8 cells 07:00-09:00, 12-13 Nov 2018, measured traffic only")
    for arm, budget, root in (("U", None, W07), ("C-30", 30, W07), ("C-60", 60, W07), ("C-90", 90, W07X),
                              ("C-120", 120, W07), ("C-150", 150, W07X), ("C-180", 180, W07X),
                              ("C-240", 240, W07X), ("C-300", 300, W07)):
        runs = [root / f"{arm}-{c}" for c in CELLS_W07]
        text += summarize(f"w07 {arm}", budget, runs)
    text += ["", "# t38: 34 T3.8 test cells (measured traffic)"]
    for arm, budget in (("U", None), ("C-30", 30)):
        runs = [fa.run_dir("test", arm, c) for c in CELLS_T38]
        text += summarize(f"t38 {arm}", budget, runs)
    body = "\n".join(text) + "\n"
    with open(out, "x", encoding="utf-8", newline="\n") as fh:
        fh.write(body)
    print(body)


if __name__ == "__main__":
    main(sys.argv[1])
