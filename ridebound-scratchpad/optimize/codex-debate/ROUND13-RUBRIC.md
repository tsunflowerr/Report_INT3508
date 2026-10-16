# Round 13 judging rubric (shared by the Claude-side judge and the Codex-side judge)

Each judge scores the OTHER side's proposals. Inputs: `ROUND13-FACT-PACK.md`, the proposal file being judged and the
survey/evidence files it cites. Strict claim boundary = the owner's newer uncommitted copy
`E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md` (READ ONLY; e.g. around line 56: do not claim as new
detecting unreliability, pre-decision control, or the service–stability trade-off), plus
`C:/Code/RideBound-noworse/docs/03-related-work-and-claim-boundary.md`.

Correction already accepted (Codex R13 verification): in `claude-work/budget-use-check-2026-10-09.txt` the column
"median" is the nearest-rank p50 (e.g. w07 C-30: riders 1.974 s and 10.048 s; conventional median 6.011 s).

## Step 1: verify (mandatory)

For every proposal, check every number or citation that the proposal's case depends on (at least 3 per proposal,
all central numbers). Mark each VERIFIED (you opened the file/URL and saw it), UNVERIFIED (could not open), or WRONG
(contradicted; give the correct value with its anchor). Code claims: open the cited file:line.

## Step 2: score each proposal 1–5 on

1. **Operator value**: evidence that an operator/business would gain (not asserted).
2. **Rider value**: evidence that riders care about the measured quantity, including counter-evidence.
3. **Research value**: would other researchers want to optimize, compare against, or reuse it (a frontier, a
   benchmark, an instrument)?
4. **Novelty within the strict claim boundary**: what remains new after the closest prior work.
5. **Feasibility in ~5 weeks** (deadline unconfirmed): tier T0–T3, effort, number of runs, deadline risk; T2 work
   needs a separate worktree and `dotnet test RideBound.slnx`.
6. **Evidence strength and falsifiability**: a clear prediction and kill criterion; not resting on one event (e.g. a
   single snow afternoon) or on post hoc choices.
7. **Fit to ONE storyline**: the owner wants one direction; does it extend or replace the current one cleanly?

## Step 3: verdict

Per proposal: KEEP / MERGE-WITH(<id>) / REJECT, one-line reason, and the single biggest risk. Then:
- the top 3 of the judged side, ranked;
- anything the judged side MISSED that you would add (new idea allowed; anchor it);
- any overclaim that must be removed before showing the owner.

Write in English, zero hallucination, cite file:line or URL+quote. No simulations, no builds, no installs.
