# R19 — Claude-side fact check of Antigravity's R16 review (`antigravity-work/R16-ANTIGRAVITY.md`)

Date 2026-10-10. Role: Claude-side fact checker. Standard: every factual statement in the Antigravity file is marked
AGREE, WRONG (with the correct value and its anchor) or CANNOT CHECK. I tried to be fair: correct and new points are
credited in §3.

**What I read.** The file under review in full. Its inputs in full: `ROUND16-FACT-PACK.md`, `ROUND16-REVIEW-STANDARD.md`,
`R13-FINAL-VERDICT.md`, `R15-CONFIRM-CODEX.md`, `BAN-GIAO-PHIEN-2026-10-09.md`, and `ANTIGRAVITY-BRIEF.md`. The later files
it did not see: `codex-work/R17-REBUTTAL-CODEX.md` and `codex-work/R18-CONFIRM-CODEX.md` in full;
`claude-work/R17-FINAL-VERDICT.md`, `R16-EVIDENCE-CLAUDE.md` and `R16-FORECAST-CLAUDE.md` in full; and the relevant
parts of `codex-work/R16-CODEX.md` and `claude-work/R16-REVIEWER-CLAUDE.md`, found by grep. I also opened their helper
outputs where a number depended on them, the selector and policy source (read only), and `D03` lines 160-220 (read
only). **I did not open `codex-work/R19-*`.**

**What I ran.** Four tiny read-only Python helpers (FleetPy env, `-B -I`). They are in the session scratchpad, not in the
project. They read `codex-work/R15-audit.json` to re-sum the T3.8 frontier counts and the 16 Nov per-cell C-30 service.
There were no simulations, builds, installs or deletions. Apart from these scratchpad helpers, this file is the only
thing I wrote.

**Anchor keys** (paths relative to `E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/` unless absolute)

| Key | File |
|---|---|
| AG | `antigravity-work/R16-ANTIGRAVITY.md` (under review) |
| FP / RS / BR | `antigravity-work/inputs/ROUND16-FACT-PACK.md` / `inputs/ROUND16-REVIEW-STANDARD.md` / `antigravity-work/ANTIGRAVITY-BRIEF.md` |
| V13 / CX15 / BG | `antigravity-work/inputs/R13-FINAL-VERDICT.md` / `inputs/R15-CONFIRM-CODEX.md` / `inputs/BAN-GIAO-PHIEN-2026-10-09.md` |
| CX16 / CX17 / CX18 | `codex-work/R16-CODEX.md` / `R17-REBUTTAL-CODEX.md` / `R18-CONFIRM-CODEX.md` |
| FV17 / EV / FC / RV | `claude-work/R17-FINAL-VERDICT.md` / `R16-EVIDENCE-CLAUDE.md` / `R16-FORECAST-CLAUDE.md` / `R16-REVIEWER-CLAUDE.md` |
| AJ / CAP / WX | `codex-work/R15-audit.json` / `R16-cap-outcomes.txt` / `R16-weather-inventory.txt` |
| LOAD / CB / NOAA / NOAA13 | `claude-work/load-and-occupancy-2026-10-07.txt` / `claude-work/calib-backtest-2026-10-07.txt` / `claude-work/r13-ml-data-samples/noaa-event-days-2026-10-09.txt` / `claude-work/r16-forecast/noaa-event-days-2009-2013-2026-10-10.txt` |
| SEL / POL | `C:/Code/RideBound-noworse/src/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs` / `…/SolverBackedRidePoolingPolicy.cs` |
| D03 | `E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md` (read only) |

Flags in the WRONG rows: **[in]** = the error was already detectable from Antigravity's own inputs; **[later]** = it
is visible only with files written after its inputs.

---

## 0. Bottom line

1. **Counts.** 123 statements were checked: **67 AGREE, 46 WRONG, 10 CANNOT CHECK.** About 40 of the 46 WRONG items
   carry the flag **[in]**: Antigravity's own inputs already contradicted them.
2. **Copied numbers are reliable; added numbers and interpretations are not.**
   - Copied: essentially every number taken from the inputs is right. This includes all numeric cells of the 8-row
     frontier table, which I re-summed from AJ (§1, row A94).
   - Added: of the ten facts it introduced without an input anchor, eight are wrong and two cannot be checked. The
     wrong ones:
     - **431 riders** (correct: 417);
     - **snow starting at 13:00** (first Central Park snow report at 13:44);
     - **80–120 h**;
     - **30–45 s** boarding time;
     - **calibration on Nov 11–14**;
     - the **+13.7 s** equal-cost target;
     - **"pre-ride-hailing era"**;
     - **"load factor 0.814"**.
3. **The most important errors.**
   - **(a) Direction 3, the Gardner–McKenzie replay, is not viable.**
     - When fitted as the Round-12 protocol prescribes, it degenerates to α = 1, β = 0, φ = 0.8. That equals the
       historical profile, so the test returns a null by construction.
     - The 15 Nov snow day is not held out.
     - Its information rule leaks.
     - Its calibration and cost targets contradict its own inputs.
   - **(b) Cost-first under C-30.**
     - It misattributes a "+10 pp sharing" hypothesis to R13 P2.1, which is about U-cost-first.
     - Its mechanism is wrong: "the stability objective rejects pooled riders". The accepted count ranks before
       every revision level. At 62,837 recorded states, re-selecting with cost first changed the accepted count 0
       times.
     - Under C-30 gates only 6.1% of new-request decisions change.
   - **(c) "Loosening the cap destroys drop reliability … negligible gains" is contradicted by the measured dials.**
     On w07, C-120 gives +6 served and +2 timely60. On WP14r, C-120 gives +29 served, +6 timely60 and 0 late120.
   - **(d) "Cumulative clause strictly inert / de facto per-step cap / audit proving" violates R15 correction 1 and the
     R17/R18 wording.**
   - **(e) "2013 / multi-year data unviable … fundamental misreading"** is wrong for the full archive.
   - **(f) "First empirical demonstration"** violates R15 correction 8 and ignores HZ eq. 7.
   - **(g) "pickup-ETA instability may increase substantially"** is wrong: pickup ETAs are locked at confirmation.
4. **Valid new points (small).**
   - Add newly accepted riders' initial pickup-wait promise as a guard metric in the cost-first study.
   - Non-zero dwell time is a scenario factor that could change budget use (hypothesis; direction uncertain).
   - It gives correct per-request percentages and the early-arrival count 1,033 for padded U + 60 s.
   - Several conclusions converge independently with the later consensus, but none is new.
5. **Reliability rating: 2 / 5.** It is accurate as a transcriber of input numbers and unreliable as an analyst. Use it
   only as a source of reviewer questions, never as evidence (§5).

