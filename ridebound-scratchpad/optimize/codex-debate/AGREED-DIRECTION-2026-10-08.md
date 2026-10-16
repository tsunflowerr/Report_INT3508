# Agreed single direction (Claude + Codex, 2026-10-08)

**Sources.** Codex: `codex-work/ONE-DIRECTION-CODEX.md` (round 8). Claude: `ROUND8-CLAUDE.md`, and the checks listed
below. Nothing has been run or edited in the thesis or docs.

## Thesis storyline (three sentences; agreed)

1. Rule C bounds the cumulative dispatch-caused movement of each rider's drop ETA.
2. A frozen historical forecast puts anticipated traffic into the initial displayed promise.
3. Signed v/e/p accounting separates dispatch from traffic, and the remaining arrival error is reported alongside the
   service and accuracy trade-offs.

## The one experiment: the "commitment ladder"

The ladder runs on the same cells, from loosest to tightest:

| arm | definition |
|---|---|
| FREE | `rolling-cost` WP4 config, no optional commitment limits, no final-confirmation locks |
| LOCKS | = T3.8 U |
| C-300 | locks plus a 300 s cumulative drop budget (conditional arm) |
| C-120 | locks plus a 120 s budget |
| C-60 | locks plus a 60 s budget |
| C-30 | locks plus a 30 s budget |

### Stage 1: 34 existing T3.8 test cells, 8 vehicles

- Reuse U (LOCKS) and C-30.
- New arms: FREE, C-60 and C-120. That is **102 jobs**, after **1 FREE smoke job**.
- C-300 adds 34 jobs, and only under the conditional stop rule.

### Cap selection rule (to be sealed)

Pick the smallest evaluated cap in {30, 60, 120, 300} that meets all three conditions:
1. at least **48** net additional completions over C-30, which is half of the 96-rider gap (U 2,434 vs C-30 2,338);
2. pooled late60 against the forecast-displayed first promise ≤ 1%;
3. zero overrides and zero integrity or enforcement breaches.

### Stage 2: high-load regime, only after selection and fixture gates

- 4 vehicles on 12 preselected cells: 14/11 r3 and r4, 16/11 r1 and r2, 17/11 r1 and r2, each in w08 and w17.
- Arms: FREE, LOCKS, C-30 and the selected cap. That is **48 jobs**.
- β stays frozen; nothing is retuned.

### Predictions (to be sealed)

- With 8 vehicles, FREE sharing is 35–55% and drop exposure is at least 15%.
- C-120 recovers at least 48 completions with late60 ≤ 1%.
- At 4 vehicles, the selected cap still passes the half-gap and late60 screen.

### Kill criteria

- A failed smoke run or audit stops the batch.
- If no cap is eligible, the expansion stops.
- If FREE at 4 vehicles has less than 35% sharing or less than 15% exposure, the high-sharing test is defeated.
- If the selected cap fails the screen at 4 vehicles, the transfer is defeated.
- Falling absolute shared completions defeat any "productive sharing" claim.

### Reporting rules

- Coverage uses all requests. Sharing, exposure and late60 use completed riders.
- Report two-sided accuracy, early arrivals, quote cost for all promised riders, visible variation, common riders and
  overrides.
- Use paired 95% day-cluster bootstrap intervals (10,000 resamples, seed 7).
- The cells were inspected before, so the result is a descriptive selection plus a regime stress test.

### Future work

- Anchor and dwell replication.
- Worlds denser than 128 requests / 32 vehicles / 96 nodes.
- Genuine reassignment.
- A lock ablation with matched objectives.
- Rider acceptance and welfare.

The room superiority claim is withdrawn. The hybrid deadline and forecast-in-dispatch are omitted.

## Corrections accepted by Claude in round 8

- **F2 (WP9 fleet comparison).** My glob mixed seed-19 robustness runs and five "unbounded" c1 runs into panel A.
  The primary panel A figures are:

  | arm | served | shared | exposed |
  |---|---|---|---|
  | b1 | 80.3% | 51.5% | 23.2% |
  | c1 | 73.2% | 14.7% | 0.7% |

  Panel B is unchanged. The absolute number of shared completions *falls* with 4 vehicles (893 → 564 for b1).
- **F5.** `displayBucketWidthMs = 60000` controls material-revision detection, not the rider display
  (`CommitmentPolicy.cs:104`). The "display-invariant" justification for 30 s is withdrawn.
- **Uber's delayed-ride guarantee** is a driver payment measured from pickup to drop, and it excludes Matched Share
  rides. It is not a rider promise-change cap.

## Disagreement resolved by Claude's check

Codex could not retrieve Lu & Kühnel 2024. Claude downloaded it (`claude-work/pdf/lu-kuehnel-2024.pdf`, SHA-256
bf03bdaa…; text :47): "In the practice, a small buffer, such as 2 or 3 minutes can be given, in order to account for
the uncertainties in traffic and other operational aspects."
- The quote is VERIFIED.
- It is a **pickup** buffer from the initially scheduled pickup, and it includes traffic.
- So it is a practice anchor for the order of magnitude only, not a direct analogue of the cumulative dispatch cap C.

## Code feasibility (verified by Claude on the cited lines)

**FREE arm.**
- The FREE WP4 candidate is `codex-work/round8-free-wp4-candidate.json`: `policyId` is `rolling-cost` and there is no
  `commitmentRecovery`.
- The overlay strips the hard limits (`CommitmentCandidateAssessor.cs:90-104`, hardLimit null).
- The accepted-vehicle lock is still enforced (`CommitmentLockEvaluator.cs:42`, activeLocks = Vehicle).
- FREE versus LOCKS also changes the objective priorities (`SolverBackedFleetSelection.cs:312-324`). So
  FREE → LOCKS is a policy-package comparison, and the C ladder is the clean comparison.

**Four-vehicle fixtures.** The prebuilt normalizer DLL can be run with `--repository` pointed to a staging folder
outside every worktree. No build is needed. Smoke gates: DLL provenance, identical requests and graph, and nested
vehicle placement.

## Next step

Owner approval for Stage 1:
1. write and seal the plan;
2. run 1 FREE smoke job;
3. run 102 jobs on AC power. Estimate: about 15 min per job with 6 in parallel, so about 4–5 h. The FREE arm may be
   slower. This is not measured.
