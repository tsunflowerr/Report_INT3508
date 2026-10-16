# Round 10 resumed (2026-10-08 22:2x)

Your round 10 stopped on the usage limit before you wrote any file. Your last messages reported:
- 1,991 primary run records plus 17 later attempts;
- 40 original FleetPy calibration runs with trip-level outcomes;
- a close prior study that learns pooled-ride offers from fleet state.

Please finish `ROUND10-CLAUDE.md` tasks A, B and C, with these updates.

1. **Task C now reviews `claude-work/ML-PILOT-PLAN-V2.md`.** It supersedes the draft. The framing is Fielbaum &
   Alonso-Mora's two remedies, "better predictions" vs "make these changes less frequent", compared at equal mean
   quote extension.
2. **The rider-level dataset already exists.** File: `C:/RideBoundData/research/ml-pilot-v1/riders-2026-10-08.csv`
   (15,023 rows, 179 runs, SHA-256 2604de64…c733e). Script: `claude-work/ml_extract_riders.py`. Check:
   - the feature timing: everything must be known at t0, the first drop promise;
   - the `load_t0` definition;
   - leakage.

   Spot-check at least 20 rows against the transcripts with your own code.
3. **Claude's survey is now available:** `claude-work/SURVEY-S4-ml-eta-from-trips.md` (28 sources). Claude
   re-verified two quotes:
   - Fielbaum & Alonso-Mora: "no public methods" (fn.7) and "better predictions or to make these changes less
     frequent" (p.10);
   - Hörl & Zwick 2022, strategy B (`claude-work/pdf/hoerl-zwick-2022.txt:527-539`).

   In your `SURVEY-ML-ETA-CODEX.md`, add the close prior study you found (with a quote). Say whether it changes the
   novelty boundary.
4. **Budget your usage.** The limit has stopped three rounds.
   - Keep each file under 1,200 words.
   - Write the files early, then refine them.
   - Order: `ML-PILOT-REVIEW-CODEX.md` (the most important; it must end with the exact sealed version you would
     accept: predictions, splits, matched-cost rule, kill criterion); then `DATA-AUDIT-CODEX.md`; then
     `SURVEY-ML-ETA-CODEX.md`.

Finish with a short message listing the files you wrote.
