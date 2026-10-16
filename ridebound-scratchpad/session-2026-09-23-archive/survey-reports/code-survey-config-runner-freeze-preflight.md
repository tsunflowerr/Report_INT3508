# RideBound survey — config schemas, sealed runner, freeze tooling, preflight

All paths absolute-rooted at `E:\Code\RideBound`. Nothing was modified.

---

## 1. Commitment config — full JSON schema and parse path

**Reader:** `E:\Code\RideBound\src\RideBound.Runner\Configuration\CommitmentPolicyConfiguration.cs` (339 lines). Class declares `ICommitmentPolicyProvider, IStopDistanceLookup` (`:12-14`).

### Entry point

`Decode(ReadOnlySpan<byte> utf8Json)` at `:64-122`:
```
67  var canonical = CanonicalJson.Canonicalize(utf8Json);
68  _ = Sha256Hex.TryCreate(
69      Convert.ToHexStringLower(SHA256.HashData(canonical)),
70      out var contentHash);
72  using var document = JsonDocument.Parse(canonical);
74  RequireObject(root, RootFields, RootFields, "$");
```
Note `RequireObject(root, RootFields, RootFields, ...)` — allowed == required, so **all three root keys are mandatory** and no extras.

### Field allowlists (`:16-39`)

| Set | Keys |
|---|---|
| `RootFields` `:16` | `configurationVersion`, `policies`, `stopDistances` — **all required** |
| `PolicyFields` `:20-28` | `policyId`, `budgetBasis`, `limits`, `materialRevisionRule`, `freezeHorizonMs`, `freezeHorizonLocks`, `finalConfirmationLocks`, `ratchetLocks` |
| `LimitFields` `:29-32` | `dimension`, `hardLimit`, `applicablePhases` |
| `RevisionFields` `:33-35` | `rawEtaThresholdMs`, `displayBucketWidthMs` |
| `DistanceFields` `:36-39` | `fromNodeId`, `toNodeId`, `distanceMm` — **all required** |

Required subsets: policy = `Fields("policyId","budgetBasis","limits","materialRevisionRule")` (`:148`); limit = `Fields("dimension","applicablePhases")` (`:191`); materialRevisionRule required set is `Fields()` — **empty**, i.e. both sub-keys optional at reader level but the domain record rejects both-null (`CommitmentPolicy.cs:84-88`).

### Complete shape

```jsonc
{
  "configurationVersion": "1.0.0",          // exact string, else throw (:76-80)
  "policies": [ {
      "policyId":   "<non-empty string>",
      "budgetBasis": "decisionInduced" | "customerVisible",   // :169-175
      "limits": [ {                          // must cover ALL 10 dimensions exactly once
          "dimension": "<protocol value>",
          "hardLimit": <long >= 0, optional>,  // absent => unbounded (null)
          "applicablePhases": ["accepted"|"waitingPickup"|"onboard", ...]  // no dupes
      } ],
      "materialRevisionRule": {
          "rawEtaThresholdMs":   <long >= 1, optional>,
          "displayBucketWidthMs":<long >= 1, optional>
      },
      "freezeHorizonMs":         <long >= 1, optional>,
      "freezeHorizonLocks":      ["vehicle"|"pickupStop"|"dropStop"|"pickupEta"|"dropEta"],
      "finalConfirmationLocks":  [ same vocabulary ],
      "ratchetLocks":            [ same vocabulary, but only pickupEta/dropEta accepted downstream ]
  } ],
  "stopDistances": [ { "fromNodeId":"…", "toNodeId":"…", "distanceMm": <long >= 0> } ]
}
```

### Dimension vocabulary (`src/RideBound.Domain/Commitments/CommitmentDimension.cs:34-58`)
`pickup_eta_total_ms`, `drop_eta_total_ms`, `material_eta_revision_count`, `vehicle_switch_count`, `pickup_stop_relocation_mm`, `pickup_stop_switch_count`, `drop_stop_relocation_mm`, `drop_stop_switch_count`, `incumbent_order_inversion_count`, `pre_pickup_inserted_stop_count`. `CommitmentDimensionVocabulary.Ordered` (`:19-32`) is the canonical order.

### Every validation error thrown (all `InvalidDataException` unless noted)

| Line | Message |
|---|---|
| `:78` | `"Commitment configurationVersion must be '1.0.0'."` |
| `:89` | `"Commitment configuration requires at least one policy."` |
| `:107` | `"Same-node stop distance is canonically zero and must be omitted."` |
| `:113` | `$"Duplicate directed stop-distance arc '{from}' -> '{to}'."` |
| `:173` | `"Unknown commitment budgetBasis."` |
| `:200` | `$"Unknown commitment dimension '{dimensionText}'."` |
| `:212` | `"Unknown commitment applicable phase."` |
| `:218` | `$"Duplicate commitment phase '{value}'."` |
| `:251` | `"Unknown promise lock."` |
| `:256` | `$"Duplicate promise lock '{value}'."` |
| `:274` | `$"'{path}' must be an object."` |
| `:287-288` | `$"Unknown field '{unknown}' at '{path}'."` / `$"Missing field '{missing}' at '{path}'."` |
| `:299` | `$"'{propertyName}' must be a non-empty string."` |
| `:313` | `$"'{propertyName}' must be a canonical non-negative integer."` (bound `DomainLimits.MaxCanonicalInteger`) |
| `:325` | `$"'{propertyName}' must be positive."` |

Plus **domain-layer** throws from the `CommitmentPolicy` ctor (`src/RideBound.Domain/Commitments/CommitmentPolicy.cs`), which surface out of `Decode`:
- `:161` `ArgumentException "A commitment policy must define every dimension exactly once."`
- `:168` `ArgumentException "Freeze-horizon locks require a freeze horizon."`
- `:173/:178` `ArgumentOutOfRangeException` for lock masks outside the 5-bit set
- `:189-193` `ArgumentOutOfRangeException(nameof(ratchetLocks), "Only pickup and drop ETA locks can be relaxed to a ratchet.")`
- `MaterialRevisionRule` ctor `:74-88`: thresholds must be `>= 1`; `ArgumentException "A material revision rule requires a raw threshold or display bucket."`
- `CommitmentDimensionLimit` ctor `:40-54`: `applicablePhases` must be non-`None` and inside `AllActive`.

`ReadLocks(element, name)` (`:233-264`) returns `PromiseLock.None` when the key is absent — that is the *optional-field* pattern.

`Program.cs:87-99` catches `IOException / UnauthorizedAccessException / InvalidDataException / ArgumentException / InvalidOperationException / JsonException / CanonicalJsonException`, prints `"Invalid commitment policy configuration: {message}"` to stderr and `return 64;`.

---

## 2. WP4 policy config — full schema, `RequireVariantFields`

**Reader:** `E:\Code\RideBound\src\RideBound.Runner\Configuration\Wp4RunnerConfiguration.cs` (719 lines).

### Field allowlists

