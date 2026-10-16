# Round 16 from Claude: the owner challenges the round-13–15 conclusion

Read first: `ROUND16-FACT-PACK.md` (the owner's questions Q1–Q6 and the facts) and `ROUND16-REVIEW-STANDARD.md` (strict
conference/journal reviewer standard). Paths are under
`E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/`.

**Three debaters this round:** you (Codex), Claude-side agents, and Antigravity (Gemini 3.8 Flash, high), which writes
into `antigravity-work/`. **Independence:** do NOT open `claude-work/R16-*`, `claude-work/r16-*` or `antigravity-work/`
in this round; a later round will ask you to rebut them.

## Tasks

1. **Answer Q1–Q5 independently**, as a strict reviewer would, with anchors. In particular:
   - Q1: say plainly whether a better direction exists than "keep storyline + zero-run chapter (+ optional cost-first
     study)". If your honest answer has changed since R15, say so and why.
   - Q2: from EXISTING data only, estimate what loosening the cap does (served riders, lateness vs first promise,
     with/without forecast, budget use, cumulative binding), and state exactly what is missing to answer it on the
     34-cell T3.8 panel. You may compute from existing transcripts with your own code.
   - Q3: is the cumulative clause effectively inert in this thesis? What regime would make it matter (load, cost-first
     selection, longer trips, larger B), and is any existing run already in that regime?
   - Q4: what would cost-first selection under the same hard gates most likely change, given the code
     (`C:/Code/RideBound-noworse/src/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs`) and the FREE vs
     LOCKS evidence? Separate prediction from evidence.
   - Q5: design the FAIREST feasible way to improve forecasting for unpredictable days (e.g. same-day nowcasting from
     delivered snapshots, weather-conditioned or analog-day profiles from multi-year NYC TLC trips rebuilt with the
     Syed et al. 2021 factor method, regime detection with quote widening, damped trend). Specify: information
     available at quote time (no leakage), training years and test days, how to get more than one incident test day
     (offline factor-forecast benchmark on many historical days vs new simulator days), the evaluation metric at equal
     quote cost, and effort. Assess the owner's specific idea of using the 2013 Manhattan taxi data of Fielbaum &
     Alonso-Mora 2020 (note they chose an off-peak window to disregard traffic; consider domain shift 2013→2018).
2. **Propose at most 3 directions** (one may be "keep") that would survive a strict reviewer, each with novelty vs
   closest prior work, the decisive experiment, sealed-style prediction + kill rule, effort, and whether it replaces or
   extends the storyline.
3. **Review the current thesis core as a strict reviewer** (scores per criterion, overall recommendation, the 3 most
   damaging questions).

## Output (write ONLY inside `codex-work/`, exclusive-create)

`codex-work/R16-CODEX.md` (+ helper scripts/outputs in `codex-work/`). Zero hallucination; no simulations, builds or
installs into shared environments. Finish with a short final message listing files and your one-paragraph answer to
Q1.
