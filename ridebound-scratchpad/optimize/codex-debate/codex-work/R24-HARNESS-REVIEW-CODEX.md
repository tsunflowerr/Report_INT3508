# R24 - independent Stage-1b harness review by Codex

**Verdict: NOT READY.** Correct the comparator's per-run digest validation and input-freeze coverage before sealing this snapshot. The panel, objective configuration and principal analysis thresholds match the agreed design, but the current comparator demonstrably accepts an invalid final checkpoint. Additional failure-latch, smoke-evidence and launch-safety changes are required below.

This is a read-only review, except for exclusive creation of this report inside `codex-work`. I did not execute a harness CLI, rerun the self-test suite, run FleetPy, build, test .NET, publish, commit, install anything, or modify the harness. I read the existing self-test/dry-run logs and executed read-only Python `-B` probes with archived bytes and synthetic objects held in memory. No probe wrote a file or started a job.

## 1. Scope and snapshot

Paths in citations:

- `S/` = `E:/Code/Report_INT3508/ridebound-scratchpad/`.
- `H/` = `S/tang3/stage1b/harness/`.
- `D/` = `S/optimize/codex-debate/`.
- `R/` = `C:/Code/RideBound-costfirst/`.
- `A/` = `C:/RideBoundData/research/tier3-t38-v1/`.
- `F/` = `E:/Code/RideBound-deadline/simulators/fleetpy-ridebound/`.

The review began with `H/HARNESS-REPORT.md`. These current file hashes reproduce its stated reviewed snapshot (`H/HARNESS-REPORT.md:9-20`), including the four files identified in the self-test header (`H/selftest-2026-10-11-final.log:2-5`):

| File under H/ | SHA-256 |
|---|---|
| `compare_equivalence_stage1b.py` | `4b3384fa39864cb12be75a89daaf85cbd235d8e8a395a37fe7c39d065224e2e7` |
| `run_stage1b.py` | `bce7e2ad09927f2987d7375796bbd3aded749fd4fa73a62dfdb512e4adaf5615` |
| `test_compare_equivalence_stage1b.py` | `689e4fe2e1c5ed061298034be7b4d9276c538fcba868e94629bd8eae521a80f2` |
| `canonical_wp4.py` | `b8ed04ce96cbaf29a27f0dacdcbf9d22891d03463d21b3afce50aeb5e6d184a1` |
| `wp4-tier3-v2-costfirst.json` | `37040657b8f6c16c8eb8430a208bfd4b155791668af0f1da49110f0f372300ae` |
| `selftest-2026-10-11-final.log` | `807656efb031c7a5e0cda9d1a14599eaa4666778ffb0a1bb96e803f684e6d519` |
| `plan-dryrun-2026-10-11-final.txt` | `87335e98e500a24d129d59e612cd43c0ff8e969b4cb64f84c1a1afa73f7a43ca` |
| `STAGE1B-PLAN-DRAFT.md` | `8b7338c07f3e399c75df676d6976508943a6ea89b6d6c66033929367ad74ce1b` |
| `RUNNER-PROVENANCE-TEMPLATE.md` | `ebd64a24cd947cb16681bf6d8cba9d4b9d2bd321635cfdca795c2f14f100b4a8` |

At review time the v3 runner/output root, v3 manifest/filled provenance receipt, final plan/seal, input freeze and four verdict files do not exist. Those are expected pending artifacts, not evidence that Gate 0 or either smoke passed (`H/HARNESS-REPORT.md:95-100,110-111`; `H/plan-dryrun-2026-10-11-final.txt:8-10,20-23,99-103`).

## 2. Findings, ranked by severity

### F1 - P1: an invalid checkpoint digest passes the exact Gate-0 comparator

Locations: `H/compare_equivalence_stage1b.py:216-224,258-264,412-430,583-585`; `R/src/RideBound.Contracts/Protocol/CheckpointMessages.cs:129-156`; required criterion `D/codex-work/R22-CODE-REVIEW-CODEX.md:173,190`.

`Normalizer.derived` verifies the string shape and assigns first-appearance tokens. The checkpoint branch checks manifest/state/previous-decision links, but never recomputes `checkpointHash` from `content`. Consequently a fresh, incorrect 64-hex checkpoint hash receives the same token as the correct hash at that position. Bundle/frame checksums establish that the bytes match their transport receipts; they do not validate this protocol digest.

