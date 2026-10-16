"""Task w07x analysis (W07X-PLAN.md §3-§4), read-only; every output file is created with mode "x".

Levels 30, 60, 90, 120, 150, 180, 240, 300 s. New runs (tier3-w07x-v1): C/Mplus at 90, 150, 180, 240 and V at 90..240.
Reused task B runs (tier3-w07-v1): U, C/Mplus at 30, 60, 120, 300 and V-30. Uses sweep_analyze.job_row (M1-M8, audit)
pointed at the right root per job, pilot_analyze.fleet_decisions for decision identity, the v1.2 world-log checks of
../w07/w07_analyze.py for the new runs, and per-rider V_r (sum |z| over drop revisions) for V's own promise.
Usage: python -B w07x_analyze.py <out-prefix> [partial]
"""
from __future__ import annotations

import base64
import hashlib
import json
import pathlib
import statistics
import sys

HERE = pathlib.Path(__file__).resolve().parent
TANG3 = HERE.parent
for sub in ("sweep", "pilot", "evidence", "world", "w07"):
    sys.path.insert(0, str(TANG3 / sub))

import audit_vep  # noqa: E402
import run_w07  # noqa: E402
import run_w07x  # noqa: E402
import sweep_analyze  # noqa: E402
import w07_analyze  # noqa: E402
from pilot_analyze import fleet_decisions  # noqa: E402
from world_v1 import BIN_S  # noqa: E402

LEVELS = (30, 60, 90, 120, 150, 180, 240, 300)
NEW_LEVELS = (90, 150, 180, 240)
CELLS = run_w07.CELLS


def root_of(arm: str) -> pathlib.Path:
    return run_w07x.OUT_ROOT if arm in run_w07x.ARMS else run_w07.OUT_ROOT


def arms_at(x: int) -> list[str]:
    names = [f"C-{x}", f"Mplus-{x}"]
    if x == 30 or x in (90, 120, 150, 180, 240):
        names.append(f"V-{x}")
    return names


def policy_hash(transcript: pathlib.Path):
    with open(transcript, encoding="utf-8") as handle:
        for line in handle:
            record = json.loads(line)
            envelope = json.loads(base64.b64decode(record["frameBase64"]))
            if envelope.get("messageType") == "initializeRun":
                found = [v for k, v in walk(envelope["payload"]) if k == "policyConfigurationHash"]
                return found[0] if len(found) == 1 else None
    return None


def walk(value, key=None):
    if isinstance(value, dict):
        for k, v in value.items():
            yield from walk(v, k)
    elif isinstance(value, list):
        for v in value:
            yield from walk(v, key)
    else:
        yield key, value


def rider_v(transcript: pathlib.Path) -> dict[str, int]:
    table, summary = audit_vep.audit(transcript)
    values = {}
    for request, coordinate, _, kind, _, _, _, _, _, _, z, closed in table:
        if coordinate == "drop":
            values.setdefault(request, 0)
            if kind != "initialPromise" and not closed:
                values[request] += abs(z)
    if sum(values.values()) != summary["sumDropV"]:
        raise SystemExit(f"{transcript}: V does not match the oracle")
    return values


def log_problems(name: str, cell: str) -> list[str]:
    log = run_w07x.LOG_ROOT / f"{name}.log"
    if not log.exists():
        return [f"{name}: no log"]
    lines = log.read_text(encoding="utf-8", errors="replace").splitlines()
    day = f"2018-11-{cell[7:9]}"
    base = w07_analyze.expected_base(day)
    problems = []
    if not lines or not lines[0].startswith("returncode=0 "):
        problems.append(f"{name}: {lines[0] if lines else 'empty log'}")
    world_sha = hashlib.sha256(run_w07.world_file(cell).read_bytes()).hexdigest()
    versions = [m for line in lines if (m := w07_analyze.VERSION.match(line))]
    if len(versions) != 1 or versions[0]["sha"] != world_sha:
        problems.append(f"{name}: v1.2 version line missing or world SHA-256 mismatch")
    guards = [m for line in lines if (m := w07_analyze.GUARD.match(line))]
    if len(guards) != 1 or (guards[0]["day"], int(guards[0]["start"])) != (day, 25200):
        problems.append(f"{name}: guard line missing or wrong")
    bins = [(int(m["bin"]), int(m["t"]), float(m["lo"]), float(m["hi"])) for line in lines
            if (m := w07_analyze.BIN.match(line))]
    if [b[0] for b in bins] != list(range(len(bins))) or any(t != b * BIN_S for b, t, _, _ in bins):
        problems.append(f"{name}: bins not 0..k at bin * {BIN_S} s")
    if any(abs(lo - base[b]) > 1e-4 or abs(hi - base[b]) > 1e-4 for b, _, lo, hi in bins):
        problems.append(f"{name}: a bin factor differs from the factor file of {day}")
    applied = [int(m["n"]) for line in lines if (m := w07_analyze.APPLIED.match(line))]
    if applied != [len(bins)]:
        problems.append(f"{name}: applied {applied} vs {len(bins)} bin lines")
    return problems