---

## 1. Statement-by-statement check

### §0–§1 (executive summary, standard)

| # | AG line | Statement (short) | Verdict | Correct value / anchor |
|---|---|---|---|---|
| A1 | 21 | 1,991 simulation runs | AGREE | BG:463-465 |
| A2 | 21 | LaTeX unedited since 2026-09-30 | AGREE | BG:71 (CX18:52, B1: file mtimes, not a certified build history) |
| A3 | 21 | Deadline mid-Nov, unconfirmed, ~5 weeks | AGREE | FP:99-100; RS:16 |
| A4 | 23 | Next step A1 at 0 runs; optional A2 at ~74 runs | AGREE (with its inputs) | V13:62-68,262-266; CX15:349. **Superseded:** next step = whole-thesis rewrite (FV17:51-54; CX17:3; CX18:3); optional study staged as 108 + conditional 72 jobs (FV17:55-60; CX18:215) |
| A5 | 23 | "inertness of the cumulative clause" | WRONG [in] | "never the recorded reason for a refusal; per-step counterfactual unrun" (CX15:193-199; FV17:64-65 "'No effect' and 'behaviourally inert' are both too strong") |
| A6 | 37 | Claim-boundary list (detection, pre-decision control, trade-off, forecast quoting, ML ETA, per-rider limits, guarantees) | AGREE | FP:91-93 |
| A7 | 14 | Lists D03 as an input anchor it used | CANNOT CHECK | BR:35-36 forbade opening files outside the folder. The D03 line ranges it cites are the ones quoted in CX15:150 (row 74). There is no evidence it opened D03 |

### Q1

| # | AG line | Statement | Verdict | Correct value / anchor |
|---|---|---|---|---|
| A8 | 55-58 | x = e − v, c = p − e, z = p − v = x + c | AGREE | FP:31; BG:97-101 |
| A9 | 59-62 | Three causes, three places (cap / forecast / ledger) | AGREE | V13:44-48 |
| A10 | 65 | C-30 2,338 = M⁺-30 2,338; 2,332 in common | AGREE | CX15:57,61 |
| A11 | 66 | M⁺-30 forced 41.3% (cell mean), self-broken 14.5% (12.4% pooled); C-30 0 / 0 | AGREE | V13:392-393 |
| A12 | 67 | C-30 + forecast: timely60 2,328 / 3,672 (ties M⁺ + forecast); late 3.25% → 0.43% (10 / 2,338); +7.4 s; 4 early (0.17%) | AGREE | CX15:64,170. My AJ re-sum: late60 10, early60 4, extension 7.37 s |
| A13 | 69 | Weekday headroom 2 / 1,471 | AGREE | V13 row 53. Scope per CX15:303-309: fixed sample and threshold, not a bound |
| A14 | 69 | ML pilot "failed 3 of its 5 stop conditions (ML2, ML3, ML5)" | WRONG [in] | ML1–ML5 were **predictions**: ML2, ML3 and ML5 were false, ML1 and ML4 true, and the **stop criterion was triggered** (BG:333-339) |
| A15 | 69 | Vehicle state added nothing | AGREE | BG:338 |
| A16 | 70 | Proportional screens +19 / +30 requests (0.52 / 0.82 pp) | AGREE | V13:462; CX15:128 |
| A17 | 70 | Called an "upper difference" | WRONG [in] | These are not upper bounds or ceilings (CX15:253-259, correction 4) |
| A18 | 70 | Collisions with Molenbruch, Lyft US12182741B2, Mt-KaRRi | AGREE | V13:476,481,482 |
| A19 | 71 | 66–68 deterministic work units per decision; zero cap truncation | AGREE | CX15:111 (row 45), :101 (row 35) |
| A20 | 51, 68 | "No scientifically viable alternative"; "every proposed alternative direction has been empirically falsified or exhausted" | WRONG [in] | CX15 correction 4 (screens are not ceilings, :253-259), correction 5 ("Do not say no hotspot exists or no pipeline optimization is possible", :279) and correction 7 (:303-309). FV17:597-602: "Vẫn còn chỗ để tối ưu … ba câu hỏi chưa thử". CX18:186 |
| A21 | 72, 353 | "5 weeks before submission without drafted chapters"; flowchart "0 Thesis Results Drafted" | WRONG [in] | The LaTeX exists; its last edit added table `bang:quet07` (BG:71). It has abstract and chapters 1–5 with results tables from an older sweep (FV17:87-92; CX18:60, B9). What is missing is the T3.8 frontier and the HZ positioning (FV17:52-54) |

### Q2 (loosening the cap; the 1,256)

| # | AG line | Statement | Verdict | Correct value / anchor |
|---|---|---|---|---|
| A22 | 82 | 1,256 are candidate evaluations, not riders | AGREE | FP:47 |
| A23 | 83 | 98 enforced-C runs, 64,371 decisions, 1,256 prunings | AGREE | CX15:87 (row 26) |
| A24 | 84 | T3.8 C-30: 845 records; 148 rejected requests; U served 116 | AGREE | FP:47-49 |
| A25 | 84 | 148 "rejected solely because of a co-rider's budget" | WRONG [in] | These are record-associated rejections, "observed pruning attribution" (CX15:130, row 59). They are "record-based path classifications, not proof of a unique causal reason" (CX18:108, B47) |
| A26 | 85 | 1,186 structural rejections | AGREE | FP:50-51 (3,672 − 2,338 − 148 = 1,186) |
| A27 | 85 | 1,186 "completely unaffected by the budget cap" | WRONG [in] | "Structural-only … does not prove that a larger-cap trajectory could never serve it" (CX17:79; CX15:130) |
| A28 | 87-91 | Overshoot p25 / p50 / p75 / max = 63.7 / 109.6 / 183.6 / 524.8 s | AGREE | FP:48-49 |
| A29 | 92-95 | B = 60 / 120 / 300 admits 11 / 59 / 135 (+0.30 / +1.61 / +3.68 pp), labelled a screen | AGREE | FP:49-50; arithmetic correct. Caveat: these are witness-crossing occurrences, with 5 / 51 / 123 co-riders newly late60 (FV17:352-356) |
| A30 | 97-99 | w07: 8 cells, 864 requests; pruned 142 → … → 4; served 660 → … → 665 | AGREE | FP:54-56; CAP:3-11 |
| A31 | 100 | 97% fewer prunings for +5 served (+0.58 pp) | AGREE | arithmetic correct |
| A32 | 102-105 | WP14r: C-30 → C-60 +6 / 0 late; C-60 → C-120 +23 / +23; → LOCKS +21 / +24 | AGREE | FP:57-58; V13:135-140 |
| A33 | 79, 101 | "Loosening the cap destroys drop reliability … negligible gains in served riders" | WRONG [in] | 1. w07 measured, C-30 → C-120: served 660 → 666, late60 47 → 51, timely60 613 → 615 (CAP:3-7; CX18:104, B43). 2. WP14r C-120: +29 served, +6 timely60, 0 late120 (EV:147; CX18:289). 3. FP:59-60 had warned that T3.8, where C-30 loses 91 of its 96 riders, has no C-60 or C-120 arm. 4. The "all feasible" end, U, is **+96 served** (FV17:61-63). CX18:353: "loosening can increase timely60 at a one-minute threshold" |
| A34 | 106 | "A cap of 120–300 s would permit single-step revisions exceeding 2–5 minutes" | WRONG [in] | Logic error: B = 120–300 s permits total dispatch movement **up to** 2–5 min (Σ\|c\| ≤ B), not exceeding it |
| A35 | 106 | The contract offers "a tight 1-to-2 minute reliability guarantee" | WRONG [in] | C bounds Σ\|c\| only, not arrival (V13:690, D6; CX15:217) |
| A36 | 106 | "Industry liability thresholds (e.g. Lyft's 10-minute threshold; FP:65)" | WRONG [in] | FP:65 contains no Lyft fact. Lyft is a qualified airport-bound **scheduled-pickup credit**, not a drop-off liability threshold (V13:696, D12; CX15:241) |
| A37 | 106 | U has 0.08% of riders > 10 min late | AGREE | V13:396 |

