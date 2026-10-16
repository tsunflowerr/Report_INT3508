# Round 6 — independent verification and closing critique

2026-10-07. **No numerical mismatch:** every selected-rule row and printed train/test metric matches Claude. **P1 FALSE, P2 TRUE, P3 TRUE; withdraw room-specific superiority.** Accept the eCFR versioner correction. The broader statement that padding cannot replace a cap requires an explicit objective and narrower scope.

## Independent method and trace

I wrote [round6_verify_backtest.py](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round6_verify_backtest.py) and ran it with `E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -B round6_verify_backtest.py`. It imports only the Python standard library, reads my independently extracted Round-5 cache, and never imports or executes Claude's code. It checks all 68 transcript size/mtime signatures against extraction time; these are cache-freshness checks, not new cryptographic transcript audits. Raw frame hashes were checked during the original extraction.

The plan's current SHA-256 matches its saved seal, including the `6175d2c13b6173c89020870b2b0a285d5c3a16267c0185335170643da4858d8d` value ([output:2](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round6-backtest-verification-2026-10-07.txt:2)). This verifies content identity; it does not independently prove the historical sealing time.

I implemented all five families, every parameter value and both lambda values in the sealed plan; training budgets 15/30/60 seconds; selection within each arm/family/budget by highest timely count, then lower mean and empirical p90 extension; and both specified chronological folds. The direct control is the plan's `maxRideTimeMs/1500` seconds proxy, not a separately recomputed shortest path. Empirical p90 uses the sorted array's zero-based floor(0.9n) index, matching the supplied implementation. Remaining exact ties retain enumeration order. Train 14/test 15 and 16, and train 14+15/test 16, are kept separate.

The numerical output was created with mode `x`. Comparing independently generated rows with Claude's saved text gives **60 rows, zero mismatches**, covering rule parameters, lambda, training metrics, Y30/Y60/Y120, early60, two-sided60, mean/p90 extension and timely counts ([output:75](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round6-backtest-verification-2026-10-07.txt:75)). No dispatcher jobs were executed.

## Prediction verdicts and kill criterion

| Prediction | Independent verdict | Evidence |
|---|---|---|
| P1: room beats uniform at both E30/E60 on both forward days | **FALSE** | E30 room: 5.50%/5.74% Y60, uniform: 2.36%/5.30%. E60 room does beat uniform: 1.31%/3.68% versus 1.57%/4.12%. [output:14,17,19,22](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round6-backtest-verification-2026-10-07.txt:14) |
| P2: room never improves on the better horizon/direct control by more than 0.5 pp | **TRUE** | Room's margins at E30 are −3.665/−1.031 pp; at E60 +0.262/−0.147 pp. [output:78](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round6-backtest-verification-2026-10-07.txt:78) |
| P3: C-30 E15 forecast-only selection has lambda=1 and Y60≤0.5% on both days | **TRUE** | 0/376 and 1/656 late; Y60 0%/0.1524%. The forecast-only family is also the best eligible E15 family on training data. [output:42](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round6-backtest-verification-2026-10-07.txt:42) |
| Room-specific superiority retained only if all sealed requirements pass | **KILL FIRES** | E30 loses to uniform; E60 loses to horizon on 16 November. At E60, room's early60 exceeds uniform by 11.78/23.42 pp, and its two-sided accuracy is lower by 11.52/22.97 pp. [output:83,86,88,91](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round6-backtest-verification-2026-10-07.txt:83) |

Withdraw the room-superiority claim, not the mathematical validity of room as an available feature. P2 is compatible with a trip-length proxy explanation; it does not establish that explanation causally or prove equivalence. The finite room grid starts at a 30-second cap, leaving no eligible forecast-plus-room option at E30 in this training set. Thus the negative comparison is specific to the sealed search. Changing the search after inspection would be a new exploratory analysis.

The sealed backtest is complete. The earlier joint plan's additional audits of all quote recipients, visible variation, full quote horizon and cost denominators remain zero-run work; a completed-rider calibration report does not finish those checks.

## What Claude's policy reading supports