**Confirmed read-only counterexample:** using the archived `U-d20181116-s10-r1-w08` bundle in memory and a synthetic, internally verified v3 runner tree, I changed the permitted initialization DLL field and replaced only the final checkpoint's `checkpointHash` with SHA-256 of `b"incorrect checkpoint digest"`. I regenerated the affected frame and bundle transport receipts. The comparator returned:

```text
INVALID_CHECKPOINT_PAIR_PASS True preconditions []
  decisions: identical
  table: identical
  served: identical
  lifecycle: identical
  boarded: identical
  alighted: identical
  frames: identical
  finalOnlineState: identical
  commitmentLedger: identical
  incidentLedger: identical
  runSemantic: identical
  PAIR EQUIVALENT
```

This is an extension of the currently accepted P2 control, not a simulated rebuilt run. The reference runner identity in the probe came from its archived TSV; I did not rehash the full v2 tree. The inspected self-test records that separate tree verification (`H/selftest-2026-10-11-final.log:30`).

Independently applying the protocol's checkpoint formula to the original archived content reproduced its original digest. That formula hashes `RideBound.CheckpointHash.v1\0`, the length-prefixed `canonicalCheckpointContent` tag and the length-prefixed canonical content bytes (`R/src/RideBound.Contracts/Protocol/CheckpointMessages.cs:32-33,140-156`). The substituted digest therefore fails the actual checkpoint codec's content check (`:129-133`). A Gate-0 pass requires a **valid** final checkpoint, so the observed pass violates R22 even though the normalized fleet behavior is equal.

The existing P3 control also substitutes each derived digest with `sha256(b"derived" + old_digest)`, then consistently remaps links; it does not calculate digests from the new underlying content (`H/test_compare_equivalence_stage1b.py:268-300`). It proves preservation of equality/link patterns, not digest validity. P2 similarly changes the initialization without rebuilding affected protocol digests (`:251-253`).

**Required change:** validate each run's protocol digest/content bindings before normalization, beginning with the confirmed checkpoint case and the manifest/state/decision bindings covered by R22. Keep raw cross-run digest equality waived. Build genuinely valid positive fixtures by recomputing affected digests according to the frozen codecs. Add a negative control with an incorrect checkpoint digest and fresh transport receipts; add a consistently rewritten decision digest/ACK/chain case that preserves links but has an incorrect content digest. Do not accept arbitrary digest substitution as proof of a valid run.

### F2 - P1: the input freeze neither requires complete coverage nor freezes the external simulator/runtime

Locations: `H/run_stage1b.py:244-275,321,368-377`; R22 requirement `D/codex-work/R22-CODE-REVIEW-CODEX.md:175-177,214`.

`freeze_problems` checks only entries that happen to be present. It does not require the path set produced by `freeze_targets`, reject duplicate entries or require any entries. A read-only AST probe supplied a header-only synthetic freeze and got:

```text
HEADER_ONLY_FREEZE_PROBLEMS []
```

Sealing the file's own hash does not repair this omission: `seal_problems` proves that the sealed file stayed unchanged, while no check proves that it describes the required input set (`H/run_stage1b.py:278-297`). The normal generator writes its current target list, but the verifier must also detect an incomplete receipt.

Even a correctly generated current freeze omits external execution inputs. It includes scratchpad helpers/configs/fixtures/worlds and `dotnet.exe`, but no FleetPy source tree, Python interpreter/environment or resolved shared .NET runtime (`H/run_stage1b.py:247-260`). In particular the actual preflight imports external `src.routing.NetworkBasic`, `src.simulation.Vehicles` and `src.misc.init_modules` (`F/actual_fleetpy_medium_preflight.py:420-424`). `NetworkBasic.py` is also absent from the adapter's six selected FleetPy receipt files (`F/ridebound_fleetpy/session.py:252-258`).

The unchanged repository inventory genuinely binds the adapter/harness repository's tracked and nonignored files (`F/actual_fleetpy_medium_preflight.py:740-782,837-845`); it does **not** bind the separate FleetPy or Python/.NET installation. The initialization's FleetPy version/commit are fixed constants, not a check of the external tree (`F/ridebound_fleetpy/session.py:16-17,477-480`). Per-run before/after receipts check drift during a run (`F/actual_fleetpy_medium_preflight.py:697-699`), not equality to a predeclared external-software baseline. The runner is framework-dependent, so hashing its tree and host alone does not freeze the selected `Microsoft.NETCore.App` implementation (`H/RUNNER-PROVENANCE-TEMPLATE.md:34-35`; `R/src/RideBound.Runner/RideBound.Runner.csproj:13`).

