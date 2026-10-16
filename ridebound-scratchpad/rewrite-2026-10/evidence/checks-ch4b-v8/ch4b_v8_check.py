"""Read-only checks for Chapter 4 part B v8 (2026-10-12). No simulation, no model fitting, no writes except the
output file (opened with mode "x").

Part A  Family-A cells TSV: pooled counts behind the scenario-mean rates of the forecast table (late > 60 s and
        early < -60 s vs. the no-forecast promise P0, the proportional pad, and the forecast promise D0), for the
        21 active weekday scenarios (days 14, 15, 16/11). count = share x served per scenario; the residual from the
        nearest integer is reported (it must be ~0 because share = count / served in forecast_family_a.py).
Part B  ML pilot rows (A1): counts behind the printed Y60 / early60 percentages, inverted from the 3-decimal rates.
        A count k is accepted only if |rate * n / 100 - k| <= 0.0005 * n / 100 (the rounding bound), which makes k
        unique whenever n < 200000.
Part C  Run manifests: the initializeRun frame (ordinal 3) of every transcript-00.ndjson of the 8 snow runs and of
        every C-30-* run folder of the main T3.8 run set; distinct (binarySha256, coreCommitSha, policyId,
        policyVersion, policyConfigurationHash) tuples are counted. Also sha256 of the archived runner DLL and the
        recovery line of the WP4 configuration.
Usage: python -I -B ch4b_v8_check.py <out-file>
"""
from __future__ import annotations

import base64
import csv
import hashlib
import itertools
import json
import pathlib
import statistics
import sys

S = pathlib.Path("E:/Code/Report_INT3508/ridebound-scratchpad")
CELLS = S / "optimize/test-family-a-causal-no15-2026-10-06-cells.tsv"
MLT = S / "optimize/codex-debate/claude-work/ml-pilot-rows-a1-2026-10-08.tsv"
RES = pathlib.Path("C:/RideBoundData/research")
SNOW_DIR = RES / "tier3-forecast-v1"
MAIN_DIR = RES / "tier3-t38-v1"
DLL = RES / "runner-tier3-v2/RideBound.Runner.dll"
WP4 = S / "tang3/configs/wp4-tier3-v2.json"

lines: list[str] = []


def say(text: str = "") -> None:
    lines.append(text)


def part_a() -> None:
    say("## Part A: Family-A cells TSV, 21 active weekday scenarios (days 14-16/11)")
    with open(CELLS, encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    say(f"rows read: {len(rows)}")
    metrics = ["Y_naive", "Y_pad", "Y_disp", "E_naive", "E_pad", "E_disp"]
    for arm in ("C-30", "U", "Mplus-30", "V-30"):
        active = [r for r in rows if r["arm"] == arm and r["cell"][7:9] in ("14", "15", "16")]
        for group in ("all", "w07", "w08", "w17"):
            members = active if group == "all" else [r for r in active if r["cell"].endswith(group)]
            served = sum(int(float(r["served"])) for r in members)
            counts, means, worst = {}, {}, 0.0
            for m in metrics:
                total = 0
                for r in members:
                    x = float(r[m]) * int(float(r["served"]))
                    k = round(x)
                    worst = max(worst, abs(x - k))
                    total += k
                counts[m] = total
                means[m] = 100 * statistics.mean(float(r[m]) for r in members)
            say(f"{arm:<9} {group:<4} scenarios {len(members):>2} served {served:>5} | counts "
                + " ".join(f"{m}={counts[m]}" for m in metrics)
                + f" | max residual {worst:.2e}")
            say(f"{'':<9} {'':<4} scenario means (%) "
                + " ".join(f"{m}={means[m]:.4f}" for m in metrics))


def part_b() -> None:
    say("")
    say("## Part B: ML pilot rows A1 (E = 30 s, window all); counts inverted from 3-decimal rates")
    with open(MLT, encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    wanted = {("measured", "U", "test15"), ("measured", "U", "test16"), ("measured", "C-30", "test15"),
              ("measured", "C-30", "test16"), ("static", "FREE", "test13")}
    for r in rows:
        if (r["world"], r["arm"], r["test"]) not in wanted or r["window"] != "all" or r["E"] != "30":
            continue
        n = int(r["n"])
        bound = 0.0005 * n / 100
        parts = []
        for col in ("Y60", "early60"):
            x = float(r[col]) * n / 100
            k = round(x)
            ok = abs(x - k) <= bound + 1e-12
            parts.append(f"{col} {r[col]}% -> {k}/{n} (residual {abs(x - k):.4f}, bound {bound:.4f}, {'OK' if ok else 'AMBIGUOUS'})")
        say(f"{r['world']:<8} {r['arm']:<5} {r['test']:<6} {r['method']:<12} n {n:>3} | " + " | ".join(parts)
            + f" | ext {r['ext']} s p90 {r['p90']} s")


def manifest(path: pathlib.Path) -> tuple[str, ...]:
    with open(path, encoding="utf-8") as handle:
        for line in itertools.islice(handle, 6):
            record = json.loads(line)
            if record.get("ordinal") != 3:
                continue
            frame = json.loads(base64.b64decode(record["frameBase64"]))
            if frame.get("messageType") != "initializeRun":
                raise SystemExit(f"ordinal 3 is not initializeRun in {path}")
            m = frame["payload"]["manifest"]
            return (m.get("binarySha256"), m.get("coreCommitSha"), m.get("policyId"), m.get("policyVersion"),
                    m.get("policyConfigurationHash"))
    raise SystemExit(f"no ordinal-3 frame in {path}")


def part_c() -> None:
    say("")
    say("## Part C: run manifests (initializeRun, ordinal 3)")
    for label, folder, prefix in (("snow", SNOW_DIR, "C-30-d20181115-s10-r"), ("main T3.8", MAIN_DIR, "C-30-")):
        dirs = sorted(d for d in folder.iterdir() if d.is_dir() and d.name.startswith(prefix)
                      and (label != "snow" or d.name[-3:] in ("w14", "w15")))
        tuples: dict[tuple[str, ...], list[str]] = {}
        for d in dirs:
            t = d / "transcript-00.ndjson"
            if not t.exists():
                say(f"{label}: {d.name}: no transcript-00.ndjson")
                continue
            tuples.setdefault(manifest(t), []).append(d.name)
        say(f"{label}: {len(dirs)} folders, {len(tuples)} distinct manifest tuple(s)")
        for key, names in tuples.items():
            say(f"   {len(names):>2} runs: binarySha256={key[0]} coreCommitSha={key[1]} policyId={key[2]} "
                f"policyVersion={key[3]} policyConfigurationHash={key[4]}")
            say(f"      e.g. {names[0]} ... {names[-1]}")
    digest = hashlib.sha256(DLL.read_bytes()).hexdigest()
    say(f"sha256 {DLL} = {digest}")
    with open(WP4, encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            if "commitmentRecovery" in line:
                say(f"{WP4}:{number}: {line.strip()}")


def main(out: str) -> int:
    say("# ch4b_v8_check.py (read-only; 2026-10-12)")
    part_a()
    part_b()
    part_c()
    text = "\n".join(lines) + "\n"
    with open(out, "x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))
