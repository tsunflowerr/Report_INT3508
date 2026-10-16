# Independent verification of tier3-w07-v1 claims (2026-09-30)

## Verdicts

| # | Claim | Verdict |
|---|---|---|
| 1 | 88 summaries pass, one inventory hash, one scenario hash per cell | MATCH |
| 2 | World logs: version, base check, t = 900*b, factors match CSV | MATCH |
| 3 | Served table per cell | MATCH (all 88 values) |
| 4 | Non-normal decisions pattern | MATCH |
| 5 | Mplus-60 A_r > 60 s shares, Mplus-30 mean, C-30 max A_r | MATCH (see rounding note) |
| 6 | Fleet-action sequence equality | MATCH |
| 7 | 13r1: one rider with A_r = 307.3 s under C-300 and Mplus-300 | MATCH |

## Method

I wrote the parser from scratch. It imports nothing from the other ridebound-scratchpad scripts. All inputs were only read.

- `verify_w07.py` reads each of the 88 `transcript-00.ndjson` files line by line. For every frame it base64-decodes the frame, checks that `sha256(frame) == frameSha256`, and JSON-parses the envelope. It then collects:
  - `decision` frames (runnerToAdapter), with their hash, `simTimeMs`, `certificate.body.normalOperation` and actions;
  - `decisionApplied` hashes (adapterToRunner), which count as acknowledgements;
  - the first `eventBatch` `simTimeMs` for each rider's `passengerAlighted`;
  - the last runnerToAdapter `checkpoint`.

  Only acknowledged decisions are used for the next four items:
  - First promise = the first `promisePublished` action per `payload.promise.requestId`, taking `payload.promise.dropEtaMs`.
  - Served = requests with `lifecycle == "completed"` in the last checkpoint's `content.onlineState.requests`.
  - A_r = (alight simTimeMs - first dropEtaMs) / 1000, computed for completed riders.
  - Fleet sequence = the list of sha256 hashes of the canonical JSON (sorted keys) of each action whose type is in {vehiclePlanUpdated, requestAccepted, requestRejected}, in transcript order.

  The script also parses the 88 job logs and `<day>_tt_factors.csv` (columns `simulation_time`, `travel_time_factor`). Output: `runs-extracted.json`.
- `evaluate_claims.py` evaluates claims 1-7. Output: `claims-output.txt`, which holds the full numbers.
- `supplementary_checks.py` re-reads the transcripts to run a stricter claim-6 check and prints the claim-5 means at full precision. Output: `supplementary-output.txt`.
- Python: `E:\RideBoundData\wp7\envs\fleetpy-1.0.2\python.exe -B` with PYTHONDONTWRITEBYTECODE=1. All output files were opened with mode "x".

Integrity checks, all passed:
- 88/88 run folders are present and there are no extra folders.
- 182,917 transcript lines were read, with 0 frameSha256 mismatches.
- In every run, the number of decisions equals the number of acknowledgements. No decision is unacknowledged and no acknowledgement lacks a decision.
- Each run has exactly one runner checkpoint.
- Every decision certificate has a `normalOperation` field.
- The only lifecycles seen are `completed` and `rejected`.
- Every completed rider has exactly one passengerAlighted and a first promise. No non-completed rider alighted.

## Claim-by-claim numbers

**1. MATCH.**
- 88/88 summaries have status `pass`.
- 88/88 have repositoryInventorySha256 `0da63eaf...cbe`.
- Each cell has exactly 1 distinct sourceScenarioContentSha256 across its 11 arms, and the 8 cells have 8 different hashes:

| Cell | sourceScenarioContentSha256 (prefix) |
|---|---|
| 12r1 | 9a78a436 |
| 12r2 | 23793cec |
| 12r3 | 39161625 |
| 12r4 | 60b6c121 |
| 13r1 | 2ad780e4 |
| 13r2 | 3ea1b8c5 |
| 13r3 | b62dd08e |
| 13r4 | 482f5069 |

