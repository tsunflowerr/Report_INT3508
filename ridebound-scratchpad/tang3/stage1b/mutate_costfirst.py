"""Mutation check for the ADR-078 cost-first option (scratch, not part of the repository).

Each mutant replaces exactly one source snippet in the worktree, runs the targeted tests, and restores
the original bytes (verified by SHA-256) before the next mutant. A mutant is "killed" when the targeted
test run fails.
"""
import hashlib
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(r"C:/Code/RideBound-costfirst")
SEL = ROOT / "src/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs"
POL = ROOT / "src/RideBound.Algorithms/Policies/SolverBackedRidePoolingPolicy.cs"
CFG = ROOT / "src/RideBound.Runner/Configuration/Wp4RunnerConfiguration.cs"
FILTER = ("FullyQualifiedName~SolverBackedFleetSelectionTests|FullyQualifiedName~ExactSmallCommitmentDifferentialTests"
          "|FullyQualifiedName~Wp4RunnerConfigurationTests")

MUTANTS = [
    ("M1 cost-first ignored in the level switch", SEL,
     "                    when hardTreatmentActive\n                        && objectiveOrder\n"
     "                            == SolverBackedSelectionObjectiveOrder.StabilityFirst:",
     "                    when hardTreatmentActive:"),
    ("M2 cost-first also drops the forced level", SEL,
     "            if (forcedTreatmentActive)\n",
     "            if (forcedTreatmentActive\n                && objectiveOrder == SolverBackedSelectionObjectiveOrder.StabilityFirst)\n"),
    ("M3 policy does not pass the order to the selector", POL,
     "            hardAssessments,\n            policyOptions.SelectionObjectiveOrder);",
     "            hardAssessments);"),
    ("M4 run options drop the order", CFG,
     "            source.ForcedNoWorseRecovery,\n            source.SelectionObjectiveOrder);",
     "            source.ForcedNoWorseRecovery);"),
    ("M5 parser maps cost-first to stability-first", CFG,
     "                CostFirstSelectionOrder => SolverBackedSelectionObjectiveOrder.CostFirst,",
     "                CostFirstSelectionOrder => SolverBackedSelectionObjectiveOrder.StabilityFirst,"),
    ("M6 parser accepts cost-first for every solver policy", CFG,
     "            && (!hasSolver || policyKind != RidePoolingPolicyKind.RideBoundHardVector))",
     "            && !hasSolver)"),
    ("M7 cost-first also drops the operational-cost level", SEL,
     "            objectives.Add(\n                MinSum(\n                    \"operational-cost\",",
     "            if (objectiveOrder == SolverBackedSelectionObjectiveOrder.StabilityFirst)\n"
     "            objectives.Add(\n                MinSum(\n                    \"operational-cost\","),
]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    results = []
    for name, path, old, new in MUTANTS:
        original = path.read_bytes()
        text = original.decode("utf-8")
        if text.count(old) != 1:
            print(f"{name}: snippet count {text.count(old)} != 1, not applied")
            results.append((name, "NOT-APPLIED"))
            continue
        path.write_bytes(text.replace(old, new).encode("utf-8"))
        try:
            run = subprocess.run(
                ["dotnet", "test", "RideBound.slnx", "--filter", FILTER],
                cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
            summary = [line.strip() for line in run.stdout.splitlines()
                       if line.strip().startswith(("Passed!", "Failed!")) or " error " in line]
            failed = [line.strip() for line in run.stdout.splitlines() if line.strip().startswith("Failed ")]
            verdict = "KILLED" if run.returncode != 0 else "SURVIVED"
            print(f"{name}: {verdict}; exit={run.returncode}")
            for line in summary[:6] + failed[:8]:
                print("    ", line)
            results.append((name, verdict))
        finally:
            path.write_bytes(original)
            assert sha(path.read_bytes()) == sha(original), f"restore failed for {path}"
    print("SUMMARY", results)
    return 0 if all(v == "KILLED" for _, v in results) else 1


if __name__ == "__main__":
    sys.exit(main())
