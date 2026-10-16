# Claude's ideas, round 4 (2026-10-07)

- **Inputs.** Surveys `SURVEY-S1-pooling-and-tradeoffs.md` (19 sources) and
  `SURVEY-S2-forecast-promising-and-budgets.md` (28 entries), written by two Claude literature agents. Zero-run
  replays `cap_vs_pad_frontier.py` and `slack_bounded_pad.py` (outputs `*-2026-10-07.txt` in this folder).
- **Independence.** I did not read `codex-work/` before writing this file.

## 0. Notation correction (my error in rounds 1–3)

Per revision entry, in `tang3/evidence/audit_vep.py:99-125`:
- `v` is the **previously published promise**;
- `e` is the **exogenous projection**: the previous plan re-projected under the new travel times;
- `p` is the new published promise.

So x = e − v is the traffic part, c = p − e the dispatch part, and z = p − v the visible change. The labels I used
were right. My sentence "v = first promise moved only by the world" was wrong. Sums over a rider's revisions telescope:
Σz = p_last − p_first.

## 1. Answer to the owner's question 3: a combined c + x budget

- A budget that accumulates both parts is a cap on visible change.
  - Cumulative |z|: that is our `V` arm.
  - Signed: it telescopes to p_t − p_0 ≤ B, which is the fixed deadline `Mplus`. This is also Schulz & Pfeiffer's
    l = B (S2 survey §3).
  - So yes: it **is** the deadline family, not a new rule.
- Our runs show the structural cost. With naive promises, `V-30` was forced in 53.8% of decisions and `Mplus-30` in
  41.3%; C-30 never was (`T38-REPORT.md` §3). With forecast-aware promises in the dispatcher, Mplus-30F was still
  forced in 47.6% (`FORECAST-REPORT.md:134`). A combined budget therefore keeps the deadline's weakness: exogenous
  delay alone can exhaust it.
- **The principled middle is the 37.131 structure** (S2 survey S24, S25): charge the operator for what it controls
  or could anticipate, and excuse what it could not.
- **This already exists in our pieces, in the right places:**
  1. **anticipated traffic** goes into the promise (the forecast display layer);
  2. **dispatch** is capped by C's budget on |c|;
  3. **unanticipated traffic** is passed through and recorded in the ledger as excusable.

  Adding x to C's budget would move us back to the deadline family. I therefore propose to keep the promise as
  "C + display + three-part ledger" and to say explicitly that the excusable-delay idea is regulatory prior art.

## 2. Ideas, ranked

### I1. Allocate the promise pad by insertion room (zero-run evidence exists now)

**What is optimized.** The allocation of a promise pad across riders, at a given mean pad. The decision variable is the
pad rule. The risk signal is known at promise time:

  room = first pickup promise + maxRideTime − first drop promise

Why this signal works:
- Pickup promises are never moved by dispatch in any arm (`exposure-check-2026-10-06.txt`).
- The max-ride constraint bounds how far a later insertion can push the drop.

**Evidence.** `slack-bounded-pad-2026-10-07.txt`.

U: dispatch exposure and naive lateness rise steeply with room.

| room | riders | exposed | Y60 |
|---|---|---|---|
| < 60 s | 342 | 0.6% | 2.3% |
| 60–120 s | 590 | 1.7% | 3.1% |
| 120–240 s | 942 | 7.0% | 7.6% |
| ≥ 240 s | 560 | 17.1% | 18.8% |

U, all on top of the forecast display ("fc"):

| policy | Y60 | mean extension | arrive > 60 s early | timely (of 3,672) |
|---|---|---|---|---|
| fc + uniform 60 s | 3.57% | 67.2 s | 42.4% | 2,347 |
| fc + min(60 s, 0.5·room) | 3.57% | 57.7 s | 26.7% | 2,347 |
| fc + uniform 120 s | 1.97% | 127.2 s | 94.4% | 2,386 |
| fc + min(180 s, 0.5·room) | 1.97% | 90.2 s | 55.3% | 2,386 |

At equal reliability, the room-bounded rule needs about 10–37 s less mean pad and gives far fewer pessimistic quotes.

**The cap-vs-pad frontier** (`cap-vs-pad-frontier-2026-10-07.txt`; timely = served and A − D ≤ 60 s, per 3,672
requests):

| configuration | timely | rate | mean extension |
|---|---|---|---|
| U naive | 2,231 | 60.76% | 0 s |
| C-30 naive | 2,262 | 61.60% | 0 s |
| C-30 + fc | 2,328 | 63.40% | 7.4 s |
| U + fc + 30 s | 2,328 | — | 37.2 s |
| U + fc + 60 s | 2,347 | — | 67.2 s |
| U + fc + min(180 s, 0.5·room) | 2,386 | — | 90.2 s |