**2. MATCH.**
- Every one of the 88 logs has exactly one `[world] version=` line, and it is `v1.2`.
- Every log has exactly one base-check line, with the correct day and windowStart=25200.
- Across the 803 bin lines, all have t = 900*b.
- The largest gap between a printed factor (both values) and the value expected from the CSV is 0.000050, which is the 4-decimal rounding limit and within the 1e-4 tolerance.
- Expected factors for b = 0..8:
  - 2018-11-12: 1.0000, 1.0597, 1.1715, 1.2339, 1.2904, 1.3824, 1.3986, 1.4635, 1.4785
  - 2018-11-13: 1.0000, 1.1338, 1.2726, 1.3474, 1.4055, 1.4570, 1.4894, 1.5262, 1.5440
- 22 logs (cells 12r2 and 12r3) have a b = 9 line. It prints f(32400)/f(25200), which is the same as the b = 8 value, as claimed.
- The highest bin in the logs is 7 for 13r3 and 8 for the other five cells.
- Every log starts with `returncode=0`.

**3. MATCH.** Recomputed served counts (U, C-30/60/120/300, Mplus-30/60/120/300, V-30, M-30):

| Cell | U | C-30 | C-60 | C-120 | C-300 | Mplus-30 | Mplus-60 | Mplus-120 | Mplus-300 | V-30 | M-30 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 12r1 | 90 | 87 | 87 | 90 | 90 | 87 | 87 | 89 | 90 | 87 | 87 |
| 12r2 | 82 | 82 | 82 | 82 | 82 | 82 | 82 | 82 | 82 | 82 | 82 |
| 12r3 | 97 | 97 | 97 | 97 | 97 | 97 | 97 | 97 | 97 | 97 | 97 |
| 12r4 | 87 | 86 | 87 | 87 | 87 | 86 | 87 | 87 | 87 | 86 | 86 |
| 13r1 | 70 | 68 | 68 | 71 | 70 | 68 | 68 | 70 | 70 | 68 | 68 |
| 13r2 | 65 | 65 | 65 | 65 | 65 | 65 | 65 | 65 | 65 | 65 | 65 |
| 13r3 | 82 | 83 | 83 | 82 | 82 | 83 | 83 | 82 | 82 | 83 | 83 |
| 13r4 | 92 | 92 | 92 | 92 | 92 | 92 | 92 | 92 | 92 | 92 | 92 |

**4. MATCH.** Non-normal acknowledged decisions per run:

| Arm | 12r1 | 12r2 | 12r3 | 12r4 | 13r1 | 13r2 | 13r3 | 13r4 |
|---|---|---|---|---|---|---|---|---|
| U, C-30, C-60, C-120, C-300 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Mplus-30 | 498 | 470 | 486 | 419 | 324 | 268 | 336 | 453 |
| Mplus-60 | 473 | 141 | 198 | 252 | 324 | 157 | 151 | 249 |
| Mplus-120 | 0 | 0 | 0 | 66 | 144 | 110 | 0 | 0 |
| Mplus-300 | 0 | 0 | 0 | 0 | 82 | 0 | 0 | 0 |
| V-30 | 498 | 470 | 532 | 419 | 350 | 356 | 336 | 534 |
| M-30 | 498 | 470 | 486 | 419 | 324 | 268 | 336 | 453 |

**5. MATCH.**

Mplus-60, riders with A_r > 60 s / completed riders:

| Cell | Count | Share |
|---|---|---|
| 12r1 | 7/87 | 0.0805 |
| 12r2 | 5/82 | 0.0610 |
| 12r3 | 4/97 | 0.0412 |
| 12r4 | 2/87 | 0.0230 |
| 13r1 | 8/68 | 0.1176 |
| 13r2 | 5/65 | 0.0769 |
| 13r3 | 5/83 | 0.0602 |
| 13r4 | 11/92 | 0.1196 |

