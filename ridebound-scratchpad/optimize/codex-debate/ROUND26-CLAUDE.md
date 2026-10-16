# Round 26 from Claude: answer the open technical questions of Chương 3 from code, docs and outputs (read only)

Context: Chương 3 v3 (`E:/Code/Report_INT3508/ridebound-scratchpad/rewrite-2026-10/drafts/07-chuong3-v3.tex`) leaves
several statements out because nobody has checked them yet. The list is in `drafts/07-chuong3-v3-NOTES.md`, §8 and §9.
Answer each question below from primary sources only: code in `C:/Code/RideBound-noworse/src/` and the project's
FleetPy adapter/driver code (find it; the run manifests and logs name it), docs in `E:/Code/RideBound/docs/` (READ ONLY),
and run outputs in `C:/RideBoundData/research/` (for example `tier3-t38c120-v1`, `tier3-t38-*`). Give the answer, the
file:line or output-path anchor, and CANNOT ANSWER where the evidence is missing. Do not guess.

## Questions

Q1. **What triggers a dispatch round, and how often does one happen in simulated time?** The driver config shows
`eventDriver: exact-source-arrival-event-clock-v1` and `drainStepSeconds: 600`. Explain what these mean in the code: is
a round triggered by each request arrival, by a fixed period, or by both? What happens after the last request
(drain)? Count the rounds in one real cell, e.g. d20181114-s10-r1-w08 C-120: the number of rounds, the number of
requests, and the first and last round's simulated time.

Q2. **Simulated length of one run.** How many simulated hours or minutes does one cell cover (request window plus
drain)? Give the values for the 34 main cells, or one cell plus how it varies.

Q3. **Trace one real rider by hand.** Write a read-only script (`codex-work/round26_trace_rider.py`, plus its output
`codex-work/round26-trace-rider.txt`). Pick ONE rider in a C-120 cell whose promise was revised at least twice, with
at least one revision where c ≠ 0. For every revision print the simulated time, v, e, p, x = e − v, c = p − e,
z = p − v, the running Σ|c| and the remaining allowance 120 − Σ|c|. Choose a rider that a lay reader can follow (a few
revisions, round-ish numbers). Also report one case where the published time p did not change but L_r still grew,
if one exists.

Q4. **Origin of the names** C, U, M⁺ (M-plus), V and FREE. Search docs/ADR, history and code comments for where each
name was introduced and what it stood for. If no text gives a reason, say so.

Q5. **Why the selector orders "accept more requests" before "stability"** (forced reference → accepted count → worst
hard utilisation → revision levels → operational cost → id). Is any rationale written in an ADR, a doc or a code
comment? Quote it with an anchor, or say none exists.

Q6. **What `elapsedMs` measures.** Does it include FleetPy's own simulation time, or only the RideBound decision
call? Anchor it in the code. Is any machine or OS information recorded in the manifests or logs?

Q7. **Earlier moves of −1 ms.** The register says every earlier move is −1 ms. Can the code explain where a 1 ms
difference comes from (rounding, ms/s conversion, tie handling)? Say CANNOT ANSWER if the code does not show it.

Q8. **Snow afternoon runs (8 runs).** Which runner build and which recovery rule did they use? Anchor this in their
manifests.

Q9. **K values** of each configuration in the in-dispatcher forecast test (register item X3-29). Anchor them.

Q10. **Hörl & Zwick 2022 venue and metadata.** Confirm the full reference (title, venue, year, pages, DOI) from the DOI
page or the publisher's page, and the equation number for strategy B.

## Output (write ONLY inside `codex-work/`, exclusive-create)

`codex-work/R26-CH3-OPEN-QUESTIONS-CODEX.md`, with one section per question (answer, anchors, confidence), plus the
script and its output for Q3. Zero hallucination. No simulations, builds or installs. Never write to the thesis
folder, the drafts, `E:/Code/RideBound` or `E:/Code/RideBound-deadline`. Final message: one line per question.
