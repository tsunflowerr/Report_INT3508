# T1.12 — result (exploratory, development panel)

Preregistration: `T112-PREREGISTRATION.md`, SHA-256
`f96d8051c3756d704adda982b53954e484460e0c8252b2f99714df5507946987`, sealed 2026-09-24T01:31:21Z,
before `t112_lockprune.py` was run. Raw output: `t112.log`.

Data: WP14R v6 development matrix (`E:/RideBoundData/wp14r/development-v6-ledger`), arms
`c1-h6ref` and `c1-nopickuplock`, 16 cells `d201811{12,13}-s10-r{1..4}-w{08,17}`.

## B — decisive service test

Accepted requests, `c1-nopickuplock` − `c1-h6ref`: **0 in 16 of 16 cells** (1,534 vs 1,534).
Prediction (0 in every cell) **confirmed**. Removing the pickup lock entirely recovers nobody on
this panel, so no lifecycle-dependent shape of that lock (WP15 axis C) can recover riders here.
**Axis C: void for service on the development panel.**

## A — timing of lock prunes

- 268 phase-lock witnesses on `pickup_eta_ms`, all with rule `final_confirmation`; 219 unique
  (cell, frame, request) events; held pickup ETA was never already in the past (0).
- Lead = held pickupEta − frame simTime. Lock events: p10 38, p25 91, p50 197, p75 294, p90 403,
  max 505 s. Exposure (all 23,649 waiting-rider publications): p10 19, p25 83, p50 193, p75 330,
  p90 444, max 600 s.
- Share with lead ≤ 60 / 120 / 300 s: lock 20.1 / 32.9 / 76.7 %; exposure 19.4 / 33.7 / 70.3 %
  (differences +0.7 / −0.9 / +6.5 pp).
- By the preregistered definition (≥ +10 pp at ≤ 300 s) lock prunes are **not concentrated near
  pickup**: they follow the exposure distribution.

Reading 1 (literal wording of `docs/tasks/47` §2 C1 and plan §9): not concentrated ⟹ axis C void.
Reading 2 (the mechanism stated in the same paragraph): ~23 % of lock prunes happen more than
300 s before pickup, which a near-pickup-only lock would remove — but B shows that removing ALL
of them recovers no rider. Both readings end at the same verdict on this panel.

## Limits

Exploratory, one development panel of 16 cells, static travel times, descriptive (no
confirmatory claim). "Accepted" = length of `semantic.acceptedRequestIds` in `run-00.json`.
The disagreement between the literal falsification wording and the stated mechanism in
`docs/tasks/47` §2 C1 is reported to the owner, not resolved here.
