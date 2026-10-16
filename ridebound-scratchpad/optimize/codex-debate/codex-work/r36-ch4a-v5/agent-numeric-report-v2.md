# R36 targeted numerical verification (v2)

All R34 correction-2 pooled main-set quantities, promise-duration means, counted service comparison, and snow runner/configuration equivalence are verified. **The proposed morning denominator 55.963 is not reproduced: the correct independently checked count is 0 / 44.270 acknowledged decisions over 64 runs.**

Inputs were read only. Every file below was created exclusively in `r36-ch4a-v5/`; nothing was overwritten. No simulation, build, installation or deliverable edit was performed.

## Saved probes and exact anchors

- `agent-numeric-v2.py` -> `agent-numeric-output-v2.txt` (N): rereads all 170 IVC extraction JSONs, 68 raw final main checkpoints, 59 raw initializeRun manifests, archived DLL/config bytes, and 64 raw morning decision/ack streams. Its final hardcoded expectation of 55.963 fails after all counts are saved; none of its main/promise/snow assertions failed.
- `agent-numeric-supplement-v2.py` -> `agent-numeric-supplement-output-v2.txt` (S): main late30 positive-scenario counts, then raw final lifecycle counts for all 128 C/Mplus morning runs; success.
- `agent-numeric-confirm-v2.py` -> `agent-numeric-confirm-output-v2.txt` (C): independently rereads all 64 morning `run-00.json`/`summary.json` files and compares their semantic `nextEpoch - 1` with every freshly parsed raw acknowledgement count; success.

`SBASE` = `E:/Code/Report_INT3508/ridebound-scratchpad/`; `R` = `C:/RideBoundData/research/`.

## Main-set quantities

The scenario list is `SBASE/tang3/t38/split-t38-v1.json` (`test`, 34 distinct cells). Each IVC file is selected from `SBASE/tang3/t38/independent/cache/<arm>-<cell>[rerun1].json`; exactly one selected file per arm/cell. All 170 selected extracts have status pass and 108 requests. The served set equals both the alighted and promised-rider sets. Every selected path and per-scenario pair is saved in N:3-176.

| Arm | Forced / acknowledged | Own promise breach / served | Positive breach scenarios / 34 | N line |
|---|---|---|---|---|
| U | 0 / 20.760 | No cap-specific breach obligation | — | 37 |
| C-30 | 0 / 20.101 | 0 / 2.338 | 0 / 34 | 72 |
| Mplus-30 | 7.710 / 20.103 | 289 / 2.338 | 28 / 34 | 107 |
| Mplus-60 | 4.031 / 20.163 | 79 / 2.347 | 22 / 34 | 142 |
| V-30 | 10.442 / 20.090 | 456 / 2.336 | 34 / 34 | 177 |

Own breach uses strict cumulative `sum |p-e| > 30.000 ms` for C, strict actual-arrival minus first-promise `> B` for Mplus, and strict cumulative `sum |p-v| > 30.000 ms` for V. Forced count is the existing IVC `nonNormalAcked`; denominator is `acked` (IVC counter semantics inspected at `tang3/t38/independent/iv_extract.py:26-45,72`). These are pooled counts, not denominators of the previous scenario means. N:181 verifies all R34 correction-2 row expectations.

Mplus-30 morning-window count pairs are 181/509 riders and 3.447/4.564 decisions, with 9/9 positive scenarios (N:178). Evening-window pairs are 8/852 and 328/7.163, with 5/11 positive scenarios (N:180). Intermediate-window pairs 100/977 and 3.935/8.376 are preserved at N:179. C-30 has 292/2.338 late30 riders and Mplus-30 289/2.338; each has late30 riders in 28/34 scenarios (S:1-2).

## Promise duration

N:183-252 rereads each final raw checkpoint for U/C-30 in `R/tier3-t38-v1/<job>/transcript-00.ndjson`, hash-checks the parsed frame, and computes first published drop ETA minus `request.arrivalTimeMs` for every completed rider. This is a mean pooled by riders measured from the call time; publication time is not substituted.

| Arm | Duration sum | Riders | Mean minutes | Printed | N line |
|---|---|---|---|---|---|
| U | 2.065.946.452 ms | 2.434 | 14,1464424267 | 14,15 | 217 |
| C-30 | 1.980.192.800 ms | 2.338 | 14,1160022812 | 14,12 | 252 |

Both R34 expected sum/count pairs pass. The means concern different served cohorts and do not establish an individual-rider promise-length comparison.

## Morning zero forced count and service comparison

