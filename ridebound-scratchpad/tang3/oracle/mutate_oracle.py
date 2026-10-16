"""Mutation check of the oracle itself: each mutant of accounting.py must make test_accounting.py
fail. Mutants are written to a temporary directory (never over the real file) and run there.
Usage: python -B mutate_oracle.py"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = (HERE / "accounting.py").read_text(encoding="utf-8")
MUTANTS = {
    "signed conduct": ("totals.C += abs(c)", "totals.C += c"),
    "visible counts e instead of v": ("totals.V += abs(z)", "totals.V += abs(row.p - row.e)"),
    "exogenous charged to conduct": ("totals.C += abs(c)", "totals.C += abs(z)"),
    "closed coordinate still accumulates": ("        if row.closed:\n            continue\n", ""),
    "uncommitted rows counted": ("        if not row.committed:\n            continue\n", ""),
    "no continuity check": ("        if row.v != totals.chain_p:", "        if False:"),
    # The defect found on real data (2026-09-25): the chain stopped at the first closed row.
    "chain not advanced on closed rows": (
        "        totals.chain_p = row.p\n        if row.closed:\n            continue\n",
        "        if row.closed:\n            continue\n        totals.chain_p = row.p\n"),
    "endpoint uses first published instead of last": ("totals.E = abs(totals.last_p - totals.p0)",
                                                      "totals.E = 0"),
    "M+ two-sided": ("max(0, row.p - totals.p0)", "abs(row.p - totals.p0)"),
    "no range check": ("    if value < 0 or value > MAX_CANONICAL:", "    if False:"),
    "duplicates allowed": ("if key in seen and row.sequence <= seen[key]:", "if False:"),
}
survivors = []
for name, (old, new) in MUTANTS.items():
    if old not in SOURCE:
        print(f"MUTANT NOT APPLICABLE: {name}")
        survivors.append(name)
        continue
    with tempfile.TemporaryDirectory() as tmp:
        (Path(tmp) / "accounting.py").write_text(SOURCE.replace(old, new, 1), encoding="utf-8")
        shutil.copy(HERE / "test_accounting.py", tmp)
        result = subprocess.run([sys.executable, "-B", "test_accounting.py"], cwd=tmp,
                                capture_output=True, text=True)
        killed = result.returncode != 0
        print(f"{'killed ' if killed else 'SURVIVED'}  {name}")
        if not killed:
            survivors.append(name)
print(f"{len(survivors)} surviving mutant(s)")
raise SystemExit(1 if survivors else 0)
