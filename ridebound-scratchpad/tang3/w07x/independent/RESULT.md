# W07X independent verification — RESULT

Date: 2026-10-01. Verifier: independent agent. All numbers below come from my own parser
(`extract.py`, `analyze.py`, `mechanism.py`, `extra.py` in this folder). I did not import or copy
any module from `ridebound-scratchpad`, and I did not read the existing analysis scripts
(`w07x_analyze.py`, `w07x_mechanism.py`). Everything was read-only on the data. No dotnet, no
simulations, no git writes.

## Verdicts

| # | Claim | Verdict |
|---|-------|---------|
| 1 | 104 new summaries pass + inventory hash; policy hash constant within arm, distinct across 23 arms | **MATCH** |
| 2 | Served table (8 cells × U + all levels) | **MATCH** (every entry) |
| 3 | C-x = Mplus-x fleet actions except (90,12r1),(120,12r1),(120,13r1); V-x = C-x with the same exceptions | **MATCH** |
| 4 | 32 new C runs have 0 non-normal decisions | **MATCH** |
| 5 | A_r > x shares under Mplus-x; non-normal shares Mplus / V | **MATCH** (all 11 numbers) |
| 6 | V_r > x shares under V-x | **MATCH** (all 5 numbers) |
| 7 | Mechanism at (90, 12r1) | **MATCH** (every sub-point) |

## Integrity checks (all 184 runs: 104 new + 80 reused)

- For all 383,059 frames, `frameSha256` = SHA-256 of the base64-decoded frame bytes. 0 mismatches.
- Every `decision` was acknowledged: the `decisionApplied` hashes match the decision hashes one to one, in order, in every run. So "acknowledged decisions" = all decisions.
- Each run has exactly 1 runner checkpoint. Every completed rider has a ledger entry and exactly one `passengerAlighted`. There are no duplicate alight events.
- Each rider's ledger has exactly one `initialPromise`, and it comes first. All other entries are `revision` / `ONLINE_REPLAN`.
- Revision chain: each revision's `previousPromise` equals the previous entry's `publishedPromise`. 0 breaks.
- Ledger vs transcript: each rider's ledger (version, dropEtaMs) sequence equals the `promisePublished` actions in acknowledged decisions. 0 mismatches in 184 runs. No promise action lacks a ledger entry.

## Claim 1 — MATCH
- New summaries: 104 of 104 have `status: pass`. 104 of 104 have `repositoryInventorySha256 = 0da63eaf…4cbe`.
- `policyConfigurationHash` (from `initializeRun.payload.manifest`) has 1 distinct value in each of the 23 arms, over 8 cells. The 23 arm values are all different (23 distinct).
- Info: the 80 reused summaries are also `pass` with the same inventory hash.

## Claim 2 — MATCH
Served = lifecycle `completed` in the last (only) runner checkpoint. Format is U | level: C/Mplus[/V].

```
12r1: U 90 | 30: 87/87/87 | 60: 87/87 | 90: 90/89/89 | 120: 90/89/89 | 150: 90/90/90 | 180: 90/90/90 | 240: 90/90/90 | 300: 90/90
12r2: U 82 | all 82
12r3: U 97 | all 97
12r4: U 87 | 30: 86/86/86 | all others 87
13r1: U 70 | 30: 68/68/68 | 60: 68/68 | 90: 69/69/69 | 120: 71/70/70 | 150: 71/71/71 | 180: 71/71/71 | 240: 70/70/70 | 300: 70/70
13r2: U 65 | all 65
13r3: U 82 | 30: 83/83/83 | 60: 83/83 | all others 82
13r4: U 92 | all 92
```

## Claim 3 — MATCH
I compared the per-decision lists of fleet actions (types vehiclePlanUpdated / requestAccepted / requestRejected / requestDeferred) over all acknowledged decisions, in order. An empty list still counts as a position. I used two comparison methods:
(a) full canonical JSON of `{decisionType, payload}`. For vehiclePlanUpdated this includes the whole route.
(b) a key of type + vehicleId + candidateId, or type + requestId.
Both methods give the same result.
- C vs Mplus differ only at (90,12r1) with first difference at index 294 (735 vs 729 decisions), (120,12r1) at index 294 (735 vs 729), and (120,13r1) at index 285 (608 vs 601). All other 61 (level, cell) pairs are identical, over levels 30, 60, 90, 120, 150, 180, 240, 300.
- V exists at levels 30, 90, 120, 150, 180, 240. V vs C differ at exactly the same 3 pairs with the same indices.
- Info: Mplus-x and V-x fleet-action sequences are identical in all 48 (level, cell) pairs where V exists.

