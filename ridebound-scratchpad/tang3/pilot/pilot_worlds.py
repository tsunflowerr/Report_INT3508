"""T3.7 check 1 (world validity), read-only on the pilot job logs.

Per job: return code 0; the `[world] config=` sha256 equals the world file on disk; bins are 0..k in order
with no gap; bin 0 has factor [1, 1] (anchored world); "bin changes applied" equals the number of bin lines.
Per (world, cell): on the bins every arm reached, every arm saw the same bin -> factor-range sequence (the
world must not depend on the arm). Arms may reach a different LAST bin, because the episode ends when the last
vehicle finishes; that is reported, not hidden.

Switch timing (found in this pilot): preflight_world.py applies a new bin at the first `_trigger_and_resolve`
at or after the bin start. The medium preflight's event clock triggers at request arrivals, vehicle physical
boundaries (arm dependent) and drain timers, so the switch lags the nominal start `bin * 900 s` and the lag can
differ between arms. Reported per bin: max lag over arms and the spread of the switch time across arms.
Usage: python -B pilot_worlds.py [arm ...]   (default: every arm)
"""
import hashlib
import pathlib
import re
import sys

from run_pilot import ARMS, CELLS, HERE, WORLD_IDS, world_file

sys.path.insert(0, str(HERE.parent / "world"))
from world_v1 import BIN_S  # noqa: E402

LOGS = HERE / "logs"
CONFIG = re.compile(r"^\[world\] config=(?P<path>.+?) sha256=(?P<sha>[0-9a-f]{64}) seed=(?P<seed>\d+)$")
BIN = re.compile(r"^\[world\] t=\s*(?P<t>\d+)s bin=(?P<bin>\d+) edges=(?P<edges>\d+) "
                 r"factor=\[(?P<lo>[\d.]+), (?P<hi>[\d.]+)\]$")
APPLIED = re.compile(r"^\[world\] bin changes applied: (?P<n>\d+)$")


def parse(log: pathlib.Path):
    lines = log.read_text(encoding="utf-8", errors="replace").splitlines()
    out = {"returncode": None, "config": None, "bins": [], "applied": None}
    for line in lines:
        if line.startswith("returncode="):
            out["returncode"] = int(line.split()[0].split("=")[1])
        elif match := CONFIG.match(line):
            out["config"] = match.groupdict()
        elif match := BIN.match(line):
            out["bins"].append((int(match["bin"]), int(match["t"]), int(match["edges"]),
                                match["lo"], match["hi"]))
        elif match := APPLIED.match(line):
            out["applied"] = int(match["n"])
    return out


def main() -> int:
    # Optional: restrict the cross-arm comparison to the named arms, e.g. `C-30 V-30`.
    arms = tuple(sys.argv[1:]) or ARMS
    unknown = set(arms) - set(ARMS)
    if unknown:
        raise SystemExit(f"unknown arms {sorted(unknown)}; known {ARMS}")
    problems, sequences = [], {}
    checked = 0
    for cell in CELLS:
        for world in WORLD_IDS:
            expected_sha = hashlib.sha256(world_file(world, cell).read_bytes()).hexdigest()
            for arm in arms:
                name = f"{arm}-{world}-{cell}"
                log = LOGS / f"{name}.log"
                if not log.exists():
                    problems.append(f"{name}: no log (not run yet?)")
                    continue
                checked += 1
                job = parse(log)
                if job["returncode"] != 0:
                    problems.append(f"{name}: returncode={job['returncode']}")
                if job["config"] is None or job["config"]["sha"] != expected_sha:
                    problems.append(f"{name}: world config sha mismatch or missing")
                bins = job["bins"]
                if [b[0] for b in bins] != list(range(len(bins))):
                    problems.append(f"{name}: bins not 0..k in order: {[b[0] for b in bins]}")
                if not bins or (bins[0][3], bins[0][4]) != ("1.0000", "1.0000"):
                    problems.append(f"{name}: bin 0 is not anchored at factor 1")
                if job["applied"] != len(bins):
                    problems.append(f"{name}: applied={job['applied']} but {len(bins)} bin lines")
                if len({b[2] for b in bins}) > 1:
                    problems.append(f"{name}: edge count changes between bins")
                sequences.setdefault((world, cell), {})[arm] = bins
    worst_lag, worst_spread = (0, None), (0, None)
    for (world, cell), by_arm in sorted(sequences.items()):
        common = min(len(bins) for bins in by_arm.values())
        prefixes = {tuple((b[0], b[3], b[4]) for b in bins[:common]) for bins in by_arm.values()}
        lengths = sorted({len(bins) for bins in by_arm.values()})
        reference = next(iter(by_arm.values()))
        factors = ", ".join(f"{b[0]}:[{b[3]},{b[4]}]" for b in reference[:common])
        lags, spreads = [], []
        for index in range(1, common):
            times = [bins[index][1] for bins in by_arm.values()]
            lag = max(times) - index * BIN_S
            lags.append(lag)
            spreads.append(max(times) - min(times))
            if lag > worst_lag[0]:
                worst_lag = (lag, f"{world} {cell} bin {index}")
            if spreads[-1] > worst_spread[0]:
                worst_spread = (spreads[-1], f"{world} {cell} bin {index}")
        print(f"{world} {cell}: arms={len(by_arm)} commonBins={common} binCounts={lengths} "
              f"identicalOnCommonBins={len(prefixes) == 1} maxSwitchLag={max(lags, default=0)}s "
              f"maxSwitchSpreadAcrossArms={max(spreads, default=0)}s")
        print(f"    factors: {factors}")
        if len(prefixes) != 1:
            problems.append(f"{world} {cell}: bin/factor sequence differs across arms on common bins")
        if any(bins[0][1] != 0 for bins in by_arm.values()):
            problems.append(f"{world} {cell}: bin 0 not applied at t=0")
    print(f"worst switch lag after the nominal bin start: {worst_lag[0]}s ({worst_lag[1]})")
    print(f"worst spread of the switch time across arms: {worst_spread[0]}s ({worst_spread[1]})")
    print(f"checked {checked} job logs; problems: {len(problems)}")
    for problem in problems:
        print("  " + problem)
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