### Q3 (cumulative clause)

| # | AG line | Statement | Verdict | Correct value / anchor |
|---|---|---|---|---|
| A38 | 113 | "Strictly unexercised (inert)" | WRONG [in] | Use "never the recorded reason for a refusal; the per-step comparison was not run" (CX15:193-199; FV17:372-386; CX17:87) |
| A39 | 116-119 | 1,256 / 1,256 have Δ > B in one step; 0 cumulative-only | AGREE | CX15:87. Correctly written "> B": B differs by arm (CX18:301) |
| A40 | 120 | 0 riders with ≥ 2 nonzero dispatch changes under measured-traffic C | AGREE | FP:43-44 (scope to drop-ETA dispatch changes, CX18:97, B41) |
| A41 | 122 | WP14r: 37,214 decisions; 6 records in 4 decisions (C-60 2 / 1, C-120 4 / 3); all served | AGREE | V13:422,129 |
| A42 | 123 | Synthetic (deduplicated): 4 records in 3 decisions; ≤ 1 rejection | AGREE | V13:423; CX15:89 ("associated", not causal) |
| A43 | 124 | "Rule C functioned de facto as a single-step dispatch cap (\|c\| ≤ B). The active working ingredient …" | WRONG [in] | CX15:193 explicitly replaces "the working ingredient is …". Row 32 (counterfactual) is CANNOT CHECK (CX15:93). B is an **all-trip** budget, not a fresh B per step (CX18:181) |
| A44 | 129 | Occupancy 0.535 per vehicle (U) vs ≈ 1.33 in FleetPy | AGREE | V13:409-410; CX15:75-76 (includes idle time; descriptive only) |
| A45 | 129 | "(load factor 0.814)"; "fleet load is exceptionally sparse" | WRONG [later] | 0.814 is the **offered load x = λτ/B**, equal for U and C-30 (LOAD:2-3). It is not a vehicle load factor. A fleet whose offered load is x ≈ 0.81 is not "sparse"; what is low is occupancy. Also, the anchor FP:44-45 contains neither number |
| A46 | 130 | "6–8 passenger vans … +15, +15, +10 s → 40 > 30 s" | CANNOT CHECK | An unlabelled illustration. The panel uses 4-seat vehicles (BG:203) |
| A47 | 132 | Median nonzero revision under U is 108.6 s | AGREE | V13:403; CX15:69 |
| A48 | 132 | Anchor FP:48-49 for the 108.6 s | WRONG [in] | FP:48-49 holds the 109.6 s overshoot median of the 148 requests. Also, 108.6 s is "a descriptive observation … not by itself the cause of inertness" (CX15:205) |
| A49 | 133 | WP14r C-120: 51.8 + 80.3 = 132.1 > 120 s | AGREE | V13:422. Minor: the new candidate was pruned, not the rider |
| A50 | 133 | WP14r FREE: 50 / 1,629 riders (3.07%) with ≥ 2 revisions | AGREE | FP:44-45 |
| A51 | 135-136 | The stability-first objective suppresses repeated revisions | AGREE (later corroborated) | Riders with ≥ 2 changes: 0.19–0.49% under stability-first vs 3.07–4.09% under cost-first (EV:230-237) |
| A52 | 138 | 0 s dwell | AGREE | BG:205 |
| A53 | 138 | "realistic 30–45 s passenger boarding delays (as in FleetPy ETRR 2026)" | WRONG [in] | The anchor gives **30 s** boarding / alighting (CX15:76). "45" is unanchored |
| A54 | 138 | Dwell "would compound pickup detours into distinct incremental delays" (a route to accumulation) | CANNOT CHECK | New hypothesis. My inference: at B = 30 s, one inserted stop with ≥ 30 s dwell before an on-board rider's drop already exceeds B in a single step, which favours per-step failures. A cumulative effect is more plausible at B ≈ 120 s |

### Q4 (cost-first selection)

