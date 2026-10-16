# Round 13 fact pack (neutral; read by BOTH Claude-side agents and Codex)

Written by Claude (main session) 2026-10-09 ~23:55. Every number below has a saved script + output; paths given.
Background in Vietnamese: `E:/Code/Report_INT3508/BAN-GIAO-PHIEN-2026-10-09.md` (full handoff; sections 3-5 = storyline,
results, errata). Claim boundary: `C:/Code/RideBound-noworse/docs/03-related-work-and-claim-boundary.md`.

## 0. Why this round exists: the owner's questions (translated faithfully)

The owner (thesis author, UET/VNU, undergraduate thesis, deadline reportedly mid-November 2026, UNCONFIRMED) asked:

- **O1.** "C-120 on measured traffic: I remember we already ran it." (Answered in section 2: yes, partly.)
- **O2.** "If the thesis is ONLY rule C (the promise is bounded by system-caused changes), what does that metric give the
  business/operator side? Would other researchers want to optimize it?"
- **O3.** "With forecast-based promising added, what is the answer to O2? What can I say about the thing RIDERS care
  about? Is it really useful and a contribution?"
- **O4.** "If rule C is widened to 120 s, what is the per-rider cumulative budget use?" (Answered in section 2.)
- **O5.** "For ML, can we find more data to train on?"
- **O6.** "Given the requirement — benefit for the business side + other researchers would want to optimize it + either a
  relatively new method, or optimizing one part / one algorithm in our system pipeline that yields a useful trade-off on
  some dimension — is there a better direction? Or keep the current direction? Or promise a different kind of thing?"
- The owner pointed to papers in `C:/PDF/Paper/` and to one example of the "algorithm optimization" style they mean:
  `C:/PDF/Paper/21020283-3476 (1).pdf` — a 2024 UET undergraduate thesis "Nghiên cứu tối ưu lịch trình cho bài toán chia
  sẻ chuyến đi" (schedule optimization for ride-sharing). Its abstract: ML predicts ride demand per time window and
  location from historical data; the system pre-forms pooled groups per taxi from predicted requests, then assigns
  online requests into those pre-formed groups, aiming at lower cost and more served requests. Its evaluation figures
  (list of figures): requests served, taxis needed, cost per served request, total time to serve 200 requests. NOTE: the
  PDF's Vietnamese text extracts with broken diacritics (missing ToUnicode); read pages visually if needed.

## 1. The current thesis core (agreed with Codex in rounds 1-12)

Ride-pooling promised drop-off time drifts for three causes, each handled at its own place:
1. System inserts more riders -> **rule C**: per rider, sum of |c| over promise revisions <= B (B = 30 s now), where
   v = previously published promise, e = old plan re-timed at new speeds, p = new promise, x = e - v (traffic),
   c = p - e (dispatch), z = p - v (visible). Summing signed c + x gives the old deadline rule M+; |c + x| gives V.
2. Predictable congestion -> **forecast promise**: add historical 15-min congestion growth to the first quote.
3. Unexpected congestion -> **three-part ledger** per rider (not automatically "excused").

Key results (sources in handoff section 4):
- T3.8, measured traffic, 34 cells x 108 requests (3,672): served U 2,434; C-30 2,338; M+-30 2,338; V-30 2,336.
  Forced (non-normal) decisions: C-30 0%, M+-30 41.3%, V-30 53.8%. Riders whose promise the rule itself broke: C 0%,
  M+-30 14.5%, V-30 21.6%. Cost of C-30 vs U: -96 riders = 2.6 pp of requests (3.9% of U served).
- Lateness vs first promise (34 cells, rider-pooled): >1 min U 8.34%, C-30 3.25%, C-30+forecast 0.43%; >5 min U 0.74%,
  C-30 0; max U 11 min, C-30 3.9 min, C-30+forecast 1.9 min.
