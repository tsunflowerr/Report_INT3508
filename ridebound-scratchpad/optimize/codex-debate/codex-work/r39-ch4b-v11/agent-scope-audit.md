# R39 independent scope and correction-completeness audit

Read-only audit of the prescribed B-v10, R37 §§1/5, R36 A-v5-v3 handoff §5, Ch3 v4-v3, appendices v2, latest Ch5 v2, assembly notes, test rerun evidence, and owner writing rules. No build, installation, simulation, or test run. This file is new; no deliverable was edited by this agent.

## Scope decisions required by newer inputs

- R39 expressly preserves unaffected sentences and forbids budget cuts unless requested by a reviewer. Trial Chapter 4 is 21 pages against 26,5. Do not execute R37's general 695-token target or conditional shortening list.
- R37 explicitly requests removal of the untested dwell/load hypothesis (v10:410–411); its supplied 408–411 replacement is a permitted isolated deletion. Remove the corresponding obsolete EV clause at 415 as part of the same change. Retain the sampled zero-dwell limit, 96-node graph, setup-specific service cost, and no-reassignment limit.
- Attempt 4 supersedes R37's old test wording: one full run on 13/10/2026 passed 1.025/1.025 with LF and an untracked marker. B381–384 must use attempt 4; retain the real Appendix C reference.
- `r31-ch5/11-phuluc-v2.tex:60` defines `phuluc:C`; do not implement R37's obsolete reference deletion. Its test detail at 119–120 still needs a later appendix edit.
- Part A snow identity has already been corrected throughout A-v5-v3. Do not reproduce those edits or revive its stale “bộ chạy chưa kiểm” caveat.
- Latest `r31-ch5/10-chuong5-v2.tex:33` already puts selector×cap first among future directions. R37's missing-Ch5 rationale is superseded. Its safe replacement (“phép thử này là một hướng phát triển còn mở”) remains a sensible requested targeted edit; record the newer source status rather than claiming Ch5 is absent.

## Required B revisions to check in the final draft

