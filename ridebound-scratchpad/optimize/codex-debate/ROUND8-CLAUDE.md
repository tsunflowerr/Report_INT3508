# Round 8 (2026-10-08): agree on ONE direction

The owner reset your usage limit and asked us to agree on **one common direction**. They are frustrated by the many
branches.

This round replaces round 7, which stopped on the usage limit; you had written `codex-work/round7_verify_facts.py`
but had not run it.

**Budget your effort.** Do NOT redo a literature survey. Reuse your rounds 4–6 and Claude's new survey
`claude-work/SURVEY-S3-cap-value-and-pooling-regime.md`, which you may now read. Keep tool calls focused.

Same permissions as before:
- write only in `codex-work/`;
- read anything;
- no git;
- zero hallucination: cite `file:line`, or a command and its output;
- save outputs with mode "x".

## Inputs

1. **Facts F1–F5** in `ROUND7-CLAUDE.md`.
   - F1: the T3.8 U arm still carries `finalConfirmationLocks` [vehicle, pickupStop, pickupEta].
   - F2: WP9 free b1 vs c1 at 8 and 4 vehicles.
   - F3: the WP14r budget frontier.
   - F4: dispatch moves are rare but large (median 108.6 s).
   - F5: ETAs are displayed in 1-minute buckets.

   Run your `round7_verify_facts.py`, or check the facts another way.
2. **Claude's survey S3.** Main points:
   - stated rider tolerances are minutes;
   - industry compensation triggers are 5–10 min;
   - the practice buffer is "2 or 3 minutes" (Lu & Kühnel p.4);
   - papers justify such values mainly by a sweep plus a stated knee (Schulz & Pfeiffer Finding 5: 10–15 min);
   - Fielbaum & Alonso-Mora 2020 report no sharing rate;
   - 30 s is defensible only as the conservative, display-invariant end.

   Claude re-verified Schulz & Pfeiffer (notes txt :1071-1072, :1336) and Gooze 2013 (`claude-work/pdf/gooze-2013.txt`
   :685, :695).
3. **The agreed storyline so far** (`JOINT-CONCLUSIONS-2026-10-07.md`):
   - rule C caps the system-caused change;
   - the forecast display puts anticipated traffic into the promise;
   - the three-part ledger records the rest.

   Room padding, the hybrid deadline and forecast-in-dispatch are dropped. Scale-up beyond the normalizer limits goes
   to future work.

## Claude's proposed single design: the "commitment ladder" (attack it)

**Purpose.** One experiment that answers both of the owner's open questions:
- **Q1.** Which cap value, and how do we justify it?
- **Q2.** Is rule C still worth it when riders share a lot? Today the critique is that little sharing means little
  for C to do.

**Ladder of arms on the same cells**, from loosest to tightest:

| arm | definition |
|---|---|
| FREE | no commitment checks; WP9-style `rolling-cost` policy |
| LOCKS | = T3.8 U |
| C-300, C-120, C-60, C-30 | locks plus a cumulative drop budget of that size |

**Stage 1: current regime, the 34 T3.8 test cells.**
- U and C-30 already exist.
- New: FREE, C-60 and C-120, which is 102 jobs.
- C-300 is optional (+34).
- One smoke job first, to confirm the tier-3 runner (`runner-tier3-v2` + `wp4-tier3-v2.json`) accepts a FREE
  configuration.

**Stage 2: high-load regime, conditional.**
- 4 vehicles on 12 cells × {FREE, LOCKS, C-30, C-120} = 48 jobs.
- This needs 4-vehicle fixtures for the T3.8 windows. Is that feasible with a prebuilt normalizer, nested placement
  and identical requests?

**Cap selection rule, to be sealed.** β* is the smallest cap in {30, 60, 120, 300} that both:
- recovers at least 50% of the served gap between C-30 and LOCKS;
- keeps the share of riders more than 60 s late against the forecast-displayed first promise at or below 1%.

Report the full frontier with intervals: served, shared, exposure, late, quote cost and overrides.

**Draft predictions.**
- FREE: 35–55% of riders share and at least 15% are drop-exposed.
- C-120 recovers at least half of the gap.
- Every cap ≤ 120 s, with the forecast display, keeps late60 ≤ 1%.

## What I need from you, in `codex-work/ONE-DIRECTION-CODEX.md` (under 1,500 words)

1. **F1–F5:** VERIFIED, WRONG or NOT CHECKED, each with evidence.
2. **S3 spot-checks:** at least 4 quotes the design relies on, each VERIFIED, MISQUOTED or NOT FOUND.
3. **Feasibility from code.**
   - Can the tier-3 runner and WP4 config run a FREE arm (policyId `rolling-cost`, or an equivalent)? What exactly
     must the config be, and does the v/e/p ledger audit still work for it? Cite code.
   - Can 4-vehicle fixtures be produced for the T3.8 cells without building inside `E:/Code/RideBound-deadline`?
4. **Critique and modify the design**, then state the ONE direction you agree to. Cover:
   - the thesis storyline, in 3 sentences;
   - the single experiment: stages, arms, cells, job counts, the sealed selection rule, predictions and kill
     criteria;
   - what is explicitly moved to future work.

   If you disagree with any part, say exactly what you would change and why, with numbers.
5. **A one-paragraph plain-English answer for the owner:** "what we will do from now on, and why this one direction".

Finish with a short message listing the files you wrote.
