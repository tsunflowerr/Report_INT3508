"""Per-rider dispatch-budget use on the WP14r v6 ladder (fixed traffic, 16 cells, denser pooling than T3.8).
Same metrics as budget_use_check.py (imported, unchanged). Arms: b1-ref (free), c1-nobudget (locks = U),
c1-budget120, c1-budget60, c1-h6ref (30 s). Usage: python -B wp14r_budget_use.py <out.txt> (mode x)."""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import budget_use_check as bu  # noqa: E402

ROOT = pathlib.Path("E:/RideBoundData/wp14r/development-v6-ledger")
ARMS = (("b1-ref", None), ("c1-nobudget", None), ("c1-budget120", 120), ("c1-budget60", 60), ("c1-h6ref", 30))


def main(out):
    text = ["# wp14r_budget_use.py: per-rider dispatch-budget use, WP14r v6 (fixed traffic, w08 + w17, 16 cells)", ""]
    for arm, budget in ARMS:
        runs = [r / "attempt-01" / "output" for r in sorted(ROOT.glob(f"w14-*-{arm}-s7"))
                if (r / "attempt-01" / "output" / "transcript-00.ndjson").exists()]
        text += bu.summarize(f"wp14r {arm}", budget, runs)
    body = "\n".join(text) + "\n"
    with open(out, "x", encoding="utf-8", newline="\n") as fh:
        fh.write(body)
    print(body)


if __name__ == "__main__":
    main(sys.argv[1])
