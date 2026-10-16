"""R13 final judge, read-only: per-run breakdown of 'cumulative-only' budget-pruned candidates (see
cumulative_decisive_check.py) for the WP14r C-60/C-120 and synthetic C-120 runs, so that a re-run duplicate
(sweep '-rerun1' folder) can be told apart.  Usage: python -B per_run_cumulative_only.py <out.txt> (mode "x")."""
import pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import cumulative_decisive_check as c  # noqa: E402


def label(path):
    p = pathlib.Path(path)
    return p.parents[2].name if p.parent.name == "output" else p.parent.name


def main():
    out = sys.argv[1]
    lines = ["# per_run_cumulative_only.py: runs with >= 1 cumulative-only budget-pruned candidate"]
    for job in c.jobs():
        if not (job[0].startswith("synthetic") or (job[0].startswith("WP14r") and job[1] in ("C-60", "C-120"))):
            continue
        r = c.analyze(job)
        if r["decisions_with_cumulative_only"]:
            lines.append(f"{job[0]} | {job[1]} | {label(job[2])} | cumulative-only candidates {r['candidates'].get('cumulative-only')} | "
                         f"decisions {r['decisions_with_cumulative_only']} | new requests {r['requests_with_cumulative_only_candidate']} | "
                         f"finally rejected {r['of_which_finally_rejected']} | served {r['served']}/{r['requests']}")
    text = "\n".join(lines) + "\n"
    with open(out, "x", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
