"""Sub-label table per (panel, arm, k, window) over the effective outputs of every stage, and the
citation form of every commitment-infeasible failure. Read-only."""
import collections
import json

import classify
import run_deadline as rd

table = collections.defaultdict(collections.Counter)
citations = collections.Counter()
for stage in ("controls", "2b-conduct", "2a-base-conduct", "2a", "2b-rest", "2a-base-visible"):
    for job, arm, k, panel, cell in rd.jobs(stage):
        directory = rd.effective_output(job)
        label = classify.classify_output(directory)
        window = "w17" if cell.endswith("w17") else "w08"
        name = "A" if panel is rd.PANEL_A else "dev"
        table[(name, arm, k, window)][label] += 1
        failure = directory / "failure-00.json"
        if failure.exists() and classify.is_commitment_infeasible(label):
            message = json.loads(failure.read_text(encoding="utf-8"))["failureMessage"]
            citations[classify.citation_of(message) or "noop-rejected-path"] += 1
for key in sorted(table, key=str):
    print("\t".join(str(v) for v in key), dict(sorted(table[key].items())))
print("citation forms among commitment-infeasible failures:", dict(citations))
