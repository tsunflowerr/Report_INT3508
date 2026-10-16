"""For every prediction miss, compare the treatment run with its reference run. Read-only.

Prints, for treatment and reference: label, last decision frame (s), total decision-induced drop
component C (s), largest running M+ over riders (s), accepted count when completed.
Usage: miss_reasons.py <analysis-report.txt>
"""
from __future__ import annotations

import sys

import classify
import holdout_predict as hp
import run_deadline as rd
from compare_controls import accepted


def summary(directory):
    chains, last, total_c = hp.trajectory(directory)
    mplus = max((max([0] + [p - chain[0][1] for _, p in chain]) for chain in chains.values()),
                default=0)
    return (classify.classify_output(directory), (last or 0) / 1000, total_c / 1000, mplus / 1000,
            accepted(directory))


misses = [line.split("\t") for line in open(sys.argv[1], encoding="utf-8")
          if line.rstrip("\n").endswith("\tNO")]
print("arm\tk\tcell\tprediction\t| treatment: label, last_s, C_s, maxM+_s, accepted "
      "| reference: label, last_s, C_s, maxM+_s, accepted")
for row in misses:
    stage, window, arm, k, cell = row[:5]
    panel = rd.PANEL_A if stage == "2a" else rd.PANEL_DEV
    treatment = rd.effective_output(f"{arm}-k{k}-{cell}-s7")
    reference = hp.reference_output(panel, int(k), cell)
    t = summary(treatment)
    r = summary(reference)
    print(f"{arm}\t{k}\t{cell}\t{row[10]}\t| {t[0]}, {t[1]:.0f}, {t[2]:.1f}, {t[3]:.1f}, {t[4]} "
          f"| {r[0]}, {r[1]:.0f}, {r[2]:.1f}, {r[3]:.1f}, {r[4]}")