| Set | Line | Keys |
|---|---|---|
| `RootFields` | `:31-43` | `configurationVersion`, `policyId`, `policyVersion`, `initialPromiseTrigger`, `candidateGeneration`, `solverExecution`, `fixedFreeze`, `repair`, `multiplePlan`, `warningProfiles`, `emitSolverExecutionEvidence`, `solverExecutionEvidenceProfile` |
| root **required** | `:215-219` | `configurationVersion`, `policyId`, `policyVersion`, `candidateGeneration` |
| `GenerationRequiredFields` | `:44-49` | `maximumCandidatesPerVehicle`, `maximumNewRequestsPerVehicle`, `exactSmallMode`, `scheduleStrategy`, `maximumExplorationWorkUnits` |
| `GenerationFields` | `:50-56` | the above + `retentionStrategy` |
| `SolverRequiredFields` | `:57-63` | `adapterVersion`, `maximumGenerationWorkUnits`, `maximumValidationWorkUnits`, `maximumSolverWorkUnits`, `maximumSolverDeterministicTimeMicros`, `randomSeed` |
| `SolverFields` | `:70-77` | the above + `skipConstantObjectiveLevels` (comment `:65-69`: "allowed but not required, so every configuration written before RB-WP14-002 keeps parsing unchanged") |
| `FreezeFields` | `:78-80` | `horizonMs`, `locks` — allowed == required (`:314-318`) |
| `RepairFields` | `:81-82` | `maximumRequestsConsideredPerVehicle` — allowed == required (`:330-334`) |
| `MultiplePlanFields` | `:83-86` | `maximumPlanCount`, `maximumCombinationWorkUnits`, `requireCompleteEnumeration` — allowed == required (`:352-356`) |
| `WarningProfileFields` | `:87-89` | `policyId`, `limits` — allowed == required (`:497-501`) |
| `WarningLimitFields` | `:90-92` | `dimension`, `warningLimit`; required only `dimension` (`:525`) |

### Enumerations / constrained values
- `configurationVersion` must be `"1.0.0"` (`:222-226`).
- `policyVersion` must satisfy `OpaqueIdentifier.IsValid` (`:237-241`).
- `initialPromiseTrigger` ∈ `"initial-acceptance"` | `"booking-confirmation"`; **default `InitialAcceptance`** when absent (`:243-255`).
- `scheduleStrategy` ∈ `"earliest-feasible"` | `"origin-hold-relocated-wait"` (`:396-403`).
- `retentionStrategy` ∈ `"legacy-accepted-count-cost-slack"` | `"service-set-stability-portfolio-v1"`; **default `LegacyAcceptedCountCostSlack`** when absent (`:404-416`).
- `solverExecution.adapterVersion` must equal `OrToolsCandidateSelectionSolver.AdapterVersion` exactly (`:443-448`) — observed value in configs: `"google-ortools-9.15.6755"`.
- `solverExecutionEvidenceProfile` ∈ `"retained-portfolio-v1"` (`:18-19`) | `"retained-portfolio-full-witness-v1"` (`:28-29`); anything else → `"Unknown solverExecutionEvidenceProfile."` (`:281-283`). Requires `emitSolverExecutionEvidence == true` **and** a `solverExecution` block (`:285-291`).
- `fixedFreeze.locks` / vocabulary in `ReadLocks` (`:595-625`): `vehicle|pickupStop|dropStop|pickupEta|dropEta`, no duplicates.
- `CollectAllCommitmentWitnesses` (`:143-146`) is `true` only for the full-witness profile.

### `RequireVariantFields` — exact quote (`:571-593`)

```csharp
private static void RequireVariantFields(
    RidePoolingPolicyKind policy,
    bool hasSolver,
    bool hasFreeze,
    bool hasRepair,
    bool hasMultiple,
    bool hasWarnings)
{
    var isB3 = policy == RidePoolingPolicyKind.FixedFreezeHorizon;
    var isB4 = policy == RidePoolingPolicyKind.NoReassignmentRepair;
    var isB5 = policy == RidePoolingPolicyKind.LeastCommitmentConsensus;
    var isC2 = policy == RidePoolingPolicyKind.CommitSoftHardHybrid;

    if (hasSolver == isB5
        || hasFreeze != isB3
        || hasRepair != isB4
        || hasMultiple != isB5
        || hasWarnings != isC2)
    {
        throw new InvalidDataException(
            "WP4 policy variant fields do not match the selected policyId.");
    }
}
```

**Exact semantics** — it is a biconditional lock, not a permission list:
- `hasSolver == isB5` fails the guard ⇒ `solverExecution` must be present for **every** policy except B5 (`least-commitment-consensus`), and must be **absent** for B5. (`hasSolver` must equal `!isB5`.)
- `fixedFreeze` present **iff** policy is `fixed-freeze-horizon` (B3).
- `repair` present **iff** policy is `no-reassignment-repair` (B4).
- `multiplePlan` present **iff** policy is `least-commitment-consensus` (B5).
- `warningProfiles` present **iff** policy is `commit-soft-hard-hybrid` (C2).

So adding a `fixedFreeze` block to a `rolling-cost` config, or omitting it from B3, both throw the same message. Called at `:293-299`, i.e. **after** the evidence-profile checks but **before** any variant block is parsed.

### Additional WP4-only errors
- `:232` `$"Unknown WP4 policyId '{policyId}'."`
- `:166-167` `InvalidOperationException "The selected WP4 policy does not use the solver-backed path."` (from `CreateSolverPolicyOptionsForRun`)
- `:178-179` `"Manifest solver seed is outside the deterministic solver range."`
- `:490` `"'warningProfiles' must be an array."`; `:506` `$"Warning profile references unknown policy '{policyId}'."`; `:514` `"Warning profile limits must be an array."`; `:534` `$"Unknown warning dimension '{dimensionText}'."`
- `:546-547` `$"Warning '{dimensionText}' requires a finite hard limit and cannot exceed it."` — guard at `:542-544`: `policy.Limits[dimension].HardLimit is not long hard || warning.Value > hard`.
- `:564-565` `"C2 must explicitly provide one warning profile for every commitment policy."` — profile ids must `SequenceEqual` `commitmentConfiguration.PolicyIds` (ordinal-sorted).

### Content hash + binding
`Decode` computes `contentHash = sha256(CanonicalJson.Canonicalize(bytes))` (`:206-209`). `BindToCommitmentConfiguration` (`:153-160`) → `Wp4PolicyConfigurationBinding.Calculate` in `E:\Code\RideBound\src\RideBound.Contracts\Protocol\Wp4PolicyConfigurationBinding.cs:31-45`:
```
hash.AppendData("RideBound.Wp4RunnerConfigurationBinding.v1\0"u8);
hash.AppendData(Convert.FromHexString(commitmentConfigurationSha256.Value));
hash.AppendData(Convert.FromHexString(wp4ConfigurationSha256.Value));
```
Python mirror: `simulators\fleetpy-ridebound\ridebound_fleetpy\mapping.py:150-158` (`wp4_policy_binding_hash`) — byte-identical domain prefix.

---

## 3. `policyId` → `RidePoolingPolicyKind`

`E:\Code\RideBound\src\RideBound.Algorithms\Policies\SolverBackedRidePoolingPolicy.cs:13-73`:

