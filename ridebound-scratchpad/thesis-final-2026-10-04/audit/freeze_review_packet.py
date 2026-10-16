"""Create one immutable, identical manuscript/source packet for three isolated reviews."""
from pathlib import Path
import json,hashlib,shutil
TASK=Path(__file__).resolve().parent.parent
packet=TASK/'review-packet-v1'
packet.mkdir(exist_ok=False)
def copy(src,dest):
    dest=packet/dest;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dest)
copy(TASK/'build'/'main.pdf',Path('thesis_draft.pdf'))
for file in (TASK/'source').rglob('*.tex'):
    copy(file,Path('source')/file.relative_to(TASK/'source'))
for file in (TASK/'source'/'hinh').iterdir():
    if file.is_file():copy(file,Path('source')/'hinh'/file.name)
neutral=['h6-frontier-per-cell-figure-data.csv','h6-frontier-summary-figure-data.csv',
 'h6-raw-movement-recheck.json','service-budget-per-cell.csv','service-budget-summary.csv',
 't38-per-episode-figure-data.csv','t38-raw-checkpoint-recheck.json','t38-actual-trip-id-overlap.json',
 'tier2-gates-figure-data.csv','tier2-recomputed-report.txt','w07-per-cell-own-promise.csv',
 'endpoint-recomputed.txt','literature-crossref-metadata.json','recheck_h6_frontier.py',
 'recheck_t38.py','recheck_wide_service.py','check_trip_overlap.py','build_verified_figures.py',
 'mechanism_figure.py']
for name in neutral:copy(TASK/'audit'/name,Path('evidence')/name)
for file in (TASK/'audit'/'papers').iterdir():
    if file.is_file():copy(file,Path('papers')/file.name)
repo=Path(r'C:\Code\RideBound-noworse')
code=['src/RideBound.Application/Promises/PromiseDeltaCalculator.cs',
 'src/RideBound.Application/Commitments/CommitmentDecisionValidator.cs',
 'src/RideBound.Domain/Commitments/CommitmentBudgetEvaluator.cs',
 'src/RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs',
 'src/RideBound.Algorithms/Candidates/ForwardSlackProfile.cs']
for path in code:copy(repo/path,Path('code')/path)
scratch=TASK.parent
for folder,names in [('deadline',['PREREGISTRATION.md','AMENDMENTS.md','predictions.csv']),
 ('tang3/t38',['T38-PLAN.md','T38-AMENDMENTS.md','split-t38-v1.json','GAMMA-t38-v1.json']),
 ('tang3/w07x',['W07X-PLAN.md'])]:
    for name in names:copy(scratch/folder/name,Path('plans')/Path(folder)/name)
setup='''# Common review criteria and assessment boundary

This is a complete Vietnamese undergraduate thesis in information technology.
Assess defensible contributions, correct mathematical assumptions, traceable empirical
evidence, prior-work boundaries, and readability. Apply the five Nature Reviewer axes
as a disciplined review framework. Do not impose Nature publication fit or journal
word limits. Elementary proofs and engineering contributions are valid at this degree
level if claimed accurately. Maximum final PDF length is80physicalpages;72–78 is a
preferred range, never a reason to pad. Original typography isTimesNewRoman13pt,
one-and-a-halfspacing,leftmargin3cm,othermargins2cm.

Input is thesis_draft.pdf plus its exact source, selected implementation source,
recorded evidence, plans, verified bibliographicmetadata and primarypaper copies.
Evidence scripts are extraction tools. They do not constitute newly independent
experiments. Raw file paths in the evidence anchor the retained original data.
Inspect supplied sources first; official primarysources may be consulted if needed.
The frozen code excerpt is from research/tier3-no-worse,commit24aa747.

Only manuscript/sourcefacts may ground concerns. Read the whole manuscript before
the report. Mark anything notassessable. Every substantive concern must have a stable
ID, claimpointer, evidencepointer and resolutiontest. Separate MajorConcerns and
MinorComments, with BlockingYes only if a central claim is not established until fixed.
Report no concern when none grounded. Also report strengths, intended readers,
five-axis assessment and readiness for an undergraduate defense.

You are an independent internal review context, not a human referee identity.
Never read another review, a shared concern ledger, rootauditreports or synthesis.
Do not modify the packet or thesis. Save one report outside packet in audit/reviews.
Freeze the report before any root synthesis. No quota of concerns.

Preassigned emphasisbriefs
R1(A) originality, closestpriorwork andclaimstrength.
R2(B) experimentdesign, inferentialunit, assumptions andtechnicalvalidity.
R3(C) readability, Vietnamese, terminology, narrativeanddisplays.
All reviewers assess the whole thesis. Emphasis does not exclude other axes.
'''
(packet/'COMMON-CRITERIA.md').write_text(setup,encoding='utf-8')
entries=[]
for file in sorted(packet.rglob('*')):
    if file.is_file():entries.append({'path':str(file.relative_to(packet)),'bytes':file.stat().st_size,'sha256':hashlib.sha256(file.read_bytes()).hexdigest()})
(packet/'MANIFEST.json').write_text(json.dumps(entries,indent=1),encoding='utf-8')
print(json.dumps({'packet':str(packet),'files':len(entries),'pdfSha256':entries[[r['path'] for r in entries].index('thesis_draft.pdf')]['sha256']}))
