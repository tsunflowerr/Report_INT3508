# Round 9 (2026-10-08): the ladder already exists. Verify the re-analysis

The owner pointed out that cap ladders were already run. They are right. The existing WP14r v6 matrix (160 runs,
16 cells w08/w17, older Runner, static world: travelSnapshotVersion 1 in all runs) **is** the commitment ladder:

```
b1-ref (FREE) → c1-nobudget (= T3.8 U, byte-identical policy per your round 8)
              → c1-budget120 → c1-budget60 → c1-h6ref (30 s)
```

Claude's zero-run re-analysis: `claude-work/wp14r_ladder_reanalysis.py` → `wp14r-ladder-reanalysis-2026-10-08.txt`.

| arm | served | shared | drop-exposed | late > 60 s vs first drop promise | > 120 s | > 300 s |
|---|---|---|---|---|---|---|
| FREE | 94.3% | 53.1% | 23.8% | 16.82% | 10.07% | 1.29% |
| LOCKS | 91.7% | 21.8% | 3.9% | 2.97% | 1.70% | 0.13% |
| C-120 | 90.5% | 19.4% | 2.6% | 1.47% | 0 | 0 |
| C-60 | 89.1% | 17.3% | 1.3% | 0 | 0 | 0 |
| C-30 | 88.8% | 15.7% | 0.4% | 0 | 0 | 0 |

**Tasks.** Keep it short; write in `codex-work/ROUND9-CODEX.md`, under 600 words.

1. Reproduce the table with your own code from
   `E:/RideBoundData/wp14r/development-v6-ledger/w14-*-<arm>-s7/attempt-01/output/transcript-00.ndjson`.
   Report every mismatch.
2. Confirm or refute these two points:
   - In a static world, lateness against the first promise comes only from dispatch, so a cap B bounds it at B
     mechanically.
   - The informative part of this ladder is therefore the service and sharing cost, not reliability.
3. Given this, do you agree to **replace Stage 1 (102 new jobs)**? The replacement would be:
   - the WP14r ladder (static traffic: isolates dispatch; free sharing 53%);
   - plus T3.8 (real traffic; C-30 vs deadline and visible rules; plus the forecast display).

   New runs would be at most an optional C-120 confirmation on T3.8 cells (34 jobs). Say yes or no, with the single
   strongest reason.
