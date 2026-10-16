# Round 14 from Claude: you are the Codex-side judge of Claude's proposals

The independence rule of round 13 is now lifted for the files below. A Claude-side judge is scoring your round-13
proposals in parallel; do not read its output (`claude-work/R13-JUDGE-OF-CODEX-BY-CLAUDE.md`) in this round.

## Read

1. The shared rubric, to follow exactly: `E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/ROUND13-RUBRIC.md`.
2. What you judge: `claude-work/R13-PROPOSALS-CLAUDE.md`, and the Claude evidence it cites:
   `claude-work/R13-PAPERS-CLAUDE.md`, `claude-work/R13-SURVEY-CLAUDE.md`, `claude-work/R13-ML-DATA-CLAUDE.md` (with its
   samples folder `claude-work/r13-ml-data-samples/`), `claude-work/wp14r-budget-use-2026-10-10.txt`, and any helper
   outputs under `claude-work/r13-proposer/`.
3. Context: `ROUND13-FACT-PACK.md`, your own round-13 files, earlier rounds, the handoff, the run data, the repo
   `C:/Code/RideBound-noworse` (read only), the owner's papers `C:/PDF/Paper/`.
4. Strict claim boundary: the owner's newer uncommitted copy `E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md`
   (READ ONLY; never write there), around line 56.

## Do

- Follow the rubric's three steps for every Claude proposal: verify the central numbers, quotes and code claims
  (VERIFIED / UNVERIFIED / WRONG with the correct value); score the 7 criteria with one-line justifications; give the
  verdict KEEP / MERGE-WITH / REJECT and the biggest risk; list Claude's top 3, what Claude missed, overclaims to remove.
- Check Claude's external quotes that carry weight (value-of-reliability numbers, patents, product guarantees,
  Mt-KaRRi, Fielbaum & Alonso-Mora freeze results, Schulz & Pfeiffer) against the primary source where you can open it.
- Then add a short section "Cross-side comparison": put every proposal from BOTH sides (yours from round 13 and
  Claude's) into one ranked list of at most 8 items with your reasons, merging duplicates. Say which of your own
  round-13 proposals you would now withdraw or change after reading Claude's.

## Output (write ONLY inside `codex-work/`, exclusive-create)

- `codex-work/R14-JUDGE-OF-CLAUDE-BY-CODEX.md`.
- Helper scripts, if any, also in `codex-work/`.

Rules: zero hallucination, cite `file:line` or URL + quote; no simulation runs, no builds, no installs into shared
environments. Finish with a short final message listing the files written.
