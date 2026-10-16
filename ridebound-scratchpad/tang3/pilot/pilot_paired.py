"""T3.7: C-30 vs V-30 visible drift on the riders BOTH arms promised (removes the "who is served" selection).

E2 compares shares over each arm's own promised riders, so an arm that serves fewer riders can look better only
because the riders it did not serve were the ones that would have drifted. Here, per (world, cell), riders are
matched by requestId (both arms see the same demand), and for the common riders the per-rider drop V (sum of |z|
over drop revisions) is compared. Row sums are cross-checked against the oracle's sumDropV.
Usage: python -B pilot_paired.py <output.tsv>   (created with mode "x")
"""
from __future__ import annotations

import sys

import audit_vep
from run_pilot import CELLS, OUT_ROOT, WORLD_IDS

LIMIT = audit_vep.E2_THRESHOLD_MS


def rider_v(name):
    table, summary = audit_vep.audit(OUT_ROOT / name / "transcript-00.ndjson")
    values = {}
    for request, coordinate, _, kind, _, _, _, _, _, _, z, closed in table:
        if coordinate != "drop":
            continue
        values.setdefault(request, 0)
        if kind != "initialPromise" and not closed:
            values[request] += abs(z)
    if sum(values.values()) != summary["sumDropV"] or len(values) != summary["promisedRiders"]:
        raise SystemExit(f"{name}: per-rider V does not match the oracle totals")
    return values


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    columns = ["world", "cell", "promisedC", "promisedV", "common", "onlyC", "onlyV",
               "commonAbove60C", "commonAbove60V", "onlyCAbove60", "onlyVAbove60"]
    with open(sys.argv[1], "x", encoding="utf-8", newline="\n") as out:
        out.write("\t".join(columns) + "\n")
        for cell in CELLS:
            for world in WORLD_IDS:
                c = rider_v(f"C-30-{world}-{cell}")
                v = rider_v(f"V-30-{world}-{cell}")
                common = set(c) & set(v)
                only_c, only_v = set(c) - set(v), set(v) - set(c)
                row = {
                    "world": world, "cell": cell, "promisedC": len(c), "promisedV": len(v),
                    "common": len(common), "onlyC": len(only_c), "onlyV": len(only_v),
                    "commonAbove60C": sum(1 for r in common if c[r] > LIMIT),
                    "commonAbove60V": sum(1 for r in common if v[r] > LIMIT),
                    "onlyCAbove60": sum(1 for r in only_c if c[r] > LIMIT),
                    "onlyVAbove60": sum(1 for r in only_v if v[r] > LIMIT),
                }
                out.write("\t".join(str(row[k]) for k in columns) + "\n")
                out.flush()
                print("  ".join(f"{k}={row[k]}" for k in columns), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
