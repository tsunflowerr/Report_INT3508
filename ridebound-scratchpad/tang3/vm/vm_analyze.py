"""Task A analysis (VM-PLAN.md §4-§6), read-only on the outputs; every output file is created with mode "x".

Reuses the verified tools: sweep/sweep_analyze.job_row (M1-M8, audit v/e/p, per-rider A and C), pilot/pilot_analyze
.fleet_decisions (ordered fleet actions of acknowledged decisions), the regexes of sweep/sweep_worlds.py, and the
per-rider V of pilot/pilot_paired.py. New here: witness counts per (stage, code) over acknowledged decisions, the
validity checks of VM-PLAN §5 and the evaluation of the sealed predictions P1-P8.

Usage: python -B vm_analyze.py <out-prefix> [partial]
  writes <out-prefix>-jobs.tsv, <out-prefix>-paired.tsv and <out-prefix>-report.txt.
  "partial" evaluates only the jobs that already have a summary (for progress checks); the report says so.
"""
from __future__ import annotations

import base64
import collections
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
TANG3 = HERE.parent
for sub in ("sweep", "pilot", "evidence"):
    sys.path.insert(0, str(TANG3 / sub))

import audit_vep  # noqa: E402
import run_sweep  # noqa: E402
import run_vm  # noqa: E402
import sweep_analyze  # noqa: E402
import sweep_worlds  # noqa: E402
from pilot_analyze import fleet_decisions  # noqa: E402
from run_sweep import run_pilot  # noqa: E402

TANGLED = [(w, c) for w in ("W1", "W2", "W4", "W5") for c in run_vm.CELLS]      # 8 cells with congestion
DRIFT = [(w, c) for w in ("W1", "W2", "W3", "W4", "W5") for c in run_vm.CELLS]  # 10 cells with drift
SMOKE_V30_W4 = pathlib.Path(r"E:/RideBoundData/research/tier3-world-v11-smoke/v11-V-30-W4")
NOWORSE_ROOT = pathlib.Path(r"C:/RideBoundData/research/tier3-sweep-noworse-v1")
ORIGINAL = (sweep_analyze.OUT_ROOT, sweep_analyze.effective, sweep_analyze.state_of)


def point_analyzer(variant: str | None) -> None:
    """Point the verified sweep row builder at one output root (None = the sweep itself)."""
    if variant is None:
        sweep_analyze.OUT_ROOT, sweep_analyze.effective, sweep_analyze.state_of = ORIGINAL
    else:
        sweep_analyze.OUT_ROOT = run_vm.VARIANTS[variant]["out"]
        sweep_analyze.effective = lambda name: name
        sweep_analyze.state_of = lambda name, v=variant: run_vm.state_of(v, name)


def witness_facts(transcript: pathlib.Path):
    """Acknowledged decisions with >= 1 witness of each (stage, code); breaches by kind in the final checkpoint."""
    witnesses, acknowledged, final = {}, set(), None
    with open(transcript, encoding="utf-8") as handle:
        for line in handle:
            record = json.loads(line)
            envelope = json.loads(base64.b64decode(record["frameBase64"]))
            kind = envelope.get("messageType")
            if record["direction"] == "runnerToAdapter" and kind == "decision":
                payload = envelope["payload"]
                body = (payload.get("certificate") or {}).get("body") or {}
                witnesses[payload["decisionHash"]] = {(w.get("stage"), w.get("code")) for w in body.get("witnesses") or []}
            elif record["direction"] == "adapterToRunner" and kind == "decisionApplied":
                acknowledged.add(envelope["payload"]["decisionHash"])
            elif record["direction"] == "runnerToAdapter" and kind == "checkpoint":
                final = envelope["payload"]["content"]["onlineState"]
    counts = collections.Counter()
    for decision_hash, pairs in witnesses.items():
        if decision_hash in acknowledged:
            counts.update(pairs)
    breaches = collections.Counter(b.get("kind") for b in (final or {}).get("incidentLedger", {}).get("breaches", []))
    return counts, breaches


def rider_v(transcript: pathlib.Path):
    table, summary = audit_vep.audit(transcript)
    values = {}
    for request, coordinate, _, kind, _, _, _, _, _, _, z, closed in table:
        if coordinate != "drop":
            continue
        values.setdefault(request, 0)
        if kind != "initialPromise" and not closed:
            values[request] += abs(z)
    if sum(values.values()) != summary["sumDropV"] or len(values) != summary["promisedRiders"]:
        raise SystemExit(f"{transcript}: per-rider V does not match the oracle totals")
    return values


