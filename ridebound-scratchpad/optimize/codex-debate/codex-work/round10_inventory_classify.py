"""Classify every independently enumerated primary experiment family for debate relevance."""
from pathlib import Path
import csv,json,collections
OUT=Path(__file__).resolve().parent
meta=json.loads((OUT/'data-inventory-codex-corrected-meta-2026-10-08.json').read_text())
with (OUT/'data-inventory-runs-codex-corrected-2026-10-08.tsv').open(encoding='utf-8',newline='') as f:allrows=list(csv.DictReader(f,delimiter='\t'))
lineby={r['evidence_path']:i+2 for i,r in enumerate(allrows)}
used={'C:/RideBoundData/research/tier3-t38-v1':'Rounds4-6 paired policy/forecast analysis','C:/RideBoundData/research/tier3-forecast-v1':'Rounds4-6 forecast runs','C:/RideBoundData/research/tier3-w07-v1':'Development report/results cited in earlier rounds','C:/RideBoundData/research/tier3-w07x-v1':'Development cap nonmonotonicity cited in earlier rounds','E:/RideBoundData/wp14r/development-v6-ledger':'Round9 independent static ladder','E:/RideBoundData/wp9/confirmatory-h6-panela-v2':'Round7 corrected 8-vehicle primary panel','E:/RideBoundData/wp9/confirmatory-h6-panelb-v2':'Round7 corrected 4-vehicle primary panel'}
answers={
'frontier-20260820':('capacity and cap price','Existing 4/8/16 vehicle pilot and capped8-vehicle frontier; capacity saturation and nonmonotone service already observed.'),
'contended-20260819':('capacity and lock/ranking price','Earlier B1/C1 contention pilot; descriptive precursor, not additional confirmation.'),
'load-probe-20260818c':('capacity and service','One B1/C1 load pair; operating-point evidence.'),
'budget-probe-20260819':('budget feasibility','Single tight C1 probe; no controlled population estimate.'),
'pareto-relaxed-20260819':('admission/objective sensitivity','One relaxed C1 pilot; scope limited to the saved configuration.'),
'frontier-v1':('cap tuning and pickup locks','141 saved records across capped/uncapped and pickup-lock/freeze/ratchet controls; planned10-arm grid is incomplete, not a fresh full experiment.'),
'drift-v1':('traffic versus dispatch attribution','Mixed k0/k1/k2 conduct/visible tests; many invariant/admissibility failures, so completed saved records are a selected slice.'),
'drift-frac-v1':('traffic and physical feasibility','Reduced disturbance k0.5 conduct tests; saved feasible subset after strong-disturbance failures.'),
'driftwide-v1':('window slack and attribution','Visible-k0 wide-window pilot; pipeline failures cannot be summarized as a valid full reliability panel.'),
'wide-window-v1':('physical slack and commitment price','20 matched B1/C1 static cells with wider pickup windows; separate service cost sensitivity already available.'),
'levelc-v1':('risk reservation versus hard cap','20 static warning60/hard120 cells; stored completions match the old120 control, not proof of improved prediction.'),
'surface-v1':('pickup slack crossed with cap','80 static jobs in four arms; combined window/cap surface, rather than a lone beta sweep.'),
'ratchet-secondary-v1':('promise consistency metrics','80 static ratchet/freeze variants; secondary revision-direction metrics available.'),
'development-ablation':('static operating point','Only one B1 reference saved; not a completed multiarm development panel.'),
'deadline-v1':('deadline and traffic allowance','165 earlier static/dynamic conduct/deadline records; different configuration/era, useful sensitivity evidence rather than current ML training.'),
'deadline-v1-pilot':('deadline mechanics','One static deadline precursor; implementation evidence only.'),
' tier3-unused-placeholder':('',''),
}
rows=[]
for full,v in meta['experiments'].items():
    family=full.split('/')[-1]
    status='used' if full in used else 'not independently used in prior debate'
    why=used.get(full,'No identified prior quantitative use in reviewed debate files; this is a coverage classification, not proof no one opened the directory.')
    if family in answers:question,answer=answers[family]
    elif family=='tier3-sweep-v1':question,answer='traffic, cap levels and recovery','168 retained directories represent156 intended jobs plus12 reruns; W0-W5 spans artificial and measured worlds on only2 development cells.'
    elif family=='tier3-pilot-v1':question,answer='traffic and promise definitions','60 earlier U/C/M/Mplus/V pilot worlds on2 cells; old runner/configuration, not an expanded current training set.'
    elif family=='tier3-sweep-noworse-v1':question,answer='recovery-rule confounding','28 no-worse reruns (22 treatment and6 control); recovery changes deadline comparisons; retain exact controls and lineage.'
    elif family in ('tier3-vm-v11-a','tier3-vm-v11-b'):question,answer='visible drift and forecast feasibility','24 M/V runs each across worlds; alternative wrapper/configuration, same narrow development cells.'
    elif family.startswith('tier3-world-') or family=='tier3-forecast-checks-v1':
        status='diagnostic';question,answer='causal profile and forecast plumbing','Smoke/leakage/forecast-control evidence; not independent service or reliability replications.'
    elif family.startswith('confirmatory-h5'):
        status='diagnostic/superseded';question,answer='historical implementation bias','Earlier H5 outputs superseded by H6 repair; do not pool for scientific service estimates.'
    elif family in ('confirmatory-h6-panela','confirmatory-h6-panelb'):
        status='duplicate archive lineage';question,answer='reproducibility','Pre-v2 archive of H6 panel; check declared content digests and do not count copied records as independent cells.'
    elif family.startswith('diagnostic-') or family.startswith('post-outcome-') or family.startswith('wp9-007-repeat-'):
        status='diagnostic';question,answer='mechanical validity and repeatability','Targeted debugging/breach/repeat artifacts; outcome-selected, not independent generalization evidence.'
    elif family=='exploratory-b4-repair-v1':question,answer='objective/repair mechanism','One repair-arm control; cannot establish broad service superiority.'
    elif family in ('exploratory-visible-basis-v1','exploratory-visible-sweep-v1'):question,answer='visible versus dispatch budget','16/28 static visible-basis experiments already test alternative burden definitions; incomplete exploratory grids.'
    elif family.startswith('e1-retained-portfolio-panel-'):question,answer='candidate retention and capacity','40-run E1 panels at8/4 vehicles; comparison concerns candidate portfolio, not learned travel time.'
    elif family.startswith('development-v') and family.endswith('-ledger'):
        status='used' if full in used else 'diagnostic/superseded';question,answer='static commitment frontier','V3/V4 short gate attempts and V5 partial pilot precede the completed V6 ladder; keep attempts separate.' if not full in used else 'Completed V6 static ladder already reproduced; main service/sharing versus cap case.'
    elif family=='results':
        status='diagnostic';question,answer='runner and portfolio engineering','WP7 performance/identity runs;3 have no transcripts, so completed counts remain unknown.'
    elif full in used:question,answer='current promise/prediction trade-off',why
    else:question,answer='inspect retained evidence',why
    rows.append(dict(experiment=full,primary_records=v['runs'],debate_use=status,usage_basis=why,open_question=question,what_saved_data_answers=answer,arms=';'.join(v['arms']),windows=';'.join(v['windows']),vehicles=';'.join(v['vehicles']),requests=';'.join(v['requests']),completed_known=v['completed_known'],completed_unknown=v['completed_unknown'],evidence_path=v['example_path'],inventory_line=lineby[v['example_path']]))
assert len(rows)==51
with (OUT/'data-inventory-experiment-classification-2026-10-08.tsv').open('x',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps({'families':len(rows),'classification_counts':dict(collections.Counter(r['debate_use'] for r in rows))},indent=2))
