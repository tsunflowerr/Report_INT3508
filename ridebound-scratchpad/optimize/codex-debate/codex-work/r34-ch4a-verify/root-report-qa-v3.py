"""Read-only final coverage check of R34 review v2; exclusive QA output."""
from pathlib import Path
import re
D=Path(__file__).parent
report=D/'R34-CH4A-V4-VERIFY-CODEX-v2.md'
text=report.read_text(encoding='utf-8-sig')
checks={}
checks['verdict']= '**Verdict: ACCEPT WITH CORRECTIONS.**' in text
checks['ten_R25_status_rows']=len(re.findall(r'^\| \d+\. .*\| \*\*(FIXED|PARTLY|NOT)\*\*',text,re.M))==10
checks['all_brief_numeric_topics']=all(x in text for x in (
 '292/2.338','289/2.338','**2.268**','**2.336**','23.027,239 / 31.353,407',
 '81,742 / 6.891,526','4.836,281 / 12.450,223','865/346/303/266/241',
 '388/62/41/20/6','**8 × 108 = 864**','**136**','192','**7/3/1**',
 '**660,057 s → 660,1**','**232,288 s → 232,3**','14,14644243',
 '14,11600228','**1.075**','**61/15/0**','**0/20.760**'))
checks['four_rejections']=all(x in text for x in ('D11:','D-c2:','G1-r2:','G1-t:'))
checks['code_and_data_reuse']=all(x in text for x in ('RunnerSession.cs:1012','HardVectorCandidateAssessor.cs:252','B460–461','C4A-11'))
checks['nine_ranked_corrections']=len(re.findall(r'^### [1-9]\. ',text,re.M))==9
checks['all_morning_arms']=all('| '+x+' |' in text for x in ('U','C-30','C-60','C-90','C-120','C-150','C-180','C-240','C-300'))
checks['successful_main_probe']= (D/'main-numbers-v4.txt').read_text(encoding='utf-8').rstrip().endswith('every initial-promise ledger rider completed')
checks['successful_extra_probe']= '"all_parsed_relevant_frames_sha256_verified": 96527' in (D/'extra-probe-output-v3.txt').read_text(encoding='utf-8')
checks['source_anchors_early_repaired']='B293–295' in text and 'A579 and B296–298' not in text
checks['prior_master_preserved']=(D/'R34-CH4A-V4-VERIFY-CODEX.md').exists()
checks['no_passenger_blame_wording']='có khách phá hạn chót' not in text
assert all(checks.values()),checks
with (D/'root-report-qa-output-v3.txt').open('x',encoding='utf-8',newline='\n') as f:
    for k,v in checks.items(): f.write(f'{k}: {"PASS" if v else "FAIL"}\n')
    f.write(f'report_bytes={report.stat().st_size}\n')
    f.write('This checks artifact coverage and saved-probe completion, not LaTeX rendering or source equivalence.\n')
print('All final review coverage checks passed; original files retained.')
