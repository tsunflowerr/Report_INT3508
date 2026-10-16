"""Tier-2 analysis (plan T2.9) against the sealed predictions. Read-only.

Usage: analyze.py <predictions.csv> [--out report.md]

Prints, in this order (nothing is pooled before the full table is printed):
  0. invariant checks (conduct arms never commitment-infeasible; no selection-noop-invariant)
  1. full prediction-outcome table (every row of predictions.csv)
  2. count table: arm x window x k x label group
  3. accuracy by (stage, window) over determinable (non-weak) pairs, and the weak cases apart
  4. 2A minimum feasible deadline per cell next to the reference max M+
  5. 2B directional table (observed counts) next to the sealed expectations
  6. threshold and negation conditions of the preregistration
  7. descriptive exact McNemar, dl-30 vs conduct-30, per panel/window
  8. secondary: accepted counts where both arms completed
"""
from __future__ import annotations

import csv
import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path

import classify
import holdout_predict as hp
import run_deadline as rd

OUT = rd.OUT_ROOT


def label_of(job: str) -> str:
    # AMENDMENTS.md A2: a recorded host failure is replaced by its rerun.
    directory = rd.effective_output(job)
    if not directory.exists():
        return "pending"
    return classify.classify_output(directory)


def group(label: str) -> str:
    if label.startswith("commitment-all-rejected/"):
        return "commitment-all-rejected"
    if label.startswith("commitment-noop-rejected/"):
        return "commitment-noop-rejected"
    return label


def accepted(job: str):
    run = rd.effective_output(job) / "run-00.json"
    if not run.exists():
        return None
    return len(json.loads(run.read_text(encoding="utf-8"))["semantic"]["acceptedRequestIds"])


def job_name(row) -> str:
    return f"{row['arm']}-k{row['k']}-{row['cell']}-s7"


def correct(prediction: str, label: str):
    if label in ("pending", "no-artifact"):
        return None
    infeasible = classify.is_commitment_infeasible(label)
    if prediction == "commitment-infeasible":
        return infeasible
    if prediction == "not-commitment-infeasible":
        return not infeasible
    return label == "window-wall"  # weak prediction


def mcnemar_exact(b: int, c: int) -> float:
    n = b + c
    if n == 0:
        return 1.0
    k = min(b, c)
    tail = sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n
    return min(1.0, 2 * tail)


