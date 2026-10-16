"""Snowstorm cells (15/11 14:00-16:00 'w14' and 15:00-17:00 'w15', samples r1..r4; grid tier3-snow-v1): copy the
fixtures written by normalize_snow.py to C:/RideBoundData/research/fixtures-snow-v1 and write drivers (the 08:00-10:00
panel A driver of the same day and sample with scenarioId and the two scenario hashes replaced). Same checks as
../../tang3/calib/panelA/prepare_panelA.py (derived from it). Never overwrites.
Usage: python -B prepare_snow.py <new-log>
"""
from __future__ import annotations

import hashlib
import json
import pathlib
import shutil
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tang3" / "world"))
import preflight_world_v1_2 as v12  # noqa: E402

REPO = pathlib.Path(r"C:/Code/RideBound-noworse")
FIXTURES = REPO / "benchmarks/fixtures/wp6/public/fleetpy-manhattan-v1"
W08_FIXTURES = FIXTURES / "wp9-confirmatory-fixed-panel-v2"
W08_DRIVERS = REPO / "benchmarks/scenarios/wp9-confirmatory"
GRID = json.loads((HERE / "grid-snow-v1.json").read_text(encoding="utf-8"))
NEW_FIXTURES = FIXTURES / GRID["gridId"]
FIXTURE_ROOT = pathlib.Path(r"C:/RideBoundData/research/fixtures-snow-v1")
DRIVER_ROOT = HERE / "drivers"
NORMALIZER_SOURCE = "34517a832014c78a572282e01795fc243896db088249fd6dade70beed2aa4d90"
DAYS = ("15",)
WINDOWS = {"w14": 50400, "w15": 54000}
DROPPED = frozenset()


def cells():
    for day in DAYS:
        for r in (1, 2, 3, 4):
            for window in WINDOWS:
                if f"d201811{day}-s10-r{r}-{window}" not in DROPPED:
                    yield f"d201811{day}-s10-r{r}", window


def selected(frame: pathlib.Path) -> set[int]:
    return {row["sourceRecordOrdinal"] for row in json.loads(frame.read_text(encoding="utf-8")) if row["disposition"] == "selected"}


def main(log_path: str) -> int:
    lines, problems = [], []
    grid = {c["cellId"]: c for c in GRID["cells"]}
    DRIVER_ROOT.mkdir(exist_ok=True)
    for cell_id in sorted(DROPPED):
        if (NEW_FIXTURES / cell_id).exists():
            problems.append(f"{cell_id}: listed as dropped but its fixture folder exists")
    built = sorted(path.name for path in NEW_FIXTURES.iterdir() if path.is_dir())
    expected_built = sorted(f"{b}-{w}" for b, w in cells())
    if built != expected_built:
        problems.append(f"fixture folders {built} differ from the expected {expected_built}")
    rows_by_base = {}
    for base, window in cells():
        cell_id = f"{base}-{window}"
        source = NEW_FIXTURES / cell_id
        scenario_path = source / "scenario-content.json"
        scenario = json.loads(scenario_path.read_text(encoding="utf-8"))
        report = json.loads((source / "normalization-report.json").read_text(encoding="utf-8"))
        summary = scenario["validationSummary"]
        day, start = v12.scenario_window(scenario_path)
        content_sha = hashlib.sha256(scenario_path.read_bytes()).hexdigest()
        template_path = W08_DRIVERS / f"{base}.driver.json"
        template = json.loads(template_path.read_text(encoding="utf-8"))
        expected_id = grid[cell_id]["scenarioId"]
        facts = {"requests": summary["requestCount"], "vehicles": summary["vehicleCount"], "nodes": summary["nodeCount"],
                 "arcs": summary["directedArcCount"], "selected": report["selectedRecordCount"],
                 "normalizerSource": scenario["normalizerSourceSha256"], "scenarioId": scenario["scenarioId"],
                 "day": day, "start": start}
        expected = {"requests": 108, "vehicles": 8, "nodes": 96, "arcs": 9120, "selected": 108,
                    "normalizerSource": NORMALIZER_SOURCE, "scenarioId": expected_id,
                    "day": f"2018-11-{base[7:9]}", "start": WINDOWS[window]}
        for key, value in expected.items():
            if facts[key] != value:
                problems.append(f"{cell_id}: {key} = {facts[key]!r}, expected {value!r}")
        if report["scenarioContentSha256"] != content_sha:
            problems.append(f"{cell_id}: report scenarioContentSha256 differs from the file")
        if True:
            driver = dict(template, scenarioId=expected_id, sourceScenarioContentSha256=content_sha,
                          sourceScenarioHash=report["scenarioHash"])
            changed = sorted(k for k in driver if driver[k] != template[k])
            if changed != ["scenarioId", "sourceScenarioContentSha256", "sourceScenarioHash"]:
                problems.append(f"{cell_id}: driver changes {changed}")
        target = FIXTURE_ROOT / cell_id
        if target.exists():
            problems.append(f"{cell_id}: fixture copy exists at {target}; not overwritten")
        else:
            shutil.copytree(source, target)
            for path in sorted(source.iterdir()):
                if path.read_bytes() != (target / path.name).read_bytes():
                    problems.append(f"{cell_id}: copy of {path.name} differs")
        with open(DRIVER_ROOT / f"{cell_id}.driver.json", "x", encoding="utf-8", newline="\n") as handle:
            json.dump(driver, handle, indent=2)
            handle.write("\n")
        rows_by_base.setdefault(base, {})[window] = selected(source / "selection-frame.json")
        lines.append(f"{cell_id}: {facts} scenarioContentSha256={content_sha}")
    lines.append(f"episodes: {sum(len(rows) for rows in rows_by_base.values())}")
    lines.append(f"problems: {len(problems)}")
    lines.extend("  " + p for p in problems)
    text = "\n".join(lines) + "\n"
    with open(log_path, "x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    sys.stdout.write(text)
    return 1 if problems else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    raise SystemExit(main(sys.argv[1]))
