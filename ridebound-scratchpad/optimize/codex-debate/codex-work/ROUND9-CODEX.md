# Round 9 — existing ladder verified

**Reproduction.** My [independent parser](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round9_reproduce_ladder_v2.py) read all **80 transcripts** for the five arms: 16 cells and 1,728 requests per arm. It checked **189,071 frame hashes**, ledger arithmetic and completed/alighted consistency. Coverage uses all requests; other rates use completed riders, pooled across cells. Sharing requires positive-duration onboard overlap; exposure means any nonzero dispatch drop revision.

| Arm | Served | Shared | Exposed | Late >60 s | >120 s | >300 s |
|---|---:|---:|---:|---:|---:|---:|
| FREE | 94.3% | 53.1% | 23.8% | 16.82% | 10.07% | 1.29% |
| LOCKS | 91.7% | 21.8% | 3.9% | 2.97% | 1.70% | 0.13% |
| C-120 | 90.5% | 19.4% | 2.6% | 1.47% | 0 | 0 |
| C-60 | 89.1% | 17.3% | 1.3% | 0 | 0 | 0 |
| C-30 | 88.8% | 15.7% | 0.4% | 0 | 0 | 0 |

**Mismatches: none in all 30 table entries**, including Claude’s written re-analysis ([counts/output:6](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round9-ladder-reproduction-2026-10-08.txt:6)). A [separate legacy-schema check:84](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round9-static-snapshot-verification-2026-10-08.txt:84) confirms exactly one travel update, snapshot.version=1, in every run; the parser’s empty version-regex results are superseded by that check.

**Point 1: observed bound confirmed; static-alone explanation needs correction.** With z=actual arrival−last promise, the exact identity is:

actual−first promise = Σc + Σx + z.

C constrains Σ|c|≤B, so the bound is B+Σx+z. Static snapshot version does **not** imply x=0: C-30 contains **41,314 nonzero exogenous ledger revisions**. However, cumulative signed x is **−997…0 ms** there, and z=0. Across all five arms, cumulative signed x is nonpositive and z=0. All capped histories respect C; maximum actual lateness is **119.434 s, 57.105 s, 27.641 s** for C-120/60/30 ([output:11](E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/round9-ladder-reproduction-2026-10-08.txt:11)). Thus the recorded bounds follow mechanically from these additional verified conditions. Static traffic generally cannot exclude execution delay, reprojection drift or overrides.

**Point 2: agree on emphasis, not exclusion.** Service/sharing cost is the principal empirical result; zero lateness beyond B checks enforcement under these conditions. FREE/LOCKS tails and within-cap frequency remain informative. For example, C-120 recovers **29/50=58%** of the LOCKS→C-30 completion gap, but its late60 is **1.47%**; C-60 recovers only **6/50=12%**. These late60 rates concern the raw first promise; they do not evaluate Round 8’s forecast-display screen.

**Replacement: YES.** The strongest reason is that the existing ladder already measures the intended trade-off with **53.1% FREE sharing**; another 102 jobs would repeat evidence already available. I withdraw that Stage 1 proposal.

Use WP14r as the static dispatch case and T3.8 as the data-derived traffic case, including C/deadline/visible rules and the frozen forecast display. Keep their worlds, runners and policy-package differences explicit; do not pool them or transfer a cap optimum.

The new-run ceiling is **34 optional T3.8 C-120 jobs**; remaining work is re-analysis. Before any approved batch, seal ≥48 net recovered completions, forecast late60≤1%, and no overrides/enforcement failures. A failed confirmation becomes a reported negative result, without adding another grid. No simulations or thesis edits were made.
