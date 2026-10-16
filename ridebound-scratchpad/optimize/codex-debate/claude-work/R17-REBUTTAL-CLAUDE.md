# R17 — Claude-side rebuttal of Codex R16 (strict-reviewer standard)

2026-10-10. Judged under `ROUND16-REVIEW-STANDARD.md`. I read `ROUND16-FACT-PACK.md`, `codex-work/R16-CODEX.md` in
full, its helper outputs and the script `R16-cap-outcomes-v2.py`, the three Claude R16 files, the Claude
`r16-evidence/` scripts and outputs I needed, `claude-work/R13-FINAL-VERDICT.md` §A2–A3 and
`codex-work/R15-CONFIRM-CODEX.md` §A2. I did **not** open `codex-work/R17-*`. `antigravity-work/R16-ANTIGRAVITY.md`
does not exist (the folder holds only `ANTIGRAVITY-BRIEF.md` and `inputs/`), so there is nothing from Antigravity to
verify.

No simulation, build, install, deletion or edit of an existing file. New files only: this report and
`claude-work/r17-rebuttal/` (5 scripts and their outputs, all opened with mode "x", at most 2 processes).

**Labels.** [M] = measured by my own code on existing transcripts or files; [S] = first-order screen on recorded
states (not a policy result); [I] = inference; [H] = hypothesis/prediction; [O] = reviewer opinion; UNVERIFIED.

**Anchor keys** (relative to `E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/` unless absolute).

| Key | File |
|---|---|
| CX | `codex-work/R16-CODEX.md` |
| CXR15 | `codex-work/R15-CONFIRM-CODEX.md` |
| V | `claude-work/R13-FINAL-VERDICT.md` |
| EV / FC / RV | `claude-work/R16-EVIDENCE-CLAUDE.md` / `R16-FORECAST-CLAUDE.md` / `R16-REVIEWER-CLAUDE.md` |
| DIAL17 | `claude-work/r17-rebuttal/r17-verify-dial-2026-10-10.txt` (`r17_verify_dial.py`) |
| WP17 | `claude-work/r17-rebuttal/r17-wp14r-check-2026-10-10.txt` (`r17_wp14r_check.py`) |
| WX17 | `claude-work/r17-rebuttal/r17-weather-recount-2026-10-10.txt` (`r17_weather_recount.py`) |
| EL17 | `claude-work/r17-rebuttal/r17-wp14r-elapsed-2026-10-10.txt` (`r17_wp14r_elapsed.py`) |
| DER17 | `claude-work/r17-rebuttal/r17-derived-counts-2026-10-10.txt` (`r17_derived_counts.py`; computed only from DIAL17/WP17 JSON) |
| DL | `E:/Code/Report_INT3508/ridebound-scratchpad/optimize/display_layer.py` |
| SEL / POL | `C:/Code/RideBound-noworse/src/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs` / `…/SolverBackedRidePoolingPolicy.cs` |
| CFG | `C:/Code/RideBound-noworse/src/RideBound.Runner/Configuration/Wp4RunnerConfiguration.cs` |
| EVM | `C:/Code/RideBound-noworse/src/RideBound.Runner/Protocol/SolverExecutionEvidenceMapper.cs` |

---

## 0. Bottom line

1. **Every central Codex R16 number I could re-derive is correct** (§1): the w07 dial, the WP14r table, the T3.8
   U-vs-C-30 relaxed endpoint and the "forecast inactive on 12/13 Nov" claim. My reader is independent of both
   Codex's and Claude-R16's readers and hash-matches all 140 transcripts against Codex's file list [M].
2. **There is no numerical disagreement between Codex and the Claude evidence agent on w07.** They report two
   different contrasts on identical counts (C-30→C-120 vs C-30→U). The forecast columns differ only because Codex
   uses the primary causal rule, which is inactive on 12–13 Nov, and Claude used the non-causal loo-no15 sensitivity.
   Codex's column is the admissible one.
3. **The Claude first-order cost-first re-selection reproduces exactly under my own DP** (445 / 325 / 173 / 104 / 0
   differing decisions, 26.0% / 19.0% / 10.1% / 6.1% / 0%). Two parts of the Claude summary wording need
   correcting. (a) "Cost −7.8%" holds only *within* the differing decisions. Averaged over all new-request decisions it
   is −2.0% under U's gates and −0.49% under C-30's gates. (b) "≤ 35.5 s" is a plan-level sum per decision, not a
   push on one rider.