```csharp
public enum RidePoolingPolicyKind
{ RollingCost, RollingPenalty, FixedFreezeHorizon, NoReassignmentRepair,
  LeastCommitmentConsensus, RideBoundHardVector, CommitSoftHardHybrid }

public static class RidePoolingPolicyRegistry
{
    public const string RollingCost = "rolling-cost";
    public const string RollingPenalty = "rolling-penalty";
    public const string FixedFreezeHorizon = "fixed-freeze-horizon";
    public const string NoReassignmentRepair = "no-reassignment-repair";
    public const string LeastCommitmentConsensus = "least-commitment-consensus";
    public const string RideBoundHardVector = "ridebound-hard-vector";
    public const string CommitSoftHardHybrid = "commit-soft-hard-hybrid";

    public static bool TryParse(string? policyId, out RidePoolingPolicyKind policyKind)
    {
        policyKind = policyId switch { … , _ => default, };
        return policyId is RollingCost or RollingPenalty or FixedFreezeHorizon
            or NoReassignmentRepair or LeastCommitmentConsensus
            or RideBoundHardVector or CommitSoftHardHybrid;
    }
    public static string ToPolicyId(RidePoolingPolicyKind policyKind) => …
        _ => throw new ArgumentOutOfRangeException(nameof(policyKind));
}
```

**Unknown id:** `TryParse` sets `policyKind = default` (= `RollingCost`, note the silent-default hazard) and returns `false`. The caller `Wp4RunnerConfiguration.Decode:230-233` immediately throws:
```csharp
if (!RidePoolingPolicyRegistry.TryParse(policyId, out var policyKind))
    throw new InvalidDataException($"Unknown WP4 policyId '{policyId}'.");
```
Per-policy `PolicyId` strings are re-asserted on the implementations: `HardVectorPolicy.cs:231`, `SoftHardHybridPolicy.cs:276`, `MultiplePlanPolicy.cs:704`, `RollingCostPolicy.cs:27`, `CommitmentMechanismPolicies.cs:28/145/205`.

`SolverBackedRidePoolingPolicyOptions` ctor (`:77-137`) re-validates: B5 is rejected outright (`:87-91`); B3 requires positive horizon + non-empty lock mask (`:93-108`); freeze settings on a non-B3 policy → `"Freeze settings are only valid for the B3 policy."` (`:110-114`); repair cap `>= 1` only for B4 else `"Repair request capacity is only valid for the B4 policy."` (`:116-128`).

---

## 4. The sealed runner — pinning, verification, and the `helloAck` EOF

### What pins a runner build

Three independent layers:

**(a) Per-run artifact receipts (Python adapter).** `simulators\fleetpy-ridebound\ridebound_fleetpy\runner_client.py:481-491` `_hash_artifacts()` SHA-256s every declared artifact path, sorted case-folded. Taken at `start()` (`:125`) and again at `shutdown()` (`:293`):
```python
294  if self._receipts_after != self._receipts_before:
295      self._state = "failed"
296      raise AdapterFailure("RBWP7_RUNNER_ARTIFACT_DRIFT", "$runner.artifacts", "pre/post hash differs")
```
The artifact set is built in `session.py:234-296`: dotnet exe, commitment config, wp4 config, **every file in `runner_root`** (`:283 published = tuple(sorted(path for path in runner_root.iterdir() if path.is_file()))`), six FleetPy files, `environment.lock.yml`, `capability-matrix.json`, every `ridebound_fleetpy/*.py`, the whole scenario root recursively, plus `ridebound_additional_artifacts`.

**(b) Manifest identity (wire).** `session.py:413-467` builds `initializeRun.payload.manifest` with:
- `"policyConfigurationHash": self.settings.policy_binding_hash` — the WP4 binding digest (`session.py:321`, `mapping.py:150-158`)
- `"coreCommitSha": self.settings.core_commit` — `git -C <repository_root> rev-parse HEAD` (`session.py:140-156`)
- `"binarySha256": _sha256(self.settings.runner_dll)` (`session.py:464`, `:129-137`)

Runner-side checks in `src\RideBound.Runner\Protocol\RunnerSession.cs`:
```
300  if (_executionMode == RunnerExecutionMode.OnlineCommitment
301      && payloadResult.Value!.Manifest.PolicyConfigurationHash != _commitmentPolicyConfigurationHash)
304      return Error("HASH_MISMATCH", ProtocolFailureDisposition.FailSession,
307              "Manifest policyConfigurationHash does not match the loaded commitment policy configuration.", …
312  if (_wp4Configuration is not null
313      && (!StringComparer.Ordinal.Equals(…Manifest.PolicyId, _wp4Configuration.PolicyId)
316          || !StringComparer.Ordinal.Equals(…Manifest.PolicyVersion, _wp4Configuration.PolicyVersion)))
320      return Error("HASH_MISMATCH", …FailSession,
323              "Manifest policyId/policyVersion does not match the loaded WP4 policy configuration.", …
```
`_commitmentPolicyConfigurationHash` is wired in `Program.cs:111-115`: the WP4 binding when a wp4 config is loaded, otherwise the bare commitment hash.

**(c) Freeze-receipt tree seals** — see §5.

### The three named hashes

| Name | Where computed | Domain-separated over |
|---|---|---|
| `repositoryInventorySha256` | `actual_fleetpy_medium_preflight.py:740-782` | `b"RideBound.Wp9RepositoryInventory.v1\0"` + len+bytes of `git rev-parse HEAD` + for each path from `git ls-files -z --cached --others --exclude-standard`, sorted: len+relpath bytes, then 8-byte file length, then full file content. **This is the whole Git-visible working tree, tracked *and* untracked-non-ignored.** |
| `semanticHash` | `actual_fleetpy_medium_preflight.py:686-694` | `b"RideBound.Wp7ActualFleetPyMedium.v1\0"` + canonical JSON of the `semantic` dict (`:660-685`) |
| `publicationDigest` | `actual_fleetpy_medium_preflight.py:669-676` | `sha256(json.dumps(control._rb_publications, sort_keys=True, separators=(",",":")))` — nested **inside** `semantic`, so it feeds `semanticHash` |

`semantic` (`:660-685`) contains: `sourceScenarioContentSha256`, `nodeMappingHash`, `manifestHash`, `checkpointBindingHash`, `requestCount`, sorted `acceptedRequestIds` / `rejectedRequestIds`, `publicationCount`, `publicationDigest`, `travelSnapshotVersion`, `nextEventSeq`, `nextEpoch`, `finalSimulationTimeMs`, `finalVehiclePositions`.

### What breaks when repo source changes

1. **`repositoryInventorySha256` moves.** `preflight:836-846` takes it before the repeats and, if `--expected-repository-inventory-sha256` was given, fails with `"repository inventory differs from the frozen matrix source state"`. `:872-884` re-takes it after and fails with `"core commit drifted during the matrix …"` / `"repository content inventory drifted during the matrix run; the Git-visible source tree must stay frozen"`. **Any file — including an untracked scratch file — changes this hash.**
2. **`coreCommitSha` moves** on a commit ⇒ `manifestHash` changes ⇒ `semanticHash` changes ⇒ repeats diverge (`preflight:885-887`).
3. **`binarySha256` / runner tree** changes on a rebuild ⇒ manifest hash changes, and the freeze receipt's `runnerDllSha256` / `runnerArtifactSha256` no longer verify (`wp14_freeze_v2.py:520-526`).
4. **Config bytes change** ⇒ `policyConfigurationHash` no longer matches the runner's loaded config ⇒ `HASH_MISMATCH` at `RunnerSession.cs:300-310`, and `wp14_run_matrix.py:239-242` refuses to launch (`"WP4 config differs from freeze"` / `"commitment config differs from freeze"`).

### `RBWP7_RUNNER_EOF at $runner: helloAck` — the exact path