| # | AG line | Statement | Verdict | Correct value / anchor |
|---|---|---|---|---|
| A55 | 147-153 | Hierarchy at SEL:271-385: forced → accepted → worst utilisation + 10 revision dimensions → operational cost → id rank | AGREE | Opened SEL:276-385; V13:433 (row 33) |
| A56 | 151 | Utilisation level saturated: 3,503 / 3,503 (U), 3,506 / 3,506 (C-30) | AGREE | V13:435 |
| A57 | 154 | Cost-first = skip level 3; keep level 1, level 2 and every gate | AGREE | V13:212-215; CX15:343 |
| A58 | 154 | FREE (rolling-cost) strips hard limits and locks | AGREE | POL:287-335: the rolling-cost kind never calls the hard assessor; V13:441-442 |
| A59 | 158 | Shared rides U 22.8%, C-30 13.4% | AGREE | V13:401 |
| A60 | 158 | C-30's pooling falls 22.8 → 13.4% **because** "the stability objective rejects [the pooled insertion]" | WRONG [in] | U and C-30 run the **same** stability-first selector, and their configs differ only in the drop hardLimit (V13:225-226,436). The accepted count is maximised before any revision level (SEL:297-303 before :319-331). Cost-first re-selection over 62,837 recorded states changed the accepted count **0 times** (EV:350-356; FV17:536, B51). AG:335 itself says U and C share the selector |
| A61 | 159 | "Cost-first under C-30 is hypothesized to increase sharing by ≥ 10 pp over C-30 (Hypothesis P2.1; R13:277)" | WRONG [in] | R13 P2.1 concerns **U-cf** (≥ 32.8% = U + 10 pp, V13:277). For C-30-cf, R13 only asks that absolute shared completions exceed ≈ 313 (V13:285-286), and Codex later asked +10% relative (CX17:181). +10 pp on C-30 would be ≈ +234 shared completions. Later fixed-state evidence: under C-30 gates 104 / 1,715 = 6.1% of decisions change, accepted count 0, summed plan-cost change 0.079% (EV:355; CX17:43; CX18:113). "First-order evidence for a sharing gain under the 30-s cap is weak" (FV17:247-249) |
| A62 | 159 | WP14r FREE 53.1% vs LOCKS 21.8% shared (a package comparison) | AGREE | V13:251 |
| A63 | 161 | Cost-first C-30 may produce the first cumulative-only records (P2.4) | CANNOT CHECK | A hypothesis. Later: the prior is low at 30 s, with 0–2 per 1,629 on uncapped paths (FV17:787, E4). The accumulation test moved to B = 120 with a per-step arm (FV17:205-212; CX18:180) |
| A64 | 163 | The Σ\|c\| bound is preserved by construction | AGREE | It bounds dispatch movement only, not arrival (CX15:217) |
| A65 | 164 | "Pickup ETA instability may increase substantially" | WRONG [in] | Pickup time is locked at confirmation under U and C (BG:108 "vẫn khóa xe, điểm đón và giờ đón khi xác nhận"; EV:373). At fixed states, pickup-ETA and switch revision levels change by 0 in every arm (EV:360-361). Only a newly accepted rider's initial wait can change (see §3) |
| A66 | 166 | Toggling to RollingCost is invalid: it loses forced recovery and hard limits (CX15:343) | AGREE (substance) | POL:322-335: the recovery flags and the hard assessor exist only in the hard-vector branch; FV17:238-240. CX15:343 itself speaks of the forced-reference level |
| A67 | 167 | Realised distance and busy time are unconfirmed | AGREE | V13:294-295; CX15:345 |
| A68 | 145 | "YES, the system behavior would materially change" | CANNOT CHECK | Untested. At fixed states, 26.0% of new-request decisions change under U gates but only 6.1% under C-30 gates (EV:352-355). FV17:661: "Sẽ khác một phần, nhưng chưa biết khác bao nhiêu" |

### Q5 (forecast, data)

| # | AG line | Statement | Verdict | Correct value / anchor |
|---|---|---|---|---|
| A69 | 178 | Fielbaum & Alonso-Mora used 15/01/2013 13–15 h to "disregard unreliability due to traffic conditions" | AGREE | FP:85-89 |
| A70 | 179 | That dataset "contains zero adverse weather anomalies" | CANNOT CHECK | Not in its inputs. Later: no snow on the ten Mon–Thu dates (CX18:136, B70), but 17.5 mm of rain on 16 Jan (NOAA13:6) |
| A71 | 179 | "a pre-ride-hailing era (2013 vs 2018)" | WRONG [in, unanchored] | Unsupported. A missing 2013 FHV-HV row does not mean zero ride-hail (FV17:580, B91; CX18:135, B69) |
| A72 | 174 | The owner's 2013 and multi-year proposals are "unviable and based on a fundamental misreading of prior work" | WRONG [in + later] | Only the F&AM **window** is the wrong sample. The full 2013 year and the 2009–2020 archive are usable as extra-history or multi-event training in future work (FC:459-465; CX17:111 "Reject blanket '2013 is the wrong data'"; FV17:436-441; CX18:187). FP:75-77 already said the factor method is rebuildable |
| A73 | 181 | Nov 2018 has 8,155,449 rows | AGREE | FP:78 |
| A74 | 183 | No public TLC schema records promised drop-off times | AGREE (scoped) | Scope: inspected schemas only (CX15:126, row 55) |
| A75 | 182-186 | "FATAL SCHEMATIC & PIPELINE BARRIERS" (no labels, simulator mismatch) | WRONG [in] | Duration and factor models need no promise labels (CX15:303-309, correction 7). The offline factor benchmark needs **no simulator** (FC:368-407, Stage 1, 0 runs) |
| A76 | 184 | One city-wide 15-min factor; bundle covers 12–18 Nov 2018 only | AGREE | FP:74-75 (15-min; hourly covers 11–18) |
| A77 | 185 | One weekday with ≥ 1 in of snow in Sep–Dec 2018 (15 Nov) | AGREE | FP:81 |
| A78 | 185 | Jul 2016–Feb 2020: 7 weekdays with ≥ 3 in of snow | AGREE | FP:81; NOAA:7. Missing context: the same window has 16 weekdays ≥ 1 in; 2014-01–2020-02 has 34 / 19; 2009–2013 has 26 / 15 (NOAA:6-7; NOAA13:2) |
| A79 | 185 | "massive confounding from holiday schedules and network infrastructure changes" | CANNOT CHECK | No anchor |
| A80 | 186 | Wrappers read factor files only from the bundle (preflight_world.py:51-71) | AGREE | FP:82-84 (cites :51-55,71) |
| A81 | 186 | Simulating a new day takes "an effort exceeding 80–120 hours with severe risk of environment corruption" | WRONG [in, unanchored] | No input has this number. The only estimate for simulating new days is 30–45 h plus risk, about 64 jobs (FC:430-443). The 80–140 h estimate is for the offline forecast benchmark, a different task (FV17:450) |
| A82 | 193 | Fair input: "the realized city-wide factor in the preceding 15-minute bin" | WRONG [later; partly in] | A bin's factor is built from trips that **start** in it, so it is known only after they end, about 15–30 min later (FP:75-76; FC:98-100,305-306). "Not necessarily finalized after one bin, or even two" (CX17:101). Fair rule: completed trips plus a declared delivery lag (FV17:444) |
| A83 | 194 | Weather advisories active at quote time are allowed | CANNOT CHECK | Archives with issuance times are UNVERIFIED (FC:366). The NWS forecast that morning was far off (FC:125-128) |
| A84 | 197 | Two-sided frontier (late vs extension and early arrivals) at equal quote cost | AGREE | CX15:167-177; FV17:446-447 |
| A85 | 200 | "the snow storm starting at 13:00 on Nov 15" | WRONG [unanchored; later] | The first Central Park snow report is at **13:44**; the factor rises from 13:30. At 13:00 the factor (4.06) was *below* that of 14 Nov (4.39) (FC:111-112; CX17:103; FV17:551, B65) |
| A86 | 200 | "The damped-trend filter projects this upward momentum forward" | WRONG [later] | The protocol's fit gives α = 1, β = 0, φ = 0.8: no trend, and forecasts equal the historical profile (FC:54-57,154-160; CX17:50,93; CX18:127, B61) |
| A87 | 201 | It is a display-layer replay over existing Nov 15 / 16 trajectories | AGREE | BG:482-487 |
| A88 | 201, 319 | "10–14 hours" | CANNOT CHECK | No anchor. The fair multi-event version is 80–140 h (FV17:450) |