**Accuracy and quote cost:** the selected C-30 forecast-only rule is substantially more accurate and has shorter quotes than the selected U padding alternatives on these two weekday evaluations. C's mean extension is 17.1/10.7 seconds and two-sided accuracy 100%/99.7%. The frozen U room rule has 63.3/59.5 seconds and 84.3%/67.0%, with early60 14.4%/29.3% ([output:82,86,87,91](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round6-backtest-verification-2026-10-07.txt:82)). This is a useful measured operating point, with a real completion cost.

**Timely count and service:** a single frozen U room rule gives 377+654=**1,031 timely**; C gives 376+655=**1,031 timely**. U completes 382+679=**1,061**, versus C's 376+656=**1,032**. These are counts from the two test days, not the 34-cell panel. Therefore padding already matches the total reference-timely count in this comparison while completing 29 more requests; it fails to match C's conditional accuracy and quote-cost combination. With the same requested population, the aggregate timely/request rate is also equal. The 96-completion gap belongs to the full 34-cell panel ([T38:49](E:/Code/Report_INT3508/ridebound-scratchpad/tang3/t38/T38-REPORT.md:49)).

**The 60-second qualification:** eligibility constrains the training mean, not the evaluation mean ([sealed plan:28](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/claude-work/CALIB-BACKTEST-PLAN.md:28)). U room reaches 63.3 seconds on 15 November; horizon reaches 65.3/62.2. Even C's E15 forecast-only rule reaches 17.1 seconds on the incident day. Report these shifts, rather than describing a strict held-out cost ceiling. The direct E60 rule stays below 60 on both days (54.4/52.5) but still has worse accuracy (Y60 1.57%/3.83%, two-sided 90.1%/81.6%); this supports the narrow accuracy conclusion without relying on a budget breach ([output:85,90](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round6-backtest-verification-2026-10-07.txt:85)).

**Candidate selection:** choosing room as the displayed “best” U rule for 15 November and horizon for 16 November uses test outcomes. That table is a descriptive envelope of separately frozen candidates, not one preselected deployable rule. The fixed-room comparison above avoids that issue.

**Population check:** I also paired completed request identities within each cell. There are 357 common completed riders on 15 November and 622 on 16 November; U-only/C-only counts are 25/19 and 57/34 ([output:94,99](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round6-backtest-verification-2026-10-07.txt:94)). On those intersections C forecast still has better late/two-sided accuracy and shorter extensions than every selected E60 U family ([output:95](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round6-backtest-verification-2026-10-07.txt:95), [output:100](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round6-backtest-verification-2026-10-07.txt:100)). This strengthens the descriptive accuracy comparison, but intersecting completed sets cannot recover rejected riders' counterfactual experience or eliminate selection.

**Scope:** weekends are absent and their causal forecast is inactive; 15 November is the documented incident date, and these panel windows do not constitute a general incident test. The separate snow-window study remains relevant. The few dates were inspected previously; fold 2 reuses 16 November and is not independent confirmation. Quote costs here condition on completion. There is no booking, cancellation, utility, or operating-cost model establishing a business optimum.

The fair closing claim is: **On this finite-grid, previously inspected weekday backtest, the selected U padding rules do not match C-30 plus forecast's combination of conditional accuracy and short quotes. U can match total reference-timely count while completing more requests.** Do not claim a universal replacement impossibility, global dominance, or causal proof that room is only trip length.

## eCFR correction

Claude is right about the [official versioner API](https://www.ecfr.gov/api/versioner/v1/versions/title-49.json?part=37&section=37.131). An independent HTTPS GET through Python urllib verified the section-level record: `amendment_date="2016-10-17"`, `issue_date="2017-01-01"`, `substantive=true`; the reissue is `issue_date="2023-04-10"`, `substantive=false`, retaining the amendment date.

I retract the Round-5 recommendation to remove the 2016 date based on the section's source note. That note ending in 2006 did not disprove the versioner record. Cite the API for the metadata. The metadata alone does not identify which amendatory language changed or establish that paragraph (f)(3)(ii) changed in 2016. The earlier substantive quotation and responsibility-versus-experienced-lateness interpretation stand.

The owner's four answers and the proposed approval choices are in [FINAL-JOINT-POSITION-CODEX.md](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/FINAL-JOINT-POSITION-CODEX.md).