def world_problems(log: pathlib.Path, world: str, cell: str):
    """Checks 3 of VM-PLAN §5 on one job log (same rules as sweep_worlds.py); returns (problems, bins)."""
    problems = []
    expected = hashlib.sha256(run_pilot.world_file(world, cell).read_bytes()).hexdigest()
    lines = log.read_text(encoding="utf-8", errors="replace").splitlines()
    if not lines or not lines[0].startswith("returncode=0 "):
        problems.append(f"{log.name}: {lines[0] if lines else 'empty log'}")
    configs = [m for line in lines if (m := sweep_worlds.CONFIG.match(line))]
    if len(configs) != 1 or configs[0]["sha"] != expected:
        problems.append(f"{log.name}: world v1.1 config line missing or SHA-256 mismatch")
    bins = [(int(m["bin"]), int(m["t"]), m["lo"], m["hi"]) for line in lines if (m := sweep_worlds.BIN.match(line))]
    if [b[0] for b in bins] != list(range(len(bins))):
        problems.append(f"{log.name}: bins not 0..k")
    if any(t != b * sweep_worlds.BIN_S for b, t, _, _ in bins):
        problems.append(f"{log.name}: a bin was not applied at exactly bin * {sweep_worlds.BIN_S} s")
    if not bins or (bins[0][2], bins[0][3]) != ("1.0000", "1.0000"):
        problems.append(f"{log.name}: bin 0 not anchored")
    applied = [int(m["n"]) for line in lines if (m := sweep_worlds.APPLIED.match(line))]
    if applied != [len(bins)]:
        problems.append(f"{log.name}: applied {applied} vs {len(bins)} bin lines")
    return problems, [(b, lo, hi) for b, _, lo, hi in bins]


