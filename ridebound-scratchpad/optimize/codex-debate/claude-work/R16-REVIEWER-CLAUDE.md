# R16 — Strict external referee report (Claude side), 2026-10-10

**Role.** An external referee of the kind a TR Part C / IEEE ITSC editor would assign. I owe nothing to the R13–R15
recommendation, and my brief is to say whether it was wrong.

**What I read.**
- In full: `ROUND16-FACT-PACK.md`, `ROUND16-REVIEW-STANDARD.md`, `ROUND16-CLAUDE.md`,
  `claude-work/R13-FINAL-VERDICT.md`, `codex-work/R15-CONFIRM-CODEX.md`, `tang3/t38/T38-REPORT.md`,
  `optimize/FORECAST-REPORT.md`, `tang3/w07x/W07X-REPORT.md`, the owner's claim boundary
  `E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md`, `codex-work/R13-SURVEY-CODEX.md` and
  `claude-work/R13-ML-DATA-CLAUDE.md` §0–§6.
- In part:
  - the handoff `BAN-GIAO-PHIEN-2026-10-09.md` §3–5 (lines 88–400);
  - `claude-work/R13-SURVEY-CLAUDE.md` §(b)–(d) and the synthesis;
  - `codex-work/ROUND12-REPLAY-PROTOCOL-CODEX.md`.
- Raw outputs, opened myself: PAD, LAD, CVP, BUD, EXP, SHARE, LOAD, the cumulative decisive check and
  `codex-work/R15-audit-summary.txt`.
- Primary papers, from text extractions:
  - Fielbaum & Alonso-Mora 2020;
  - Schulz & Pfeiffer 2026;
  - Hörl & Zwick 2022.
- Code: `C:/Code/RideBound-noworse/src/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs:271-372`.
- The LaTeX thesis `E:/Code/Report_INT3508/ridebound/noi-dung/*.tex`. Read only:
  - all of 02, 05 and 09;
  - ch.3 :280-330 and :495-535;
  - ch.4 :1-200, :1313-1377, :1826-1900 and :2208-2271.

**Not opened, as instructed.** `codex-work/R16-*`, `codex-work/r16-*`, `antigravity-work/`,
`claude-work/R16-EVIDENCE-CLAUDE.md`, `R16-FORECAST-CLAUDE.md` and the folders `claude-work/r16-evidence`,
`claude-work/r16-forecast`.

**What I did not do.** No simulation, build, install, deletion, or write outside this file.

**Evidence labels.**

| Label | Meaning |
|---|---|
| **[M]** | measured in existing runs |
| **[S]** | first-order screen on recorded paths |
| **[I]** | my inference |
| **[H]** | hypothesis or prediction |
| **[O]** | reviewer opinion |
| UNVERIFIED | I could not check it myself |

**Anchor keys** (relative to `E:/Code/Report_INT3508/ridebound-scratchpad/`).

| Key | File |
|---|---|
| FP | `optimize/codex-debate/ROUND16-FACT-PACK.md` |
| V | `optimize/codex-debate/claude-work/R13-FINAL-VERDICT.md` |
| R15 / R15A | `optimize/codex-debate/codex-work/R15-CONFIRM-CODEX.md` / `…/R15-audit-summary.txt` |
| T38 / FR / W07X | `tang3/t38/T38-REPORT.md` / `optimize/FORECAST-REPORT.md` / `tang3/w07x/W07X-REPORT.md` |
| PAD | `optimize/codex-debate/claude-work/cap-vs-pad-frontier-2026-10-07.txt` |
| LAD | `…/claude-work/wp14r-ladder-reanalysis-2026-10-08.txt` |
| CVP | `…/claude-work/r13-proposer/cumulative-vs-perinsertion-2026-10-10.txt` |
| CDC | `…/claude-work/r13-final-judge/cumulative-decisive-check-2026-10-10.txt` |
| BUD | `…/claude-work/budget-block-diagnosis-2026-10-07.txt` |
| EXP / SHARE / LOAD | `…/codex-debate/exposure-check-2026-10-06.txt` / `pooling-share-2026-10-06.txt` / `…/claude-work/load-and-occupancy-2026-10-07.txt` |
| MLD | `…/claude-work/R13-ML-DATA-CLAUDE.md` |
| D03 | `E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md` |
| FAM | Fielbaum & Alonso-Mora 2020, text `…/scratchpad/papers/Unreliability_in_ridesharing_systems_Measuring_cha.txt` |
| SP | Schulz & Pfeiffer 2026, text `…/scratchpad/papers/s00291-026-00847-0.txt` |
| HZ | Hörl & Zwick 2022, text `optimize/codex-debate/claude-work/pdf/hoerl-zwick-2022.txt` |
| SEL | `C:/Code/RideBound-noworse/src/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs` |
| TEX | `E:/Code/Report_INT3508/ridebound/noi-dung/` |

---

## 0. Bottom line

1. **As a TR-C submission, the core is a reject. As an ITSC paper it is a weak reject.** As an undergraduate
   thesis it is a pass, provided the written text undergoes major revision. The empirical work is unusually careful:
   sealed plans, and independent re-computation over 227 transcripts (R15:11-13). The contribution is narrow, though,
   and its two distinctive mechanism claims are weaker than the text says:
   - **The cumulative clause never acted on measured traffic.** All 1,256 recorded budget prunings exceeded B in a
     single dispatch increment (CDC:4-30; R15A:7,10-17) [M].
   - **The cause-separated reference already exists.** Hörl & Zwick 2022, strategy B, uses a traffic-updated
     expected drop-off as the binding reference: "t_dropoff required = max(t_updated, t_latest)" (HZ:569). They
     introduced it precisely "To overcome the issue of undefined system states" (HZ:507). The thesis LaTeX does not
     cite it anywhere (TEX/10-tai-lieu.tex bibitems; grep found no "Hörl" or "Zwick") [M].
2. **Rule C has no outcome advantage over the deadline rule, or over a padded quote.**
   - Rule C and M⁺-30:
     - serve the same number of riders, 2,332 of them in common (R15A:19);
     - take the same fleet actions in 30 of 34 cells (T38:64);
     - tie at 2,328 on-time completions with the forecast (PAD:33,54).
   - U + forecast + 30 s pad also reaches 2,328 on-time completions, and it serves 96 more riders (R15:169-171).
   - C's "0% forced against 41.3%" is a property of the obligation C chose (it excludes traffic). It is not a better
     outcome for riders [I/O].
