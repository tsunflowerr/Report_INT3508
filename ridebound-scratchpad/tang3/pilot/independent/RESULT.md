# Independent verification of the T3.7 pilot report, claims 1-8

- Script: `E:\Code\Report_INT3508\ridebound-scratchpad\tang3\pilot\independent\verify_pilot.py` (written from scratch; imports no author module)
- Python: `E:\RideBoundData\wp7\envs\fleetpy-1.0.2\python.exe` 3.10.20
- Inputs: `E:\RideBoundData\research\tier3-pilot-v1` (summary.json, transcript-00.ndjson streamed), `E:\Code\Report_INT3508\ridebound-scratchpad\tang3\pilot\logs` (<job>.log)
- Run at: 2026-09-25 11:36:24 local, 135 s
- Only acknowledged decisions count (ack must follow its decision; distinct hashes). Final state = last runnerToAdapter checkpoint. Per-rider drop C/X/V summed over revision entries; E2 = drop V > 60000 ms (strict) over promised riders (histories with a drop promise).
- Values stated rounded in the report (0.835, 0.298, 0.056) are compared at 3 decimals; every other value is compared exactly.

## Summary

- Claim 1: **MATCH**
- Claim 2: **MATCH**
- Claim 3: **MATCH**
- Claim 4: **MATCH**
- Claim 5: **MATCH**
- Claim 6: **MATCH**
- Claim 7: **MISMATCH** - max lag over all bins >= 1 of all 60 logs (s): report `149` vs raw `265`; where (arm, world, cell, bin): report `W4 w08 bin 3` vs raw `C-30 W4 w08 bin 9`
- Claim 8: **MATCH**

## Verdicts (detail)

### Claim 1: MATCH

All 60 summary.json have status "pass"; all 60 have a final checkpoint.

- [ok] job directories present (expected 60 named jobs): report/expected `60`, raw `60`
- [ok] extra directories in output root: report/expected `[]`, raw `[]`
- [ok] summary.json status == "pass": report/expected `60`, raw `60`
- [ok] final runnerToAdapter checkpoint with onlineState: report/expected `60`, raw `60`

### Claim 2: MATCH

Each cell has 108 requests; served (completed) per arm/world/cell = table 2.6; E2 numerators/denominators of C-30 and V-30 = table 2.6.

- [ok] jobs with exactly 108 requests (and 108 distinct requestIds): report/expected `60`, raw `60`
- [ok] served cells differing from table 2.6 (60 cells): report/expected `[]`, raw `[]`
- [ok] E2 num/den differing from table 2.6 (24 cells): report/expected `[]`, raw `[]`

### Claim 3: MATCH

C-30: 0 non-normal decisions and 0 forcedReference breaches in 12/12; largest per-rider drop C = 19118 ms (<= 30000).

- [ok] C-30 jobs: report/expected `12`, raw `12`
- [ok] C-30 acknowledged decisions with normalOperation=false (sum over 12): report/expected `0`, raw `0`
- [ok] C-30 forcedReference breaches (sum over 12): report/expected `0`, raw `0`
- [ok] largest per-rider drop C over C-30 (at C-30-W4-d20181112-s10-r1-w08): report/expected `19118`, raw `19118`
- [ok] that value <= 30000: report/expected `True`, raw `True`

### Claim 4: MATCH

Episodes (of 12) with non-normal share > 0.5: C-30 0, V-30 5, Mplus-30 2, M-30 5; max V-30 share 0.835 at V-30-W4-...-w17.

- [ok] C-30 episodes with share > 0.5: report/expected `0`, raw `0`
- [ok] V-30 episodes with share > 0.5: report/expected `5`, raw `5`
- [ok] Mplus-30 episodes with share > 0.5: report/expected `2`, raw `2`
- [ok] M-30 episodes with share > 0.5: report/expected `5`, raw `5`
- [ok] max V-30 share (3 dp; exact 585/701 = 0.8345221112696148): report/expected `0.835`, raw `0.835`
- [ok] job with max V-30 share: report/expected `V-30-W4-d20181112-s10-r1-w17`, raw `V-30-W4-d20181112-s10-r1-w17`

### Claim 5: MATCH

Mean forced/fleet: max over V-30 is 0.298 at V-30-W2-...-w17; share of pending decisions with every vehicle forced: 0 for V-30-W2-...-w17, max 0.056 over all jobs (Mplus-30-W2-...-w17).

- [ok] max V-30 meanForcedFleetShare (3 dp; exact 0.29764957264957265): report/expected `0.298`, raw `0.298`
- [ok] job with that max: report/expected `V-30-W2-d20181112-s10-r1-w17`, raw `V-30-W2-d20181112-s10-r1-w17`
- [ok] V-30-W2-w17 pending decisions with every vehicle forced (count, exact): report/expected `0`, raw `0`
- [ok] max pendingAllForcedShare over all 60 jobs (3 dp; exact 6/107): report/expected `0.056`, raw `0.056`
- [ok] job(s) with that max: report/expected `['Mplus-30-W2-d20181112-s10-r1-w17']`, raw `['Mplus-30-W2-d20181112-s10-r1-w17']`
- [ok] decisions whose forced vehicles are not all in vehicleLosses (all jobs): report/expected `0`, raw `0`

### Claim 6: MATCH

Paired C-30 vs V-30 by requestId: common/onlyC/onlyV and '>60 s' counts = table 2.8; W0 (both cells) and W3 morning have identical rider sets (and equal >60 s counts).

- [ok] (world, cell) rows differing from table 2.8 / identical-set statement (12 rows): report/expected `[]`, raw `[]`

### Claim 7: MISMATCH