Thus unchanged declared identities and even equal behavior on the four controls cannot establish the required unchanged simulator/runtime for later cells.

**Required change:** require an exact, nonempty, duplicate-free required path inventory when verifying the freeze. Extend the frozen contract to the external code/data and execution environment actually used, including FleetPy, Python/dependencies and the selected .NET runtime; verify it before phases/jobs. Preserve the existing adapter repository inventory check. If an archived external-software baseline is unavailable, disclose that provenance gap and resolve the comparison contract before execution; do not infer historical byte equality from a hardcoded version string.

### F3 - P2: failure verdicts are not a complete stop latch, and malformed started jobs can escape verdict creation

Locations: `H/run_stage1b.py:300-326,404-420`; `H/compare_equivalence_stage1b.py:169-175,700-710,719-742,748-758`.

The driver checks `GATE0-FAILED.txt` only while validating the smoke/main prerequisite. It checks `SMOKE-FAILED.txt` only for main. It does not reject `run gate0` because a failure verdict exists, or `run smoke` because its own failure verdict exists. Read-only AST probes, with other prerequisites stubbed as valid, confirmed:

```text
GATE0_FAILED_DRIVER_GATE0 []
SMOKE_FAILED_DRIVER_SMOKE []
SMOKE_FAILED_DRIVER_MAIN ['refused: SMOKE_FAILED.txt exists; Stage 1b stops (R22:208, R17 G0)']
```

These exercised admission checks only; no jobs were submitted. Existing output reuse protections still prevent replacing completed directories (`H/run_stage1b.py:106-113,345-349`). The defect is that the failure file itself does not produce the universal refusal claimed in `H/HARNESS-REPORT.md:90-92` and the plan's stop rule (`H/STAGE1B-PLAN-DRAFT.md:98-99,108`).

There is a second persistence gap. Missing required files in an existing job are explicitly turned into failure results, but malformed JSON in an otherwise present bundle raises `SystemExit` from `Run.__init__`. The phase loop has no handler that converts it into a failed comparison/verdict (`H/compare_equivalence_stage1b.py:169-175,719-731,748-753`). Some malformed frame/state shapes can similarly raise rather than return a precondition problem (`:373-425,452-460`). Such a started, unusable run writes neither a failure receipt nor a first-difference report, contrary to the declared verdict behavior (`H/STAGE1B-PLAN-DRAFT.md:98-99`). This cannot yield a pass by itself, but leaves the failure unlatched and the comparator eligible to be invoked again.

**Required change:** make any phase failure a global refusal for every job-start path; make successful phase verdicts close that phase to further execution as well. Convert malformed started-run artifacts into explicit per-job failures and persist the phase failure exactly once, while preserving the existing no-verdict behavior for genuinely unstarted/unsealed inputs. Validate the user report path before evaluating: it is currently unrestricted and can collide with the reserved verdict filename (`H/compare_equivalence_stage1b.py:663-666,698,741-742,757-758`). Keep phase report outputs under H/ and distinct from verdict paths, as the module promises (`:39`).

### F4 - P2: smoke validation can waive all the execution evidence it is intended to inspect

Locations: `H/compare_equivalence_stage1b.py:597-617,641-657`; `H/wp4-tier3-v2-costfirst.json:6`; R22 integration requirement/recommendation `D/codex-work/R22-CODE-REVIEW-CODEX.md:60-66,242,250`.

Absent `solver.executionEvidence.selection`, absent primary/final diagnostics and empty objective-bound lists only generate informational counts. No stability level is found, and the accepted-before-cost condition is evaluated only if `operational-cost` appears. Missing omission counts are added as zero. A synthetic decision with solver status `feasible` and no execution evidence produced **zero problems**, with `executionPath=None`, `finalSolveStatus=None`, both diagnostics absent and omitted-candidate sum zero.

The ON config explicitly enables execution evidence. A broken RunnerSession/adapter evidence path can therefore satisfy the smoke's objective checks vacuously and contribute to `SMOKE-PASSED.txt`. Also, the report prints objective-list lengths but not the actual objective bounds/work values that R22 asks the operator to inspect (`H/compare_equivalence_stage1b.py:609-616,653`; `D/codex-work/R22-CODE-REVIEW-CODEX.md:66`).

