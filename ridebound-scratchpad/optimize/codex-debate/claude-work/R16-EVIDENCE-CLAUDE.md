# R16 evidence (Claude-side analyst): Q2 cap dial, Q3 accumulation, Q4 cost-first — existing data only

2026-10-10. Zero runs: no simulation, build, install or deletion. Every number below comes from a script I ran over
existing transcripts (outputs created with mode "x") or from a file:line I opened. Labels: **[M]** measured on recorded
runs; **[S]** first-order screen on a recorded path (not a policy result, not a bound — R15 correction 4);
**[I]** inference; **[H]** hypothesis; **[A]** my arithmetic on the cited numbers.

## Summary (details and anchors below)

- **Q2, the dial.** On the 8 w07 cells (07–09 h only) the dial C-30 → U buys +5 served for +3 naive late > 60 s
  (+7 late > 120 s); timely completions are flat. This window is not representative: on T3.8, 91 of the 96 riders C-30
  loses are in 08–10 h and 17–19 h. On WP14r (fixed traffic), C-30 → C-60 buys +6 riders for 0 extra late riders.
  From C-60 upward each step costs about one rider more than 60 s late per extra rider (C-60 → C-120: +23 for +23;
  C-120 → LOCKS: +21 for +24). At the 120-s threshold, C-60 → C-120 costs nothing and C-120 → LOCKS costs 27 riders
  (Tables 1–3).
- **Q2, the 1,256 and the 148.** The 1,256 are candidate records in 971 decisions. 807 of the 973 request–run pairs they
  touch were served anyway. First order on T3.8, B = 120 s lets 59 of the 148 pass and pushes about 51 co-riders past
  60 s, but only 6 past 120 s. The screen matched realised net counts on w07 (6 vs +6), but the served set reshuffled
  (17 in, 11 out) (Table 4).
- **Q3.** Riders with ≥ 2 nonzero dispatch moves are 0.19–0.49% under stability-first and 3.1–4.1% under cost-first.
  They take long, crowded trips. A cumulative budget differs from a per-step cap only at B ≈ 90–300 s on cost-first paths
  (3.5–10.4 per 1,000). In this thesis the clause is behaviourally inert, but it is a correct per-trip guarantee
  (Tables 5–6).
- **Q4.** T3.8 transcripts cannot answer it: they record no candidate costs. WP14r portfolios can, with configs
  byte-identical to T3.8's. An exact re-selection reproduces 62,837/62,837 recorded choices. First order, cost-first
  under the same gates re-picks 26.0% of new-request decisions under U's gates (median +90.8 s incumbent drop movement,
  −7.8% plan cost) but only 6.1% under C-30's gates (≤ 35.5 s). Of FREE's 401 promise-changing decisions, only 76 are
  gate-forbidden. So the FREE → LOCKS gap is mostly ranking (Tables 7–8).

## Anchor keys

Scripts and outputs are in `E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/claude-work/r16-evidence/`
(Python `E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -B`, `PYTHONIOENCODING=utf-8`, ≤ 4 worker processes).

| Key | Output file (script) |
|---|---|
| DIAL | `q2-cap-dial-2026-10-10.txt` (`q2_cap_dial.py` v1; its w07 and WP14r lines are valid, its T3.8 forecast lines are superseded, see "Bug") |
| DIAL2 | `q2-cap-dial-t38-v2-2026-10-10.txt` (`q2_cap_dial.py` v2, population t38) |
| SCR | `q2-budget-screen-2026-10-10.txt` (`q2_budget_screen.py`) |
| IDN | `q2-screen-identity-w07-2026-10-10.txt` (`q2_screen_identity_w07.py`) |
| REC | `q2-records-to-requests-2026-10-10.txt` (`q2_records_to_requests.py`) |
| MC | `q3-multi-change-riders-2026-10-10.txt` (`q3_multi_change_riders.py`) |
| WIN | `q3-t38-windows-2026-10-10.txt` (`q3_t38_windows.py`) |
| CF | `q4-cost-first-reselect-2026-10-10.txt` (`q4_cost_first_reselect.py`) |
| GD | `q4-free-gate-decomposition-2026-10-10.txt` (`q4_free_gate_decomposition.py`) |
| RET | `q4-retention-check-2026-10-10.txt` (`q4_retention_check.py`) |
| PP / PF | `probe-portfolio-presence.txt` / `probe-portfolio-frame-LOCKS.txt` (read-only structure probes) |
| SRC | `C:/Code/RideBound-noworse/src/` (read only) |
| FJ | `claude-work/r13-final-judge/cumulative-decisive-check-2026-10-10.txt` |
| W14 | `C:/Code/RideBound-noworse/docs/benchmarking/wp14r-013-v6-matrix-and-h6-rerun-2026-09-05.md` |