- The ceiling for C-30 is 2,338, its served count.
- Reading: **below about 40 s of quote inflation the cap wins; above about 60 s, no cap plus a room-bounded pad
  wins.** The cap buys reliability with riders; the pad buys it with promise length.

**Trade-off to report.** Timely completions against mean quote inflation, with early-arrival share as a third axis.
Model limit: longer quotes cost bookings (Schmidt et al. 2026, arXiv 2609.11950 [abstract only]), and our simulation
has no booking response. As an illustration only, Lyft's wait elasticity of −0.0427 (`SOURCES-2026-10-05.md:55`) is
for pickup ETAs, not drop promises.

**Novelty.**
- Already published: buffer and supplement allocation (TCRP 113, Kroon 2008), quantile and newsvendor promises
  (Salari 2022, Deshpande & Arıkan 2012), and ETA layers separated from routing (DeeprETA).
- Not found in our ~47 sources: using the max-ride insertion room of a pooled trip as the risk signal for the
  displayed drop promise. That is a search result, not proof of absence.
- Claim it at most as "an application of buffer allocation to pooled promises, evaluated in replay".

**Falsifiable.**
- Prediction: under leave-one-day-out fitting of (k, a), the room-bounded rule beats the uniform pad at equal mean
  extension on held-out days.
- Kill criterion: at equal mean extension, held-out Y60 is no lower than the uniform pad's in at least 3 of 5 days.

### I2. Cap budget sweep to complete the frontier (runs)

**What is optimized.** The budget β of rule C, jointly with the I1 pad rule. The objective is to maximise timely
completions subject to mean quote inflation ≤ E, for E ∈ {15, 30, 60} s.

**Why.** On the 34 test cells we have only β = 30 and no cap. On 8 dev cells at 07–09 h, C-120 served 666 vs U 665
vs C-30 660 (`tang3/w07x/W07X-REPORT.md:20-30`). But the T3.8 service cost sits in the 08 and 17 h windows (−39 and
−52 riders), where no β > 30 was run.

**Runs.** C-60, C-120, C-300 on the 34 test cells, reusing the T3.8 runner, wrappers and configs:
- 102 jobs. T3.8's 170 jobs took about 7 h, so this is about 4–5 h on AC power.
- Pads are then replayed on top; no extra runs are needed for them.

**Prediction to seal.**
- Served rises monotonically with β, and C-120 recovers at least half of the 96-rider gap.
- At E = 30 s, the best (β, pad) beats both C-30 + fc (2,328) and U + fc + pad.

**Kill criterion.** If C-120 recovers less than a quarter of the gap, or its post-promise tail returns (Y120 > 1%), the
cap is not a tunable lever at this scale.

**Novelty.** None for budget sweeps (Schulz & Pfeiffer sweep l). The value is the frontier itself, which reviewers
expect (S1 survey §S3).

### I3. Scale sensitivity (runs; the strongest threat to validity)

Every density source in the S1 survey says pooling grows steeply with demand density, and our cells are 16–25× sparser
than the only study on the same data (FleetPy ETRR 2026: 21,400 requests/day, 180 vehicles).

**Proposal.** Rebuild a small set of fixtures with demand and fleet scaled together, e.g. ×2.5 and ×5 (270/20 and
540/40), on 6 cells. Run U and C-30, then measure exposure, shared share, the cap's served cost and Y60.

**Prediction.** Exposure and the cap's served cost both rise with density. That is what would make the rule matter
more, not less.

**Risks.**
- Runner time grows with fleet × requests: not checked.
- Fixture generation needs the normalizer. It must not be built inside the worktree a job uses
  (`E:/Code/RideBound-deadline`), so it would use `C:/Code/RideBound-noworse` instead: not checked.

### I4. Excusable-delay KPI (zero-run, reporting only)

- Report per rider: dispatch + anticipated-traffic lateness (the operator's account) against unanticipated (excusable),
  mirroring 37.131.
- No new rule and no novelty claim. It turns the ledger into a contract-facing measure.

## 3. What I would drop

- "Forecast-aware promising" as a contribution. It is prior art: Google time-of-day baseline, Ele.me promised times,
  TCRP 113 percentiles.
- Any credit to rule C for the display gain. Mplus-30 and V-30 reach the same 0.17%.
- Forecast inside the dispatcher (Family B rejected).
