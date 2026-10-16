"""Stamp an amendment: SHA-256 of the given files and the UTC time, into amendment-<id>.sha256.

Refuses to overwrite. Also records which rerun outputs exist (must be none when stamping A2).
Usage: stamp_amendment.py <id> <file> [...]
"""
import datetime
import hashlib
import sys
from pathlib import Path

import run_deadline as rd

amendment, files = sys.argv[1], sys.argv[2:]
reruns = sorted(d.name for d in rd.OUT_ROOT.iterdir() if "-rerun" in d.name)
stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
lines = [f"# amendment {amendment} stamped {stamp}; rerun outputs present: {len(reruns)} {reruns}"]
lines += [f"{hashlib.sha256(Path(rd.HERE / f).read_bytes()).hexdigest()}  {f}" for f in files]
with open(rd.HERE / f"amendment-{amendment}.sha256", "x", encoding="utf-8", newline="\n") as handle:
    handle.write("\n".join(lines) + "\n")
print("\n".join(lines))