**Required change:** require the execution-evidence structures promised by this configuration and explicit, valid status/path/omission accounting. Report bounds and work evidence, and record the integration inspection before authorizing main. Validate the retained objective order when applicable. Preserve the legitimate distinction that exhausted-budget/fallback diagnostics may omit objective bounds; absence must have an explicit supported reason, rather than silently passing every evidence check. Do not infer cost-first from a U objective list alone: the verified ON binding remains the primary configuration identity (R22:242).

Add smoke negatives for missing selection evidence and forbidden stability levels, plus legitimate exhausted-budget/fallback positives. The current self-test contains no smoke-report or driver-refusal tests (`H/test_compare_equivalence_stage1b.py:136-375`).

### F5 - P2: AC-only, STOP and disk admission are weaker than the sealed safety claim

Locations: `H/run_stage1b.py:335-361,412-413`; inherited policy `S/tang3/pilot/run_pilot.py:41,73-81`; claimed safety `H/STAGE1B-PLAN-DRAFT.md:175-177`.

**Battery override:** `wait_for_power` calls `run_pilot.may_start_job`, which returns true on battery when inherited `RB_ALLOW_BATTERY_MIN_PERCENT` permits it. The driver neither rejects that setting nor implements a local AC-only predicate. A pure probe of the inherited function with battery status `(0,100)` and override `50` returned true. This is inherited behavior, but it conflicts with this plan's AC-only promise; the study has not declared a battery exception.

**STOP during the power wait:** STOP is checked inside the loop only when `may_start_job()` is false. If STOP appears during the sleep and AC returns before the next condition, the loop exits successfully. A fake-clock probe with power results `[False, True]` and STOP created by the intervening fake sleep returned `True` with STOP present. `run_job` has no STOP recheck between this return and `subprocess.run`. This is a specific wait-state defect, beyond the unavoidable small interval between any check and process launch.

**Disk admission:** free space is checked before a possible 20-minute wait, then used without rechecking. Six workers independently check the same unreserved free-space value (`H/run_stage1b.py:352-360,412-413`; `S/tang3/pilot/run_pilot.py:42`). The condition proves room for one 410-MiB allowance at that instant; it does not reserve allowances for concurrent starts or enforce a hard 50-GiB floor.

Current capacity is adequate for the historical-size estimate: the existing dry-run records 60,895 MiB free, and my read-only check returned 60,919 MiB. The four reference bundles are 81,637,143-95,773,980 bytes; projecting that range to 74 jobs gives about 6.04-7.09 decimal GB, broadly matching the stated estimate (`H/plan-dryrun-2026-10-11-final.txt:11`; `H/HARNESS-REPORT.md:99`; `H/STAGE1B-PLAN-DRAFT.md:179`). This is an estimate, not a measured CF output size or a repair of concurrent admission.

**Required change:** use a strict local AC predicate; recheck STOP, phase failure latches and disk admission immediately after waiting and before launch; serialize/reserve disk allowances across workers. Keep the 1,200-second deferral policy and keep-awake cleanup. Do not change the archived helper in place.

### F6 - P3: complete the plan's start/second-build rules and soften the remaining H3 attribution

Locations: `H/STAGE1B-PLAN-DRAFT.md:17-25,100,137,159,161-166`; controlling records `D/claude-work/R17-FINAL-VERDICT.md:280-288`; `D/codex-work/R18-CONFIRM-CODEX.md:222-230`; interpretation correction `D/codex-work/R19-CODEX.md:178`.

The numerical Stage-2 gate is correct. Three textual requirements should be completed before seal:

1. Restore/record the A1 milestone, confirmed deadline and at-least-three-weeks Stage-1 start condition from R17/R18, or explicitly record an already-authorized amendment. The reviewed draft does not provide those facts. It repeats the five-/ten-working-day time boxes but omits R17's consequence: otherwise drop the remaining study and report it as future work. This is a missing protocol record; I have not established that the actual timing condition failed.
2. State explicitly that **all Stage-2 arms use the same second published binary**, and that the frozen two OFF rechecks exercise the changed 120-s path against available controls. The draft requires aligned per-step semantics and frozen arms/cells/references but leaves these two R18 constraints implicit (`R18:226-228`). No Stage-2 job is authorized by this review.
3. Replace H3's failure sentence, "Failing: the selector does reliability work under the cap," with: **"Failing means the changed policy missed a predeclared aggregate reliability threshold; report the service composition and trajectory evidence before attributing the difference to the selector."** A missed fraction guard alone does not isolate that mechanism (`D/codex-work/R19-CODEX.md:178`; `D/codex-work/R18-CONFIRM-CODEX.md:247-249`).

