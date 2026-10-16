# Round 16 brief for Antigravity (Gemini 3.8 Flash, high)

You are one of three independent debaters (with OpenAI Codex and Anthropic Claude) reviewing an undergraduate thesis,
RideBound: reliable promised drop-off times in ride-pooling, simulated with FleetPy on Manhattan (Nov 2018 NYC taxi
demand). Your answer will be checked line by line by the other two; unanchored claims will be discarded.

## Read (all in `inputs/` of this folder)

1. `ROUND16-FACT-PACK.md` — the owner's questions Q1–Q6 and the established facts. **Start here.**
2. `ROUND16-REVIEW-STANDARD.md` — judge as a strict reviewer at a top transportation / operations research venue.
3. `R13-FINAL-VERDICT.md` — the previous final verdict (sections A–E; section C is in Vietnamese).
4. `R15-CONFIRM-CODEX.md` — Codex's corrections to that verdict (they override its wording).
5. `BAN-GIAO-PHIEN-2026-10-09.md` — Vietnamese handoff with all earlier results (sections 3–5).

## Task

Answer the owner's questions Q1–Q5 from the fact pack, as a strict reviewer:
- Q1: is there a better direction than "keep the storyline + one zero-run results chapter (+ optional cost-first
  selection study)"? Say yes or no, and why.
- Q2: would loosening the cap so the 1,256 single-step budget rejections become feasible be better? Use only numbers
  in the inputs.
- Q3: is the cumulative part of rule C effectively inert? What would make it matter?
- Q4: what would cost-first selection likely change?
- Q5: how to improve the forecast for unpredictable days (e.g. a snow afternoon) FAIRLY: methods, data (including the
  owner's idea of using 2013 Manhattan taxi data from Fielbaum & Alonso-Mora 2020, and multi-year NYC TLC data),
  information available at quote time, test design, effort.
Then propose at most 3 directions with: novelty vs the closest prior work, the decisive experiment, a falsifiable
prediction and kill rule, effort in hours/runs, and whether it replaces or extends the storyline.

## Rules (strict)

- Use ONLY facts from the input files or from web pages you actually open; cite the file and section (or URL and a
  short quote). If you are unsure, write "UNVERIFIED". Do not invent numbers, papers, authors or years.
- Distinguish measured results, screens, inferences, hypotheses and opinions.
- Do NOT run terminal commands, do NOT install anything, do NOT edit or create any file except the single output
  file below. Do not open or modify anything outside this folder.

## Output

Write your full answer (English, Markdown) to ONE new file in this folder: `R16-ANTIGRAVITY.md`.
End the file with a line `END OF ANTIGRAVITY R16`.
