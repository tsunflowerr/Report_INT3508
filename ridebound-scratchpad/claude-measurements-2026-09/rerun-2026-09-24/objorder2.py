"""Lexicographic objective levels actually used, per arm, over all cells.

Extends objorder.py (which read one C1 cell) to every cell of an arm, and adds
the number of DISTINCT incumbent values per objective, so "this level is
constant" can be read off directly instead of inferred from a nonzero count.

Read-only. Usage: objorder2.py <root> <substring-of-cell-dir> [<label>]
"""
import base64
import collections
import json
import os
import sys

root, tag = sys.argv[1], sys.argv[2]
label = sys.argv[3] if len(sys.argv) > 3 else tag
cells = sorted(d for d in os.listdir(root)
               if tag in d and os.path.exists(os.path.join(root, d, "transcript-00.ndjson")))
levels = collections.defaultdict(collections.Counter)
count = collections.Counter()
nonzero = collections.Counter()
values = collections.defaultdict(set)
decisions = 0
for cell in cells:
    with open(os.path.join(root, cell, "transcript-00.ndjson"), encoding="utf-8") as h:
        for line in h:
            frame = json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
            if frame.get("messageType") != "decision":
                continue
            evidence = frame["payload"].get("solver", {}).get("executionEvidence", {})
            bounds = (evidence.get("selection", {}).get("finalSolverDiagnostics", {})
                      .get("objectiveBounds", []))
            if not bounds:
                continue
            decisions += 1
            for bound in bounds:
                name = bound["objectiveName"]
                family = name.split(":")[0] if not name.startswith(("revision:", "warning-excess:")) else name
                levels[family][bound["levelIndex"]] += 1
                count[family] += 1
                value = bound.get("incumbentValue", 0)
                values[family].add(value)
                if value != 0:
                    nonzero[family] += 1

print(f"[{label}] cells={len(cells)} decisions-with-objectiveBounds={decisions}")
print(f"{'objective':<44}{'level':>9}{'count':>8}{'nonzero':>9}{'distinct':>9}  min..max")
for family in sorted(levels, key=lambda k: (min(levels[k]), k)):
    ls = sorted(levels[family])
    span = f"{ls[0]}" if ls[0] == ls[-1] else f"{ls[0]}..{ls[-1]}"
    vs = values[family]
    print(f"{family:<44}{span:>9}{count[family]:>8}{nonzero[family]:>9}{len(vs):>9}  "
          f"{min(vs)}..{max(vs)}")
