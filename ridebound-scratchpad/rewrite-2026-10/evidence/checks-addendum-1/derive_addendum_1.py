"""Evidence-register addendum 1: derived arithmetic that the addendum cites but the two run-reading scripts do not print
as such. Reads ONLY my own outputs recompute-addendum-1-2026-10-11.txt (ADD1) and check-snow-c30-2026-10-11.txt (SNOW1).
Read-only; one process; output mode "x".
Usage: E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -B derive_addendum_1.py
"""
import ast
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ADD1 = (HERE / "recompute-addendum-1-2026-10-11.txt").read_text(encoding="utf-8").split("\n")
SNOW1 = (HERE / "check-snow-c30-2026-10-11.txt").read_text(encoding="utf-8").split("\n")
OUT = HERE / "derive-addendum-1-2026-10-11.txt"

win = {}
pat = re.compile(r"^- (w\d\d) \((\d+) cells, (\d+) requests\) (\S+)\s*: served (\d+); late60 (\d+); timely60 (\d+); "
                 r"timely120 (\d+); fc late60 (\d+); fc timely60 (\d+)$")
for i, line in enumerate(ADD1, 1):
    m = pat.match(line)
    if m:
        w, cells, req, arm = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)
        win[(w, arm)] = dict(line=i, cells=cells, requests=req, served=int(m.group(5)), late60=int(m.group(6)),
                             timely60=int(m.group(7)), timely120=int(m.group(8)), fc_late60=int(m.group(9)),
                             fc_timely60=int(m.group(10)))
out = ["# derive_addendum_1.py: arithmetic on ADD1 / SNOW1 lines (line numbers of the inputs given)"]
for w in ("w07", "w08", "w17"):
    a, b, u = win[(w, "C-120")], win[(w, "C-30")], win[(w, "U")]
    out.append(f"{w} (ADD1:{a['line']},{b['line']},{u['line']}): C-120 - C-30 served {a['served'] - b['served']:+d}, late60 "
               f"{a['late60'] - b['late60']:+d}, timely60 {a['timely60'] - b['timely60']:+d}, timely120 "
               f"{a['timely120'] - b['timely120']:+d}, fc timely60 {a['fc_timely60'] - b['fc_timely60']:+d}; "
               f"U - C-30 served {u['served'] - b['served']:+d}; cells {a['cells']}, requests {a['requests']}")
tot_cells = sum(win[(w, "U")]["cells"] for w in ("w07", "w08", "w17"))
tot_req = sum(win[(w, "U")]["requests"] for w in ("w07", "w08", "w17"))
out.append(f"cells per window sum {tot_cells}; requests per window sum {tot_req}")

n15 = next((i, l) for i, l in enumerate(ADD1, 1) if l.startswith("N-15: + Stage 1a"))
runs = int(re.search(r"=> runs (\d+)", n15[1]).group(1))
recs = int(re.search(r"records (\d+), cumulative-only", n15[1]).group(1))
cum = int(re.search(r"cumulative-only (\d+); my", n15[1]).group(1))
snow = next((i, l) for i, l in enumerate(SNOW1, 1) if l.startswith("all 8:"))
classes = ast.literal_eval(re.search(r"prune classes (\{[^}]*\})", snow[1]).group(1))
snow_total = sum(classes.values())
snow_cum = classes.get("cumulative-only", 0)
out.append(f"audited C runs incl. the 8 snow C-30 runs (ADD1:{n15[0]}, SNOW1:{snow[0]}): runs {runs} + 8 = {runs + 8}; "
           f"records {recs} + {snow_total} = {recs + snow_total}; cumulative-only {cum} + {snow_cum} = {cum + snow_cum}")
text = "\n".join(out) + "\n"
with open(OUT, "x", encoding="utf-8", newline="\n") as fh:
    fh.write(text)
sys.stdout.write(text)
