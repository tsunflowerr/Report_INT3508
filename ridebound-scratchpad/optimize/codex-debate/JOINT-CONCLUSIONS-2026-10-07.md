# Joint conclusions, rounds 4–6 (2026-10-07)

**Participants.**
- Claude (Opus 5.5), with two Claude literature agents.
- Codex gpt-6.1-sol, reasoning effort ultra, in session `01a11056-6e20-7ef1-b6e4-fe375272c630`. From round 4 Codex
  had workspace-write access limited to `codex-work/`.

**Sources.**
- Codex: `codex-work/FINAL-JOINT-POSITION-CODEX.md` and `codex-work/ROUND6-VERIFICATION-CODEX.md`.
- Claude: `claude-work/IDEAS-CLAUDE.md` and `claude-work/REVIEW-OF-CODEX-BY-CLAUDE.md`.

**Cross-checks.** Every number below was produced by one side and reproduced by the other with separate code:
- Codex `round5_reproduce.py`: all required rows match.
- Codex `round6_verify_backtest.py`: 60 of 60 rows match.

Nothing in the thesis, docs/18 or docs/19 has been edited.

## Answers to the owner's four questions

### 1. Why are so few riders delayed by pooling? Is the scale too small?

**Sharing and being delayed by pooling are different things.**
- Under U, 22.8% of served riders share the vehicle at some point (`pooling-share-2026-10-06.txt`).
- Only 7.1% have their drop promise moved by a later dispatch change (`exposure-check-2026-10-06.txt`). Much sharing
  is already planned inside the first promise.
- The first promise contains the whole planned trip: on average 14.1 min, of which 6.4 min is waiting
  (`burden-and-rescale-2026-10-06.txt`).

**Real example.** Rider `rq-30b7e083c7b` in cell `d20181115-s10-r1-w07`
(`report-extras/example-rider-2026-10-06.txt`):
- booked at 7:11:56 and was promised 7:34:51, which already included the 10.5 min wait;
- picked up at 7:22:30 and arrived at 7:38:02, 190.5 s late;
- the late seconds appeared at the traffic steps of 7:15 and 7:30;
- with the forecast display, the promise shown would have been 7:37:44, only 17.6 s off.

**The experiment is small and sparse.**
- Each cell has 108 requests, 8 vehicles, 96 nodes and 0 s dwell.
- The selected trips are shorter than the eligible ones.
- The load is x = 0.81 < 1 (Molkenthin et al. 2020: below 1, riders can in principle be served one by one).
- Mean occupancy is 0.54 passengers per vehicle, idle time included (`claude-work/load-and-occupancy-2026-10-07.txt`).

**Same dataset, different setting.** The only study on the same data is FleetPy, ETRR 2026
(`claude-work/pdf/fleetpy-etrr-2026.txt:422-424`):
- 21,400 requests, 180 vehicles, 480 s maximum wait, 30 s boarding;
- it reports 90% served and occupancy of about 1.33;
- it reports no shared-ride share.

The "90% shared" figure comes from Alonso-Mora 2017: full NYC 2013 demand, 1,000–3,000 vehicles, a different dataset.

**Status.** Scale and density are a plausible contributor, not a proven cause.

### 2. Is forecast-aware promising new? What is our forecast? Is the traffic real?

**It is not new.** Prior art includes:
- Google's time-of-day historical baseline;
- Uber DeepETA, which uses quantiles and is separated from routing;
- Ele.me's "service promise";
- transit percentiles (TCRP 113) and airline block times;
- Schilde et al. 2014, who use historical time-of-day speeds in dynamic DARP.

**Our forecast** is the plain historical average of 2–3 earlier same-kind days, per 15-minute bin, applied to the
remaining trip time, and it never shortens a promise (`optimize/display_layer.py:1-20`).

**The traffic factors are real data.** They are derived from recorded NYC TLC trip times (FleetPy README:28,34). The
simulation applies them as one citywide multiplier, anchored at the 00:00 level.

**Residual contribution.** At most, audited per-rider accounting plus a measured frontier. Global novelty is not
established.