3. **The thesis already contains its own Hörl & Zwick-style baseline.** M⁺ with recovery rule (b) lets a forced
   vehicle re-route provided it is "no worse" on every gate the old route already violated (TEX/08-chuong4.tex:1319-1321).
   That is the logic of HZ eq. (7) [I]. M⁺(b) served the same as C in 21 of 22 runs (TEX/08:1361-1362) [M]. So the
   claim "only the conduct cap never empties the choice set" (TEX/02-tom-tat.tex:24-26; TEX/05:169-171) is true only
   inside the four families the thesis chose.
4. **The R13–15 recommendation was right on sequencing, but under-specified.** Its sequencing: keep the storyline,
   consolidate first, run nothing. Three corrections:
   - **The rewrite is bigger than one chapter.** The LaTeX was last edited 2026-09-30, before T3.8 and the forecast.
     It is built on the four-family theorem, and it contains several claims that prior work contradicts (§3).
   - **A2 as designed cannot test accumulation.** At B = 30 s, cumulative-only exposure is 0–0.12% even under
     uncapped cost-first dispatch. At 120 s it is 0.69–1.04% (CVP:5,7,20,22,30,32) [S].
   - **"Never forced" was over-sold** as the real separation from the deadline rule (V:206-207).
5. **No pivot is better.** I checked the main candidates:
   - incident-day forecasting from multi-year NYC data;
   - the 2013 Fielbaum & Alonso-Mora data;
   - a new promise object (windows or tiers).

   Each loses the mechanism identity and gains no novelty under the owner's own boundary (D03:56; FP:91-93). The
   2013 data were chosen by their authors so that they could "disregard unreliability due to traffic conditions"
   (FAM:574-575). That is the opposite of what Q5 needs.
6. **Ranked extensions, at most one before the deadline:**
   1. **A2′.** Cost-first selection under unchanged gates, at B = 30 s and B = 120 s. It is the only one that can
      produce a non-definitional mechanism result.
   2. Strong-baseline completion: C-0 (config only) plus M⁺(b) on T3.8.
   3. A density sweep.
   4. An offline multi-day incident-forecast benchmark from TLC 2016–2020.
   5. A different promise object, or the 2013 data: not recommended.
7. **The three most damaging questions** (detail in §1.5):
   - What is new beyond Hörl & Zwick B, given that accumulation is inert?
   - Which rider or operator outcome does C improve over the deadline rule or padded quoting?
   - Is the forecast result an artefact of one city-wide factor and 0 s dwell in a low-density, toy-scale cell?

---

## 1. Referee report on the thesis core

### 1.1 Summary of the submission's claims

The core, as the storyline defines it (handoff:88-156; V:44-48):
- **Rule C.** For each rider, the sum of absolute dispatch-caused drop-off revisions is at most B = 30 s. Dispatch
  is c = p − e, separated from traffic x = e − v by re-projecting the old plan at current speeds.
- **The forecast quote.** The first drop-off promise is stretched by a historical 15-minute traffic-growth profile.
- **The three-part ledger.** It splits lateness into dispatch, anticipated traffic and unanticipated traffic.

**Evidence.** One simulator (FleetPy Manhattan). In each cell: 108 requests, 8 vehicles, 96 nodes on a metric
closure, 0 s dwell, and one city-wide travel-time factor per 15 minutes. The main T3.8 panel has 34 cells and 3,672
requests, over 14–18 Nov 2018 and three windows.

**Headline results [M].**
- **C-30 against M⁺-30 (deadline from the first quote).**
  - Served 2,338 = 2,338.
  - Forced decisions: 0% against 41.3%. Self-broken promises: 0% against 14.5% as a cell mean, 12.4% pooled
    (T38:57-60,111).
- **C-30 against U (no drop cap; same locks and same objective).**
  - Served: −96 riders.
  - Late by more than 60 s against the first promise: 203 against 76 riders (R15A:7,9).
  - Shared rides: 22.8% against 13.4% (SHARE:2-3).
- **The forecast.**
  - C-30, late > 60 s: 3.25% → 0.43% pooled by rider. The quote grows by 7.4 s (PAD:25,33).
  - The gain is not specific to C; M⁺ and V reach the same (FR:65).
  - Snow afternoon: 7.19% → 5.94%, and 92.5% of late seconds are "unanticipated" (FR:103-104).
- **The new audit.** On measured traffic the cumulative clause decided nothing: 0 of 1,256 prunings were
  cumulative-only (CDC; R15A).

### 1.2 Closest prior work and what is left

| Prior work (anchor I opened) | What it already contains | What is left for this thesis |
|---|---|---|
| **Hörl & Zwick 2022, strategy B** (HZ:495-497,507,531-541,569) | (1) A traffic-updated expected drop-off computed "by traversing the routes and summing up travel times". That is the thesis's e. (2) New pickups are allowed "as long as the on-board requests are not dropped off later than what is the absolute minimum, given current traffic conditions". That is a dispatch-only bound with tolerance 0 for riders already at risk. (3) The motivation is avoiding "undefined system states" under traffic, the same failure the thesis's theorem addresses. | (a) A tolerance B > 0 for all riders, from booking, against the displayed promise rather than the service window. (b) A hard gate rather than a penalty. (c) A per-rider ledger and certificate. (d) A measured comparison with a deadline rule on measured-traffic factors. |
| **Fielbaum & Alonso-Mora 2020** (FAM:948-986,1004-1006,1038-1039) | Measures one-time unreliability per rider. Controls it before the decision (§6). Shows the trade-off: rejections 34.5% → 45.6%, per Codex's PDF check (R15 row 62). Warns that banning in-vehicle detours would make the system "(almost) non-shared". Names as open "how to … provide more accurate times without increasing the rejection rate". | C does **not** answer that open question: it raises rejections (−96 served) and roughly halves pooling (shared passenger-minutes 2,962 → 1,388; EXP:2-3). |
| **Schulz & Pfeiffer 2026** (SP:489-490,1204-1205,1466-1497,1665-1670) | A drop-off deadline set from the first offer: "customer i is certainly served within the time interval". l = 900 s, "also done this way in practice". l is swept from 0 to 30 min. Per-customer l by direct travel time and price tiers are named as future work. Travel times are fixed. | Without traffic, C and M⁺ accept the same set (12/12; handoff:154-155). The thesis's difference appears only under drift, and only at B = 30 s, which is 30× tighter than SP's 900 s. |
| Elmi et al. 2026; UberX Share; Mt-KaRRi 2026; Lyft US12182741B2 (D03:211-213; V rows 68,71,72) | Per-rider guarantees; "additional pickups won't increase your estimated arrival time"; latest arrival relative to the accepted trip; per-match ETA-ratio limits | The narrow combination specified in D03 §1. Its "cumulative / path-dependent" element is inert in every measured run (§1.4 C2). |
| Forecast quoting (D03:267-269; handoff:139-142) | Standard practice | Only the measurement and the ledger split |