| v10 lines | Required treatment | Evidence / rationale |
|---|---|---|
| 2–7 | Identify v11, and name assembly partner `08-chuong4-phanA-v5-v3.tex`. Preserve prior provenance except stale integration status. | R39 and R36 §5. |
| 39–59 | Bound complete table to available line width, including both long multicolumn headings. Keep every heading, cell and EV anchor. Narrowing only the 9,4 cm first column will not by itself wrap natural-width multicolumn headings. | R39; trial log 29,2 pt. |
| 71–73 | Apply safe open-future-work wording, without claiming latest Ch5 is absent. | R37 §1.6; Ch5 v2:31–34 now exists. |
| 124–128 | Restore M+-30 denominator 1.471, V-30 1.470, U 1.512, U17h 437 and C17h 418; state same 21-scenario cohort. | R37 §1.2 / N4B8-02. |
| 130–137 | Make 13,7-second scenario mean explicitly the 21-scenario group if revising; mark oracle-fit 2.305 as all 34 scenarios. Keep favorable simulation and pickup-check caveats. | R37 §1.2 / F06,F10. |
| 170–174 | This location belongs to a TikZ figure, not a table. Width-limit the diagram locally with an existing package; keep TikZ text/coordinates and caption unchanged. Inspect trial context before claiming an actual layout cure. | R39 trial 15,8 pt; B139–176. |
| 177 | Correct whole-second labels to 82+5.353+783=6.218 versus 6.217 (1-second discrepancy), rather than 0,1 second. | R37 §1.10 / N4B8-11. |
| 181–188 | Enter 3.849/8.496 with forecast and 5.121/8.468 without forecast on the same 15 completed M+ runs. Keep 47,6%/62,8% labeled scenario means, distinct from these pools. The 39,0%/11,0% rider means are from eight morning scenarios; R36 also asks for checked component pools or a switch to checked pooled presentation. Verify before importing new rider pools. | R37 §1.4 / dispatcher paired pools; R36 §5. |
| 191–192 | “mô hình cây quyết định tăng cường (gradient boosting)” removes unparenthesized English. Preserve the other model/profile/calibration/preview details. | R37 §1.3. |
| 206–211 | Explain that printed ML integer counts were recovered from three-decimal rounded pooled rates and have one compatible integer each. Preserve every model count/denominator and negative result. | R37 §1.3 / verify-numbers-v2.json:ml; ml_pilot_run.py:37–42,175–176. |
| 220–222 | Separate theoretical 30-second cap under (N) from observed 29,2-second maximum in the 34 main scenarios. Preserve 174 riders, 590,1 seconds, inactive weekend forecast and 96 lost services. | R37 §1.1 / padding pool, C20,N-23,N-28,A06,A22,K05. |
| 269–272 | Say nearly equal promise extension, restrict cap to C-30, retain 2.336/2.328 and 2.338/2.366, and describe the particular 37,18/7,37≈fivefold row rather than a necessary minimum. | R37 §1.1 / padding,N-16,N-17,N-18. |
| 284–288 | Prefer R36's checked pooled form 7.710/20.103, 28/34, original nonforecast obligation and unchanged original decisions. If retaining 41,3%, explicitly say scenario mean and give the pool separately. Avoid implying forecast replay changed its obligation. | R36 §5; R37 §1.4 / N-21,C13,X3-16. |
| 295–300 | Restrict claim to C-30 forecast versus U forecast+pad30, print 2.366 versus 2.338 on 3.672 inputs, state (N), preserve 96/242 cost and operator choice. Keep C-120 paragraph as an anti-generalization safeguard. | R37 §1.1 / N-19,C02,N-20,A22. |
| 347–352 | Explicit lower clipping limit zero and upper residual after dispatch. Preserve the signed-ledger distinction and 886,9/25,7% / 2.299,0/66,7% values. | R37 §1.9 / N4B8-07. |
| 358–362 | Add valid ledger 0≤Lr≤B at the current decision and (N) at every decision for the trip-long conclusion. Do not imply observed exact zero-count denominators were unconditional mathematical predictions. Preserve 20.101/20.435/20.760 and maxima. | R36 §5 / Ch3:371–390, A-v5-v3. |
| validation section | Add that ML count checking validates table arithmetic, not fitting or prediction. Do not import the obsolete blanket claim that main forecast/padding arithmetic lacks independent checking. | R37 §1.8 / verification section C. |
| 381–384 | Full run 1.025/1.025 on 13/10/2026, conditions LF/untracked file retained in body or clearly in provenance plus Appendix C; EV attempt 4 and fullrun log. | R39/R36 §5 / TESTRUN:18. |
| 408–415 | Isolated reviewer-requested hypothesis removal only, with obsolete EV hypothesis clause removed. | R37 §§1.7/7.1. |
| 419–420 | Add missing solver-seed sensitivity and consequence. Do not invent runs or robustness. | R37 §1.8; Ch3 fixed seed 7, B09,B11. |
| 421–428 | Add “kể cả các phép tính thử ở 120 giây” to reused-main-data disclosure. Keep snow and ML preview locally. Update stale A-v4 EV provenance to A-v5-v3 where used. | R36 §5 / I06,C4A-11,I11,K42; A:231–235. |

## Handoff only: cannot be edited under R39's B-only deliverables

1. Ch3:706–707: replace broad counter claim with “mục~\\ref{muc:c4-hople} báo các bộ đếm đã đọc của bộ sinh. Các số này không đo mọi giới hạn của bước sinh, kiểm và giải.” Keep subsequent ten-dimension/order-check explanation. R37 §1.5; assembly row 7.
2. Ch3:724: change test date from 12/10 to 13/10; already says all 1.025 with LF and untracked file. Ch3:737: supersede attempts 3/3b with attempt 4 + fullrun log. Do not replace the current statement with obsolete 1.024+1 wording. R39/R36 §5 and TESTRUN:18.
3. Appendix C:119–120: replace separate 1.024+1 results with one full 1.025/1.025 run on 13/10, retaining commit 45f8026, LF and untracked-file conditions; earlier attempts may remain as history only if distinguished. Its label is real and must be preserved.
4. Ch3:467: assembly row 6 still asks “vế cộng dồn”→“phần cộng dồn”; latest Ch3 still contains old term. This is a preexisting terminology handoff, not authorization to modify Ch3 in R39.
5. Assembly notes need the new B-v11 path and provenance/appendix/date updates, replacing stale “v10 final” and undefined-appendix expectations. R39 must report these; do not overwrite assembly notes.
6. Evidence registrar: new/reused derivations must be registered or precisely anchored in R39 CHANGES, including ML rounding note replacing the invalid generic radius<1 uniqueness rationale. A already supplies R36-A01/02/03; no duplicate fabricated register rows are needed.

No further Part A snow edit or Ch5 ordering edit is required. Citation keys are existing; no new bibliography entry is implied by these corrections. Actual layout and assembled compile remain unverified because this round forbids builds.
