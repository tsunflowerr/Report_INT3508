# R34 complementary number checks (second report)

Read `CODEX-PARALLEL-RULES.md`, `WRITING-BRIEF.md`, ADDENDUM-1 §0, the revised draft and ADDENDUM-4. All writes are exclusive new text files in the authorized subfolder. No simulation, build or install.

The following statuses concern the assigned complementary numbers, not the master verdict. Line numbers are one-based in `08-chuong4-phanA-v4.tex`.

## Fixed traffic: AGREE

Independent raw reading of all 80 transcripts under `E:/RideBoundData/wp14r/development-v6-ledger/`. Sharing is counted with an on-board event sweep on half-open actual pickup/alight intervals; dispatch movement is computed as nonzero published drop ETA minus exogenous drop ETA in a ledger revision. This avoids the reviser’s pairwise overlap implementation and does not import any project analyzer. All parsed relevant frames are hash/length checked.

| v4 line | Arm | Served | Shared | Dispatch-moved | Own raw output anchor |
|---|---|---:|---:|---:|---|
| 493 | FREE | 1,629 | 865 (53.1%) | 388 (23.8%) | `extra-probe-output-v2.txt:2–17` |
| 494 | U | 1,584 | 346 (21.8%) | 62 (3.9%) | `extra-probe-output-v2.txt:18–33` |
| 495 | C-120 | 1,563 | 303 (19.4%) | 41 (2.6%) | `extra-probe-output-v2.txt:34–49` |
| 496 | C-60 | 1,540 | 266 (17.3%) | 20 (1.3%) | `extra-probe-output-v2.txt:50–65` |
| 497 | C-30 | 1,534 | 241 (15.7%) | 6 (0.4%) | `extra-probe-output-v2.txt:66–81` |

The draft’s counts and all ten one-decimal percentages agree: shared 865/346/303/266/241 and moved 388/62/41/20/6. Denominators are the respective served cohorts 1,629/1,584/1,563/1,540/1,534. Draft caption lines 483–485 labels this correctly. Existing corroboration: C4A-04, WBU:4/7/10/13/16; those were not substituted for this raw count.

## Full morning ladder: AGREE

Own raw reading of U and every C level, 72 transcripts on the same eight morning scenarios. Strict lateness means actual alight time minus the initial published drop ETA exceeds the threshold; “timely” is served minus the strict lateness count. Every run has 108 requests.

| v4 line | Arm | Served | Late >60 s | Timely ≤60 s | Timely ≤120 s | Own output anchor |
|---|---|---:|---:|---:|---:|---|
| 529 | U | 665 | 50 | 615 | 656 | `extra-probe-output-v3.txt:82` |
| 530 | C-30 | 660 | 47 | 613 | 658 | `extra-probe-output-v3.txt:83` |
| 531 | C-60 | 661 | 47 | 614 | 659 | `extra-probe-output-v3.txt:84` |
| 532 | C-90 | 664 | 50 | 614 | 660 | `extra-probe-output-v3.txt:85` |
| 533 | C-120 | 666 | 51 | 615 | 659 | `extra-probe-output-v3.txt:86` |
| 533 | C-150 | 666 | 51 | 615 | 659 | `extra-probe-output-v3.txt:87` |
| 533 | C-180 | 666 | 51 | 615 | 659 | `extra-probe-output-v3.txt:88` |
| 534 | C-240 | 665 | 50 | 615 | 656 | `extra-probe-output-v3.txt:89` |
| 534 | C-300 | 665 | 50 | 615 | 656 | `extra-probe-output-v3.txt:90` |

The grouped values at v4 lines 533–534 and the plotted coordinates at lines 643–648 agree. Corroboration: C4A-05 and the older independent CAP:3–11.

## Morning archived subset: AGREE

At v4 lines 128–130, **136 of 192** is correct. Own directory/summary inventory gives 88 morning runs plus 104 extension runs, all succeeded; the chapter selects 17 arms × 8 scenarios = 136. The remaining 56 are M-30: 8, V-120: 8, V-150: 8, V-180: 8, V-240: 8, V-30: 8, V-90: 8. Anchor: `extra-probe-output-v3.txt:93–95`. This confirms the archived inventory, not a new run. The code corroboration is RW7:33–34 and RW7X:35–36.

## Snow requests: AGREE

At v4 lines 134–136, **864 requests** is correct: 8 raw final states × 108; 601 served. Per-run served counts in the probe’s sorted order: 86, 75, 74, 66, 80, 85, 75, 60. Own raw anchors: `extra-probe-output-v3.txt:74–81` and total at line 91. Existing corroboration: C4A-06 / INV:14–15,17–22.

## “B14 (1.075)” in round brief: AGREE on number; identifier correction

At v4 lines 449–454, the group with no recorded budget-block evidence is **1,186 = 111 served by U + 1,075 rejected by U**. The group with recorded evidence is **148 = 116 served by U + 32 rejected by U**. Own raw 34-scenario probe (C-30’s repaired 14/11 r3 w17 run used) agrees exactly: `extra-probe-output-v3.txt:130`. The scan collects request IDs from a pruned candidate only when its code and a commitment witness both say `COMMITMENT_BUDGET_EXCEEDED`, then crosses with raw final lifecycle states.

The brief calls the 1,075 claim B14, but its evidence ID is **D13**; main-register B14 is initial-promise length (14.15 vs 14.12 min), assigned elsewhere. The draft correctly cites D13 at line 454. No thesis correction is required for this typo in the brief. The v4 wording “không có bản ghi chặn nào được ghi” and its explicit caution at lines 451–452 are justified; no recorded witness does not establish a structural-only cause.

## Extra snow scope check

Both `optimize/snow/worlds/W5-d20181115-w14.json:1` and `...w15.json:1` explicitly set **sigma = 0.0 and shockRate = 0.0**. `optimize/run_forecast.py:85–87` selects them; line 133 passes the selected file as `RB_WORLD_CONFIG`. This supplies source evidence for the intended no-noise snow configuration relevant to v4 lines 65–69. `run_forecast.py:94–102` passes the C-30 commitment config and the common WP4 config; `tang3/configs/wp4-tier3-v2.json:7` enables `no-worse-than-reference-v1` recovery.

Saved read-only source probe: `extra-snow-scope-v2.py` → `extra-snow-scope-output-v2.txt` (exit 0). It also opens all eight raw initialization manifests: masterSeed 7, policyVersion `tier3-exploratory-v1`, and the same policyConfigurationHash `a2f11a3ada0773f9b30b85c56c935058e2e931f13c907f46b2ddfff8c1285f1c`. Their manifests contain no world-file hash; this source check does **not** constitute a binary audit of the snow runner. The retained “Chưa kiểm lại” caveat at v4 lines 135–136 remains appropriate.

## Probe completion/provenance

`extra-probe.py`/its header-only output were interrupted before aggregates. `extra-probe-v2.py` saved all 80 fixed runs, then stopped on a short adapter-frame prefix; those completed fixed rows remain valid. `extra-probe-v3.py` repairs that prefix handling and probes only the remaining morning/snow/budget subjects. It exits 0 when complete. All files were preserved; no existing file was overwritten.

**No numerical corrections identified in these assigned complementary checks.** All completed results are AGREE; no assigned numeric item remains CANNOT CHECK.
