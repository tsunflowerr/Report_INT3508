"""Tests for classify.py. Run: python -B test_classify.py (exits non-zero on failure)."""
import json
import re
import tempfile
from pathlib import Path

import classify as c

failures = []

# A C# string literal (plain or interpolated) and a chain of them joined by `+`.
LITERAL = r'\$?"(?:[^"\\]|\\.)*"'
CHAIN = re.compile(rf"{LITERAL}(?:\s*\+\s*{LITERAL})*")


def joined_literals(source: str) -> list[str]:
    """Every concatenated chain of string literals, joined, with quotes removed."""
    out = []
    for match in CHAIN.finditer(source):
        pieces = re.findall(LITERAL, match.group(0))
        out.append("".join(piece.lstrip("$")[1:-1] for piece in pieces))
    return out


def check(name, condition):
    if not condition:
        failures.append(name)
        print("FAIL", name)


# 1. Every message constant appears in its source file, after joining literal chains.
for message, relative in c.CONSTANTS:
    source = (c.WORKTREE / relative).read_text(encoding="utf-8")
    check(f"constant present in {relative}: {message[:40]}",
          any(message in literal for literal in joined_literals(source)))

prefix = "RBWP7_RUNNER_PROTOCOL_ERROR at $runner: INTERNAL_ERROR: "
# 2. Labels.
noop_cite = c.ALL_REJECTED[0] + c.CITE_NOOP[0] + ": "
first_cite = c.ALL_REJECTED[0] + c.CITE_FIRST[0] + ": "
cases = {
    prefix + noop_cite + c.DEADLINE_LATE[0]: "commitment-all-rejected/deadline-late",
    prefix + noop_cite + c.DEADLINE_WINDOW[0]: "commitment-all-rejected/deadline-window",
    prefix + noop_cite + c.BUDGET[0]: "commitment-all-rejected/budget",
    prefix + first_cite + c.BUDGET[0]: "commitment-all-rejected/budget",
    prefix + noop_cite + c.PHASE_LOCK[0]: "commitment-all-rejected/lock",
    prefix + noop_cite + "Actual pickup physical": "all-rejected/non-commitment",
    prefix + c.ALL_REJECTED[0] + "Unknown citation: " + c.BUDGET[0]: "other",
    prefix + c.NOOP_REJECTED[0] + c.DEADLINE_WINDOW[0]: "commitment-noop-rejected/deadline-window",
    prefix + c.NOOP_REJECTED[0] + c.DEADLINE_LATE[0]: "commitment-noop-rejected/deadline-late",
    prefix + c.NOOP_REJECTED[0] + c.BUDGET[0]: "commitment-noop-rejected/budget",
    prefix + c.NOOP_REJECTED[0] + "PICKUP_WINDOW physical": "noop-rejected/non-commitment",
    "SOLVER_MODEL_MAPPING_FAILED: " + c.SELECTION_INVARIANT[0]: "selection-noop-invariant",
    "x " + c.GENERATION_NOOP[0] + "no-op candidate.": "generation-noop",
    "RBWP7_RUNNER_PROTOCOL_ERROR at $runner: SCHEMA_VALIDATION_FAILED: " + c.WINDOW_WALL[0]: "window-wall",
    "something else": "other",
}
for text, expected in cases.items():
    got = c.classify_text(text)
    check(f"label {expected} (got {got})", got == expected)

check("citation noop", c.citation_of(prefix + noop_cite + c.BUDGET[0]) == "noop")
check("citation first", c.citation_of(prefix + first_cite + c.BUDGET[0]) == "first")
check("citation none", c.citation_of(prefix + c.NOOP_REJECTED[0] + c.BUDGET[0]) is None)
check("binary commitment", c.is_commitment_infeasible("commitment-all-rejected/budget"))
check("binary non-commitment all-rejected",
      not c.is_commitment_infeasible("all-rejected/non-commitment"))
check("binary window-wall", not c.is_commitment_infeasible("window-wall"))
check("binary non-commitment no-op", not c.is_commitment_infeasible("noop-rejected/non-commitment"))

# 3. Real artifacts from earlier runs classify as their recorded class.
real = {
    "E:/RideBoundData/wp14/drift-frac-v1/df-visible-k05-d20181114-s10-r1-s7": "commitment-all-rejected/budget",
    "E:/RideBoundData/wp14/drift-frac-v1/df-conduct-k05-d20181114-s10-r4-s7": "window-wall",
    "E:/RideBoundData/wp14/drift-v1/dr-conduct-k0-d20181114-s10-r1-s7": "completed",
}
for path, expected in real.items():
    got = c.classify_output(Path(path))
    check(f"real {Path(path).name}: {expected} (got {got})", got == expected)

with tempfile.TemporaryDirectory() as tmp:
    root = Path(tmp)
    check("no artifact", c.classify_output(root) == "no-artifact")
    (root / "failure-00.json").write_text(json.dumps({"failureMessage": "boom"}), encoding="utf-8")
    check("other from artifact", c.classify_output(root) == "other")

print(f"{len(failures)} failure(s)")
raise SystemExit(1 if failures else 0)