### Direction 1

| # | AG line | Statement | Verdict | Correct value / anchor |
|---|---|---|---|---|
| A89 | 217 | 458,477 decoded frames, 227 transcripts | AGREE | CX15:11-13 |
| A90 | 217 | "100% verified … by independent readers" (soundness 5/5) | WRONG [in] | Specific counts were reproduced, but row 32 is CANNOT CHECK and row 45 is WRONG (CX15:93,111). Both later strict reviews score soundness 3 (FV17:135-137) |
| A91 | 220, 250 | 14–20 h, 0 runs | AGREE | V13:190. Superseded by 24–40 h for the whole-thesis rewrite (FV17:163) |
| A92 | 226 | Closest prior: F&AM (pre-decision control), S&P (first-offer deadline, static times), HZ-B (per-step 0 s bound) | AGREE | V13:152-158 |
| A93 | 227 | "Genuine Novelty: First empirical demonstration … alongside an empirical audit proving the cumulative clause functioned as a per-step cap" | WRONG [in] | CX15:321-323 (correction 8) forbids implying no earlier dispatch-only controls. HZ eq. 7 already uses the traffic-updated reference (FV17:455-459). "Proving" contradicts CX15:93 (row 32) |
| A94 | 231-240 | Frontier table, all numeric cells (8 rows) | AGREE | V13:88-96; CX15:167-171. My AJ re-sum: U + forecast + 60 s early60 = 1,033; M⁺-30 naive late120 = 11 → timely120 2,327; M⁺-30 early60 3 / 2,338 = 0.13%; U + forecast + 30 s late120 68 → 2,366; U + forecast + 60 s late120 48 → 2,386; extensions 7.18 / 37.18 / 67.18 / 7.37 / 7.34 s |
| A95 | 233-236 | "Self-Broken Promises 0.0%" for U, U + forecast and padded-U rows | WRONG [in] | U has no drop-promise obligation, so the value is not 0% but undefined. Inputs report self-broken shares only for C-30 / M⁺-30 / M⁺-60 / V-30 (V13:392) |
| A96 | 244 | U ∩ C = 2,207; 227 / 131; C ∩ M⁺ = 2,332; 6 / 6 | AGREE | V13:395 |
| A97 | 245 | Liability table at T ∈ {1, 2, 5, 10} min | AGREE | V13:115-121 |
| A98 | 248-249 | Reproduce "within ±0 riders"; kill "if any discrepancy > 1 rider" | WRONG (internal) | A ±0 target with a > 1 kill rule leaves an undecided gap. V13:199 uses ±1 |
| A99 | 252 | Padded U: 5× the extension (37.2 vs 7.4 s), 10× the early share (1.81 vs 0.17%), 106 vs 10 late | AGREE | Arithmetic: 5.0×; 10.6× (44 vs 4 riders) |
| A100 | 252 | "C-30 protects the brand without inflating promises" | WRONG [in] | No brand, retention or satisfaction claim may be made (CX15:231-247, correction 3; D03:236-245) |

### Direction 2

| # | AG line | Statement | Verdict | Correct value / anchor |
|---|---|---|---|---|
| A101 | 271 | "Prior literature has studied lexicographic vs weighted objectives in ride-pooling (e.g. Schulz & Pfeiffer 2026)" | CANNOT CHECK (unanchored attribution) | Inputs say only "weighted, ordered and lexicographic objectives are known (D03E:177)" (V13:245), and D03:177 names no paper. BG:148-157 describes S&P as fixed times, acceptance probability e^(−μ·RD), a 900 s deadline and a maximise-acceptances objective |
| A102 | 264 | ≈ 3 h wall at 6 parallel jobs | AGREE | V13:265-267 (cost-first runtime UNCONFIRMED) |
| A103 | 265, 281, 288 | 4 + 2 + 68 = 74 runs, 25–35 h, Tier T2 | AGREE (inputs) | V13:261-266; CX15:349. Superseded: staged 108 + 72 (FV17:220-231; CX18:215) |
| A104 | 284-287 | P2.1–P2.4 thresholds (≥ 32.8% / kill < 25.8%; ≤ 4.25%; ≥ 2,315; ≥ 1 cumulative-only) | AGREE | V13:277-289 |
| A105 | 284-287 | Kill readings: "not a lever", "cap alone protects", "ordered objective doing essential reliability work", "remains inert" | WRONG [in] | Replace "cap alone suffices" (CX15:225). A missed materiality target is not an invariance or insignificance proof (CX18:197-204) |
| A106 | 290 | Pickup volatility rising would "directly prove the value of the stability-first ordered objective" | WRONG [in] | An outcome contrast cannot isolate the objective's causal role (CX15:351; CX18:200). The premise also fails: pickup ETAs are locked (row A65) |

### Direction 3 (Gardner–McKenzie nowcasting replay)

