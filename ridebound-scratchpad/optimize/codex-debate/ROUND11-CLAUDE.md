# Round 11 (2026-10-08): verify the sealed ML pilot result

**What was done.**
- I adopted your exact sealed version as `claude-work/ML-PILOT-SEALED.md`.
- Seal: SHA-256 93f6b968…, sealed 22:46:17 (`ML-PILOT-SEALED.sha256`).
- Causal data: `ml_pilot_extract.py` → `C:/RideBoundData/research/ml-pilot-v1/riders-causal-2026-10-08.csv` (10,064
  rows, 112 runs, SHA-256 7075ad97…). The causal state comes from the first promise's `projection.serviceOrder`.
- Analysis: `ml_pilot_run.py`, run once in `C:/RideBoundData/envs/ml-v1` → `ml-pilot-report-2026-10-08.txt` and
  `ml-pilot-rows-2026-10-08.tsv`.

**Result.**

| Prediction | Verdict | Detail |
|---|---|---|
| ML1 | TRUE | C-30 HGB gain is 0 pp on both dates |
| ML2 | FALSE | U gains are +0.69 / +0.00 pp vs fc+uniform, and the guards fail |
| ML3 | FALSE | FREE gain is +1.24 pp, and the guards fail |
| ML4 | TRUE | No learner matches C-30 |
| ML5 | FALSE | G_full = G_nostate |

The kill criterion fired.

## Tasks (write `codex-work/ROUND11-CODEX.md`, under 700 words)

1. **Reproduce** every E = 30 number and verdict with your own code from the causal CSV. Report any mismatch.
2. **Audit the extraction** against the sealed plan:
   - the serviceOrder-based state (other_assigned, other_onboard);
   - the fixed 12/11 + 13/11 profile vintage;
   - the splits;
   - one effective run per cell.

   Spot-check 20 rows against the transcripts.
3. **Audit the analysis** against the sealed plan: matched-cost ρ rule, controls, WIN guards, metric definitions and
   p90 rank. Flag any deviation.
4. **Interpretation.** Say what the thesis may claim in 3 sentences, including the limits:
   - few days;
   - small test cohorts (145–807 riders);
   - fixed learners;
   - simple features;
   - simulated worlds.

   Address Fielbaum & Alonso-Mora's two remedies: is "fewer changes beats better predictions at equal quote cost, in
   these worlds" a fair reading?
