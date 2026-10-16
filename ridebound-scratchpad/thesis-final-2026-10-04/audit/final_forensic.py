"""Post-review editorial audit. Reads saved evidence; launches no experiments."""
from pathlib import Path
import csv, hashlib, json, math, re, sys

ROOT = Path(__file__).resolve().parents[1]
A = ROOT / 'audit'
sys.path.insert(0, str(ROOT / 'runtime'))
import pymupdf

checks = []
def check(aid, desc, actual, expected, unit, source, tolerance=1e-8):
    ok = abs(actual - expected) <= tolerance if isinstance(actual, (float, int)) else actual == expected
    checks.append(dict(audit_id=aid, status='passed' if ok else 'confirmed_internal_error',
                       check=desc, result=actual, expected=expected, unit=unit,
                       evidence_pointer=source, reviewer_overlap='editorial audit; not reviewer consensus'))
    assert ok, (aid, actual, expected)

h6 = json.loads((A/'h6-frontier-recheck.json').read_text(encoding='utf-8'))
for arm in h6['arms']:
    rows = [r for r in h6['runs'] if r['arm'] == arm['arm']]
    for key in ['served', 'publications', 'decisionMs', 'visibleMs', 'unchangedMs', 'requests']:
        check(f'H6-{arm["arm"]}-{key}', 'Sum of recorded per-cell values', sum(r[key] for r in rows), arm[key], key, 'h6-frontier-recheck.json')
    check(f'H6-{arm["arm"]}-ratio', 'Pooled decision/visible ratio', 100*arm['decisionMs']/arm['visibleMs'], arm['ratioDecisionVisiblePercent'], '%', 'h6-frontier-recheck.json')
b1, c1 = h6['arms'][0], next(r for r in h6['arms'] if r['arm']=='c1')
check('H6-loss', 'Completion loss divided by all arrivals', 100*(b1['served']-c1['served'])/2160, 7.12962962962963, 'percentage points', 'h6-frontier-recheck.json')
check('H6-primary-verdict', 'Loss exceeds the frozen 1 pp maximum', 100*(b1['served']-c1['served'])/2160 > 1, True, 'FAIL preserved', 'evidence-audit.md; H6 freeze')
service = list(csv.DictReader((A/'service-budget-summary.csv').open(encoding='utf-8')))
for row in service:
    check(f'WIN-{row["windowSeconds"]}-{row["arm"]}', 'Served loss at the stated window and denominator', 100*(int(row['baselineServed'])-int(row['served']))/int(row['requests']), float(row['lossPp']), 'percentage points', 'service-budget-summary.csv')

t38 = json.loads((A/'t38-raw-checkpoint-recheck.json').read_text(encoding='utf-8'))
s, runs = t38['summary'], t38['runs']
check('T38-runs', '15 calibration plus 34 paired test cells times five arms', len(runs), 15+34*5, 'runs', 't38-raw-checkpoint-recheck.json')
check('T38-revisions', 'All checked drop revisions summed', sum(r['revisionCount'] for r in runs), s['revisionCount'], 'revisions', 't38-raw-checkpoint-recheck.json')
cal = [r for r in runs if r['phase']=='calib']
ctest = [r for r in runs if r['phase']=='test' and r['arm']=='C-30']
check('T38-gamma', 'Order statistic ceil((15+1)*0.9)=15', sorted(r['scoreMs'] for r in cal)[math.ceil(16*.9)-1], s['gammaMs'], 'ms', 't38-raw-checkpoint-recheck.json')
check('T38-bound', 'beta+gamma', 30000+s['gammaMs'], s['visibleBoundMs'], 'ms', 't38-raw-checkpoint-recheck.json')
check('T38-score-cover', 'Number of C test cells below gamma', sum(r['scoreMs']<=s['gammaMs'] for r in ctest), 32, 'of 34 cells', 't38-raw-checkpoint-recheck.json')
check('T38-visible-cover', 'Number below actual visible bound', sum(r['maxVMs']<=s['visibleBoundMs'] for r in ctest), 33, 'of 34 cells', 't38-raw-checkpoint-recheck.json')
check('T38-exceedance', 'Actual visible bound exceedance', max(r['maxVMs'] for r in ctest)-s['visibleBoundMs'], 233, 'ms', 't38-raw-checkpoint-recheck.json')
check('T38-C-max', 'Maximum conduct ledger across all 49 C runs', max(r['maxCMs'] for r in cal+ctest), 29239, 'ms', 't38-raw-checkpoint-recheck.json')
for arm, summary in s['arms'].items():
    rows = [r for r in runs if r['phase']=='test' and r['arm']==arm]
    check(f'T38-{arm}-served', 'Completed lifecycle count', sum(r['served'] for r in rows), summary['served'], 'riders', 't38-raw-checkpoint-recheck.json')
    check(f'T38-{arm}-mean-own', 'Unweighted mean of 34 cell fractions', sum(r['ownBrokenShare'] for r in rows)/34, summary['meanOwnBrokenShare'], 'fraction', 't38-raw-checkpoint-recheck.json')
    check(f'T38-{arm}-pooled-own', 'Pooled count divided by pooled denominator', sum(r['ownBrokenCount'] for r in rows)/sum(r['ownBrokenDenominator'] for r in rows), summary['pooledOwnBrokenShare'], 'fraction', 't38-raw-checkpoint-recheck.json')
    check(f'T38-{arm}-mean-forced', 'Unweighted mean of decision fractions', sum(r['forcedShare'] for r in rows)/34, summary['meanForcedShare'], 'fraction', 't38-raw-checkpoint-recheck.json')
