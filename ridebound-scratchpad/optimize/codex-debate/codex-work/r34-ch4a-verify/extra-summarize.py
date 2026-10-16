"""Summarize completed own R34 probes, exclusive new small markdown output."""
import collections,json,pathlib
HERE=pathlib.Path(__file__).resolve().parent
def rows(name):
    return [(i,json.loads(line)) for i,line in enumerate((HERE/name).read_text(encoding='utf-8').splitlines(),1)
            if line.startswith('{')]
fixed=rows('extra-probe-output-v2.txt')
remaining=rows('extra-probe-output-v3.txt')
fixed_arms=('b1-ref','c1-nobudget','c1-budget120','c1-budget60','c1-h6ref')
labels=('FREE','U','C-120','C-60','C-30')
fixed_expected=((1629,865,388),(1584,346,62),(1563,303,41),(1540,266,20),(1534,241,6))
morning_expected={
 'U':(665,50,615,656),'C-30':(660,47,613,658),'C-60':(661,47,614,659),
 'C-90':(664,50,614,660),'C-120':(666,51,615,659),'C-150':(666,51,615,659),
 'C-180':(666,51,615,659),'C-240':(665,50,615,656),'C-300':(665,50,615,656)}
lines=['# R34 complementary number checks (second report)',
       '',
       'Read `CODEX-PARALLEL-RULES.md`, `WRITING-BRIEF.md`, ADDENDUM-1 §0, the revised draft and ADDENDUM-4. All writes are exclusive new text files in the authorized subfolder. No simulation, build or install.',
       '',
       'The following statuses concern the assigned complementary numbers, not the master verdict. Line numbers are one-based in `08-chuong4-phanA-v4.tex`.',
       '',
       '## Fixed traffic: AGREE',
       '',
       'Independent raw reading of all 80 transcripts under `E:/RideBoundData/wp14r/development-v6-ledger/`. Sharing is counted with an on-board event sweep on half-open actual pickup/alight intervals; dispatch movement is computed as nonzero published drop ETA minus exogenous drop ETA in a ledger revision. This avoids the reviser’s pairwise overlap implementation and does not import any project analyzer. All parsed relevant frames are hash/length checked.',
       '',
       '| v4 line | Arm | Served | Shared | Dispatch-moved | Own raw output anchor |',
       '|---|---|---:|---:|---:|---|']
for index,(arm,label,expected) in enumerate(zip(fixed_arms,labels,fixed_expected)):
    selected=[(i,r) for i,r in fixed if r.get('group')=='fixed' and r['arm']==arm]
    assert len(selected)==16,(arm,len(selected))
    actual=tuple(sum(r[key] for i,r in selected) for key in ('served','shared','moved'))
    assert actual==expected,(arm,actual,expected)
    assert all(r['requests']==108 and r['moved']==r['moved_all_accepted'] for i,r in selected)
    served,shared,moved=actual
    lines.append(f'| {493+index} | {label} | {served:,} | {shared} ({100*shared/served:.1f}%) | {moved} ({100*moved/served:.1f}%) | `extra-probe-output-v2.txt:{selected[0][0]}–{selected[-1][0]}` |')
lines.extend(['',
 'The draft’s counts and all ten one-decimal percentages agree: shared 865/346/303/266/241 and moved 388/62/41/20/6. Denominators are the respective served cohorts 1,629/1,584/1,563/1,540/1,534. Draft caption lines 483–485 labels this correctly. Existing corroboration: C4A-04, WBU:4/7/10/13/16; those were not substituted for this raw count.',
 '',
 '## Full morning ladder: AGREE',
 '',
 'Own raw reading of U and every C level, 72 transcripts on the same eight morning scenarios. Strict lateness means actual alight time minus the initial published drop ETA exceeds the threshold; “timely” is served minus the strict lateness count. Every run has 108 requests.',
 '',
 '| v4 line | Arm | Served | Late >60 s | Timely ≤60 s | Timely ≤120 s | Own output anchor |',
 '|---|---|---:|---:|---:|---:|---|'])
for arm,expected in morning_expected.items():
    found=[(i,r) for i,r in remaining if r.get('group')=='morning-total' and r['arm']==arm]
    assert len(found)==1,arm
    i,r=found[0];actual=tuple(r[key] for key in ('served','late60','timely60','timely120'))
    assert r['runs']==8 and r['requests']==864 and actual==expected,(arm,r)
    line=529 if arm=='U' else 530 if arm=='C-30' else 531 if arm=='C-60' else 532 if arm=='C-90' else 533 if arm in ('C-120','C-150','C-180') else 534
    lines.append(f'| {line} | {arm} | {actual[0]} | {actual[1]} | {actual[2]} | {actual[3]} | `extra-probe-output-v3.txt:{i}` |')
lines.extend(['',
 'The grouped values at v4 lines 533–534 and the plotted coordinates at lines 643–648 agree. Corroboration: C4A-05 and the older independent CAP:3–11.',
 '',
 '## Morning archived subset: AGREE',
 ''])
