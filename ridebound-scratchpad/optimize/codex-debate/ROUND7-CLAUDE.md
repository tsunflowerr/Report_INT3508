# Round 7 (2026-10-07): how to choose the cap value, and how to reach a high-sharing regime

Same permissions as before: write only in `codex-work/`; read anything; web search; zero hallucination; scripts and
outputs saved with mode "x".

**Independence.** Claude has one literature agent surveying the same questions into
`claude-work/SURVEY-S3-cap-value-and-pooling-regime.md`. Do NOT read that file in this round.

## The owner's questions (paraphrased)

1. Why do we keep repeating 30 s for rule C? We could choose another value. What value is appropriate, and how
   should it be justified?
2. Can we configure the data with many requests and few vehicles to raise sharing? Otherwise the argument is "little
   sharing, so few pooling-induced changes". And is each change small, under 30 s anyway?
3. Survey carefully.

## New zero-run facts from Claude (please verify; files in `claude-work/`)

**F1. The T3.8 "U" arm is not unconstrained.** `tang3/configs/U.json` and `C-30.json` both carry
`finalConfirmationLocks: [vehicle, pickupStop, pickupEta]` plus hard limits of 0 on vehicle switches and on
pickup/drop stop switches. U differs from C-30 only by having no `drop_eta_total_ms` limit. U is therefore like WP14's
`c1-nobudget`, not like the free `b1` baseline.

**F2. Fewer vehicles, from WP9 H6 v2** (`fleet_size_wp9_check.py` → `fleet-size-wp9-check-2026-10-07.txt`). Older
Runner and WP9 world; 108 requests per cell; descriptive only.

| panel | vehicles | arm | served | shared | drop-exposed |
|---|---|---|---|---|---|
| A | 8 | b1 (rolling cost, no commitment) | 80.6% | 50.1% | 22.7% |
| A | 8 | c1 (tight 30 s) | 74.1% | 16.6% | 1.8% |
| B | 4 | b1 | 44.7% | 58.4% | 26.9% |
| B | 4 | c1 | 39.8% | 21.9% | 2.9% |

**F3. A budget frontier already exists.** `C:/Code/RideBound-noworse/docs/benchmarking/wp14r-013-v6-matrix-and-h6-rerun-2026-09-05.md:74-86`,
16 cells, older world:

| arm | served |
|---|---|
| b1-ref | 94.27% |
| c1-nobudget | 91.67% |
| budget 120 | 90.45% |
| budget 60 | 89.12% |
| budget 30 (h6ref) | 88.77% |

The pickup lock, freeze and ratchet ablations were inert.

**F4. Changes are rare but large, not small.**
- Under T3.8 U, a nonzero dispatch drop revision has |c| median 108.6 s, p90 260.6 s, max 554.8 s
  (`optimize/report-extras/constraints-and-pooling-2026-10-06.txt`).
- The insertions C-30 blocked would have overshot 30 s by a median of 110 s (`budget-block-diagnosis-2026-10-07.txt`).
- Under C-30 the largest recorded dispatch change is 29.2 s.

**F5. Display rounding.** The configs set `materialRevisionRule.displayBucketWidthMs = 60000`: riders see ETAs in
1-minute buckets.

## Tasks (write `codex-work/SURVEY-CAP-AND-REGIME-CODEX.md`, under 2,000 words, plus any scripts)

**A. Verify F1–F5** against code, configs and outputs. Say whether U = c1-nobudget in behaviour, or what differs.

**B. Survey: how to choose the cap value.** Primary sources only, with verbatim quotes. Cover:
- rider tolerance or perception of ETA changes and lateness (minute rounding, notice thresholds, the size of changes
  apps avoid);
- industry guarantees (e.g. Uber's delayed-ride guarantee at 5 min);
- DRT/DARP slack and time-window conventions (Schulz & Pfeiffer's l, max ride ratios, paratransit windows);
- how papers choose such caps: sweep plus frontier, or a threshold from the literature.

Then propose 2–3 defensible ways to pick our value. Candidates:
- half or one display bucket (30–60 s);
- the knee of a measured served-vs-reliability frontier;
- the rider's trip-length share.

**C. Survey: what raises sharing in simulation.** Demand-to-fleet ratio, demand density, wait and detour windows,
reassignment and commitment locks (e.g. Fielbaum & Alonso-Mora 2020 on protecting announced waits), and which of these
our tool can change within its limits (≤ 128 requests, ≤ 32 vehicles, ≤ 96 nodes, 10-min pickup window, 1.5× ride).
Use F2 and F3.

**D. Recommend ONE design** that answers the owner within the thesis's single storyline: rule C caps system-caused
change, the forecast display covers anticipated traffic, and the ledger records the rest.
- Which cap values, which sharing regime, how many jobs.
- What prediction to seal.

Keep it to the smallest design that answers both questions credibly.

Finish with a short message listing the files you wrote.