- Forecast family A (21 weekday cells, cell mean): late>60 s 6.01% -> 0.17% under C-30; U 9.72% -> 3.90%. Promise
  only 7.4-13.7 s longer. Uniform padding at equal cost much worse; padding 120-180 s removes lateness but 97-99.5% of
  riders arrive >1 min early. Snow afternoon (15 Nov): 92.5% of lateness unexpected; forecast only 7.19% -> 5.94%.
- WP14r ladder (fixed traffic, 16 cells): FREE served 94.3%, shared 53.1%, drop-exposed 23.8%, late>1 min 16.82%;
  LOCKS(=U) 91.7/21.8/3.9/2.97%; C-120 90.5/19.4/2.6/1.47%; C-60 89.1/17.3/1.3/0; C-30 88.8/15.7/0.4/0.
- ML pilot (sealed, + amendment A1): fixed learners with simple features gave no qualifying gain; none matched C-30's
  reliability. Only 8 days of traffic data (11-18 Nov 2018) exist in the FleetPy bundle.
- Why C-30 rejects riders: 148 requests blocked only by a co-rider's budget (U served 116 of them; median overshoot
  110 s); only 2/148 blockers had spent budget earlier. A budget proportional to the co-rider's direct trip time, at
  equal mean budget, unblocks more (60 s: 11 -> 30; 120 s: 59 -> 89), first-order screen ignoring cascades.
- Simulation limits: 108 requests / 8 vehicles per cell, ~0.54 riders per vehicle on average (FleetPy 2026 paper on
  the same data reports ~1.33 with 21,400 requests / 180 vehicles); 0 s dwell; one city-wide traffic factor; tool caps
  128 requests / 32 vehicles / 96 nodes; trips selected are shorter than eligible trips.

NOT claimable as novel (docs/03 + surveys): dynamic insertion, ETA limits, reassignment, route similarity,
least-commitment, time consistency, rider satisfaction, forecast-based quoting (Google, Uber DeeprETA, DoorDash, Lyft,
Ele.me, TCRP 113, airlines), ML ETA, "predictability as a design parameter" (Leonardi et al. 2024, arXiv 2411.11899),
learning pooled outcomes from FleetPy simulation (Ding, Dandl & Bogenberger), Hörl & Zwick 2022 strategy B
(close to rule C but only for riders about to be late, not cumulative, no ledger), Schulz & Pfeiffer 2026 deadline
component (fixed travel times, acceptance probability e^(-mu*RD), deadline 900 s).

Permitted contribution (narrow): (1) per-rider cumulative dispatch-change budget + v/e/p ledger, implemented and
verified; (2) vs deadline: same riders, never forced to break; vs free pooling: removes pooling-caused lateness at a
measured rider cost; (3) exploratory: under C the pooled promise becomes a traffic-forecasting problem, simple forecast
suffices on weekdays; C and forecast are complementary; at equal quote length "fewer changes" gave more reliable
promises than the tested learners (do not overstate).

## 2. New this session (zero-run re-analysis of existing transcripts)

**O1 answer.** C-120 on measured traffic EXISTS: `C:/RideBoundData/research/tier3-w07-v1` (C-30/60/120/300, U, M+,
V-30; 8 cells, 07:00-09:00, 12-13 Nov) and `tier3-w07x-v1` (C/M+/V at 90/150/180/240). Report:
`E:/Code/Report_INT3508/ridebound-scratchpad/tang3/w07x/W07X-REPORT.md`. Served (864 requests; U 665): C-30 660,
C-60 661, C-90 664, C-120 666, C-150 666, C-180 666, C-240 665, C-300 665. M+ forced 58.6/35.5/13.0/6.6/6.8/2.8/1.7%
at 30/60/90/120/150/180/240 s; C never forced. NOT run: C-120 on the full 34-cell T3.8 panel (other windows).
Also C-120 exists on synthetic worlds (`E:/RideBoundData/research/tier3-sweep-v1`, 13 runs) and fixed traffic (WP14r).

