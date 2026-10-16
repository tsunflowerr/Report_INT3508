# Joint conclusions of the Claude–Codex debate (2026-10-06)

- **Participants.** Claude (Opus 5.5) and Codex CLI 0.160.1, model gpt-6.1-sol, reasoning effort ultra, sandbox
  read-only (each log header).
- **Session.** One Codex session, `01a11056-6e20-7ef1-b6e4-fe375272c630`, over three rounds:
  `ROUND{1,2,3}-CLAUDE.md` → `ROUND{1,2,3}-CODEX.md`, plus `ROUND2-ADDENDUM.md`. Logs are `round*-codex.log`.
  The first round-2 try stopped on the Codex usage limit; the owner reset it.
- **Question.** The owner asked whether the small post-promise lateness (about 1 min) is meaningful, whether "the data"
  causes it, and what the three studies jointly support:
  - T3.8/T3.9: cap vs no cap, and vs the deadline rule;
  - rider experience;
  - the forecast study.
- **Evidence.** Every number below comes from a saved script and output in this folder or from an earlier saved
  report. Claude re-checked each Codex number and citation it relied on.

## 1. Facts both sides accept

| # | Fact | Source |
|---|---|---|
| F1 | The tested deadline rule `Mplus-30` is fixed: drop ≤ first drop promise + 30 s, with **no traffic allowance**. Claude's round-1 brief said otherwise; the written reports were right. | `CommitmentLockEvaluator.cs` (RideBound-deadline, the tree T3.8 ran from); `EVIDENCE-PACK-2026-10-06.md:22` |
| F2 | Each cell has 108 requests, 8 vehicles of capacity 4 and 96 service nodes. `sample_10` is exactly 10% of the day file, so a cell holds about 0.4% of the matched-source trips in its window. | fixture `normalization-report.json`; `wc -l` of the demand CSVs |
| F3 | Dwell and boarding time is 0 at every stop. | `service-duration-check-2026-10-06.txt` and code cited in `ROUND1-CODEX.md` |
| F4 | All 49 panel-A fixtures scale arcs by the 00:00 traffic factor, and the world multiplies by f(t)/f(start). Simulated / measured absolute time at the window start: 07:00 0.86–1.14 (weekdays); 08:00 0.60–0.89 (weekdays); 17:00 0.47–0.77 (built cells); weekend mornings 1.23–1.55. | `factor-anchor-check-2026-10-06.txt` |
| F5 | Selection keeps shorter trips. Free-flow direct time, median 165 s selected vs 196 s eligible; p90 303 vs 429 s. Below 1 in 49/49 fixtures. These are modelled base-network times. | `selection-length-check-2026-10-06.txt` (verified by Codex) |
| F6 | The first promise already contains the planned wait and ride: mean promised door-to-door 14.1 min. Mean lateness after it is 0.32 min under U (2.2%) and 0.16 min under C-30 (1.1%). | `burden-and-rescale-2026-10-06.txt` |
| F7 | Shared rides (another rider on board) are 22.8% under U and 12.9–14.1% under the caps. Shared passenger-time is 15.2% of onboard passenger-time under U and 7.2–7.7% under the caps. Alonso-Mora et al. (PNAS 2017) report about 90% shared rides with the same denominator, but in a full-NYC simulation with 1,000–3,000 vehicles. | `exposure-check-…`, `shared-time-share-2026-10-06.txt`; `alonso-mora-pnas2017-author-corrected.txt:538,597` |
| F8 | A rider's drop promise is moved by dispatch (c ≠ 0) for 7.1% of U riders (174) and 1.1–1.7% under the caps. Pickup promises are never moved by dispatch in any arm. Under U, 134 of the 203 late riders are among the 174 exposed (77% of them late). Unexposed riders are late at 3.05–3.21% in every arm. | `exposure-check-2026-10-06.txt` (counts reproduced by Codex) |
| F9 | U vs C-30 served sets: common 2,207, only U 227, only C-30 131. Common riders ride 10.5 s shorter under C-30. | `common-riders-check-2026-10-06.txt` (exact match, both sides) |
| F10 | Lateness distribution vs the first drop promise. U: > 1 / 2 / 5 / 10 min = 8.34 / 4.19 / 0.74 / 0.08%, max 11.0 min. C-30: 3.25 / 0.47 / 0 / 0%, max 3.9 min. C-30 + display: 0.43 / 0 / 0 / 0%. | `report-extras/lateness-distribution-2026-10-06.txt` |

## 2. Joint conclusions

1. **SUPPORTED.** "Lateness after the first promise" measures how accurate the promise is, not how long the rider
   waits or rides. The first promise already contains the planned burden (F6). The selection favours shorter modelled
   trips (F5).
2. **SUPPORTED.** Against U, every cap improves measured post-promise reliability (F10). Every cap also lowers:
   - service coverage (−2.6 percentage points of requests for C-30);
   - exposure to dispatch changes (F8);
   - shared passenger-time (F7).
3. **SUPPORTED.** C-30 shortens common riders' rides modestly (F9). It keeps its own dispatch-change contract with no
   overrides in these runs. The deadline rule makes a different promise, so "C keeps its promise and Mplus breaks its
   own" compares two different guarantees, not one stronger arrival guarantee.