4. **Codex's direction 1 is the right experiment, but 143 (+48) jobs is not the minimum.** The decisive design is
   the 2×2 {stability-first, cost-first} × {U, C-30}: 68 new jobs plus 6 gate jobs = **74**. Codex itself certified that
   number as "the minimum described plan" in R15 (CXR15:349). It also said there that the C-120 dial must not run
   alongside A2 as a default extension (CXR15:335). The new screen shows why the 2×2 is enough: the objective changes
   26.0% of decisions under U's gates, but only 6.1% under C-30's gates.
5. **Codex's direction 2 effort (80–140 h) is more credible than Claude's 35–50 h** for a leakage-safe design (§3).
   But the direction cannot touch rule C: dispatch caused 9 of 3,446 late-seconds on the snow afternoon. So it is
   future work, not an alternative for this deadline.

---

## 1. Verification of Codex R16's central numbers

Reader: `r17_verify_dial.py` (own frame-type sniffing, own ledger walk; forecast via the canonical `display_layer`
library). All 140 transcripts match Codex's `R13-raw-verification.json` on SHA-256, path and completed count
(DIAL17:3-13, "sha_ok 8/8 … 34/34"). WP14r: `r17_wp14r_check.py` (WP17).

### 1.1 w07 cap dial (8 cells, 12–13 Nov, 07–09 h, 864 requests per arm)

| Arm | Codex (CX:80-88) served / late60 / late120 / timely60 | Mine (DIAL17:3-11) | Codex exposed, mean/max S | Mine |
|---|---|---|---|---|
| C-30 | 660 / 47 / 2 / 613 | 660 / 47 / 2 / 613 | 2, 6.0 / 10.0 | 2, 6.0 / 10.0 |
| C-60 | 661 / 47 / 2 / 614 | same | 3, 18.0 / 41.9 | same |
| C-90 | 664 / 50 / 4 / 614 | same | 7, 49.7 / 86.9 | same |
| C-120 / 150 / 180 | 666 / 51 / 7 / 615 | same | 9, 56.2 / 96.7 | same |
| C-240 / 300 / U | 665 / 50 / 9 / 615 | same | 11, 74.7 / 208.2 | same |

**VERIFIED.** C-30→C-120: +6 served, +4 late60, +2 timely60, +5 late120. C-30→U: +5 served, +3 late60, +2 timely60, +7 late120.
Both Codex (CX:90) and Claude (EV:10-11,102-103) are right. They state different endpoints of the same table.

**Forecast on w07.** `causal-no15` is "active only with >= 2 source days … 12/11, 13/11, 17/11, 18/11 inactive"
(DL:11-12), enforced at DL:50-51. My reader finds 0 of 8 active cells, so forecast = naive (DIAL17:3-11,
"active 0"). **Codex CX:76 VERIFIED.** The Claude column uses `loo-no15`, whose sources include *later* days
(DL:13-14, :45-46). My recount reproduces it exactly: C-30 0, C-120 7, U 9 forecast-late60, ext about 21 s,
active 8 (DIAL17:3-11) = EV:84-92. That column is a non-causal sensitivity. Claude labelled it "optimistic" (EV:78-80);
a strict reviewer would not accept it as evidence. **Resolution:** both tables are arithmetically right; only Codex's
forecast column is admissible.

### 1.2 T3.8 relaxed endpoint (34 cells, 3,672 requests)

| | Codex (CX:114-115) | Mine (DIAL17:12-13) |
|---|---|---|
| C-30 served / late60 naive / fc / timely60 naive / fc / timely120 naive / fc / ext | 2338 / 76 / 10 / 2262 / 2328 / 2327 / 2338 / 7.4 s | identical |
| U same | 2434 / 203 / 137 / 2231 / 2297 / 2332 / 2347 / 7.2 s | identical |
| exposed / repeated / max S: C-30, U | 33 / 0 / 29.2 s; 174 / 12 / 590.1 s | identical |

