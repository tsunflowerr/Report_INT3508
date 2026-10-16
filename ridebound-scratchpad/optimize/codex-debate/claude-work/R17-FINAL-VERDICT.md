# R17 — Final verdict on rounds 16–17 (Claude final judge), 2026-10-10

**Role.** Final judge of rounds 16–17 (Claude vs Codex; Antigravity produced no output). Standard: a strict
top-venue referee (`ROUND16-REVIEW-STANDARD.md`). I owe nothing to either side's earlier ranking.

**What I read.** All files listed in the brief: `ROUND16-FACT-PACK.md`, `ROUND16-REVIEW-STANDARD.md`,
`ROUND16-CLAUDE.md`, `ROUND17-CLAUDE.md`; Codex `R16-CODEX.md`, `R17-REBUTTAL-CODEX.md`, `R15-CONFIRM-CODEX.md` and
their helper outputs; Claude `R16-EVIDENCE/FORECAST/REVIEWER-CLAUDE.md`, `R17-REBUTTAL-CLAUDE.md` and their helper
outputs; `R13-FINAL-VERDICT.md` (§0–A2); the handoff `BAN-GIAO-PHIEN-2026-10-09.md` (§3–§8); Hörl & Zwick 2022 text
(lines 480–619); Fielbaum & Alonso-Mora 2020 text (lines 565–610, 1039); the claim boundary D03; the thesis LaTeX
(02 in full; 05, 07, 08, 09 at the cited lines; the bibliography); the selector and policy source.

**What I ran.** One read-only helper, `claude-work/r17-final-judge/spot_check_forced_noworse.py`, one process: it
decodes the terminal checkpoint frame of 3 T3.8 M⁺-30 transcripts, checks the frame SHA-256 and counts breach-kind
tokens. Output `spot-check-forced-noworse-2026-10-10.txt` (mode "x"); stderr empty (`spot-check.stderr.txt`). No
simulation, build, install, deletion, or write outside `claude-work/R17-FINAL-VERDICT.md` and that folder.

**Labels.** [M] measured on archived runs (by me or reproduced by both sides); [S] first-order screen on recorded
states (not a policy result); [A] arithmetic; [I] inference; [H] hypothesis/prediction; [O] reviewer opinion;
UNCONFIRMED = I did not check it.

**Anchor keys** (relative to `E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/` unless absolute).

| Key | File |
|---|---|
| FP / STD | `ROUND16-FACT-PACK.md` / `ROUND16-REVIEW-STANDARD.md` |
| A | `codex-work/R15-audit-summary.txt` (Codex independent 227-transcript audit) |
| R15 | `codex-work/R15-CONFIRM-CODEX.md` |
| CX16 / CX17 | `codex-work/R16-CODEX.md` / `codex-work/R17-REBUTTAL-CODEX.md` |
| CAP / WX / SCOPE | `codex-work/R16-cap-outcomes.txt` / `R16-weather-inventory.txt` / `R16-scope-inventory.txt` |
| PV / CASE / SF / META / SIZE | `codex-work/R17-portfolio-verification.txt` / `R17-C30-sum-case.txt` / `R17-screen-forecast-verification.txt` / `R17-metadata-verification.txt` / `R17-data-size-verification.txt` |
| EV / FC / RV / CR17 | `claude-work/R16-EVIDENCE-CLAUDE.md` / `R16-FORECAST-CLAUDE.md` / `R16-REVIEWER-CLAUDE.md` / `R17-REBUTTAL-CLAUDE.md` |
| DIAL17 / WP17 / DER17 / EL17 / WX17 | `claude-work/r17-rebuttal/r17-verify-dial-…txt` / `r17-wp14r-check-…txt` / `r17-derived-counts-…txt` / `r17-wp14r-elapsed-…txt` / `r17-weather-recount-…txt` |
| IDN | `claude-work/r16-evidence/q2-screen-identity-w07-2026-10-10.txt` |
| RP1 / FS1 / FS2 / PQ / NOAA13 | `claude-work/r16-forecast/rider-nowcast-replay-2026-10-10.txt` / `factor-nowcast-screen-2026-10-10.txt` / `factor-nowcast-screen-v2-2026-10-10.txt` / `parquet-footer-probe-2013-2026-10-10.txt` / `noaa-event-days-2009-2013-2026-10-10.txt` |
| BUD / SHARE / EXP / CVP | `claude-work/budget-block-diagnosis-2026-10-07.txt` / `pooling-share-2026-10-06.txt` / `exposure-check-2026-10-06.txt` / `claude-work/r13-proposer/cumulative-vs-perinsertion-2026-10-10.txt` |
| RUNTIME / TLC | `claude-work/RUNTIME-ESTIMATE-2026-10-07.md` / `claude-work/r13-ml-data-samples/tlc_data_reports_monthly.csv` |
| SPOT | `claude-work/r17-final-judge/spot-check-forced-noworse-2026-10-10.txt` (this round) |
| V / HO | `claude-work/R13-FINAL-VERDICT.md` / `E:/Code/Report_INT3508/BAN-GIAO-PHIEN-2026-10-09.md` |
| HZ / FAM | `claude-work/pdf/hoerl-zwick-2022.txt` / `C:/Users/quang/AppData/Local/Temp/claude/e--Code-RideBound/4f238113-dd3b-4bd1-b13f-53613b57f0e6/scratchpad/papers/Unreliability_in_ridesharing_systems_Measuring_cha.txt` |
| D03 | `E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md` (read only) |
| TEX | `E:/Code/Report_INT3508/ridebound/noi-dung/` (read only) |
| T38 / RUN38 / WP4 / W07X | `E:/Code/Report_INT3508/ridebound-scratchpad/tang3/t38/T38-REPORT.md` / `…/tang3/t38/run_t38.py` / `…/tang3/configs/wp4-tier3-v2.json` / `…/tang3/w07x/W07X-REPORT.md` |
| FR / SNOW | `E:/Code/Report_INT3508/ridebound-scratchpad/optimize/FORECAST-REPORT.md` / `…/optimize/test-snow-2026-10-06-report.txt` |
| SEL / POL | `C:/Code/RideBound-noworse/src/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs` / `…/SolverBackedRidePoolingPolicy.cs` |

---

## 0. Bottom line

1. **Sequencing: Codex is right.** The single next step is the whole-thesis claim-and-results rewrite, with **0 new
   simulation jobs**. The LaTeX was last built on 30 Sep 2026, contains no T3.8 result, never cites Hörl & Zwick
   2022, and sells claims that HZ eq. 7 and the thesis's own recovery-(b) data contradict (§D). The rewrite is needed
   whatever any experiment shows; an experiment cannot repair those sentences.
2. **Optional extension (at most one): a staged selector × cap mechanism study.** Stage 1 = Claude's 2×2
   {stability-first, cost-first} × {U, C-30} (74 jobs) plus stability-first C-120 (34 jobs, no code, archived
   binary) = **108 jobs**. Stage 2 = cost-first C-120 + cost-first per-step-120 (72 jobs), **only** if a registered
   Stage-1 gate shows that accumulation can bind. Primary endpoint: **attribution** (objective × cap interaction in
   naive late60), not sharing. Codex's 178-job design is right in content but wrong to front-load the riskiest
   engineering (the per-step semantics) before knowing whether accumulation can bind.
3. **Q2.** Making "all 1,256 feasible" is essentially U, which is already measured: +96 served, +127 late60, −31
   timely60 per request. A moderate cap (120 s) is "better" only at a ~2-minute tolerance; the main-panel point is
   missing and is the cheapest piece of the extension.
4. **Q3.** The cumulative clause was never the recorded reason for a refusal on measured traffic; whether it changes
   trajectories is unrun. "No effect" and "behaviourally inert" are both too strong.
5. **Q5.** Incident-day forecasting is a legitimate *future* direction (80–140 h, all components prior work); it
   cannot touch rule C (dispatch = 9 s of 3,446 late-seconds on the snow afternoon). Fielbaum & Alonso-Mora's 2013
   window is the wrong sample (chosen to disregard traffic); the full 2013 archive is usable only as an extra-history
   ablation.
6. **Strict-venue verdict on the current core: REJECT** (both sides agree). Undergraduate thesis: defensible after a
   major text revision (committee standard UNCONFIRMED).

---

## A. Final ranked list (≤ 3 items)

### Resolution of the sequencing dispute (decided)

| | Codex R17 (CX17:3,69,153-163,211) | Claude R17 rebuttal (CR17:314-363) |
|---|---|---|
| Single next step | rewrite the whole thesis, 0 jobs | the cost-first 2×2, 74 jobs; rewrite "mandatory" in parallel |