found=[(i,r) for i,r in remaining if r.get('group')=='morning-archive'];assert len(found)==1
i,archive=found[0]
assert archive['archived']==192 and archive['chosen']==136 and len(archive['chosen_arms'])==17
assert set(archive['chosen_arms'].values())=={8} and sum(archive['other_arms'].values())==56
lines.extend([f'At v4 lines 128–130, **136 of 192** is correct. Own directory/summary inventory gives 88 morning runs plus 104 extension runs, all succeeded; the chapter selects 17 arms × 8 scenarios = 136. The remaining 56 are '+', '.join(f'{arm}: {n}' for arm,n in sorted(archive['other_arms'].items()))+f'. Anchor: `extra-probe-output-v3.txt:{i-2}–{i}`. This confirms the archived inventory, not a new run. The code corroboration is RW7:33–34 and RW7X:35–36.',
 '',
 '## Snow requests: AGREE',
 ''])
snow=[(i,r) for i,r in remaining if r.get('group')=='snow']
assert len(snow)==8 and all(r['requests']==108 for i,r in snow)
assert sum(r['requests'] for i,r in snow)==864 and sum(r['served'] for i,r in snow)==601
st=[(i,r) for i,r in remaining if r.get('group')=='snow-total'];assert len(st)==1
si,sr=st[0]
lines.extend([f'At v4 lines 134–136, **864 requests** is correct: 8 raw final states × 108; 601 served. Per-run served counts in the probe’s sorted order: '+', '.join(str(r['served']) for i,r in snow)+f'. Own raw anchors: `extra-probe-output-v3.txt:{snow[0][0]}–{snow[-1][0]}` and total at line {si}. Existing corroboration: C4A-06 / INV:14–15,17–22.',
 '',
 '## “B14 (1.075)” in round brief: AGREE on number; identifier correction',
 ''])
found=[(i,r) for i,r in remaining if r.get('group')=='budget-rejection'];assert len(found)==1
i,bd=found[0]
expected={'has-record:completed':116,'has-record:rejected':32,'no-record:completed':111,'no-record:rejected':1075}
assert bd['counts']==expected and bd['runs']==34,(bd,expected)
lines.extend([f'At v4 lines 449–454, the group with no recorded budget-block evidence is **1,186 = 111 served by U + 1,075 rejected by U**. The group with recorded evidence is **148 = 116 served by U + 32 rejected by U**. Own raw 34-scenario probe (C-30’s repaired 14/11 r3 w17 run used) agrees exactly: `extra-probe-output-v3.txt:{i}`. The scan collects request IDs from a pruned candidate only when its code and a commitment witness both say `COMMITMENT_BUDGET_EXCEEDED`, then crosses with raw final lifecycle states.',
 '',
 'The brief calls the 1,075 claim B14, but its evidence ID is **D13**; main-register B14 is initial-promise length (14.15 vs 14.12 min), assigned elsewhere. The draft correctly cites D13 at line 454. No thesis correction is required for this typo in the brief. The v4 wording “không có bản ghi chặn nào được ghi” and its explicit caution at lines 451–452 are justified; no recorded witness does not establish a structural-only cause.',
 '',
 '## Extra snow scope check',
 '',
 'Both `optimize/snow/worlds/W5-d20181115-w14.json:1` and `...w15.json:1` explicitly set **sigma = 0.0 and shockRate = 0.0**. `optimize/run_forecast.py:85–87` selects them; line 133 passes the selected file as `RB_WORLD_CONFIG`. This supplies source evidence for the intended no-noise snow configuration relevant to v4 lines 65–69. `run_forecast.py:94–102` passes the C-30 commitment config and the common WP4 config; `tang3/configs/wp4-tier3-v2.json:7` enables `no-worse-than-reference-v1` recovery.',
 '',
 'Saved read-only source probe: `extra-snow-scope-v2.py` → `extra-snow-scope-output-v2.txt` (exit 0). It also opens all eight raw initialization manifests: masterSeed 7, policyVersion `tier3-exploratory-v1`, and the same policyConfigurationHash `a2f11a3ada0773f9b30b85c56c935058e2e931f13c907f46b2ddfff8c1285f1c`. Their manifests contain no world-file hash; this source check does **not** constitute a binary audit of the snow runner. The retained “Chưa kiểm lại” caveat at v4 lines 135–136 remains appropriate.',
 '',
 '## Probe completion/provenance',
 '',
 '`extra-probe.py`/its header-only output were interrupted before aggregates. `extra-probe-v2.py` saved all 80 fixed runs, then stopped on a short adapter-frame prefix; those completed fixed rows remain valid. `extra-probe-v3.py` repairs that prefix handling and probes only the remaining morning/snow/budget subjects. It exits 0 when complete. All files were preserved; no existing file was overwritten.',
 '',
 '**No numerical corrections identified in these assigned complementary checks.** All completed results are AGREE; no assigned numeric item remains CANNOT CHECK.'])
with (HERE/'extra-findings-v2.md').open('x',encoding='utf-8',newline='\n') as handle:handle.write('\n'.join(lines)+'\n')
print('Created extra-findings-v2.md; all assigned complementary values AGREE.')
