"""Independent check of Codex's round-11 finding: original source trips shared between ML-pilot fit and calibration
splits. Runtime requestId = 'rq-' + sha256(b's' + 8-byte big-endian length + fixture requestId) (mapping.py
_typed_frame + register; verified 108/108 on wp14 d20181112-s10-r4-w08). Each fixture request carries
sourceRecordOrdinal (0-based data row) into its demand file (normalizer-configuration.json demandMemberPath), whose
request_id is the original FleetPy trip. Report overlaps fit/cal, fit/test, cal/test per world and arm.
Usage: python -B provenance_overlap_check.py <out> (mode x)."""
import base64, csv, hashlib, json, pathlib, sys, collections
FIXROOTS = [pathlib.Path("E:/Code/RideBound/benchmarks/fixtures/wp6/public/fleetpy-manhattan-v1/wp14-development-panel-v1"),
            pathlib.Path("C:/RideBoundData/research/fixtures-w07-v1"), pathlib.Path("C:/RideBoundData/research/fixtures-panelA-v1")]
DEMROOT = pathlib.Path("E:/RideBoundData/wp6/extracted/sha256/d9/d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e")
DEM = pathlib.Path("E:/RideBoundData/wp6/extracted/sha256/d9/d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e/"
                   "FleetPy_Manhattan/demand/Manhattan_2018/matched/Manhattan_2019_corrected")
rows = list(csv.DictReader(open("C:/RideBoundData/research/ml-pilot-v1/riders-causal-2026-10-08.csv", encoding="utf-8")))
OPT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(OPT))
import forecast_family_a as fa
W07 = pathlib.Path("C:/RideBoundData/research/tier3-w07-v1")
W14 = pathlib.Path("E:/RideBoundData/wp14r/development-v6-ledger")
TAGS = {"FREE": "b1-ref", "LOCKS": "c1-nobudget", "C-120": "c1-budget120", "C-60": "c1-budget60", "C-30": "c1-h6ref"}
def transcript(world, arm, cell):
    if world == "static":
        return W14 / f"w14-{cell}-{TAGS[arm]}-s7" / "attempt-01" / "output" / "transcript-00.ndjson"
    p = W07 / f"{arm}-{cell}" / "transcript-00.ndjson"
    return p if p.exists() else fa.run_dir("test", arm, cell) / "transcript-00.ndjson"
demand_cache = {}
def runtime_id(fixture_id):
    b = fixture_id.encode("utf-8")
    return "rq-" + hashlib.sha256(b"s" + len(b).to_bytes(8, "big") + b).hexdigest()
def fixture_dir(world, cell):
    roots = FIXROOTS[:1] if world == "static" else FIXROOTS[1:]
    for root in roots:
        if (root / cell / "scenario-content.json").exists():
            return root / cell
    raise SystemExit(f"no fixture for {world} {cell}")
def original_ids(world, arm, cell):
    fx = fixture_dir(world, cell)
    path = json.loads((fx / "normalizer-configuration.json").read_text(encoding="utf-8"))["demandMemberPath"]
    if path not in demand_cache:
        with (DEMROOT / path).open(encoding="utf-8") as fh:
            demand_cache[path] = [row["request_id"] for row in csv.DictReader(fh)]
    sc = json.loads((fx / "scenario-content.json").read_text(encoding="utf-8"))
    return {runtime_id(q["requestId"])[:16]: demand_cache[path][q["sourceRecordOrdinal"]] for q in sc["requests"]}
cells = collections.defaultdict(set)
for r in rows:
    cells[(r["world"], r["arm"], r["role"])].add(r["cell"])
out = ["# provenance_overlap_check.py: original FleetPy request_id overlap between ML-pilot splits (riders in the causal CSV)"]
for (world, arm) in sorted({(w, a) for w, a, _ in cells}):
    ids = collections.defaultdict(set)
    for role in ("fit", "cal", "test13", "test15", "test16"):
        for cell in cells.get((world, arm, role), ()):
            m = original_ids(world, arm, cell)
            for r in rows:
                if r["world"] == world and r["arm"] == arm and r["cell"] == cell:
                    ids[role if not role.startswith("test") else "test"].add(m[r["rider"]])
    out.append(f"{world:<8} {arm:<6} fit {len(ids['fit'])} cal {len(ids['cal'])} test {len(ids['test'])} | overlap fit&cal {len(ids['fit'] & ids['cal'])} "
               f"fit&test {len(ids['fit'] & ids['test'])} cal&test {len(ids['cal'] & ids['test'])} | fit&cal ids {sorted(ids['fit'] & ids['cal'])[:12]}")
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
