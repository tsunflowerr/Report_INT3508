"""T3.8/T3.9 split of the 49 panel A episodes into calibration and test (T38-PLAN.md §2). Run once, before any job.

Unit of the split: the (day, sample) group, not the single cell. The three windows of one (day, sample) are drawn from
the same demand file and share selected source rows (prepare-2026-10-01.log: 3-20 of 108 rows shared between w07 and
w08), so splitting a group across calibration and test would put the same riders on both sides.
Rule, fixed before any simulation on these cells:
  * group d20181114-s10-r1 goes to calibration (its w08 cell was seen in the Tier 3 smoke runs T3.5/T3.6);
  * then, for each day 14..18/11, one more group is drawn for calibration from that day's remaining groups with
    random.Random(SEED).sample over the sorted group names, days in order;
  * every other group is test.
This gives 6 calibration groups (one per day, two on 14/11) and 14 test groups. No outcome of any run is used.
Usage: python -B make_split_t38.py <new-manifest.json> <new-log>   (both mode "x")
"""
from __future__ import annotations

import hashlib
import json
import pathlib
import random
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "calib" / "panelA"))
import prepare_panelA  # noqa: E402  (constants only: DAYS, WINDOWS, DROPPED, cells())

SEED = 20261001
FORCED_CALIBRATION = "d20181114-s10-r1"


def main(manifest_path: str, log_path: str) -> int:
    episodes = [f"{base}-{window}" for base, window in prepare_panelA.cells()]
    groups: dict[str, list[str]] = {}
    for episode in episodes:
        groups.setdefault(episode[:16], []).append(episode)
    rng = random.Random(SEED)
    calibration_groups = [FORCED_CALIBRATION]
    for day in prepare_panelA.DAYS:
        candidates = sorted(g for g in groups if g[7:9] == day and g not in calibration_groups)
        calibration_groups += rng.sample(candidates, 1)
    calibration = sorted(e for g in calibration_groups for e in groups[g])
    test = sorted(e for e in episodes if e not in calibration)
    manifest = {
        "splitId": "tier3-t38-split-v1",
        "seed": SEED,
        "unit": "(day, sample) group",
        "forcedCalibrationGroup": FORCED_CALIBRATION,
        "calibrationGroups": sorted(calibration_groups),
        "calibration": calibration,
        "test": test,
    }
    text = json.dumps(manifest, indent=2) + "\n"
    with open(manifest_path, "x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    lines = [f"# make_split_t38.py seed {SEED}; {len(episodes)} episodes in {len(groups)} groups",
             f"calibration groups: {sorted(calibration_groups)}",
             f"calibration episodes: {len(calibration)}; test episodes: {len(test)}"]
    for label, part in (("calibration", calibration), ("test", test)):
        for window in prepare_panelA.WINDOWS:
            lines.append(f"  {label} {window}: {sum(1 for e in part if e.endswith(window))}")
        for day in prepare_panelA.DAYS:
            lines.append(f"  {label} 201811{day}: {sum(1 for e in part if e[7:9] == day)}")
    shared = {e[:16] for e in calibration} & {e[:16] for e in test}
    lines.append(f"groups on both sides: {sorted(shared) or 'none'}")
    lines.append(f"manifest sha256 {hashlib.sha256(text.encode('utf-8')).hexdigest()}")
    out = "\n".join(lines) + "\n"
    with open(log_path, "x", encoding="utf-8", newline="\n") as handle:
        handle.write(out)
    sys.stdout.write(out)
    return 1 if shared or len(calibration) + len(test) != 49 else 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    raise SystemExit(main(sys.argv[1], sys.argv[2]))