## 3. Checks that agree with the intended design

### Comparator and verdict structure

The R22 F1/F2 repairs are substantial and correctly scoped, subject to F1/F2 above:

- The DLL token is applied only at `adapterToRunner / initializeRun / payload.manifest.binarySha256`, and only for the verified DLL value (`H/compare_equivalence_stage1b.py:265-271`). Initialization's other fields are compared raw, the arm binding is recomputed, the archived DLL/tree are required, and all four new DLL identities must agree (`:531-552,669-671,714-738`).
- Stable policy/scenario/graph/travel snapshot hashes remain raw, including event/final-state snapshot keys. `coreCommitSha`, versions, seed, units and capabilities remain in the exact manifest/frame comparisons (`:65-68,259-260,537-544`). Unclassified hash fields fail (`:273,473-474`).
- Publication IDs map to request/history-entry identities and breach IDs to incident identities with occurrence counts. Unmapped references and duplicate ledger IDs fail. Certificate membership retains cardinality, and actions are sorted as a multiset without removing duplicates (`:226-255,277-308,397-404`). Route/service, history, event and frame sequence remain ordered (`:280-281,425-430`). No identified ordering exception improperly sorts those objects.
- The eleven reported components retain R22's five core comparisons and explicitly report lifecycle/boarding and final state/ledgers; frame equality preserves objective diagnostics, certificates, simulation time and deterministic accounting (`:450-480,483-527`). Successful summary/run statuses, own bundle/frame transport integrity and final checkpoint presence are required (`:176-193,330-350,362-378`). Digest validity is the confirmed missing precondition.
- Phase verdict files use exclusive creation and include DLL/tree identity. The driver rejects a prerequisite pass receipt for another runner build and requires **both** pass receipts for main (`:739-758`; `H/run_stage1b.py:300-325`). The ordinary gate0/smoke CLI refuses rejudgment of a phase with an existing verdict and refuses unstarted/unsealed inputs without writing a verdict (`H/compare_equivalence_stage1b.py:700-710`). `pair` writes an exploratory comparison report, not the fixed Gate-0 pass receipt (`:686-697`); its lighter CLI checks must not be used as a substitute for `gate0`.

I found no demonstrated false rejection of an otherwise equivalent valid rebuilt run in the reviewed controls. However, the arbitrary-digest positive fixtures do not prove acceptance of a fully valid rebuilt protocol run; that remains to be tested after F1.

### Driver, panel and outputs

| Phase | Verified design | Source |
|---|---|---|
| Gate 0 | U/C-30 x `d20181116-s10-r1-w08`, `d20181116-s10-r1-w17`; 4 OFF jobs; archived `-t38` labels | `H/run_stage1b.py:70-73,90-95` |
| Smoke | CF-U/CF-C-30 x `d20181114-s10-r1-w08`; 2 ON jobs | `H/run_stage1b.py:72,94-95` |
| Main | CF-U/CF-C-30 x the exact 34 split test cells; 68 ON jobs | `H/run_stage1b.py:73,94-95`; `S/tang3/t38/split-t38-v1.json:31-65` |

I independently read the split: 34 unique test cells, comprising 9 w07, 14 w08 and 11 w17 cells. The w08/w17 primary subset has 25 cells. The smoke cell is in the forced calibration group and absent from test (`S/tang3/t38/split-t38-v1.json:5,14-17,31-65`). Both Gate-0 cells are also in test. There are **35 distinct cells** across all phases; 37 counts phase-specific cell checks with the Gate-0 cells repeated, not 37 distinct fixture cells (`H/run_stage1b.py:245`; compare `H/HARNESS-REPORT.md:98`).