**O4 answer** (`claude-work/budget_use_check.py` -> `claude-work/budget-use-check-2026-10-09.txt`). S = per-rider
sum of |c| on the drop promise; pickup dispatch part is 0 for every rider in every arm (pickup locked at confirmation).

| Population, arm | riders | with S > 0 | S among exposed: mean / median / max | riders using >= 90% of B | riders with >= 2 nonzero changes |
|---|---|---|---|---|---|
| w07 U (no cap) | 665 | 11 (1.65%) | 74.7 / 68.3 / 208.2 s | — | 0 |
| w07 C-30 | 660 | 2 (0.30%) | 6.0 / 2.0 / 10.0 s | 0 | 0 |
| w07 C-60 | 661 | 3 (0.45%) | 18.0 / 10.0 / 41.9 s | 0 | 0 |
| w07 C-90 | 664 | 7 (1.05%) | 49.7 / 68.3 / 86.9 s | 1 | 0 |
| w07 C-120 | 666 | 9 (1.35%) | 56.2 / 68.3 / 96.7 s | 0 | 0 |
| w07 C-150, C-180 | 666 | identical to C-120 | | 0 | 0 |
| w07 C-240, C-300 | 665 | identical to U | | 0 | 0 |
| T3.8 U (34 cells) | 2,434 | 174 (7.15%) | 137.7 / 117.0 / 590.1 s (p90 260.7) | — | 12 (0.49%), max 3 |
| T3.8 C-30 (34 cells) | 2,338 | 33 (1.41%) | 10.9 / 8.3 / 29.2 s | 4 (0.17%) | 0 |

T3.8 U riders who would exceed a cap: 30 s 5.92%, 60 s 5.34%, 120 s 3.53%, 300 s 0.49%.
**Reading:** in this low-load simulation the *cumulative* part of rule C is almost never exercised: no rider under any
C cap had two nonzero dispatch changes; C acts as a per-insertion cap. Accumulation would matter only in denser pooling
(WP14r FREE arm: 23.8% of riders drop-exposed). This is a weakness to address honestly, or an opportunity.

## 3. Papers the owner supplied (`C:/PDF/Paper/`, 13 PDFs)

1-s2.0-S0191261522000716-main.pdf; 1-s2.0-S0965856426000662-main.pdf; 21020283-3476 (1).pdf (example thesis);
2508.04811v1.pdf; BregniA._DAvinoM.SchiraldiM.M.pdf; FreezingtheMPSMgtScipaper.pdf; Networks - 2014 - Kovacs - Vehicle
routing problems in which consistency considerations are important A survey.pdf;
OperationalEffectsofServiceLevelVariations-publication151005.pdf; Scale_analysis_for_on-demand_ridepooling_systems_a.pdf;
Unreliability_in_ridesharing_systems_Measuring_cha.pdf; Value_of_time_and_reliability_for_urban_pooled_on-.pdf;
s00291-025-00812-3.pdf; s00291-026-00847-0.pdf. (pdftotext: `C:/Program Files/Git/mingw64/bin/pdftotext.exe`.)

## 4. Hard constraints for everyone

- Zero hallucination: every factual claim cites `file:line`, or a URL plus a short verified quote. Unverified = say so.
- No simulation runs, no builds, no edits outside your own output folder. Never touch `E:/Code/RideBound`,
  `E:/Code/RideBound-deadline`, the thesis `E:/Code/Report_INT3508/ridebound/`, or the internship report.
- Proposals must respect the claim boundary above; say exactly what is new and what is prior work.
- Feasibility tiers: (T0) analysis of existing transcripts only; (T1) new runs with existing code, config only;
  (T2) core code change (C#, Domain/Application, tests, worktree); (T3) new data pipeline. Deadline ~5 weeks, unconfirmed.
- The owner wants ONE storyline. A proposal may replace, extend or keep the current one, but must say which.
