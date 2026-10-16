"""Regroup data-inventory-runs-2026-10-08.tsv by experiment (fixes the grouping bug of data_inventory.py's summary:
C:/RideBoundData/research runs were grouped per run). Experiment = first folder under C:/RideBoundData/research, or the
first two folders under E:/RideBoundData. Arm tokens are taken from run-folder names where recognisable.
Usage: python -B data_inventory_group.py <tsv-in> <out> (mode x)."""
import collections, csv, re, sys
rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8"), delimiter="\t"))
def exp_of(r):
    e = r["exp"]
    if e.startswith("research") and not e.startswith("research/"):
        return "C:research/" + e[len("research"):].split("/")[0]
    return "E:" + e
SEP = "[-/\\x5c]"  # hyphen, slash or backslash
ARM = re.compile(r"(?:^|" + SEP + r")(U|FREE|C-\d+F?|Mplus-\d+F?|M-\d+|V-\d+|b1[-a-z0-9]*|c1[-a-z0-9]*|conduct-\d+|visible-\d+|dl2?-\d+)(?=" + SEP + r"|$)")
g = collections.defaultdict(list)
for r in rows:
    g[exp_of(r)].append(r)
out = [f"# data_inventory_group.py: {len(rows)} runs, {len(g)} experiments",
       "experiment | runs | transcripts | req | veh | accepted | world (static = 1 travel snapshot) | arms (from names) | dates"]
for e, rs in sorted(g.items()):
    arms = collections.Counter()
    for r in rs:
        m = ARM.findall(r["run"])
        arms[m[-1] if m else "?"] += 1
    world = collections.Counter("static" if r["snap"] == "1" else ("varying" if r["snap"] not in ("", "None") and int(r["snap"]) > 1 else "unknown") for r in rs)
    c = lambda k: dict(collections.Counter(r[k] for r in rs).most_common(3))  # noqa: E731
    out.append(f"{e} | {len(rs)} | {sum(1 for r in rs if r['tr_mb'] not in ('0', '0.0', ''))} | {c('req')} | {c('veh')} | "
               f"{sum(int(r['acc'] or 0) for r in rs)} | {dict(world)} | {dict(arms.most_common(12))} | {min(r['mtime'] for r in rs)}..{max(r['mtime'] for r in rs)}")
text = "\n".join(out) + "\n"
open(sys.argv[2], "x", encoding="utf-8", newline="\n").write(text); print(text)