The actual command retains the T3.8 wrapper, fixtures, derivative/normalization/selection files, driver, seed 7, one repeat and inventory argument; the intended differences are runner root, phase-specific WP4, labels and outputs (`H/run_stage1b.py:116-135`; `S/tang3/t38/run_t38.py:84-103`). It sets the measured-world configuration, clears inherited `RB_FORECAST_CONFIG`, and uses the archived harness cwd (`H/run_stage1b.py:356-361`).

Output roots are `C:/RideBoundData/research/tier3-stage1b-v1/<phase>/<job>`; logs are under H/. Existing output directories and existing pending logs are not retried; logs are exclusive-created and keep-awake is cleared in `finally` (`H/run_stage1b.py:61,83,106-113,345-365,407-419`). Phase-level v3 tree/manifest, DLL-not-v2, receipt, configuration, split, wrapper, harness HEAD, world, reference, seal and freeze checks are present (`:140-241,278-326`). The seal requires all twelve listed artifacts (`:79-82,294-296`). Their incompleteness and the safety exceptions are the findings above.

### WP4 and bindings

I independently calculated compact sorted canonical bytes for these actual ASCII/integer/boolean documents and the domain-separated binding formula. All values match R22. ON differs from OFF in exactly one root key; removing it restores identical canonical v2 bytes (`H/wp4-tier3-v2-costfirst.json:9`; `H/make_wp4_costfirst.py:47-65`; `D/codex-work/R22-CODE-REVIEW-CODEX.md:226-240`).

| Identity | Independently reproduced SHA-256 |
|---|---|
| OFF physical WP4 | `66e9b59249d9491d520f3ed592e8c878a0d3b100e39432d5f4b73321617b4518` |
| OFF canonical WP4 | `fb2813c4036d309490e12df77e37de1683b92b92a9ebdd71e16cad35d50ecd42` |
| ON physical WP4 | `37040657b8f6c16c8eb8430a208bfd4b155791668af0f1da49110f0f372300ae` |
| ON canonical WP4 | `16dcb7e3337763aab7889f7528365dced2aa49028db6dbf390f8b3dce79b3140` |
| CF-U binding | `90b290d7e63f6885ac8e93e18017d55dddc54c27a05d8476a65dcf7d802e2df5` |
| CF-C30 binding | `e6b33be5649dc2b1208b42b90cef227d00721cba59e4340fdbc4e96f21796f76` |

The canonicalizer mirrors the relevant C# parsing, duplicate-key, integer, string-escaping and ordinal-property rules, and the binding domain/order is correct for the actual frozen files (`H/canonical_wp4.py:46-69,74-109,132-137`; `R/src/RideBound.Contracts/Serialization/CanonicalJson.cs:120-158,178-225,247-303`; `R/src/RideBound.Contracts/Protocol/Wp4PolicyConfigurationBinding.cs:19-20,31-44`). The commitment files and both OFF bindings remain the archived values (`H/make_wp4_costfirst.log:6-7`; `H/run_stage1b.py:158-183`). No WP4 edit is requested.

### Plan endpoints and Stage 2

These reviewed plan terms agree:

- Primary `I_L = (L_CF,U - L_CF,C30) - 127`, with `I_L = I_served - I_timely60`. The SF baselines give served difference 96 and timely difference -31, hence 127. The draft requires service composition, the full 2x2 outcomes, overlaps and cell/day patterns, and disclaims independent-cell/general causal interpretations (`H/STAGE1B-PLAN-DRAFT.md:112-124`; `D/codex-work/R18-CONFIRM-CODEX.md:236-251`).
- H6 uses the exact SF-C30 shared-completion count 313: `ceil(1.10 * 313) = 345`; the service guard is `ceil(0.99 * 2338) = 2315` and explicitly survives a failed H6 (`H/STAGE1B-PLAN-DRAFT.md:140`; `S/tang3/t38c120/C120-RESULTS.md:25`; `D/codex-work/R18-CONFIRM-CODEX.md:202,249`; `D/codex-work/R19-CODEX.md:179`).
- H2 remains a conjunction; H4 preserves the +40 pooled and 15/25 cell targets; H5 remains a guard; H7 requires ten **completed** cumulative-only CF-U histories at 120 s, with corrected resource-allocation interpretation (`H/STAGE1B-PLAN-DRAFT.md:136-141`). The other R18 failure-interpretation corrections are retained apart from the H3 sentence in F6.
- Stage 2 requires H2 **and** H7 and at least two weeks remaining; counts are 34+34+2+2 = 72; without it no empirical cumulative-versus-per-step outcome claim is allowed (`H/STAGE1B-PLAN-DRAFT.md:163-171`; `D/codex-work/R18-CONFIRM-CODEX.md:215,226-232`). Add the explicit second-build constraints in F6.
- Main analysis scripts are not yet written. Freezing their hashes by amendment before opening any main output is explicitly promised; their absence is disclosed rather than silently treated as completed analysis (`H/STAGE1B-PLAN-DRAFT.md:154-158`; `H/HARNESS-REPORT.md:122-123,147-149`). Implement and verify that promise before main results are inspected.

