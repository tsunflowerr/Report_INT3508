from pathlib import Path
import json,re,datetime,collections
OUT=Path(__file__).resolve().parent
KIT=Path('E:/Code/Report_INT3508/ridebound-scratchpad/rewrite-2026-10')
def read(name):return (OUT/name).read_text(encoding='utf-8')
def cite_keys(text):
    text=re.sub(r'(?<!\\)%[^\n]*','',text)
    return {k.strip() for group in re.findall(r'\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}',text) for k in group.split(',') if k.strip()}
tex=read('10-tai-lieu-draft.tex')
assert tex.count('20%.')==1
tex=tex.replace('20%.',r'20\%.')
tex=tex.replace('BIB-VERIFICATION.md','BIB-VERIFICATION-v2.md')
md=read('BIB-VERIFICATION.md').replace('\\\\','\\')
md=md.replace('New York City Taxi \\& Limousine Commission.','New York City Taxi & Limousine Commission.')
md=md.replace('**53 khóa**','**53 khóa**')
resolution=read('HORL-ZWICK-RESOLUTION.md').replace('10-tai-lieu-draft.tex','10-tai-lieu-draft-v2.tex')
now=datetime.datetime.now().astimezone().isoformat()
paths=[KIT/'drafts'/n for n in ['07-chuong3-v3.tex','08-chuong4-phanA-v4.tex','09-chuong4-phanB-v7.tex']]+sorted((KIT/'drafts').glob('06-chuong2*.tex'))
scanned={p.name:sorted(cite_keys(p.read_text(encoding='utf-8'))) for p in paths}
cited={k for keys in scanned.values() for k in keys}
bibkeys=re.findall(r'\\bibitem\{([^}]+)\}',tex)
records=json.loads(read('verified-records-final-v2.json'))
statuses=collections.Counter(r['status'] for r in records)
assert len(records)==53
assert statuses=={'VERIFIED':45,'CORRECTED':7,'CANNOT VERIFY':1}
assert not cited-set(bibkeys)
assert len(scanned['06-chuong2-v4.tex'])==15
assert len(bibkeys)==len(set(bibkeys))==23
table=re.findall(r'^\| `([^`]+)` \| (VERIFIED|CORRECTED|CANNOT VERIFY) \|',md,re.M)
assert len(table)==53 and len(set(k for k,s in table))==53
assert collections.Counter(s for k,s in table)==statuses
assert len(re.findall(r'^\| J\d\d \|',md,re.M))==42
assert re.search(r'(?<!\\)%',re.sub(r'^\s*%[^\n]*','',tex,flags=re.M)) is None
assert tex.count('{')==tex.count('}')
active_tex=re.sub(r'(?<!\\)%[^\n]*','',tex)
assert '\\chapter*{' not in active_tex
assert active_tex.count('\\begin{thebibliography}')==1
assert active_tex.count('\\end{thebibliography}')==1
assert active_tex.count('\\addcontentsline')==1
md+='''
## Bản giao sau kiểm tra cuối

Các tệp dùng để ghép là `BIB-VERIFICATION-v2.md`, `10-tai-lieu-draft-v2.tex` và `HORL-ZWICK-RESOLUTION-v2.md`; ba bản không có hậu tố được giữ nguyên. Bản v2 thoát ký tự phần trăm trong tên trang UberX Share (`20\\%`) để LaTeX không hiểu đó là dấu bắt đầu chú thích; sửa cách ghi lệnh LaTeX trong ghi chú cho dễ đọc. Dữ liệu thư mục, 23 khóa được giữ và các trạng thái kiểm chứng không đổi.

Lần quét lại cuối: '''+now+'''. Bốn tệp Ch2 vẫn là bản đầu, v2, v3, v4; không có khóa mới hoặc thiếu khóa. Kết quả kiểm tra bổ sung lưu ở `final-consistency-output-v2.json`. Không dựng LaTeX theo luật phiên.
'''
outputs={'BIB-VERIFICATION-v2.md':md,'10-tai-lieu-draft-v2.tex':tex,'HORL-ZWICK-RESOLUTION-v2.md':resolution}
for name in outputs:assert not (OUT/name).exists(), 'Refusing overwrite '+name
for name,content in outputs.items():
    with (OUT/name).open('x',encoding='utf-8',newline='\n') as h:h.write(content)
qa={'check_time':now,'files_scanned':scanned,'statuses':dict(statuses),'bibitems':len(bibkeys),'missing_cited_keys':sorted(cited-set(bibkeys)),'unescaped_percent_signs_in_tex':0,'metadata_rows':len(table),'register_mapping_rows':42,'outputs':list(outputs),'all_original_files_preserved':True,'latex_build_run':False}
with (OUT/'final-consistency-output-v2.json').open('x',encoding='utf-8') as h:json.dump(qa,h,ensure_ascii=False,indent=2)
print(json.dumps(qa,ensure_ascii=False,indent=2))
