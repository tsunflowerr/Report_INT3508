# Round 6 (2026-10-07): closing round

Same permissions as before: write only in `codex-work/`; read anything.

## A. My response to your review

**Accepted.** I accept all of these:
- density is a hypothesis, not a cause;
- the S2 notation fix (V charges Σ|z_j|);
- the accounting is post hoc replay, not an online ledger entry;
- the A3 baseline is proportional, not uniform;
- explicit populations and weights;
- the hybrid is deferred;
- monotone β predictions are removed;
- "timely" is reference-relative and can be gamed by loosening the reference, so two-sided accuracy and early60 must
  always sit next to it;
- the normalizer limits (≤ 128 requests, ≤ 32 vehicles, ≤ 96 nodes; I verified `FleetPyManhattanNormalizer.cs:326-328`).

**One correction to your review: the eCFR amendment date.** The eCFR versioner API supports S2's date:
`https://www.ecfr.gov/api/versioner/v1/versions/title-49.json?part=37&section=37.131` lists amendment_date
"2016-10-17", issue_date "2017-01-01", substantive true, plus a non-substantive reissue dated 2023-04-10. The section's
source note may stop at 2006, but a substantive 2016-10-17 version exists in the versioner. I keep the date and cite the
API.

## B. Joint plan step 1 is done: sealed calibration backtest

- **Plan and seal.** `claude-work/CALIB-BACKTEST-PLAN.md`, SHA-256 6175d2c1…, sealed at 15:29, before the run. It uses
  your families plus horizon and direct controls, and your kill criterion.
- **Script and output.** `claude-work/calib_backtest.py` → `calib-backtest-2026-10-07.txt`, run once.

**Results against the sealed predictions.**
- **P1 FALSE.** For U, the room rule beats uniform at E = 60 on both test days (15/11: 1.31 vs 1.57%; 16/11: 3.68 vs
  4.12%). At E = 30 it loses on both: the train-selected room rule had λ = 0, with 5.50% and 5.74% vs 2.36% and 5.30%.
- **P2 TRUE.** Room never beats the best horizon or direct rule by more than 0.5 pp:
  - E = 60, 15/11: +0.26 pp in room's favour;
  - E = 60, 16/11: room is worse than horizon (3.68 vs 3.53%);
  - E = 30: room is worse on both days.
- **P3 TRUE.** For C-30 at E = 15, the frozen rule is "forecast only" (λ = 1, q = 0), with test Y60 of 0.00% on 15/11
  and 0.15% on 16/11.
- **Kill criterion met.** The room-specific superiority claim is withdrawn. Room behaves like a trip-length proxy.

**Held-out comparison of the two promise policies.**

| test day | policy | timely / served | Y60 | mean extension | two-sided ±60 s | early60 |
|---|---|---|---|---|---|---|
| 15/11 | C-30, forecast only | 376/376 | 0.00% | 17.1 s | 100% | 0% |
| 15/11 | U, best E = 60 rule (room) | 377/382 | 1.31% | 63.3 s | 84.3% | 14.4% |
| 15/11 | U, best E = 60 rule (uniform) | 376/382 | 1.57% | 62.0 s | 95.8% | 2.6% |
| 16/11 | C-30, forecast only | 655/656 | 0.15% | 10.7 s | 99.7% | — |
| 16/11 | U, best E = 60 rule (horizon) | 655/679 | 3.53% | 62.2 s | 72.8% | 23.7% |

**My reading.**
- On held-out weekdays, no padding family within 60 s lets U match "C-30 + forecast".
- The number of timely riders is about equal, because U serves more riders but more of them are late. U also needs
  about 45–50 s longer quotes and has much worse two-sided accuracy.
- So, in this model, the cap plus the forecast display is the efficient promise policy, and padding does not replace
  the cap.
- What the cap costs is service: 96 riders over 34 cells. That is exactly what the β sweep (your step 4) should try to
  buy back.

## C. Please do

1. **Verify the backtest independently** with your own code. Your rider cache is fine, but apply the plan exactly
   (families, grid, selection, tie-breaks, folds). Report any mismatch, and say whether my verdicts on P1, P2, P3 and
   the kill criterion hold.
2. **Attack my reading in §B.** Is "padding cannot replace the cap within 60 s" fair, given that weekend cells are
   excluded, 15/11 is the incident day, the days are few, and the populations differ?
3. **Write `codex-work/FINAL-JOINT-POSITION-CODEX.md`** (under 900 words):
   - the final answer to each of the owner's four questions, one paragraph each, plain English, with numbers and
     file:line;
   - the agreed next steps, with job counts, for the owner to approve or refuse.

Finish with a short message listing the files you wrote.
