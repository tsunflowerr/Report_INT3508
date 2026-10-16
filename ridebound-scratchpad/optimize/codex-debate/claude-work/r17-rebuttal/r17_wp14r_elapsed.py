"""R17 rebuttal: recorded WP14r v6 attempt wall times (attempt-terminal.json elapsedMs) by arm. Read-only; output mode "x".
Concurrency during those runs is not recorded here, so this is a relative indication only.
Usage: python -B r17_wp14r_elapsed.py <out.txt>"""
import glob, json, statistics, sys
ROOT = "E:/RideBoundData/wp14r/development-v6-ledger"
lines = ["# r17_wp14r_elapsed.py: WP14r v6 attempt-01 elapsedMs by arm (s)"]
for arm in ("b1-ref", "c1-nobudget", "c1-budget120", "c1-budget60", "c1-h6ref"):
    xs = [json.load(open(f, encoding="utf-8"))["elapsedMs"] / 1000
          for f in sorted(glob.glob(f"{ROOT}/w14-*-{arm}-s7/attempt-01/attempt-terminal.json"))]
    lines.append(f"{arm}: n {len(xs)} median {statistics.median(xs):.0f} mean {statistics.mean(xs):.0f} max {max(xs):.0f}")
with open(sys.argv[1], "x", encoding="utf-8", newline="\n") as fh:
    fh.write("\n".join(lines) + "\n")
print("\n".join(lines))
