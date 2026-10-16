# Round 13 from Claude: independent proposals on value, optimization and direction

Read first: `E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/ROUND13-FACT-PACK.md` (neutral facts,
the owner's six questions O1-O6, the constraints). You may read anything you used in rounds 1-12, the handoff
`E:/Code/Report_INT3508/BAN-GIAO-PHIEN-2026-10-09.md`, the research repo `C:/Code/RideBound-noworse`, the run data, and
`C:/PDF/Paper/*.pdf`.

**Independence rule.** Claude-side agents are doing the same task in parallel. Do NOT open any file in
`codex-debate/claude-work/` whose name starts with `R13-` until a later round asks you to. (Older claude-work files are
fine, and so is `claude-work/budget-use-check-2026-10-09.txt`.)

## Tasks

1. **Verify the two new facts** in fact-pack section 2 (O1 run existence; O4 budget-use table) from the raw
   transcripts with your own code. Report MATCH / MISMATCH per row.
2. **Read the owner's papers** in `C:/PDF/Paper/`, especially the example thesis `21020283-3476 (1).pdf` (broken
   Vietnamese diacritics in text extraction; figure/table captions and numbers are still readable). For each paper:
   one line on what it says that bears on O2/O3/O6, with a page or line anchor. Identify what "optimizing one part of
   the pipeline for a useful trade-off" looks like in the example thesis (what was optimized, against what baseline,
   which metrics).
3. **Survey (web, live).** Find primary evidence on:
   - (a) business value of promise/ETA reliability for ride-hailing, ride-pooling, delivery, transit: conversion,
     cancellation, retention, complaints/refunds, willingness to pay, value of reliability; operator guarantees
     (late-arrival credits, arrival guarantees, reserve products);
   - (b) whether researchers treat promise stability / reliability / "decision-induced" change as an objective or
     constraint to optimize (who, how, with what trade-off curves);
   - (c) alternative promise forms: interval/window promises, probabilistic or quantile promises, guaranteed arrival
     with compensation, tiered products (pay more for a guarantee), pickup-only promises, notification budgets;
   - (d) public data that could train or test ML for pooled-trip timing or traffic profiles over many weeks (e.g. NYC
     TLC high-volume FHV records with shared-ride flags and request/on-scene/pickup/dropoff timestamps, Chicago TNP
     trips with pooled flags, NYC taxi Oct-Nov 2018): exact fields, time resolution, whether they contain a promised
     time (they probably do not), and what a thesis could legitimately learn from them.
   Quote short verified passages; give URLs; mark anything you could not open.
4. **Propose directions** that answer O2, O3, O5, O6. Write at most 8 proposals, ranked, ALWAYS including
   "P0 = keep the current storyline unchanged" as an honest baseline option. For each proposal give:
   - one-sentence idea; which owner question it answers;
   - who benefits (operator / rider / researcher) and the cited evidence for that benefit;
   - what is new vs the closest prior work (cite); what must NOT be claimed;
   - evidence already in hand (paths) vs new evidence needed;
   - feasibility tier T0-T3, estimated effort (hours of work, number of runs) under a ~5-week deadline;
   - a falsifiable prediction and the result that would kill it;
   - how it changes the single storyline (replace / extend / unchanged).
   At least one proposal must be of the "optimize one algorithm in our pipeline for a measurable trade-off" kind
   (the owner's example), and at least one must address "promise a different kind of thing". Be creative, but every
   factual claim must be anchored.
5. **Answer O2 and O3 directly** in plain words: what an operator gains from rule C alone, what it gains from rule C +
   forecast, what can honestly be said about what riders care about, and whether this is a real contribution. Include
   the weakest point a thesis committee would attack.

## Output (write ONLY inside `codex-work/`, files opened in exclusive-create mode)

- `codex-work/R13-SURVEY-CODEX.md` — sources and quotes (tasks 2-3).
- `codex-work/R13-PROPOSALS-CODEX.md` — task 1 verification table, tasks 4-5.
- Any scripts you use, also in `codex-work/`.

Rules: zero hallucination, cite `file:line` or URL + quote; no simulation runs, no builds; mark unverifiable items.
Finish with a short final message listing the files written.