| # | AG line | Statement | Verdict | Correct value / anchor |
|---|---|---|---|---|
| A107 | 301, 321 | "true held-out adverse shock days"; "Nov 15 is evaluated zero-shot" | WRONG [in] | "Retrospective: dates already inspected" (FP:70-71); "all 7 bundle days … were inspected before this round" (FC:21-22). Confirmatory scores must exclude the inspected week (CX17:147) |
| A108 | 302 | Reproducibility 5/5: "deterministic Python replay script" | WRONG [in] | The protocol was "CHƯA niêm phong, CHƯA chạy" (BG:362). No script existed until R16 built screens (FC:134-135) |
| A109 | 313 | "Calibrate α, φ strictly on Nov 11–14 factors" | WRONG [in] | BG:483 says calibrate on 14/11, and the R12 protocol fixes 12/13 (FC:89-91). 15-min factors exist only for 12–18 Nov (FP:75). It omits β, which the fit sets to 0 |
| A110 | 314 | Snow afternoon: 601 riders | AGREE | V13:458 (34 of 601) |
| A111 | 314 | Nov 16 w07/w08 holdout: "431 riders" | WRONG [unanchored; later] | Not in any input. C-30 served on 16 Nov is **197 (w07) + 220 (w08) = 417** (my sum over the 6 cells' ledgers in AJ). 431 = 1,032 − 601 would mix the 15–16 Nov backtest population (376 riders on 15 Nov plus 656 on 16 Nov, CB C-30 fold 1) with the snow cells |
| A112 | 315 | Equal-cost benchmark at the historical profile's "+13.7 s" | WRONG [in] | 13.7 s is the 21-cell weekday cell-mean extension (V13:454). The handoff protocol fixes an equal quote length of 30 s (BG:485). The historical profile's extension on the snow cells is 2.0 s (FC:202) |
| A113 | 317 | Targets: snow ≥ 1.0 pp better, weekday no more than 0.2 pp worse | AGREE | BG:486 |
| A114 | 317 | Baselines 5.94% → ≤ 4.94%; weekday ≤ 0.37% | WRONG [in] | 5.94% is a cell mean; pooled it is 34 / 601 = 5.66% (CX17:95; CX18:125, B59). 0.37% treats the 21-cell weekday mean (0.17%) as a Nov-16 baseline. A prediction at ≥ 1.0 pp with a kill only below 0.5 pp leaves an undecided band |
| A115 | 318 | Kill rule: "report the residual as an unforecastable external shock" | WRONG [later] | The residual is method-dependent, not a knowability limit (FV17:429-431; CX17:97; CX18:331) |
| A116 | 306 | Verdict "ACCEPT (EXCELLENT APPENDIX)", scores 3/3/5/5/5/5 | WRONG [in] | Its own input demoted this item: "At most a sealed appendix; its weekday headroom is at most 2 riders" (V13:374). Later: "Not recommended at all before the deadline: re-running the Round-12 damped-trend protocol (it degenerates)" (FV17:320-321). Later scores for the Q5 direction: 1/2/3/1/4/2 (FC:471-476) and 1/2/3/2/3/1 (CX17:138) |

### §4 reviewer questions and §5 synthesis

| # | AG line | Statement | Verdict | Correct value / anchor |
|---|---|---|---|---|
| A117 | 216, 331 | "breaches its own promise in 14.5% of cases"; "deadline rules break 14.5% of promises" (unqualified) | WRONG [in] | V13:694 (D10): say it is a cell mean (12.4% pooled), conditional on the optimistic first quote |
| A118 | 332 | R2 defence scoped to "B = 30 s"; "acts empirically as a per-step dispatch cap" | WRONG [in] | The 98 runs cover B = 30…300 s (FP:39-40; CX18:301). The per-step wording is A43 again |
| A119 | 333 | Padding "degrades … customer trust to artificially inflate timely completion ratios" | WRONG [in] | No trust measure exists (D03:236-245). The padding comparison must be balanced: padded U serves 96 more riders and wins at 120 s, 2,366 vs 2,338 (CX15:175-177; FV17:175) |
| A120 | 334 | R4: building ML pipelines for "a 2-rider margin" is unjustified | WRONG [in] | The question was about the snow afternoon, where the headroom is 34 / 601, not 2 / 1,471 (FC:28-35). 2 / 1,471 is not a general bound (CX15:303-309) |
| A121 | 335 | U and C share the selector; late 203 → 76; 134 → 4 exposed-late | AGREE | V13:402; CX15:68 |
| A122 | 335 | C "eliminates pooling-induced exposure" | WRONG [in] | 134 / 203 and 4 / 76 are intersections, "not counts causally made late by pooling", and 4 remain (CX15:68,211-215) |
| A123 | 342-348 | "8 wording corrections in CX:185-326" (lists 6) | AGREE (incomplete) | There are 8 groups (CX15:185-325). It omits correction 6 (rider constructs), 7 (ML / data scope) and 8 (novelty), and it violates 7 and 8 itself (A20, A75, A93) |

**Tally:** AGREE 67, WRONG 46, CANNOT CHECK 10 (123 statements). Mixed statements were split, numbers versus
interpretation (for example A16 / A17, A26 / A27, A47 / A48), so that a correct number is never counted as wrong
because of its framing.

---

## 2. Focus checks (a)–(e)

### (a) Numbers not present in the inputs (possible fabrication)

| Number / fact | Where | Status |
|---|---|---|
| 431 riders (16 Nov w07/w08) | AG:314 | **WRONG**: the correct value is 417 (197 + 220; AJ). It is probably 1,032 − 601, an invalid derivation (CB) |
| Snow "starting at 13:00" | AG:200 | **WRONG**: 13:44 (FC:111-112) |
| "80–120 hours" to simulate a new day | AG:186 | **Unanchored**; the only estimate is 30–45 h plus risk (FC:443) |
| "10–14 hours" for Direction 3 | AG:201,319 | **Unanchored** |
| "30–45 s" boarding | AG:138 | **WRONG**: 30 s (CX15:76) |
| "Nov 11–14" calibration | AG:313 | **WRONG**: 14 Nov (BG:483) or 12/13 Nov (FC:89-91) |
| "+13.7 s" equal-cost target | AG:315 | A real number misapplied (BG:485 says 30 s; snow HIST extension 2.0 s) |
| "Schulz & Pfeiffer … lexicographic vs weighted" | AG:271 | **Unanchored attribution** |
| "pre-ride-hailing era" | AG:179 | **Unsupported** (FV17:580) |
| "load factor 0.814" | AG:129 | **Mislabel** (LOAD:2) |
| Derived arithmetic: 60.76 / 62.55 / 63.40 / 63.92 / 61.60 / 61.66%; 1,033 early; +0.30 / +1.61 / +3.68 pp; 97%; +0.58 pp; 5× / 10× | various | **All correct** (I checked each one; 1,033 against AJ) |

No invented paper title or author was found. Every paper it names appears in its inputs.

### (b) Gardner–McKenzie damped-trend replay as a "fair viable" T0 direction — REJECT

1. **It returns a null by construction.**
   - Fitted as R12 prescribes (36 triples, 80 one-step targets on 12/13 Nov), the protocol selects α = 1.0, β = 0,
     φ = 0.8.
   - With initial trend 0, β = 0 and α = 1, the residual multiplier is 1, so the forecast equals the historical
     profile (FC:54-57,154-160).
   - Codex reproduced it independently: SSE 0.0118126096, triple (1, 0, .8), "withdraw running that protocol as a
     promising test" (CX17:50,93). CX18:127 (B61) adds the precise condition: β = 0 alone is not enough for α < 1.
   - "No fixed triple helps the snow afternoon without hurting weekdays." The best snow triple (1.0, 0.3, 0.98) raises
     weekday late60 from 1.98% to 2.40% and early60 from 4.90% to 6.35% (FC:157-159).
   - So "projects upward momentum forward" (AG:200) is false for the specified method.
2. **It is not held out** (A107). FP:70-71 says the dates were already inspected.
3. **Mis-specified inside its own inputs.** The calibration days are wrong (A109), the equal-cost target is wrong
   (A112), and β is omitted.
4. **Its information rule leaks** (A82): a preceding-bin factor is not delivered at quote time.
5. **Its own input had already demoted it** (V13:374). The later verdict says not to re-run it (FV17:320-321).
6. **What survives, for fairness.**
   - The *idea* of adapting to an abnormal day has retrospective signal, but not via G&M. On the 601 snow riders a
     strict in-window blend gives 34 → 21; the "19" needs an undelivered morning prefix and a post-hoc gate; a lagged
     trend gives 29 (FV17:416-423).
   - That is one inspected event. The fair version is the 80–140 h multi-event future-work benchmark (FV17:442-450).
   - Antigravity's fairness principles are sound and match that design: no future factors, a two-sided frontier and
     equal quote cost (A84).

### (c) Sharing hypothesis for cost-first (≥ +10 pp) against the fixed-state re-selection evidence

- **Attribution error** (A61). The +10 pp target in R13 P2.1 is for U-cf, not C-30-cf.
- **Mechanism error** (A60).
  - The pooling difference between U and C-30 cannot come from the stability objective, because both use it.
  - The accepted count ranks first among the two (SEL:297-303 before :319-331).
  - Re-selection at fixed states never changed the accepted count (0 changes in all 5 arms, EV:350-356).
- **Evidence it could not see.** On the WP14r recorded portfolios (62,837 / 62,837 selections reproduced), dropping
  the stability levels under C-30 gates changes 104 / 1,715 new-request decisions (6.1%). The extra plan-summed drop
  movement is at most 35.5 s (2 × 17.77 s), and the summed plan-cost change is 0.079%. Under U gates the figures are
  445 / 1,714 decisions (26.0%) and 0.307% (EV:352-356; CX17:42-43,63-65; CX18:113-114).
- **Reading.**
  - A sizeable change under U-cf is plausible.
  - A "substantial recovery of shared-ride pooling" under C-30-cf is not supported. Codex lowered its own confidence
    in even a +10% relative target (CX17:61).
  - The final design makes attribution (the DiD on late60) primary and sharing a key secondary (FV17:245-249;
    CX18:216).
  - All of these are fixed-state screens on older fixed-traffic runs, not trajectories (FV17:403-408).

### (d) Cumulative clause, the 1,256, 0.535 riders per vehicle, 7 snow weekdays in 4 years

- **Cumulative clause.**
  - Numbers: all AGREE (A39–A42).
  - Wording: WRONG in four places, A5, A38, A43 and A93 ("strictly unexercised (inert)", "de facto single-step cap",
    "working ingredient", "audit proving").
  - The approved sentence is in FV17:372-379, with CX18:301-307 noting that B varies by arm and is an all-trip budget.
- **The 1,256.**
  - AGREE as records (A22–A24). The later reconciliation shows 971 decisions and 973 request–run pairs, of which 807
    (83%) were served anyway (FV17:343-346). Antigravity did not have this, but did not contradict it.
  - WRONG: "solely" (A25) and "completely unaffected" (A27).
- **0.535.**
  - Value AGREE (A44).
  - WRONG: the "load factor 0.814" gloss and "exceptionally sparse" (A45). The 0.535 includes idle time and is a
    descriptive limitation, not a matched benchmark (CX15:75-76).
- **7 snow weekdays.**
  - AGREE with FP:81 for Jul 2016–Feb 2020 at ≥ 3 in (A78).
  - The conclusion drawn from it, "unviable" and "FATAL", is WRONG (A72, A75). The same source gives 16 weekdays
    ≥ 1 in for that window, 34 / 19 for 2014-01–2020-02 and 26 / 15 for 2009–2013 (NOAA:6-7; NOAA13:2).
  - The event count is an open design issue for future work (FV17:789, E6; CX18:259), not a proof of infeasibility.

### (e) Compliance with the overclaim corrections

| Correction | Respected? | Evidence in AG |
|---|---|---|
| CX15-1: narrow the cumulative finding | **No** | A5, A38, A43, A93, A118 (it does correctly add "not a proof of theoretical redundancy", AG:113) |
| CX15-2: number vs riders; obligation vs arrival; no causal blame | **Partly** | Correct: "same number, 2,332 common". Violations: A35, A105 ("cap alone"), A122 ("pooling-induced") |
| CX15-3: business value symbolic | **No** | A36 (Lyft as liability threshold), A100 ("brand"), A119 ("trust") |
| CX15-4: screens are not ceilings | **Partly** | A17 ("upper difference") |
| CX15-5: solver time units | **Yes** | AG:71, 348 |
| CX15-6: rider-reliability constructs | Not used | — |
| CX15-7: ML / data scope | **No** | A20, A72, A75, A120 |
| CX15-8: novelty boundary | **No** | A93 ("First empirical demonstration"); Direction 3 novelty 3/5 (A116) |
| CX15 §2: show both pad rows, balanced | **Table yes, prose no** | A94 vs A119 |
| CX18-1: Q2/Q3 scope (148 record-associated; B by arm; loosening can raise timely60) | **No** | A25, A27, A33, A118 |
| CX18-2: missed targets are not invariance proofs | **No** | A105 |
| CX18-3: residual is not a knowability limit; pooled vs cell-mean denominators | **No** | A114, A115 |
| CX18-4: no "hard gate vs penalty" novelty | Yes (not claimed) | — |
| CX18-5: staged budget | Superseded (74-run plan) | A103 |

Antigravity's §5 tells the owner to enforce the R15 corrections, while the same document violates correction groups
1, 3, 7 and 8.

---

## 3. Points where Antigravity adds something correct and new

1. **A guard metric for the cost-first study.** AG:164,289 worries about pickup degradation. With the premise corrected
   (confirmed pickup ETAs are locked, BG:108; EV:360-361), a valid residual concern remains: under cost-first, the
   initial pickup wait or initial pickup promise of *newly accepted* riders can change. The A2 guard list (FV17:270-274)
   has no initial-wait column; adding it is a cheap, correct improvement.
2. **Dwell time as a scenario factor for budget use** (AG:138). No other participant linked the 0 s dwell to the
   cumulative clause; others treated it as a forecast and transfer limitation (RV:169,256). It is a reasonable
   limitation sentence. Its direction is uncertain (A54): at B = 30 s it would probably create single-step failures,
   not cumulative ones.
3. **Small verified arithmetic for the frontier table.** It gives timely completions as a percentage of requests
   (60.76% … 63.92%) and the padded-U + 60 s early count, 1,033 riders (checked against AJ).
4. **Independent convergence (correct, not new).**
   - Cost-first selection and longer shared chains as the conditions under which accumulation could bind; consistent
     with EV:230-255.
   - The cost-first study as the single optional extension; consistent with FV17 A2.
   - The F&AM 2013 *window* as the wrong sample; consistent with FV17:433-435.
   - Strict quote-time information, a two-sided frontier and equal quote cost; consistent with FV17:442-449.
   - The padded-U-30 question as a top reviewer question; consistent with RV:254.

---

## 4. Wrong points that must not reach the owner or the thesis

1. Direction 3, the Gardner–McKenzie replay, offered as a viable, held-out, 10–14 h T0 study or an "excellent
   appendix" (A86, A107–A116).
2. "The owner's 2013 / multi-year idea is unviable / a fundamental misreading", "pre-ride-hailing era" and "FATAL
   barriers" (A71, A72, A75).
3. "Cost-first under C-30 raises sharing by ≥ 10 pp" and "the stability objective rejects pooled riders" (A60, A61).
4. "Loosening the cap destroys drop reliability with negligible gains", and "120–300 s caps permit single-step
   revisions exceeding 2–5 min" (A33, A34).
5. "The cumulative clause is strictly inert / a de facto per-step cap / proven by the audit" (A5, A38, A43, A93, A118).
6. "First empirical demonstration" and the 5/5 soundness and rigor scores. The top-venue verdict "ACCEPT WITH MAJOR
   REVISION" contradicts the REJECT given by both later strict reviews (A90, A93; CX17:127; FV17:70; CX18:218).
7. "Pickup-ETA instability may increase substantially" (A65, A106).
8. Business and trust wording: "protects the brand", "customer trust", "Lyft liability threshold" (A36, A100, A119).
9. "148 rejected solely because of budget" and "1,186 completely unaffected" (A25, A27).
10. The leaky information rule ("realized factor of the preceding 15-min bin") (A82).
11. The wrong or unanchored numbers: 431 (correct 417), 13:00 (13:44), 80–120 h, 30–45 s, Nov 11–14, the +13.7 s
    target, "load factor 0.814", and the self-broken 0% shown for U (A45, A53, A81, A85, A95, A109, A111, A112).
12. "No drafted chapters / 0 thesis results drafted" (A21). The thesis exists and needs rewriting, not first drafting.

---

## 5. Overall reliability rating: **2 / 5**

| Aspect | Rating | Reason |
|---|---|---|
| Transcription of input numbers | 5 / 5 | Every copied number checked was right, including the full 8-row frontier |
| Self-introduced numbers and facts | 1 / 5 | 8 of 10 wrong, 2 unverifiable (§2a) |
| Interpretation within its own evidence | 2 / 5 | About 40 of 46 errors were contradicted by its own inputs, for example: FP:59-60 on the cap panel, FP:70-71 on inspected dates, V13:277 on P2.1, V13:374 on the G&M demotion, BG:108 on pickup locks, BG:485 on the equal 30 s quote, BG:71 on the thesis existing, and the CX15 corrections it lists itself |
| Strategic recommendation | 3 / 5 | "Keep the storyline; zero-run consolidation first; at most one optional cost-first study" is right in direction, but it restates its inputs and is superseded by the whole-thesis rewrite and the staged 108 + 72 study. Its one new direction is a null |
| Calibration of verdicts | 1 / 5 | 5/5 scores for soundness, rigor and reproducibility, and an "accept with major revision" at a top venue, against REJECT from both later strict reviews |

**Use rule.** Antigravity's file may be used as a source of reviewer questions: R3 (padded U), R5 (selector versus
cap), and the pickup-wait guard. No number, wording or direction from it should enter the thesis or the owner's notes
unless it is re-anchored to the audited files listed above.

