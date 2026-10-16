"""R16 evidence, Q3 add-on (zero-run, read-only): in which T3.8 window / day do the U riders with >= 2 nonzero drop
dispatch changes, and the cumulative-only riders at B = 90/120/180, sit?  Reuses q3_multi_change_riders.analyze
(imported, unchanged) per cell.
Usage: python -B q3_t38_windows.py <out.txt>   (out opened with mode "x"; <= 4 processes)."""
import collections
import pathlib
import sys
from concurrent.futures import ProcessPoolExecutor

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import q3_multi_change_riders as q3  # noqa: E402


def job(cell):
    label, rows = q3.analyze((cell, q3.fa.run_dir("test", "U", cell) / "transcript-00.ndjson"))
    return cell, rows


def main():
    out = sys.argv[1]
    cells = list(q3.fa.run_t38.PHASES["test"][1])
    with ProcessPoolExecutor(max_workers=4) as pool:
        res = list(pool.map(job, cells))
    k2 = collections.Counter()
    acc = collections.Counter()
    cum = {b: collections.Counter() for b in (90, 120, 180)}
    detail = []
    for cell, rows in res:
        w = cell[-3:]
        acc[w] += len(rows)
        for r in rows:
            if r["k"] >= 2:
                k2[w] += 1
                detail.append(f"{cell}: sizes {[round(s, 1) for s in r['sizes']]} co-riders {r['co']} direct {r['direct_min']:.1f} min")
            for b in cum:
                if r["sizes"] and max(r["sizes"]) <= b < sum(r["sizes"]):
                    cum[b][w] += 1
    lines = ["# q3_t38_windows.py: T3.8 U riders with >= 2 nonzero drop dispatch changes, by window", ""]
    for w in sorted(acc):
        lines.append(f"{w}: accepted {acc[w]}; k>=2 {k2[w]}; cumulative-only at B=90/120/180: "
                     f"{cum[90][w]}/{cum[120][w]}/{cum[180][w]}")
    lines += ["", "# each k>=2 rider:"] + sorted(detail)
    text = "\n".join(lines) + "\n"
    with open(out, "x", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(text)


if __name__ == "__main__":
    main()
