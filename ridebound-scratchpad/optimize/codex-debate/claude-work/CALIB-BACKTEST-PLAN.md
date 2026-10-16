# Calibration backtest plan (joint plan step 1). Sealed before the run, 2026-10-07

This plan is a zero-run replay of the saved T3.8 test runs, arms U and C-30. It follows
`codex-work/JOINT-PLAN-DRAFT-CODEX.md` §3 item 1, adapted as noted below.

**Labels.**
- This is a chronological backtest, not a fresh holdout.
- These days were already inspected, and an in-sample screen exists (`slack-bounded-pad-2026-10-07.txt`,
  `chrono-promise-rule-2026-10-07.txt`).

## Rule families

Each rule sets the first drop quote F = P0 + λ·(D0 − P0) + q.
- λ ∈ {0, 1}.
- D0 is the causal-no15 forecast display.
- In the formulas below, P0 − t0 is the initial drop horizon; direct = maxRideTimeMs / 1.5.

| family | q | parameters |
|---|---|---|
| none | 0 | — |
| uniform | b | b ∈ {15, 30, 45, 60, 90, 120, 180} s |
| horizon | a·(P0 − t0) | a ∈ {0.02, 0.04, 0.06, 0.08, 0.10, 0.15, 0.20} |
| direct | a·direct | a ∈ {0.05, 0.10, 0.15, 0.20, 0.30, 0.40} |
| room | min(b, a·room) | a ∈ {0.25, 0.5, 1}, b ∈ {30, 60, 90, 120, 180} s |

## Selection, fixed in advance

1. For each arm, family and budget E ∈ {15, 30, 60} s, look at the TRAIN riders and keep the rules whose mean
   extension (F − P0) is ≤ E.
2. Among those, pick the rule with the most timely riders (A − F ≤ 60 s).
3. Break ties by the smaller mean extension, then the smaller p90 extension.
4. Freeze the rule and evaluate it unchanged on each TEST day separately.

**Folds.**
- Train 14/11, test 15/11 and test 16/11 separately.
- Second fold: train 14+15/11, test 16/11.
- Report 15/11 knowing it is the incident (snow) day.

**Test metrics.**
- Late shares: Y30, Y60, Y120.
- early60: share with A − F < −60 s.
- two-sided60: share with |A − F| ≤ 60 s.
- Mean and p90 extension.
- Timely count.

## Sealed predictions

- **P1.** For U, at E = 30 s and E = 60 s, the frozen room rule has a lower test Y60 than the frozen uniform rule on
  both 15/11 and 16/11 (fold 1).
- **P2.** For U, the room rule does **not** beat the better of the horizon and direct rules by more than 0.5 pp of Y60
  on either test day. I expect room to behave mostly like a trip-length proxy.
- **P3.** For C-30, at E = 15 s the frozen rule has λ = 1, and its test Y60 is ≤ 0.5% on both test days.

## Kill criterion (Codex's, adopted)

A room-specific predictive claim stays only if all three hold:
1. the frozen room rule lowers late share on **both** forward weekday evaluations within the budget;
2. it improves on the horizon and direct controls;
3. it does not raise early60 or two-sided error by more than 1 pp.

Otherwise the room-specific superiority claim is removed, and only the descriptive calibration frontier is kept.
