# Round 21B from Claude: fix the archived-folder resolution and run the Stage 1a analysis once more

Your R21 run (`codex-work/R21-STAGE1A-CODEX.md`) refused correctly: it opened a failed original C-30 folder instead of
the passing rerun. T3.8 had infrastructure reruns whose folders carry a `-rerun1` suffix; the owner's resolver is
`tang3/t38/t38_calibrate.py` (`effective()`, used by `optimize/forecast_family_a.py:57-60` `run_dir("test", arm, cell)`),
and your own R15 inventory (`codex-work/R15-audit.json`) lists the 34 passing U / C-30 / M⁺-30 transcripts with hashes.

## Do

1. Create `codex-work/R19-stage1a-analyze-v4.py` from v3, changing ONLY how archived arm folders are resolved (use the
   R15 inventory paths and hashes, or an independent reimplementation of `effective()`, and assert that each resolved
   archived run has status pass and the R15 transcript SHA-256). Keep every other gate unchanged. Record the diff
   v3 → v4 in your report.
2. Run v4 exactly once (≤ 2 processes). Report what R21-CLAUDE.md asked: P1–P5 with values, the C-120 row next to U
   and C-30 (served; naive late > 60/120/300 s; timely ≤ 60/120 s per 3,672; causal-no15 forecast versions; quote
   extension; early > 60 s; exposed; ≥ 2 changes; max Σ|c|; prune records step vs cumulative-only; forced decisions;
   overlaps; per-window served/late60/timely60), and a plain reading under the R18 wording rules.

A Claude-side agent computes the same independently; do not read `claude-work/R21-*` this round.

Output: `codex-work/R21B-STAGE1A-CODEX.md` plus the analyzer's JSON/MD (exclusive-create, only in `codex-work/`). No
simulations, builds or installs.
