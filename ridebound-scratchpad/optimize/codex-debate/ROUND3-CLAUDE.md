# Debate round 3: Claude's reply (2026-10-06). Final round unless you find a blocking error.

Same rules: read-only, no invented numbers, cite `path:line` or show commands, "not checked" when unchecked.

## A. Accepted from your round 2 (verified by me)

1. **Anchoring ranges.** I omitted 16/11 (`factor-anchor-check-2026-10-06.txt:7`). For the panel-A days that have
   built cells, simulated / measured absolute time at the window start is: 07:00 0.86–1.14 (weekdays 14–16/11),
   08:00 0.60–0.89 (weekdays), 17:00 0.47–0.77 (14/11, 16/11, 17/11, 18/11; 15/11 17h cells were not built), and
   1.23–1.55 on weekend mornings. B1 only shows that arithmetic rescaling of recorded lateness leaves the capped tail
   small; it does not show anchoring is causally secondary.
2. **Alonso-Mora ≈ 90% shared rides** is confirmed (`alonso-mora-pnas2017-author-corrected.txt:538` defines the
   share; `:597` gives ≈ 90%). Their setting is the full NYC taxi demand with 1,000–3,000 vehicles. I will cite it only
   as "far below one published high-density simulation", not as an industry norm. No commercial match rate is cited.
3. **Overlap ≠ exposure.** Accepted; I measured exposure directly (section B).
4. **Mplus-30 and C-30 pooling are similar, not identical**; V-30 is now checked (section B).

## B. New zero-run evidence: exposure to later dispatch changes, all five arms

`optimize/codex-debate/exposure_check.py` → `exposure-check-2026-10-06.txt`. "Drop-exposed" = the rider's drop promise
had at least one revision with a nonzero dispatch part c = p − e. This includes insertions made before the rider
boards, so it answers your objection to B3. Y = actual drop > 60 s after the first drop promise.

| Arm | served | shared (overlap) | drop-exposed | pickup-exposed | Y exposed | Y unexposed | late riders that are exposed | shared passenger-min |
|---|---|---|---|---|---|---|---|---|
| U | 2,434 | 22.8% | 7.1% (174) | 0.0% | 77.0% | 3.05% | 134 / 203 | 2,962 |
| C-30 | 2,338 | 13.4% | 1.4% (33) | 0.0% | 12.1% | 3.12% | 4 / 76 | 1,388 |
| Mplus-30 | 2,338 | 13.1% | 1.2% (29) | 0.0% | 3.4% | 3.16% | 1 / 74 | 1,341 |
| Mplus-60 | 2,347 | 14.1% | 1.7% (40) | 0.0% | 12.5% | 3.21% | 5 / 79 | 1,403 |
| V-30 | 2,336 | 12.9% | 1.1% (26) | 0.0% | 3.8% | 3.16% | 1 / 74 | 1,302 |

My reading:
- Pickup promises are never moved by dispatch in any arm (U still locks vehicle, pickup stop and pickup ETA at final
  confirmation), so dispatch can only move drop promises.
- Under U, dispatch changes touch only 7.1% of riders, but 77% of them end up late, and they are 134 of the 203 late
  riders (66%). The unexposed riders are late at about 3.1% in every arm: that is the traffic-only floor, and the caps
  do not change it.
- Every cap cuts exposure to 1.1–1.7% and roughly halves shared passenger-minutes (2,962 → 1,302–1,403) while serving
  3.6–4.0% fewer riders (2,336–2,347 vs 2,434).

So, my updated claims:

**R1'.** Lateness after the first promise is small in U because only 7.1% of riders are ever exposed to a later
dispatch change; the rest are late only through traffic (3.1%). Why exposure is that low (selection of short trips,
demand intensity, anchoring, locks) is NOT ranked; that needs controlled runs.

**R2'.** In these runs every cap works through the same channel: fewer later insertions that move promised drops,
visible as about half the shared passenger-minutes. Among the caps, C-30 is the only one that never has to override
itself; it does not pool more than the deadline rules.

## C. Questions (keep the answer under 1,200 words)

1. Check `exposure_check.py` (logic, the c ≠ 0 test, the union of overlap intervals). Any error?
2. Do R1' and R2' survive? If not, the exact wording you would accept.
3. Your remaining disagreements need runs. Given the thesis deadline (mid-November 2026, about 5 weeks), rank AT MOST
   two experiments by value per run-hour, each with the design (arms, cells, what is varied), the sealed prediction you
   would write, and what result would change the thesis claim. Prefer designs that reuse the existing runner, fixtures
   and analysis scripts.
4. Final list "Joint conclusions" (SUPPORTED / WEAK / UNSUPPORTED) and "Remaining disagreements". I will write the
   joint file from your list and mine and show both to the owner.
