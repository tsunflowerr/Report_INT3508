# Independent check: Tier 2 drift switch timing

- Script: `E:\Code\Report_INT3508\ridebound-scratchpad\tang3\pilot\independent\verify_tier2_switch.py` (from scratch; no author module imported)
- Input: `E:\Code\Report_INT3508\ridebound-scratchpad\deadline\logs\runs`; run at 2026-09-25 11:41:09 local
- Step j = the j-th `[drift] t=` line (0-based), nominal j*900 s. Shares compared at 3 dp (as claimed); all other numbers exactly. Medians are `statistics.median` (mean of the two middle values when even).

## Verdicts

- MATCH: (a) runs with > 1 switch line: claimed `196`, computed `196`
- MATCH: (a) switches (step >= 1): claimed `865`, computed `865`
- MATCH: (a) median lag (s): claimed `22`, computed `22`
- MATCH: (a) max lag (s): claimed `210`, computed `210 at conduct-30-k1-d20181117-s10-r2-s7 step 1, dl-120-k1-d20181117-s10-r2-s7 step 1, dl-30-k1-d20181117-s10-r2-s7 step 1, dl-60-k1-d20181117-s10-r2-s7 step 1, visible-30-k1-d20181117-s10-r2-s7 step 1`
- MATCH: (a) share of switches with lag > 60 s (3 dp): claimed `0.147`, computed `0.147 (127/865 = 0.14682080924855492)`
- MATCH: (b) (group, step) comparisons: claimed `208`, computed `208`
- MATCH: (b) max spread (s): claimed `70`, computed `70`
- MATCH: (b) where the max spread is: claimed `k1-d20181114-s10-r1-s7 step 4`, computed `k1-d20181114-s10-r1-s7 step 4`
- MATCH: (b) median spread (s): claimed `0`, computed `0.0`
- MATCH: (b) share of comparisons with spread > 60 s (3 dp): claimed `0.014`, computed `0.014 (3/208 = 0.014423076923076924)`

## Input facts

- files in runs/: 296; non-.log files: none; unparsed .log names: none
- runs after the rerun rule: 296; `-rerunN` logs found: none (deadline/AMENDMENTS.md A4 says the five A2 reruns wrote their stdout under the ORIGINAL log name, so the rule is a no-op here and those five logs are the rerun logs)
- families: {'conduct-30': 36, 'ctl-conduct': 20, 'ctl-visible': 20, 'dl-120': 56, 'dl-30': 56, 'dl-60': 56, 'dl2-30': 16, 'visible-30': 36}
- first-line returncode over the chosen logs: {'0': 165, '1': 131} (returncode 1 = run stopped early; such runs are included, as the definition asks for every run with > 1 switch line)
- switch-line count distribution: {1: 100, 2: 52, 3: 31, 4: 19, 5: 5, 6: 7, 7: 5, 8: 7, 9: 70}
- logs whose line index differs from floor(t/900): 0; logs whose first switch line is not t=0: 0
- groups (keys): 56; groups with >= 2 families: 56
- the max-spread comparison, switch time per family: conduct-30: 3736; dl-120: 3666; dl-30: -; dl-60: -; visible-30: -

## Side variants (informational; not the claimed definitions)

- comparisons restricted to steps EVERY family of the group reached: 76, max spread 16 s, median 0.0 s
- per-comparison lag of the latest family (max t - step*900) over the 208 comparisons: median 25.0 s, max 210 s
- same latest-family lag over the 76 every-family-reached comparisons: median 22.5 s, max 210 s
- The T3.7 report section 2.1 cites Tier 2 as 'trễ trung vị 22,5 s, lớn nhất 210 s ... lệch giữa các họ lớn nhất chỉ 16 s, trung vị 0 s, trên 76 lần đổi bước' and section 0 says 'lệch giữa các họ <= 16 s'; compare those figures with the lines above.