The error is raised in `runner_client.py:374-375`, inside `_read_expected`:
```python
374  if item is _EOF:
375      self._fail("RBWP7_RUNNER_EOF", message_type)
```
with `message_type == "helloAck"` because `negotiate()` calls `self._read_expected("helloAck")` (`:160`). `_fail` (`:549-551`) sets state `failed` and raises `AdapterFailure(code, "$runner", detail)` — hence the rendering `RBWP7_RUNNER_EOF at $runner: helloAck`. `_EOF` is pushed by the reader thread when `process.stdout.readline()` returns empty (`:313-317`).

**It is not a version mismatch.** It means the runner process closed stdout without answering `hello`. The dominant cause is that the runner **never reached the protocol loop**: `Program.cs` parses the configs *before* `RunnerHost.RunAsync` and exits:
```
 96  await Console.Error.WriteLineAsync(
 97      $"Invalid commitment policy configuration: {error.Message}");
 98  return 64;
```
(also `Program.cs:25-27, :56-62` for bad `--maximum-line-bytes` / bad argv shape, both `return 64`). So **any new/renamed/mistyped key in a commitment or wp4 config surfaces at the adapter as `RBWP7_RUNNER_EOF at $runner: helloAck`, with the real message only on stderr** (readable via `RunnerClient.diagnostics`, `:118-121`).

The *actual* handshake version checks, for reference:
- Adapter side, `runner_client.py:430-431`: `if envelope.get("schemaVersion") != "1.0.0": self._fail("RBWP7_RUNNER_SCHEMA_VERSION_MISMATCH", …)`; then `:161-172` `RBWP7_RUNNER_ACK_INVALID` / `RBWP7_RUNNER_CAPABILITY_DOWNGRADE` (status != "accepted") / `RBWP7_RUNNER_POSITION_DOWNGRADE` / `RBWP7_RUNNER_CAPABILITY_MISSING`.
- Runner side, `src\RideBound.Runner\Protocol\CapabilityNegotiator.cs:69-79`:
```csharp
if (!hello.SupportedSchemaVersions.Any(
        version => ProtocolVersionCompatibility.Evaluate(version).IsCompatible))
{
    return Failure(
        CapabilityNegotiationErrorCode.UnsupportedSchemaVersion,
        "UNSUPPORTED_SCHEMA_MINOR",
        "Client and runner do not share a supported schema version.", …);
}
```
`ProtocolVersionCompatibility.Evaluate` (`src\RideBound.Contracts\Protocol\ProtocolVersionCompatibility.cs:38-70`) rejects a major mismatch (`UnsupportedMajor`) and a higher minor unless an explicit safe forward profile applies (`UnsupportedMinor`).
- Requirements the runner enforces: `RunnerHost.cs:11-21` — `RequiredPositionModel: "nodeOnly"`, `RequiredCapabilities: ["exactEventOrdering"]`, optional `dynamicTravelTimes`/`oldPlanProjection`, min fleet/request 1. The adapter offers `directedEdgeProgress` + 4 capabilities (`session.py:547-565`) and *demands back* `directedEdgeProgress` plus `exactEventOrdering, dynamicTravelTimes, oldPlanProjection` (`runner_client.py:52-57`). `SupportsPositionModel` (`CapabilityNegotiator.cs:253-258`) allows `DirectedEdgeProgress` to satisfy a `NodeOnly` requirement; the ack echoes `hello.PositionModel` (`:217`), which is why the adapter's stricter check passes.
- `InitializeRunValidator.cs:104-157` then cross-binds envelope/helloAck/manifest schema versions (`:104-110`), offered-version patch compatibility (`:112-120`), adapter identity (`:122-134`), and capability selection equality (`:136-157`) — all `IDENTITY_MISMATCH`.

Python test of the EOF path: `simulators\fleetpy-ridebound\tests\test_runner_client.py:239-240` (`"crash": "RBWP7_RUNNER_EOF"`).

---

## 5. Freeze-receipt tooling

