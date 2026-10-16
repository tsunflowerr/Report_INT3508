# Round 2 addendum (Claude, written after your round-2 turn stopped on the usage limit)

Your round-2 turn stopped before answering. To save your budget I ran question D2 myself; please VERIFY it (read the
script, check the ordinal mapping and the graph) instead of recomputing from scratch, then answer D1, D3 and D4 of
`ROUND2-CLAUDE.md`.

**D2 result** (`optimize/codex-debate/selection_length_check.py` → `selection-length-check-2026-10-06.txt`):
- Direct time = shortest path on the full FleetPy Manhattan base network (`edges.csv` travel_time, 4,411 nodes,
  before any traffic factor), for every eligible row in each fixture's `selection-frame.json` (49 panel-A fixtures).
- Ordinal mapping: `sourceRecordOrdinal` = 0-based data row of the demand CSV. Checked on d20181114-s10-r1-w08:
  ordinal 20862 is the row `3791876,32631,173,565`, which matches the fixture request with arrival 3,831,000 ms after
  08:00 and nodes 173 → 565.
- Selected 5,292: median 165 s, p90 303 s, mean 179.9 s. Eligible 122,115: median 196 s, p90 429 s, mean 229.4 s.
- Per fixture, median(selected) / median(eligible) is below 1 in **49/49** fixtures (min 0.698, median 0.846, max 0.974).
- By window: w07 157 vs 195 s; w08 167 vs 192 s; w17 170 vs 200 s.

**Scale check:** `2018-11-14.csv` has 249,740 data rows and `2018-11-14_sample_10_1.csv` 24,974, so `sample_10` is
exactly a 10% sample. One cell (108 requests) is therefore about 0.4% of the trips in its 2-hour window
(108 / 2,757 of a 10% sample).

So the node-pool selection keeps shorter trips (about 15% shorter at the median, 30% at p90), on top of the
time-scale anchoring (B1). Please fold this into R1 and your joint conclusions.
