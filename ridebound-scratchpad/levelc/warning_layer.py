"""Was the warning layer ever in a position to decide anything?

Level C inserts a warning-excess layer into the lexicographic objective of the
fleet-wide set packing:

    worst-hard-utilization  >  warning-excess  >  revision  >  cost

Measured outcome: every decision on every finished cell is identical to the
control -- same plans, same promises, same reason codes. The question is why.

Two distinct ways a lexicographic layer can be inert:

  (a) its value is identically zero, so it never distinguishes anything;
  (b) its value varies, but a HIGHER layer already settles every comparison, so
      the lower layer never gets a say.

The distinction matters for the report. (a) says the 60 s warning threshold is
simply never reached under a 120 s cap. (b) says the threshold is reached but
worst-hard-utilization -- which both arms minimise first -- has already picked
the winner.

The solver records its lexicographic stack per decision in
selection/finalSolverDiagnostics/objectiveBounds. This reads the stack out of
both arms and reports, layer by layer, how often each one takes a non-zero
value and how often it is the first layer that is not already forced.

Read-only.
"""

from __future__ import annotations

import base64
import collections
import json
import pathlib

CONTROL = pathlib.Path(r"E:/RideBoundData/wp9/frontier-v1")
TREAT = pathlib.Path(r"E:/RideBoundData/wp14/levelc-v1")
CELLS = [
    "d201811{}-s10-r{}".format(day, rep)
    for day in (14, 15, 16, 17, 18)
    for rep in (1, 2, 3, 4)
]


def frames(path: pathlib.Path):
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                yield json.loads(base64.b64decode(json.loads(line)["frameBase64"]))


def bounds_of(frame):
    node = (frame.get("payload", {}).get("solver", {})
            .get("executionEvidence", {}).get("selection", {})
            .get("finalSolverDiagnostics", {}))
    return node.get("objectiveBounds") or []


def scan(directory: pathlib.Path) -> tuple[collections.Counter,
                                           collections.Counter,
                                           list[str]]:
    seen: collections.Counter = collections.Counter()
    nonzero: collections.Counter = collections.Counter()
    order: list[str] = []
    for frame in frames(directory / "transcript-00.ndjson"):
        if frame.get("messageType") != "decision":
            continue
        for position, bound in enumerate(bounds_of(frame)):
            name = bound.get("objectiveName") or "#{}".format(position)
            # the per-vehicle deterministic tiebreaker appears once per vehicle;
            # collapse it so it does not swamp the table
            if name.startswith("candidate-id-rank:"):
                name = "candidate-id-rank:<per-xe>"
            if name not in order:
                order.append(name)
            seen[name] += 1
            value = bound.get("incumbentValue")
            try:
                if value is not None and float(value) != 0.0:
                    nonzero[name] += 1
            except (TypeError, ValueError):
                pass
    return seen, nonzero, order


def report(label: str, root: pathlib.Path, pattern: str) -> None:
    seen: collections.Counter = collections.Counter()
    nonzero: collections.Counter = collections.Counter()
    order: list[str] = []
    cells = 0
    for cell in CELLS:
        directory = root / pattern.format(cell)
        if not (directory / "summary.json").exists():
            continue
        cells += 1
        a, b, o = scan(directory)
        seen.update(a)
        nonzero.update(b)
        for name in o:
            if name not in order:
                order.append(name)
    print("=== {} -- {} o ===".format(label, cells))
    if not order:
        print("  khong doc duoc tang muc tieu nao")
        print()
        return
    print("  {:<34}{:>12}{:>12}{:>10}".format(
        "tang muc tieu", "so lan", "khac 0", "ti le"))
    for name in order:
        total = seen[name]
        share = 100.0 * nonzero[name] / total if total else 0.0
        print("  {:<34}{:>12,}{:>12,}{:>9.2f}%".format(
            str(name)[:34], total, nonzero[name], share))
    print()


def main() -> int:
    print("TANG MUC TIEU CUA BAI TOAN DONG GOI TAP HOP, DOC TU BANG CHUNG SOLVER")
    print()
    report("doi chung (vector cung, tran 120 s)", CONTROL, "fr-budget120-{}-s7")
    report("muc C (soft-hybrid, canh bao 60 s)", TREAT, "lc-{}-s7")
    print("Neu tang 'warning-excess' luon bang 0 -> nguong 60 s khong bao gio bi")
    print("cham duoi tran 120 s, tang canh bao rong theo nghia (a).")
    print("Neu no khac 0 nhung ket qua van trung khop -> tang cao hon da quyet")
    print("xong truoc, tuc rong theo nghia (b).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