Files: `wp13_e1_freeze.py`, `wp14_freeze.py` (v1), `wp14_freeze_v2.py`, `wp14r_freeze_v2..v6.py`, `wp9_freeze_v6.py`, `wp9_freeze_verify.py`, all under `E:\Code\RideBound\simulators\fleetpy-ridebound\`.

### `wp14_freeze_v2.py` (672 lines) — the reference builder

- `STATIC_REPOSITORY_FILES` (`:81-100`) — 18 repo-relative paths: three JSON schemas, `environment.lock.yml`, `capability-matrix.json`, `capability_probe.py`, `actual_fleetpy_medium_preflight.py`, `actual_fleetpy_medium_verify.py`, `wp14_freeze_v2.py` (**self-sealing**), `wp14_run_matrix.py`, `wp14_frontier_analyze.py`, `wp14_development_panel_audit.py`, four `tests/test_wp14_*.py`, one evidence JSON, one research MD. At build time it is extended (`:356-385`) with the grid manifest, every arm's commitment + wp4 config, and every cell driver.
- `sha256_file` `:137-144`; `artifact()` `:147-154` records `{path, lengthBytes, sha256}` and rejects empty files.
- `tree_sha256(root, domain, excluded_names)` `:168-190` — domain prefix + for each file sorted by posix relpath: len+relpath, 8-byte size, content. Exclusion tests `path.relative_to(root).parts` (directory-aware — this is the `__pycache__` fix described in `docs\benchmarking\wp14r-013-v6-matrix-and-h6-rerun-2026-09-05.md:210-217`).
- `runtime_identity` `:203-293` pins: FleetPy commit == `FLEETPY_COMMIT` and clean worktree (`:238-239`), `.NET runtime set == ["10.0.9"]` (`:240-241`), presence of `RideBound.Runner.dll` (`:242-244`), `pythonExecutableSha256`, `dotnetExecutableSha256`, `dotnetRuntimeTreeSha256` (tree seal over the whole `Microsoft.NETCore.App/<ver>` directory), and a `capability_probe.py` result hash.
- `sourceIdentity.treeSeals` `:510-527`:
  ```python
  "adapterPackageSha256":     tree_sha256(repo/"simulators/fleetpy-ridebound/ridebound_fleetpy", b"RideBound.Wp14AdapterPackage.v1", {"__pycache__"}),
  "developmentFixtureSha256": tree_sha256(fixture_root, b"RideBound.Wp14DevelopmentFixture.v1"),
  "runnerArtifactSha256":     tree_sha256(runner_root, b"RideBound.Wp14RunnerArtifact.v1"),
  "runnerDllSha256":          sha256_file(runner_root / "RideBound.Runner.dll"),
  ```
- Receipt is JSON-Schema validated (`:531-537`) and written with `O_EXCL` (`:547-555`) so a receipt can never be overwritten.
- `verify_receipt` `:558-594` **rebuilds the whole receipt from live sources** and demands both structural equality and byte-canonical equality:
  ```python
  585  if actual != expected or receipt_path.read_bytes() != canonical(actual) + b"\n":
  586      raise FreezeError("freeze receipt differs from its sources or is not canonical")
  ```
- CLI `:597-668`: `--repository --output-root --forbidden-root(×N) --runner-root --fleetpy-root --python --dotnet --development-panel-audit --resource-planning-evidence --frozen-at-utc --maximum-parallel-jobs --output --write`. Verify mode is the default; `--frozen-at-utc` is only legal with `--write`.

### `wp14r_freeze_v6.py` (638 lines) — layered on top

- `verify_base_freeze` `:261-294` loads `wp14_freeze_v2.py` dynamically and re-runs its `verify_receipt` against `benchmarks/scenarios/wp14-development/freeze-receipt-v2.json`, first checking `EXPECTED_BASE_RECEIPT_SHA256 = "36a3ff1c…b363"` (`:52-54, :263-264`).
- Its own `REPOSITORY_FILES` (`:100-125`) is self-sealing (`wp14r_freeze_v6.py` + `tests/test_wp14r_freeze_v6.py` both listed).
- `source_identity` `:393-426` **reuses** `base["sourceIdentity"]["treeSeals"]["runnerArtifactSha256"]` rather than recomputing — the runner identity is inherited from the base freeze.
- Adds host policy, isolation roots, mechanics-gate artifacts with pinned SHAs (`:126-140`), and a `jobOrderSha256` over the 160 job ids (`:350`).

### Procedure to build a NEW sealed runner so a new arm is admissible

Derived from `docs\benchmarking\wp8-011c-pre-outcome-runner-artifact-repin.md` (the precedent), `docs\handoffs\wp14-continuation-2026-08-25.md:334`, and the builders:

1. `dotnet test RideBound.slnx` green (AGENTS.md baseline).
2. Clean **Release** publish to a root **outside the repository** (`E:\RideBoundData\...`), Release/win-x64 — precedent roots: `E:\RideBoundData\wp14\runner-v1`, `E:\RideBoundData\wp9\runner\audited-evidence-hotpath-v2-current`. Pattern of the publish command is in `scripts\run-wp3-commitment-demo.ps1:34-41` (`--configuration Release --runtime <rid> --self-contained -p:PublishSingleFile=true -p:ContinuousIntegrationBuild=true --output <root>`); the experiment roots are framework-dependent multi-file trees invoked as `dotnet <root>\RideBound.Runner.dll` (`session.py:189, 336-349`), so the freeze builder requires `RideBound.Runner.dll` to exist in the root (`wp14_freeze_v2.py:242-244`).
3. The publish root must be *stable*: `runner_client._hash_artifacts` hashes **every file** in it, and `tree_sha256` seals it.
4. Add/author the new arm's configs under `benchmarks/configurations/`, the driver/grid entries, and the new-arm row in `ARMS` / `WP4_CONFIG_BY_POLICY`.
5. Write a **new** freeze builder module (`wp14_freeze_v3.py`-style), self-sealing: its own path and its own test path must be in `STATIC_REPOSITORY_FILES` — enforced by `tests\test_wp14_freeze_v2.py:212-222` (`Wp14FreezeV2SelfSealTests`). Never mutate an existing receipt: `write_exclusive` (`:547-555`) refuses, and `wp14r-013:203-206` records that reusing v1's names in v2's `STATIC_REPOSITORY_FILES` was itself a provenance defect.
6. Run the builder with `--write --frozen-at-utc <Z>`; then re-run it **without** `--write` so `verify_receipt` reconstructs and byte-compares.
7. Take the `repositoryInventorySha256` **after** everything is committed and pass it to every run via `--expected-repository-inventory-sha256` (`preflight:934, 843-846`).
8. Run the matrix through `wp14_run_matrix.py`, which re-checks `wp4ConfigSha256` / `commitmentConfigSha256` / `driverSha256` / `scenarioContentSha256` against the receipt (`:239-258`) before spawning the preflight.

---

## 6. Preflight entry point — `actual_fleetpy_medium_preflight.py` (958 lines)

`main()` at `:918-954`. Every flag:

| Flag | Line | Type / default | Effect |
|---|---|---|---|
| `--label` | `:920` | str, **required** | run id becomes `f"wp7-medium-{label}"` (`:230`); the matrix passes `job["jobId"]` |
| `--fleetpy-root` | `:921` | Path, required | prepended to `sys.path` (`:800`); → `ridebound_fleetpy_root` (`:226`); 6 files enter the artifact set |
| `--runner-root` | `:922` | Path, required | → `ridebound_runner_root` (`:221`); must contain `RideBound.Runner.dll` (`session.py:189-191`) |
| `--dotnet` | `:923` | Path, required | → `ridebound_dotnet_path` (`:220`); argv[0] of the runner process |
| `--commitment-config` | `:924` | Path, required | **`:222-224`** `"ridebound_commitment_config": str(arguments.commitment_config.resolve())` |
| `--wp4-config` | `:925` | Path, required | **`:225`** `"ridebound_wp4_config": str(arguments.wp4_config.resolve())` |
| `--scenario` | `:926` | Path, required | read at `:801`; SHA checked against `driver["sourceScenarioContentSha256"]` (`:803-808`); hashed into `semantic` (`:661`); added to artifacts (`:488`) |
| `--derivative-manifest` | `:927` | Path, required | artifact only (`:489`) |
| `--normalization-report` | `:928` | Path, required | artifact only (`:490`) |
| `--selection-frame` | `:929` | Path, required | artifact only (`:491`) |
| `--driver` | `:930` | Path, required | read `:802`; supplies `expectedRequestCount/VehicleCount/NodeCount/DirectedArcCount` (`:812-817`) and `completeTravelSnapshotMaximumNodes` (`:832-834, :502`) |
| `--output` | `:931` | Path, required | `mkdir(parents=True, exist_ok=False)` (`:848`) — **never reuses a directory**; holds `run-NN.json`, `transcript-NN.ndjson`, `failure-NN.json`, `summary.json`, `bundle-manifest.json` |
| `--repeats` | `:932` | int, default 3 | loop `:850-866`; must be ≥ 1 (`:936-937`); all repeats must yield one `semanticHash` (`:885-887`) |
| `--master-seed` | `:933` | int, default 7 | `_validate_master_seed` 0..2147483647 (`:785-793`); → `ridebound_master_seed` (`:232`) → manifest `masterSeed` (`session.py:421`) → solver seed via `--solver-seed-source manifest-master-seed` |
| `--expected-repository-inventory-sha256` | `:934` | str, optional | lowercase 64-hex validated `:942-952`; compared `:843-846` |

**`--repository-root` is not a flag** — it is derived: `arguments.repository_root = adapter_root.parents[1]` (`:798`).

### Forwarding chain for the two config flags
`main` → `run(arguments)` `:953` → `_run_repeat` `:419` → `_operator_settings(...)` `:498-504` → the dict at `:217-242` → FleetPy operator attributes → `RideBoundSessionSettings.from_attributes` (`session.py:182-324`, reads `ridebound_commitment_config` at `:192`, `ridebound_wp4_config` at `:193`) → `RideBoundProtocolSession.__init__` builds the argv (`session.py:336-349`):
```python
command = [str(settings.dotnet), str(settings.runner_dll),
           "--mode", "commitment",
           "--policy-config", str(settings.commitment_config),
           "--wp4-config", str(settings.wp4_config),
           "--solver-seed-source", "manifest-master-seed",
           "--maximum-line-bytes", str(RUNNER_MAXIMUM_INPUT_LINE_BYTES)]