check('T38-service-pp', '96/all test arrivals', (2434-2338)/3672*100, s['gapServicePp'], 'percentage points', 't38-raw-checkpoint-recheck.json')
check('T38-service-relative', '96/U completions', (2434-2338)/2434*100, s['gapRelativeToUPercent'], '% relative', 't38-raw-checkpoint-recheck.json')
overlap = json.loads((A/'t38-actual-trip-id-overlap.json').read_text(encoding='utf-8'))
check('T38-overlap', 'Sum of unique shared trip IDs by source day', sum(r['overlap'] for r in overlap['byDay']), 75, 'original trips', 't38-actual-trip-id-overlap.json')
check('T38-source-days', 'Distinct source days in overlap audit', len(overlap['byDay']), 5, 'days', 't38-actual-trip-id-overlap.json')

w07 = list(csv.DictReader((A/'w07-per-cell-own-promise.csv').open(encoding='utf-8')))
for arm, mean_expected, pooled_expected in [('Mplus-30',24.036980941247,156/660*100),('Mplus-60',7.250466450153,47/661*100)]:
    rows = [r for r in w07 if r['arm']==arm]
    check(f'W07-{arm}-mean', 'Mean of eight cell shares, not pooled share', sum(float(r['ownBrokenShare']) for r in rows)/8*100, mean_expected, '% unweighted cell mean', 'w07-per-cell-own-promise.csv')
    check(f'W07-{arm}-pooled', 'Sum broken riders divided by sum promised riders', sum(int(r['ownBrokenCount']) for r in rows)/sum(int(r['ownBrokenDenominator']) for r in rows)*100, pooled_expected, '% pooled riders', 'w07-per-cell-own-promise.csv')
report=(A/'tier2-recomputed-report.txt').read_text(encoding='utf-8')
block=report.split('stage\twindow\tarm\tk\tcell')[1].split('## 2.')[0]
lines=block.splitlines()[1:]
preds=[dict(zip(['stage','window','arm','k','cell','tau_s','ref_T_s','ref_C_s','far','weak','prediction','outcome','correct'],line.split('\t'))) for line in lines if line.startswith(('2a\t','2b\t'))]
for aid, stage, window, num, den in [('T2-main','2a','w08',98,102),('T2-morning','2b','w08',31,32),('T2-evening','2b','w17',40,40)]:
    rows=[r for r in preds if r['stage']==stage and r['window']==window and r['weak']=='False']
    check(aid+'-den', 'Strong prediction rows excluding predeclared weak cases',len(rows),den,'predictions','tier2-recomputed-report.txt')
    check(aid+'-num', 'Correct strong prediction rows',sum(r['correct']=='yes' for r in rows),num,'predictions','tier2-recomputed-report.txt')