**Reader validation (my scripts reproduce earlier, independently checked numbers).** T3.8 naive: U 2,434 served /
203 / 102 / 18 late > 60/120/300 s, C-30 2,338 / 76 / 11 / 0; timely60 2,231 / 2,262; timely120 2,332 / 2,327; forecast
late60 137 / 10, timely60 2,297 / 2,328, timely120 2,347 / 2,338, early60 0.33% / 0.17% (DIAL2:7-10) — identical to
`cap-vs-pad-frontier-2026-10-07.txt:4,12,25,33` and R15 A:7-9. Shared 22.80 / 13.39% and drop-exposed 7.15 / 1.41%
(DIAL2:7,9) = `pooling-share-2026-10-06.txt:2-3`, `exposure-check-2026-10-06.txt:2-3`. WP14r served/late60 (DIAL:80-92) =
`wp14r-ladder-reanalysis-2026-10-08.txt:2-6`. Screen 148 / 116 / 11 / 59 / 135 and overshoot quartiles (SCR:5-13) =
`budget-block-diagnosis-2026-10-07.txt:2-10`. 1,256 records (REC:12) = FJ:4-30. Cumulative-only exposure (MC:10,25,34,43,52)
= `r13-proposer/cumulative-vs-perinsertion-2026-10-10.txt`. LOCKS decision-induced drop seconds 7,496.4 (GD:10) = W14:77
attributed burden 7,496,399 ms.

**Bug found and fixed in my own script.** `q2_cap_dial.py` v1 counted forecast lateness only in forecast-active cells, so
its T3.8 forecast lines (DIAL:35-78) dropped the 13 inactive cells. v2 counts inactive cells at the naive promise
(docstring of `q2_cap_dial.py`); v2 reproduces the published forecast numbers (above). The w07 forecast lines are
unaffected (all 8 w07 cells are active under the rule used there); WP14r has no forecast. A copy of v1 is kept as
`q2_cap_dial_v1_superseded.py.txt`.

---

## Q2a. The existing cap dial, with lateness against the FIRST drop promise

Definitions (all populations): served = passengerAlighted with an initial drop promise; late_k = A − p0 > k s;
timely_k per request = served − late_k; early60 = A − p0 < −60 s; drop-exposed = any later drop revision with dispatch
part c ≠ 0; shared = another served rider on the same vehicle with overlapping on-board time.

### Table 1 — w07/w07x, 8 cells, 07:00–09:00 on 12–13 Nov 2018, measured traffic, 864 requests per arm [M]

Forecast columns use **loo-no15**, the NON-CAUSAL sensitivity rule (sources 13, 14, 16 Nov for 12 Nov; 12, 14, 16 Nov for
13 Nov; `optimize/display_layer.py:11-16`), because the primary causal rule is inactive on 12–13 Nov. Treat them as
optimistic. Budget-pruned records from FJ:7-30.

| Arm | Budget-pruned records | Served | Late > 60 | > 120 | > 300 | Timely60 | Timely120 | Exposed | Shared | FC late > 60 | FC > 120 | FC timely60 | FC timely120 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C-30 | 142 | 660 | 47 | 2 | 0 | 613 | 658 | 0.30% | 11.67% | 0 | 0 | 660 | 660 |
| C-60 | 106 | 661 | 47 | 2 | 0 | 614 | 659 | 0.45% | 11.95% | 0 | 0 | 661 | 661 |
| C-90 | 71 | 664 | 50 | 4 | 0 | 614 | 660 | 1.05% | 13.40% | 4 | 0 | 660 | 664 |
| C-120 | 38 | 666 | 51 | 7 | 0 | 615 | 659 | 1.35% | 14.41% | 7 | 1 | 659 | 665 |
| C-150 | 26 | 666 | 51 | 7 | 0 | 615 | 659 | 1.35% | 14.41% | 7 | 1 | 659 | 665 |
| C-180 | 18 | 666 | 51 | 7 | 0 | 615 | 659 | 1.35% | 14.41% | 7 | 1 | 659 | 665 |
| C-240 | 6 | 665 | 50 | 9 | 1 | 615 | 656 | 1.65% | 14.74% | 9 | 3 | 656 | 662 |
| C-300 | 4 | 665 | 50 | 9 | 1 | 615 | 656 | 1.65% | 14.74% | 9 | 3 | 656 | 662 |
| U | — | 665 | 50 | 9 | 1 | 615 | 656 | 1.65% | 14.74% | 9 | 3 | 656 | 662 |
| M⁺-30 | — | 660 | 47 | 2 | 0 | 613 | 658 | 0.30% | 11.67% | 0 | 0 | 660 | 660 |
| M⁺-60 | — | 661 | 47 | 2 | 0 | 614 | 659 | 0.45% | 11.95% | 0 | 0 | 661 | 661 |
| M⁺-120 | — | 664 | 51 | 5 | 0 | 613 | 659 | 1.05% | 13.86% | 5 | 1 | 659 | 663 |
| M⁺-300 | — | 665 | 50 | 9 | 1 | 615 | 656 | 1.65% | 14.74% | 9 | 3 | 656 | 662 |
| V-30 | — | 660 | 47 | 2 | 0 | 613 | 658 | 0.30% | 11.67% | 0 | 0 | 660 | 660 |