**VERIFIED** [M]. U vs C-30: +96 served, +127 late60 both naive and with forecast, −31 timely60 both ways, +5 / +9
timely120 (CX:117). One addition from my per-cell table (DER17:3-13): U has more late60 riders than C-30 in **25 of 25**
w08/w17 cells, and in 3 of 9 w07 cells (6 ties). That sign pattern sets the per-cell criteria in §4.

### 1.3 WP14r fixed traffic (16 cells, 1,728 requests)

| Arm | Codex (CX:98-102) served / late60 / late120 / timely60 / exposed / mean, max S | Mine (WP17:2,5,9,14,19) |
|---|---|---|
| C-30 | 1534 / 0 / 0 / 1534 / 6 / 13.9, 27.6 | identical |
| C-60 | 1540 / 0 / 0 / 1540 / 20 / 35.8, 57.1 | identical |
| C-120 | 1563 / 23 / 0 / 1540 / 41 / 62.3, 119.6 | identical |
| LOCKS | 1584 / 47 / 27 / 1537 / 62 / "not recomputed" | identical; mean / max S 120.9 / 414.0 s |
| FREE | 1629 / 274 / 164 / 1355 / 388 / "not recomputed" | identical; mean / max S 125.0 / 538.9 s, repeated 50 |

**VERIFIED** [M]. I did not re-verify Codex's cumulative-only witness counts (2/1, 4/3). They come from its own R15
audit, which Claude agreed with in R15.

### 1.4 Other Codex facts I checked

- **U and C-30 differ only by `"hardLimit": 30000`.** `diff U.json C-30.json` shows one added key
  (`tang3/configs/`). VERIFIED.
- **Weather inventory** (Codex WX:3-7) reproduced exactly: test_2018 has 14 flagged / 10 weekdays / 11 spells / 1
  snow day; 2019 has 30 / 21 / 25 / 7 (WX17:2-5). VERIFIED. Codex's caveat that these are "weather opportunities,
  not proven traffic incidents" (CX:213) is correct.
- **The 4-vehicle check needs new fixtures.** The normalizer takes the first `VehicleCount` HMAC-ranked nodes
  (`FleetPyManhattanNormalizer.cs:461-476`). VERIFIED. Building that check therefore means a normalizer rerun and new
  fixture hashes.

---

## 2. Audit of Codex's recommended experiment (direction 1)

### 2.1 Is the Claude cost-first re-selection valid evidence?

**Reproduction [M].** My DP is my own code (WP17). Cost-first order = recorded forced / accepted / operational-cost /
candidate-id-rank levels, over the recorded eligible set. I validated the reading against necessary optimality
conditions rather than by re-solving the stability order. In every acknowledged frame the recorded plan is feasible,
has the maximum accepted count, and is lexicographically ≤ the cost-first plan under its own recorded order:
12,663 / 12,525 / 12,364 / 12,325 / 12,960 frames, 0 invalid (WP17:3,6,10,15,20).

| Gates | Differs (% of new-request frames) | Strictly cheaper | Saving per differing frame (mean) | Saving per new-request frame [A] | Saving over all acked frames | Extra plan-summed drop movement, median / max |
|---|---|---|---|---|---|---|
| LOCKS (= T3.8 U config) | 445 (26.0%) | 433 | 7.79% | 2.02% | 0.307% | 90.8 / 390.8 s |
| C-120 | 325 (19.0%) | 313 | 7.96% | 1.51% | 0.237% | 57.3 / 236.9 s |
| C-60 | 173 (10.1%) | 164 | 7.68% | 0.77% | 0.124% | 21.7 / 106.6 s |
| C-30 | 104 (6.1%) | 95 | 8.00% | 0.49% | 0.079% | 12.5 / 35.5 s |
| FREE (control) | 0 | 0 | — | — | 0 | — |

Sources WP17:7-8,11-12,16-17,21-22; per-new-request column DER17:15-18. All differing counts, percentages
and medians equal EV:350-356. **VERIFIED, with three wording corrections to the Claude side:**
1. "−7.8% plan cost" (EV:27) is conditional on the decision differing. Over all new-request decisions it is about
   −2.0% (U gates) or −0.5% (C-30 gates). Plan cost is the solver's `Schedule.OperationalCost`, not realised fleet
   cost (SEL:365-368; Codex CX:155 is right on this).
