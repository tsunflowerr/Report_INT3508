"""Task B preparation, after the normalizer wrote the w07 fixtures into C:/Code/RideBound-noworse (read-only there).

1. Check every generated cell: 108 requests, 8 vehicles, 96 nodes, 9120 arcs, normalizerSourceSha256 34517a83...,
   local window start 07:00 on the cell's day, scenarioId as in grid-w07-v1.json, selected rows = 108.
2. Copy each fixture directory to FIXTURE_ROOT (outside every repository); never overwrite.
3. Write one driver per cell from the w08 driver of the same (day, sample): only scenarioId,
   sourceScenarioContentSha256 (SHA-256 of scenario-content.json) and sourceScenarioHash (report scenarioHash) change.
4. Overlap with the w08 cells already analysed: selected source-row ordinals (selection-frame.json) of w07 and w08
   for the same (day, sample), both from the same demand file.
Usage: python -B prepare_w07.py <new-log>   (mode "x"; also refuses to overwrite fixtures or drivers)
"""
from __future__ import annotations

import hashlib
import json
import pathlib
import shutil
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "world"))
import preflight_world_v1_2 as v12  # noqa: E402
import run_w07  # noqa: E402

SOURCE = pathlib.Path(r"C:/Code/RideBound-noworse/benchmarks/fixtures/wp6/public/fleetpy-manhattan-v1")
GRID = json.loads((HERE / "grid-w07-v1.json").read_text(encoding="utf-8"))
W08_FIXTURES = SOURCE / "wp14-development-panel-v1"
W08_DRIVERS = pathlib.Path(r"C:/Code/RideBound-noworse/benchmarks/scenarios/wp14-development")
NORMALIZER_SOURCE = "34517a832014c78a572282e01795fc243896db088249fd6dade70beed2aa4d90"


def selected(frame: pathlib.Path) -> set[int]:
    return {row["sourceRecordOrdinal"] for row in json.loads(frame.read_text(encoding="utf-8"))
            if row["disposition"] == "selected"}


def main(log_path: str) -> int:
    lines, problems = [], []
    out = lines.append
    cells = {cell["cellId"]: cell for cell in GRID["cells"]}
    for cell_id in run_w07.CELLS:
        cell = cells[cell_id]
        generated = SOURCE / GRID["gridId"] / cell_id
        scenario_path = generated / "scenario-content.json"
        scenario = json.loads(scenario_path.read_text(encoding="utf-8"))
        report = json.loads((generated / "normalization-report.json").read_text(encoding="utf-8"))
        summary = scenario["validationSummary"]
        day, start = v12.scenario_window(scenario_path)
        facts = {"requests": summary["requestCount"], "vehicles": summary["vehicleCount"], "nodes": summary["nodeCount"],
                 "arcs": summary["directedArcCount"], "selected": report["selectedRecordCount"],
                 "eligible": report["eligibleRecordCount"], "normalizerSource": scenario["normalizerSourceSha256"],
                 "scenarioId": scenario["scenarioId"], "localDay": day, "localStart": start}
        expected = {"requests": 108, "vehicles": 8, "nodes": 96, "arcs": 9120, "selected": 108,
                    "normalizerSource": NORMALIZER_SOURCE, "scenarioId": cell["scenarioId"],
                    "localDay": cell["sourceLocalDate"], "localStart": 25200}
        for key, value in expected.items():
            if facts[key] != value:
                problems.append(f"{cell_id}: {key} = {facts[key]!r}, expected {value!r}")
        content_sha = hashlib.sha256(scenario_path.read_bytes()).hexdigest()
        if report["scenarioContentSha256"] != content_sha:
            problems.append(f"{cell_id}: report scenarioContentSha256 differs from the file")
        out(f"{cell_id}: {facts} scenarioContentSha256={content_sha} scenarioHash={report['scenarioHash']}")

        target = run_w07.FIXTURE_ROOT / cell_id
        if target.exists():
            problems.append(f"{cell_id}: fixture copy already exists at {target}; not overwritten")
        else:
            shutil.copytree(generated, target)
            for path in sorted(generated.iterdir()):
                if hashlib.sha256(path.read_bytes()).digest() != hashlib.sha256((target / path.name).read_bytes()).digest():
                    problems.append(f"{cell_id}: copy of {path.name} differs")
        template = json.loads((W08_DRIVERS / f"{cell_id.replace('-w07', '-w08')}.driver.json").read_text(encoding="utf-8"))
        driver = dict(template, scenarioId=cell["scenarioId"], sourceScenarioContentSha256=content_sha,
                      sourceScenarioHash=report["scenarioHash"])
        changed = sorted(k for k in driver if driver[k] != template[k])
        if changed != ["scenarioId", "sourceScenarioContentSha256", "sourceScenarioHash"]:
            problems.append(f"{cell_id}: driver changes {changed}")
        run_w07.DRIVER_ROOT.mkdir(parents=True, exist_ok=True)
        with open(run_w07.DRIVER_ROOT / f"{cell_id}.driver.json", "x", encoding="utf-8", newline="\n") as handle:
            json.dump(driver, handle, indent=2)
            handle.write("\n")

        w07_rows = selected(generated / "selection-frame.json")
        w08_rows = selected(W08_FIXTURES / cell_id.replace("-w07", "-w08") / "selection-frame.json")
        same_demand = cell["demandMemberPath"] == json.loads(
            (W08_FIXTURES / cell_id.replace("-w07", "-w08") / "normalizer-configuration.json").read_text(
                encoding="utf-8"))["demandMemberPath"]
        out(f"    overlap with {cell_id.replace('-w07', '-w08')} (same demand file: {same_demand}): "
            f"{len(w07_rows & w08_rows)} of 108 selected source rows are in both cells")
    out(f"problems: {len(problems)}")
    for problem in problems:
        out("  " + problem)
    text = "\n".join(lines) + "\n"
    with open(log_path, "x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    sys.stdout.write(text)
    return 1 if problems else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    raise SystemExit(main(sys.argv[1]))
