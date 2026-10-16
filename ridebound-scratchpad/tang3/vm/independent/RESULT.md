# Independent verification of Tier 3 V/M (task A) claims

Date: 2026-09-29. Verifier code: `verify_vm.py` (main), `supplement.py` (diagnostics), written from
scratch. Nothing was imported or copied from `ridebound-scratchpad`. The raw outputs are in
`verify_output-20260929-213120.txt` and `supplement_output-20260929-213218.txt`. `extract.json` is a
compact per-run extract made from the transcripts, and `run1-console.log` is the console log. All
output files were opened with mode `x`. Every input was only read.

Python: `E:\RideBoundData\wp7\envs\fleetpy-1.0.2\python.exe -B`, with `PYTHONDONTWRITEBYTECODE=1` and
`PYTHONIOENCODING=utf-8`.

## Inputs (60 runs)

- Task A: 48 folders, `C:\RideBoundData\research\tier3-vm-v11-{a,b}\{V-30,M-30}-W{0..5}-d20181112-s10-r1-{w08,w17}`.
- C-30: 12 folders, `E:\RideBoundData\research\tier3-sweep-v1\C-30-W{0..5}-<cell>`. For W4 w17 I used
  `C-30-W4-d20181112-s10-r1-w17-rerun1`.

## Parsing method

For each line of `transcript-00.ndjson` the script:

- base64-decodes `frameBase64` and checks the SHA-256 of the decoded bytes against `frameSha256`;
- checks that `ordinal` is contiguous;
- parses the JSON envelope.

The messages it uses:

- **runnerToAdapter `decision`:** `payload.decisionHash`, `payload.actions`, `payload.certificate.body.normalOperation` and `.witnesses`.
- **adapterToRunner `decisionApplied`:** `payload.decisionHash`. An acknowledged decision is one whose hash appears here.
- **adapterToRunner `eventBatch`:** for each requestId, the envelope `simTimeMs` of the first batch that contains its `passengerAlighted` event.
- **runnerToAdapter `checkpoint`:** the last one is the final state. From it the script reads `content.onlineState.requests[*].lifecycle` and `onlineState.commitmentLedger`.

**Integrity: clean in all 60 runs.**

- 0 SHA mismatches and 0 ordinal gaps.
- Every decision is acknowledged: decisions = decisionApplied, with no duplicate hashes and no applied hash that is missing from the decisions.
- Every decision has status `produced` and certificate status `produced`.
- Only four action types occur: `promisePublished`, `vehiclePlanUpdated`, `requestAccepted`, `requestRejected`.

## Verdicts

### Claim 1: MATCH

- All 48 task A `summary.json` files have `status == "pass"` and
  `repositoryInventorySha256 == 0da63eaf…4cbe`.
- The labels agree with the variants: all 24 variant a folders end in `-vma` and all 24 variant b
  folders end in `-vmb`.
- The 12 C-30 summaries also pass, with the same inventory hash.

### Claim 2: MATCH, 12 of 12 cells

`served` = the number of requests with `lifecycle == "completed"` in the last checkpoint. The table
below is recomputed and equals the claimed table in every cell (C-30 | V-30 a/b | M-30 a/b).

| World | w08 | w17 |
|---|---|---|
| W0 | 97 \| 97/97 \| 97/97 | 95 \| 95/95 \| 95/95 |
| W1 | 82 \| 80/82 \| 79/85 | 79 \| 78/79 \| 78/79 |
| W2 | 85 \| 77/85 \| 77/85 | 79 \| 66/79 \| 66/79 |
| W3 | 108 \| 108/108 \| 108/105 | 107 \| 103/107 \| 102/107 |
| W4 | 94 \| 92/94 \| 89/94 | 89 \| 85/89 \| 86/89 |
| W5 | 90 \| 92/90 \| 87/92 | 99 \| 96/99 \| 97/99 |

Cross-check: the number of distinct requestIds with a `passengerAlighted` event equals `served` in all
60 runs.

### Claim 3: MATCH

- **W0:** all four variants have 0 decisions with `normalOperation == false` in both cells. C-30 has 0
  in every cell.
- **W1..W5:** the minimum counts are V-30 a = 153 (W3 w08) and M-30 a = 152 (W3 w08). The counts are
  identical whether I count all decisions or only acknowledged ones, because every decision is
  acknowledged.
- **Full counts:** V-30 a per cell (w08/w17) is W1 256/181, W2 409/388, W3 153/245, W4 533/544 and
  W5 332/433. M-30 a per cell is W1 267/181, W2 418/388, W3 152/215, W4 536/535 and W5 321/433.

### Claim 4: MATCH

**Definitions used.**

- **Fleet actions:** all actions whose `decisionType` is in {vehiclePlanUpdated, requestAccepted,
  requestRejected}. In these transcripts that is the same as every action that is not
  `promisePublished`.
- **Comparison:** each action is hashed as canonical JSON (sorted keys), keeping transcript order,
  over acknowledged decisions only.

**Six comparison methods, all with the same result.** The methods are:

- flattened sequence;
- per-decision lists, which keep decision boundaries and empty decisions;
- per-decision lists plus each decision's `simTimeMs`;
- the flattened and per-decision comparisons again with `candidateId` removed;
- per-decision lists with the actions sorted.