```
(8-argument commitment form, matching `Program.cs:37-50`; `RUNNER_MAXIMUM_INPUT_LINE_BYTES = 64 MiB`, `session.py:27`.)

Adapter-side pre-checks on the configs before the process starts: `session.py:198-203` requires `policyId` / `policyVersion` strings in the wp4 file (`RBWP7_WP4_POLICY_INVALID`); `_require_declared_commitment_policy` `:103-126` requires `ridebound_commitment_policy_id` (hard-coded `"wp6-synthetic-policy-overlay-v1"` at `preflight:234`) to appear in `$.policies[].policyId` (`RBWP7_COMMITMENT_POLICY_UNDECLARED`). `_read_json` `:92-100` rejects duplicate JSON keys.

---

## 7. Template: adding a new config FIELD end to end (traced on `ratchetLocks`)

`ratchetLocks` is the newest optional commitment-policy field; here is every file it touches, in order.

**1. JSON text** — `E:\Code\RideBound\benchmarks\configurations\wp14-c1-f2-ratchet-v1.json:99-101` and `wp14-c1-f1f2-freeze300-ratchet-v1.json:102-104`:
```json
"ratchetLocks": [ "pickupEta" ]
```

**2. Reader allowlist** — `src\RideBound.Runner\Configuration\CommitmentPolicyConfiguration.cs:28` — add the key to `PolicyFields` (or `RootFields`/`LimitFields`/`RevisionFields` as appropriate). Omitting this makes `RequireObject` (`:280-289`) throw `Unknown field 'ratchetLocks' at '$.policies[]'`, which (see §4) reaches the adapter only as `RBWP7_RUNNER_EOF at $runner: helloAck`.

**3. Reader parse + wiring** — `CommitmentPolicyConfiguration.cs:183`, inside `ReadPolicy`:
```csharp
183            ReadLocks(element, "ratchetLocks"));
```
Optional-field pattern: `ReadLocks` returns `PromiseLock.None` when absent (`:233-238`). Scalar analogue is `freezeHorizonMs` at `:178-180`, numeric-optional is `OptionalPositiveInteger` at `:328-333`.

**4. Domain object** — `src\RideBound.Domain\Commitments\CommitmentPolicy.cs`:
- ctor parameter with default `:137` `PromiseLock ratchetLocks = PromiseLock.None`
- invariant `:184-194`:
```csharp
const PromiseLock orderedLocks = PromiseLock.PickupEta | PromiseLock.DropEta;
// A ratchet needs an order on the field. Vehicle and stop identities have
// none, so only the two ETA fields can be relaxed this way.
if ((ratchetLocks & ~orderedLocks) != 0)
    throw new ArgumentOutOfRangeException(nameof(ratchetLocks),
        "Only pickup and drop ETA locks can be relaxed to a ratchet.");
```
- assignment `:202`, public property + doc comment `:221-229`.

**5. Consumer (the "assessor" chain)** — `src\RideBound.Domain\Commitments\CommitmentLockEvaluator.cs`:
- `:77` passes `policy.RatchetLocks` into `AddWitnesses`
- `:94` new parameter
- `:119-137` applies it to `pickup_eta_ms` / `drop_eta_ms`
- `:140-147` the behaviour:
```csharp
/// An exact lock rejects any movement. A ratcheted lock rejects only movement
/// that makes the promise later, so the decision may still improve it.
private static bool Violates(SimTime before, SimTime after, bool ratcheted) =>
    ratcheted ? after.Milliseconds > before.Milliseconds : after != before;