Source DIAL:4-31. Early > 60 s is 0 in every naive row and 2 (0.30%) in every forecast row; the mean forecast quote
extension is 20.9–21.1 s (DIAL:5-31).

**Trade-off curve on w07 [M, A].** From C-30 to U the dial buys **+5 served** (660 → 665) for **+3 late > 60 s and +7
late > 120 s** naive, or **+9 late > 60 s** with the (non-causal) forecast quote. Step by step: C-30→C-60 +1 served, +0
late60; C-60→C-90 +3, +3; C-90→C-120 +2, +1; C-120→C-180 0, 0; C-180→C-240 −1, −1. C-240 and C-300 coincide with U on
every column. Timely60 per request is flat naive (613–615) and, with the forecast quote, peaks at C-60 (661) and is
lowest at C-240/C-300/U (656). At this window the dial barely matters.

**Why w07 cannot answer Q2 [M].** It is 8 cells of one window (07–09 h) on the two development days. On the 34 T3.8
cells the cap costs only 5 riders in 07–09 h but 39 in 08–10 h and 52 in 17–19 h (T38-REPORT.md:50-52; reproduced
DIAL2:18-42), and in 07–09 h lateness is traffic-dominated: naive late60 is 47–51 for every arm on w07 (Table 1), and
U 70 vs C-30 61 in the T3.8 w07 window, against U 66 vs C-30 0 in w17 (Table 2).

### Table 2 — T3.8, 34 test cells, measured traffic, 3,672 requests [M]

Forecast = causal-no15 (primary rule; 21 active cells; inactive cells at the naive promise). Source DIAL2.

| Arm (cells) | Requests | Served | Late > 60 | > 120 | > 300 | Timely60 | Timely120 | Exposed | Shared | FC late > 60 | FC timely60 | FC timely120 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| U (34) | 3,672 | 2,434 | 203 | 102 | 18 | 2,231 | 2,332 | 7.15% | 22.80% | 137 | 2,297 | 2,347 |
| C-30 (34) | 3,672 | 2,338 | 76 | 11 | 0 | 2,262 | 2,327 | 1.41% | 13.39% | 10 | 2,328 | 2,338 |
| M⁺-30 (34) | 3,672 | 2,338 | 74 | 11 | 0 | 2,264 | 2,327 | 1.24% | 13.13% | 10 | 2,328 | 2,338 |
| M⁺-60 (34) | 3,672 | 2,347 | 79 | 11 | 0 | 2,268 | 2,336 | 1.70% | 14.06% | 14 | 2,333 | 2,347 |
| V-30 (34) | 3,672 | 2,336 | 74 | 11 | 0 | 2,262 | 2,325 | 1.11% | 12.89% | 10 | 2,326 | 2,336 |
| U, w07 (9) | 972 | 516 | 70 | 18 | 2 | 446 | 498 | 2.91% | 16.09% | 11 | 505 | 510 |
| C-30, w07 (9) | 972 | 511 | 61 | 11 | 0 | 450 | 500 | 1.37% | 13.31% | 2 | 509 | 511 |
| U, w08 (14) | 1,512 | 1,014 | 67 | 37 | 10 | 947 | 977 | 6.90% | 21.60% | 60 | 954 | 980 |
| C-30, w08 (14) | 1,512 | 975 | 15 | 0 | 0 | 960 | 975 | 0.92% | 12.10% | 8 | 967 | 975 |
| M⁺-60, w08 (14) | 1,512 | 982 | 19 | 0 | 0 | 963 | 982 | 1.43% | 13.34% | 11 | 971 | 982 |
| U, w17 (11) | 1,188 | 904 | 66 | 47 | 6 | 838 | 857 | 9.85% | 27.99% | 66 | 838 | 857 |
| C-30, w17 (11) | 1,188 | 852 | 0 | 0 | 0 | 852 | 852 | 2.00% | 14.91% | 0 | 852 | 852 |
| M⁺-60, w17 (11) | 1,188 | 856 | 1 | 0 | 0 | 855 | 856 | 2.57% | 16.00% | 1 | 855 | 856 |

DIAL2:7-47. Early > 60 s naive: U 7, C-30 3; forecast: U 8, C-30 4 (DIAL2:7-10). In w17 the forecast adds 0.1 s on
average (DIAL2:41), so it cannot help there; the cap removes all 66 naive late riders of U in w17 while serving 52 fewer.

**What is missing on T3.8 [M].** No C-B arm with B > 30 s was run on the 34 cells (`tang3/t38/run_t38.py:42-45`: arms U,
C-30, Mplus-30, Mplus-60, V-30). The only larger-budget point is M⁺-60, a different rule (deadline from the first quote,
traffic included): +9 served vs C-30, +3 naive late60, +4 forecast late60, forecast timely60 +5, forecast timely120 +9
(Table 2) [M, A].

