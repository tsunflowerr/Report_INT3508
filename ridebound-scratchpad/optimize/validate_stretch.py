"""Validate promise_stretch on DEVELOPMENT runs only (task B, C-30, 8 cells 12-13/11 07:00-09:00): with the cell day's
TRUE factor path, the stretched first drop promise should equal the actual alight time for riders whose dispatch part
(sum of p - e over drop revisions) is 0. Usage: python -B validate_stretch.py <out> (mode x)"""
import pathlib, statistics, sys
HERE = pathlib.Path(__file__).resolve().parent
TANG3 = HERE.parent / "tang3"
for sub in ("sweep", "evidence", "w07"):
    sys.path.insert(0, str(TANG3 / sub))
sys.path.insert(0, str(HERE))
import audit_vep, sweep_analyze, run_w07, promise_stretch as ps
out = ["# validate_stretch.py (development cells only)"]
allres, alln = [], 0
for cell in run_w07.CELLS:
    t = run_w07.OUT_ROOT / f"C-30-{cell}" / "transcript-00.ndjson"
    table, _ = audit_vep.audit(t)
    _, alighted = sweep_analyze.event_times(t)
    first, disp = {}, {}
    for r, c, _, k, pub, v, e, p, _, _, _, _ in table:
        if c != "drop":
            continue
        if k == "initialPromise":
            first[r] = (pub, p); disp[r] = 0
        else:
            disp[r] += abs(p - e)
    day = f"2018-11-{cell[7:9]}"
    res = []
    for r, (pub, p0) in first.items():
        if r not in alighted or disp[r] != 0:
            continue
        pt = ps.stretch(pub, p0 - pub, ps.true_weight(day, 25200, pub))
        res.append(alighted[r] - pt)
    naive = [alighted[r] - first[r][1] for r in first if r in alighted and disp[r] == 0]
    alln += sum(1 for r in first if r in alighted)
    allres += res
    out.append(f"{cell}: riders with dispatch part 0: {len(res)}/{sum(1 for r in first if r in alighted)}; "
               f"A - true-stretch: min {min(res)/1000:.2f} max {max(res)/1000:.2f} s; A - naive P0: mean {statistics.mean(naive)/1000:+.1f} max {max(naive)/1000:.1f} s")
out.append(f"ALL: {len(allres)}/{alln} riders; |A - true-stretch| <= 1 s for {sum(1 for x in allres if abs(x) <= 1000)}; "
           f"<= 5 s for {sum(1 for x in allres if abs(x) <= 5000)}; max |.| {max(abs(x) for x in allres)/1000:.2f} s")
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