2. 12 of 445 and 9 of 104 "differences" are pure tie-breaks (equal cost, different candidate IDs).
3. **How a push "≤ 35.5 s" can exceed the 30 s cap.** It is a per-decision sum of the per-candidate
   `revision:drop_eta_total_ms` contributions over the plan (SEL:326-329 builds one vector per candidate), not a
   per-rider move. The only C-30 frame above 30 s puts all 35.5 s on one vehicle's candidate (WP17:23). Every eligible
   C-30 candidate keeps each rider's cumulative dispatch ≤ 30 s, so that candidate must move ≥ 2 riders [I]. The same
   pattern holds at C-60 (96.4, 106.6 s) and C-120 (207.0, 236.9 s) (WP17:13,18). EV:355's column header ("per
   differing frame") was correct; the summary line EV:27 ("≤ 35.5 s") was not.

**Comparability with T3.8.**
- **Commitment configs are byte-identical [M].** SHA-256 values:

  | T3.8 config (`tang3/configs/`) | WP14r config (`benchmarks/configurations/`) | SHA-256 prefix |
  |---|---|---|
  | `U.json` | `wp14-c1-nobudget-v1.json` | 998a0a94 |
  | `C-30.json` | `wp14-c1-h6-reference-v1.json` | d6124f3f |
  | `C-60.json` | `wp14-c1-budget60-v1.json` | 0956b536 |
  | `C-120.json` | `wp14-c1-budget120-v1.json` | ac0f9758 |

  The Claude claim (EV:335-336) is VERIFIED.
- **But the runner configs differ [M].** T3.8 `wp4-tier3-v2.json` adds `commitmentRecovery: no-worse-than-reference-v1`
  and `lateBoarding: record-v1`, and lacks `skipConstantObjectiveLevels: true` and the portfolio evidence profile. WP14r
  `wp14-development-ridebound-hard-vector-v1.json` has those two and lacks the first two. Generation and solver
  budgets are otherwise identical. EV:337-340 lists recovery and lateBoarding but omits `skipConstantObjectiveLevels`.
  That option should not change an optimum (it skips constant levels), but it is a difference [I].
- **Runner core differs.** 38d517d vs 1ce15e9, per Codex's own raw-manifest reads (CXR15:104-105). I did not re-read
  this.
- **Traffic, days and windows differ.** Fixed vs measured traffic; 12–13 Nov w08/w17 vs 14–18 Nov.
- **First-order only.** The screen changes one decision on a frozen state. Trajectories diverge after it.

**Verdict.** The screen is valid evidence of direction and order of magnitude for the *mechanism*: the cap
restricts what cost-first can change by a factor of about 4 (26.0% → 6.1%). It is not an estimate of T3.8 outcomes.
Pooling signal: in 89 of 104 differing C-30 decisions, 2 or more vehicles change (the new rider moves to another
vehicle), and in 81 of 104 the cost-first plan moves an incumbent's drop ETA; under LOCKS gates, 397/445 and 426/445
(DER17:15,18). That is the
signature of a new pooled insertion. It directly supports Codex's sharing hypothesis (CX:260) [S/I].

### 2.2 Is a narrow objective-order option needed? Code-size estimate

**Codex is right, for a stronger reason than it states (CX:148; CXR15:343).** There are two different "switches".
- **Policy kind `rolling-cost`.** POL:287 defaults the profile to RollingCost, and the switch at POL:290-354 has no
  RollingCost case. So the hard assessor (`AssessAndFilter`, POL:325-341) never runs. That *is* FREE: no gates at all.
- **Keep `ridebound-hard-vector` but pass the RollingCost profile to the selector.** This keeps the filter but
  silently loses three things:
  - the forced-reference level (SEL:276-280, conditional on HardVector/SoftHardHybrid). It matters because T3.8 runs
    `no-worse-than-reference` recovery;
  - the hard-assessment completeness check (SEL:256-269);
  - the recorded revision/worst vectors in the mapped selection (SEL:446-465).

  The evidence would also be mislabelled `rollingCost` (EVM:291-299).

