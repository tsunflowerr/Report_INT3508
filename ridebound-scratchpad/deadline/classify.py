"""Tier-2 outcome classifier (plan T2.7): exact message constants from the source code.

A run's outcome label has two parts: the failure PATH and the RULE that rejected the
safety no-op. "Commitment-infeasible" is exactly: label starts with "commitment-".
Never count failures without classifying them (trap 12.4).

Every constant below is asserted, by test_classify.py, to appear verbatim in the named
source file of the research worktree, so a changed message breaks the test instead of
silently changing a label.
"""
from __future__ import annotations

import json
from pathlib import Path

WORKTREE = Path(r"E:/Code/RideBound-deadline")

# (constant, source file relative to WORKTREE)
# The fail-closed message is "<ALL_REJECTED><citation>: <rejection>". The runner cites the
# no-op ("No-op rejection") when the vehicle has exactly one; the fallback, and every runner
# built before the diagnostic change, cites the ordinal-first candidate ("First rejection").
ALL_REJECTED = ("C1 rejected every generated candidate for this vehicle. ",
                "src/RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs")
CITE_NOOP = ("No-op rejection", "src/RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs")
CITE_FIRST = ("First rejection", "src/RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs")
NOOP_REJECTED = ("C1 rejected the safety no-op while other candidates survived. No-op rejection: ",
                 "src/RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs")
DEADLINE_LATE = ("The candidate delays the drop ETA beyond the initial-promise deadline.",
                 "src/RideBound.Application/Commitments/CommitmentDecisionValidator.cs")
DEADLINE_WINDOW = ("The candidate moves the drop ETA outside the initial-promise window.",
                   "src/RideBound.Application/Commitments/CommitmentDecisionValidator.cs")
BUDGET = ("The candidate exceeds a hard commitment dimension.",
          "src/RideBound.Application/Commitments/CommitmentDecisionValidator.cs")
PHASE_LOCK = ("The candidate changes a phase-locked promise field.",
              "src/RideBound.Application/Commitments/CommitmentDecisionValidator.cs")
GENERATION_NOOP = ("The active route could not be retained as the safety ",
                   "src/RideBound.Algorithms/Candidates/InsertionCandidateGenerator.cs")
WINDOW_WALL = ("Actual pickup time must remain inside the accepted pickup window.",
               "src/RideBound.Domain/Requests/RideRequest.cs")
SELECTION_INVARIANT = ("Each vehicle must have candidate options and exactly one no-op option.",
                       "src/RideBound.Application/Optimization/CandidateSelectionModel.cs")

CONSTANTS = [ALL_REJECTED, CITE_NOOP, CITE_FIRST, NOOP_REJECTED, DEADLINE_LATE,
             DEADLINE_WINDOW, BUDGET, PHASE_LOCK, GENERATION_NOOP, WINDOW_WALL,
             SELECTION_INVARIANT]

REASONS = [
    (DEADLINE_LATE[0], "deadline-late"),
    (DEADLINE_WINDOW[0], "deadline-window"),
    (BUDGET[0], "budget"),
    (PHASE_LOCK[0], "lock"),
]


def _reason(text: str, prefix: str) -> str | None:
    """The commitment rule named after `prefix`, or None if the reason is not a
    commitment rejection (e.g. a state-application or physical failure of the no-op)."""
    tail = text.split(prefix, 1)[1]
    for message, name in REASONS:
        if tail.startswith(message):
            return name
    return None


def citation_of(text: str) -> str | None:
    """'noop' or 'first' for a fail-closed message, else None. A 'first' citation names
    an arbitrary candidate's rejection, not necessarily the no-op's."""
    for cite, name in ((CITE_NOOP[0], "noop"), (CITE_FIRST[0], "first")):
        if ALL_REJECTED[0] + cite + ": " in text:
            return name
    return None


def classify_text(text: str) -> str:
    if ALL_REJECTED[0] in text:
        citation = citation_of(text)
        if citation is None:
            return "other"
        cite = CITE_NOOP[0] if citation == "noop" else CITE_FIRST[0]
        rule = _reason(text, ALL_REJECTED[0] + cite + ": ")
        # A cited rejection that is not a commitment rule (physical, projection, state)
        # is not commitment-infeasible.
        return f"commitment-all-rejected/{rule}" if rule else "all-rejected/non-commitment"
    if NOOP_REJECTED[0] in text:
        rule = _reason(text, NOOP_REJECTED[0])
        # A no-op rejected for a non-commitment reason is not commitment-infeasible.
        return f"commitment-noop-rejected/{rule}" if rule else "noop-rejected/non-commitment"
    if SELECTION_INVARIANT[0] in text:
        return "selection-noop-invariant"
    if GENERATION_NOOP[0] in text:
        return "generation-noop"
    if WINDOW_WALL[0] in text:
        return "window-wall"
    return "other"


def classify_output(output: Path) -> str:
    """Label one run directory: 'completed' when a summary exists, else the failure label."""
    if (output / "summary.json").exists():
        return "completed"
    failure = output / "failure-00.json"
    if not failure.exists():
        return "no-artifact"
    record = json.loads(failure.read_text(encoding="utf-8"))
    return classify_text(record.get("failureMessage", ""))


def is_commitment_infeasible(label: str) -> bool:
    return label.startswith("commitment-")