def main() -> int:
    rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8")))
    out_lines: list[str] = []

    def emit(line: str = "") -> None:
        print(line)
        out_lines.append(line)

    # 0. invariants over every existing output
    emit("## 0. Invariants")
    bad_conduct, bad_selection = [], []
    for directory in sorted(OUT.iterdir()) if OUT.exists() else []:
        label = classify.classify_output(directory)
        if label == "selection-noop-invariant":
            bad_selection.append(directory.name)
        if (directory.name.startswith("conduct-30") or directory.name.startswith("ctl-conduct")) \
                and classify.is_commitment_infeasible(label):
            bad_conduct.append(directory.name)
    emit(f"conduct arms commitment-infeasible: {len(bad_conduct)} {bad_conduct}")
    emit(f"selection-noop-invariant anywhere: {len(bad_selection)} {bad_selection}")

    # 1. full table
    emit("\n## 1. Prediction-outcome table")
    emit("stage\twindow\tarm\tk\tcell\ttau_s\tref_T_s\tref_C_s\tfar\tweak\tprediction\toutcome\tcorrect")
    results = []
    for row in rows:
        job = job_name(row)
        label = label_of(job)
        ok = correct(row["prediction"], label)
        results.append((row, label, ok))
        emit("\t".join([row["stage"], row["window"], row["arm"], row["k"], row["cell"],
                        row["tau_s"] or "-", row["reference_T_s"], row["reference_C_s"],
                        row["far_from_fallback"], row["weak"], row["prediction"], label,
                        "-" if ok is None else ("yes" if ok else "NO")]))

    # 2. count table
    emit("\n## 2. Counts (stage x arm x window x k x label group)")
    counts = defaultdict(Counter)
    for row, label, _ in results:
        counts[(row["stage"], row["arm"], row["window"], row["k"])][group(label)] += 1
    for key in sorted(counts):
        emit(f"{key[0]}\t{key[1]}\t{key[2]}\tk={key[3]}\t" + ", ".join(
            f"{g}={n}" for g, n in sorted(counts[key].items())))

    # 3. accuracy
    emit("\n## 3. Accuracy over determinable (non-weak) pairs")
    acc = defaultdict(lambda: [0, 0])
    weak = []
    for row, label, ok in results:
        if ok is None:
            continue
        if row["weak"] == "True":
            weak.append((row, label, ok))
            continue
        key = (row["stage"], row["window"])
        acc[key][0] += int(ok)
        acc[key][1] += 1
    for key in sorted(acc):
        hit, n = acc[key]
        emit(f"{key[0]}\t{key[1]}\t{hit}/{n}\t{100 * hit / n:.1f}%")
    emit(f"weak predictions: {len(weak)}; correct {sum(1 for w in weak if w[2])}")
    for row, label, ok in weak:
        emit(f"  weak\t{job_name(row)}\tpredicted window-wall\toutcome {label}")

    # 4. minimum feasible deadline, 2A
    emit("\n## 4. 2A minimum feasible deadline per cell")
    emit("k\tcell\tmin_l_feasible\tref_max_Mplus_s")
    for k in (0, 1):
        for cell in rd.PANEL_A["cells"]:
            feasible = [l for l in (30, 60, 120)
                        if (lab := label_of(f"dl-{l}-k{k}-{cell}-s7")) not in ("pending", "no-artifact")
                        and not classify.is_commitment_infeasible(lab)]
            ref = hp.reference_output(rd.PANEL_A, k, cell)
            max_mplus = "-"
            if (ref / "transcript-00.ndjson").exists():
                chains, _, _ = hp.trajectory(ref)
                values = [max([0] + [p - chain[0][1] for _, p in chain]) for chain in chains.values()]
                max_mplus = f"{max(values) / 1000:.1f}" if values else "-"
            emit(f"{k}\t{cell}\t{min(feasible) if feasible else 'none(>120)'}\t{max_mplus}")

    # 5. 2B directional table
    emit("\n## 5. 2B directional table (commitment-infeasible cells / 8)")
    expected = {
        "w08": {"conduct-30": "0/8", "dl-30": ">=4/8", "dl-120": "<=1/8",
                "dl2-30": ">= dl-30 per cell", "visible-30": ">=4/8"},
        "w17": {"conduct-30": "0/8", "dl-30": "<=1/8", "dl-120": "0/8",
                "dl2-30": ">=4/8", "visible-30": ">=4/8"},
    }
    observed = {}
    for window in ("w08", "w17"):
        cells = [c for c in rd.PANEL_DEV["cells"] if c.endswith(window)]
        for arm in ("conduct-30", "dl-30", "dl-60", "dl-120", "dl2-30", "visible-30"):
            labels = [label_of(f"{arm}-k1-{c}-s7") for c in cells]
            done = [l for l in labels if l not in ("pending", "no-artifact")]
            n = sum(classify.is_commitment_infeasible(l) for l in done)
            observed[(window, arm)] = (n, len(done), labels, cells)
            emit(f"{window}\t{arm}\t{n}/{len(done)} run\texpected {expected[window].get(arm, '-')}")
    night = {arm: observed[("w17", arm)][0] for arm in ("conduct-30", "dl-30", "dl-120", "dl2-30", "visible-30")}
    row_w17 = (night["conduct-30"] == 0 and night["dl-30"] <= 1 and night["dl-120"] == 0
               and night["dl2-30"] >= 4 and night["visible-30"] >= 4)
    # dl2-30 >= dl-30 per cell, morning
    n08, _, l2, _ = observed[("w08", "dl2-30")]
    _, _, l1, _ = observed[("w08", "dl-30")]
    per_cell = all(classify.is_commitment_infeasible(a) or not classify.is_commitment_infeasible(b)
                   for a, b in zip(l2, l1))
    emit(f"w17 row as expected: {row_w17}; w08 dl2-30 >= dl-30 per cell: {per_cell}")

    # 6. thresholds
    emit("\n## 6. Thresholds")
    hit, n = acc.get(("2b", "w17"), [0, 0])
    night_acc = hit / n if n else float("nan")
    emit(f"2B night accuracy {hit}/{n} = {100 * night_acc:.1f}% (>= 90% needed); w17 row {row_w17}")
    emit(f"2B confirmed on held-out set: {bool(n) and night_acc >= 0.9 and row_w17}")
    a_hit = sum(acc[k][0] for k in acc if k[0] == "2a")
    a_n = sum(acc[k][1] for k in acc if k[0] == "2a")
    dl30_k1 = [label_of(f"dl-30-k1-{c}-s7") for c in rd.PANEL_A["cells"]]
    dl30_inf = sum(classify.is_commitment_infeasible(l) for l in dl30_k1)
    emit(f"2A accuracy {a_hit}/{a_n}; dl-30 k=1 commitment-infeasible {dl30_inf}/20 (>= 11 needed)")
    emit(f"2A confirmed (controlled mechanism): {bool(a_n) and a_hit / a_n >= 0.9 and dl30_inf >= 11}")
    late_night = sum(l == "commitment-all-rejected/deadline-late" or l == "commitment-noop-rejected/deadline-late"
                     for l in observed[("w17", "dl-30")][2])
    emit("negations: night accuracy < 75%: "
         f"{bool(n) and night_acc < 0.75}; night dl-30 deadline-late >= 3/8: {late_night >= 3} ({late_night}); "
         f"night dl2-30 and visible-30 both <= 2/8: {night['dl2-30'] <= 2 and night['visible-30'] <= 2}")

    # 7. McNemar
    emit("\n## 7. Exact McNemar (descriptive only): dl-30 vs conduct-30, commitment-infeasible")
    for name, panel, window in (("2A", rd.PANEL_A, ""), ("2B", rd.PANEL_DEV, "w08"), ("2B", rd.PANEL_DEV, "w17")):
        cells = [c for c in panel["cells"] if c.endswith(window)] if window else panel["cells"]
        b = c = 0
        for cell in cells:
            x = label_of(f"dl-30-k1-{cell}-s7")
            y = label_of(f"conduct-30-k1-{cell}-s7")
            if "pending" in (x, y):
                continue
            xi, yi = classify.is_commitment_infeasible(x), classify.is_commitment_infeasible(y)
            b += int(xi and not yi)
            c += int(yi and not xi)
        emit(f"{name} {window or 'w08'}\tdl-30 only {b}\tconduct-30 only {c}\tp = {mcnemar_exact(b, c):.4f}")

    # 8. secondary: accepted where both completed
    emit("\n## 8. Accepted requests where both arms completed (dl-30 vs conduct-30, k=1)")
    for panel in (rd.PANEL_A, rd.PANEL_DEV):
        for cell in panel["cells"]:
            x, y = f"dl-30-k1-{cell}-s7", f"conduct-30-k1-{cell}-s7"
            if label_of(x) == "completed" and label_of(y) == "completed":
                emit(f"{cell}\tdl-30 {accepted(x)}\tconduct-30 {accepted(y)}")

    if "--out" in sys.argv:
        target = Path(sys.argv[sys.argv.index("--out") + 1])
        with open(target, "x", encoding="utf-8", newline="\n") as handle:
            handle.write("\n".join(out_lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
