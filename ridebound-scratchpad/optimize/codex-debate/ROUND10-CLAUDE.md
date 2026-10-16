# Round 10 (2026-10-08): promise + prediction, learning from previous trips, and a complete data audit

The owner asks:
1. **Does the project have nothing left to do?**
2. **Promise plus traffic prediction.** Focus on this direction and find what can be exploited that other systems do
   not do. Real systems usually train ML models on the times of previous trips, not on "previous congested days".
   Survey carefully.
3. **Audit all data already run,** so we never again miss existing data as we missed WP14r.

Same permissions as before:
- write only in `codex-work/`;
- read anything;
- web search;
- zero hallucination: cite `file:line`, or a URL with a verbatim quote;
- outputs in mode "x".

You may use a scikit-learn environment Claude created outside the simulation env:
`C:/RideBoundData/envs/ml-v1/Scripts/python.exe` (sklearn 1.7.2; package list in
`claude-work/ml-v1-env-freeze-2026-10-08.txt`). Do NOT install anything into
`E:/RideBoundData/wp7/envs/fleetpy-1.0.2`.

## Tasks (write the files named below in `codex-work/`)

**A. Independent data audit: `DATA-AUDIT-CODEX.md`, plus a TSV.**
1. Build your own inventory of every saved run under `E:/RideBoundData` and `C:/RideBoundData/research`. For each,
   record: experiment, arms, cells and windows, vehicles, requests, world (static or time-varying travel), runner or
   era, and completed trips.
2. **Only after that**, compare your inventory with Claude's:
   - `claude-work/data-inventory-runs-2026-10-08.tsv`;
   - `claude-work/data-inventory-by-experiment-2026-10-08.txt` (1,991 runs, 51 experiments).
   - Note: `data-inventory-summary-2026-10-08.txt` has a grouping bug and is superseded by the by-experiment file.
3. List every experiment that bears on our open questions but was NOT used in the debate. For example:
   - `wp8/frontier-20260820`, with 4, 8 and 16 vehicles;
   - `wp9/frontier-v1`;
   - `wp14/drift-*`;
   - `wp14/wide-window-v1`;
   - `research/tier3-sweep-v1`.

   Say what each one already answers.

**B. Survey: `SURVEY-ML-ETA-CODEX.md`, under 1,800 words.** Primary sources, verbatim quotes. Cover:
- how industry and academia train ETA or promise models on historical trips: inputs, targets, ground truth;
- ETA or promise models specific to pooled or shared rides, and prediction of insertion or detour delay;
- quantile, conformal or distributional promises;
- work linking dispatch commitment to ETA predictability or consistency.

Conclude what our system could exploit that others do not, if anything.

**C. Critique of Claude's ML pilot plan: `ML-PILOT-REVIEW-CODEX.md`.**
- The plan is `claude-work/ML-PILOT-PLAN-DRAFT.md`.
- Is hypothesis H-ML ("commitment makes promise error learnable from simple inputs") worth testing? Is it novel
  against your survey B?
- Fix the design: features, leakage risks, splits, matched-extension comparison and predictions ML1–ML4. Propose the
  exact sealed version.
- Give a direct answer to the owner's question 1, "nothing left to do?", as one paragraph.

Finish with a short message listing the files you wrote.
