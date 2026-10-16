# T1.12 — Falsification test C1 of WP15 axis C — preregistration

Written BEFORE running `t112_lockprune.py`. Data: WP14R v6 development matrix,
`E:/RideBoundData/wp14r/development-v6-ledger/`, 16 development cells
`d201811{12,13}-s10-r{1..4}-w{08,17}` (not H6, not E1, not WP14-v1; WP15 constraint #2).
Only the arms `c1-h6ref` and `c1-nopickuplock` are read. Read-only.

## What is measured

A. Timing (plan §9 T1.12, `docs/tasks/47` §2 C1). In arm `c1-h6ref`, every pruned candidate
whose `commitmentWitnesses[]` contains `code == COMMITMENT_PHASE_LOCK` on
`dimension == pickup_eta_ms` is a lock prune. For each unique (cell, frame, request) lock
event, lead = pickupEtaMs of that request's last published promise before the frame − frame
`simTimeMs`. Baseline ("exposure"): the same lead for every published promise of a rider that
is still waiting for pickup (publications whose pickupEtaMs > simTimeMs), same arm, same cells.
Report shares with lead ≤ 60 / 120 / 300 s for both, and the full quantiles.

B. Service consequence (decisive, independent of how A is read). Per cell, number of accepted
requests in `c1-nopickuplock` minus `c1-h6ref`.

## Criteria fixed now

- A is REPORTED under both readings found in the locked documents, because they disagree:
  - Reading 1 (literal text of `tasks/47` §2 C1 and plan §9): axis C is void if lock prunes are
    NOT concentrated near pickup.
  - Reading 2 (the mechanism stated in the same paragraph, "the prunes far from pickup must
    disappear"): axis C can only recover prunes that happen FAR from pickup, so it is void if
    lock prunes ARE concentrated near pickup.
  - "Concentrated near pickup" := share(lead ≤ 300 s) among lock events exceeds the exposure
    share(lead ≤ 300 s) by at least 10 percentage points.
- B: axis C is VOID FOR SERVICE on this panel if the per-cell difference is 0 in every one of
  the 16 cells (removing the pickup lock entirely recovers nobody, so no horizon shape of that
  lock can). If any cell differs, report the cells and the total; no threshold is applied to
  claim a benefit, because this is a descriptive development panel.

## Prediction (registered before running)

B: difference 0 in all 16 cells (the 2026-09-02 descriptive slice of 4 cells already showed
`c1-nopickuplock` ≡ `c1-h6ref` on completed count). A: no prediction on the shares.