**Decision: rewrite first.** Reasons, each confirmed from files:
1. **It is mandatory regardless of outcomes.** Both sides say so: CX17:69; CR17:360-362 ("The rewrite is the binding
   constraint and is needed whatever this experiment shows"). Claude's own R16 referee also put it first
   (RV:526-538).
2. **The exposure is in the text, not in the data.** The abstract claims "the core departure from the literature is
   that the displacement is decomposed by cause" (TEX/02-tom-tat.tex:66-69; Vietnamese :17-20) and that "only the
   conduct cap is never the cause of an empty choice set" (:71-75; :22-26). HZ eq. 7 already sets the required drop-off
   to max(updated, latest) using the traffic-updated route (HZ:529-541,567-569). The bibliography has 27 entries and
   no Hörl or Zwick (TEX/10-tai-lieu.tex:7-162; META:4,6). No T3.8 number appears in any TEX file (my grep for
   2338 / 2.338 / 2{,}338: 0 hits in 11 files). An experiment adds a result; it does not remove these sentences.
3. **Asymmetric deadline risk.** The deadline (mid-November) is UNCONFIRMED (HO:494). If the rewrite slips, nothing
   else matters. If the experiment slips, the thesis stays defensible. The experiment needs a worktree, a code option,
   tests and a Gate 0 against binary drift (R15 rows 38-40, not re-opened by me); its duration is uncertain.
4. **The experiment's interpretation depends on the rewritten claim.** What the cost-first result means ("the cap
   carries reliability" vs "the selector did") only makes sense once the contribution is stated without uniqueness or
   causal language.

Claude's best counter-argument: delaying the 2×2 risks never running the only non-definitional mechanism test
(CR17:50-54,314-318). I accept the risk: the thesis is defensible without it and is not defensible with the current
overclaims. The 2×2 remains the core of the optional extension.

---

### A1. RECOMMENDED NEXT STEP (exactly one): whole-thesis claim-and-results rewrite — 0 jobs

**What.**
1. **Re-centre the contribution** (abstract, ch.1 §1.3–1.4, ch.5). The contribution becomes: a specified,
   implemented and audited per-rider dispatch-only budget (rule C, Σ|c| ≤ B with c = p − e, FP:31-33), with the v/e/p
   ledger, plus a measured service / reliability / quote frontier on 34 measured-factor cells against U, the
   first-offer deadline M⁺ (run with recovery (b)) and quote padding.
2. **Position against the closest prior work**: Hörl & Zwick 2022 strategy B, Fielbaum & Alonso-Mora 2020 §6,
   Schulz & Pfeiffer 2026 (900 s, D03:214-217), Elmi et al. 2026 (D03:211-213). The handoff already demanded the HZ
   citation (HO:145-147,396).
3. **State the honest distinction from HZ-B [I, from the two definitions]:**
   - Under HZ eq. 7 the dispatch allowance is traffic-dependent: an at-risk rider gets zero extra dispatch delay;
     a rider whose trip sped up can absorb more than B.
   - C gives every rider the same dispatch allowance B, independent of traffic slack. It charges absolute changes in
     both directions, summed over the whole trip, with a per-rider ledger and certificate.
   - Do **not** claim "hard gate vs penalty". HZ also has hard routing constraints with relaxed required times
     (eqs. 9–10), plus a penalty for violating the original times (eq. 11) (HZ:575-588).
4. **Add the T3.8 results that are missing** (all zero-run, all audited):
   - the frontier U / C-30 / M⁺-30 × naive / forecast, padded U +30 / +60, served-set overlap, shared share,
     dispatch exposure;
   - the cumulative audit;
   - the w07 and WP14r cap dials;
   - the fixed-state cost-first screen as a labelled diagnostic;
   - the snow ledger as an exploratory limitation.
   Numbers are in the table at "What may be claimed" below.
5. **Demote by-construction properties.** The four-family theorem becomes a remark scoped "among the four families
   compared". Cap compliance (291 < 300 …) moves to validation. Unverified welfare rows go. "Causal attribution"
   becomes "model-based attribution". Full list in §D.

**Why.** Reasons 1–4 above. Also: under the strict standard the current core scores 2/2/3/2/4/4 in Codex's review
(CX16 strict-review table) and 2/2/3/3/4/4 in Claude's referee report, which notes 2–3 for rigor at journal level
(RV:163-172). Novelty and significance cannot be raised by writing, but soundness
can, by removing contradicted claims.

**Decisive evidence (zero runs).** Every headline number must reproduce from audited outputs:

| Target | Value | Anchor |
|---|---|---|
| Served U / C-30 / M⁺-30 | 2,434 / 2,338 / 2,338 | A:7-9; T38:46 |
| Naive late60 (riders) U / C-30 | 203 / 76 | A:7,9; DIAL17:12-13 |
| Forecast late60 U / C-30 / M⁺-30 | 137 / 10 / 10 | A:7-9 |
| Timely60 per 3,672 requests, forecast U / C-30 / M⁺-30; padded U +30 | 2,297 / 2,328 / 2,328; 2,328 | A:7-9 (fc, fc_pad30) [A] |
| Timely120, forecast C-30 vs padded U +30 | 2,338 vs 2,366 | A:7,9 [A] |
| Quote extension: C-30 + forecast vs padded U +30 | 7.4 s vs 37.2 s | A:7,9 ext_sum_ms / served [A] |
| Early60: C-30 + forecast vs padded U +30 | 4 (0.17%) vs 44 (1.81%) | A:7,9 |
| Served sets | C/M⁺ 2,332 common, 6 / 6 unique; U/C 2,207 common, 227 / 131 unique | A:18-19 |
| Cumulative audit (measured traffic) | 98 runs; 64,371 decisions; 1,256 budget prunings, all single-step > B; 0 cumulative-only | A:7,10-17 [A] |

**Sealed-style predictions / kill rules (process).**
- K1: any number in the abstract, ch.1 or ch.5 without an anchor in a claim–evidence table → remove it.
- K2: after the rewrite, uniqueness or causal phrases ("duy nhất", "chỉ … không bao giờ", "khác biệt cốt lõi so
  với văn liệu", "không ai tách", "quy trách nguyên nhân") occur only with an explicit scope ("trong bốn họ đã so",
  "phép chiếu mô hình").
- K3: HZ 2022 is cited in ch.1 positioning, in the theory remark and in ch.5.
- K4: one adversarial pass (Codex) on the rewritten contribution paragraph. Kill any sentence it can falsify with an
  anchor, rather than inventing a new novelty to save it (CX17:159).

**Effort.** 24–40 h for claim / evidence restructuring across chapters (Codex's estimate, CX17:161, which I adopt
because the cross-chapter scope is confirmed in TEX), plus the remaining writing and supervisor review.
UNCONFIRMED.

**Deadline risk.** Low (no code, no runs). It is the binding constraint.

**What may be claimed** (with scope: one simulator, measured city-wide factors, 34 previewed cells over 5 days):
- C is implemented and audited: 0 recorded budget overshoots (A:7). On T3.8, C-30 has 0 forced decisions vs
  41.3% (cell mean) for M⁺-30 (T38:58).
- C-30 and M⁺-30 serve the same number (2,338; 2,332 in common) and tie on forecast timely60 (2,328). The difference
  is in the obligation each one checks, not in rider arrivals.
- Against U: −96 served (2.6 pp of requests), −127 late60, +31 timely60 per request (naive and forecast).
- Padded U ties C at 60 s and beats it at 120 s (2,366 vs 2,338), at a longer quote and more early arrivals.
- The cumulative clause was never the recorded reason for a refusal (precise sentence in Q3 below).
- The historical-profile forecast cuts C-30 late60 from 76 to 10 riders on these recorded journeys (A:7).
  Retrospective replay; the gain is not specific to C (FR:65 per R15 row 50).

**What may NOT be claimed:**
- novelty of the cause-separated or traffic-updated reference;
- the never-empty property as unique beyond the four families;
- causal blame;
- empirical necessity of accumulation;
- "C serves more" or "C gives more on-time arrivals";
- business value, satisfaction or profit (D03:236-245);
- generality beyond this testbed;
- "0.17%" without its denominator (D03:267-268).

**Milestone and decision point.** When the abstract, ch.1 positioning and contributions, the T3.8 frontier section
and ch.5 are drafted, confirm the deadline. A2 may start only then (start rules in A2).

---

### A2. OPTIONAL EXTENSION (at most one): staged selector × cap mechanism study

**What.** Test the referee's most damaging open mechanism question: is C's reliability due to the cap or to the
stability-first selector that U and C share (SEL:276-303,319-331,365-368; utilisation level saturated in
3,503/3,503 U and 3,506/3,506 C-30 decisions, A:7,9)? And, only if it can bind, does accumulation change outcomes
versus a per-step rule?

**Why staged** (resolving the 74-vs-178 dispute):
- **Attribution needs only the 2×2.** SF-U and SF-C30 are archived; CF-U and CF-C30 are new. Codex itself certified
  74 jobs as "the minimum described plan" (R15:349).
- **Accumulation cannot be tested at B = 30 s.** On uncapped cost-first paths, cumulative-only riders are
  2/1,629 at 30 s but 13/1,629 at 120 s (WP14r FREE); WP9 panels show 12/1,735 and 10/966 at 120 s; T3.8 SF-U has
  4/2,434 (CVP:5,7,17,22,32).
- **A witness alone settles nothing.** Codex is right that a cumulative-only witness in CF-C120 needs a per-step
  counterpart before any outcome claim (CX16:263,265; CX17:184).
- **The per-step arm is the riskiest engineering.** It needs aligned assessor, validator, certificate and breach
  semantics (CX17:176). It should be built only if CF-U trajectories, which Stage 1 produces anyway, show enough
  cumulative-only exposure at 120 s.
- **SF-C120 is cheap and decoupled.** It runs on the archived runner `C:/RideBoundData/research/runner-tier3-v2`
  (RUN38 via run_w07.py:40) with the existing `C-120.json` (sha256 ac0f9758…). It needs no code and no Gate 0, and it
  answers the owner's Q2 on the main panel. Both sides included it (CR17:365-374; CX17:169-174).

**Arms, panel, jobs** (34 T3.8 test cells, same fixtures, worlds, seed 7, WP4 config with recovery (b); the 34 keys
are in SCOPE:14):

| Stage | Arm | Code | Jobs |
|---|---|---|---|
| 1a | SF-C120 (stability-first, cumulative 120 s) | none (config + copied harness entry) | 34 |
| 1b | Gate 0: new binary with the option OFF reproduces archived SF-U and SF-C30 on d20181116-s10-r1-w08 and -w17 | cost-first option | 4 |
| 1b | ON smoke: CF-U, CF-C30 on one cell | — | 2 |
| 1b | CF-U, CF-C30 (cost-first: forced → accepted → operational cost → id rank; gates, locks, recovery unchanged) | — | 68 |
| **Stage 1 total** | | | **108** |
| 2 (conditional) | CF-C120; CF-per-step-120 (gate δ ≤ 120 s per step; cumulative S kept for audit only) | per-step option | 68 |
| 2 | ON smoke 2 + OFF re-check 2 (the binary changes) | — | 4 |
| **Stage 2 total** | | | **72** |

If both stages run, the total is 180, i.e. Codex's 178 plus an OFF re-check after the second build. Compute at the
historical ~15 min/job, 6 in parallel (RUNTIME:24-25): about 4.5 h wall for Stage 1 and about 3 h for Stage 2.
Cost-first runtime on T3.8 is UNCONFIRMED; on WP14r the rolling-cost arm's median was 730 s vs 667 s (LOCKS) and
641 s (C-30) (EL17:2-6).

**Implementation constraints.**
- New worktree from `C:/Code/RideBound-noworse`; never `E:/Code/RideBound` or `E:/Code/RideBound-deadline`.
- Add a narrow objective-order option. Switching the profile to RollingCost alone is wrong: it drops the
  forced-reference level, which is conditional on HardVector/SoftHardHybrid (SEL:276-280), and policy kind
  rolling-cost skips the hard assessor entirely (POL:287,322-330).
- `dotnet test RideBound.slnx` and docs/18–19 updates in that research repo (AGENTS.md).
- Record full witnesses, solver status/bounds and generation/retention omissions (R15 row 37).
- The owner must approve every run (HO:480 "Chưa có việc nào được duyệt chạy").

**Primary endpoint: attribution, not sharing.**
- The referee's question is about reliability, and the thesis storyline is reliability.
- First-order evidence for a sharing gain under the 30-s cap is weak: only 6.1% of new-request decisions change, and
  the aggregate plan-cost change is 0.079% (PV:5). Codex lowered its own confidence in that target (CX17:61,181).
- Sharing stays the key secondary, reported whatever it shows.

**Sealed-style predictions [H]** (seal with a hash before Stage 1 starts; reference numbers from A:7,9, DIAL17:12-13,
SHARE:2-3, EXP:2-3, DER17:8,11):

| ID | Stage | Prediction | Basis | Kill / interpretation |
|---|---|---|---|---|
| a1 | 1a | SF-C120 served ∈ [2,362, 2,434] | Screen: 59/148 pass at 120 s, 49 of them U-served (EV:189; SF:14). WP14r C-30→C-120 +29 (r17-wp14r-check) | Below 2,362: the cap level is not the main service lever on this panel |
| a2 | 1a | SF-C120 naive late60 ∈ [90, 170] | C-30 76, U 203; WP14r +23 late60 for +29 served | Descriptive only |
| **a3** | 1a | SF-C120 naive timely120 per request ≥ 2,333, i.e. above both C-30 (2,327) and U (2,332) | Interior peaks: WP14r timely120 C-120 1,563 > LOCKS 1,557 > C-30 1,534; w07 C-90 660 > C-30 658 > U 656 (CAP:3-11) | ≤ 2,332: no interior gain at a 2-minute tolerance. Never call a single point "the optimum" |
| G0 | 1b | OFF reproduces the archived fleet-action fingerprints and final ledgers on all 4 gate jobs | binary drift is possible (R15 row 40) | Any mismatch: stop. No re-running of controls without owner approval |
| H1 | 1b | CF-C30: every rider S ≤ 30 s; 0 overshoots; every forced or no-worse record explained | contract | Fail: implementation defect, stop |
| H2 | 1b | Lever check: CF-U drop-exposed riders ≥ 261 (1.5 × 174) **and** naive late60 ≥ 243 (203 + 40) | At fixed states, 26.0% of new-request decisions change under U's gates, 426/445 moving an incumbent (PV:2; DER17:15). Exposed U riders are 77% late60 (EXP:2) | Fail: the selector is not a material lever under the locks on this panel; the confounder is small. Report it; no Stage 2 |
| H3 | 1b | Cap holds: CF-C30 naive late60 ≤ 4.25% of served and forecast late60 ≤ 1.0% of served (SF-C30: 3.25%, 0.43%) | 72 of 76 C-30 late riders had no recorded dispatch exposure (EXP:3); per-rider cap 30 s | Fail: withdraw "the cap alone suffices"; the selector does real reliability work |
| **H4 (primary)** | 1b | DiD = (CF-U − CF-C30) − (203 − 76) ≥ +40 riders (naive late60, pooled), and per-cell DiD > 0 in ≥ 15 of the 25 w08/w17 cells | H2 + H3; under SF, U > C-30 late60 in 25/25 w08/w17 cells (DER17:8,11) | DiD < +40 with H3 holding: the cap's protective effect does not depend on the selector (also informative). Every outcome is reported |
| H5 (guard) | 1b | Forecast timely60 per request: CF-C30 − CF-U ≥ +31 (the SF value 2,328 − 2,297) | rider-facing denominator (3,672) | Reported next to H4; not a second primary |
| H6 (key secondary) | 1b | CF-C30 absolute shared completions ≥ 345 (1.10 × ~313 = 13.4% × 2,338) with served ≥ 2,315 (99%) | Codex's target (CX16:260); 81/104 differing C-30 decisions move an incumbent (DER17:18). Low confidence | Fail: cost-first under the 30-s cap does not buy pooling here |
| H7 (Stage-2 gate) | 1b | On CF-U trajectories, ≥ 10 cumulative-only riders at B = 120 s (every nonzero move ≤ 120 s, sum > 120 s), about 4 per 1,000 served | Uncapped cost-first precedents 6.9–10.4 per 1,000; SF-U 1.6 per 1,000 (CVP:7,17,22,32) | < 10: do not build the per-step arm. Accumulation stays "never the recorded reason; unlikely to matter on this panel" |
| H8 | 2 | CF-per-step-120 has ≥ 5 completed riders with S > 120 s; CF-C120 has ≥ 1 distinct cumulative-only decision | H7 exposure | 0 and 0: no demonstrated need for accumulation in this tested design |
| H9 | 2 | Aggregate outcomes nearly equal: \|Δserved\| ≤ 10 and \|Δtimely60\| ≤ 10 between CF-C120 and CF-per-step-120 | the exposure is a few per 1,000 | A larger gap is a real outcome effect of accumulation, to report with its sign |

**Guards for every arm.**
- Report served; timely60/120 per request (naive and frozen causal-no15 forecast); late60/120 among served;
  early60; mean quote extension; median initial promised ride time; absolute shared completions; exposed and
  repeated riders; budget prunings; cumulative-only records and decisions; forced and no-worse counts; per-cell and
  per-day paired signs.
- An arrival gain achieved with a median initial promise more than 30 s longer is not claimed (CX16:161).
- No forecast retuning inside the study. Padded-U rows are descriptive references only, not matched controls
  (CX17:178).
- No new B or load values may be searched after a null and then called confirmation (CX17:186).

**Start rules and time boxes.**
- Start only after the A1 milestone, with the deadline confirmed.
- At least 3 weeks left: Stage 1 (1a then 1b).
- 1–3 weeks left: Stage 1a only (34 jobs, no code).
- Less than 1 week: nothing.
- Gate 0 must pass within 5 working days of starting 1b, and Stage 1 analysis must finish within 10 working days.
  Otherwise drop the rest and report it as future work.
- Stage 2 only if H2 and H7 pass and at least 2 weeks remain after Stage 1. At a mid-November deadline, expect
  Stage 2 to become future work.

**Effort [O, my estimate, UNCONFIRMED].**
- Stage 1a: 2–4 h (harness copy with its own inventory hash; analysis with the existing readers `r17_verify_dial.py`
  and `pooling_share.py`).
- Stage 1b: 25–43 h (option + tests 10–18; Gate 0 + smoke 3–5; analysis 6–10; write-up 6–10).
- Stage 2: 22–44 h (per-step semantics + tests 15–30; re-check 1–2; analysis and write-up 6–12).
- For comparison: Claude 30–50 h for the 2×2 (CR17:351); Codex 70–110 h for the 7-arm design (CX17:188).

**Deadline risk.** Stage 1a low; Stage 1b moderate to high; Stage 2 high.

**What may be claimed afterwards.** On 34 previewed cells over 5 days, with one simulator and city-wide factors:
whether the 30-s cap kept its reliability when the selector stopped ranking stability (H3/H4); whether cost-first
under the cap changed pooling (H6); one more point on the cap curve (a1–a3).

**What may not be claimed.**
- generality to other cities, loads or networks;
- realised operating-cost or profit savings: Schedule.OperationalCost is a plan cost counted repeatedly through
  time (SEL:365-368; CX17:65);
- "C-120 is optimal";
- "accumulation matters" from witnesses alone;
- independence of the 34 cells (5 days).

---

### A3. NOT before the deadline (future-work protocol, one paragraph in ch.5)

- **Multi-event causal incident-forecast benchmark.** Codex's design (CX16 Q5; CX17:190-198), with Claude's event-count
  concern recorded (§E). 80–140 h, plus 20–50 h if weather vintages are added. Every component is prior work
  (FC:254-265).
- **A literal HZ-style relaxed deadline p ≤ max(p0 + B, e)** as a direct baseline. It is a new gate type, distinct
  from recovery (b) (CX17:121,208).
- Not recommended at all before the deadline:
  - re-running the Round-12 damped-trend protocol (it degenerates, SF:27);
  - the 4-vehicle offered-load check (new fixtures, CX16:255; CR17:246-248);
  - new promise objects;
  - allocation;
  - an ML chapter (V:69; R15 §4).

---

## Explicit resolutions

### R1. Scope of the optional study
Decided as in A2:
- the 2×2 is the minimal design for attribution;
- SF-C120 is a no-code add-on that answers Q2;
- CF-C120 + per-step-120 are Stage 2, gated by H2 and H7.

Codex's argument that C120-stable is needed "to isolate cap relaxation from objective change" (CX17:174) holds for
a {CF} × {U, C30, C120} design. Under the staged design it is satisfied because SF-C120 runs in Stage 1a. Claude's
argument that CF-C120 alone "cannot settle Q3" (CR17:239-241) is right, which is why it is paired with per-step-120
in Stage 2.

### R2. Q2 — what existing data say about loosening the cap
- **The 1,256 are candidate records, not riders.**
  - 971 decisions and 973 request–run pairs; 807 (83%) of those pairs were served anyway, 166 rejected, 148 of them
    on T3.8 C-30 (SF:2,11).
  - On T3.8, 1,186 rejections are structural only (BUD:4-5: 1,075 + 111).
- **The "all feasible" endpoint is U.**
  - The smallest overshoot among the 148 has median 109.6 s and maximum 524.8 s above the 30-s cap (BUD:6). Passing
    the median needs B ≈ 140 s; passing all needs B ≈ 555 s. U's largest per-rider sum is 590.1 s (A:9).
  - U is measured: +96 served, +127 late60 (naive and forecast), −31 timely60 per request, +5 / +9 timely120
    (A:7,9; DIAL17:12-13).
- **The 148 screen counts crossing occurrences, not riders or a joint frontier.** At B = 60 / 120 / 300 s, 11 / 59 /
  135 requests pass. Co-rider occurrences newly late > 60 s: 5 / 51 / 123; > 120 s: 0 / 6 / 79. At 120 s the 59
  occurrences involve 58 distinct blocking rider–run pairs (SF:12,14,18). The screens are marginal and fail-fast
  (R15 row 30), so they cannot be summed into a trajectory. EV:213-216's "about 2,380" timely120 is arithmetic over
  incompatible screens, not an estimate (CX17:83).
- **Calibration.** On w07 at 120 s the screen predicted 6 passes. The run gained 17 and lost 11 (net +6) (IDN:5;
  SF:26). Net counts roughly right, identities wrong.
- **Measured dials.**
  - w07 (8 cells, 07–09 h, 12–13 Nov, causal forecast inactive): C-30 → C-120 gives +6 served, +4 late60, +5
    late120, +2 timely60, +1 timely120. C-120 serves 666 vs U 665 (CAP:3-7). No monotone law.
  - WP14r fixed traffic: C-30 / C-60 / C-120 / LOCKS = 1,534 / 1,540 / 1,563 / 1,584 served; late60 0 / 0 / 23 / 47;
    timely120 1,534 / 1,540 / 1,563 / 1,557 (WP17).
  - Claude's "at most 96 recovered" (RV:493) is WRONG as a bound (CX17:85).
- **Is SF-C120 on 34 cells worth running alone?** Yes, as the cheapest piece of A2, not as a separate project.
  - It is the only way to measure the dial where C-30 loses most: −39 riders at 08–10 h and −52 at 17–19 h, against
    −5 at 07–09 h (T38:50-52).
  - It costs 34 config-only jobs on the archived binary.
  - It cannot establish an optimum. The informative registered test is a3 (an interior timely120 gain).

### R3. Q3 — the precise honest sentence
> **EN.** In 98 enforced-C simulation runs driven by measured city-wide traffic factors (64,371 acknowledged
> decisions), each of the 1,256 recorded drop-budget pruning records shows a single dispatch increment larger than B.
> None needed prior spending to explain the recorded refusal, and no served rider under C had more than one nonzero
> dispatch change. The cumulative clause was therefore never the recorded reason for a refusal. We did not implement
> or run a per-step rule, so we do not claim that trajectories or outcomes would have been identical without
> accumulation. Outside measured traffic, possible cumulative-only records occur in 4 decisions (fixed traffic) and
> 3 decisions (one synthetic world, after removing a duplicate rerun). These are recorded witnesses, not measured
> policy effects.

Anchors: A:3-7,10-17,20; R15:195-197; FP:43-45; R15 row 30 (fail-fast).

Do not say:
- "behaviourally inert" (EV:281);
- "never changed a decision";
- "at most 7 decisions / at most 1 rejection" as a bound (RV:501-503; V:51-61).

### R4. Q4 — what the WP14r fixed-state re-selection shows and does not
**Shows [S, reproduced by both sides].**
- 62,837 / 62,837 recorded selections reproduce (PV:2-7 [A]; WP17).
- Removing the stability levels at frozen states changes the plan in 445 / 1,714 new-request decisions (26.0%)
  under U's gates, but in 104 / 1,715 (6.1%) under C-30's gates.
- Plan-cost saving: 7.79% (U) and 8.00% (C-30) where the choice differs. Per new-request decision: 2.02% / 0.49%.
  Over all acknowledged frames: 0.307% / 0.079% (PV:2,5; WP17:7,21; DER17:15,18).
- Under C-30, the extra plan-summed drop movement is at most 35.5 s. The single > 30 s case is two incumbents ×
  17.77 s; no rider exceeds 30 s (CASE). 12 / 445 and 9 / 104 "differences" are tie-breaks (WP17:7,21).
- **FREE vs LOCKS.** 325 of FREE's 401 promise-changing decisions (81%) are drop-only changes that LOCKS gates
  permit. They carry 33,555 s of 48,509 drop seconds (69%). The other 76 are pre-boarding pickup changes, an upper
  bound (PV:8).
- Reading: the cap restricts what a cost-first selector can change by about 4×, and ranking plausibly explains much
  of FREE's local promise movement.

**Does not show.**
- trajectory outcomes (service, lateness, sharing);
- realised cost: plan cost is counted repeatedly through time;
- transfer to T3.8: fixed traffic, older runner, a different runner config (CR17:168-174; not re-opened by me);
- that 81% of the FREE–LOCKS *outcome* gap is ranking (CX17:67);
- that C-30-cf would raise sharing.

**Prediction [H].** CF-U moves and delays incumbents more; CF-C30 stays close to SF-C30 in reliability. Tested by
H2–H4.

### R5. Q5 — the incident-forecast direction
**What the snow replay shows** [S; retrospective; 8 cells, 601 served riders; first-quote replay only, no dispatch
change]:
- **Late60 counts:**
  - HIST (current profile): 34;
  - strict in-window blend: **21**;
  - morning-prefix blend, which the regime gate also selects: **19**. It uses same-day bins from 06:00 that the
    14/15 h windows never delivered, and threshold 1.3 was chosen after seeing 1.244 / 1.323 (FC:142; FS2:219-223);
  - lagged blend BLEND-L1: **29**. Its anchor still uses the exact current snapshot, so it is not a full
    realistic-latency test (CX17:101; RP1 has no regime-gate-with-lag row);
  - equal-cost uniform pad: 27 (RP1:7-20; SF:28).
- **Damped trend.** The Round-12 damped-trend fit gives α = 1, β = 0, φ = 0.8 and equals HIST (SF:27; FS1:2).
  Withdraw it as a promising test.
- **Denominators.** 34 / 601 = 5.66% pooled. The reported 5.94% / 7.19% are cell means (RP1:6-8 "cell means").
- **Ledger** (41 naive-late riders, 3,445.9 s): dispatch 8.6 s; HIST explains 251.5 s; the prefix blend explains
  886.9 s more (25.7%); 2,299.0 s (66.7%) stay unexplained (SF:29 [A]).
- **Corrected wording.** "This retrospective prefix model explains about 26% more of the naive-late cohort's late
  seconds; about two-thirds remain unexplained by the methods tried." Never write "67% unknowable" (FC:41 is WRONG as
  an interpretation; CX17:97).