## Claim 4 — MATCH
All 32 new C runs (C-90/150/180/240 × 8 cells) have 0 decisions with `certificate.body.normalOperation == false`. Info: the reused C-30/60/120/300 runs also have 0.

## Claim 5 — MATCH
A_r = simTimeMs of the first eventBatch that contains the rider's `passengerAlighted`, minus the rider's first drop promise (ledger `initialPromise.publishedPromise.projection.dropEtaMs`). Denominator = completed riders in the cell. The mean is over the 8 cells. Using ">" or ">=" gives identical results.

| x | mean share A_r > x (Mplus-x) | claimed | per cell (k/n: 12r1..12r4, 13r1..13r4) |
|---|---|---|---|
| 90 | 0.021180 | 0.0212 | 4/89 3/82 1/97 1/87 2/69 1/65 0/82 2/92 |
| 150 | 0.005073 | 0.0051 | 1/90 0/82 0/97 0/87 1/71 1/65 0/82 0/92 |
| 180 | 0.005073 | 0.0051 | same as 150 |
| 240 | 0.001786 | 0.0018 | 0/90 0/82 0/97 0/87 1/70 0/65 0/82 0/92 |

Non-normal share = non-normal acknowledged decisions / acknowledged decisions per cell, averaged over cells.

| x | Mplus | V | claimed |
|---|---|---|---|
| 90 | 0.129608 | 0.173571 | 0.130 / 0.174 |
| 120 | 0.065718 (reused) | 0.074291 | 0.066 / 0.074 |
| 150 | 0.068184 | 0.086121 | 0.068 / 0.086 |
| 180 | 0.028206 | 0.028206 | 0.028 / 0.028 |
| 240 | 0.016998 | 0.016998 | 0.017 / 0.017 |

Per-cell counts (non-normal / acknowledged decisions):
```
Mplus-90   132/729 106/688 108/791 66/719 82/593 110/566 0/685 106/753
V-90       219/729 124/688 108/791 69/719 103/593 110/566 55/685 171/753
Mplus-120  0/729 0/688 0/791 66/719 144/601 110/566 0/685 0/753
V-120      50/729 0/688 0/791 66/719 144/601 110/566 0/685 0/753
Mplus-150  84/735 0/688 0/791 0/719 144/608 110/566 0/685 0/753
V-150      122/735 0/688 0/791 66/719 144/608 110/566 0/685 0/753
Mplus-180  84/735 0/688 0/791 0/719 43/608 23/566 0/685 0/753
Mplus-240  0/735 0/688 0/791 0/719 82/603 0/566 0/685 0/753   (V-180 = Mplus-180, V-240 = Mplus-240)
```

## Claim 6 — MATCH
V_r = sum over the rider's `revision` entries of |p.dropEtaMs − v.dropEtaMs|, where v = `previousPromise` and p = `publishedPromise`.

Why I used the ledger: the checkpoint ledger holds v, e and p explicitly for every revision. I cross-checked it against the `promisePublished` actions (0 mismatches) and checked the revision chain (0 breaks). Because the chain holds, this sum equals Σ|d_k − d_{k−1}| over consecutive published drop ETAs.

Denominator = riders with an initial promise (promised riders). Here the promised riders are exactly the completed riders, so the completed-rider denominator gives identical results. I used strict ">".

| V-x | mean share V_r > x | claimed | per cell k/n |
|---|---|---|---|
| 90 | 0.028924 | 0.0289 | 4/89 4/82 1/97 1/87 3/69 1/65 2/82 3/92 |
| 120 | 0.010121 | 0.0101 | 1/89 0/82 0/97 1/87 3/70 1/65 0/82 0/92 |
| 150 | 0.008270 | 0.0083 | 1/90 0/82 0/97 1/87 2/71 1/65 0/82 0/92 |
| 180 | 0.005073 | 0.0051 | 1/90 0/82 0/97 0/87 1/71 1/65 0/82 0/92 |
| 240 | 0.003571 | 0.0036 | 0/90 0/82 0/97 0/87 2/70 0/65 0/82 0/92 |