---

## 6. Tóm tắt cho chủ nghiên cứu (tiếng Việt)

- Antigravity chép lại số liệu từ các tệp đầu vào khá chính xác: 67 câu đúng. Nhưng có 46 câu sai. Phần lớn là nói
  quá hoặc suy luận sai. Một số con số do Antigravity tự thêm vào cũng sai.
- **Không làm hướng 3 (dự báo Gardner–McKenzie).**
  - Khi chỉnh tham số đúng như giao thức vòng 12, mô hình tự quay về đúng cách dự báo hiện tại (α = 1, β = 0,
    φ = 0,8). Vì vậy chạy nó chắc chắn không cải thiện được gì.
  - Ngày tuyết 15/11 cũng đã được xem trước, nên không phải dữ liệu kiểm độc lập.
- **Không viết "đổi bộ chọn sang ưu tiên chi phí sẽ tăng đi chung thêm 10 điểm %" cho C-30.** Khi tính lại trên các
  quyết định đã ghi, với trần 30 giây bộ chọn chỉ đổi 6,1% quyết định, và không lần nào đổi số khách được nhận.
- **Không viết "nới trần làm hỏng độ tin cậy".** Ví dụ thật: ở 8 ô buổi sáng, trần 120 giây chở thêm 6 khách và có
  thêm 2 lượt đến không trễ quá 1 phút so với trần 30 giây.
