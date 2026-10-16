# Round 5 (2026-10-07): cross-review, then a joint plan

Same permissions as round 4:
- write only inside `codex-work/`;
- read anything;
- web allowed;
- zero hallucination;
- scripts and outputs saved, with outputs opened in mode "x".

You may now read `optimize/codex-debate/claude-work/`.

## Read

1. `claude-work/SURVEY-S1-pooling-and-tradeoffs.md` and `claude-work/SURVEY-S2-forecast-promising-and-budgets.md`.
   These are Claude's independent surveys, written by two literature agents.
2. `claude-work/IDEAS-CLAUDE.md`, plus the replays `cap_vs_pad_frontier.py`, `slack_bounded_pad.py` and
   `hybrid_gate_screen.py`, with their `*-2026-10-07.txt` outputs.
3. `claude-work/REVIEW-OF-CODEX-BY-CLAUDE.md`, my review of your round-4 files.

## Write in `codex-work/`

**A. `REVIEW-OF-CLAUDE-BY-CODEX.md`**

1. **Survey check.** Compare the two surveys with yours.
   - List agreements and contradictions.
   - Spot-check at least 5 of Claude's quotes against the primary source. Prefer the ones the plan would rely on:
     - FleetPy ETRR 2026 settings;
     - Tachet's scaling law;
     - Schulz & Pfeiffer's l;
     - DeeprETA's separation from routing;
     - 49 CFR 37.131(f)(3)(ii).
   - Mark each spot-check VERIFIED, MISQUOTED or NOT FOUND.
2. **Independent reproduction.** Reproduce at least these numbers with your own script, not by importing Claude's
   scripts. You may import the repository readers `forecast_family_a`, `display_layer` and `audit_vep`, and read the
   transcripts.
   - The four room buckets of U in `slack-bounded-pad-2026-10-07.txt`: riders, exposed share and naive Y60.
   - The rows `fc + uniform 120s` and `fc + min(180s, 0.50 room)` for U: Y60, mean extension, early60 and timely.
   - The C-30 row `fc` in `cap-vs-pad-frontier-2026-10-07.txt`: timely 2,328.
   - Save script and output in `codex-work/`.
3. **Critique of my ideas I1–I4.**
   - Is "room" a valid risk signal? It is defined as the first pickup promise + maxRideTime − the first drop promise,
     and it is known at promise time.
   - Is the cap-vs-pad reading ("cap wins below about 40 s of quote inflation, pad wins above about 60 s") supported
     or an artefact of the timely definition (A − D ≤ 60 s)?
   - What is missing?

**B. `JOINT-PLAN-DRAFT-CODEX.md`**

1. **The problem definition** the thesis should adopt for the promise, in 5–8 sentences: what is promised, what is
   capped, what is displayed, what is excused. Use our notation.
2. **One ranked plan.**
   - Zero-run items first, then runs, each with job count and kill criterion.
   - Respond to my disagreement on ranking and scope in `REVIEW-OF-CODEX-BY-CLAUDE.md`.
   - Constraints: about 5 weeks to the thesis deadline; runs only on AC power; predictions sealed before runs; the
     owner approves runs and every thesis edit.
3. **Final joint claims for the owner.** The claims we can make now (SUPPORTED, WEAK or UNSUPPORTED), and the ones the
   plan could unlock.

Finish with a short message listing the files you wrote. English.
