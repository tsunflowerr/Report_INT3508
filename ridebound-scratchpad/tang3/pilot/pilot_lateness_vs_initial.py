"""How late, relative to the FIRST promise, did published drop times get in each pilot episode (read-only)?

Schulz & Pfeiffer (2026) set a deadline = first promised drop time + L (default L = 15 min) and require every
later plan to keep the drop no later than it. If, in an episode of arm U (no research gate), every published drop
promise stayed within first promise + L, then U's chosen candidate always satisfies that deadline; with the same
objective and tie-break, an M⁺ arm with slack L would then choose exactly as U (a prediction, not a run).
Per job: max over riders of max(p - p_first) on drop publications, and the number of riders above 60/300/900 s.
Usage: python -B pilot_lateness_vs_initial.py <arm> [<arm> ...]
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "evidence"))
import audit_vep  # noqa: E402
from run_pilot import CELLS, OUT_ROOT, WORLD_IDS  # noqa: E402

for arm in sys.argv[1:]:
    for cell in CELLS:
        for world in WORLD_IDS:
            name = f"{arm}-{world}-{cell}"
            table, _ = audit_vep.audit(OUT_ROOT / name / "transcript-00.ndjson")
            first, late = {}, {}
            for request, coordinate, _, kind, _, _, _, p, _, _, _, _ in table:
                if coordinate != "drop":
                    continue
                if kind == "initialPromise":
                    first[request] = p
                    late.setdefault(request, 0)
                else:
                    late[request] = max(late.get(request, 0), p - first[request])
            worst = max(late.values(), default=0)
            counts = [sum(1 for v in late.values() if v > limit * 1000) for limit in (60, 300, 900)]
            print(f"{name:<32} maxLateVsFirst={worst / 1000:7.1f}s  riders>60s={counts[0]:>3} "
                  f">300s={counts[1]:>3} >900s={counts[2]:>3}", flush=True)