- **The owner's 2013 idea.**
  - Fielbaum & Alonso-Mora used 15/01/2013, 13–15 h (plus ten weekdays from 14/01/2013), chosen because "traveling
    times are somewhat stable, which allows us to disregard unreliability due to traffic conditions" (FAM:571-576).
    That subset is the wrong sample for incident forecasting.
  - The full 2013 TLC year is a separate question. It is about 2.14 GB compressed (SF:31). The current official files
    carry zone IDs, not coordinates (META:2-3; PQ:1-2). It contains 2 weekdays with ≥ 3 in of snow (8 Feb, 8 Mar
    2013; NOAA13:4).
  - It is usable only as an extra-history ablation, with an explicit year effect: yellow trips/day were 479,527 in
    Nov 2013 vs 271,501 in Nov 2018 (TLC:860,556). "Ride-hail rose from 0" (FC:70) is unsupported; only the 2018
    FHV-HV figure 691,379 is in the table (TLC:552).
- **Fair design** (Codex's, which I adopt):
  - rebuild the Syed-style factor target and validate it on 12–18 Nov 2018;
  - build causal observations from trips with dropoff + declared delivery lag ≤ t;
  - chronological fit / calibration / test, excluding the inspected bundle week from confirmatory scores;
  - strong same-data calendar and persistence baselines, a damped residual and one frozen regime / analog candidate;
  - quote-cost budgets fixed on calibration;
  - event-block uncertainty;
  - 2013 as an ablation (CX16 Q5; CX17:194).
- **Effort: 80–140 h** (Codex; Claude conceded, CR17:297-300,397). Claude's 35–50 h is the happy path of a leakier
  L = 1 design (CR17:285-289).
- **Unresolved design point:** event count (§E, row 6).

### R6. Prior work
- **HZ eq. 7 is decisive prior work for the traffic-updated reference and the never-undefined motivation.**
  - "To overcome the issue of undefined system states" (HZ:507).
  - "not dropped off later than what is the absolute minimum, given current traffic conditions" (HZ:537-539).
  - Required drop-off = max(updated, latest) for requests on the evaluated vehicle (HZ:567-569).
  - Substituting a first-offer deadline gives p ≤ max(p0 + B, e). The do-nothing plan (p = e) always passes [I].
- **"Hard gate vs penalty" is not a valid distinguishing claim.** HZ routes under hard constraints on the relaxed
  required times (eqs. 9–10) and adds penalties only for violating the original times (eq. 11) (HZ:575-588). Codex
  is right; RV:157(b) is WRONG.
- **The valid distinction** is what is bounded: a traffic-independent dispatch allowance B for every rider, absolute
  and cumulative over the trip, with a per-rider ledger. This matches the handoff's note "chỉ áp cho khách sắp vi
  phạm, không cộng dồn, không có sổ" (HO:145-147). Its cumulative part was never exercised on measured traffic.
- **Recovery (b) was already enabled in T3.8.** "recovery rule (b) for every arm" (RUN38:9); `"commitmentRecovery":
  "no-worse-than-reference-v1"` (WP4:7). 154 forcedNoWorse entries across the 34 M⁺-30 terminal checkpoints
  (META:8). My spot check reproduces 11 / 17 / 0 on three cells (SPOT = META:9,21,11).
- So M⁺-30 on T3.8 *is* M⁺(b), and it serves 2,338 = C-30. RV's candidate 2 "add M⁺(b) on T3.8" (RV:386-395) is
  redundant (WRONG premise).
- The 21/22 table (TEX/08-chuong4.tex:1361-1362: (b) 1,874, (a) 1,864, C 1,873) is from the tier-3 sweep (6
  synthetic + 2 measured cells, TEX/08:1340-1350), not from T3.8.

---

## B. Confirmation table (every number, quote and code fact used above)

| # | Fact | Anchor | Status |
|---|---|---|---|
| **Thesis text** | | | |
| 1 | LaTeX last built 30 Sep 2026 (main.pdf 04:19; 02/05/08/09 dated 30 Sep) | `ls -la` of TEX and `ridebound/` | VERIFIED |
| 2 | No Hörl / Zwick citation; 27 bibitems | TEX/10-tai-lieu.tex:7-162; META:4,6 | VERIFIED |
| 3 | No T3.8 number (2338 variants) in any of 11 TEX files | my grep | VERIFIED |
| 4 | "core departure … decomposed by cause" | TEX/02:66-69 (VN :17-20) | VERIFIED |
| 5 | "only the conduct cap is never the cause of an empty choice set" | TEX/02:71-75 (:22-26); 05:169-171,174-182; 09:18-22,224-231; 08:20 | VERIFIED |
| 6 | "accumulates monotonically" ledger as mechanism | TEX/02:64-65 (:14-16); 05:202-204,213-217 | VERIFIED |
| 7 | "không ai tách phần do nhà điều hành … khỏi … đường tắc" | TEX/05:64-69 | VERIFIED |
| 8 | Theorem by construction: A = \|e − e\| = 0 | TEX/07:292-297 | VERIFIED |
| 9 | Recovery (b) 1,874 / (a) 1,864 / C 1,873; 21/22 equal; 19/22 same actions; sweep cells (6 synthetic + 2 measured) | TEX/08:1340-1350,1361-1362 | VERIFIED |
| 10 | Welfare rows use a value "chưa đối chiếu được với bản gốc" | TEX/08:1852-1857 | VERIFIED |
| 11 | "phản ánh đúng tác động của cam kết" | TEX/08:1894-1897 | VERIFIED |
| 12 | Keywords "quy trách nguyên nhân" / "causal attribution" | TEX/02:46-47,97-98 | VERIFIED |
| 13 | "Trần hành vi, theo cấu tạo, giữ mọi lời hứa của nó" | TEX/02:43,94 | VERIFIED |
| 14 | "điểm mới nằm ở chỗ mốc tham chiếu ngoại sinh tính được …" | TEX/09:30-32 | VERIFIED |
| 15 | "thí nghiệm có tiền đăng ký … xác nhận nó" | TEX/09:226-231 | VERIFIED |
| **Code and configuration** | | | |
| 16 | T3.8 every arm uses recovery (b) | RUN38:9; WP4:7 | VERIFIED |
| 17 | 154 forcedNoWorse entries in 34 M⁺-30 terminal checkpoints | META:8 (Codex); SPOT 11 / 17 / 0 = META:9,21,11 | VERIFIED (3/34 spot-checked) |
| 18 | U vs C-30 differ only by `"hardLimit": 30000`; sha 998a0a94 / d6124f3f; C-120 sha ac0f9758 | `diff`, `sha256sum` of tang3/configs | VERIFIED |
| 19 | Selector order: forced (HardVector / SoftHardHybrid only) → accepted → worst utilisation + revisions (HardVector with a hard limit) → operational cost → id rank | SEL:271-303,319-331,365-385 | VERIFIED |
| 20 | Policy default profile RollingCost; RideBoundHardVector runs AssessAndFilter | POL:287,322-330 | VERIFIED |
| 21 | Fixed-freeze strips hard limits | R15 rows 41-42 | UNCONFIRMED by me (Codex-checked) |
| 22 | Utilisation level saturated 3,503/3,503 (U), 3,506/3,506 (C-30) | A:7,9 | VERIFIED |
| 23 | Archived runner and 49 fixtures / drivers exist | `ls` runner-tier3-v2, fixtures-panelA-v1, panelA/drivers | VERIFIED |
| 24 | Binary drift: core 1ce15e9 vs later src commit 45f8026 | R15 rows 38-40 | UNCONFIRMED by me |
| 25 | Validator is fail-fast under the default evidence profile | R15 row 30 | UNCONFIRMED by me (Codex-checked) |
| **T3.8 outcomes** | | | |
| 26 | Served U 2,434 / C-30 2,338 / M⁺-30 2,338 / M⁺-60 2,347 / V-30 2,336 | A:7-9; T38:46 | VERIFIED |
| 27 | Late60 naive 203 / 76; forecast 137 / 10 (M⁺ 10) | A:7-9; DIAL17:12-13 | VERIFIED |
| 28 | Timely60 naive 2,231 / 2,262, forecast 2,297 / 2,328; timely120 naive 2,332 / 2,327, forecast 2,347 / 2,338 | DIAL17:12-13 | VERIFIED |
| 29 | Padded U +30: late60 106, timely60 2,328, timely120 2,366, ext 37.2 s, early60 44 (1.81%) | A:9 (fc_pad30) [A] | VERIFIED |
| 30 | C-30 + forecast ext 7.4 s, early60 4 (0.17%) | A:7 [A] | VERIFIED |
| 31 | Served sets C/M⁺ 2,332 common, 6 / 6; U/C 2,207, 227 / 131 | A:18-19 | VERIFIED |
| 32 | Shared U 22.8% / C-30 13.4% / M⁺-30 13.1% (≈555 / 313 absolute) | SHARE:2-4 [A] | VERIFIED |
| 33 | Late riders also dispatch-exposed: 134/203 (U), 4/76 (C-30); exposed U riders 77.01% late60 | EXP:2-3 | VERIFIED |
| 34 | Service gap by window −39 / −52 / −5 | T38:50-52 | VERIFIED |
| 35 | M⁺-30 forced 41.3%, self-broken 14.5% (cell means); 30/34 identical action sequences with C-30 | T38:58-59,64 | VERIFIED |
| 36 | U > C-30 late60 in 25/25 w08/w17 cells | DER17:8,11 | VERIFIED |
| 37 | U: 174 exposed, 12 repeated, max S 590.1 s; C-30: 33, 0, 29.2 s | A:7,9; DIAL17:12-13 | VERIFIED |
| **Cumulative clause** | | | |
| 38 | 98 measured C runs; 64,371 decisions; 1,256 = 845 + 411 records, all step-fails; 0 cumulative-only | A:7,10-17 [A] | VERIFIED |
| 39 | Fixed traffic: C-60 2 records / 1 decision, C-120 4 / 3; none finally rejected | A:3,5 | VERIFIED |
| 40 | Synthetic C-120: 6 / 5 incl. a duplicate; 4 / 3 after dedup; one final rejection | A:6,20; R15:195 | VERIFIED |
| 41 | No C rider on measured traffic with two nonzero dispatch changes | A:7,10-17 ("repeated": 0) | VERIFIED |
| 42 | Cumulative-only at 120 s: T3.8 U 4/2,434; FREE 13/1,629; WP9 A 12/1,735; WP9 B 10/966; FREE 2 at 30 s | CVP:5,7,17,22,32 | VERIFIED |
| **Cap dials and screens** | | | |
| 43 | w07 dial (C-30 … C-300, U): served / late60 / late120 / timely60 / timely120 | CAP:3-11; DIAL17:3-11 | VERIFIED |
| 44 | Causal forecast inactive on w07 (12–13 Nov) | CAP:2; DIAL17 "active 0" | VERIFIED |
| 45 | WP14r ladder FREE / LOCKS / C-120 / C-60 / C-30: served 1,629 / 1,584 / 1,563 / 1,540 / 1,534; late60 274 / 47 / 23 / 0 / 0; timely120 1,465 / 1,557 / 1,563 / 1,540 / 1,534 | WP17:2,5,9,14,19 | VERIFIED |
| 46 | 971 decisions, 973 pairs, 807 served, 166 rejected; T3.8 643 / 495 / 148 | SF:2,11 | VERIFIED |
| 47 | 148 budget-blocked (116 U-served); structural 1,186; overshoot median 109.6, p25 63.7, p75 183.6, max 524.8; pass 11 / 59 / 135 | BUD:2-9 | VERIFIED |
| 48 | Co-rider crossings late60 5 / 51 / 123, late120 0 / 6 / 79; 58 distinct pairs at 120 s | SF:12,14,18 | VERIFIED (as occurrences) |
| 49 | w07 at 120 s: 6 screen-pass, 17 gained, 11 lost, net +6 | IDN:5; SF:26 | VERIFIED |
| **Cost-first re-selection** | | | |
| 50 | 62,837 / 62,837 reproduced (12,663 + 12,525 + 12,364 + 12,325 + 12,960) | PV:2-7 [A] | VERIFIED |
| 51 | 445 / 1,714 = 26.0%; 104 / 1,715 = 6.1%; 0 accepted-count changes | PV:2,5 | VERIFIED |
| 52 | Saving 7.79% / 8.00% conditional; 2.02% / 0.49% per new-request decision; 0.307% / 0.079% over all frames | PV:2,5; WP17:7,21; DER17:15,18 | VERIFIED |
| 53 | Extra plan-summed drop movement median 90.8 s (U), 12.5 s (C-30), max 35.5 s; case = 2 × 17.77 s | PV:2,5,7; CASE | VERIFIED |
| 54 | FREE GATE 76 / RANK 325 / NONE 12,559; 33,555.4 of 48,508.9 drop s | PV:8 [A] | VERIFIED |
| 55 | WP14r commitment configs byte-identical to T3.8's; runner config and core differ | CR17:158-174 | UNCONFIRMED by me |
| 56 | WP14r elapsed medians 730 / 667 / 641 s | EL17:2-6 | VERIFIED |
| 57 | 170 jobs ≈ 7 h at 6 parallel (≈15 min/job) | RUNTIME:24-25 | VERIFIED |
| **Forecast and data** | | | |
| 58 | Snow late60 NAIVE 41, HIST 34, BLEND-in 21, BLEND-pre = REGB-1.3 19, BLEND-L1 29, PAD@REGB 27 | RP1:7-20; SF:28 | VERIFIED |
| 59 | 5.94% / 7.19% are cell means; 34/601 = 5.66% | RP1:6-8 [A] | VERIFIED |
| 60 | Ledger 3,445.9 s; dispatch 8.6; HIST 251.5; prefix 1,138.4 (+886.9 = 25.7%); residual 2,299.0 (66.7%) | SF:29 [A] | VERIFIED |
| 61 | Damped-trend fit (1.0, 0.0, 0.8), 80 targets | SF:27; FS1:2 | VERIFIED |
| 62 | Gate statistic: snow min 1.323, weekday max 1.244 | FS2:219-223 | VERIFIED |
| 63 | Weekday forecast-late 2 / 1,471 | RP1:39-40 | VERIFIED |
| 64 | Snow naive late120 0.69% (cell mean) | SNOW:10; family_snow.py:37 | VERIFIED |
| 65 | First Central Park SN report 13:44 on 15 Nov (saved file) | SF:30 | VERIFIED (not city-wide onset) |
| 66 | Test split Sep 2018–Dec 2019: 1 + 4 = 5 snow spells (≥ 25.4 mm), one is 15 Nov | WX:6-7; WX17:4-5 | VERIFIED |
| 67 | Official 2013 parquet: PULocationID / DOLocationID, no lat/lon; 14,776,617 / 14,388,451 rows | META:2-3; PQ:1-2 | VERIFIED |
| 68 | Sizes: 2016-07..2020-02 = 5.354 GB; 2013 = 2.144 GB | SIZE:2; SF:31 | VERIFIED |
| 69 | Yellow trips/day 479,527 (2013-11) vs 271,501 (2018-11); FHV-HV 691,379 (2018-11) | TLC:860,556,552 | VERIFIED |
| 70 | 2013: 6 weekdays ≥ 1 in snow, 2 ≥ 3 in (8 Feb, 8 Mar); FA window Mon–Thu without snow | NOAA13:4-6 | VERIFIED |
| 71 | FA: 4,091 nodes / 9,453 edges; 15/01/2013 13–15 h; ten weekdays; "disregard unreliability due to traffic conditions"; 19,610 requests | FAM:571-584 | VERIFIED |
| 72 | TLC publishes monthly with ~two-month delay | CX17:101 (web) | UNCONFIRMED |
| 73 | Donovan & Work, Cetin & Comert, Gardner & McKenzie contents | FC §2; CX17:113 | UNCONFIRMED by me (not load-bearing) |
| **Prior work and boundary** | | | |
| 74 | HZ eq. 7 max(updated, latest); "absolute minimum, given current traffic"; "undefined system states" | HZ:507,537-539,567-569 | VERIFIED |
| 75 | HZ hard routing constraints on required times (9–10) + violation penalty (11) | HZ:575-588 | VERIFIED |
| 76 | S&P slack 900 s; Elmi per-rider guarantees not novel | D03:211-217 | VERIFIED |
| 77 | Not novel: detection, pre-decision control, service–stability trade-off | D03:56 | VERIFIED |
| 78 | No satisfaction / revenue claims; value unconfirmed | D03:236-245 | VERIFIED |
| 79 | Handoff lists HZ-B as the close mechanism and requires citing it | HO:145-147,396 | VERIFIED |
| **Debate positions** | | | |
| 80 | Codex R15: 74 jobs minimum; A3 not alongside A2 | R15:349,335 | VERIFIED |
| 81 | Codex R17: rewrite first; 178 jobs, 70–110 h | CX17:153-188,211 | VERIFIED |
| 82 | Claude R17: 2×2 first (74 jobs, 30–50 h); SF-C120 34; A1 mandatory | CR17:314-386 | VERIFIED |
| 83 | Claude R16 referee: A1+ first, 0 runs | RV:524-538 | VERIFIED |
| 84 | Antigravity: no R16 output (folder has only the brief and inputs) | `ls antigravity-work` | VERIFIED |
| 85 | Deadline mid-November 2026 | HO:494 ("cần xác nhận") | UNCONFIRMED |
| **Statements found WRONG** | | | |
| 86 | "≤ 35.5 s" read as a per-rider push | EV:27 vs CASE | WRONG (plan-summed over 2 riders) |
| 87 | "−7.8% plan cost" without conditioning | EV:27 vs PV:2 | WRONG as stated (conditional; 0.31% overall) |
| 88 | "(b)+(c) not knowable … about 67%" | FC:41-42 | WRONG interpretation (method-dependent residual) |
| 89 | "34 → 19 … one-bin latency 34 → 29" as delivered-information results | FC:43-51 | WRONG labels (19 uses an undelivered prefix and a post-hoc gate; strict = 21; L1 anchor exact) |
| 90 | "whole headroom sits in the 60–120 s band" | FC:35 | WRONG as general (one replay; 0.69% > 120 s) |
| 91 | "ride-hail rose from 0" | FC:70 | UNSUPPORTED |
| 92 | "(b) a hard gate rather than a penalty" as a distinction from HZ | RV:157 | WRONG (HZ:575-588) |
| 93 | T3.8 M⁺ uses keep-route recovery; M⁺(b) missing on T3.8 | RV:184-186,386-395 | WRONG (RUN38:9; WP4:7; META:8; SPOT) |
| 94 | "wins back at most the 96-rider gap" | RV:493 | WRONG as a bound (CAP:3,7: C-120 666 > U 665) |
| 95 | "at most 7 decisions … at most 1 final rejection"; "behaviourally inert" | RV:501-503; EV:281 | WRONG as bounds / overstated |
| 96 | "about 2,380 timely120" | EV:213-216 | Not an estimate (incompatible screens) |
| 97 | "a per-step cap … would have admitted exactly the same candidates" | V:56 | WRONG as stated (R15 correction 1) |

---

## C. Trả lời chủ nghiên cứu (tiếng Việt, ngắn gọn)

**Tóm lại trong một câu:** giữ hướng; việc tiếp theo duy nhất là viết lại luận văn cho đúng (không chạy thêm); sau đó,
nếu hạn nộp cho phép, làm đúng một thí nghiệm: đổi bộ chọn sang "ưu tiên chi phí" nhưng giữ nguyên trần.

### Câu 1. "Thật sự không còn hướng mới, không còn chỗ nào để tối ưu? Vì sao vẫn giữ hướng này?"

- Vẫn còn chỗ để tối ưu, chúng tôi không nói là hết. Có ba câu hỏi chưa thử:
  - đổi bộ chọn sang ưu tiên chi phí nhưng giữ nguyên trần;
  - nới trần trên bộ 34 ô chính;
  - dự báo tốt hơn cho ngày có sự kiện bất ngờ.
- Nhưng chưa cái nào đã được chứng minh là tốt hơn. Cũng không cái nào làm phần "mới" của luận văn lớn hơn so với
  các bài báo đã có.
- Giữ hướng vì phần lõi đã vững. Luật C, sổ cái và dự báo đã chạy xong. Hai bên tính lại độc lập và khớp đến từng
  khách.
- Chỗ yếu nhất hiện nay là bản luận văn đang nói quá. Ví dụ, phần tóm tắt viết "khác biệt cốt lõi so với văn liệu là
  độ dời được phân rã theo nguyên nhân". Nhưng Hörl và Zwick (2022) đã dùng giờ trả cập nhật theo tắc đường làm mốc,
  và luận văn chưa trích bài này.
- Ví dụ số. Không có trần, nhưng có dự báo và hứa dài thêm 30 giây, thì cũng có 2.328 lượt đến không trễ quá 1 phút
  trên 3.672 yêu cầu, đúng bằng luật C có dự báo.
  - Vì vậy không được viết "luật C cho nhiều khách đúng giờ hơn".
  - Luật C chỉ hơn ở chỗ lời hứa sát hơn (dài thêm 7,4 giây thay vì 37,2 giây) và ít khách tới sớm hơn (0,17% so
    với 1,81%).
- Câu hỏi khó nhất mà người phản biện sẽ hỏi là: "độ tin cậy đến từ trần, hay từ bộ chọn vốn đã thận trọng?". Đó là
  lý do thí nghiệm tùy chọn nên là thí nghiệm ưu tiên chi phí.

### Câu 2. "Nếu nới trần để 1.256 phương án bị chặn thành hợp lệ ngay từ lần đầu thì có tốt hơn không?"

- 1.256 không phải là 1.256 khách. Đó là 1.256 phương án bị loại, nằm trong 971 quyết định. Trong 973 cặp khách–lần
  chạy liên quan, 807 cặp (83%) vẫn được chở bằng một phương án khác.
- Trên 34 ô chính, số khách thật sự bị từ chối vì trần là 148.
- Muốn cho cả 148 khách này qua, trần phải lên khoảng 555 giây. Lúc đó gần như không còn trần.
- Bản không trần đã chạy rồi:
  - chở thêm 96 khách;
  - nhưng thêm 127 khách trễ quá 1 phút;
  - và số lượt đến không trễ quá 1 phút giảm 31.
- Nới vừa phải thì sao?
  - Ở 8 ô buổi sáng, trần 120 giây chở 666 khách thay vì 660, và có thêm 4 khách trễ quá 1 phút.
  - Ở 16 ô có tắc đường cố định, trần 120 giây chở thêm 29 khách và có thêm 23 khách trễ quá 1 phút.
- Phép sàng lọc 148 khách cho thấy: với trần 120 giây, 59 khách có thể qua, nhưng có 51 lần một khách đang đi cùng
  bị đẩy trễ quá 1 phút. Đây là số lần chứ không phải số người, và không cộng dồn được thành một kết quả chạy thật.
- Kết luận: nới trần chỉ "tốt hơn" khi ta chấp nhận trễ khoảng 2 phút. Ở mức 1 phút, gần như cứ thêm một khách thì
  có thêm một khách trễ.
- Chạy trần 120 giây trên 34 ô (34 lần chạy, không sửa mã) là đáng làm nếu còn thời gian.
  - Lý do: 34 ô này là nơi trần làm mất nhiều khách nhất (−39 khách ở khung 8–10 giờ, −52 khách ở khung 17–19 giờ).
  - Nhưng kết quả chỉ thêm một điểm trên đường đánh đổi, không phải "mức trần tốt nhất".

### Câu 3. "Phần cộng dồn chỉ tác dụng ở 7 quyết định. Vậy phần cộng dồn của hệ thống không có tác dụng?"

- Trên tắc đường đo thật, đúng là chưa lần nào nó là lý do từ chối.
  - Cả 1.256 lần chặn đều do một lần dời đã vượt trần 30 giây ngay.
  - Dưới luật C, không khách nào bị điều phối dời giờ trả hai lần.
- Con số 7 (4 quyết định ở tắc đường cố định, 3 ở một thế giới giả lập) chỉ là số lần được ghi lại. Nó không phải
  giới hạn trên của tác dụng.
- Điều chưa đo: nếu thay bằng luật "mỗi lần dời không quá 30 giây" thì kết quả có giống hệt không. Chưa chạy, nên
  không được viết "giống hệt", cũng không được viết "vô dụng".
- Phần cộng dồn vẫn có nghĩa về định nghĩa. Luật "mỗi lần ≤ 30 giây" vẫn cho phép một khách bị dời ba lần, tổng 90
  giây.
- Ví dụ thật: ở bản không trần, 12 khách bị điều phối dời từ hai lần trở lên, và có khách bị dời tổng cộng 590 giây.
- Câu nên viết trong luận văn:

  > Trong 98 lần chạy mô phỏng có áp luật C với hệ số tắc đường lấy từ dữ liệu đo (64.371 quyết định), cả 1.256 bản
  > ghi chặn do ngân sách giờ trả đều có một lần dời do điều phối đã vượt B. Không bản ghi nào cần đến phần ngân sách
  > đã dùng trước đó, và dưới luật C không khách nào bị điều phối dời giờ trả quá một lần. Vì vậy phần cộng dồn chưa
  > từng là lý do từ chối được ghi nhận. Chúng tôi chưa cài đặt và chưa chạy luật "mỗi lần một trần", nên không khẳng
  > định rằng bỏ phần cộng dồn thì quỹ đạo và kết quả sẽ giống hệt. Ngoài tắc đường đo, các bản ghi có thể chỉ do cộng
  > dồn xuất hiện ở 4 quyết định (tắc đường cố định) và 3 quyết định (một thế giới giả lập). Đó là dấu vết được ghi
  > lại, không phải tác dụng đã đo của chính sách.

### Câu 4. "Nếu đổi bộ chọn sang ưu tiên chi phí thì kết quả có khác không?"

- Sẽ khác một phần, nhưng chưa biết khác bao nhiêu, vì chưa chạy.
- Chúng tôi tính lại trên các quyết định đã ghi của 16 ô có tắc đường cố định. Nếu bỏ hai tầng "ưu tiên ổn định",
  bộ chọn đổi lựa chọn ở:
  - 26,0% quyết định có khách mới khi không có trần;
  - chỉ 6,1% khi có trần 30 giây.
- Tiết kiệm chi phí ở những quyết định bị đổi khoảng 8%. Nhưng tính trên tất cả quyết định thì chỉ còn 0,31% (không
  trần) và 0,08% (trần 30 giây). Đây là chi phí kế hoạch của bộ giải, không phải tiền xăng hay lợi nhuận.
- Nghĩa là trần đã tự chặn phần lớn những gì bộ chọn ưu tiên chi phí muốn đổi. Đó là dấu hiệu tốt cho luật C.
- Nhưng đây mới là phép tính trên một quyết định đứng yên. Khi chạy thật, các quyết định sau sẽ khác đi.
- Muốn biết chắc thì phải chạy thí nghiệm 2×2: {ưu tiên ổn định, ưu tiên chi phí} × {không trần, trần 30 giây}.
  - Hai ô "ưu tiên ổn định" đã có sẵn.
  - Cần 68 lần chạy mới, cộng 6 lần kiểm tra.
- Dự đoán của chúng tôi:
  - không trần + ưu tiên chi phí sẽ dời giờ trả nhiều hơn và trễ nhiều hơn rõ;
  - có trần 30 giây thì độ tin cậy gần như giữ nguyên.
  - Nếu đúng như vậy, luận văn có một kết quả thật về cơ chế: chính trần, chứ không phải bộ chọn thận trọng, giữ lời
    hứa.

### Câu 5. "Hướng tốt hơn có phải là tối ưu ngày có sự kiện bất ngờ? Làm thế nào, công bằng ra sao, có dùng được dữ liệu 2013 mà hệ thống của Alonso-Mora đã dùng không?"

- Đây là một hướng nghiên cứu thật, nhưng không nên làm trước hạn nộp.
- **Lý do thứ nhất.** Trên buổi chiều tuyết 15/11/2018, phần trễ do điều phối chỉ là 9 giây trong tổng 3.446 giây
  trễ. Dự báo tốt hơn không thay đổi kết luận nào về luật C.
- **Lý do thứ hai.** Thử lại trên dữ liệu đã có, một cách dự báo "nhận ra hôm nay bất thường" giảm số khách trễ quá 1
  phút từ 34 xuống 21. Cách này chỉ dùng dữ liệu trong khung giờ đang chạy.
  - Con số 19 thì phải dùng thêm dữ liệu buổi sáng mà hệ thống không được thấy, và một ngưỡng chọn sau khi đã xem kết
    quả.
  - Khi tính một phần độ trễ của dữ liệu, chỉ còn giảm xuống 29.
  - Tất cả chỉ là một buổi chiều, và đã xem trước.
- **Lý do thứ ba.** Các thành phần (xu hướng giảm dần, chuyển chế độ khi bất thường, thêm thời tiết) đều đã có trong
  văn liệu. Cách "xu hướng giảm dần" theo giao thức vòng 12, khi khớp trên dữ liệu, tự quay về đúng cách dự báo hiện
  tại; chạy nó sẽ ra kết quả bằng không.
- **Cách nói đúng.** Không được viết "67% không thể biết trước". Chỉ được viết: "cách dự báo đã thử giải thích thêm
  khoảng 26% số giây trễ; khoảng hai phần ba còn lại chưa giải thích được bằng các cách đã thử".
- **Làm công bằng thì cần:**
  - dựng lại hệ số tắc đường 15 phút từ chuyến taxi nhiều năm, theo đúng công thức của Syed và cộng sự, rồi kiểm
    rằng nó khớp tuần 12–18/11/2018;
  - học trên các năm trước, thử trên các năm sau;
  - lúc hứa chỉ được dùng những chuyến đã kết thúc và đã gửi về;
  - so với một dự báo lịch sử mạnh, ở cùng độ dài lời hứa;
  - tính độ bất định theo từng sự kiện, không theo từng khách;
  - không chấm điểm trên tuần 12–18/11/2018 đã xem.
  - Công sức khoảng 80–140 giờ.
- **Một khó khăn.** Giai đoạn thử 9/2018–12/2019 chỉ có 5 đợt tuyết từ 1 inch trở lên, và một đợt là chính ngày 15/11
  đã xem.
- **Dữ liệu 2013.**
  - Bộ Fielbaum và Alonso-Mora dùng là 13–15 giờ ngày 15/1/2013. Họ chọn khung này chính vì "thời gian đi khá ổn
    định", để bỏ qua tắc đường. Nên bộ đó không giúp gì cho ngày bất thường.
  - Cả năm 2013 thì có thể dùng làm dữ liệu học thêm: khoảng 2,14 GB nén, có 2 ngày thường tuyết dày từ 3 inch
    (8/2 và 8/3/2013).
  - Nhưng tệp chính thức hiện nay chỉ có mã vùng, không có tọa độ.
  - Thành phố cũng đã đổi nhiều: taxi vàng 479.527 chuyến/ngày (11/2013) so với 271.501 (11/2018).
  - Nên chỉ dùng 2013 như một phép thử thêm. Nếu thêm 2013 mà dự báo trên các năm sau không tốt hơn thì bỏ.

### Đánh giá theo phản biện khó tính về lõi luận văn hiện tại

- **Gửi tạp chí hàng đầu (như TR Part C): từ chối.**
  - Phần mới hẹp so với Hörl và Zwick 2022, Fielbaum và Alonso-Mora 2020, Schulz và Pfeiffer 2026.
  - Phần cộng dồn chưa từng là lý do từ chối trên tắc đường đo.
  - Luật C không hơn luật hạn chót về số khách hay số lượt đúng giờ (2.338 = 2.338; 2.328 = 2.328).
  - Mô phỏng nhỏ: 8 xe, 108 yêu cầu mỗi ô, 96 điểm, một hệ số tắc đường cho cả thành phố, 5 ngày.
- **Hội nghị (như ITSC): ở ranh giới**, nếu viết thành một ghi chú thực nghiệm trung thực.
- **Khóa luận đại học: bảo vệ được nếu viết lại lớn.** Điều này còn phụ thuộc yêu cầu của hội đồng, chưa xác nhận.
- **Điểm mạnh thật:** số liệu kiểm lại được, kế hoạch được niêm phong, hai bên tính lại độc lập đều khớp.
- **Muốn đăng được, cần:**
  1. đặt đúng vị trí so với Hörl và Zwick, nói rõ khác ở đâu và không nói "duy nhất";
  2. một kết quả cơ chế không hiển nhiên (thí nghiệm 2×2 là ứng viên tốt nhất);
  3. nhiều ngày và sự kiện độc lập hơn, tải cao hơn hoặc mạng đường thật;
  4. so cùng một chuẩn đúng giờ cho mọi luật, có khoảng tin cậy;
  5. bằng chứng rằng một nhà vận hành thật cần đúng loại trần này.

---

## D. Overclaims to remove (current LaTeX first, then debate wording)

Thesis files: TEX = `E:/Code/Report_INT3508/ridebound/noi-dung/` (read only; edits are for the owner).

| # | Location | Current claim (short) | Problem (anchor) | Corrected wording |
|---|---|---|---|---|
| D1 | 02:6-10, 56-59; 09:5-7 | "mọi thước đo chuẩn … đều không ghi nhận" | FA measure and control revisions per rider (D03:54-56) | "Các hàm mục tiêu điều phối theo thông lượng không định giá việc sửa lời hứa; Fielbaum và Alonso-Mora (2020) đã đo và kiểm soát hiện tượng này." |
| D2 | 02:17-20, 66-69 | "Khác biệt cốt lõi so với văn liệu là … phân rã theo nguyên nhân" | HZ eq. 7 uses the traffic-updated reference (HZ:529-541,567-569); not cited | "Tiếp nối mốc giờ trả cập nhật theo tắc đường của Hörl và Zwick (2022, chiến lược B), khóa luận chỉ tính vào sổ phần dời do quyết định điều phối, cho mọi khách cùng một mức cho phép B không phụ thuộc phần tắc đường, cộng dồn trị tuyệt đối qua cả chuyến và kiểm được theo từng khách." |
| D3 | 02:22-26, 71-75; 05:169-171, 174-182; 09:18-22, 224-231; 08:20 | "chỉ ràng buộc theo hành vi không bao giờ là nguyên nhân làm rỗng tập phương án"; "Chỗ khác biệt chứng minh được" | Holds by construction (07:292-297); an HZ-style max(p0+B, e) shares it [I]; on T3.8, M⁺ with no-worse recovery serves the same 2,338 (T38:46; RUN38:9) | Demote to a remark: "Trong bốn họ được so, chỉ luật C không bao giờ tự loại phương án giữ nguyên kế hoạch; điều này đúng theo cấu tạo. Một hạn chót nới theo kiểu Hörl và Zwick (2022) cũng có tính chất này; trên 34 ô đo, luật hạn chót có phục hồi 'không tệ hơn' chở đúng bằng luật C." |
| D4 | 02:14-16, 63-66; 05:202-204, 213-217 | ledger "cộng dồn và chỉ tăng" as the mechanism; "trần luôn được tôn trọng ở mọi cấu hình — 291 < 300 …" | Cumulative clause never the recorded reason (A:7,10-17); compliance is a correctness check | Add the Q3 sentence (§C, Câu 3). Move "291 < 300 …" to the validation section. |
| D5 | 05:64-69 | "không có quy trách nguyên nhân … không ai tách …" | False: HZ-B (HZ:529-541) | "Ngoài phân loại định tính của Fielbaum và Alonso-Mora, Hörl và Zwick (2022) đã tách phần do tắc đường bằng cách tính lại tuyến cũ theo tốc độ hiện tại; khóa luận dùng một phép chiếu tương tự để tính sổ." |
| D6 | 05:71-73, 75-82 | "Không chỉ số nào trả lời …"; "chưa được chuyển sang lĩnh vực này" | FA §6, Elmi 2026, D03:54-56,211-213 | Delete, or scope to "các chỉ số thông lượng kinh điển". |
| D7 | 05:99-104; 09:215-218 | "về mặt toán học, không thể trở thành ràng buộc" | Strawman: FA §6 already constrains the promise (conceded at 05:106-111) | "Thước đo hai đầu của họ là hậu nghiệm; mục 6 của họ đã ràng buộc trực tiếp lời hứa đón." |
| D8 | 05:267-271; 09:125-128 | "biến một đại lượng trước nay chỉ đo được sau sự việc thành một ràng buộc cưỡng chế được" | Pre-decision control is prior work (D03:56) | "Khóa luận cài đặt và kiểm một dạng kiểm soát trước quyết định, và đo cái giá của nó." |
| D9 | 02:28-30, 78-80; 05:244-248; 08:16-17, 173-178; 09:36-37 | "89,06% … do chính bộ điều phối gây ra" | Static-travel-time panel; model projection, not causal (D03:222-224; 09:104-105) | "Trong phép chiếu mô hình trên panel thời gian đi tĩnh (độ trôi chỉ do trễ thực thi), phần dời gắn với quyết định điều phối chiếm 89,06%." |
| D10 | 02:46-47, 97-98 | Keyword "quy trách nguyên nhân" / "causal attribution" | D03:222-224 | "quy trách theo mô hình" / "model-based attribution" |
| D11 | 02:43, 94; 05:241 | "Trần hành vi, theo cấu tạo, giữ mọi lời hứa của nó" | True by definition; it promises less (it excludes traffic) | "… giữ nghĩa vụ của chính nó theo cấu tạo, vì nghĩa vụ ấy không bao gồm phần do tắc đường; về giờ đến thực tế, luật C và luật hạn chót cho kết quả như nhau trên 34 ô." |
| D12 | 05:250-253 | "trần 30 giây cắt xáo trộn xuống còn 0,17% … giá 7,13 điểm" | A package comparison (locks + budget + fixed pickup, 08:136-138); "0,17%" collides with the forecast metric (D03:267-268) | Say it is the C1 package versus B1; rename the metric; keep −7,13 pp as the package cost. |
| D13 | 05:261-264 | "thước đo hai đầu của họ bỏ sót 49%" | Reads as a flaw; it is by design | "Một thước đo hai đầu không đếm các lần sửa tự triệt tiêu; dưới cam kết, 49% khách bị sửa lời hứa không có thay đổi ở hai đầu." |
| D14 | 09:30-32 | "điểm mới nằm ở chỗ mốc tham chiếu ngoại sinh tính được …" | HZ computes the same reference | Delete "điểm mới"; keep the legal analogy as an interpretation only. |
| D15 | 09:226-231 | "một thí nghiệm có tiền đăng ký trên dữ liệu tắc đường thật xác nhận nó" | Simulation with city-wide factors; exploratory; confirms a by-construction property | "… nhất quán với nó, trong mô phỏng dùng hệ số tắc đường toàn thành phố lấy từ dữ liệu đo (thăm dò)." |
| D16 | 08:1852-1859 (table before it) | Welfare thresholds using an unchecked 20–25 EUR/h value | Source unverified (08:1855-1857); D03:236-245 | Remove the two unverified rows, or move the section to an appendix as illustration with symbolic q/m. |
| D17 | 08:1894-1897 | "chênh lệch … phản ánh đúng tác động của cam kết" | B1 vs C1 differ in locks, budget and pickup fixing (08:128-138) | "… phản ánh tác động của cả gói cam kết, không phải của giới hạn tính toán." |
| D18 | Missing everywhere | T3.8, M⁺(b), forecast, ledger, padded-U frontier, cumulative audit, Q4 screen | No 2338 in TEX (grep) | Add per A1. Lead with "C và luật hạn chót cùng số khách (2.338; 2.332 khách chung)" (equal aggregate service, not the same riders) and the padded-U tie (2.328 = 2.328 at 60 s; 2.366 vs 2.338 at 120 s). |
| D19 | 10-tai-lieu.tex | No Hörl & Zwick 2022 (also Mt-KaRRi, UberX Share per RV:563) | HO:396; D03 §2 | Add it, with the distinction in D2 and D3. |

**Debate wording that must not enter the thesis or the owner's notes.**

| Wrong or overstated | Use instead |
|---|---|
| "≈ 67% not knowable" (FC:41-42) | "about two-thirds unexplained by the methods tried" |
| "26% knowable from delivered snapshots"; "34 → 19 with no weekday cost" (FC:39,43-46) | "strict in-window blend 34 → 21; 19 uses an undelivered morning prefix and a post-hoc threshold" |
| "one-bin latency 34 → 29" as realistic latency (FC:51) | "a lagged-trend sensitivity whose anchor is still the exact current snapshot" |
| "−7.8% plan cost", "≤ 35.5 s push" (EV:27) | "7.8% where the choice changes; 0.31% (U gates) / 0.08% (C-30 gates) over all frames; ≤ 35.5 s summed over riders" |
| "behaviourally inert"; "at most 7 decisions / 1 rejection" (EV:281; RV:501-503) | the Q3 sentence |
| "wins back at most the 96" (RV:493) | "U is one measured endpoint; finite caps need not lie between" |
| "C-30 and M⁺-30 serve the same riders" (RV:254; CX17:125) | "the same number, 2,332 in common, 6 unique each" |
| "hard gate rather than penalty" as novelty (RV:157) | the traffic-independent allowance distinction (R6) |
| "M⁺(b) missing on T3.8" (RV:386-395) | "T3.8 M⁺ already used recovery (b)" |
| "about 2,380 timely120 at B = 120" (EV:213-216) | omit; it is not an estimate |
| "whole headroom in the 60–120 s band" (FC:33-35) | "on this one replay, naive > 120 s is 0.69% (cell mean)" |
| "ride-hail rose from 0" (FC:70) | "FHV-HV 691,379 trips/day in Nov 2018; no 2013 FHV-HV row in the table" |
| "only A2′ can produce a non-definitional result" (RV:111) | "A2′ is the most relevant bounded mechanism test" (CX17:71) |

---

## E. Remaining disagreements and the evidence that would settle them

| # | Disagreement | Claude side | Codex side | My ruling | What settles it |
|---|---|---|---|---|---|
| 1 | Sequencing | 2×2 first (CR17:314) | rewrite first (CX17:153) | **Codex** (§A) | Nothing further needed. Revisit only if the deadline is confirmed to be much later. |
| 2 | Scope | 74 jobs (+34 SF-C120) | 178 jobs incl. CF-C120 + per-step-120 | **Staged**: 108, then 72 if H2 + H7 pass | Stage-1 CF-U exposure count at 120 s (H7) |
| 3 | Primary endpoint | attribution DiD | sharing +10% | **Attribution primary**, sharing key secondary | Stage 1 results; both reported |
| 4 | Can CF-C30 create cumulative-only witnesses? | yes [H] (CR17:242-245) | doubtful; per-step comparison needed | Unknown; low prior at 30 s (CVP: 0–2 per 1,629 at 30 s) | CF-C30 audit counts in Stage 1 |
| 5 | "FREE–LOCKS gap is mostly ranking" | yes (EV:391-396) | local decomposition only (CX17:67) | **Codex**: a mechanism inference, not an outcome decomposition | CF-U vs SF-U trajectories (H2) |
| 6 | Forecast test design | rolling-origin by winter, about 18 heavy-snow test weekdays 2014–2020 (FC:376-377) | chronological 2018-09…2019-12, ≥ 10 proxy spells incl. rain (CX16:281) | Open. Codex's split has only 5 snow spells, one already inspected (WX:6-7); Claude's needs older years and a year effect | A QA'd event inventory: ≥ 10 independent snow spells outside the bundle week under a leak-free as-of rule. Future work |
| 7 | Forecast effort | conceded 80–140 h | 80–140 h | **Codex** | — |
| 8 | Closest baseline | wanted M⁺(b) on T3.8 | already present; literal HZ is distinct | **Codex** (SPOT; RUN38:9) | Only a literal max(p0 + B, e) implementation would add information. Future work |
| 9 | Accumulation wording | "inert" | "never the recorded reason; unrun" | **Codex** | A per-step trajectory arm (Stage 2), on this panel only |
| 10 | Whether the snow headroom is irreducible | "(c) plausibly larger" (FC:242-244) | a hypothesis, not a measurement | **Codex** | Frozen models on independent storms with as-of feeds and archived weather vintages |
| 11 | Deadline, committee standard | UNCONFIRMED | UNCONFIRMED | — | The owner and the supervisor |
| 12 | Significance for operators | unanswered | unanswered | Unanswered | A real operator problem, cost and acceptance threshold (D03:241-245) |

---

## Files

- `claude-work/R17-FINAL-VERDICT.md` (this file; exclusive-created).
- `claude-work/r17-final-judge/spot_check_forced_noworse.py`: read-only helper; one process; no simulation.
- `claude-work/r17-final-judge/spot-check-forced-noworse-2026-10-10.txt`: output, mode "x". Frame SHA-256 checks
  pass; counts 11 / 17 / 0 equal META:9,21,11.
- `claude-work/r17-final-judge/spot-check.stderr.txt`: empty.
