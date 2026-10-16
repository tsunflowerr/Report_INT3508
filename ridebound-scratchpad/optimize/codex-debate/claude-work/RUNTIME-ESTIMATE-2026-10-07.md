# Runtime estimate for scaling demand and fleet up (Claude, 2026-10-07). EXTRAPOLATION, not measured

## Measured facts

1. **Past run sizes and runtimes.** `runtime-scaling-2026-10-07b.txt` covers 1,787 saved runs (script
   `runtime_scaling.py`).
   - The first output file `runtime-scaling-2026-10-07.txt` is empty because of a status-filter bug; it is kept, not
     deleted.
   - No run ever exceeded 128 requests or 32 vehicles.
   - Medians by size:

   | requests | vehicles | window | decisions | wall time | wall time per decision |
   |---|---|---|---|---|---|
   | 108 | 4 | 2 h | 419 | 283 s | 0.68 s |
   | 108 | 8 | 2 h | 692 | 918 s | 1.33 s |
   | 128 | 8 | 2 h | 928 | 1,374 s | 1.48 s |
   | 128 | 16 | 2 h | 1,020 | 1,478 s | 1.45 s (only 2 runs) |
   | 128 | 32 | 24 h | 1,026 | 367 s | 0.36 s |

   The rows come from different experiments, Runner versions and machine loads, so they are confounded.
2. **What the CPU field measures.** The recorded CPU (`resources.userCpuMilliseconds`) covers only the Python FleetPy
   process (`actual_fleetpy_medium_preflight.py:701-718`, `process.cpu_times()`). The .NET Runner process is not
   included, so wall time is the usable measure.
3. **Parallelism.** T3.8 ran 6 jobs in parallel (`tang3/pilot/run_pilot.py:42`, WORKERS = 6) on an i7-9850H (6
   physical / 12 logical cores). That gave 170 jobs in about 7 h, about 15 min per job.
4. **Per-vehicle candidate generation grows steeply with route length.** From `docs/18-status-and-decision-log.md:3423-3427`
   (Runner v8 micro-harness, minimum of three runs):

   | stops in the mutable suffix | time per Generate |
   |---|---|
   | 4 | 16.6 ms |
   | 8 | 170 ms |
   | 12 | 587 ms |
   | 16 | 1,018 ms |

5. **Decisions per request.** About 6–8 per request; there are 692 decisions for 108 requests.
6. **Transcript volume.** About 75 MB per 108-request run. Event batches (vehicle movement) are the largest part:
   25.8 MB in `U-d20181115-s10-r2-w08`, against 19.4 MB of decisions and 13.1 MB of checkpoints.
7. **Hard limits.**
   - The normalizer accepts at most 128 requests, 32 vehicles and 96 nodes (`FleetPyManhattanNormalizer.cs:326-328`).
   - 96 nodes already could not hold 108 requests in 11 of 60 panel-A cells (`T38-PLAN.md:42`).
   - Travel snapshots are complete n × n matrices: 96 nodes give 9,120 arcs; the full Manhattan network has 4,411
     nodes, about 19.4 million arcs.

## Model (assumption)

Scale requests and vehicles together by k, in the same 2-hour window. The three factors:
- decisions grow about ×k;
- each decision evaluates every vehicle, so it grows about ×k (fact 1 supports this for 108/4 → 108/8 but not for
  128/8 → 128/16);
- the cost per vehicle grows with route length. If denser demand doubles the stops per vehicle (4 → 8), that is up to
  ×10 (fact 4).

So time per job is ×k² (optimistic: routes do not get longer) to ×10·k² (pessimistic). The baseline is about 15 min
per job, 6 in parallel.

| k | requests / vehicles | per job (optimistic … pessimistic) | 12 jobs (6 cells × 2 arms), 6 in parallel |
|---|---|---|---|
| 1 | 108 / 8 | 15 min | about 0.5 h |
| 2.5 | 270 / 20 | about 1.5 h … 15 h | about 3 h … 30 h |
| 5 | 540 / 40 | about 6 h … 2.5 days | about 12 h … 5 days |
| 10 | 1,080 / 80 | about 1 day … 10 days | days … weeks |
| ≈ 300 (Alonso-Mora 2017) | ≈ 35,000 / 2,000+ | not feasible with this architecture | — |

Before any run there is engineering work, not included above:
- raise the normalizer limits;
- use more than 96 nodes, which makes the n² snapshot frames larger;
- regenerate fixtures and check the limits of the Runner, adapter and wrapper;
- pass `dotnet test`.

The first measured step should be **one timing pilot job** at k = 2 or 2.5, to fit the real exponent before committing
any panel.
