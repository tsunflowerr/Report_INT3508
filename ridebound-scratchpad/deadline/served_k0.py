"""Served requests at k = 0 on panel A: deadline arms vs the conduct control. Read-only."""
import run_deadline as rd
from compare_controls import accepted

rows = {}
for arm, prefix in (("conduct-30 (ctl)", "ctl-conduct-k0"), ("dl-30", "dl-30-k0"),
                    ("dl-60", "dl-60-k0"), ("dl-120", "dl-120-k0")):
    values = [accepted(rd.effective_output(f"{prefix}-{cell}-s7")) for cell in rd.PANEL_A["cells"]]
    rows[arm] = values
    done = [v for v in values if v is not None]
    print(f"{arm:<18} completed {len(done)}/20  total accepted {sum(done)}")
base = rows["conduct-30 (ctl)"]
for arm in ("dl-30", "dl-60", "dl-120"):
    diff = [a - b for a, b in zip(rows[arm], base) if a is not None and b is not None]
    print(f"{arm} - conduct per cell: more {sum(d > 0 for d in diff)}, equal {sum(d == 0 for d in diff)}, "
          f"fewer {sum(d < 0 for d in diff)}, total {sum(diff):+d}")
