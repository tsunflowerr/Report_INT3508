"""Task B analysis (W07-PLAN.md §4-§5), read-only on the outputs; every output file is created with mode "x".

Reuses sweep/sweep_analyze.job_row (M1-M8, audit v/e/p, per-rider A and C) pointed at the task B output root, and
pilot/pilot_analyze.fleet_decisions. Validity (plan §4): status, audit, the v1.2 world lines of every log (version,
measured-base guard naming the cell's own day and 07:00, bins exactly at bin * 900 s, and every bin factor equal to
f(07:00 + bin * 900) / f(07:00) of the cell's own day from the factor file), one scenario hash per cell, one
inventory. Then the sealed predictions Q1-Q7, then descriptive tables (labelled as such).
Usage: python -B w07_analyze.py <out-prefix> [partial]
"""
from __future__ import annotations

import json
import pathlib
import re
import statistics
import sys

HERE = pathlib.Path(__file__).resolve().parent
TANG3 = HERE.parent
for sub in ("sweep", "pilot", "evidence", "world"):
    sys.path.insert(0, str(TANG3 / sub))

import audit_vep  # noqa: E402
import preflight_world as pw  # noqa: E402
import run_w07  # noqa: E402
import sweep_analyze  # noqa: E402
from pilot_analyze import fleet_decisions  # noqa: E402
from world_v1 import BIN_S  # noqa: E402

VERSION = re.compile(r"^\[world\] version=v1\.2 config=(?P<path>.+?) sha256=(?P<sha>[0-9a-f]{64}) seed=(?P<seed>\d+)$")
GUARD = re.compile(r"^\[world\] measured base check: day=(?P<day>\S+) windowStart=(?P<start>\d+) matches the scenario$")
BIN = re.compile(r"^\[world\] t=\s*(?P<t>\d+)s bin=(?P<bin>\d+) edges=(?P<edges>\d+) factor=\[(?P<lo>[\d.]+), (?P<hi>[\d.]+)\]$")
APPLIED = re.compile(r"^\[world\] bin changes applied: (?P<n>\d+);")
LEVELS = (30, 60, 120, 300)


def expected_base(day: str) -> tuple[float, ...]:
    saved = pw.ALLOWED_WINDOW_STARTS
    pw.ALLOWED_WINDOW_STARTS = (25200, 28800, 61200)
    try:
        return pw.measured_base(day, 1.0, 25200, 24)
    finally:
        pw.ALLOWED_WINDOW_STARTS = saved


def rider_v(transcript: pathlib.Path) -> dict[str, int]:
    table, summary = audit_vep.audit(transcript)
    values = {}
    for request, coordinate, _, kind, _, _, _, _, _, _, z, closed in table:
        if coordinate == "drop":
            values.setdefault(request, 0)
            if kind != "initialPromise" and not closed:
                values[request] += abs(z)
    if sum(values.values()) != summary["sumDropV"]:
        raise SystemExit(f"{transcript}: per-rider V does not match the oracle")
    return values


