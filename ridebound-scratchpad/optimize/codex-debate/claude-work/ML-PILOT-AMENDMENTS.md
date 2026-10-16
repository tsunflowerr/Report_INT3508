# ML pilot: amendments (written AFTER the sealed run; labelled post hoc)

## A1 (2026-10-08): provenance purge that the sealed plan required but the first run skipped

**Finding.** Codex round 11 (`codex-work/ROUND11-CODEX.md`) found that the sealed plan's gate was bypassed. The gate
required purging source trips duplicated between fit and calibration. Claude confirmed this independently
(`provenance_overlap_check.py` → `provenance-overlap-check-2026-10-08.txt`):
- In all five static WP14r arms, exactly **11 original FleetPy trips** appear in both fit (12/11, r1–r3) and
  calibration (12/11, r4): 3212940, 3218675, 3222010, 3228410, 3229318, 3229612, 3232267, 3233063, 3234082, 3346430,
  3350441.
- There is no overlap between fit and test, or between calibration and test, in any arm.
- The measured worlds (U, C-30) have no overlap at all.

**Amendment.**
- Drop the riders whose original trip is in that set from the static **calibration** split. The fit split is kept, so
  the fitted models are unchanged, and only the matched-cost factor ρ is affected.
- Write the purged data to a new CSV, `riders-causal-a1-2026-10-08.csv`.
- Run the **byte-identical** `ml_pilot_run.py` once on it, writing `ml-pilot-report-a1-2026-10-08.txt` and
  `ml-pilot-rows-a1-2026-10-08.tsv`.

**Status of the first run.** Under the sealed kill rule ("invalid provenance stops the pilot before fitting"), the
first run is NOT a valid sealed result. It is kept and reported as the pre-amendment run. The A1 run is the amended,
post-hoc result. Neither is a fresh holdout.

**Also owed.** The common-completed supplement that the first run omitted. Codex supplied it
(`codex-work/round11-reproduce-common-pairwise.tsv`). Claude will report it alongside the A1 result.