### Table 3 — WP14r v6, 16 cells (w08 + w17, 12–13 Nov), FIXED traffic, older runner `38d517d`, 1,728 requests [M]

| Arm | Served | Late > 60 | > 120 | > 300 | Timely60 | Timely120 | Exposed | Shared | Budget-pruned records |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| FREE (b1-ref, rolling-cost) | 1,629 | 274 | 164 | 21 | 1,355 | 1,465 | 23.82% | 53.10% | — |
| LOCKS (c1-nobudget = T3.8 U config) | 1,584 | 47 | 27 | 2 | 1,537 | 1,557 | 3.91% | 21.84% | — |
| C-120 | 1,563 | 23 | 0 | 0 | 1,540 | 1,563 | 2.62% | 19.39% | 405 |
| C-60 | 1,540 | 0 | 0 | 0 | 1,540 | 1,540 | 1.30% | 17.27% | 711 |
| C-30 (c1-h6ref) | 1,534 | 0 | 0 | 0 | 1,534 | 1,534 | 0.39% | 15.71% | 848 |

DIAL:80-94; pruned records FJ:31-45. Early > 60 s is 0 in every arm (fixed traffic: lateness equals summed dispatch
movement, so C-B with B ≤ 60 s has 0 late > 60 s by construction). Steps [A]: FREE→LOCKS −45 served / −227 late60;
LOCKS→C-120 −21 / −24; C-120→C-60 −23 / −23; C-60→C-30 −6 / 0. Timely60 per request is maximal and flat between LOCKS,
C-120 and C-60 (1,537–1,540); timely120 is maximal at C-120 (1,563).

**Reading of Q2a [I].** Across all three panels, raising B buys riders mainly where the cap binds (T3.8 w08/w17, WP14r),
and each extra rider is paid for by roughly one rider late against the first promise at the 60-s threshold (WP14r steps
C-60→C-120: 23 riders for 23 late; LOCKS→C-120 21 for 24). At a 120-s threshold the price is much lower (WP14r
C-60→C-120: +23 served, 0 late > 120). On w07 the dial is nearly flat because neither the cap nor dispatch is the cause
of lateness there.

---

## Q2b. What the 1,256 and the 148 are, and what a larger B would do (first order)

### The 1,256 are candidate records, not riders [M]

| Population | Runs | Budget-prune records | Decisions | Distinct requests (per run, summed) | …served anyway in that run | …rejected |
|---|---:|---:|---:|---:|---:|---:|
| T3.8 C-30 | 34 | 845 | 641 | 643 | 495 | 148 |
| w07 C-30 … C-300 (8 arms) | 64 | 411 | 330 | 330 | 312 | 18 |
| **Total** | 98 | **1,256** | 971 | 973 | **807** | **166** |