World switch: max lag 149 s (W4 w08 bin 3); max cross-arm spread 131 s (W5 w17 bin 8); C-30/V-30 only 130 s; factor ranges identical across arms on bins all arms reached.

- [MISMATCH] max lag over all bins >= 1 of all 60 logs (s): report/expected `149`, raw `265`
- [MISMATCH] where (arm, world, cell, bin): report/expected `W4 w08 bin 3`, raw `C-30 W4 w08 bin 9`
- [ok] max lag restricted to bins all 5 arms reached (s) [scope of the author's pilot_worlds.py]: report/expected `149`, raw `149`
- [ok] where, restricted scope: report/expected `W4 w08 bin 3`, raw `U W4 w08 bin 3, C-30 W4 w08 bin 3`
- [ok] max spread across the 5 arms, bins all 5 arms reached (s): report/expected `131`, raw `131`
- [ok] where: report/expected `[('W5', 'w17', 8)]`, raw `[('W5', 'w17', 8)]`
- [ok] max spread across arms, bins reached by >= 2 arms (s) [robustness]: report/expected `131`, raw `131`
- [ok] max spread C-30 vs V-30, bins both reached (s): report/expected `130`, raw `130`
- [ok] bins (all arms reached) whose factor range differs across arms: report/expected `[]`, raw `[]`
- [ok] bins (>= 2 arms reached) whose factor range differs across arms [robustness]: report/expected `[]`, raw `[]`
- [ok] logs with returncode=0 [context]: report/expected `60`, raw `60`
- [ok] logs whose bins are exactly 0..k and bin 0 at t=0 with factor [1.0000, 1.0000] [context]: report/expected `60`, raw `60`
- [ok] '[world] t=' lines that failed the bin regex [parser sanity]: report/expected `0`, raw `0`
- Note: bins (any arm) with lag > 149 s: U W4 w08 bin 9: t=8364s lag=264s (bin NOT reached by all 5 arms); C-30 W4 w08 bin 9: t=8365s lag=265s (bin NOT reached by all 5 arms)
- Note: The report text (section 2.1, 'Trễ lớn nhất 149 s') does not state the restriction to bins every arm reached; over all bins of all 60 logs the maximum is larger (see above).

### Claim 8: MATCH

Late pickups: 71 over 60 jobs, at most 4 per job, largest lateness 207156 ms.

- [ok] total late pickups: report/expected `71`, raw `71`
- [ok] max late pickups in one job: report/expected `4`, raw `4`
- [ok] max actualPickupMs - latestPickupMs (ms): report/expected `207156`, raw `207156`

## Integrity checks on the raw data (sums over 60 jobs; expected 0 / empty unless noted)

- frameShaMismatch: `0`
- frameLengthMismatch: `0`
- duplicateDecisionConflicts: `0`
- ackWithoutPriorDecision: `0`
- duplicateAcks: `0`
- decisionsUnacknowledged: `0`
- forcedNoneVehicleId: `0`
- duplicateLedgerRequestId: `0`
- emptyHistory: `0`
- firstEntryNotInitial: `0`
- laterEntryNotRevision: `0`
- dropChainBreak: `0`
- dropDeltaMismatch: `0`
- historyWithoutDrop: `0`
- latePickupNonPositive: `0`
- jobs where decisionsWithEvidence != decisionsAcknowledged: `0`
- jobs where promisedRiders != ledgerHistories: `0`
- fleet sizes seen: `['8']`
- jobs where promised riders != completed riders (as sets): `[]`

## Other report statements recomputed on the side (not in the 1-8 list; informational)

- table 2.7 C-30: non-normal share range excl. W0: `0.000-0.000`
- table 2.7 C-30: forced-breach rider share range excl. W0 / all 12: `0.000-0.000 / 0.000-0.000`
- table 2.7 C-30: mean forced fleet share range excl. W0 / all 12: `0.000-0.000 / 0.000-0.000`
- table 2.7 V-30: non-normal share range excl. W0: `0.178-0.835`
- table 2.7 V-30: forced-breach rider share range excl. W0 / all 12: `0.062-0.522 / 0.000-0.522`
- table 2.7 V-30: mean forced fleet share range excl. W0 / all 12: `0.049-0.298 / 0.000-0.298`
- table 2.7 Mplus-30: non-normal share range excl. W0: `0.000-0.660`
- table 2.7 Mplus-30: forced-breach rider share range excl. W0 / all 12: `0.000-0.295 / 0.000-0.295`
- table 2.7 Mplus-30: mean forced fleet share range excl. W0 / all 12: `0.000-0.180 / 0.000-0.180`
- table 2.7 M-30: non-normal share range excl. W0: `0.178-0.738`
- table 2.7 M-30: forced-breach rider share range excl. W0 / all 12: `0.052-0.507 / 0.000-0.507`
- table 2.7 M-30: mean forced fleet share range excl. W0 / all 12: `0.052-0.291 / 0.000-0.291`
- U episodes with non-normal share > 0.5: `0`
- V-30-W2-w17 pending decisions with >= half the fleet forced (report 36.4%): `39/107 = 0.364`
- V-30-W2-w17 forced-breach rider share (report 52.2%): `36/69`
- U W0 w08 E2 (report 3/102 sáng, 5/99 tối): `3/102`
- U W0 w17 E2 (report 3/102 sáng, 5/99 tối): `5/99`
- V-30-W4-w17 largest per-rider drop C (report: one rider with 129 s): `129053`
- C-30 served - V-30 served: >=0 count / >0 count / range (report 12/12, 9/12, 1-10): `12/12, 9/12, 1-10`
- C-30 served - U served range (report -5..+1): `-5..1`
- bin counts per log (report: 9 or 10): `[9, 10]`
- logs where 'bin changes applied' != number of bin lines: `0`
- logs whose edge count changes between bins: `0`