For C-30/60/120/300, the source root is `R/tier3-w07-v1/`; for C-90/150/180/240 it is `R/tier3-w07x-v1/`. The eight cells are day 12/13, replicates 1-4, window w07 (source selection independently inspected at `tang3/w07/run_w07.py:34-35` and `tang3/w07x/run_w07x.py:37-39`).

N:320-383 saves all 64 raw per-run counts. All parsed decision and decisionApplied frames pass SHA256 and byte-length checks; an applied decision must reference an earlier parsed decision hash; certificate `body.normalOperation` must be Boolean. Distinct applied hashes are counted. There are zero forced events. The arm denominators are **5.510, 5.515, 5.530, 5.545, 5.545, 5.545, 5.540, 5.540**, totalling **44.270**, not 55.963 (N:384-391; C:2,67-75). All 88.540 relevant raw frames were hash-checked. C:3-66 confirms every raw count independently against `run-00.json` semantic `nextEpoch - 1`; every summary status is pass. The failed expectation in the first probe is preserved and explicitly corrected here.

If a decision-level pair is inserted, use **0 trong 44.270 lượt quyết định được xác nhận áp dụng, gộp trên 64 lần chạy**. The R34 wording that describes zero events across the 64 runs is also supported.

The raw final lifecycle comparison of the 128 C/Mplus morning runs gives:

| Cap seconds | C served | Mplus served | Pooled difference | S line |
|---|---|---|---|---|
| 30 | 660 | 660 | 0 | 19 |
| 60 | 661 | 661 | 0 | 36 |
| 90 | 664 | 663 | 1 | 53 |
| 120 | 666 | 664 | 2 | 70 |
| 150 | 666 | 666 | 0 | 87 |
| 180 | 666 | 666 | 0 | 104 |
| 240 | 665 | 665 | 0 | 121 |
| 300 | 665 | 665 | 0 | 138 |

Each level has eight scenarios and 864 input requests per arm. Every pooled absolute difference is at most two; the maximum absolute per-scenario difference is one. All 128 relevant final checkpoint frames were hash-checked; their paths, ordinals and SHA256s are saved at S:3-137. This supports the exact R34 counted replacement at A546-548.

## Snow runner and recovery addendum

All eight `R/tier3-forecast-v1/C-30-d20181115-s10-r{1,2,3,4}-w{14,15}/transcript-00.ndjson` initializeRun manifests, and all 51 archived `R/tier3-t38-v1/C-30-*` manifests, have the same five fields (N:254-314):

- binarySha256 = `a631038b6ea4850ffa29be2d5e4058fba2e57b725ee568075686d7a43c6f5fac`;
- coreCommitSha = `1ce15e92d2c1459d4254bbbcd581529197257fb2`;
- policyId = `ridebound-hard-vector`;
- policyVersion = `tier3-exploratory-v1`;
- policyConfigurationHash = `a2f11a3ada0773f9b30b85c56c935058e2e931f13c907f46b2ddfff8c1285f1c`.

Every parsed manifest frame passes byte-length and SHA256 checks. The SHA256 freshly computed from `R/runner-tier3-v2/RideBound.Runner.dll` matches all manifests (N:315).

Freshly canonicalizing the JSON inputs gives `C-30.json` SHA256 `f07395f5f2c967e0d89cceb4a55b23c4f896971db071d8c7876f05e20ef09884` and WP4 v2 SHA256 `fb2813c4036d309490e12df77e37de1683b92b92a9ebdd71e16cad35d50ecd42` (N:316-317). Recomputing the binding as SHA256(`RideBound.Wp4RunnerConfigurationBinding.v1` plus NUL, raw commitment digest, raw WP4 digest) matches the recorded configuration hash in all 59 manifests (N:318). Primary code inspected: `C:/Code/RideBound-noworse/src/RideBound.Contracts/Protocol/Wp4PolicyConfigurationBinding.cs:19-44`; canonical object sorting inspected in `RideBound.Contracts/Serialization/CanonicalJson.cs:129-166`.

The bound `SBASE/tang3/configs/wp4-tier3-v2.json:7` specifies `commitmentRecovery=no-worse-than-reference-v1`. Its semantics are documented at `C:/Code/RideBound-noworse/src/RideBound.Runner/Configuration/Wp4RunnerConfiguration.cs:54-58` and recognized at 331-338. Therefore the snow-runner caveats at A table/A142/A435 can be removed. This freshly reproduces R26 Q8 (R26-CH3-OPEN-QUESTIONS-CODEX.md:253-281), N4B8-05, and `checks-ch4b-v8/ch4b-v8-check-2026-10-12.txt:65-72`, all opened during this pass.

Boundary: this is a targeted read-only check. Existing IVC main extraction values were reaggregated rather than every main raw event frame re-extracted; no claim of a full new simulator audit or fresh rendered-layout verification is made.