- The mean of the eight shares is 0.072505, which rounds to 0.073.
- Mplus-30, riders with A_r > 30 s:

| Cell | Count | Share |
|---|---|---|
| 12r1 | 24/87 | 0.2759 |
| 12r2 | 21/82 | 0.2561 |
| 12r3 | 24/97 | 0.2474 |
| 12r4 | 14/86 | 0.1628 |
| 13r1 | 26/68 | 0.3824 |
| 13r2 | 16/65 | 0.2462 |
| 13r3 | 13/83 | 0.1566 |
| 13r4 | 18/92 | 0.1957 |

  The mean is 0.240370, which rounds to 0.240.
- C-30 max A_r per cell, in seconds:

| 12r1 | 12r2 | 12r3 | 12r4 | 13r1 | 13r2 | 13r3 | 13r4 |
|---|---|---|---|---|---|---|---|
| 109.074 | 102.913 | 99.659 | 148.747 | 99.061 | 194.045 | 88.248 | 106.300 |

  All eight equal the claimed values at 0.1 s.

**6. MATCH.**
- The full action JSON (including candidateId) was compared:
  - Mplus-30 vs C-30: equal in 8/8 cells.
  - Mplus-60 vs C-60: equal in 8/8 cells.
  - Mplus-300 vs C-300: equal in 8/8 cells.
  - Mplus-120 vs C-120: equal in 6/8 cells. The two that differ:
    - 12r1: 381 vs 383 fleet actions, first divergence at 0-based action index 165.
    - 13r1: 324 vs 327 fleet actions, first divergence at index 162.
  - V-30 vs C-30: equal in 8/8 cells.
- The same counts hold under two stricter definitions (from `supplementary_checks.py`):
  - each action tagged with its decision's simTimeMs;
  - actions grouped per acknowledged decision, with empty groups kept.

  Wherever the sequences are equal, the number of acknowledged decisions is also equal. For Mplus-120 vs C-120 the counts differ: 729/735 in 12r1 and 601/608 in 13r1.
- Ignoring candidateId gives the same counts.

**7. MATCH.**
- In d20181113-s10-r1-w07, rider `rq-a019727097c102a93db2f0845b4d081077db5b98a7120c6b3d9beb199adebf5a` has A_r = 307.313 s under both C-300 and Mplus-300.
- It is the only A_r > 300 s in each of those two runs.

## Anomalies and notes (none change a verdict)

- **Claim 5 rounding.** The Mplus-60 mean is 0.072505, just above the 0.0725 rounding boundary. Averaging the already-rounded per-cell values gives exactly 0.0725. So "0.073" holds only when rounding the exact mean.
- **Claim 7 "only A_r > 300 s in that cell".** U has the same rider with the same A_r of 307.313 s. No other arm in 13r1 has any A_r > 300 s. So across all 11 arms of the cell, that rider is still the only one above 300 s.
- **M-30 vs Mplus-30.** M-30's non-normal counts are identical to Mplus-30 in all 8 cells. V-30 has higher counts in 12r3, 13r1, 13r2 and 13r4.
- **Fleet actions of M-30.** M-30's fleet-action sequence equals C-30's (and so V-30's and Mplus-30's) in 8/8 cells. For comparison, U equals C-30 in 4/8 cells.
- **Negative A_r.** The minimum A_r over all 88 runs is -0.476 s: some riders alight slightly before their first promised drop ETA.
- **Mplus-120.** It also has non-normal decisions in 12r4, 13r1 and 13r2. This is not claimed, and is reported only for completeness.

## Files (all new, in this folder)

- `explore.py`, `explore2.py`: format discovery only.
- `verify_w07.py`: extraction script, producing `runs-extracted.json`.
- `evaluate_claims.py`: claim evaluation, producing `claims-output.txt`.
- `supplementary_checks.py`: stricter claim-6 check and full-precision means, producing `supplementary-output.txt`.
