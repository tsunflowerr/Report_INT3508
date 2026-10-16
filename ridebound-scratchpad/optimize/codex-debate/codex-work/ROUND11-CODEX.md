# Round 11 — reproduction passes; provenance gate fails

Independent code reproduces **all 95 E=30 metric rows and 665 numerical cells at the published three-decimal precision**, with no mismatch. Every value is in [the reproduced table](round11-reproduce-reported-formula-metrics.tsv); [cell comparisons](round11-reproduce-comparison.tsv), [calibration coefficients](round11-reproduce-calibration.tsv), and [code](round11-reproduce-independent.py) provide the audit trail.

| Prediction | Verdict | Reproduced result |
|---|---|---|
| ML1 | TRUE | C-30 HGB Y60 gain: 0/0 pp on November 15/16. |
| ML2 | FALSE | U gains: 8.276/2.500 pp versus uniform; 0.690/0.000 versus fc+uniform; guards fail. |
| ML3 | FALSE | FREE gain: 1.239 pp; positive in both windows, but threshold and guards fail. |
| ML4 | TRUE | No fixed learner jointly matches C-30’s Y60 and symmetric accuracy. |
| ML5 | FALSE | Full/state-ablated Y60 gains coincide; predictions need not coincide. |

The numerical kill criterion fires. Reconstructing targets from timestamps instead of the CSV’s rounded fields produces 36 differing metric cells: maximum changes are 0.359 s mean extension, 2.434 s p90 extension, and 1 pp early/symmetric accuracy; Y60 and all verdicts remain unchanged ([sensitivity](round11-reproduce-rounding-sensitivity.json)). This qualifies numerical precision, not the primary reproduction.

Extraction checks pass for the concrete timing/features specification: 10,064 rows, 112 expected unique run cells, no missing/extra cells or duplicate rider keys, matching CSV hash, and one effective run per cell. All fixed November 12+13 profile calculations pass. Splits match: measured fitting November 12/13, calibration 14, separate tests 15/16; static fitting November 12 replicas 1–3, calibration replica 4, testing November 13 replicas 1–4, both windows. I checked **23 rows across 23 runs**, exceeding the requested 20: all 299 numeric comparisons and independently reconstructed assigned/onboard states agree, using the first published serviceOrder and source-ordered events; 49,427 frame hashes verify ([v3 evidence](round11-extraction-audit-codex-v3.tsv), [audit](round11-extraction-audit-codex-v3.json)).

**Material protocol failure:** the seal claims unchanged adoption, but the [accepted source-group gate](ML-PILOT-REVIEW-CODEX.md:15) requires purging fitting/calibration source-trip duplicates. Independent source-to-runtime mapping proves **11 original trips retained in both splits in each of five static arms: 55 arm-pairs**. For example, original trip 3212940 appears in FREE fitting CSV line 2697 and calibration line 2837; the full source-row hashes match despite different runtime IDs ([mapped witnesses](round11-extraction-provenance-mapped-codex.tsv)). This proves a bypassed provenance gate, not identical simulated labels or a quantified bias. The pilot is numerically reproducible but fails the originally agreed protocol; no purge/refit was performed here.

Analysis implements rho=(E−mean(delta))/mean(w), nonnegative weights, infeasibility and zero-weight fallback, both controls, frozen test application, all four WIN guards, strict late/early boundaries, inclusive symmetric accuracy, and nearest-rank p90 correctly. Claude omitted the required common-completed supplement; my frozen-quote comparisons supply U/C-30 intersections of 141/192 riders, FREE/C-30 748, and LOCKS/C-30 761, with no learner jointly matching C-30 ([paired metrics](round11-reproduce-common-pairwise.tsv)).

E=30 equalizes calibration extension, not realized test cost: U HGB averages 41.624/35.565 s versus C-30 fc+uniform 36.717/31.952 s; static FREE HGB averages 29.392 s versus C-30 30 s. Static FREE/LOCKS/C-30 complete 807/792/772 of 864 requests, so coverage also differs.

The thesis may report an exploratory retrospective result: these fixed learners with simple features achieved no qualifying gain over their controls, and none jointly matched C-30’s late-tail and symmetric reliability on own or paired cohorts. Fielbaum and Alonso-Mora’s two remedies are usefully compared, but “fewer changes beats better predictions at equal quote cost, in these worlds” overstates the evidence because test costs and service coverage differ and the agreed provenance gate failed. Few days, small test cohorts of 145–807 riders, fixed learners, simple features and simulated worlds prevent general claims about ML or real-world dominance.