- **Không viết "dữ liệu 2013 hay dữ liệu nhiều năm là vô dụng".** Chỉ riêng khung giờ mà Fielbaum và Alonso-Mora chọn
  là sai mẫu, vì họ cố ý tránh tắc đường. Cả năm 2013 và các năm khác vẫn dùng được làm dữ liệu học thêm. Đây là việc
  cho tương lai.
- **Ví dụ số sai.**
  - Antigravity ghi ngày 16/11 khung 7–9 giờ có 431 khách; số đúng là 417 (197 + 220).
  - Antigravity ghi tuyết bắt đầu lúc 13:00; trạm Central Park ghi tuyết lần đầu lúc 13:44.
- **Điểm đúng và mới.** Nếu làm thí nghiệm ưu tiên chi phí, nên đo thêm thời gian chờ đón của *khách mới nhận*. Giờ
  đón của khách đã xác nhận thì đã bị khóa, nên không thể "dao động" như Antigravity lo.
- **Kết luận.** Chỉ dùng bài của Antigravity để lấy câu hỏi phản biện, không dùng làm bằng chứng.

---

## 7. Verification record

- Read only. No simulation, build, install or deletion. `codex-work/R19-*` was not opened.
- The helper scripts are in the session scratchpad
  (`C:/Users/quang/AppData/Local/Temp/claude/e--Code-RideBound/4f238113-…/scratchpad/r19_probe_audit*.py`). They read AJ
  only. Their results are quoted in rows A12, A94 and A111.
- This file was created new; it did not exist before (checked with `ls` immediately before writing).

END OF R19 CHECK