def main() -> int:
    if len(sys.argv) not in (2, 3) or (len(sys.argv) == 3 and sys.argv[2] != "partial"):
        print(__doc__)
        return 2
    prefix, partial = sys.argv[1], len(sys.argv) == 3
    rows, fleets, vshare, problems, hashes = {}, {}, {}, [], {}
    needed = {"U"} | {a for x in LEVELS for a in arms_at(x)}
    for arm in sorted(needed):
        root = root_of(arm)
        for cell in CELLS:
            name = f"{arm}-{cell}"
            state = (run_w07x.state_of if root == run_w07x.OUT_ROOT else run_w07.state_of)(name)
            if not state.startswith("status-"):
                if not partial:
                    problems.append(f"{name}: state {state}")
                continue
            sweep_analyze.OUT_ROOT, sweep_analyze.effective = root, (lambda n: n)
            sweep_analyze.state_of = run_w07x.state_of if root == run_w07x.OUT_ROOT else run_w07.state_of
            row = sweep_analyze.job_row(name, arm, "W5", cell)
            rows[(arm, cell)] = row
            if state != "status-pass":
                problems.append(f"{name}: {state}")
            if row.get("audit") != "ok":
                problems.append(f"{name}: audit {row.get('audit')}")
                continue
            transcript = root / name / "transcript-00.ndjson"
            fleets[(arm, cell)] = [d for _, d in fleet_decisions(transcript)]
            hashes[(arm, cell)] = policy_hash(transcript)
            summary = json.loads((root / name / "summary.json").read_text(encoding="utf-8"))
            if summary.get("repositoryInventorySha256") != run_w07.EXPECTED_INVENTORY:
                problems.append(f"{name}: inventory {summary.get('repositoryInventorySha256')}")
            if arm.startswith("V-"):
                x_ms = int(arm.split("-")[1]) * 1000
                values = rider_v(transcript)
                vshare[(arm, cell)] = sum(1 for v in values.values() if v > x_ms) / len(values)
            if root == run_w07x.OUT_ROOT:
                problems.extend(log_problems(name, cell))
    for arm in sorted(needed):
        hs = {hashes[(arm, c)] for c in CELLS if (arm, c) in hashes}
        if len(hs) > 1:
            problems.append(f"{arm}: {len(hs)} policyConfigurationHash values across cells")
    arm_hash = {arm: next(iter({hashes[(arm, c)] for c in CELLS if (arm, c) in hashes}), None) for arm in needed}
    known = [h for h in arm_hash.values() if h]
    if len(set(known)) != len(known):
        problems.append("two arms share one policyConfigurationHash")

    out = []
    say = out.append
    served = lambda arm, cell: rows.get((arm, cell), {}).get("M1_completed")  # noqa: E731
    mean = lambda arm, key: (statistics.mean(float(rows[(arm, c)].get(key) or 0) for c in CELLS)  # noqa: E731
                             if all((arm, c) in rows for c in CELLS) else None)
    total = lambda arm: sum(served(arm, c) for c in CELLS) if all((arm, c) in rows for c in CELLS) else None  # noqa: E731
    same = lambda a, b: sum(1 for c in CELLS if (a, c) in fleets and (b, c) in fleets and fleets[(a, c)] == fleets[(b, c)])  # noqa: E731
    fmt = lambda v, p=3: "-" if v is None else f"{v:.{p}f}"  # noqa: E731
    say(f"# w07x_analyze.py {'PARTIAL' if partial else 'FULL'}; jobs analysed {len(rows)}")
    say(f"== validity: {len(problems)} problem(s)")
    for problem in problems or ["none"]:
        say("  " + problem)
    say(f"  policyConfigurationHash distinct per arm: {len(set(known))} hashes for {len(known)} arms")

    say("\n== per level (8 cells, 864 requests): served U/C/Mplus/V, same decisions, prunes, max C_r, promise broken, forced, E2")
    say(f"  U served {total('U')}")
    for x in LEVELS:
        c, m, v = f"C-{x}", f"Mplus-{x}", f"V-{x}"
        has_v = v in arms_at(x)
        vshares = [vshare[(v, cc)] for cc in CELLS if (v, cc) in vshare] if has_v else []
        say(f"  x={x:>3}: served C {total(c)} M+ {total(m)}" + (f" V {total(v)}" if has_v else "")
            + f" | same C/M+ {same(c, m)}/8" + (f" V/C {same(v, c)}/8" if has_v else "")
            + f" | prunes C {sum(int(rows[(c, cc)]['M7_gatePrunes']) for cc in CELLS if (c, cc) in rows)}"
            f" M+ {sum(int(rows[(m, cc)]['M7_gatePrunes']) for cc in CELLS if (m, cc) in rows)}"
            + (f" V {sum(int(rows[(v, cc)]['M7_gatePrunes']) for cc in CELLS if (v, cc) in rows)}" if has_v else "")
            + f" | max C_r (s) C {fmt(max((rows[(c, cc)]['M4_maxC_ms'] for cc in CELLS if (c, cc) in rows), default=0) / 1000, 1)}")
        say(f"          own promise broken: C {fmt(mean(c, 'M4_shareC_gt_x'))} M+ {fmt(mean(m, 'M3_shareA_gt_x'))}"
            + (f" V {fmt(statistics.mean(vshares) if len(vshares) == 8 else None)}" if has_v else "")
            + f" | by the deadline rule (A > x): C {fmt(mean(c, 'M3_shareA_gt_x'))} M+ {fmt(mean(m, 'M3_shareA_gt_x'))}"
            + (f" V {fmt(mean(v, 'M3_shareA_gt_x'))}" if has_v else "")
            + f" | forced C {fmt(mean(c, 'M5_nonNormalShare'))} M+ {fmt(mean(m, 'M5_nonNormalShare'))}"
            + (f" V {fmt(mean(v, 'M5_nonNormalShare'))}" if has_v else "")
            + f" | E2 C {fmt(mean(c, 'M2_E2'))} M+ {fmt(mean(m, 'M2_E2'))}" + (f" V {fmt(mean(v, 'M2_E2'))}" if has_v else ""))
    say("\n== served per cell: U | then per level C/M+/V")
    for cell in CELLS:
        parts = [f"U {served('U', cell)}"] + [
            f"{x}: {served(f'C-{x}', cell)}/{served(f'Mplus-{x}', cell)}" + (f"/{served(f'V-{x}', cell)}" if f"V-{x}" in arms_at(x) else "")
            for x in LEVELS]
        say(f"  {cell}: " + " | ".join(parts))

    say("\n== predictions (W07X-PLAN §4)")
    cjobs = [(f"C-{x}", c) for x in NEW_LEVELS for c in CELLS if (f"C-{x}", c) in rows]
    bad = [f"{a}-{c}" for a, c in cjobs if float(rows[(a, c)]["M5_nonNormalShare"] or 0) > 0]
    say(f"R1 new C-x jobs with non-normal decisions: {len(bad)}/{len(cjobs)} {bad} -> "
        f"{'HELD' if len(cjobs) == 32 and not bad else 'NOT HELD' if bad else 'incomplete'}")
    r2 = {x: 8 - same(f"C-{x}", f"Mplus-{x}") for x in NEW_LEVELS}
    complete = all((f"{f}-{x}", c) in fleets for x in NEW_LEVELS for f in ("C", "Mplus") for c in CELLS)
    say(f"R2 cells where C-x and Mplus-x decisions differ: {r2} -> "
        f"{'HELD' if complete and all(1 <= v <= 4 for v in r2.values()) else 'NOT HELD' if complete else 'incomplete'}")
    r3 = {}
    for x in NEW_LEVELS:
        diffs = [served(f"C-{x}", c) - served(f"Mplus-{x}", c) for c in CELLS
                 if served(f"C-{x}", c) is not None and served(f"Mplus-{x}", c) is not None]
        r3[x] = (sum(diffs), sum(1 for d in diffs if d > 0), diffs)
    ok3 = complete and all(abs(t) <= 2 and pos <= 2 for t, pos, _ in r3.values())
    say(f"R3 per level (total C-M+, cells with C>M+, per-cell diffs): {r3} -> {'HELD' if ok3 else 'NOT HELD' if complete else 'incomplete'}")
    r4 = {x: (mean(f"V-{x}", "M5_nonNormalShare"), mean(f"Mplus-{x}", "M5_nonNormalShare")) for x in (90, 120, 150, 180, 240)}
    ok4 = all(v is not None and m is not None and v > m for v, m in r4.values())
    say(f"R4 forced share V vs M+: { {x: (fmt(v), fmt(m)) for x, (v, m) in r4.items()} } -> "
        f"{'HELD' if ok4 else 'NOT HELD' if all(v is not None and m is not None for v, m in r4.values()) else 'incomplete'}")
    r5 = {x: (total(f"V-{x}"), total(f"C-{x}")) for x in (90, 120, 150, 180, 240)}
    ok5 = all(a is not None and b is not None and abs(a - b) <= 2 for a, b in r5.values())
    say(f"R5 served V vs C: {r5} -> {'HELD' if ok5 else 'NOT HELD' if all(a is not None and b is not None for a, b in r5.values()) else 'incomplete'}")
    seq = {x: mean(f"Mplus-{x}", "M3_shareA_gt_x") for x in (60, 90, 120, 150, 180, 240, 300)}
    vals = list(seq.values())
    ok6 = (None not in vals and all(a >= b for a, b in zip(vals, vals[1:])) and 0.015 <= seq[90] <= 0.05
           and all(seq[x] <= 0.01 for x in (150, 180, 240)))
    say(f"R6 M+ own promise broken by level: { {x: fmt(v, 4) for x, v in seq.items()} } -> "
        f"{'HELD' if ok6 else 'NOT HELD' if None not in vals else 'incomplete'}")
    r7 = {x: (mean(f"C-{x}", "M3_shareA_gt_x"), mean(f"Mplus-{x}", "M3_shareA_gt_x")) for x in NEW_LEVELS}
    ok7 = all(a is not None and b is not None and abs(a - b) <= 0.01 for a, b in r7.values())
    say(f"R7 A > x share C vs M+: { {x: (fmt(a, 4), fmt(b, 4)) for x, (a, b) in r7.items()} } -> "
        f"{'HELD' if ok7 else 'NOT HELD' if all(a is not None and b is not None for a, b in r7.values()) else 'incomplete'}")
    vown = {x: (statistics.mean(vshare[(f'V-{x}', c)] for c in CELLS) if all((f'V-{x}', c) in vshare for c in CELLS) else None,
                mean(f"V-{x}", "M3_shareA_gt_x")) for x in (30, 90, 120, 150, 180, 240)}
    own = [a for a, _ in vown.values()]
    ok8 = None not in own and all(a >= b for a, b in zip(own, own[1:])) and all(a >= b for a, b in vown.values())
    say(f"R8 V own promise broken vs V's A > x: { {x: (fmt(a, 4), fmt(b, 4)) for x, (a, b) in vown.items()} } -> "
        f"{'HELD' if ok8 else 'NOT HELD' if None not in own else 'incomplete'}")

    columns = sorted({k for r in rows.values() for k in r if not k.startswith("_")},
                     key=lambda k: (k not in ("job", "arm", "cell", "state", "audit"), k))
    with open(f"{prefix}-jobs.tsv", "x", encoding="utf-8", newline="\n") as handle:
        handle.write("\t".join(columns + ["root", "policyConfigurationHash", "V_own_broken"]) + "\n")
        for (arm, cell), r in rows.items():
            handle.write("\t".join(["" if r.get(c) is None else str(r.get(c)) for c in columns]
                                   + [str(root_of(arm)), str(hashes.get((arm, cell))), str(vshare.get((arm, cell), ""))]) + "\n")
    text = "\n".join(out) + "\n"
    with open(f"{prefix}-report.txt", "x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