**Minimal change [I, from reading the code].**
1. A new enum value, e.g. `HardVectorCostFirst` (SEL:10-16). Treat it like HardVector at SEL:256, :276-278 and
   :446-448, with no case at :319-331, so cost follows the accepted count directly.
2. A boolean in the policy options constructor, valid only for `RideBoundHardVector`, following the
   `forcedReferenceRecovery` validation pattern (POL:84-156, :139-145). Profile choice at POL:348-351.
3. A new optional root property in the runner config, parsed like `commitmentRecovery` (CFG:331-352) and passed at
   CFG:405-413. The allowed-root-field list must be extended too; I did not locate it (UNVERIFIED).
4. One string arm in EVM:291-299.

That is about 40–60 production lines in 4 files, plus perhaps 100–200 test lines:
- the level list for the new profile;
- config accept/reject;
- OFF ⇒ identical problem.

Domain and Application stay untouched (AGENTS.md boundary respected). `dotnet test RideBound.slnx` and the
docs/18–19 updates apply in the worktree repo.

### 2.3 Is 143 the minimum? No: the decisive design is the 2×2 (74 jobs)

**The most damaging reviewer question** (Codex's own words, CX:54): "what changes when the conservative objective is
removed while every hard gate stays fixed?" Equivalently (V:222): "is your reliability from the cap or from a
conservative dispatcher?" Answering it needs four cells of one factorial, two of which are archived:

| | U (no drop cap) | C-30 |
|---|---|---|
| Stability-first | archived (34) | archived (34) |
| Cost-first | **new (34)** | **new (34)** |

- (CF-U − CF-C30) gives the cap's value against a cost-seeking dispatcher.
- (CF-C30 − SF-C30) shows whether the conservative ordering adds anything once the cap is in place.
- The difference-in-differences is the attribution test.

**Fewer arms fail.**
- CF-C30 alone answers only the second contrast.
- {CF, SF} × {C-30, C-120} has no uncapped cost-first arm, so it cannot say what the cap buys.

**What Codex's extra 69 + 48 jobs add, and why they are secondary.**
- **SF-C120 (34 jobs).** A dose-response point between two endpoints that are already measured (U and C-30, §1.2).
  It needs **no code** (the C-120 config exists and is hash-identical to WP14r's), so it can stand alone if the owner
  wants Q2 answered on the main panel (item 2 in §4).
- **CF-C120 (34 jobs).** Codex's rationale is accumulation. Codex itself writes that a positive witness "does not
  measure a cumulative-versus-per-step trajectory effect" and that a per-step ablation is still needed and not
  included (CX:263,265). It therefore cannot settle Q3.
- **CF-C30 may already produce cumulative-only witnesses [H].** Under cost-first, the extra moves under C-30 gates
  are small (median 12.5 s per decision, WP17:22). A rider who spends about 12 s can then be refused a later 18–30 s
  move by the cumulative clause alone. Stability-first never creates such a history (0 repeated riders, DIAL17:13).
  This is a hypothesis, not a screen result.
- **4-vehicle offered-load check (48 jobs).** It needs new normalizer output and new fixture hashes. Codex states
  that "new fixture/harness validity is not certified yet" (CX:255). It is the riskiest piece and is not needed for
  the attribution question. Drop it for this deadline.

**Runtime is not the bottleneck either way.**
- T3.8 ran 170 jobs in about 7 h at 6 in parallel (RUNTIME-ESTIMATE-2026-10-07.md:24-25), so 74 jobs take about
  3 h of wall time and 143 about 6 h.
- On WP14r the cost-first (rolling-cost) arm's recorded median elapsed time was 730 s against 667 s for LOCKS and
  641 s for C-30 (EL17:2-3,6). That is about 10% slower; concurrency at the time was not recorded.

The real cost difference is engineering and analysis: 6 arms vs 4, the multiple comparisons, and the fixture work.

### 2.4 Codex's sealed-style predictions against the screens

| Codex prediction (CX:260-263) | My assessment |
|---|---|
| CF-C30 shared completions ≥ +10% vs SF-C30, served ≥ 99% | **Plausible [S/I].** 81 of 104 C-30 differing decisions are pooled insertions on 16 WP14r cells, against about 241 shared riders in WP14r SF-C30 (15.7% × 1,534; `wp14r-ladder-reanalysis-2026-10-08.txt:6`). 0 accepted-count changes at first order (WP17:21). I keep it, as secondary. |
| SF-C120 recovers ≥ 24 of the 96 C-30/U gap | **Plausible, conservative [S].** At B = 120 s, 59 of 148 budget-only-blocked requests pass the screen and 49 of those are U-served (EV:189). On w07 the screen got the net count right (+6 vs +6), but the served set reshuffled (17 in, 11 out) (EV:198-204). |
| Zero overshoot for every C run | Agree (contract test). |
| Accumulation as a secondary measured outcome | Agree. See [H] above for CF-C30. |

The missing primary in Codex's list is the **reliability-attribution interaction**: does the cap protect riders more
when the ordering stops protecting them? I add it as the primary in §4.

---

## 3. Audit of Codex's direction 2 (incident-adaptive forecasting) against the Claude forecast agent

**Facts I re-checked [M].**
- The damped-trend fit gives "alpha=1.0 beta=0.0 phi=0.8" (`r16-forecast/factor-nowcast-screen-2026-10-10.txt:2`).
- Dispatch caused 9 of the 3,446 late-seconds of the 41 snow-afternoon late riders
  (`r16-forecast/rider-nowcast-replay-2026-10-10.txt:24`).
- The regime gate leaves 19 riders late and an equal-cost pad 27 (same file, lines 15-16 and 20).
- Naive late > 120 s on the snow day is 0.69% (`optimize/test-snow-2026-10-06-report.txt:10`, "late120 0.0069").
- The "≈26% knowable" share is a retrospective screen with a post-hoc threshold (FC:36-51). Its range is 8–43%, and
  it is 15.2% with one-bin latency (`rider-nowcast-replay:30`).

**Where Codex is right and the Claude design is weaker.**
- **Leakage.** The bundle factor of bin b is built from trips *starting* in b (FC:305-306). Claude's primary rule
  allows "factors of bins finished at least L bins before t0, L = 1" (FC:354). Trips longer than 15 min that started in
  bin b−1 are still running at t0, so L = 1 is not leak-free. Codex's completed-trip as-of construction (CX:183) is
  the correct contract, and it costs more work.
- **Reconstruction gate.** Matching Syed's published series with an unknown speed–distance definition and random
  node mapping is open-ended. Claude budgets 8–12 h for the builder plus gate (FC:441). That is a happy-path figure.

**Where the Claude design is stronger.** Event count.
- Codex's chronological test split (Sep 2018–Dec 2019) contains only **5 snow spells**, one of which is the
  already-inspected 15 Nov (WX17:4-5). Its "≥ 10 spells" minimum (CX:281) is reached only by counting rain days.
- Rain days carry level effects of a few percent (FC:259).
- Claude's rolling-origin-by-winter design reaches about 18 heavy-snow test weekdays over 2014–2020 (FC:376-377).

**Effort verdict [O].** For a design a strict reviewer would accept (causal completed-trip feed, validated
reconstruction, enough snow events), **Codex's 80–140 h is the more credible range**. Claude's 35–50 h is a
lower bound for a leakier design. Both exclude new simulated days and both need a pyarrow install approval
(FC:293-294).

**Ranking verdict.** Codex calls this a credible alternative to direction 1 (CX:50,273). I disagree for this
deadline.
- Even a full success cannot change any claim about rule C (9 s of dispatch).
- Its ceiling in this simulator is a 60–120 s band (0.69% > 120 s naive).
- Every method component is prior work (FC:254-265).

It belongs in the thesis as one diagnostic paragraph plus a future-work protocol (FC:486-498), not as a work package.

---

## 4. Converged ranked list (at most 3 items)

### 1. RECOMMENDED SINGLE NEXT STEP: the 2×2 objective × cap experiment (A2-min, 74 jobs), time-boxed

**The step itself.** In a new worktree from `C:/Code/RideBound-noworse`, implement the cost-first option (§2.2), then
pass **Gate 0**. Everything else in this item depends on Gate 0.

**Design.**
- Arms SF-U and SF-C30 are archived. CF-U and CF-C30 are new.
- Panel: the 34 T3.8 test cells, same fixtures, worlds, seeds, WP4 config and recovery; only the new option differs.
- Forecast: the existing `causal-no15` display replay applied post hoc, with no retuning.
- Jobs: 4 OFF-equivalence (SF-U and SF-C30 on one w08 and one w17 cell, e.g. d20181116-s10-r1-w08/w17)
  + 2 ON smoke + 68 main = **74** (= V:262-266 and CXR15:349).

**Sealed-style predictions** [H]. Seal them, with a hash, before Gate 0. Reference numbers are from DIAL17:12-13 and
`pooling-share-2026-10-06.txt:2-3`.

| ID | Prediction | Basis |
|---|---|---|
| G0 | OFF reproduces the archived fleet actions and final ledger (decision and state hashes, not file bytes) on all 4 gate jobs | binary drift exists (CXR15:106) |
| H1 | CF-C30: every rider S ≤ 30 s, 0 overshoots, forced decisions 0 or each explained | contract |
| H2 (lever) | CF-U shared ≥ 32.8% (SF-U 22.8% + 10 pp, = V P2.1), exposed ≥ 348 (2 × 174), naive late60 ≥ 263 (203 + 60) | [S] 26.0% re-picked, median +90.8 s; WP14r FREE vs LOCKS 274 vs 47 late60 |
| H3 (cap alone protects) | CF-C30 naive late60 ≤ 4.25% of served (= V P2.2) and forecast late60 ≤ 1.0% of served (SF-C30 0.43%) | [S] 6.1% re-picked; per-rider ≤ 30 s |
| **H4 (primary: attribution)** | DiD in naive late60, [CF-U − CF-C30] − [203 − 76], ≥ +50 pooled, and > 0 in ≥ 18 of the 25 w08/w17 cells (under SF, U > C-30 in 25/25 of them, DER17:6-13) | H2 + H3 |
| H5 (rider-facing co-primary) | forecast timely60 per request: [CF-C30 − CF-U] ≥ +31 (the SF value, 2,328 − 2,297) | WP14r fixed: C-30 1,534 vs FREE 1,355 timely60 |
| H6 (service and sharing under the cap) | CF-C30 served ≥ 2,315 and shared ≥ 345 (313 × 1.10) | Codex CX:260; V P2.3; [S] 81/104 pooled insertions |
| H7 (secondary) | ≥ 1 cumulative-only budget record in CF-C30 | [H] §2.3; a witness, not a per-step effect |

**Kill and interpretation rules (fixed before running).**
- G0 fails → stop; no cost-first claim; go to item 3. Do not reuse archived controls.
- H1 fails → implementation defect; stop.
- Gate 0 not passed within 5 working days of starting, or the whole item not done within 10 → drop it; item 3.
- H3 fails → the ordering does real reliability work under the cap; withdraw "the cap alone suffices" and say so.
- H2 fails (CF-U ≈ SF-U) → the objective is not the lever; the conservative-dispatcher objection is empirically
  small; report and stop.
- H6 served fails → cost-first plus the cap blocks later riders; report it as a negative.
- Every outcome is reported, including false predictions.
- Claims stay limited to 34 previewed cells and 5 days. No profit claim without a realised-cost extraction.

**Effort** (my estimate, UNVERIFIED): 30–50 h.
- option plus tests 10–18 h;
- gate and smoke 3–5 h;
- compute about 3–4 h of unattended wall time;
- analysis 6–10 h with existing readers (`r17_verify_dial.py`, `pooling_share.py`);
- write-up 8–12 h.

V estimated 25–35 h; Codex 60–90 h for its 6-arm + offered-load version.

**Deadline risk: moderate to high.** The deadline (mid-November) is UNCONFIRMED, and the LaTeX predates T3.8 and the
forecast (RV §1.3 row 6). The rewrite is the binding constraint and is needed whatever this experiment shows. Start
the chapter text that does not depend on the 2×2 in parallel. If the deadline is confirmed at under 4 weeks, skip
item 1.

### 2. OPTIONAL, zero code: SF-C120 on the 34 T3.8 cells (34 jobs)

This answers the owner's Q2 on the main panel. It now has the separate owner request that CXR15:335 required.
- Existing runner and `C-120.json` (sha ac0f9758…). It needs only a copied harness entry.
- Predictions [H, from the screen at EV:187-204]:
  - served ≥ 2,362 (≥ +24, Codex's threshold);
  - naive late60 between 90 and 160;
  - naive timely120 ≥ 2,350.
- Kill: none. It is a descriptive dose point and must never be presented as an optimum.
- Effort: about 2 h compute plus 3–4 h analysis.

### 3. MANDATORY and fallback: the bounded zero-run results chapter (A1), with direction 2 as future work

Narrowed claims:
- the cumulative clause was inert on measured traffic;
- C vs M⁺ compares obligations, not outcomes;
- the padded-U tie;
- Hörl & Zwick 2022 must be cited (RV:76-80);
- the forecast (a)/(b)/(c) split as a labelled limitation.

Plus Codex's/Claude's leakage-safe incident-forecast protocol as a future-work paragraph. Effort 16–24 h of analysis
and claim work (CX:295), plus the rewrite.

---

## 5. Remaining disagreements with Codex, and what would settle them

| # | Disagreement | My position | What settles it |
|---|---|---|---|
| 1 | Scope: 143 (+48) jobs vs 74 | The 2×2 answers the most damaging question. C-120 arms answer dose-response and a witness hunt that Codex says cannot settle Q3. The 4-vehicle fixtures are unvalidated. | Agreement on which question is primary. Codex's own R15 minimum (CXR15:349) and its "do not execute alongside A2" (CXR15:335). If the owner wants Q2 on the main panel, add item 2 (zero code), not CF-C120. |
| 2 | Primary endpoint: CF-C30 vs SF-C30 sharing (CX:260) vs the attribution DiD | DiD on late60 / timely60 primary; sharing co-primary | Codex's own framing at CX:54 is an attribution question. Its design already contains CF-U, so this is about labelling, not jobs. |
| 3 | Direction 2 as an alternative (CX:273) vs future work | Future work: ceiling 60–120 s, 9 s of dispatch, about 5 snow spells in Codex's own test split | Codex would need to show a forecast result that changes a rule-C claim, or ≥ 10 snow events in a leak-free split. Neither exists. |
| 4 | Direction-2 effort | **I concede to Codex** (80–140 h is more credible than 35–50 h) | — |
| 5 | Direction-1 effort | 30–50 h for the 2×2 vs Codex's 60–90 h for its larger design | Not an empirical dispute; it follows from #1. |

**Concessions** (Codex right, Claude side wrong or imprecise):
- the w07 forecast column must be the causal one (§1.1);
- the RollingCost shortcut is insufficient (§2.2);
- the L = 1 leakage critique (§3);
- direction-2 effort (§3);
- the sharing hypothesis is supported by the screen (§2.1).

**Corrections to the Claude R16 evidence wording:**
- "−7.8%" is conditional (−2.0% / −0.49% per new-request decision; 0.31% / 0.08% over all acknowledged frames);
- "≤ 35.5 s" is a plan-level sum over ≥ 2 riders;
- 12 and 9 tie-break-only "differences";
- the omitted `skipConstantObjectiveLevels` config difference.

**Not verified by me:**
- Claude's FREE-vs-LOCKS 401/76 gate decomposition (EV:378-387);
- the 973/807 request–run pairs;
- the 5/51/123 co-rider screen;
- the Hörl & Zwick citation claims.

Codex is verifying those this round.

## 6. Files

- `claude-work/R17-REBUTTAL-CLAUDE.md` (this file).
- `claude-work/r17-rebuttal/`:
  - `r17_verify_dial.py` → `r17-verify-dial-2026-10-10.{txt,json}`: 140 transcripts, hash-checked;
  - `r17_wp14r_check.py` → `r17-wp14r-check-2026-10-10.{txt,json}`: 80 transcripts, ledgers plus independent
    cost-first DP;
  - `r17_weather_recount.py` → `r17-weather-recount-2026-10-10.txt`;
  - `r17_wp14r_elapsed.py` → `r17-wp14r-elapsed-2026-10-10.txt`;
  - `r17_derived_counts.py` → `r17-derived-counts-2026-10-10.txt`: per-cell signs and first-order details from the
    JSON above;
  - run logs `run-dial.*`, `run-wp14r.*` (stderr empty, exit 0).