## Claim 7 — MATCH (`mechanism_output_90_d20181112-s10-r1-w07.txt`)
- The first acknowledged decision whose fleet actions differ is index **294** (epochId 295) at simTime **3073000 ms**, in both runs. All 294 earlier decisions are identical.
- C-90 does `requestAccepted rq-150ba8d3b7b9…` and `vehiclePlanUpdated veh-176f918dfe… candidate-v1-45ce21a4…`. Mplus-90 does `requestRejected rq-150ba8d3…` with reason NO_FEASIBLE_INSERTION. Both decisions have normalOperation = true.
- C-90's candidate `candidate-v1-45ce21a4…` for veh-176f91… appears once in Mplus-90's `prunedCandidates` at decision 294:
  - code `COMMITMENT_DEADLINE_EXCEEDED`, newRequestIds = [rq-150ba8d…]
  - witness `{rule: deadline_cap, stage: lock, dimension: drop_eta_ms, requestId: rq-c7683667e6b3…}`
- The witness rider in the C-90 run:
  - Initial promise at decision 247 (t = 2669000), drop ETA 4182321.
  - 19 revisions before decision 294: Σ(e − v) = **+78.993 s**, Σ(p − e) = **0.000 s**.
  - At decision 294: v = 4261314, e = 4261402, p = 4329664. So e − v = +0.088 s and p − e = **+68.262 s**. This agrees with the action's `decisionDelta.dropEtaTotalMs = 68262`.
  - In Mplus-90 at the same decision, this rider gets decisionDelta 0 and exogenous 88 ms.

## Anomalies / observations (not claim failures)
1. **Non-normal operation seldom changes fleet actions.** Mplus-90 has 13% non-normal decisions and V-90 has 17%. Even so, C = Mplus = V in 7 of the 8 cells at x = 90.
   - Because fleet actions match, the A_r and V_r shares under Mplus and V equal those under C except at the divergent pairs. For A_r: C-90 0.021118 vs Mplus-90 0.021180; C-120 0.011791 vs Mplus-120 0.008717. For V_r: C-90 0.028861 vs 0.028924; C-120 0.013180 vs 0.010121.
2. **Non-normal share is not monotone in x.** Mplus goes 0.066 (x=120) then 0.068 (x=150); V goes 0.074 then 0.086.
   - In the same cell, a looser level can have more non-normal decisions. Examples: 12r1 Mplus-120 0/729 vs Mplus-150 84/735; 12r4 V-120 66 vs V-180 0.
   - I did not investigate why. It is not only a run-length effect: in 12r4 all levels have 719 decisions.
3. **Same mechanism at x = 120.** The first divergence is again a `deadline_cap` prune.
   - (120,12r1): identical to the x = 90 case (index 294, same rider, 79.0 + 0.09 + 68.3 = 147.3 s total drift).
   - (120,13r1): index 285, t = 2903000, rider rq-f6c8ce78…, Σ(e − v) = +60.889 s, Σ(p − e) = 0, then p − e = +61.181 s at the decision.
   - In both cases the total drift from the first promise (147.3 s and 122.2 s) exceeds x, and at x ≥ 150 the pairs no longer diverge. This fits a cap on cumulative drift from the first promise, but that reading is mine and I did not check it against the policy code.
4. **Exceedances come from exogenous drift.** Under V-x, the dispatch-only sum Σ|p − e| never exceeds x at any V level. Maximum Σ|p − e|: 86.9 s at V-90, 96.7 s at V-150, 208.2 s at V-240. So every V_r > x case includes exogenous drift.
5. **Unused reused arm.** The reused root also has an `M-30` arm, which is not among the 23 arms. I ignored it.
6. **Housekeeping.**
   - `extract/C-90-d20181112-s10-r1-w07.json` is a one-run smoke test from before a `runId` field-path fix. It is superseded by `runs/`, not used, and was left in place (no deletions).
   - One exploration dump (`explore2.txt`) was written to the Claude session temp scratchpad, not to any data or repo location.

## Files
- `extract.py`: per-run parser, 6 processes, writes `runs/<arm>-<cell>.json` (mode "x").
- `analyze.py`: claims 1–6. Output is in `analyze_output.txt`.
- `mechanism.py`: claim 7. Outputs are `mechanism_output_90_d20181112-s10-r1-w07.txt` and the two `_120_` files.
- `extra.py`: Mplus vs V comparison and maxima. Output is in `extra_output.txt`.
- `explore*.py`: format exploration only.
