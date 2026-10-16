"""Lateness of served riders vs their FIRST drop promise, in minutes, with the tail, and relative to trip length,
on the 34 T3.8 test cells: arms U, C-30, Mplus-30 (naive promises) and C-30 with the causal-no15 display layer.
Also pickup lateness vs first pickup promise, wait and ride time. Usage: python -B lateness_distribution.py <out> (mode x)"""
import pathlib, statistics as st, sys
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import display_layer as dl, forecast_family_a as fa
CELLS = fa.run_t38.PHASES["test"][1]
def q(xs, p):
    xs = sorted(xs); return xs[min(len(xs) - 1, int(p * len(xs)))]
out = ["# lateness_distribution.py (34 T3.8 test cells; served riders pooled)"]
for arm, disp in (("U", False), ("C-30", False), ("Mplus-30", False), ("C-30", True)):
    late, rel, pick, wait, ride = [], [], [], [], []
    for cell in CELLS:
        run = fa.run_dir("test", arm, cell)
        t = run / "transcript-00.ndjson"
        _, _, state = fa.audit_vep.load(t)
        table, _ = fa.audit_vep.audit(t)
        _, alighted = fa.sweep_analyze.event_times(t)
        req = {r["requestId"]: r for r in state["requests"]}
        prof = dl.profile(fa.day_of(cell), cell[-3:], "causal-no15") if disp else None
        first = {}
        for r, c, s, k, pub, v, e, p, x, cc, z, closed in table:
            if k == "initialPromise":
                first[(r, c)] = (pub, p)
        for (r, c), (pub, p) in first.items():
            if r not in alighted:
                continue
            shown = dl.display(pub, p, prof) if prof else p
            if c == "drop":
                a = alighted[r] - shown
                late.append(a / 60000)
                door = alighted[r] - req[r]["arrivalTimeMs"]
                rel.append(a / door)
                wait.append((req[r]["actualPickupTimeMs"] - req[r]["arrivalTimeMs"]) / 60000)
                ride.append((alighted[r] - req[r]["actualPickupTimeMs"]) / 60000)
            else:
                pick.append((req[r]["actualPickupTimeMs"] - shown) / 60000)
    n = len(late)
    share = lambda xs, t: 100 * sum(1 for x in xs if x > t) / len(xs)  # noqa: E731
    label = f"{arm}{' + display' if disp else ''}"
    out.append(f"\n== {label}: {n} served riders")
    out.append(f"  drop lateness (min): mean {st.mean(late):+.2f}, p50 {q(late, .5):+.2f}, p90 {q(late, .9):+.2f}, p99 {q(late, .99):+.2f}, max {max(late):+.2f}")
    out.append(f"  share late > 1 / 2 / 3 / 5 / 10 min: {share(late, 1):.2f} / {share(late, 2):.2f} / {share(late, 3):.2f} / {share(late, 5):.2f} / {share(late, 10):.2f} %")
    out.append(f"  lateness as share of door-to-door time: share > 5% {share(rel, .05):.2f}%, > 10% {share(rel, .10):.2f}%, > 20% {share(rel, .20):.2f}%")
    out.append(f"  pickup lateness vs first pickup promise (min): mean {st.mean(pick):+.2f}, share > 1 min {share(pick, 1):.2f}%, max {max(pick):+.2f}")
    out.append(f"  wait (min): mean {st.mean(wait):.2f}, p90 {q(wait, .9):.2f}; ride (min): mean {st.mean(ride):.2f}, p90 {q(ride, .9):.2f}")
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
