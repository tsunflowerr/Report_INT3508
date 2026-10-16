"""Feasibility check (2026-10-06, exploratory, not a thesis result): can a rider's final drop lateness be attributed to
dispatch decisions vs traffic, the way paratransit contracts excuse "causes beyond the control of the entity"?

For each served rider: A = alight time - first promised drop ETA (p0). From the v/e/p audit (signed, drop coordinate,
revisions after the initial promise): S_c = sum (p - e) (dispatch-caused), S_x = sum (e - v) (route kept, i.e. traffic).
Identity to check: A = S_c + S_x + residual, residual = alight - last published drop ETA (execution error).
Prints, per run, the identity check and the late riders (A > 60 s) split into dispatch vs traffic, plus examples.
Usage: python -B contract_split_check.py <out-file> <run-name> [<run-name> ...]   (out-file mode "x")
"""
from __future__ import annotations

import pathlib
import sys

TANG3 = pathlib.Path(__file__).resolve().parents[1] / "tang3"
for sub in ("sweep", "evidence", "t38"):
    sys.path.insert(0, str(TANG3 / sub))

import audit_vep  # noqa: E402
import sweep_analyze  # noqa: E402

ROOT = pathlib.Path(r"C:/RideBoundData/research/tier3-t38-v1")


def riders(run: str):
    transcript = ROOT / run / "transcript-00.ndjson"
    table, _ = audit_vep.audit(transcript)
    _, alighted = sweep_analyze.event_times(transcript)
    first, last, sc, sx = {}, {}, {}, {}
    for request, coordinate, _, kind, _, v, e, p, _, _, _, _ in table:
        if coordinate != "drop":
            continue
        if kind == "initialPromise":
            first[request] = p
            sc[request] = sx[request] = 0
        else:
            sc[request] += p - e
            sx[request] += e - v
        last[request] = p
    out = []
    for r in first:
        if r in alighted:
            a = alighted[r] - first[r]
            out.append((r, a, sc[r], sx[r], alighted[r] - last[r]))
    return out


def main(out_file: str, runs: list[str]) -> int:
    lines = ["# contract_split_check.py (exploratory feasibility check, not a thesis result)"]
    for run in runs:
        rows = riders(run)
        bad = [r for r in rows if r[1] != r[2] + r[3] + r[4]]
        nonzero_resid = sum(1 for r in rows if r[4] != 0)
        late = [r for r in rows if r[1] > 60_000]
        dispatch_led = [r for r in late if r[2] > r[3]]
        late_without_dispatch = [r for r in late if r[1] - max(r[2], 0) > 60_000]
        lines.append(f"\n{run}: served {len(rows)}; identity A = Sc + Sx + residual fails for {len(bad)}; "
                     f"riders with residual != 0: {nonzero_resid}")
        lines.append(f"  late > 60 s: {len(late)}; of these, dispatch part larger than traffic part: {len(dispatch_led)}; "
                     f"still late > 60 s after removing the dispatch part: {len(late_without_dispatch)}")
        lines.append(f"  sum over late riders: dispatch {sum(r[2] for r in late) / 1000:.1f} s, traffic {sum(r[3] for r in late) / 1000:.1f} s")
        for r in sorted(late, key=lambda r: -r[1])[:4]:
            lines.append(f"    {r[0][:14]}: late {r[1] / 1000:.1f} s = dispatch {r[2] / 1000:+.1f} s + traffic {r[3] / 1000:+.1f} s"
                         f" + execution {r[4] / 1000:+.1f} s")
    text = "\n".join(lines) + "\n"
    with open(out_file, "x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    raise SystemExit(main(sys.argv[1], sys.argv[2:]))
