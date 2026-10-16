"""Task B, descriptive diagnostic of the one Q4 failure (written after the full analysis, 2026-09-30).

For d20181113-s10-r1-w07 and arms C-30, C-300, Mplus-300: the riders with A = actual drop - first promised drop
> 60 s, with A split into the sum of signed exogenous changes x (e - v) and of signed dispatch changes c (p - e)
over the rider's drop revisions (audit_vep rows), plus the final correction (actual - last promise).
Usage: python -B w07_q4_rider.py <new-log>   (mode "x")
"""
from __future__ import annotations

import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
for sub in ("sweep", "evidence"):
    sys.path.insert(0, str(HERE.parent / sub))
import audit_vep  # noqa: E402
import run_w07  # noqa: E402
from sweep_analyze import event_times  # noqa: E402

CELL = "d20181113-s10-r1-w07"


def main(log_path: str) -> int:
    lines = [f"# w07_q4_rider.py (descriptive, after the analysis); cell {CELL}"]
    for arm in ("C-30", "C-300", "Mplus-300"):
        transcript = run_w07.OUT_ROOT / f"{arm}-{CELL}" / "transcript-00.ndjson"
        table, _ = audit_vep.audit(transcript)
        first, last, sx, sc = {}, {}, {}, {}
        for request, coordinate, _, kind, _, _, _, p, x, c, _, closed in table:
            if coordinate != "drop":
                continue
            if kind == "initialPromise":
                first[request] = p
                sx[request] = sc[request] = 0
            elif not closed:
                sx[request] += x
                sc[request] += c
            last[request] = p
        _, alighted = event_times(transcript)
        late = sorted(((alighted[r] - first[r], r) for r in first if r in alighted and alighted[r] - first[r] > 60000),
                      reverse=True)
        lines.append(f"{arm}: riders with A > 60 s: {len(late)}")
        for a, r in late[:5]:
            lines.append(f"  {r[:14]}  A {a / 1000:7.1f} s = sum x {sx[r] / 1000:7.1f} + sum c {sc[r] / 1000:7.1f} "
                         f"+ final correction {(alighted[r] - last[r]) / 1000:6.1f} s")
    text = "\n".join(lines) + "\n"
    with open(log_path, "x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    raise SystemExit(main(sys.argv[1]))