4. **SUPPORTED.** The forecast display layer improves promise calibration while every vehicle action stays fixed.
   The "anticipated" share of the lateness ledger is defined from the forecast used, so it is forecast-relative.
5. **WEAK.**
   - "Reduced later pooling explains most of the improvement."
   - "Unexposed lateness is an invariant traffic-only floor."
   - "The causes of scarce exposure (short trips, density, anchoring, locks) can be ranked."
6. **UNSUPPORTED.**
   - Human harm reduction, satisfaction, retention or commercial benefit.
   - That simulated rates bound real lateness from either side.
   - That C-30 improves reliability at a pooling efficiency comparable to U.

**Wording accepted by both sides for the thesis:**

> Under U, nonzero dispatch-induced drop revisions affect relatively few served riders, but lateness is concentrated
> among them: 174 exposed riders account for 134 of the 203 late riders. Observed lateness among riders without
> recorded dispatch-induced drop changes is similar across arms (3.05–3.21%). These results locate the observed errors
> without establishing why exposure is scarce.

> Every tested cap reduces the share of served riders with nonzero dispatch-induced drop revisions and reduces shared
> passenger-time relative to U (15.2% → 7.2–7.7% of onboard passenger-time). This is consistent with restricting later
> pooling changes as an important mechanism, but the summaries do not count insertions or establish complete
> mediation. C-30 maintains its dispatch-change contract without overrides in these runs; no material pooling
> advantage over the deadline rules is established.

## 3. The owner's question, answered

- **"Is it the data?"** Not the raw data: demand and traffic factors are real NYC 2018 records. The small numbers
  come from:
  - how the experiment is built: small cells, shorter selected trips, zero dwell, deterministic execution and a
    00:00 traffic anchor;
  - what the metric measures: error after a promise that already contains the planned trip.
- **The 100+ GB on disk** is mostly run transcripts. For example, one T3.8 run writes a 54 MB transcript, and T3.8
  totals about 13 GB (`data-size-2026-10-06.txt`). The size does not reflect the size of each experiment.
- **Is "1 minute" meaningful?**
  - It is meaningful as a measure of promise accuracy inside this model.
  - It is not evidence of harm. Thresholds linked to harm in the literature are at the minutes scale; the Via study
    concerns pickup ETA error of about 8–10 min.
  - Report the whole curve (1, 2, 5, 10 min) and lateness as a share of trip time, never only "> 60 s".

## 4. Remaining disagreements and the experiments that would settle them

These are limits on interpretation, not reasons to reject the saved descriptive results.

| Disagreement | What would settle it |
|---|---|
| Mediation: which insertions explain the changed errors | Insertion-level histories per common rider |
| Efficiency: does C-30 beat a simple conservative rule? | Experiment E1 below |
| Generalization: does the 00:00 anchor change the comparisons? | Experiment E2 below |

Codex's ranked proposals (Claude checked the cited cells and parameters; runtimes not checked):

- **E1. Conservative comparator.**
  - Design: U with vehicle capacity 1 (no pooling), on the six test cells `d20181114-s10-r3` and `d20181117-s10-r3`
    × w07/w08/w17, compared with the saved U, C-30 and Mplus-30. That is 6 new jobs.
  - Prediction to seal: lower exposure and lateness than U, and C-30 keeps more timely completions.
  - Claim-changing result: capacity-1 U matches C-30's reliability with at least as many timely completions. Then any
    suggested advantage over simply not pooling must be withdrawn.
- **E2. Corrected anchoring.**
  - Design: regenerate the same six fixtures with `travelFactorAtSeconds` = window start, keeping the requests, node
    pool and fleet placement. Run U, C-30 and Mplus-30. That is 18 new jobs.
  - Prediction to seal: weekday U lateness and exposure rise, and weekend falls. C-30 keeps zero overrides.
  - Claim-changing result: materially different tails or service losses. Then the numerical claims must be narrowed
    to the original anchoring.

Neither experiment has been run. Both need the owner's approval, a sealed plan and AC power.

## 5. Corrections owed to existing documents (not applied; owner approval needed)

1. **`FORECAST-REPORT.md` §6 "Gần như tất định" and docs/18 limitations.** Add F4 (00:00 anchoring for all cells,
   not only snow), F5 (selection keeps shorter trips) and F3 (zero dwell).
2. **`T38-REPORT.md` §3.** Write the U cost as "2.6 percentage points of requests (3.9% of U's served riders)". Add
   that the served sets differ by 227 + 131 riders, not only by 96.
3. **Anywhere C-30 is contrasted with Mplus "breaking its own promise".** State that the two rules promise different
   things (F1 and conclusion 3).
4. **Pending earlier Codex corrections.**
   - Via: the ETA error is for pickup, and the link to engagement is observational.
   - C display 0.51% over 34 cells vs 0.17% over 21 cells.
   - The forecast gain is not specific to C.
   - The ledger attribution is not causal.
   - Family B holds for wrapper v1.3 only.
   - 108.6 s is the median of nonzero revisions.