def main() -> int:
    if len(sys.argv) not in (2, 3) or (len(sys.argv) == 3 and sys.argv[2] != "partial"):
        print(__doc__)
        return 2
    prefix, partial = sys.argv[1], len(sys.argv) == 3
    sweep_analyze.OUT_ROOT = run_w07.OUT_ROOT
    sweep_analyze.effective = lambda name: name
    sweep_analyze.state_of = run_w07.state_of
    rows, problems, scenario, inventories, fleets = {}, [], {}, set(), {}
    bases = {day: expected_base(day) for day in ("2018-11-12", "2018-11-13")}
    for name, arm, cell in run_w07.jobs():
        state = run_w07.state_of(name)
        if partial and not state.startswith("status-"):
            continue
        row = sweep_analyze.job_row(name, arm, "W5", cell)
        rows[(arm, cell)] = row
        output = run_w07.OUT_ROOT / name
        if state != "status-pass":
            problems.append(f"{name}: state {state}")
        if (output / "failure-00.json").exists():
            failure = json.loads((output / "failure-00.json").read_text(encoding="utf-8"))
            problems.append(f"{name}: failure {failure.get('failureType')}: {failure.get('failureMessage')}")
        if row.get("audit") != "ok":
            problems.append(f"{name}: audit {row.get('audit')}")
        if (output / "summary.json").exists():
            summary = json.loads((output / "summary.json").read_text(encoding="utf-8"))
            inventories.add(summary.get("repositoryInventorySha256"))
            scenario.setdefault(cell, set()).add(summary.get("sourceScenarioContentSha256"))
        transcript = output / "transcript-00.ndjson"
        if transcript.exists() and row.get("audit") == "ok":
            fleets[(arm, cell)] = [d for _, d in fleet_decisions(transcript)]
        log = run_w07.LOG_ROOT / f"{name}.log"
        if not log.exists():
            problems.append(f"{name}: no log")
            continue
        lines = log.read_text(encoding="utf-8", errors="replace").splitlines()
        day = f"2018-11-{cell[7:9]}"
        if not lines or not lines[0].startswith("returncode=0 "):
            problems.append(f"{name}: {lines[0] if lines else 'empty log'}")
        versions = [m for line in lines if (m := VERSION.match(line))]
        world_sha = __import__("hashlib").sha256(run_w07.world_file(cell).read_bytes()).hexdigest()
        if len(versions) != 1 or versions[0]["sha"] != world_sha:
            problems.append(f"{name}: v1.2 version line missing or world SHA-256 mismatch")
        guards = [m for line in lines if (m := GUARD.match(line))]
        if len(guards) != 1 or (guards[0]["day"], int(guards[0]["start"])) != (day, 25200):
            problems.append(f"{name}: measured-base guard line missing or wrong day/window")
        bins = [(int(m["bin"]), int(m["t"]), float(m["lo"]), float(m["hi"])) for line in lines if (m := BIN.match(line))]
        if [b[0] for b in bins] != list(range(len(bins))):
            problems.append(f"{name}: bins not 0..k")
        if any(t != b * BIN_S for b, t, _, _ in bins):
            problems.append(f"{name}: a bin was not applied at exactly bin * {BIN_S} s")
        if any(abs(lo - bases[day][b]) > 1e-4 or abs(hi - bases[day][b]) > 1e-4 for b, _, lo, hi in bins):
            problems.append(f"{name}: a bin factor differs from the factor file of {day}")
        applied = [int(m["n"]) for line in lines if (m := APPLIED.match(line))]
        if applied != [len(bins)]:
            problems.append(f"{name}: applied {applied} vs {len(bins)} bin lines")
    for cell, hashes in sorted(scenario.items()):
        if len(hashes) != 1:
            problems.append(f"{cell}: {len(hashes)} scenario hashes")
    if inventories and inventories != {run_w07.EXPECTED_INVENTORY}:
        problems.append(f"inventories {sorted(map(str, inventories))}")

    out = []
    say = out.append
    cells = run_w07.CELLS
    get = lambda arm, cell: rows.get((arm, cell), {})  # noqa: E731
    served = lambda arm, cell: get(arm, cell).get("M1_completed")  # noqa: E731
    nn = lambda arm, cell: get(arm, cell).get("M5_nonNormalShare")  # noqa: E731
    have = lambda arm: [c for c in cells if served(arm, c) is not None]  # noqa: E731
    say(f"# w07_analyze.py {'PARTIAL' if partial else 'FULL'}; jobs analysed {len(rows)}/88")
    say(f"== validity (W07-PLAN §4): {len(problems)} problem(s)")
    for problem in problems or ["none"]:
        say("  " + problem)
    say("  inventories: " + ", ".join(sorted(map(str, inventories))))

    say("\n== served (completed / 108) per cell: U | C-30/60/120/300 | Mplus-30/60/120/300 | V-30 | M-30")
    for cell in cells:
        say(f"  {cell}: U {served('U', cell)} | C " + "/".join(str(served(f'C-{x}', cell)) for x in LEVELS)
            + " | M+ " + "/".join(str(served(f'Mplus-{x}', cell)) for x in LEVELS)
            + f" | V {served('V-30', cell)} | M {served('M-30', cell)}")

    say("\n== predictions (W07-PLAN §5)")
    c_jobs = [(f"C-{x}", c) for x in LEVELS for c in cells if nn(f"C-{x}", c) is not None]
    bad = [f"{a}-{c}" for a, c in c_jobs if nn(a, c) > 0]
    say(f"Q1 C-x jobs with non-normal decisions: {len(bad)}/{len(c_jobs)} {bad} -> "
        f"{'HELD' if len(c_jobs) == 32 and not bad else 'NOT HELD' if bad else 'incomplete'}")
    forced30 = [c for c in have("Mplus-30") if nn("Mplus-30", c) > 0]
    say(f"Q2 Mplus-30 forced in {len(forced30)}/{len(have('Mplus-30'))} cells -> "
        f"{'HELD' if len(forced30) >= 7 else 'NOT HELD' if len(have('Mplus-30')) == 8 else 'incomplete'}")
    broken60 = [c for c in have("Mplus-60") if (get("Mplus-60", c).get("M3_shareA_gt_x") or 0) > 0]
    say(f"Q3 Mplus-60 promise broken (A > 60 s share > 0) in {len(broken60)}/{len(have('Mplus-60'))} cells "
        f"{[(c[:9] + c[-6:-4], round(get('Mplus-60', c)['M3_shareA_gt_x'], 3)) for c in have('Mplus-60')]} -> "
        f"{'HELD' if len(broken60) >= 4 else 'NOT HELD' if len(have('Mplus-60')) == 8 else 'incomplete'}")
    q4 = [c for c in have("Mplus-300") if nn("Mplus-300", c) == 0 and (get("Mplus-300", c).get("M3_shareA_gt_x") or 0) == 0]
    say(f"Q4 Mplus-300 unforced and never late by > 300 s in {len(q4)}/{len(have('Mplus-300'))} cells -> "
        f"{'HELD' if len(q4) == 8 else 'NOT HELD' if len(have('Mplus-300')) == 8 else 'incomplete'}")
    q5_all = True
    for x in LEVELS:
        pairs = [(served(f"C-{x}", c), served(f"Mplus-{x}", c)) for c in cells
                 if served(f"C-{x}", c) is not None and served(f"Mplus-{x}", c) is not None]
        close = sum(1 for a, b in pairs if abs(a - b) <= 2)
        q5_all &= len(pairs) == 8 and close >= 7
        say(f"Q5 x={x}: |C - Mplus| <= 2 in {close}/{len(pairs)} cells; diffs {[a - b for a, b in pairs]}")
    say(f"Q5 -> {'HELD' if q5_all else 'NOT HELD or incomplete'}")
    v_forced = [c for c in have("V-30") if nn("V-30", c) > 0]
    v_close = [c for c in have("V-30") if served("C-30", c) is not None and abs(served("V-30", c) - served("C-30", c)) <= 2]
    say(f"Q6 V-30 forced in {len(v_forced)}/{len(have('V-30'))}; |V-30 - C-30| <= 2 in {len(v_close)}/{len(have('V-30'))} -> "
        f"{'HELD' if len(v_forced) == 8 and len(v_close) >= 7 else 'NOT HELD' if len(have('V-30')) == 8 else 'incomplete'}")
    q7 = [c for c in cells if served("C-30", c) is not None and served("U", c) is not None and served("C-30", c) <= served("U", c)]
    say(f"Q7 C-30 <= U in {len(q7)}/{sum(1 for c in cells if served('C-30', c) is not None and served('U', c) is not None)} -> "
        f"{'HELD' if len(q7) >= 7 else 'NOT HELD or incomplete'}")

    say("\n== descriptive (not predictions): per level, mean over cells")
    for x in LEVELS:
        m, c = f"Mplus-{x}", f"C-{x}"
        cs = [cell for cell in cells if get(m, cell).get("audit") == "ok" and get(c, cell).get("audit") == "ok"]
        if not cs:
            continue
        mean = lambda arm, key: statistics.mean(get(arm, cell).get(key) or 0 for cell in cs)  # noqa: E731
        same = sum(1 for cell in cs if fleets.get((m, cell)) == fleets.get((c, cell)))
        say(f"  x={x}: served C {sum(served(c, cell) for cell in cs)} M+ {sum(served(m, cell) for cell in cs)} "
            f"| M+ promise broken (A>x) {mean(m, 'M3_shareA_gt_x'):.3f} | C scored by M+ rule {mean(c, 'M3_shareA_gt_x'):.3f} "
            f"| C promise broken (C_r>x) {mean(c, 'M4_shareC_gt_x'):.3f} | M+ forced {mean(m, 'M5_nonNormalShare'):.3f} "
            f"| M+ frozen fleet {mean(m, 'M5_meanForcedFleetShare'):.3f} | M+ same decisions as C {same}/{len(cs)} cells")
    say("\n== descriptive: C-30 per cell, lateness against the first promise (A) and C's own promise")
    for cell in cells:
        r = get("C-30", cell)
        if "_A" not in r:
            continue
        a = sorted(r["_A"].values())
        share = lambda limit: sum(1 for v in a if v > limit) / len(a)  # noqa: E731
        say(f"  {cell}: riders {len(a)} | A>30 {share(30000):.3f} A>60 {share(60000):.3f} A>120 {share(120000):.3f} "
            f"| max A {a[-1] / 1000:.1f} s | early by >30 s {sum(1 for v in a if v < -30000) / len(a):.3f}")
    say("\n== descriptive: V-30 own promise (drop V > 30 s) for V-30 and C-30; V-30 same decisions as C-30")
    for cell in cells:
        paths = {arm: run_w07.OUT_ROOT / f"{arm}-{cell}" / "transcript-00.ndjson" for arm in ("V-30", "C-30")}
        if not all(p.exists() for p in paths.values()) or get("V-30", cell).get("audit") != "ok":
            continue
        shares = {arm: (lambda v: sum(1 for x in v.values() if x > 30000) / len(v))(rider_v(p)) for arm, p in paths.items()}
        say(f"  {cell}: V>30 V-30 {shares['V-30']:.3f} C-30 {shares['C-30']:.3f} | V-30 forced {nn('V-30', cell):.3f} "
            f"| same decisions {fleets.get(('V-30', cell)) == fleets.get(('C-30', cell))}")

    columns = sorted({k for r in rows.values() for k in r if not k.startswith("_")},
                     key=lambda k: (k not in ("job", "arm", "cell", "state", "audit"), k))
    with open(f"{prefix}-jobs.tsv", "x", encoding="utf-8", newline="\n") as handle:
        handle.write("\t".join(columns) + "\n")
        for r in rows.values():
            handle.write("\t".join("" if r.get(c) is None else str(r.get(c)) for c in columns) + "\n")
    text = "\n".join(out) + "\n"
    with open(f"{prefix}-report.txt", "x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
