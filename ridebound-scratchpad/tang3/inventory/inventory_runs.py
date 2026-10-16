"""Count run directories and bytes of the Tier 2 / Tier 3 output roots, read-only (2026-09-29).

For the thesis table bang:quymo (handoff 2026-09-29 §7 errata 6). Per root:
- directories, and how many hold summary.json, failure-00.json, both, neither;
- directories whose name ends with -rerun1 (reruns kept next to the failed original);
- total bytes of every file under the root (summed per file, not `du`).

Usage: python -B inventory_runs.py <new-log-path>   (mode "x": never overwrites)
"""
import datetime
import os
import pathlib
import sys

ROOTS = [
    ("Tang 2 (deadline-v1)", r"E:/RideBoundData/research/deadline-v1"),
    ("Tang 2 pipeline pilot (not evidence)", r"E:/RideBoundData/research/deadline-v1-pilot"),
    ("Tang 3 pilot T3.7", r"E:/RideBoundData/research/tier3-pilot-v1"),
    ("Tang 3 sweep C/M+", r"E:/RideBoundData/research/tier3-sweep-v1"),
    ("Tang 3 no-worse (b)", r"C:/RideBoundData/research/tier3-sweep-noworse-v1"),
    ("Tang 3 world smoke v1", r"E:/RideBoundData/research/tier3-world-smoke-v1"),
    ("Tang 3 world smoke v1.1", r"E:/RideBoundData/research/tier3-world-v11-smoke"),
    # Added 2026-09-29 after task A (the first log, inventory-2026-09-29.txt, predates these roots).
    ("Tang 3 task A (a)", r"C:/RideBoundData/research/tier3-vm-v11-a"),
    ("Tang 3 task A (b)", r"C:/RideBoundData/research/tier3-vm-v11-b"),
    ("Tang 3 world smoke v1.2", r"C:/RideBoundData/research/tier3-world-v12-smoke"),
    ("Tang 3 task B 07-09h", r"C:/RideBoundData/research/tier3-w07-v1"),
]


def tree_bytes(path):
    total = 0
    files = 0
    for base, _dirs, names in os.walk(path):
        for name in names:
            total += os.path.getsize(os.path.join(base, name))
            files += 1
    return total, files


def main(log_path):
    lines = [f"# inventory_runs.py, run {datetime.datetime.now().isoformat(timespec='seconds')}",
             "root | dirs | summary | failure-00 | both | neither | -rerun1 dirs | files | bytes | GB (1e9) | GiB"]
    for label, root in ROOTS:
        p = pathlib.Path(root)
        if not p.exists():
            lines.append(f"{label} | {root} | MISSING")
            continue
        dirs = sorted(d for d in p.iterdir() if d.is_dir())
        summ = {d.name for d in dirs if (d / "summary.json").exists()}
        fail = {d.name for d in dirs if (d / "failure-00.json").exists()}
        names = {d.name for d in dirs}
        reruns = sorted(n for n in names if n.endswith("-rerun1"))
        size, files = tree_bytes(p)
        lines.append(f"{label} ({root}) | {len(dirs)} | {len(summ)} | {len(fail)} | {len(summ & fail)} | "
                     f"{len(names - summ - fail)} | {len(reruns)} | {files} | {size} | {size / 1e9:.2f} | {size / 2**30:.2f}")
        for n in reruns:
            lines.append(f"    rerun: {n}; original has summary: {(p / n[:-len('-rerun1')] / 'summary.json').exists()}, "
                         f"original has failure-00: {(p / n[:-len('-rerun1')] / 'failure-00.json').exists()}")
        neither = sorted(names - summ - fail)
        if neither:
            lines.append(f"    neither summary nor failure-00 ({len(neither)}): " + ", ".join(neither))
    text = "\n".join(lines) + "\n"
    with open(log_path, "x", encoding="utf-8") as fh:
        fh.write(text)
    sys.stdout.write(text)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: inventory_runs.py <new-log-path>")
    main(sys.argv[1])
