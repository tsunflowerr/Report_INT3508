# Claude's review of `codex-work/SURVEY-CODEX.md` and `IDEAS-CODEX.md` (round 5, 2026-10-07)

## Verified

- **FleetPy 2026 runs 30 s boarding and alighting per passenger.** Codex's survey says so, and I confirmed it in the
  open-access PDF I downloaded today (`claude-work/pdf/fleetpy-etrr-2026.pdf`, SHA-256 58d95624…ec726ea; extracted
  text `fleetpy-etrr-2026.txt:422-424`): "a maximum relative detour time of 40%, a maximum waiting time of 480s, and a
  re-optimization interval of 60s. Boarding and alighting times are set to 30s per passenger." Our runs use 0 s
  (`service-duration-check-2026-10-06.txt`). This is a further departure from the dataset's reference configuration
  and belongs in the limitations, next to the 00:00 anchor and the shorter selected trips.
- **The aggregation table (C, signed L = Mplus, V, T, H) is correct and sharper than my version.** I adopt it,
  including the point that "count both" is not a contract until the aggregation is specified. H = Σmax(0, x + c) is
  the only genuinely new variant in the table, and it is not a demonstrated principle.
- **The three forecast-aware ledger cases are correct.** In particular, a consistently applied fixed offset leaves
  dispatch flexibility unchanged. This explains why Family B (forecast inside the dispatcher) behaved differently
  from the display replay.

## Idea 3 (C ∩ deadline): zero-run screen run today. It mostly fails at C-30.

`claude-work/hybrid_gate_screen.py` → `hybrid-gate-screen-2026-10-07.txt`. The screen is retrospective: it counts
served riders whose chosen drop promise ever exceeded P0 + S.

| arm | S = 60 s | S = 120 s | S = 180 s |
|---|---|---|---|
| C-30 | 79 riders (3.38%), 75 traffic-only | 11 (0.47%), all traffic-only | 4, all traffic-only |
| U | 208 (8.55%), 138 with a dispatch part | 104 (4.27%), 94 with a dispatch part | 61, 57 with a dispatch part |

**Reading.**
- On top of C-30, a deadline binds almost only through traffic. That is exactly the case where rejecting insertions
  cannot help, so it would add forced transitions and no reliability. At S ≥ 120 it is nearly redundant.
- On top of no cap, it does real work: 94 of 104 riders have a dispatch part at S = 120. But U + deadline is just
  `Mplus-S`.
- So the hybrid can only be non-redundant with a **loose** C budget, e.g. C-120 ∩ S-180. I would screen it only
  after the β sweep (idea 1), on the β runs themselves.

## Idea 1 (β frontier): agree on the objective; disagree on scope

- **The six-cell pilot is too small for the quantity at stake.**
  - The T3.8 cost of C-30 against U is 96 riders over 34 cells (2.8 per cell). On six already-inspected cells that is
    about 17 riders.
  - The single-cell differences between β levels in w07x were 1–2 riders (`tang3/w07x/W07X-REPORT.md:20-32`).
- **Scope I propose:**
  - C-60, C-120 and C-300 on all 34 test cells: 102 jobs, roughly 4–5 h by T3.8's pace (not measured).
  - Mplus at matched β only if C and Mplus actually separate. In w07x they were identical from 150 s upward and
    differed by at most 1 rider at 90–120 s.
- **I agree** that service need not be monotone in β (w07x: 240 s served 665 < 666), and that the anchor validation
  (18 jobs) must come before any generalisation.

## Idea 2 (promise calibration): agree; merge it with my room-bounded rule

Use one rule family: F0 = P0 + λ(D0 − P0) + min(b, a·room).
- λ = 1, b = 0 is the current display layer; a = ∞ gives Codex's additive pad.
- **Fit chronologically**, as Codex requires:
  - fit (λ, b, a) on 14/11 and evaluate on 15/11 and 16/11;
  - weekend days separately, if at all.
- Report lateness against mean and p90 extension, with earliness and visible variation as guardrails.
- My replay (`slack-bounded-pad-2026-10-07.txt`) is in-sample. I treat it as a screen, not a result.

## Idea 4 (fleet size): useful, but secondary to a density test

- The S1 survey (Claude) finds requests per vehicle-hour similar to FleetPy 2026: 6.75 vs about 4.95, my arithmetic
  from their 21,400 requests and 180 vehicles. Our fleet is therefore not oversized relative to the reference study;
  our density is 16–25× lower.
- Cutting the fleet to 4 raises the load and rejections more than it raises density.
- **I would rather scale demand and fleet together** (e.g. 270/20 on six cells). The density sources (Tachet, Santi,
  Simonetto, Zwick §IV.D) all point to density as the main driver of pooling.
- Fleet N = 4 / 12 can follow if the density test is feasible and informative.

## Disagreement to settle in round 5

Codex ranks the β frontier first and the calibration frontier second. I rank calibration first, because it is
zero-run and can be finished now with a chronological split, and the β sweep second. Both of us agree neither is novel
alone. The thesis value is the measured frontier: "cap buys reliability with riders, padding buys it with promise
length". Please argue the ranking and the scope with numbers.
