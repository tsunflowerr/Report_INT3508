"""Reference-stage check: conduct-30 k=1 on panel A (new runner) vs wp14/drift-v1 dr-conduct-k1.

drift-v1 kept artifacts only for its 9 completed k=1 cells; the other 11 stopped on the pickup
window invariant (thesis bang:phanloai: 9 run, 0 commitment, 11 invariant). The new runner must
complete the same 9 cells with identical decisions, and stop on the other 11 without any
commitment-* label. Also prints every 2b-conduct label. Read-only.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "levelc"))

import classify  # noqa: E402
import decision_identity as di  # noqa: E402
import run_deadline as rd  # noqa: E402
from compare_controls import accepted  # noqa: E402

OLD = Path(r"E:/RideBoundData/wp14/drift-v1")
bad = 0
print("cell\tnew_label\told_label\tnew_acc\told_acc\tplans\tpromises\treasons")
for cell in rd.PANEL_A["cells"]:
    new = rd.OUT_ROOT / f"conduct-30-k1-{cell}-s7"
    old = OLD / f"dr-conduct-k1-{cell}-s7"
    nl = classify.classify_output(new)
    ol = classify.classify_output(old) if old.exists() else "no-artifact(stopped in drift-v1)"
    row = [cell, nl, ol, accepted(new), accepted(old) if old.exists() else None]
    if nl == "completed" and ol == "completed":
        a, b = di.trace(new), di.trace(old)
        same = [a[i] == b[i] for i in range(3)]
        row += ["same" if s else "DIFF" for s in same]
        bad += (not all(same)) or row[3] != row[4]
    else:
        row += ["-", "-", "-"]
        bad += (nl == "completed") != (ol == "completed")
    bad += classify.is_commitment_infeasible(nl)
    print("\t".join(str(v) for v in row))
print(f"panel A k=1 mismatches: {bad}")
print()
inv = 0
for cell in rd.PANEL_DEV["cells"]:
    label = classify.classify_output(rd.OUT_ROOT / f"conduct-30-k1-{cell}-s7")
    inv += classify.is_commitment_infeasible(label)
    print(f"2b-conduct\t{cell}\t{label}")
print(f"2b-conduct commitment-infeasible: {inv}")
raise SystemExit(1 if bad or inv else 0)