REC:3-12 (w07 rows REC:4-11 summed [A]). **83% of the request–run pairs touched by a budget prune were served anyway**
by another candidate in the same run [A: 807/973]. Making all 1,256 records feasible "at the first attempt" would
mostly change which plan carried an already-served rider (and push a co-rider's drop time by the overshoot); the
directly blocked riders are the 166 rejected, 148 of them on T3.8 (a changed B also reshuffles who is served, see IDN below).

### Table 4 — screen of the 148 T3.8 budget-only-blocked requests at larger B [S]

Method (`q2_budget_screen.py` docstring): a request passes at B if one of its recorded budget-pruned candidates has every
reported drop witness with after = before + delta ≤ B; the blocking co-rider's drop time is then pushed by delta, added
to his realised C-30 lateness against his first promise. 0 of 845 records carry a non-drop or missing witness (SCR:4).

| B (s) | Requests passing | …of which served by U | Mean push on blocking co-rider (s) | Co-riders newly late > 60 s | > 120 s | > 300 s |
|---:|---:|---:|---:|---:|---:|---:|
| 60 | 11 | 8 | 48.7 | 5 | 0 | 0 |
| 90 | 35 | 30 | 64.9 | 28 | 1 | 0 |
| 120 | 59 | 49 | 81.1 | 51 | 6 | 0 |
| 150 | 81 | 66 | 95.8 | 72 | 25 | 0 |
| 180 | 96 | 78 | 105.8 | 87 | 40 | 0 |
| 240 | 122 | 97 | 127.8 | 112 | 66 | 1 |
| 300 | 135 | 105 | 141.0 | 123 | 79 | 3 |

SCR:3-13. 1,186 of the 1,334 rejections are structural only (SCR:5). Smallest overshoot over 30 s: median 109.6 s,
p25 63.7, p75 183.6, max 524.8 (SCR:6).

**Calibration on w07, where C-60 … C-300 were actually run [M vs S].** The same screen on the 8 w07 C-30 cells finds only
7 budget-only-blocked requests (SCR:17) and predicts 1 / 5 / 6 / 6 / 6 / 7 / 7 passing at B = 60 / 90 / 120 / 150 / 180 /
240 / 300 (SCR:19-25). The realised net served change against C-30 is +1 / +4 / +6 / +6 / +6 / +5 / +5, and **every
screen-passing request was in fact served by the corresponding C-B run** (IDN:3-9, "in both" = screen-pass). But the
served set reshuffles: at B = 120 s the run gained 17 requests and lost 11 that C-30 served (IDN:5). Lateness: the
screen predicts 4 co-riders newly late > 60 s and 3 > 120 s at B = 120 (SCR:21); realised C-120 − C-30 is +4 late60 and
+5 late120 (Table 1). So on w07 the screen got the net counts about right; the sample is tiny (7 requests vs 148).

**Reading of Q2b [S, I, A].**
- First order on T3.8, B = 120 s would admit about 59 of the 148 (1.6 pp of 3,672 requests) and push about 51 already
  accepted co-riders more than 60 s past their first promise, but only 6 more than 120 s. That is about 0.86 late
  co-riders per extra rider at the 60-s threshold, close to the WP14r measured steps (Table 3) and to the U vs C-30
  cohort ratio 96 / 127 ≈ 0.76 (R15 correction 3).
- The forecast does not absorb these pushes: its mean quote extension is 7.4 s for C-30 (DIAL2:10), against a mean push
  of 81.1 s at B = 120. Not computed against the forecast quote; inference only.
- Arithmetic only, not a policy result: naive timely120 for C-30 is 2,327 (Table 2); adding 59 riders minus 6 newly late
  beyond 120 s gives about 2,380, above U naive 2,332, U + forecast 2,347 and the padded U 2,366 (R15 §2). The w07 calibration
  realised only +1 timely120 at B = 120 (659 vs 658), against +3 implied by the screen. This needs the C-120 run on the 34
  cells (verdict item A3) before anyone can write it as a result.
- **Answer to the owner's Q2:** a larger B is "better" only under a lateness tolerance of about 2 minutes. At a
  1-minute tolerance it trades roughly one late rider for one extra rider. The 1,256 records mostly do not stand for
  lost riders.

---

## Q3. Where accumulation could bind

### Table 5 — riders with ≥ 2 nonzero dispatch changes of the drop promise, uncapped arms [M]

k = number of later drop revisions with c ≠ 0. Direct-time proxy = maxRideTimeMs / 1.5 (maximumRideTimePermille 1500 in
every grid). Co-riders = other served riders with overlapping on-board time on the same vehicle.

| Population (objective, traffic, fleet) | Accepted | k ≥ 2 | Direct min k≥2 / k=0 (median) | Ride min k≥2 / k=0 | Co-riders mean k≥2 / k=0 | Single change k=1 (median s) | k≥2 changes: first / later median (s) | Min between changes (median) | Changes before boarding |
|---|---:|---:|---|---|---|---:|---|---:|---:|
| T3.8 U (stability-first, measured, 8 veh) | 2,434 | 12 (0.49%) | 11.8 / 6.1 | 15.7 / 6.8 | 2.42 / 0.18 | 111.7 | 40.6 / 99.0 | 4.5 | 12 of 25 |
| w07 U (stability-first, measured, 8 veh) | 665 | 0 | — | — | — | — | — | — | — |
| WP14r LOCKS (stability-first, fixed, 8 veh) | 1,584 | 3 (0.19%) | 10.3 / 4.9 | 15.0 / 4.9 | 3.00 / 0.22 | 98.2 | 25.7 / 156.0 | 2.2 | 4 of 6 |
| WP14r FREE (cost-first, fixed, 8 veh) | 1,629 | 50 (3.07%) | 7.5 / 4.6 | 10.1 / 4.8 | 2.14 / 0.48 | 97.3 | 105.2 / 90.8 | 2.9 | 83 of 103 |
| WP9 A b1 (cost-first, fixed, 8 veh, older runner) | 1,735 | 71 (4.09%) | 11.2 / 5.5 | 15.0 / 5.6 | 2.38 / 0.48 | 118.2 | 104.7 / 126.7 | 4.0 | 103 of 147 |
| WP9 B b1 (cost-first, fixed, 4 veh, older runner) | 966 | 38 (3.93%) | 9.4 / 5.4 | 12.9 / 5.5 | 2.29 / 0.58 | 115.2 | 127.8 / 69.8 | 3.1 | 63 of 79 |

MC:3-52. Share of k ≥ 2 riders with ≥ 2 co-riders: 100% (T3.8 U), 86.0% (FREE), 95.8% (WP9 A), 92.1% (WP9 B), against
1.5–11.6% for k = 0 riders (MC:4,6,19,21,37,39,46,48). Booking time (minutes after window start, median): 64 vs 54 for
k≥2 vs k=0 on T3.8 U (MC:4,6). T3.8 U by window: w07 1, w08 5, w17 6 riders with k ≥ 2 (WIN:3-5). By day, 10 of the 12 are
on the weekend days 17–18 Nov and 8 on 18 Nov alone [A, WIN:8-19]. One of the 12 has a "nonzero" change that rounds to
0.0 s (WIN:12). Only 1 of the 360 changes of all k ≥ 2 riders (25 + 103 + 6 + 147 + 79 [A]) moved a promise earlier
(MC:7,22,31,40,49).

### Table 6 — cumulative-only riders (every change ≤ B < sum) per 1,000 accepted, same paths [M; exposure, not a policy result]

| Population | B = 30 | 60 | 90 | 120 | 180 | 300 |
|---|---:|---:|---:|---:|---:|---:|
| T3.8 U | 0 | 0 | 0.41 | 1.64 | 0.41 | 0 |
| w07 U | 0 | 0 | 0 | 0 | 0 | 0 |
| WP14r LOCKS | 0 | 0 | 0 | 0 | 1.26 | 0 |
| WP14r FREE | 1.23 | 0 | 3.68 | 7.98 | 9.21 | 3.68 |
| WP9 A b1 | 0 | 0.58 | 3.46 | 6.92 | 10.37 | 10.37 |
| WP9 B b1 | 0 | 0 | 5.18 | 10.35 | 5.18 | 10.35 |

MC:10,16,25,34,43,52 (counts are printed there with the per-1,000 rates). For comparison, per-step-exceed riders at
B = 30 s are 13.5 (w07 U) to 238.1 (WP9 B) per 1,000 (same lines).

### Where a cumulative budget would act differently from a per-step cap [I, H]

A difference needs three things at once: a rider gets ≥ 2 nonzero dispatch moves, each move is ≤ B, and their sum
exceeds B.
1. **The objective drives the first condition.** Cost-first / rolling-cost paths have 3.07–4.09% k ≥ 2 riders;
   stability-first paths have 0.19–0.49% (Table 5). Fleet size under rolling-cost barely moves it (8 vehicles 4.09%,
   4 vehicles 3.93%), but WP9 A and B are different cohorts (R15 row 60 caveat), so load is not isolated. Under an
   enforced cap the cap itself suppresses repeats: no enforced-C rider on measured traffic had two nonzero changes
   (fact pack §1; `budget-use-check-2026-10-09.txt`), and WP14r C-120 had one (`wp14r-budget-use-2026-10-10.txt:10`).
2. **B must be near the size of a typical single move.** Single moves have medians of about 97–118 s (Table 5), so at
   B = 30–60 s almost no multi-move rider has all moves ≤ B (0–2 riders per population). The cumulative-only rate is
   material only at B = 90–300 s and only on cost-first paths (3.5–10.4 per 1,000; Table 6).
3. **Who.** Long trips (direct proxy about 9–12 min against about 5–6 min), on vehicles carrying ≥ 2 other riders, with
   moves a few minutes apart, mostly before boarding on cost-first paths (Table 5). Time of day is not a clear driver;
   on T3.8 the few cases cluster on the weekend cells (WIN), which is 12 riders and cannot be generalised.
4. **Regime estimate [H].** A cumulative budget would act differently in roughly 0.4–1% of riders only under a
   cost-first (or cost-heavier) objective with B of about 90–300 s, on paths with long, heavily shared trips. The Q4
   re-selection supports the direction: under cost-first with C-120 gates, 325 decisions change and the extra
   incumbent drop movement has median 57.3 s (CF:16,18), that is, two moves can fit under one 120-s budget.
   Recorded witnesses also point to fixed traffic and B ≥ 60 s: 6 records in 4 decisions on WP14r C-60/C-120 (FJ:31-45).

**Is the cumulative clause inert in this thesis? [M + I]** Behaviourally, yes, on the tested measured-traffic regime:
- 0 of 1,256 recorded budget prunes needed prior spending (FJ:4-30);
- uncapped stability-first paths expose at most 1.6 riders per 1,000 at B ≤ 180 s (Table 6);
- the 34-cell panel has only B = 30 s, where exposure is 0.

It is not inert as a specification. It is what makes the bound a per-trip total: a per-step cap of 30 s would allow
k × 30 s (k reached 3 in these runs, MC:3,18,36,45). No run has shown that this matters for outcomes. A per-step
counterfactual trajectory was never run (R15 row 32).

**Honest thesis sentence (English).** "Rule C bounds the total dispatch-induced movement of each rider's promised
drop-off time over the whole trip. In our measured-traffic experiments every refusal by this budget was already caused
by a single move larger than B. The cumulative form therefore guarantees the bound but did not change any recorded
decision. It would matter only under a cost-first objective with budgets of about 1.5–5 minutes, which we did not test
on measured traffic."

**Vietnamese (simple).** "Luật C giới hạn tổng số giây mà các quyết định điều phối được phép dời giờ trả của mỗi khách
trong cả chuyến. Trong các lần chạy với giao thông đo thật, mọi lần luật này từ chối đều do một lần dời đã vượt mức B
ngay từ đầu. Nên phần 'cộng dồn' là bảo đảm đúng về mặt định nghĩa, nhưng chưa làm thay đổi quyết định nào đã ghi lại.
Nó chỉ có thể có tác dụng khi bộ chọn ưu tiên chi phí và mức B khoảng 1,5–5 phút, điều chưa được thử trên giao thông đo
thật."

---

## Q4. Cost-first selection under the same hard gates

### What the code does [M, code]

- Levels of the selection (`SRC/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs`):
  - forced-reference count, only when some candidate is a forced reference (:276-295);
  - accepted-request count, maximise (:297-303);
  - under HardVector with any applicable hard limit (:271-272): worst-hard-utilisation (MinMaximum, :319-325), then the
    ten revision dimensions (:326-329; AddRevisionObjectives :510-522);
  - operational cost (:365-368);
  - per-vehicle candidate-id rank tie-breaks (:370-386).
- Solver: exactly one candidate per vehicle (`SRC/RideBound.Solvers.OrTools/OrToolsCandidateSelectionSolver.cs:355`),
  each new request at most once (:364), sum or max aggregation (:383-402), and lexicographic fixing of earlier levels
  (:406-409).
- The hard gates act before selection: the hard-vector assessor filters candidates
  (`SolverBackedRidePoolingPolicy.cs:322-323`).
- FREE is `rolling-cost`: the profile defaults to RollingCost (:287) and the switch at :290 has no RollingCost case, so
  there is no commitment filter. Its recorded levels are accepted
  → operational cost → id rank (PP:17).
- **"Cost-first under the same gates"** therefore means: keep the eligible set, and drop levels :319-331 so that cost
  follows the accepted count directly.

### What the records allow [M]

- T3.8 and w07 transcripts (evidenceVersion 1.1.0) carry no candidate portfolio (PP:2-13). Their selection evidence
  holds only the chosen plan's level values and the infeasible (pruned) candidates (`probe-t38-U-w08-skip40.txt`). **So
  "how often the chosen candidate was not the cheapest feasible one" cannot be measured on T3.8 or w07.**
- WP14r (evidenceVersion 1.2.0, profile `retained-portfolio-full-witness-v1`,
  `wp14-development-ridebound-hard-vector-v1.json:24`) records each decision's retained candidates with
  `policyEligibility`, `objectiveContributions` aligned with `selectionProblem.objectiveLevels`,
  `schedule.operationalCost` and `selectedCandidateIds` (PP:14-25; PF:733-837).
- The WP14r commitment configurations are byte-identical to T3.8's (sha256 of `U.json` = `wp14-c1-nobudget-v1.json` =
  998a0a94…; `C-30.json` = `wp14-c1-h6-reference-v1.json` = d6124f3f…; C-60 and C-120 identical by `diff`). The runner and
  world differ:
  - commit 38d517d vs 1ce15e9;
  - T3.8 adds `commitmentRecovery`/`lateBoarding`, `tang3/configs/wp4-tier3-v2.json:7-8`;
  - fixed vs measured traffic.
