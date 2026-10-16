"""Compare the v1.3 forecast-OFF control run with task B's v1.2 run of the same job (C-30, d20181112-s10-r1-w07).
Equal means: same acknowledged fleet decisions in order WITH their simulation times, same signed v/e/p audit table
(every promise revision of every rider), same served count and same frame count. Also prints, for the forecast-ON
smoke run, the decision count, served count, how many decisions differ from v1.2, and the [forecast] log lines.
Usage: python -B compare_v13_control.py <out-file>   (mode "x")
"""
from __future__ import annotations

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
TANG3 = HERE.parent / "tang3"
for sub in ("pilot", "evidence", "w07"):
    sys.path.insert(0, str(TANG3 / sub))
import audit_vep  # noqa: E402
import run_w07  # noqa: E402
from pilot_analyze import fleet_decisions  # noqa: E402

BASE = run_w07.OUT_ROOT / "C-30-d20181112-s10-r1-w07"
CHECKS = pathlib.Path(r"C:/RideBoundData/research/tier3-forecast-checks-v1")


def facts(run: pathlib.Path):
    transcript = run / "transcript-00.ndjson"
    table, summary = audit_vep.audit(transcript)
    frames = sum(1 for _ in transcript.open(encoding="utf-8"))
    status = json.loads((run / "summary.json").read_text(encoding="utf-8")).get("status")
    return {"status": status, "decisions": fleet_decisions(transcript), "table": table,
            "served": summary["lifecycle"].get("completed", 0), "frames": frames, "sumDropV": summary["sumDropV"]}


def main(out: str) -> int:
    base, control, smoke = facts(BASE), facts(CHECKS / "control-off"), facts(CHECKS / "smoke-k2")
    lines = ["# compare_v13_control.py"]
    same = {
        "status pass": control["status"] == "pass",
        "fleet decisions with times identical": control["decisions"] == base["decisions"],
        "signed v/e/p audit table identical": control["table"] == base["table"],
        "served identical": control["served"] == base["served"],
        "frame count identical": control["frames"] == base["frames"],
    }
    lines.append(f"control-off vs v1.2 task B: " + "; ".join(f"{k}: {v}" for k, v in same.items()))
    lines.append(f"  decisions {len(control['decisions'])} vs {len(base['decisions'])}; served {control['served']} vs {base['served']}; "
                 f"frames {control['frames']} vs {base['frames']}")
    diff = sum(1 for a, b in zip(smoke["decisions"], base["decisions"]) if a[1] != b[1])
    lines.append(f"smoke-k2: status {smoke['status']}; decisions {len(smoke['decisions'])}; served {smoke['served']} "
                 f"(v1.2 {base['served']}); decision digests differing at the same position: {diff}; "
                 f"sum drop V {smoke['sumDropV'] / 1000:.1f} s (v1.2 {base['sumDropV'] / 1000:.1f} s)")
    log = (HERE / "checks-logs" / "smoke-k2.log").read_text(encoding="utf-8", errors="replace").splitlines()
    lines += ["  smoke [forecast] lines:"] + ["    " + l for l in log if l.startswith("[forecast]")][:20]
    clog = (HERE / "checks-logs" / "control-off.log").read_text(encoding="utf-8", errors="replace").splitlines()
    lines += ["  control [world]/[forecast] lines:"] + ["    " + l for l in clog if l.startswith(("[world] version", "[world] measured", "[forecast]"))]
    text = "\n".join(lines) + "\n"
    with open(out, "x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    sys.stdout.write(text)
    return 0 if all(same.values()) else 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    raise SystemExit(main(sys.argv[1]))
