"""Seal the Tier-2 preregistration: SHA-256 of the preregistration, predictions and code, with UTC.

Refuses to run if any output of a predicted arm already exists, and never overwrites the seal.
"""
import datetime
import hashlib
from pathlib import Path

import run_deadline as rd

FILES = ["PREREGISTRATION.md", "predictions.csv", "run_deadline.py", "classify.py",
         "holdout_predict.py", "analyze.py", "figure_families.py", "test_classify.py",
         "test_predict.py", "preflight_drift_v2.py"]

present = [d.name for d in rd.OUT_ROOT.iterdir()
           if d.name.startswith(("dl-", "dl2-", "visible-30-"))]
if present:
    raise SystemExit(f"refusing to seal: predicted-arm outputs exist: {present[:5]}")
stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
lines = [f"# sealed {stamp} UTC; predicted-arm outputs present at sealing: 0"]
for name in FILES:
    lines.append(f"{hashlib.sha256(Path(rd.HERE / name).read_bytes()).hexdigest()}  {name}")
with open(rd.HERE / "PREREGISTRATION.sha256", "x", encoding="utf-8", newline="\n") as handle:
    handle.write("\n".join(lines) + "\n")
print("\n".join(lines))