- Retention never truncated in WP14r (0 caps applied, 0 omitted by cap, 0 work-budget exhaustions; RET:2-6), so the
  portfolio is the whole feasible generated set.

### Table 7 — first-order cost-first re-selection on the recorded WP14r portfolios [S on recorded states]

For each acknowledged decision I re-solved the selection exactly (dynamic program over the covered new requests, with
'maximum' levels handled by threshold filtering). With all recorded levels it reproduces the recorded selection in
**62,837 of 62,837 frames** (5 arms [A]). With cost-first levels (forced, accepted, cost, id rank) on the same eligible set:

| Gates (arm) | Frames | …with a new request | Cost-first picks differently | % of new-request frames [A] | Accepted count changes | Cost saving where different (mean / median / max) | Extra incumbent drop-ETA movement per differing frame (median / p90 / max, s) | Frames with > 60 s extra |
|---|---:|---:|---:|---:|---:|---|---|---:|
| LOCKS (= T3.8 U config) | 12,663 | 1,714 | 445 | 26.0% | 0 | 7.79 / 7.10 / 30.75% | 90.8 / 183.8 / 390.8 | 286 |
| C-120 | 12,525 | 1,715 | 325 | 19.0% | 0 | 7.96 / 7.56 / 30.75% | 57.3 / 108.6 / 236.9 | 160 |
| C-60 | 12,364 | 1,716 | 173 | 10.1% | 0 | 7.68 / 6.80 / 30.75% | 21.7 / 53.3 / 106.6 | 2 |
| C-30 | 12,325 | 1,715 | 104 | 6.1% | 0 | 8.00 / 7.25 / 30.75% | 12.5 / 25.0 / 35.5 | 0 |
| FREE (validation of rolling-cost) | 12,960 | 1,714 | 0 | 0% | 0 | — | — | — |