rows=[r for r in preds if r['stage']=='2a' and r['arm']=='dl-30' and r['k']=='1']
check('T2-Mplus-fail', 'Main variable-world Mplus-30 commitment rejection count', sum(r['outcome'].startswith('commitment-all-rejected') for r in rows),19,'of 20 runs','tier2-recomputed-report.txt')

frozen = {}
expected = dict(A='5b716e6cbcd842c6c2c4b98cc639ca5f82929298afea187751df9398a42471c2', B='851a84a7f0a3b992b34fb9ab37d708d309b838317a7799d7958beff6fd463d08', C='3cae59193c84d01ecfefe0370dee32b809e887a3f3446b63a62b4a98d7a1521a')
for letter, sha in expected.items():
    p=A/'reviews'/f'reviewer-{letter}.md'
    got=hashlib.sha256(p.read_bytes()).hexdigest()
    check(f'REVIEW-{letter}', 'Frozen report preserved before editorial audit', got, sha, 'SHA256', str(p))
    frozen[letter]=got
(A/'reviews'/'frozen-reports.json').write_text(json.dumps(frozen, indent=2), encoding='utf-8')

pdf = Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'build'/'main.pdf'
doc=pymupdf.open(pdf)
numeric=[]
for page_i,page in enumerate(doc,1):
    text=page.get_text()
    for m in re.finditer(r'\d+(?:[.,]\d+)*(?:\s*/\s*\d+)?(?:\s*%|\s*(?:ms|giây|phút|khách|ô|trang|nút|xe))?', text):
        numeric.append(dict(page=page_i, value=m.group(), context=' '.join(text[max(0,m.start()-85):m.end()+85].split())))
with (A/'all-numbers-final-pdf.csv').open('w', encoding='utf-8-sig', newline='') as out:
    w=csv.DictWriter(out, fieldnames=['page','value','context']);w.writeheader();w.writerows(numeric)
# Central recurring numbers, with every PDF occurrence and nearby context.
metrics = {
 'H6 decision/visible B1 ratio %':['89,06','89.06'],
 'H6 decision/visible C1 ratio %':['1,37','1.37'],
 'H6 service loss pp':['7,13','7.13'],
 'Tier2 commitment-failure contrast':['19/20','0/20'],
 'Tier2 sealed predictions':['98/102','31/32','40/40'],
 'W07 mean own-deadline %':['24,04','7,25'],
 'T38 source-trip overlap':['75 chuyến','75\nchuyến'],
 'T38 C max seconds':['29,239'],
 'T38 gamma/bound seconds':['222,259','252,259'],
 'T38 score/actual bound coverage':['32/34','33/34'],
 'T38 relative versus rate gap':['2,61','3,94'],
 'T38 mean own violation %':['14,5','4,2','21,6'],
 'T38 forced mean %':['41,3','22,5','53,8'],
}
positions=[]
for metric, variants in metrics.items():
    found=[]
    for i,page in enumerate(doc,1):
        txt=page.get_text()
        for v in variants:
            for m in re.finditer(re.escape(v),txt):
                found.append(dict(page=i,value=v,context=' '.join(txt[max(0,m.start()-65):m.end()+95].split())))
    positions.append(dict(metric=metric,all_locations=found))
(A/'numerical-consistency.json').write_text(json.dumps(positions,ensure_ascii=False,indent=2),encoding='utf-8')
with (A/'numerical-consistency.csv').open('w',encoding='utf-8-sig',newline='') as out:
    w=csv.writer(out);w.writerow(['Metric','all PDF locations','values and contexts'])
    for p in positions:w.writerow([p['metric'], ', '.join(str(x['page']) for x in p['all_locations']), json.dumps(p['all_locations'],ensure_ascii=False)])
(A/'forensic-consistency.json').write_text(json.dumps(dict(pdf=str(pdf),pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),pages=len(doc),checks=checks),ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(checks=len(checks),passed=len(checks),pages=len(doc),numeric_occurrences=len(numeric),central_metrics=len(metrics))))