```

**6. Application validator** — `src\RideBound.Application\Commitments\CommitmentDecisionValidator.cs:347-373` calls `_lockEvaluator.Evaluate(request, priorHistory.Current.PublishedPromise, exogenousProjection, candidateProjection, simTime, policy)` and turns witnesses into `CommitmentValidationStage.Lock` failures. **No edit was needed here** because the field travels inside `policy`.

**7. Algorithms / candidate assessor** — `src\RideBound.Algorithms\Commitments\CommitmentCandidateAssessor.cs:217-228` invokes the validator with the same `CommitmentPolicy`. **No edit needed.** Caveat for a *new* field: `MechanismCommitmentPolicyProvider.TryGetPolicy` (`:97-108`) **rebuilds** a stripped policy and currently does **not** forward `ratchetLocks` (it passes only `_freezeHorizon`, `_freezeLocks`, `finalConfirmationLocks: PromiseLock.None`) — so a new field silently defaults to zero on the B2 revision-penalty mechanism path. Any new field must decide explicitly whether it belongs there.

**8. Solver-backed policy** — `src\RideBound.Algorithms\Policies\SolverBackedRidePoolingPolicy.cs:259` and `HardVectorPolicy.cs` / `SoftHardHybridPolicy.cs` consume the same policy object. No edit for a commitment-policy field.

**Files that do NOT need editing for a commitment-policy field:** `OnlineStateCanonicalizer.cs` and `OnlineStateCheckpointCodec.cs` — their `budgetBasis` handling (`:383-390` / `:298-303`) is the **ledger entry's** basis, not the policy config. They only change if the new field alters ledger-entry shape.

**If the new field belongs to the WP4 policy config instead:** the equivalent chain is `Wp4RunnerConfiguration.cs` — add to the relevant `Fields(...)` set (`:31-92`), parse in `Decode` (`:257-386`) or the sub-readers (`ReadGeneration :389-432`, `ReadSolverBudget :434-482`, `ReadWarningProfiles :484-569`), extend `RequireVariantFields` (`:571-593`) if it is variant-scoped, thread it through the private ctor (`:95-117`) and the public properties (`:119-146`), and — if it must survive a manifest-seeded run — through `CreateSolverPolicyOptionsForRun` (`:162-199`) into `SolverBackedRidePoolingPolicyOptions` (`SolverBackedRidePoolingPolicy.cs:77-137`), then consume it at `RunnerSession.cs:846-902`.

**Hash consequence (must be in the plan):** adding a field to any config file changes that file's canonical SHA-256 ⇒ `ContentHash` ⇒ `Wp4PolicyConfigurationBinding` ⇒ `manifest.policyConfigurationHash` ⇒ `manifestHash` ⇒ `semanticHash`, and it changes `repositoryInventorySha256`. Every frozen receipt naming that file (`arm["commitmentConfigSha256"]`, `arm["wp4ConfigSha256"]`, `sourceIdentity.repositoryFiles`) stops verifying. That is why `Wp4RunnerConfiguration.cs:21-29` keeps `retained-portfolio-full-witness-v1` as a *separate* profile instead of widening `retained-portfolio-v1`.

---

## 8. Test projects and the tests that must be updated

`RideBound.slnx` declares 9 test projects under `tests/`: `RideBound.Algorithms.Tests`, `RideBound.ArchitectureTests`, `RideBound.Application.Tests`, `RideBound.Benchmarking.Contracts.Tests`, `RideBound.Benchmarking.Tests`, `RideBound.Contracts.Tests`, `RideBound.Domain.Tests`, `RideBound.Runner.Tests`, `RideBound.Solvers.OrTools.Tests`.

### Commitment-config parsing
| File | Lines | What it pins |
|---|---|---|
| `tests\RideBound.Runner.Tests\Configuration\CommitmentPolicyConfigurationTests.cs` | 103 | **Hard-coded content hash** `"d1be06163dd38de567e4489100acd05b74c41cc454300f7b7286b459355e928f"` for `wp3-boundary-test-v1.json` (`:22-23`) — **any change to that fixture breaks this**; unknown-field rejection (`:43-60`); duplicate-phase and same-node-distance rejection (`:62-95`) |
| `tests\RideBound.Runner.Tests\Configuration\Wp14FactorConfigurationTests.cs` | 188 | All 9 `wp14-c1-*` levels decode (`:16-47`); reference == `wp8-drop-eta-budget-tight-v1` (`:49-62`); each factor moves exactly one thing (`:64-146`); **all nine content hashes distinct** (`:148-157`). A new arm/level must be added to `FactorConfigurations()` at `:16-27` |
| `tests\RideBound.Runner.Tests\Configuration\Wp4RunnerConfigurationTests.cs` | 564 | 14 cases incl. `Policy_specific_fields_are_required_and_forbidden_exactly` (`:442-468`, asserts the `"variant fields"` message), `C2_requires_all_profiles_and_rejects_warning_above_hard_limit` (`:470-507`), `B5_uses_explicit_plan_pool_budget_and_forbids_solver_block` (`:509-541`), `Retained_portfolio_profile_is_strict_solver_only_and_seed_preserving` (`:166-250`), `Full_witness_collection_needs_its_own_profile` (`:251-294`), `Frozen_e1_configurations_do_not_collect_the_full_witness_set` (`:295-331`), `Constant_level_skip_is_optional_and_off_unless_declared` (`:332-391`), `Candidate_retention_strategy_is_explicit_for_new_configs_and_legacy_when_absent` (`:392-441`). Fixtures: `wp3-boundary-test-v1.json` (`:543-549`) and `wp4-rolling-cost-boundary-v1.json` (`:551-556`) |
| `tests\RideBound.Contracts.Tests\Protocol\Wp4PolicyConfigurationBindingTests.cs` | 43 | The binding digest |

### Assessor / lock-evaluation
| File | Lines | Notes |
|---|---|---|
| `tests\RideBound.Domain.Tests\Commitments\CommitmentLockEvaluatorTests.cs` | 132 | accepted-assignment, onboard, `Freeze_horizon_and_final_confirmation_use_explicit_policy_flags` (`:55-91`), exogenous-drift (`:92-`) |
| `tests\RideBound.Domain.Tests\Commitments\CommitmentRatchetLockTests.cs` | 145 | **the template test-file for a new optional field**: `A_ratchet_only_rejects_a_later_pickup` (`:22-52`), `A_ratchet_on_one_field_does_not_relax_the_other` (`:53-75`), `Only_ordered_eta_fields_can_be_ratcheted` (`:76-90`), `A_policy_ratchets_nothing_by_default` (`:91-94`) |
| `tests\RideBound.Domain.Tests\Commitments\CommitmentPolicyTests.cs` | 56 | policy-ctor invariants |
| `tests\RideBound.Application.Tests\Commitments\CommitmentDecisionValidatorTests.cs` | 475 | + `CommitmentValidatorFixtures.cs` (164), `CommitmentWitnessCollectionTests.cs` (117) |
| `tests\RideBound.Algorithms.Tests\Oracle\ExactSmallCommitmentDifferentialTests.cs` | 1030 | the only direct `CommitmentCandidateAssessor.AssessRevisionPenalty` caller in tests (`:30-31, :73-74`) |
| `tests\RideBound.Algorithms.Tests\Policies\CommitmentMechanismPolicyTests.cs` | 447 | B2/B3/B4 mechanism policies |
| `tests\RideBound.Runner.Tests\Online\Wp4RunnerIntegrationTests.cs` | 823 | end-to-end over the real runner session: manifest binding, audited evidence, retained portfolio, booking-confirmation C1 ranking, manifest-seed mode, `Manifest_policy_identity_mismatch_fails_before_online_state_changes` (`:544-568`), B5 checkpoint/restore |
| `tests\RideBound.Runner.Tests\Online\CommitmentRunnerSessionTests.cs` (243), `CommitmentCheckpointProcessTests.cs` (125) | | session + checkpoint |
| `tests\RideBound.ArchitectureTests\DependencyRuleTests.cs` | | `AllowedReferences` (`:8-31`): Domain and Contracts have **zero** references; Application→Domain only; Algorithms→Application+Domain; Runner→Algorithms, Application, Contracts, Infrastructure, Solvers.OrTools. Plus a forbidden-term source scan (`:98-128`) |

### Python side (pytest/unittest under `simulators\fleetpy-ridebound\tests\`, 49 files)
Most relevant to this work: `test_runner_client.py` (handshake + adversarial stdout, `:232-256`), `test_protocol.py`, `test_fleet_control.py`, `test_mapping.py`, `test_medium_verifier.py`, `test_wp14_run_matrix.py`, `test_wp14_freeze.py`, `test_wp14_freeze_v2.py` (incl. `Wp14FreezeV2SelfSealTests`, `:212-234`), `test_wp14r_freeze_v2..v6.py`, `test_wp9_freeze_v6.py` / `test_wp9_freeze_verify.py`.

---

## Appendix A — all 27 files in `benchmarks/configurations/`

**Commitment configs (14)** — root key `policies`, all `policyId` `wp6-synthetic-policy-overlay-v1` except `wp3-boundary-test-v1.json` (`uniform-v1`):
`wp14-c1-budget120-v1.json` (2378 B), `wp14-c1-budget60-v1.json` (2377), `wp14-c1-f1-freeze300-v1.json` (2448), `wp14-c1-f1-freeze600-v1.json` (2448), `wp14-c1-f1f2-freeze300-ratchet-v1.json` (2501), `wp14-c1-f2-ratchet-v1.json` (2430), `wp14-c1-h6-reference-v1.json` (2377), `wp14-c1-nobudget-v1.json` (2347), `wp14-c1-nopickuplock-v1.json` (2356), `wp3-boundary-test-v1.json` (1882), `wp6-public-mechanical-commitment-v1.json` (1903), `wp8-drop-eta-budget-loose-v1.json` (2378), `wp8-drop-eta-budget-medium-v1.json` (2377), `wp8-drop-eta-budget-tight-v1.json` (2377), `wp8-relaxed-stopswitch-commitment-v1.json` (2295).

**WP4 policy configs (12)**: `wp13-e1-fleetpy-ridebound-hard-vector-retained-v1.json`, `wp13-e1-fleetpy-rolling-cost-retained-v1.json`, `wp14-development-ridebound-hard-vector-v1.json`, `wp14-development-rolling-cost-v1.json`, `wp4-ridebound-hard-vector-boundary-v1.json`, `wp4-rolling-cost-boundary-v1.json`, `wp7-fleetpy-ridebound-hard-vector-v1.json`, `wp7-fleetpy-rolling-cost-v1.json`, `wp9-fleetpy-ridebound-hard-vector-audited-v1.json`, `wp9-fleetpy-rolling-cost-audited-v1.json`, `wp9-fleetpy-soft-hard-hybrid-audited-v1.json`.

**Neither (1)**: `wp10-ridepy-paired-subset-v1.json` (3525 B) — a RidePy paired-subset descriptor (`subsetId`, `arms`, `graph`, `baseOd`), not consumed by either C# reader.

**No config in this directory uses `fixedFreeze`, `repair`, or `multiplePlan`** — B3/B4/B5 variants exist only in test literals.

### Full content — `wp14-c1-h6-reference-v1.json`
```json
{
  "configurationVersion": "1.0.0",
  "policies": [
    {
      "policyId": "wp6-synthetic-policy-overlay-v1",
      "budgetBasis": "decisionInduced",
      "limits": [
        { "dimension": "pickup_eta_total_ms",
          "applicablePhases": ["accepted","waitingPickup","onboard"] },
        { "dimension": "drop_eta_total_ms",
          "applicablePhases": ["accepted","waitingPickup","onboard"],
          "hardLimit": 30000 },
        { "dimension": "material_eta_revision_count",
          "applicablePhases": ["accepted","waitingPickup","onboard"] },
        { "dimension": "vehicle_switch_count", "hardLimit": 0,
          "applicablePhases": ["accepted","waitingPickup","onboard"] },
        { "dimension": "pickup_stop_relocation_mm",
          "applicablePhases": ["accepted","waitingPickup"] },
        { "dimension": "pickup_stop_switch_count", "hardLimit": 0,
          "applicablePhases": ["accepted","waitingPickup"] },
        { "dimension": "drop_stop_relocation_mm",
          "applicablePhases": ["accepted","waitingPickup","onboard"] },
        { "dimension": "drop_stop_switch_count", "hardLimit": 0,
          "applicablePhases": ["accepted","waitingPickup","onboard"] },
        { "dimension": "incumbent_order_inversion_count",
          "applicablePhases": ["accepted","waitingPickup","onboard"] },
        { "dimension": "pre_pickup_inserted_stop_count",
          "applicablePhases": ["accepted","waitingPickup"] }
      ],
      "materialRevisionRule": {
        "rawEtaThresholdMs": 1000,
        "displayBucketWidthMs": 60000
      },
      "finalConfirmationLocks": ["vehicle","pickupStop","pickupEta"]
    }
  ],
  "stopDistances": []
}
```
(reproduced from the file with array formatting compacted; key order and values verbatim.)

### Full content — `wp9-fleetpy-ridebound-hard-vector-audited-v1.json`
```json
{
  "configurationVersion": "1.0.0",
  "policyId": "ridebound-hard-vector",
  "policyVersion": "wp9-confirmatory-audited-v1",
  "initialPromiseTrigger": "booking-confirmation",
  "emitSolverExecutionEvidence": true,
  "candidateGeneration": {
    "maximumCandidatesPerVehicle": 100,
    "maximumNewRequestsPerVehicle": 2,
    "exactSmallMode": false,
    "scheduleStrategy": "earliest-feasible",
    "maximumExplorationWorkUnits": 10000,
    "retentionStrategy": "service-set-stability-portfolio-v1"
  },
  "solverExecution": {
    "adapterVersion": "google-ortools-9.15.6755",
    "maximumGenerationWorkUnits": 10000,
    "maximumValidationWorkUnits": 10000,
    "maximumSolverWorkUnits": 100000,
    "maximumSolverDeterministicTimeMicros": 1000000,
    "randomSeed": 7
  }
}
```

### Full content — `wp9-fleetpy-soft-hard-hybrid-audited-v1.json`
```json
{
  "configurationVersion": "1.0.0",
  "policyId": "commit-soft-hard-hybrid",
  "policyVersion": "wp9-exploratory-audited-v1",
  "initialPromiseTrigger": "booking-confirmation",
  "emitSolverExecutionEvidence": true,
  "candidateGeneration": {
    "maximumCandidatesPerVehicle": 100,
    "maximumNewRequestsPerVehicle": 2,
    "exactSmallMode": false,
    "scheduleStrategy": "earliest-feasible",
    "maximumExplorationWorkUnits": 10000,
    "retentionStrategy": "service-set-stability-portfolio-v1"
  },
  "warningProfiles": [
    {
      "policyId": "wp6-synthetic-policy-overlay-v1",
      "limits": [
        { "dimension": "pickup_eta_total_ms" },
        { "dimension": "drop_eta_total_ms", "warningLimit": 60000 },
        { "dimension": "material_eta_revision_count" },
        { "dimension": "vehicle_switch_count" },
        { "dimension": "pickup_stop_relocation_mm" },
        { "dimension": "pickup_stop_switch_count" },
        { "dimension": "drop_stop_relocation_mm" },
        { "dimension": "drop_stop_switch_count" },
        { "dimension": "incumbent_order_inversion_count" },
        { "dimension": "pre_pickup_inserted_stop_count" }
      ]
    }
  ],
  "solverExecution": {
    "adapterVersion": "google-ortools-9.15.6755",
    "maximumGenerationWorkUnits": 10000,
    "maximumValidationWorkUnits": 10000,
    "maximumSolverWorkUnits": 100000,
    "maximumSolverDeterministicTimeMicros": 1000000,
    "randomSeed": 7
  }
}
```
Note: `drop_eta_total_ms` `warningLimit: 60000` only validates because the paired commitment config's hard limit for that dimension is finite and ≥ 60000 (`Wp4RunnerConfiguration.cs:542-548`).

---

## Appendix B — wire protocol summary (`ridebound_fleetpy/`)

- **`protocol.py` (414)** — `OrderedEventBuffer` (`:105-204`) buffers callbacks, enforces monotone `simulationTime` (`RBWP7_CALLBACK_TIME_REGRESSION` `:139-144`, `RBWP7_BATCH_TIME_REGRESSION` `:168-173`), dedupes (`RBWP7_CALLBACK_DUPLICATE` `:150-153`), and drains into an `eventBatch` envelope with gapless `eventSeq` and monotone `epochId` (`:181-204`), always appending a `timerTick` unless suppressed. `parse_decision` (`:207-327`) accepts exactly `requestAccepted | requestRejected | requestDeferred | vehiclePlanUpdated | promisePublished`; `offerProposed` / `commitmentBreachDeclared` are explicitly `RBWP7_DECISION_TYPE_UNSUPPORTED` (`:322-323`). `_exact_object` (`:14-24`) does set-equality on keys — **no unknown or missing field tolerated anywhere**. `_validate_vector` (`:396-414`) pins the 10 camelCase commitment-vector keys.
- **`runner_client.py` (551)** — state machine `created → new → negotiated → initialized ⇄ pending → closed` (`_require_state` `:467-469`). Strict NDJSON: LF-only framing (`RBWP7_RUNNER_CRLF_FORBIDDEN` `:387-388`), duplicate JSON keys rejected (`_strict_object` `:519-526`), floats and `NaN/Infinity` rejected (`_reject_json_number` `:528-530`), envelope key allowlist `:426-429`, `schemaVersion == "1.0.0"` `:430-431`. Shutdown drains stdout and requires EOF with no extra frames (`_assert_no_extra_stdout` `:493-517`), then re-hashes artifacts (`:293-296`) and requires exit 0 (`:297-299`).
- **`session.py` (565)** — pins `FLEETPY_VERSION = "1.0.2"`, `FLEETPY_COMMIT = "053aa9d4fcfde91c5d303435d5748f9206c071b0"`, `ADAPTER_ID/VERSION` (`:16-19`). `restart()` (`:495-532`) does a full re-handshake against a **byte-identical** `initializeRun` and requires the same `manifestHash` (`RBWP7_RESTART_MANIFEST_MISMATCH` `:521-526`), then `restore(payload)` which verifies the returned `checkpointHash` (`runner_client.py:192-203`).
- **`transcript.py` (74)** — append-only, opened with `"xb"` so an existing transcript path is a hard failure (`:17-24`); one canonical-JSON record per frame with `ordinal`, `direction`, `frameLengthBytes`, `frameSha256`, `frameBase64`, flushed every write (`:41-58`). Shared across runner restarts.