CF:4-43. In the differing frames the cost-first plan moves incumbents' drop ETAs more in 424/445 (LOCKS), 304/325,
152/173 and 81/104 (CF:7,16,25,34). Summed over the differing frames the extra decision-induced drop movement is
+42,714.7 s for LOCKS and +1,196.1 s for C-30. In every arm the pickup-ETA and switch revision levels change by 0
(CF:10,19,28,37). The extra drop seconds are a plan-level sum over incumbents; the per-rider budget still holds under the
C gates.

The prior WP9 measurement (C1 at 30 s: the local choice changes in 28/3,794 = 0.738% of vehicle choice sets;
`C:/Code/RideBound-noworse/docs/handoffs/wp14-continuation-2026-08-25.md:114`,
`docs/reviews/wp1-wp13-optimization-and-fairness/README.md:155`) is of the same order as my C-30 row (0.84% of all frames; a different unit, fleet-level frames). **It
does not carry over to U's gates**: there the stability levels change about a quarter of all new-request decisions.

### Table 8 — decomposing FREE's promise-changing decisions by what LOCKS would do (FREE's own path) [M]

GATE = a decision-induced change that LOCKS forbids:
- a vehicle, pickup-stop or drop-stop switch (hardLimit 0, `wp14-c1-nobudget-v1.json`);
- or a pre-boarding pickup-ETA change (finalConfirmationLocks pickupEta; `SRC/RideBound.Domain/Commitments/CommitmentLockEvaluator.cs:55-58`,
  compared with the exogenous projection :157-160, exact equality :204-207).

