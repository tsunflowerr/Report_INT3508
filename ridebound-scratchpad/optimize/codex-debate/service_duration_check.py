"""Count serviceDurationMs values and boarding-related fields in decoded transcript frames of T3.8 test runs.
Usage: python -B service_duration_check.py <out> (mode x). Read-only on run outputs."""
import base64, collections, json, pathlib, re, sys
ROOT = pathlib.Path("C:/RideBoundData/research/tier3-t38-v1")
RUNS = ["C-30-d20181114-s10-r1-w07", "U-d20181115-s10-r2-w08", "Mplus-30-d20181116-s10-r1-w17"]
out = ["# service_duration_check.py"]
for run in RUNS:
    vals, keys = collections.Counter(), collections.Counter()
    with open(ROOT / run / "transcript-00.ndjson", encoding="utf-8") as fh:
        for line in fh:
            frame = base64.b64decode(json.loads(line)["frameBase64"]).decode("utf-8")
            for m in re.finditer(r'"serviceDurationMs":(\d+)', frame):
                vals[int(m.group(1))] += 1
            for m in re.finditer(r'"([A-Za-z]*(?:[Dd]well|[Bb]oarding|[Aa]lighting)[A-Za-z]*)"', frame):
                keys[m.group(1)] += 1
    out.append(f"{run}: serviceDurationMs values {dict(vals.most_common(8))}; boarding/dwell keys {dict(keys.most_common(8))}")
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