### 3. Should the ledger accumulate system and traffic changes together?

**Our notation**, verified in `audit_vep.py:99-125`:
- v = previous publication;
- e = the old plan re-projected under the new travel times;
- x = e − v, the traffic part;
- c = p − e, the dispatch part.

**What a combined budget turns into.**
- Signed Σ(x + c) telescopes to p_n − P0. Checking it at every step **is** the existing fixed deadline (Mplus).
- Σ|x + c| **is** the existing V rule.
- Σ(|x| + |c|) and Σmax(0, x + c) are other contracts, with no established novelty.

**So yes, it collides with the essence of the deadline.**
- Traffic alone can exhaust such a budget: V-30 was forced in 53.8% of decisions and Mplus-30 in 41.3%, against 0% for
  C-30.
- Putting the forecast inside the dispatcher still left Mplus-30F forced in 47.6%.

**Agreed structure.**
- Anticipated traffic goes into the displayed promise.
- C caps the dispatch part.
- Everything else is reported as a residual. A forecast miss is not automatically "excusable".

**Hybrid C-30 plus a customer deadline S.** We screened it. At S = 120 s it would be reached by only 11 riders (0.47%),
all through traffic alone; at S = 60, by 79, of whom 75 are traffic-only (`claude-work/hybrid-gate-screen-2026-10-07.txt`).
The decision was to defer it.

### 4. What can be optimized, and what is the trade-off?

There are two ways to make promises reliable:
- **the cap**, which costs riders: C-30 completes 96 fewer of 3,672 requests (`T38-REPORT.md:49`);
- **padding the promise**, which costs promise length and accuracy.

**Sealed chronological backtest.** Plan `claude-work/CALIB-BACKTEST-PLAN.md` (SHA-256 6175d2c1…), output
`calib-backtest-2026-10-07.txt`, verified by Codex.

Train on 14/11, test on 15/11 and 16/11, with rules frozen on the training day:

| policy | timely riders | completed | mean extra promise | arrive within ±60 s of the promise |
|---|---|---|---|---|
| C-30 + forecast | 1,031 | 1,032 | 17.1 s / 10.7 s | 100% / 99.7% |
| U + frozen room pad (E = 60) | 1,031 | 1,061 | 63.3 s / 59.5 s | 84.3% / 67.0% |

**The fair claim.** On these previously inspected weekdays, U with padding matches C-30 + forecast in timely riders
and completes 29 more requests. It cannot match C-30 + forecast's accuracy with short quotes.

**Not claimed:**
- that padding can never replace the cap;
- any welfare optimum, because there is no booking model.

**The room-based pad is withdrawn.** The sealed prediction P1 was false, P2 true and P3 true; the kill criterion
fired. Room behaves like a trip-length pad.

## Proposed next steps (each batch needs the owner's approval; predictions sealed first; AC power only)

| Step | Work | Jobs |
|---|---|---|
| 0 | Finish zero-run audits: quote cost for all promised riders, visible variation, common riders, incidents | 0 |
| 1 | Anchor validation: U, C-30 and Mplus-30 on six cells, with travel times anchored at the window start | 18 |
| 2 | Budget sweep C-60 and C-120 on all 34 test cells, to buy back the 96 riders while keeping accuracy; C-300 is conditional (+34) | 68 |
| 3 | Optional density pilot: needs extending the normalizer limits (≤ 128 requests, ≤ 32 vehicles, ≤ 96 nodes) first | 12 (+6) |
| — | Deferred: hybrid, fleet-only tuning | — |

## Corrections owed to existing documents (not applied)

1. Add the limitations: the 00:00 anchor (all cells), shorter selected trips, 0 s dwell versus FleetPy's 30 s, load and
   occupancy.
2. Fix the v/e/p wording wherever "v = first promise moved by traffic" appears. The correct definition is
   `audit_vep.py:99-125`.
3. The display gain is rule-agnostic; the forecast is not novel.
4. Report "timely" always together with two-sided accuracy and early arrivals.
5. Carry over the round 1–3 corrections listed in `JOINT-CONCLUSIONS-2026-10-06.md` §5.