def main() -> int:
    if len(sys.argv) not in (2, 3) or (len(sys.argv) == 3 and sys.argv[2] != "partial"):
        print(__doc__)
        return 2
    prefix, partial = sys.argv[1], len(sys.argv) == 3
    report = []
    say = report.append
    rows, private = [], {}
    problems = []
    sequences = collections.defaultdict(dict)
    scenario = collections.defaultdict(dict)
    inventories = set()
    for variant, name, arm, world, cell in run_vm.jobs():
        state = run_vm.state_of(variant, name)
        if partial and not state.startswith("status-"):
            continue
        point_analyzer(variant)
        row = sweep_analyze.job_row(name, arm, world, cell)
        row["variant"] = variant
        output = run_vm.VARIANTS[variant]["out"] / name
        transcript = output / "transcript-00.ndjson"
        if state != "status-pass":
            problems.append(f"{variant} {name}: state {state}")
        if (output / "failure-00.json").exists():
            failure = json.loads((output / "failure-00.json").read_text(encoding="utf-8"))
            problems.append(f"{variant} {name}: failure {failure.get('failureType')}: {failure.get('failureMessage')}")
        if row.get("audit") not in ("ok",):
            problems.append(f"{variant} {name}: audit {row.get('audit')}")
        if transcript.exists() and row.get("audit") == "ok":
            counts, breaches = witness_facts(transcript)
            for (stage, code), n in sorted(counts.items(), key=str):
                row[f"W_{stage}_{code}"] = n
            for kind, n in sorted(breaches.items(), key=str):
                row[f"B_{kind}"] = n
            row["_fleet"] = [d for _, d in fleet_decisions(transcript)]
            row["_witness"] = counts
        summary_file = output / "summary.json"
        if summary_file.exists():
            summary = json.loads(summary_file.read_text(encoding="utf-8"))
            inventories.add(summary.get("repositoryInventorySha256"))
            scenario[cell][f"{variant}:{arm}:{world}"] = summary.get("sourceScenarioContentSha256")
        log = run_vm.log_path(variant, name)
        if log.exists():
            found, bins = world_problems(log, world, cell)
            problems.extend(found)
            sequences[(world, cell)][f"{variant}:{arm}"] = bins
        rows.append(row)
        private[(variant, arm, world, cell)] = row
    # Comparators from the sweep (C-30, never forced) and, for context, U and Mplus-30 (a) / (b).
    point_analyzer(None)
    comparators = {}
    for world in run_vm.WORLD_IDS:
        for cell in run_vm.CELLS:
            name = f"C-30-{world}-{cell}"
            row = sweep_analyze.job_row(name, "C-30", world, cell)
            row["variant"] = "sweep"
            used = run_sweep.effective(name)
            transcript = run_sweep.OUT_ROOT / used / "transcript-00.ndjson"
            row["_fleet"] = [d for _, d in fleet_decisions(transcript)]
            comparators[(world, cell)] = row
            summary = json.loads((run_sweep.OUT_ROOT / used / "summary.json").read_text(encoding="utf-8"))
            scenario[cell][f"sweep:C-30:{world}"] = summary.get("sourceScenarioContentSha256")
            inventories.add(summary.get("repositoryInventorySha256"))
            found, bins = world_problems(run_sweep.LOG_ROOT / f"{used}.log", world, cell)
            problems.extend(found)
            sequences[(world, cell)]["sweep:C-30"] = bins
            rows.append(row)
    for key, by_arm in sorted(sequences.items()):
        common = min(len(s) for s in by_arm.values())
        if len({tuple(s[:common]) for s in by_arm.values()}) != 1:
            problems.append(f"{key}: world factors differ across arms on common bins")
    for cell, by_job in sorted(scenario.items()):
        if len(set(by_job.values())) != 1:
            problems.append(f"{cell}: sourceScenarioContentSha256 differs across jobs")
    if inventories != {run_vm.EXPECTED_INVENTORY}:
        problems.append(f"repository inventories {sorted(map(str, inventories))}")

    def get(variant, arm, world, cell):
        return private.get((variant, arm, world, cell), {})

    def served(row):
        return row.get("M1_completed")

    def non_normal(row):
        share = row.get("M5_nonNormalShare")
        return None if share is None else share > 0

    say(f"# vm_analyze.py {'PARTIAL (only finished jobs)' if partial else 'FULL'}; jobs analysed: "
        f"{sum(1 for r in rows if r.get('variant') in ('a', 'b'))}/48")
    say(f"== validity (VM-PLAN §5): {len(problems)} problem(s)")
    for problem in problems or ["none"]:
        say("  " + problem)
    say("  inventories: " + ", ".join(sorted(map(str, inventories))))

    say("\n== served (completed / 108) per world and cell: C-30 | V-30 a/b | M-30 a/b | non-normal share V a/b, M a/b")
    for world in run_vm.WORLD_IDS:
        for cell in run_vm.CELLS:
            c = comparators[(world, cell)]
            va, vb, ma, mb = (get(v, arm, world, cell) for arm in ("V-30", "M-30") for v in ("a", "b"))
            fmt = lambda r: "-" if r.get("M5_nonNormalShare") is None else f"{r['M5_nonNormalShare']:.3f}"  # noqa: E731
            say(f"  {world} {cell[-3:]}: C {served(c)} | V {served(va)}/{served(vb)} | M {served(ma)}/{served(mb)} | "
                f"nn V {fmt(va)}/{fmt(vb)} M {fmt(ma)}/{fmt(mb)} | E2 C {c.get('M2_E2')} Vb {vb.get('M2_E2')}")

    say("\n== predictions (VM-PLAN §6)")
    # P1: control.
    checked, failed = 0, []
    for (variant, arm, world, cell), row in private.items():
        if variant != "a" or non_normal(row) is not False:
            continue
        other = get("b", arm, world, cell)
        if "_fleet" not in other or "_fleet" not in row:
            continue
        checked += 1
        if other["_fleet"] != row["_fleet"]:
            failed.append(f"{arm}-{world}-{cell}")
    say(f"P1 control (a without forcing => b identical fleet actions): {checked - len(failed)}/{checked} identical"
        f"{'; MISMATCH ' + str(failed) if failed else ''} -> {'HELD' if checked and not failed else 'NOT HELD' if failed else 'n/a'}")
    # P2: W0.
    p2 = []
    for cell in run_vm.CELLS:
        c = comparators[("W0", cell)]
        for arm in ("V-30", "M-30"):
            for variant in ("a", "b"):
                r = get(variant, arm, "W0", cell)
                if "_completedSet" in r:
                    p2.append((f"{variant}:{arm}:{cell[-3:]}", non_normal(r) is False
                               and set(r["_completedSet"]) == set(c["_completedSet"])))
    say(f"P2 W0 no forcing and same completed set as C-30: {sum(ok for _, ok in p2)}/{len(p2)} "
        f"{[k for k, ok in p2 if not ok]} -> {'HELD' if len(p2) == 8 and all(ok for _, ok in p2) else 'NOT HELD' if p2 and not all(ok for _, ok in p2) else 'incomplete'}")
    # P3: V-30(a), M-30(a) forced in each of the 10 drift cells.
    for arm in ("V-30", "M-30"):
        flags = [(f"{w}{c[-3:]}", non_normal(get("a", arm, w, c))) for w, c in DRIFT]
        known = [f for f in flags if f[1] is not None]
        say(f"P3 {arm}(a) forced in drift cells: {sum(1 for _, f in known if f)}/{len(known)} "
            f"(not forced: {[k for k, f in known if not f]}) -> "
            f"{'HELD' if len(known) == 10 and all(f for _, f in known) else 'NOT HELD' if any(not f for _, f in known) else 'incomplete'}")
    # P4: (b) vs (a) served.
    for arm in ("V-30", "M-30"):
        pairs = [(served(get("a", arm, w, c)), served(get("b", arm, w, c))) for w, c in DRIFT]
        pairs = [(a, b) for a, b in pairs if a is not None and b is not None]
        total_a, total_b = sum(a for a, _ in pairs), sum(b for _, b in pairs)
        at_least = sum(1 for a, b in pairs if b >= a)
        say(f"P4 {arm}: drift cells {len(pairs)}/10, served (a) {total_a} (b) {total_b}, (b)>=(a) in {at_least} -> "
            f"{'HELD' if len(pairs) == 10 and total_b > total_a and at_least >= 7 else 'NOT HELD' if len(pairs) == 10 else 'incomplete'}")
    # P5: new exemption paths exercised end to end.
    budget = sum(get("b", "V-30", w, c).get("_witness", {}).get(("forcedNoWorse", "COMMITMENT_BUDGET_EXCEEDED"), 0)
                 for w, c in DRIFT)
    floor = sum(sum(n for (stage, _), n in get("b", "M-30", "W3", c).get("_witness", {}).items() if stage == "forcedNoWorse")
                for c in run_vm.CELLS)
    say(f"P5 V-30(b) decisions with forcedNoWorse/BUDGET witness over drift cells: {budget}; "
        f"M-30(b) decisions with a forcedNoWorse witness in W3: {floor} -> {'HELD' if budget >= 1 and floor >= 1 else 'NOT HELD (so far)'}")
    # P6: H2 signal criterion (predicted NOT met) and totals.
    for arm in ("V-30", "M-30"):
        gaps = [(f"{w}{c[-3:]}", served(comparators[(w, c)]) - served(get("b", arm, w, c)))
                for w, c in TANGLED if served(get("b", arm, w, c)) is not None]
        big = [k for k, g in gaps if g >= 3]
        total_c = sum(served(comparators[(w, c)]) for w, c in TANGLED if served(get("b", arm, w, c)) is not None)
        total_x = sum(served(get("b", arm, w, c)) for w, c in TANGLED if served(get("b", arm, w, c)) is not None)
        verdict = ("criterion MET" if len(big) >= 6 else "criterion NOT met") if len(gaps) == 8 else "incomplete"
        tag = "P6" if arm == "V-30" else "P6-descriptive"
        extra = ""
        if arm == "V-30" and len(gaps) == 8:
            extra = f"; prediction (NOT met and C total >= V(b) total) -> {'HELD' if len(big) < 6 and total_c >= total_x else 'NOT HELD'}"
        say(f"{tag} C-30 - {arm}(b) per tangled cell {gaps}; >=3 in {len(big)}/{len(gaps)}; totals C {total_c} "
            f"{arm}(b) {total_x}: {verdict}{extra}")
    # P7: E2 of V-30(b) <= C-30 in >= 5/8 tangled cells.
    e2 = [(f"{w}{c[-3:]}", get("b", "V-30", w, c).get("M2_E2"), comparators[(w, c)].get("M2_E2")) for w, c in TANGLED]
    e2 = [(k, v, c) for k, v, c in e2 if v is not None]
    low = sum(1 for _, v, c in e2 if v <= c)
    say(f"P7 E2 V-30(b) <= C-30 in {low}/{len(e2)}: {[(k, round(v, 3), round(c, 3)) for k, v, c in e2]} -> "
        f"{'HELD' if len(e2) == 8 and low >= 5 else 'NOT HELD' if len(e2) == 8 else 'incomplete'}")
    # P8: determinism reference against the v1.1 smoke.
    mine = get("a", "V-30", "W4", run_vm.CELLS[0])
    if "_fleet" in mine and (SMOKE_V30_W4 / "transcript-00.ndjson").exists():
        smoke = [d for _, d in fleet_decisions(SMOKE_V30_W4 / "transcript-00.ndjson")]
        same = smoke == mine["_fleet"]
        say(f"P8 V-30(a) W4-w08 vs v11 smoke: identical fleet actions {same} ({len(mine['_fleet'])}/{len(smoke)} "
            f"decisions), served {served(mine)} -> {'HELD' if same and served(mine) == 92 else 'NOT HELD'}")
    else:
        say("P8 incomplete")

    # Context (descriptive): Mplus-30 (a) from the sweep, (b) from no-worse where treated, U.
    say("\n== context: U | Mplus-30 (a)/(b) served per cell (sweep and no-worse tables)")
    import csv
    sweep_rows = {(r["arm"], r["world"], r["cell"]): r for r in csv.DictReader(
        open(TANG3 / "sweep/sweep-jobs-2026-09-26.tsv", encoding="utf-8"), delimiter="\t")}
    nw_rows = {(r["arm"], r["world"], r["cell"]): r for r in csv.DictReader(
        open(TANG3 / "sweep/noworse-jobs-2026-09-26.tsv", encoding="utf-8"), delimiter="\t") if r["kind"] == "treatment"}
    for world in run_vm.WORLD_IDS:
        for cell in run_vm.CELLS:
            a = sweep_rows[("Mplus-30", world, cell)]["M1_completed"]
            b = nw_rows.get(("Mplus-30", world, cell), sweep_rows[("Mplus-30", world, cell)])["M1_completed"]
            say(f"  {world} {cell[-3:]}: U {sweep_rows[('U', world, cell)]['M1_completed']} | Mplus-30 {a}/{b}")

    # Paired diagnostic: C-30 vs V-30(b) on common riders (E2 threshold of audit_vep).
    paired = []
    limit = audit_vep.E2_THRESHOLD_MS
    for world, cell in TANGLED:
        vb = run_vm.VARIANTS["b"]["out"] / f"V-30-{world}-{cell}" / "transcript-00.ndjson"
        if not vb.exists() or get("b", "V-30", world, cell).get("audit") != "ok":
            continue
        cv = rider_v(run_sweep.OUT_ROOT / run_sweep.effective(f"C-30-{world}-{cell}") / "transcript-00.ndjson")
        vv = rider_v(vb)
        common = set(cv) & set(vv)
        paired.append({"world": world, "cell": cell, "promisedC": len(cv), "promisedVb": len(vv), "common": len(common),
                       "onlyC": len(set(cv) - set(vv)), "onlyVb": len(set(vv) - set(cv)),
                       "commonAbove60C": sum(1 for r in common if cv[r] > limit),
                       "commonAbove60Vb": sum(1 for r in common if vv[r] > limit),
                       "onlyCAbove60": sum(1 for r in set(cv) - set(vv) if cv[r] > limit),
                       "onlyVbAbove60": sum(1 for r in set(vv) - set(cv) if vv[r] > limit)})
    say("\n== paired diagnostic C-30 vs V-30(b), riders promised by both (drop V > 60 s)")
    for p in paired:
        say("  " + "  ".join(f"{k}={v}" for k, v in p.items()))

    columns = sorted({k for r in rows for k in r if not k.startswith("_")},
                     key=lambda k: (k not in ("variant", "job", "arm", "world", "cell", "state", "audit"), k))
    with open(f"{prefix}-jobs.tsv", "x", encoding="utf-8", newline="\n") as handle:
        handle.write("\t".join(columns) + "\n")
        for r in rows:
            handle.write("\t".join("" if r.get(c) is None else str(r.get(c)) for c in columns) + "\n")
    if paired:
        with open(f"{prefix}-paired.tsv", "x", encoding="utf-8", newline="\n") as handle:
            handle.write("\t".join(paired[0]) + "\n")
            for p in paired:
                handle.write("\t".join(str(v) for v in p.values()) + "\n")
    text = "\n".join(report) + "\n"
    with open(f"{prefix}-report.txt", "x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