RANK = only drop-ETA changes, which LOCKS permits and only ranks lower.

| Arm | Decisions | GATE | RANK | NONE | Drop seconds in GATE / RANK decisions |
|---|---:|---:|---:|---:|---|
| FREE (b1-ref) | 12,960 | 76 | 325 | 12,559 | 14,953.5 / 33,555.4 |
| LOCKS control | 12,663 | 0 | 63 | 12,600 | 0 / 7,496.4 |

GD:3-12. All 76 GATE decisions are pre-boarding pickup-ETA changes; FREE made **0** vehicle or stop switches (GD:7).
Caveat (GD docstring): a rider not yet in WaitingPickup carries only the vehicle lock
(`CommitmentLockEvaluator.cs:42,72`; WaitingPickup starts at BookingConfirmed, `SRC/RideBound.Application/State/EventReducer.cs:204-205`),
so 76 is an upper bound. **[A]** 325 of the 401 promise-changing FREE decisions (81%), carrying 69% of FREE's
decision-induced drop seconds, are choices the LOCKS gates permit. Only the stability ranking would stop them.

### Reading of Q4 [I, H] — what cost-first under the same gates would most likely change

1. **The FREE → LOCKS package difference is mostly ranking, not gates [I].** First order:
   - LOCKS's gates forbid at most 76 of FREE's 401 promise-changing decisions (Table 8);
   - cost-first with LOCKS's gates re-picks 445 decisions, almost all by moving an incumbent's drop ETA later
     (Table 7);
   - its summed extra drop movement (+42,715 s) is of the same order as all of FREE's decision-induced drop seconds
     (48,509 s [A], GD:4-5), against LOCKS's own 7,496 s.
2. **Prediction for U-cf (no drop cap) [H].** Lateness against the first promise would rise toward FREE's (WP14r: FREE
   late60 16.82% vs LOCKS 2.97%, Table 3). Service and sharing would probably rise as well, since cost saving frees
   capacity (FREE +45 served, shared 53.1% vs 21.8%). The size of the service gain cannot be predicted zero-run: FREE's
   +45 mixes the pickup lock and the ranking, and later states diverge.
3. **Prediction for C-30-cf [H].** Small first-order change: 6.1% of new-request decisions, extra plan movement ≤ 35.5 s,
   cost saving of about 8% of plan cost in those decisions (about 0.5% per new-request decision [A]). The 30-s per-rider
   budget still binds, so under fixed traffic late > 60 s stays 0 by construction; under measured traffic only traffic
   is added. This makes the "cap alone suffices at B = 30 s" hypothesis plausible.
4. **Reviewer attack: "is reliability from the cap or from a conservative dispatcher?" [I].** On this first-order
   evidence: at B = 30 s it is mostly the cap; without a drop cap (U/LOCKS) it is the stability-first ranking, not the
   locks.
5. **Link to Q3 [H].** Cost-first with C-120 gates is where the cumulative clause is most likely to bind (19.0% of
   new-request decisions re-picked; extra movement median 57.3 s).
6. **What is missing.**
   - The T3.8 portfolio evidence: it would need re-running with the retained-portfolio profile, which is a run.
   - Any cost-first trajectory: every cost-first number above is first order, the same state with one decision changed.
   - WP14r has fixed traffic, an older runner and only w08/w17 cells on 12–13 Nov.