With every method, V-30 b equals C-30 in 11 of 12 cells. The one exception is W4 w08.

- In W4 w08 the first divergence is at acknowledged decision index 634 (simTime 6 394 000 ms), and
  65 of 771 per-decision fleet lists differ.
- At that point C-30 does `requestAccepted` + `vehiclePlanUpdated`, while V-30 b does
  `requestRejected`. V-30 b's decision there is `normalOperation=false` with 7 witnesses of type
  forcedReference / COMMITMENT_BUDGET_EXCEEDED.
- In W0, all four variants (V-30 a/b, M-30 a/b) equal C-30 with every method.

**Not claimed, for context.** M-30 b also equals C-30 in W1 w17, W2 w08 and W4 w08. V-30 a and M-30 a
differ from C-30 in every W1..W5 cell.

### Claim 5: MATCH

**V-30 b.** Acknowledged decisions with at least one witness where `stage == "forcedNoWorse"` and
`code == "COMMITMENT_BUDGET_EXCEEDED"`, per cell (w08/w17):

- W1 8/11
- W2 23/11
- W3 2/14
- W4 21/16
- W5 9/3

The total is **118**.

**M-30 b in W3.** Acknowledged decisions with any forcedNoWorse witness: w08 = 2, w17 = 10, total
**12**.

**Notes.**

- M-30's forcedNoWorse witnesses all carry the code `COMMITMENT_DEADLINE_EXCEEDED`. With the budget
  code the M-30 b W3 count would be 0, so the claim is only correct as phrased, with "any"
  forcedNoWorse witness.
- The claim counts decisions, not witness entries. A few decisions carry two witnesses: V-30 b W3 w17
  has 15 entries in 14 decisions, W4 w08 has 22 in 21, and W5 w08 has 10 in 9.

### Claim 6: MATCH

**Source of the promises.** I used the `promisePublished` actions of acknowledged decisions.

- The drop-time promise is `action.payload.promise.dropEtaMs`, grouped by `promise.requestId` in
  transcript order.
- `promiseVersion` runs 1..n with no gaps for every rider, and the first publication always has
  `reasonCode == INITIAL_BOOKING_CONFIRMATION`.

**Metric.** Total movement per rider = Σ over k ≥ 2 of |dropEta_k − dropEta_{k−1}|. The share is
(riders with total > 30 000 ms) / (riders with at least one promise).

**Cross-check.** I reran the same metric from the last checkpoint's `commitmentLedger`
(`entries[*].publishedPromise.projection.dropEtaMs`). The publicationId sequences are identical to
the decision-based ones and the result is the same.

**Results, W5 w08.**

| Arm | Riders moved > 30 s | Share |
|---|---|---|
| C-30 | 11 / 90 | 0.1222 |
| V-30 b | 11 / 90 | 0.1222 |
| V-30 a | 8 / 92 | 0.087 |
| M-30 a | 10 / 87 | 0.115 |
| M-30 b | 11 / 92 | 0.120 |

The promised riders are exactly the completed riders in these runs (90 = 90).

**Sensitivity (C-30).** Count of riders whose total movement exceeds each threshold:

| Threshold | > 0 s | > 1 s | > 10 s | > 30 s | > 60 s |
|---|---|---|---|---|---|
| Riders | 90 | 80 | 36 | 11 | 2 |

### Claim 7: MATCH

For C-30 W5 w08, with actual drop = the `simTimeMs` of the first eventBatch containing the rider's
`passengerAlighted` event (each rider has exactly one such event), and first promise = `dropEtaMs` of
promiseVersion 1, over all 90 completed riders:

- **Late by more than 30 s** (actual − first > 30 000 ms): **2/90 = 0.0222**.
- **Off by more than 30 s either way** (|actual − first| > 30 000 ms): **7/90 = 0.0778**, made up of
  2 late and 5 early.

V-30 b gives the same 2/90 and 7/90.

## Anomalies and observations

1. **The last promise equals the actual drop time.** Every completed rider's last drop promise is
   published at or after the alight time, and its `dropEtaMs` equals the actual alight time exactly
   (90/90 in C-30 and in V-30 b, W5 w08). So:
   - The claim 6 movement includes a final correction to the realised time.
   - Leaving out publications made at or after alight does not change the result (still 11/90).
   - In claim 7, |actual − first| is the same as the net movement |last − first|.
2. **C-30 W4 w17 folder.** The original folder was not used, as instructed. The `-rerun1` folder
   passes and has the same inventory hash.
3. **Where V-30 b departs from C-30 in W4 w08.** The departure is caused by a forcedReference
   decision (a rejection), not by a forcedNoWorse one. Of V-30 b's 21 forcedNoWorse decisions in that
   cell, 16 have per-decision fleet actions identical to C-30's; the other 5 come after the
   divergence. In the other 9 W1..W5 cells, every forcedNoWorse decision of V-30 b has fleet actions
   identical to C-30's at the same index.
4. **Two task A arms serve more riders than C-30.** They are M-30 b W1 w08 (85 vs 82) and V-30 a W5
   w08 (92 vs 90). This is only noted as context; neither contradicts a claim.
5. **No other anomalies found.** No transcript errors, no unacknowledged decisions, no unexpected
   action types and no duplicate alight events turned up.