### 1.3 Scores (1 = poor, 5 = excellent)

| # | Criterion | Score | Reason |
|---|---|---|---|
| 1 | Novelty / originality | **2** | Hörl & Zwick B already has the cause-separated reference and the "never undefined" motivation. Schulz & Pfeiffer and Fielbaum & Alonso-Mora cover deadline and control. The one element that is not in prior work, accumulation, never acted on measured traffic (CDC:4-30). What remains is a tolerance-B, all-rider, auditable variant plus a careful comparison. |
| 2 | Significance | **2** | No rider-facing or service outcome beats the deadline rule (2,328 = 2,328 on-time) or the padded quote (2,328 = 2,328, with +96 served for padded U). C costs 3.9% of U's served riders and 53% of shared passenger-minutes (EXP:2-3) [M]. The gains are mostly under 2 minutes, while real compensation thresholds are about 10 minutes (V row 70). The ledger is a reusable diagnostic; that is the main value. |
| 3 | Technical soundness | **3** | The gate is implemented and audited: 0 overshoots and 0 forced decisions (T38:47). Witness semantics were checked (V rows 29-31). Weaknesses: (a) the headline theorem holds by construction (TEX/07-chuong3.tex:292-297, "A = \|e − e\| = 0"); (b) "attribution" is a model projection (D03:222-224); (c) the stability-ordered objective, not the cap, may supply part of the reliability, which is untested (SEL:283-331); (d) low density, occupancy 0.535 (LOAD:2), against ≈ 1.33 in the FleetPy paper (R15 row 20); (e) one scalar traffic factor and 0 s dwell make the forecast close to an oracle (FR:77,167-169). |
| 4 | Experimental rigor | **3** (journal: 2–3) | Strengths: sealed plans with hashes; sealed predictions, with failures reported (T38:67-78; FR:148-163); cluster bootstrap; independent re-implementation. Weaknesses: 5 days; 34 cells whose demand overlaps 3–20 of 108 rows (T38:93); one episode per cell (T38:90); exploratory thresholds chosen after previewing (T38:8,89); the forecast is fitted on a federal holiday and a 26.9 mm rain day (FR:97; MLD:23); one snow event; the padded-U comparator was added post hoc; strongest baselines are missing (cost-first + cap, C-0, Hörl & Zwick-style relaxed deadline on T3.8). |
| 5 | Reproducibility | **4** | SHA-sealed plans, inventory hashes, a fixed seed. Codex reproduced the counts over 458,477 decoded frames (R15:13). Drawbacks: the stack is complex (C# runner + FleetPy + wrappers), and the archived binary core `1ce15e9` sits one `src/` commit behind HEAD (V row 40). |
| 6 | Feasibility (~5 weeks, unconfirmed) | **4** for A1 (0 runs); **2** for any T2 extension | The binding constraint is writing. The LaTeX predates every result the storyline relies on: files dated 2026-09-24/30, and no "2.338", "2.434" or forecast text in TEX/*.tex [M]. |

### 1.4 Major concerns

**C1. Novelty against Hörl & Zwick 2022 B. Not addressed in the thesis.**
- HZ eq. (7), "max(t_updated, t_latest)" (HZ:569), applied to a promise deadline instead of a service window,
  becomes the relaxed deadline p ≤ max(p0 + B, e) [I].
- That rule shares C's key property: the do-nothing plan has p = e, so it always passes [I, one line].
- The thesis puts "the only family that never empties the choice set" at the centre of its contribution
  (TEX/05-chuong1.tex:174-182; TEX/09-chuong5.tex:18-22,224-231). That framing omits the closest published
  mechanism, which has the same property.
- The thesis's own M⁺ recovery rule (b) implements that logic (TEX/08:1319-1321) and is service-equivalent to C
  (TEX/08:1361-1362). The T3.8 M⁺ arm instead uses the "keep the rejected route" recovery
  (SEL:284-286: "A forced option keeps a route that a commitment gate rejected"). Whether it is rule (a) for all
  T3.8 runs is UNVERIFIED by me.

**C2. The mechanism claimed is not the mechanism observed.**
- The text sells a cumulative per-rider budget:
  - TEX/02-tom-tat.tex:15-16, "cộng dồn và chỉ tăng" (accumulating and only increasing);
  - D03:7, "cumulative/switch budget".
- What was observed:
  - 0 of 1,256 measured-traffic prunings were cumulative-only (CDC:4-30; R15A:7,10-17) [M];
  - under C on measured traffic, no rider had two nonzero dispatch changes (FP:43-45) [M].
- So what acted was a per-step cap on the dispatch increment. That a per-step cap would reproduce the trajectories
  is an inference that was never run (R15 row 32, CANNOT CHECK).
- Why: moves are lumpy. Nonzero U revisions have a median of 108.6 s (V row 13), so at B = 30 s almost any move
  exceeds B in one step [M/I].

**C3. The C vs M⁺ result compares obligations, not outcomes.**
- Rider-facing outcomes are the same:
  - late > 60 s: 3.25% against 3.17% (PAD:25,46);
  - on the deadline yardstick (A > x), C and M⁺ are 24.0% and 24.0% at 30 s on w07 (W07X:22);
  - dispatch-exposed late riders: 4/76 against 1/74 (EXP:3-4).
- C's 0 self-broken promises follow from C not promising traffic. A referee will read this as "C never breaks its
  promise because it promises less" [O].
- The contrast exists only at tight B. M⁺ forced decisions fall to 1.7% at 240–300 s (W07X:28-29), and SP uses
  900 s (SP:1204-1205).

**C4. Against padded quoting, C does not dominate.**
- U + forecast + 30 s pad:
  - on-time completions per request 2,328 = C-30 + forecast 2,328;
  - 2,366 against 2,338 at 120 s;
  - 96 more riders served (R15:167-177) [M].
- C's gains are confined to:
  - quote sharpness: 7.4 s against 37.2 s extension; early > 60 s 0.17% against 1.81%;
  - lateness among served riders: 10 against 106 late > 60 s (R15A:7,9).
- **My first-order arithmetic.** Hold everything else fixed: same operating cost, no demand response to a 30 s
  longer quote. C + forecast is better than padded U only when one late completion costs the operator q > m, where
  m is the margin of one trip. Why:
  - at 60 s: Δserved = −96 and Δlate = 10 − 106 = −96, so q/m > 1.00;
  - at 120 s: Δlate = 0 − 68 = −68, so q/m > 96/68 ≈ 1.41.

  This is sensitivity arithmetic, not an ROI estimate (D03:241-245).

**C5. The testbed limits what the forecast and ledger results mean.**
- The setting:
  - one multiplier per 15 minutes for the whole city (MLD:61-66);
  - 0 s dwell (handoff:205);
  - a stretch under true traffic fits arrivals within 2 s for 2,305 of 2,305 dispatch-zero riders (FR:77).
- So "anticipated traffic" is a univariate series that is highly predictable from two prior days. The weekday result
  6.01% → 0.17% is, as FR:169 itself says, an upper bound ("mức trần") for a time-of-day forecast.
- The density issue: occupancy 0.535 (LOAD:2), against ≈ 1.33 in the FleetPy paper on the same data (R15 row 20).
  Pooling is sparse, so dispatch-caused lateness is small to start with, and accumulation cannot be tested.

**C6. Confounder: the objective, not the cap.**
- U and C share the order forced-reference → accepted count → hard utilisation → revisions → cost (SEL:283-331,
  365-368; verified this round).
- The utilisation level is saturated in every decision (V row 35), so "fewest revisions" ranks before "cheapest".
- The thesis cannot say whether a cost-first dispatcher under the same cap keeps C's reliability. FREE against
  LOCKS is a package comparison (LAD:2-3).

**C7. A small, previewed, correlated sample.**
- 5 days and 3 windows; the cells of one day share demand rows (T38:93).
- The forecast's A1 survives with cluster-t on df = 5, but fails when the holiday source day is dropped (FR:94-99).
- No population claim is possible (D03:224-226).

### 1.5 The five most damaging reviewer questions

| # | Question | Does existing evidence answer it? |
|---|---|---|
| Q-A | "Hörl & Zwick (2022) B already replaces the drop-off constraint by the traffic-updated expected drop-off and forbids extra dispatch delay for at-risk riders, precisely to avoid undefined system states under traffic. Your 'only the conduct cap never empties the choice set' omits this family. With accumulation inert, what is new beyond a tolerance B > 0?" | **No.** Not cited. The thesis's own M⁺(b) is evidence that the HZ-style relaxed deadline is service-equivalent (TEX/08:1361-1362). |
| Q-B | "Your mechanism is a cumulative per-rider budget, but none of 1,256 prunings was cumulative-only. Is C anything other than a per-insertion cap on dispatch delay?" | **Yes, against the claim.** It is a per-step cap in this regime (CDC; R15A). A trajectory-level ablation was not run. |
| Q-C | "C-30 and M⁺-30 serve the same riders, act identically in 30/34 cells, and tie on on-time completions with the forecast. U + forecast + 30 s pad ties too, with 96 more riders. Which outcome does C improve, and why test the deadline at 30 s when practice uses 900 s?" | **Partly.** Quote sharpness and lateness among served riders (R15:167-177); enforceability. No rider or operator outcome; tightness not justified (D03:214-217). |
| Q-D | "Is C's reliability due to the cap or to the stability-ordered objective that U and C share? Would a cost-first dispatcher under the same cap keep it?" | **No.** A2 has not been run. FREE/LOCKS is a package (LAD:2-3). |
| Q-E | "One city-wide factor, 0 s dwell, 108 requests and 8 vehicles on 96 nodes, occupancy 0.54 against 1.33, 5 days, one snow event: does anything transfer beyond this simulator?" | **No.** Acknowledged as limitations only (handoff:202-211; FR:165-177). |

### 1.6 Minor issues (the referee would list them)

- "0.17%" is used for two different things:
  - the 30 s cap's churn ratio (TEX/05:252);
  - the forecast's cell-mean lateness (FR:42).

  The all-34-cell value is 0.51% and the pooled value 0.43% (D03:267-268).
- The welfare section (TEX/08:1852-1859) monetises cumulative churn with a value of unexpected time. It also
  attributes 20–25 EUR/h to Geržinič et al., "chưa đối chiếu được với bản gốc" (not checked against the original).
  An unverified source should not appear in a results table.
- "Measured traffic" must read as "city-wide factors derived from TLC trips". Base speeds are anchored at 00:00, and
  simulated/real travel-time ratios are 0.60–0.89 at 08 h (handoff:210-211).
- The 34 of 1,471 forecast pickup displays later than the latest pickup (FR:70) is an operational contradiction.
  It belongs in the main text, not only in the limitations.
- Report CIs on the frontier table (PAD), not only on H2 (T38:43-44).

### 1.7 Recommendation

- **TR Part C (journal): REJECT.**
  - Novelty is incremental relative to Hörl & Zwick 2022, Fielbaum & Alonso-Mora 2020 and Schulz & Pfeiffer 2026.
  - The one non-prior element is inert.
  - The testbed is toy-scale with a one-scalar traffic model.
  - Resubmission advice: show accumulation matters in a dense or cost-first regime, add the HZ-style baseline, and
    move to a realistic network and density.
- **IEEE ITSC (conference): WEAK REJECT / BORDERLINE.** It is fixable to borderline-accept as an honest empirical
  note. Suggested title: "Dispatch-only drop-off caps versus first-offer deadlines under measured congestion". It
  needs:
  - the HZ positioning;
  - the padded-quote frontier;
  - the cumulative-inert result stated plainly;
  - ideally A2′.
- **Undergraduate thesis (UET): ACCEPT (pass), conditional on a major revision of the text.**
  - The engineering, audit discipline and honesty about negative results are well above the usual level.
  - The current LaTeX would draw a damaging committee question on §3 items T1–T6, starting with T2 and T5.
  - Whether "good enough" for this committee: UNVERIFIED (R15:297).

---

## 2. Q1 audit: was "keep the storyline, run nothing, consolidate; optional cost-first" right?

### 2.1 Verdict on the R13–15 recommendation

**Mostly right, but under-specified on three points, and one of its arguments was over-sold.**

**What it got right:**
- Consolidate before adding.
- Report the padded-U row (R15 §2).
- State the cumulative audit plainly (V:126-132).
- No ML chapter.
- No new promise object.
- At most one optional experiment.

Given an unedited thesis and about 5 weeks, a zero-run consolidation is the only zero-risk path [O].

**What it under-specified:**
1. **The size and target of the rewrite.**
   - "One results chapter" (V:62-65) understates the task. The abstract, ch.1 and ch.5 still centre on the
     four-family theorem and on B1/C1 panel numbers, and several statements are contradicted by HZ or FAM (§3).
   - The most exposed claim in the actual thesis is that theorem, not the frontier table. The verdict cites HZ in a
     table (V:156) but never asks for the thesis's headline to be demoted.
2. **A2 as designed cannot test accumulation.** Its prediction P2.4 asks for at least one cumulative-only rejection
   under C-30-cf (V:287-289). The uncapped cost-first screens give:
   - at 30 s: 0.12% of riders (WP14r FREE), 0% (WP9 A b1), 0% (WP9 B b1);
   - at 120 s: 0.80%, 0.69% and 1.04% (CVP:5,30,20 for 30 s; CVP:7,32,22 for 120 s) [S].

   A cost-first study that means to say anything about accumulation must include **C-120-cf**.
3. **The HZ-style baseline already sits in the thesis's own sweep.** M⁺(b) ≈ C in 21 of 22 runs (TEX/08:1361-1362).
   It should be presented as such.

**What it over-sold.** It called "never forced (0% against 41.3%)" "a real measured separation" (V:206-207). The
separation is real but definitional. It exists only at B ≤ about 120 s (W07X:22-29), and it changes no arrival
(PAD:25,46,33,54). A reviewer will not count it as significance.

**Did it under-sell a better direction?** No. No pivot I can construct raises novelty within the owner's boundary.
It did under-sell the one study that could give the mechanism a non-definitional result: A2 run at B = 120 s.

### 2.2 Steelman of the opposite ("change direction")

The case, put as strongly as I can:
- C's distinctive outcome is definitional (C3), and the accumulation it advertises is inert (C2).
- The largest per-request improvement comes from the forecast:
  - U → U + forecast: on-time completions 2,231 → 2,297, +66;
  - U → C-30: 2,231 → 2,262, +31 (PAD:4,12,25) [M].
- The largest unexplained residual is the unpredictable day (snow: 34 of 601 late riders; MLD:293-298).
- So, the argument runs, the thesis should become "promise accuracy under traffic", with incident nowcasting
  evaluated on many held-out incident days from multi-year NYC data.

**Why it fails review [O]:**
- Forecast quoting and ML ETA are excluded as novelty (D03:267-269; FP:91-93).
- Damped-trend and regime-switch nowcasting are classical (Gardner & McKenzie 1985).
- In this simulator the target is one scalar per 15 minutes (MLD:323-324). The study collapses into univariate
  time-series forecasting, and a TR-C reviewer would call it out of scope.
- It discards the only piece with any novelty residue, the dispatch-only all-rider cap and its ledger.
- Measured per served rider instead, the cap is the bigger lever:
  - U → C-30: late > 60 s 8.34% → 3.25%, −5.09 pp;
  - U → U + forecast: 8.34% → 5.63%, −2.71 pp (PAD:4,12,25).

  So "forecast is the main lever" depends on the denominator.

### 2.3 Candidate directions

#### Candidate 1 — A2′: cost-first selection under unchanged hard gates, at B = 30 s and B = 120 s

- **Reviewer value: highest.** It answers Q-D, the confounder. It is also the only experiment that could turn Q-B
  from "inert" into "binds only in regime X, for y% of riders" (a mechanism result).
- **Evidence it might work.** Under uncapped cost-first dispatch, 0.69–1.04% of riders accumulate more than 120 s
  without a single step exceeding it (CVP:7,22,32) [S].
- **Minimal decisive experiment.**
  - Gate 0: the option set OFF reproduces the archived U and C-30 runs on 2 cells (4 runs; V:271-276).
  - Arms: U-cf, C-30-cf, C-120-cf on the 34 T3.8 cells, 102 runs. A reduced design uses the 25 w08/w17 cells, where
    C's cost lives (T38:49-52).
  - Sealed predictions [H]:
    - C-120-cf has ≥ 3 cumulative-only prunes per 1,000 served riders (the screens imply about 7–10);
    - C-30-cf late > 60 s ≤ 4.25%;
    - U-cf shared ≥ 32.8%.
  - Kill rules as in V:277-289, plus: C-120-cf has 0 cumulative-only prunes. Then the thesis states that
    accumulation is inert even under cost-first dispatch at 120 s.
- **Optional add-on.** A per-step variant of C-120-cf (compare delta, not after, against B) gives the real
  per-step vs cumulative ablation. It is only worth running inside A2′; in the current regime the answer is already
  known.
- **Risks.**
  - T2 code in `RideBound.Algorithms/Policies`. A naive switch to the RollingCost profile drops forced-reference
    priority (R15:343).
  - Gate 0 may fail on binary drift.
  - Cost-first runtime is UNCONFIRMED; the T3.8 precedent is about 15 min per job at 6 in parallel (V row 46).
  - The outcome may be "cap loses more riders under cost-first", which is still informative.
  - Effort: about 30–45 h including the per-step variant (my estimate).

#### Candidate 2 — Strong-baseline completion on measured traffic

- **What.** C-0 (UberX-Share-like; config only, V row 48) plus M⁺-30(b), the HZ-style relaxed deadline, on the 34
  T3.8 cells.
- **Reviewer value: high for positioning, low in new information.** The predictable result is C ≈ M⁺(b) in service
  (TEX/08:1361-1362), with C-0 somewhat below C-30.
- **Minimal experiment.** 68 runs, T1. The M⁺(b) configuration key exists (TEX/08:1320-1321); that it is applicable
  to the T3.8 harness is UNVERIFIED.
- **Risk.** It deflates distinctiveness, but it is the honest answer to Q-A. Effort about 10–14 h plus about 3 h
  wall [I].

#### Candidate 3 — Density sweep (more requests per vehicle within the normaliser caps)

- **Reviewer value: medium–high for external validity** (Q-E). It also tests whether accumulation and C's cost grow
  with density.
- **Evidence.** WP9 panel B (4 vehicles, older runner):
  - b1 has 1.04% cumulative-only at 120 s (CVP:22);
  - C-30 costs −11% there against −8.9% at 8 vehicles (V:377-378).
- **Minimal experiment.** U, C-30 and C-120 at 5 vehicles on 16 cells: 48 runs, config only. The normaliser caps
  are 128 requests and 32 vehicles (R15 row 47).
- **Risk.** Structural rejections dominate, and pickup-window stops may return (TEX/08:2242-2246). It is another
  sweep in a corpus that already has six (handoff:246).

#### Candidate 4 — Fair incident-aware forecast evaluated on many held-out days (Q5)

- **Reviewer value: low–medium.** It fixes rigor concerns:
  - the vintage is a holiday plus a rain day (MLD:23);
  - there is one snow event.

  It adds no novelty.
- **Minimal decisive experiment (offline, no simulator).**
  1. **Rebuild factors.** Use Syed et al. eq. S1 (total recorded duration ÷ total free-flow duration of trips
     starting in each 15-minute bin, speed filter 1–30 m/s; MLD:72-81) on TLC yellow, Jul 2016 – Feb 2020: 44 files,
     5.35 GB (MLD:222).
  2. **Validation gate.** Reproduce the bundle's 12–18 Nov 2018 per-bin factors; seal median |relative error| ≤ 3%
     (MLD:239-241).
  3. **Information at quote time.** Only bins whose trips have finished; lag ≥ 2 bins, because bin b uses trips
     starting in b (MLD:100-102,354-355). No daily weather totals (MLD:356-357).
  4. **Methods.**
     - (H) k-week same-weekday profile;
     - (D) Gardner–McKenzie damped trend on log residuals (the protocol in `codex-work/ROUND12-REPLAY-PROTOCOL-CODEX.md`
       R2);
     - (R) a regime switch to (D) when the observed same-day deviation exceeds τ, with τ fixed on the training years.
  5. **Chronological split.** Train 2016–2017, calibrate the first half of 2018, test from mid-2018 to Feb 2020.
     Exclude 12–18 Nov 2018, which was inspected.
  6. **Incident strata.**
     - Over Jul 2016 – Feb 2020: 16 weekdays with ≥ 1 in of snow, 7 with ≥ 3 in, 49 with ≥ 20 mm rain
       (MLD:231-234).
     - How many fall in the test span: UNVERIFIED.
  7. **Metric at equal quote cost.** The simulator's dispatch-zero arrivals are a pure stretch of the factor path
     (FR:77). So pseudo-rider lateness can be computed offline as the integral under the realised path against the
     integral under the forecast path. Report Y60, early60, MAE and mean/p90 extension. Match the mean extension on
     the calibration year (ROUND12 protocol R3). Bootstrap by day.
- **Risks.**
  - Parquet needs pyarrow, which needs owner approval (MLD:243-245).
  - The validation gate may fail: random node assignment, and an unknown speed-filter distance (MLD:106-107).
  - The result is a univariate-index forecast benchmark, not ride-pooling evidence.
  - Simulating new incident days needs new world wrappers and demand files (MLD:325-331; acceptance by the medium
    preflight UNVERIFIED).
  - Effort 1.5–3 weeks (MLD:371-373).
- **The owner's 2013 idea.**
  - Feasible as data: TLC yellow exists from 2009 (MLD:136).
  - Not advisable:
    - Fielbaum & Alonso-Mora picked 15 Jan 2013, 13–15 h, because "traveling times are somewhat stable, which
      allows us to disregard unreliability due to traffic conditions" (FAM:571-576). That is the opposite of an
      incident sample.
    - 2013 → 2018 is a domain shift, whose magnitude is UNVERIFIED by me.
    - Whether the current 2013 parquet carries zone IDs or coordinates is UNVERIFIED. The 2014 – Jun 2016 parquet is
      zone-only (MLD:136,224).
    - The 2013 days cannot be simulated in this bundle without new network, demand and factor files.
  - The same-era 2016–2020 series dominates it on every count.

#### Candidate 5 — Per-step vs cumulative ablation in the current regime

- **Reviewer value: about zero.** CDC already shows the candidate classes coincide. The trajectory identity is
  near-certain [I].
- Run it only inside A2′ at B = 120 s.

#### Candidate 6 — A different promise object: arrival window, tiers, conformal interval, compensated SLA

- **Reviewer value: negative.** Prior art collides with each of them:
  - MOIA Express sells "a shorter arrival window" (V row 69);
  - SP names per-customer windows and price tiers as future work (SP:1665-1670);
  - the Lyft patent has per-match ETA-ratio limits (V row 71);
  - conformal bus-arrival windows exist (R13-SURVEY-CLAUDE item 47).
- C bounds only Σ|c|, not terminal coverage (V W5).
- High effort; it restarts the storyline.

**Ranking** (expected gain in acceptance probability, then cost; reviewer opinion [O]):

| Rank | Direction | Acceptance gain | Tier / runs | Main risk |
|---|---|---|---|---|
| 1 | **A2′** cost-first at B = 30 and 120 s (+ per-step variant) | medium–high | T2 / 4 + 102 (+34) | code, Gate 0, a null result |
| 2 | C-0 + M⁺(b) baselines on T3.8 | medium | T1 / 68 | deflation; harness key unverified |
| 3 | Density sweep | medium | T1 / about 48 | structural rejections; yet another sweep |
| 4 | Offline multi-year incident-forecast benchmark | low–medium | T3 data pipeline / 0 simulation runs | install, validation gate, out of scope |
| 5 | Per-step ablation in the current regime | about zero | T2 | redundant |
| 6 | New promise object; 2013 data | negative | T2–T3 | prior-art collision; domain shift |

### 2.4 Reviewer-position answers to the owner's Q2–Q5 (evidence separated from prediction)

- **Q2 (loosen the cap).**
  - The 1,256 are pruned candidate records, not riders. On T3.8, 148 requests were blocked only by budget; U served
    116 of them (BUD:2-3).
  - Making all 148 pass at the first attempt needs a cap of about 30 + 524.8 s, the largest smallest overshoot
    (BUD:6). At that cap C is essentially U: the U and C configs differ only in hardLimit (V row 36), and U's
    maximum per-rider sum is 590 s (R15A:9) [M/I].
  - So loosening moves along the C → U line. It wins back at most the 96-rider gap and gives back lateness: U is
    203 late > 60 s, or 137 with the forecast (R15A:9) [M].
  - Measured partial dials:
    - w07: C-120 serves 666, U 665 (W07X:25);
    - WP14r: C-120 recovers 29 of the 50 riders lost between LOCKS and C-30, at 1.47% late > 60 s (LAD:3-6).
  - Missing on the 34-cell panel: C-60 and C-120, with and without the forecast (V A3). Not "better", only another
    point on the curve.
- **Q3 (is the cumulative part useless?).**
  - On measured traffic: yes, it never acted on a recorded decision (CDC; R15A) [M].
  - Elsewhere: at most 7 decisions over the fixed-traffic and synthetic worlds, and at most 1 final rejection
    (R15:195-197) [M].
  - Its value is a worst-case per-rider guarantee that this regime never needed.
  - It would matter with several small moves per rider: cost-first dispatch, B ≥ 120 s, denser pooling (CVP screens
    above) [S].
  - No enforced measured-traffic run is in that regime.
- **Q4 (cost-first).**
  - Evidence: only the package comparison FREE vs LOCKS (shared 53.1% against 21.8%, late > 60 s 16.82% against
    2.97%; LAD:2-3) [M].
  - Prediction [H]:
    - U-cf: pooling and exposure up, lateness toward FREE.
    - C-30-cf: dispatch lateness still ≤ 30 s per rider by construction. Total lateness should stay close to C-30,
      because 72 of 76 C-30 late riders had no dispatch change (EXP:3). Served could move either way. Cumulative
      binding stays negligible at 30 s.
    - C-120-cf: the first enforced arm where accumulation should show.
- **Q5 (better forecast for incident days; 2013 data).**
  - Fair design: Candidate 4.
  - The 2013 data are feasible but the wrong sample (FAM:574-575).
  - Headroom on weekdays: 2 of 1,471 riders; snow: 34 of 601 in one event (MLD:284-298) [M].
  - Snow-day nowcasting looks promising only in a retrospective screen: 30-minute growth error 8.20/10.95% → 5.01/5.19%
    with a blend, which hurts normal days (MLD:300-317) [S].

### 2.5 My single recommendation

1. **Next step (exactly one): "A1+".** The zero-run consolidation as specified in V A1, with R15's eight corrections,
   **plus**:
   - **(i)** Re-centre the thesis contribution away from the four-family theorem. Make the headline the measured
     comparison and the ledger.
   - **(ii)** Cite and position Hörl & Zwick 2022 B, Mt-KaRRi and UberX Share. Present M⁺(b) as the HZ-style
     relaxed deadline.
   - **(iii)** State the cumulative clause as a specified guarantee that was not exercised.
   - **(iv)** Apply every §3 edit.

   0 runs.
2. **Optional (at most one), only once A1+ is drafted and the deadline is confirmed: A2′ with C-120-cf included.**
   - If the owner wants config-only runs instead, Candidate 2 is the safe substitute.
   - Do not run both.

---

## 3. What must be removed or reworded in the current LaTeX (TEX = `E:/Code/Report_INT3508/ridebound/noi-dung/`)

| # | Location | Current claim (short) | Problem (anchor) | Replace with |
|---|---|---|---|---|
| T1 | 02-tom-tat.tex:6-10, :55-59; 09-chuong5.tex:6-7 | "mọi thước đo chuẩn của ngành … không ghi nhận" / "none of the field's standard metrics … record this at all" | FAM measures exactly this, per rider: "measuring for each passenger the difference between the first announced waiting times, detours and total delay, with the real ones"; "we counted how many times did the predictions change" (FAM:1001,1011; D03:54-56) | "Throughput-oriented dispatch objectives do not price revisions. Fielbaum & Alonso-Mora (2020) measure and control them." |
| T2 | 02-tom-tat.tex:17-20, :66-69 | "Khác biệt cốt lõi so với văn liệu là … phân rã theo nguyên nhân" / "The core departure … decomposed by cause" | HZ B already uses the traffic-updated expected drop-off as the binding reference (HZ:531-541,569) | "Following the traffic-updated reference of Hörl & Zwick (2022, strategy B), we charge only the dispatch part, with a tolerance B for every rider, and audit it per rider." |
| T3 | 02-tom-tat.tex:22-26, :71-76; 05-chuong1.tex:169-182; 09-chuong5.tex:18-22, :224-231 | "chỉ ràng buộc theo hành vi không bao giờ là nguyên nhân làm rỗng tập phương án"; "Chỗ khác biệt chứng minh được của khóa luận" | (a) Holds by construction (07-chuong3.tex:292-297). (b) An HZ-style deadline max(p0+B, e) shares the property; the thesis's own M⁺(b) ≈ C (08-chuong4.tex:1319-1321,1361-1362) | Demote it to a remark, worded as: "Among the four families compared, only C never rejects the do-nothing plan, by construction. A deadline relaxed as in Hörl & Zwick (2022) shares this; in our sweep it served the same as C." |
| T4 | 02-tom-tat.tex:14-16, :63-66; 05-chuong1.tex:202-204, :213-217 | "lời hứa có biên được chứng nhận … cộng dồn và chỉ tăng"; "trần luôn được tôn trọng ở mọi cấu hình" | The cumulative clause never acted on measured traffic (CDC:4-30). Cap compliance is a correctness check, not a result | Add: "On measured traffic every budget rejection exceeded B in one move; the cumulative definition was not exercised." Move "291 < 300 …" to validation. |
| T5 | 05-chuong1.tex:64-69 | "Thứ hai, không có quy trách nguyên nhân … không ai tách phần do nhà điều hành … khỏi … đường tắc" | False: HZ B (HZ:531-541) | Name HZ 2022 as the exception, together with FAM's qualitative split |
| T6 | 05-chuong1.tex:71-73, :75-82 | "Không chỉ số nào trả lời …"; "chưa được chuyển sang lĩnh vực này" | FAM §6; Elmi 2026; TC-DARP (D03:37-56,209-213) | Delete, or scope to "classical throughput metrics" |
| T7 | 05-chuong1.tex:99-104; 09-chuong5.tex:215-222 | "về mặt toán học, không thể trở thành ràng buộc" | A strawman: FAM §6 already constrains it (FAM:957-965). The thesis itself concedes this at 05:106-111 | "Their endpoint measure is ex post; their §6 constrains the pickup promise directly." |
| T8 | 05-chuong1.tex:269-271; 09-chuong5.tex:125-128 | "biến một đại lượng trước nay chỉ đo được sau sự việc thành một ràng buộc cưỡng chế được" | Pre-decision control is prior work (D03:56; SP:489-490; FAM §6) | "We implement and audit one form of pre-decision control and measure its trade-off." |
| T9 | 02-tom-tat.tex:27-30, :78-80; 05-chuong1.tex:244-248; 08-chuong4.tex:16-17, :173-178; 09-chuong5.tex:36-37 | "phần do chính bộ điều phối gây ra bằng 89,06%" | Measured on a static-travel-time panel where drift is execution lag only (09:104-105). It is a model projection, not causal (D03:222-224) | "In the model projection on the static panel…", with the scope stated |
| T10 | 02-tom-tat.tex:46-47, :97-98 | Keywords "quy trách nguyên nhân" / "causal attribution" | D03:222-224 | "model-based attribution" |
| T11 | 05-chuong1.tex:250-253 | "trần 30 giây cắt xáo trộn xuống còn 0,17% … giá 7,13 điểm" | A package (locks + budget + fixed pickup; 08:136-138). "0.17%" collides with the forecast metric | Say it is a package comparison (H6 negative, D03:238). Rename the metric. |
| T12 | 05-chuong1.tex:261-264; 08-chuong4.tex:31 | "thước đo hai đầu của họ bỏ sót 49%"; "Thước đo của văn liệu mù ở chế độ cam kết" | By design FAM's measure is an endpoint difference; "blind" reads as a flaw | "An endpoint measure does not count revisions that cancel; under commitment 49% of revised riders show no endpoint change." |
| T13 | 09-chuong5.tex:30-32 | "điểm mới nằm ở chỗ mốc tham chiếu ngoại sinh tính được ranh giới 'ngoài tầm kiểm soát'" | HZ computes the same reference (HZ:531-535) | Delete "điểm mới"; keep the legal analogy as an interpretation only |
| T14 | 09-chuong5.tex:226-231 | "thí nghiệm có tiền đăng ký trên dữ liệu tắc đường thật xác nhận nó" | City-wide factors in simulation (V D17); exploratory; it "confirms" a by-construction property | "…is consistent with it, in simulation with city-wide measured factors (exploratory)." |
| T15 | 08-chuong4.tex:1852-1859 (table at 1835-1850) | Welfare break-even 2.7–3.4 EUR, with an unverified Geržinič value | An unverified source (the text admits it); construct mismatch: churn ≠ lateness; D03:236-245 | Remove the two unverified rows, or move the whole section to an appendix as an illustration. Use the symbolic q/m form (§1.4 C4). |
| T16 | 08-chuong4.tex:1894-1897 | "chênh lệch tỉ lệ phục vụ … phản ánh đúng tác động của cam kết" | B1 against C1 differ in locks, budget and pickup fixing (08:128-138) | "…reflects the commitment package, not computation limits." |
| T17 | Missing everywhere | — | T3.8, M⁺ comparison, forecast, ledger, padded-U frontier and the cumulative audit are absent (no "2.338" or "2.434" in TEX/*.tex) | Add them per A1+. Lead with C = M⁺ in service and the padded-U tie (R15:167-177). |
| T18 | 10-tai-lieu.tex | No Hörl & Zwick 2022, Mt-KaRRi 2026 or UberX Share | D03 §2 checklist (D03:155-164); handoff:396 already requires HZ | Add them, with the distinction stated in T2/T3 |

Also never write, whatever the chapter (inherited from V §D, still valid):
- "C serves more" (D2);
- "C gives more on-time arrivals" (D3);
- "30 s is below perception" (D5);
- "window is pooling-proof" (D6);
- "business, revenue or satisfaction shown" (D7);
- "forecast works because of C" (D8).

---

## 4. Tóm tắt cho chủ nghiên cứu (tiếng Việt, ngắn)

**Câu Q1: hướng cũ có đúng không?**
- Đúng ở chỗ **giữ một câu chuyện** và **viết lại trước, chưa chạy thêm**.
- Nhưng việc viết lại lớn hơn "một chương": bản LaTeX hiện tại (sửa lần cuối 30/9) vẫn lấy "định lý bốn họ cổng"
  làm đóng góp chính, và chưa có kết quả T3.8, dự báo, sổ ba phần.
- Hörl & Zwick (2022) đã dùng đúng ý "giờ trả cập nhật theo tắc đường làm mốc, không cho điều phối làm trễ thêm",
  để hệ thống không bị kẹt. Luận văn chưa trích bài này.

**Ví dụ thật.** Luật hạn chót có "phục hồi kiểu (b)" của chính luận văn chở bằng luật C ở 21/22 lần chạy. Vậy "chỉ
luật C không bao giờ kẹt" chỉ đúng trong bốn họ mình tự chọn.

**Câu Q3: phần cộng dồn có tác dụng không?** Trên tắc đường đo được thì **không**: 1.256/1.256 lần chặn đều do một
lần dời đã vượt 30 s. Phần này chỉ có ý nghĩa khi bộ điều phối ưu tiên chi phí và trần lớn (khoảng 120 s). Sàng lọc
cho thấy khi đó khoảng 0,7–1% khách sẽ bị cộng dồn vượt trần.

**Câu Q2: nới trần?** Nới trần chỉ là đi dọc đường từ C về U:
- tối đa lấy lại 96 khách;
- đổi lại khách trễ tăng: U có 203 khách trễ quá 1 phút, hoặc 137 nếu có dự báo.

**Câu Q4: ưu tiên chi phí?** Chưa có số đo, chỉ có dự đoán. Nếu làm thì phải có cả C-120. Chỉ chạy C-30 thì gần như
chắc chắn không thấy cộng dồn.

**Câu Q5: dự báo ngày bất thường?** Làm được theo cách công bằng:
- dựng lại hệ số tắc đường từ taxi NYC 2016–2020;
- chia theo thời gian;
- kiểm trên nhiều ngày tuyết hoặc mưa;
- so ở cùng độ dài lời hứa.

Nhưng đây là bài toán dự báo một chuỗi số, không mới. Dữ liệu 2013 của Fielbaum & Alonso-Mora được chọn đúng lúc
"không tắc đường", nên không hợp cho câu hỏi này.

**Nếu chỉ làm một việc:** viết lại toàn bộ theo "A1+", 0 lần chạy.
- Thêm: C bằng hạn chót về số khách; U có dự báo và đệm 30 s cũng đạt 2.328 khách đúng giờ; cộng dồn chưa từng
  tác dụng.
- Trích Hörl & Zwick.
- Sửa 18 chỗ ở mục 3.

Nếu còn thời gian thì thêm một thí nghiệm ưu tiên chi phí (có C-120).

---

## Appendix: verification log and unverified items

**Facts I checked myself this round:**
- HZ:495-497, 507, 531-541, 559-575.
- FAM:1-40, 125-135, 560-590, 930-1045.
- SP:1-60, 425-500, 1195-1215, 1466-1497, 1660-1675.
- SEL:271-372, the objective order. Comment at :284-286.
- Raw outputs:
  - PAD:1-64;
  - R15A:1-20;
  - CDC:1-50;
  - CVP:1-40;
  - BUD:1-10;
  - LAD:1-6;
  - EXP:1-6;
  - SHARE:1-4;
  - LOAD:1-3.
- T38 in full; FR in full; W07X in full; D03 in full.
- TEX:
  - 02 in full; 05 in full; 09 in full;
  - 07:280-330 and :495-535;
  - 08:1-200, :1313-1377, :1826-1900 and :2208-2271;
  - file dates by `ls`;
  - grep for T3.8 numbers and for Hörl & Zwick: no matches.

**My own arithmetic.**

| Quantity | Value | Inputs |
|---|---|---|
| Δlate between C + forecast and padded U, at 60 s and 120 s | 96 and 68 | R15A:7,9 |
| Break-even q/m | 1.00 and 1.41 | from the row above |
| Shared passenger-minutes, C against U | −53% (1,388 against 2,962) | EXP:2-3 |
| Served lost by C | 96 / 2,434 = 3.9% | R15A |
| Late > 60 s per served rider: cap lever against forecast lever | −5.09 pp against −2.71 pp | PAD:4,12,25 |

**UNVERIFIED by me:**
- Which recovery rule the T3.8 M⁺ arm used for every run.
- Whether the M⁺(b) key works in the T3.8 harness.
- Whether the medium preflight accepts new demand and factor days.
- The layout of the 2013 TLC parquet.
- The magnitude of the 2013 → 2018 domain shift.
- Cost-first runtime.
- The FleetPy ≈ 1.33 occupancy figure: Codex checked it (R15 row 20); I did not open the PDF.
- Committee standards.
- The deadline.