### Proposed publish and separate provenance

The receipt correctly separates the archived harness `coreCommitSha` from the eventual runner-source commit and requires base/reviewed-diff identity, clean source, tests, toolchain, exact command/log, DLL/tree/TSV hashes and file-list differences (`H/RUNNER-PROVENANCE-TEMPLATE.md:13-67`). The current automated receipt check only checks existence and the occurrence of the DLL/tree hashes; it does not validate that the other fields are filled or source claims true (`H/run_stage1b.py:149-154`). All receipt fields therefore need actual evidence/manual review before seal; merely embedding two hashes is insufficient provenance.

My read-only Git checks reproduced HEAD `761915cbb89d03f410cd9989ad1cf136e6234bf8`, branch `research/tier3-cost-first`, and current LF-normalized diff/patch SHA `c48042af4e7cee2db01bdee5efb804dac703d80c8c657276fc5718816e1ad690`. The 97 changes between v2 source `45f8026` and base `761915c` are all under `docs/`, with no diff under `src`, `simulators` or `tools`. This supports the template's base-source claim (`H/RUNNER-PROVENANCE-TEMPLATE.md:19-24`; reviewed patch identity `D/codex-work/R22-CODE-REVIEW-CODEX.md:17-28`). The harness HEAD independently remains `1ce15e92d2c1459d4254bbbcd581529197257fb2`.

The proposed `dotnet publish ... -c Release -o ...runner-tier3-v3` form is consistent with the recorded Tier-2 command and the v2 framework-dependent layout; the template explicitly labels the inferred v2 command as an inference (`H/RUNNER-PROVENANCE-TEMPLATE.md:78-100`; `S/session-2026-09-23-archive/tier2-v2-draft.md:352-356`). There is no observed v3 publish result to certify. Keep the output-root nonexistence precondition, record the effective SDK/runtime/package output, compare the full file list and verify the final tree. Run the SDK diagnostic commands from the source worktree as required by the comment; moving `Set-Location` ahead of those commands would make the literal snippet self-contained (`H/RUNNER-PROVENANCE-TEMPLATE.md:73-80`). The known clean-tree test failure is transparently disclosed, not a newly observed failure (`:26`; `S/tang3/stage1b/IMPLEMENTATION-REPORT.md:245-246`).

## 4. Self-test assessment and conditions for another review

The inspected final log has **59 OK**, no BAD, and `SELFTEST PASS` in 233 s (`H/selftest-2026-10-11-final.log:6-66`). Its hashes bind it to the current comparator/canonicalizer/test/config snapshot. The canonical controls, runner identity checks, all four archived reference integrity checks, stable configuration/input mutations, decision time, route order, ledger/alight values, publication references, broken ACK, unclassified hash and transport/status negatives are useful coverage (`:6-65`).

The most important missing negative is **a wrong derived digest with valid transport receipts and preserved link patterns**, demonstrated by F1. The existing N15 changes an ACK alone, which exercises link mismatch; it does not exercise a consistently rewritten but invalid content digest (`H/test_compare_equivalence_stage1b.py:356-358`).

Before another sealing review, add meaningful controls for F1-F5: valid recomputed rebuilt/salted positives; incorrect checkpoint/linked decision digests; incomplete/duplicate freeze and external-runtime drift; malformed started bundles; every failure-latch entry point; missing smoke evidence and supported fallback/exhaustion; strict AC, STOP on power restoration, and concurrent/stale disk admission. Regenerate the self-test evidence and plan snapshot after fixes. These are pure harness controls, not additional FleetPy jobs.

The study design and ON hashes can be retained. Correct and review the harness, complete the manual plan/provenance requirements, then obtain the already-required publish/run authorization through the existing process. This review supplies no authorization to run, publish or commit, and no empirical Gate-0 or smoke pass.
