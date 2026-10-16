"""Central Tier-2 figure (plan T2.9): morning vs evening, four gate families at a 30 s cap.

Development panel (2B), k = 1. For each window and family: bar = observed share of cells that
are commitment-infeasible; dot = share predicted commitment-infeasible in the sealed
predictions.csv (the conduct family has no prediction row; Theorem 4(a) predicts 0).
Read-only except the output figure (written with mode "x").

Usage: figure_families.py <predictions.csv> <out.pdf>
"""
from __future__ import annotations

import csv
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

import classify  # noqa: E402
import run_deadline as rd  # noqa: E402

FAMILIES = [("C\nhành vi", "conduct-30"), ("M⁺\nhạn chót\nmột chiều", "dl-30"),
            ("M\nhạn chót\nhai chiều", "dl2-30"), ("V\nkết quả", "visible-30")]
WINDOWS = [("w08", "Sáng 8:00–10:00 (tắc tăng)"), ("w17", "Tối 17:00–19:00 (tắc giảm)")]

# Styling (A6): validated categorical slots 1-2 of the dataviz reference palette, light mode;
# text in ink tokens, never the series colour; recessive grid and axes.
SERIES_OBSERVED, SERIES_PREDICTED = "#2a78d6", "#eb6834"
SURFACE, INK, INK_2, RULE = "#ffffff", "#0b0b0b", "#52514e", "#e4e3de"


def main() -> int:
    rows = [r for r in csv.DictReader(open(sys.argv[1], encoding="utf-8")) if r["stage"] == "2b"]
    plt.rcParams.update({"font.size": 9, "text.color": INK, "axes.labelcolor": INK_2,
                         "xtick.color": INK_2, "ytick.color": INK_2})
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.3), sharey=True, facecolor=SURFACE)
    for axis, (window, title) in zip(axes, WINDOWS):
        cells = [c for c in rd.PANEL_DEV["cells"] if c.endswith(window)]
        observed, predicted, counts = [], [], []
        for _, arm in FAMILIES:
            labels = [classify.classify_output(rd.effective_output(f"{arm}-k1-{c}-s7"))
                      for c in cells]
            n = sum(classify.is_commitment_infeasible(l) for l in labels)
            counts.append(n)
            observed.append(n / len(cells))
            mine = [r for r in rows if r["arm"] == arm and r["window"] == window]
            predicted.append(sum(r["prediction"] == "commitment-infeasible" for r in mine) / len(cells)
                             if mine else 0.0)
        xs = list(range(len(FAMILIES)))
        axis.bar(xs, observed, width=0.58, color=SERIES_OBSERVED, label="kết cục",
                 edgecolor=SURFACE, linewidth=2, zorder=2)
        axis.scatter(xs, predicted, s=70, color=SERIES_PREDICTED, edgecolor=SURFACE,
                     linewidth=2, zorder=3, label="dự đoán (niêm phong)")
        for x, y, n in zip(xs, observed, counts):
            axis.text(x, y + 0.075, f"{n}/{len(cells)}", ha="center", va="bottom",
                      color=INK_2, fontsize=8)
        axis.set_xticks(xs, [name for name, _ in FAMILIES], fontsize=8)
        axis.set_title(title, fontsize=9.5, color=INK)
        axis.set_ylim(0, 1.15)
        axis.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
        axis.grid(axis="y", color=RULE, linewidth=0.8, zorder=0)
        axis.set_axisbelow(True)
        for side in ("top", "right"):
            axis.spines[side].set_visible(False)
        for side in ("left", "bottom"):
            axis.spines[side].set_color(RULE)
        axis.set_facecolor(SURFACE)
    axes[0].set_ylabel("Tỉ lệ ô vô nghiệm do cam kết")
    handles, names = axes[0].get_legend_handles_labels()
    fig.legend(handles, names, loc="upper center", ncol=2, frameon=False, fontsize=8.5,
               bbox_to_anchor=(0.5, 1.0))
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    with open(sys.argv[2], "xb") as handle:
        fig.savefig(handle, format="pdf")
    print(f"wrote {sys.argv[2]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
