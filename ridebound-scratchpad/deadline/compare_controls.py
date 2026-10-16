"""T2.4 control comparison: the new runner must reproduce drift-v1 at k = 0.

For every panel-A cell and both control arms, compare the new output with the drift-v1
output of the same arm:
  - label (classify.classify_output); drift-v1 artifacts missing for a cell -> "no-artifact"
  - accepted count (len(run-00.json semantic.acceptedRequestIds))
  - decision identity (levelc/decision_identity.trace): ordered (vehicleId, candidateId) plans,
    per-frame sorted published promises, per-frame reason codes
Message text and candidate ids of FAILURE witnesses are not compared (ADR-074: the new
runner cites the no-op, the old one the ordinal-first candidate).

Read-only. Usage: compare_controls.py <new-root> [cells...]   (default: all 20 cells)
Exit 1 if any completed-vs-completed decision trace differs or a label pairing is not allowed.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "levelc"))

import classify  # noqa: E402
import decision_identity as di  # noqa: E402
import run_deadline as rd  # noqa: E402

OLD_ROOT = Path(r"E:/RideBoundData/wp14/drift-v1")
ARMS = {"ctl-conduct": "dr-conduct", "ctl-visible": "dr-visible"}
# Known from drift-v1 / WP9 (thesis bang:doicho): the outcome basis at k = 0 is
# commitment-infeasible on exactly these four panel-A cells.
KNOWN_VISIBLE_INFEASIBLE = {"d20181116-s10-r2", "d20181116-s10-r4",
                            "d20181117-s10-r1", "d20181117-s10-r3"}


def accepted(directory: Path):
    run = directory / "run-00.json"
    if not run.exists():
        return None
    return len(json.loads(run.read_text(encoding="utf-8"))["semantic"]["acceptedRequestIds"])


def main() -> int:
    new_root = Path(sys.argv[1])
    cells = sys.argv[2:] or rd.PANEL_A["cells"]
    bad = 0
    print("arm\tcell\tnew_label\told_label\tnew_acc\told_acc\tplans\tpromises\treasons")
    for arm, old_arm in ARMS.items():
        for cell in cells:
            new = new_root / f"{arm}-k0-{cell}-s7"
            old = OLD_ROOT / f"{old_arm}-k0-{cell}-s7"
            if not new.exists():
                continue
            new_label = classify.classify_output(new)
            if new_label == "no-artifact":
                print(f"{arm}\t{cell}\tpending (job still running)")
                continue
            old_label = classify.classify_output(old) if old.exists() else "no-artifact"
            row = [arm, cell, new_label, old_label, accepted(new), accepted(old)]
            if new_label == "completed" and old_label == "completed":
                a, b = di.trace(new), di.trace(old)
                same = [a[i] == b[i] for i in range(3)]
                row += ["same" if s else "DIFF" for s in same]
                if not all(same) or row[4] != row[5]:
                    bad += 1
            else:
                row += ["-", "-", "-"]
                # A cell that completed in drift-v1 must complete now, and vice versa.
                if (new_label == "completed") != (old_label == "completed"):
                    bad += 1
            if arm == "ctl-visible":
                expected = cell in KNOWN_VISIBLE_INFEASIBLE
                if classify.is_commitment_infeasible(new_label) != expected:
                    bad += 1
                    row.append("UNEXPECTED-INFEASIBILITY")
            elif classify.is_commitment_infeasible(new_label):
                bad += 1
                row.append("CONDUCT-COMMITMENT-INFEASIBLE")
            print("\t".join(str(v) for v in row))
    print(f"mismatching cells: {bad}")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
