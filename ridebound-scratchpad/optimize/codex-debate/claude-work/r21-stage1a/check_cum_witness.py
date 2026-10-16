"""R21 Stage 1a (Claude analyst), step 3: context for the C-120 cumulative-only prune records (P5), from the
extraction files only. For each record: the witness rider's final sum |c| (should be >= the witness 'before'), its
nonzero-change count and lateness vs its first drop promise; the new request's final lifecycle in C-120 and whether
the same request was served in C-30 / U (riders.tsv holds accepted riders only, so 'not in file' = not accepted).
Usage: python -B check_cum_witness.py <prefix> <out.txt>   (out opened with mode "x")
"""
import json
import pathlib
import sys


def main(prefix, out):
    rows = {}
    with open(f"{prefix}-riders.tsv", encoding="utf-8") as fh:
        header = fh.readline().rstrip("\n").split("\t")
        for line in fh:
            r = dict(zip(header, line.rstrip("\n").split("\t")))
            rows[(r["arm"], r["cell"], r["requestId"])] = r
    runs = json.loads(pathlib.Path(f"{prefix}-runs.json").read_text(encoding="utf-8"))
    lines = ["# check_cum_witness.py: C-120 cumulative-only prune records, witness and new-request context"]
    for rec in runs:
        if rec["arm"] != "C-120":
            continue
        for det in rec["cumulativeOnlyOwn"]:
            cell = rec["cell"]
            for rider, before, delta, after, limit in det["witness"]:
                w = rows.get(("C-120", cell, rider))
                lat = (int(w["A"]) - int(w["p0"])) / 1000 if w and w["A"] else None
                lines.append(f"{cell}: witness {rider[:14]} before {before / 1000:.1f} s + delta {delta / 1000:.1f} s = "
                             f"after {after / 1000:.1f} s > limit {limit / 1000:.0f} s | witness final sum|c| "
                             f"{int(w['sumAbsC']) / 1000 if w else 'n/a'} s, nonzero c {w['nonzeroC'] if w else 'n/a'}, "
                             f"lifecycle {w['lifecycle'] if w else 'n/a'}, A - p0 {lat} s")
            for new in det["newRequestIds"]:
                status = {}
                for arm in ("C-120", "C-30", "U"):
                    r = rows.get((arm, cell, new))
                    status[arm] = "not accepted" if r is None else ("served" if r["A"] else r["lifecycle"])
                lines.append(f"    new request {new[:14]}: C-120 {status['C-120']}; C-30 {status['C-30']}; U {status['U']}")
    text = "\n".join(lines) + "\n"
    with open(out, "x", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    sys.stdout.write(text)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    main(sys.argv[1], sys.argv[2])
