from pathlib import Path
import json, re, datetime, collections
OUT=Path(__file__).resolve().parent
KIT=Path('E:/Code/Report_INT3508/ridebound-scratchpad/rewrite-2026-10')
DRAFTS=KIT/'drafts'
inputs=['agent-core-v2.json','agent-legacy-v2.json','agent-legacy-extra-v2.json','agent-followup-v2.json','root-references-v2.json']
rows=[r for name in inputs for r in json.loads((OUT/name).read_text(encoding='utf-8'))]
assert len(rows)==len({r['key'] for r in rows}), 'Duplicate keys'
bykey={r['key']:r for r in rows}
bykey['schulz2026']['status']='VERIFIED'
bykey['schulz2026']['notes']='All existing metadata correct; add missing issue2 as a verified completion, not an error. '+bykey['schulz2026']['notes']
for r in rows:
    r['tex']=r['tex'].replace('?.','?').strip()
    r['metadata']=r['metadata'].replace('?.','?')
    r.setdefault('body_status','BIBLIOGRAPHIC METADATA ONLY')

mapping={}
for n in range(1,6):mapping[f'J{n:02}']=['horl2022']
for n in range(6,10):mapping[f'J{n:02}']=['fielbaum2020']
mapping.update(dict(J10=['schulz2026'],J11=['schulz2026'],J12=['elmi2026'],J13=['haferkamp2024'],J14=['ackermann2025'],J15=['tellez2022'],J16=['wang2026'],J17=['alonsomora2017'],J18=['engelhardt2026'],J19=['syed2021'],J20=['gardner1985'],J21=['leonardi2024'],J22=['lu2024'],J23=['wardman2026'],J24=['alonsogonzalez2020'],J25=['molenbruch2017'],J26=['kovacs2014','sridharan1987'],J27=['cohen2022'],J28=['uberxshare'],J29=['uberdelayed2026'],J30=['lyftscheduled'],J31=['moiaexpress'],J32=['laupichler2026'],J33=['yu2022'],J34=['lyftpatent2024'],J35=['hu2022','doordash2024'],J36=['ecfr37131'],J37=['watkins2011'],J38=[],J39=[],J40=['gschwind2019'],J41=['ding2025'],J42=['schmidt2026']))
assert set(mapping)=={f'J{n:02}' for n in range(1,43)}
planned_ids={'J01','J03','J05','J06','J07','J08','J09','J10','J11','J12','J16','J17','J18','J21','J22','J23','J24','J25','J28','J31','J32','J33','J35','J41'}
planned_keys={k for j in planned_ids for k in mapping[j]}
def cite_keys(text):
    text=re.sub(r'(?<!\\)%[^\n]*','',text)
    return sorted({k.strip() for group in re.findall(r'\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}',text) for k in group.split(',') if k.strip()})
base=['07-chuong3-v3.tex','08-chuong4-phanA-v4.tex','09-chuong4-phanB-v7.tex']
paths=[DRAFTS/n for n in base]+sorted(DRAFTS.glob('06-chuong2*.tex'))
inventory={'scan_time':datetime.datetime.now().astimezone().isoformat(),'files':[{'path':p.as_posix(),'keys':cite_keys(p.read_text(encoding='utf-8'))} for p in paths]}
inventory['cited_keys']=sorted({k for f in inventory['files'] for k in f['keys']})
latest_ch2=next(f for f in inventory['files'] if f['path'].endswith('06-chuong2-v4.tex'))
inventory['latest_ch2_keys']=latest_ch2['keys']
inventory['active_keys']=sorted({k for f in inventory['files'] if not Path(f['path']).name.startswith('06-') or f is latest_ch2 for k in f['keys']})
inventory['planned_keys']=sorted(planned_keys)
legacy=re.findall(r'\\bibitem\{([^}]+)\}',Path('E:/Code/Report_INT3508/ridebound/noi-dung/10-tai-lieu.tex').read_text(encoding='utf-8'))
retain=set(inventory['cited_keys'])|planned_keys
assert retain<=set(bykey),'Missing verified records '+str(retain-set(bykey))
assert set(legacy)<=set(bykey),'Missing legacy verification'
assert not {k for k in retain if bykey[k]['status']=='CANNOT VERIFY'},'Cannot include unverified bibliography identity'
drop=sorted(set(legacy)-retain)
order=['alonsomora2017','fielbaum2020','horl2022','schulz2026','elmi2026','laupichler2026','wang2026','engelhardt2026','ortools','molenbruch2017','leonardi2024','lu2024','hu2022','doordash2024','wardman2026','alonsogonzalez2020','yu2022','uberxshare','moiaexpress','ding2025','tlc','kovacs2014','sridharan1987']
assert set(order)==retain
counts=collections.Counter(r['status'] for r in rows)
inventory['retained_keys']=order
inventory['legacy_drop_candidates']=drop
inventory['status_counts']=dict(counts)

heading=r'''% Bản dự thảo vòng 32, ngày 13/10/2026; đưa vào mẫu report hiện tại bằng \input.
% Không thêm \chapter* trước môi trường này: thebibliography tự tạo tiêu đề chương.
% Mẫu DACN chia theo ngôn ngữ. Tập nguồn hiện tại không có mục tiếng Việt;
% vì vậy chỉ in nhóm Tiếng Anh, không tạo nhóm trống hoặc thêm nguồn ngoài phạm vi.
\renewcommand{\bibname}{Tài liệu tham khảo}
\begin{thebibliography}{99}
\phantomsection
\addcontentsline{toc}{chapter}{\bibname}
\setlength{\itemsep}{5pt}

\item[]\textbf{Tiếng Anh}
'''
tex=heading+'\n\n'.join('% EV: '+(', '.join(bykey[k]['register_ids']) or 'nguồn sơ cấp trong BIB-VERIFICATION.md')+'\n'+bykey[k]['tex'] for k in order)+'\n\n\\end{thebibliography}\n'
tex=tex.replace('\\\\input','\\input').replace('\\\\chapter','\\chapter')
texkeys=re.findall(r'\\bibitem\{([^}]+)\}',tex)
assert texkeys==order and len(texkeys)==len(set(texkeys))
assert all(k in texkeys for k in latest_ch2['keys'])
assert tex.count('\\begin{thebibliography}')==tex.count('\\end{thebibliography}')==1
assert '\\chapter*{' not in re.sub(r'%[^\n]*','',tex)
assert tex.count('\\addcontentsline')==1
assert tex.count('{')==tex.count('}')

def cell(text):return str(text).replace('|','\\|').replace('\n',' ')
def links(value):
    urls=re.findall(r'https?://[^\s;()]+',value)
    return '<br>'.join('[mở nguồn]('+u+')' for u in urls)
def disposition(key):
    if key in inventory['active_keys']:return 'Đang trích'
    if key in inventory['cited_keys']:return 'Ch2 cũ; giữ theo phạm vi quét'
    if key in planned_keys:return 'Dự kiến trong đề cương'
    if key in legacy:return 'Cân nhắc bỏ'
    return 'Chỉ lập bản đồ sổ'
md=['# Kiểm chứng thư mục vòng 32','',
    'Ngày kiểm: 12–13/10/2026; lần quét cuối: '+inventory['scan_time']+'. Các bản ghi do phiên chính và hai phiên phụ kiểm trên nguồn sơ cấp; phiên chính đọc toàn bộ dữ liệu bàn giao, đối chiếu các sửa đổi và khóa trước khi ghép. Tệp cũ được giữ nguyên.',
    '',f'Tổng **{len(rows)} khóa**: **{counts["VERIFIED"]} VERIFIED; {counts["CORRECTED"]} CORRECTED; {counts["CANNOT VERIFY"]} CANNOT VERIFY**. Trạng thái ở bảng dưới nói về nhận dạng và dữ liệu thư mục; việc đã đọc nội dung được ghi riêng. Thêm số kỳ, DOI hoặc ngày truy cập còn thiếu mà không thay dữ kiện sai được tính là VERIFIED.',
    '',f'Quét đủ **{len(paths)} tệp**: ba tệp Ch3/Ch4 được chỉ định và bốn tệp `06-chuong2*.tex`. Hợp của mọi bản Ch2 có **{len(inventory["cited_keys"])} khóa**; dùng riêng Ch2-v4 với ba tệp còn lại có **{len(inventory["active_keys"])} khóa**. Ch2-v4 có **15 khóa**, đều có trong dự thảo. Tệp đầu tiên của phiên bị ngắt chưa thấy Ch2; lần này đã quét lại ở đầu và cuối.',
    '', '## Phạm vi và lựa chọn','',
    f'Dự thảo có **{len(retain)} mục**: hợp các khóa được trích trong phạm vi tệp mà brief yêu cầu và các nguồn được đề cương dự kiến. `kovacs2014` và `sridharan1987` chỉ còn ở Ch2 bản đầu/v2; giữ chúng vì brief yêu cầu quét mọi `06-chuong2*.tex`. Nếu chỉ ghép Ch2-v4, có thể bỏ hai mục này và còn 21 mục. Không thay khóa `laupichler2026` bằng tên bộ điều phối Mt-KaRRi; không tạo khóa thứ hai cho cùng bài.',
    '', 'Nguồn Uber cho J35 được đại diện bằng `hu2022`; nguồn DoorDash dùng `doordash2024`. `deepeta2022` là bản ghi đối chiếu, không thêm một mục blog trùng vai trò. Các nguồn chỉ có trong J01–J42 nhưng không được dự kiến trong các hàng Ch1–Ch2 hoặc mục tài liệu tham khảo được kiểm và lập bản đồ, không tự thêm vào danh mục.',
    '', '## Một dòng cho mỗi khóa','',
    '| Khóa | Trạng thái | Dữ liệu thư mục cuối | URL đã mở | Vai trò và ghi chú |','|---|---|---|---|---|']
for r in sorted(rows,key=lambda x:x['key']):
    metadata=r['metadata']
    doi=re.search(r'https://doi.org/([^}\s]+)',r['tex'])
    if doi and doi.group(1) not in metadata:metadata+=' DOI '+doi.group(1)+'.'
    md.append('| `'+r['key']+'` | '+r['status']+' | '+cell(metadata)+' | '+links(r['url'])+' | '+cell(disposition(r['key'])+'; '+r['notes']+' Nội dung: '+r['body_status'])+' |')
md+=['','## Đối chiếu 15 khóa của Ch2-v4','',
    'Đối chiếu độc lập với `06-chuong2-BIB.md` và C2-01…24: '+', '.join('`'+k+'`' for k in latest_ch2['keys'])+'. Tất cả nhận dạng thư mục có nguồn sơ cấp đọc được. Các sửa đổi trong ghi chú của người viết về tác giả Alonso-González và năm in Molenbruch là đúng. Tên hội nghị của Hörl–Zwick được bổ sung từ ETH IVT, ngoài dữ liệu DataCite mà người viết Ch2 đã dùng. `schulz2026` được bổ sung số kỳ 2, `engelhardt2026` số kỳ 1; đây là dữ kiện bổ sung, không đổi nhận dạng.',
    '', 'DeeprETA: đúng bốn tác giả theo thứ tự, đúng arXiv:2206.02127v1 và ngày 05/06/2022; không có dòng chỉ bản tạp chí trên trang arXiv. Đọc cả bản HTML chính thức xác nhận phép hiệu chỉnh giờ đến của bộ tìm đường và phân vị cho giờ hiển thị. Đường dẫn blog DeepETA đúng trong bảng đối chiếu hiện mở được; việc URL khác từng chết không làm thay đổi giá trị của nguồn `hu2022`.',
    '', 'Các dòng C2 về mã, dữ liệu và kết quả mô phỏng không phải mục thư mục; vòng này không xác nhận lại C2-22/23 hoặc mọi số thực nghiệm. Bảng thư mục không tự nâng một câu nội dung chỉ vì DOI đúng.',
    '', '## Các nội dung còn thiếu hoặc cần giữ đúng phiên bản','',
    '- **J16 / `wang2026`:** nhận dạng thư mục VERIFIED; toàn văn không mở được. Không nâng câu cụ thể về lịch tham chiếu và cơ chế không làm khách tệ hơn từ UNVERIFIED. Có thể giữ mục dự kiến trong thư mục, nhưng chưa đưa các chi tiết đó vào thân bài.',
    '- **J12 / `elmi2026`:** đã đọc độc lập bản xuất bản cuối ở các trang 5, 12, 13; độ chùng sau lần gán đầu và cơ chế chọn khách nhận độ chùng bằng không được xác nhận. C2-08 không còn phụ thuộc chỉ vào văn bản ranh giới.',
    '- **J41 / `ding2025`:** phiên phụ đã mở bản gốc TUM 24 trang; trang 7 xác nhận dữ liệu đầu vào và giá trị dịch vụ thực hiện của FleetPy dùng cho học. Trang TUM xác nhận hội nghị TRB 2025, khác ngày bản thảo 12/11/2024. Phiên chính đọc dữ liệu bàn giao; lần thử mở lại ở phiên chính bị chặn, không phải phủ định lần mở thành công của phiên phụ.',
    '- **J36 / `ecfr37131`:** chưa lấy được văn bản hiện hành ở URL chính thức; không trích câu quy định này. Nguồn này không thuộc danh mục dự thảo.',
    '- **J13/J14/J15/J19/J27/J34/J37/J40:** nhận dạng thư mục được kiểm; ghi chú của từng mục giới hạn phần nội dung đã đọc. Không tự chứng nhận toàn bộ nhận xét so sánh trong sổ. `gerzinic2023` không xác nhận mức định giá 20–25 EUR/giờ từng bị cảnh báo ở K35.',
    '', '### Hai bản công bố sau cần phân biệt','',
    'Lu–Kühnel: kết quả tìm kiếm của nhà xuất bản cho bản *Case Studies on Transport Policy* 21:101499 (2025), DOI 10.1016/j.cstp.2025.101499; trang bản cuối và toàn văn vẫn bị chặn. Đây là bản công bố ứng viên được nhận diện, chưa phải một bản cuối đã mở. Giữ `lu2024`, DOI của DepositOnce, vì công thức giờ đón và khoảng đệm của C2-14 gắn với bản đó. Không nhập năm 2025 và DOI tạp chí vào một mục ghi năm 2024.',
    '', 'Leonardi: đã mở [bản ghi cơ quan tác giả](https://researchportal.ip-paris.fr/en/publications/data-driven-assessment-for-the-predictability-of-demand-responsiv/) xác nhận bản *Transportmetrica A: Transport Science* (2026), DOI 10.1080/23249935.2026.2650136, tên cuối *Data-driven assessment for the predictability of demand responsive transit*. Bản ghi ghi đang in; chưa xác nhận tập, kỳ hoặc trang, toàn văn nhà xuất bản bị chặn. Tóm tắt của bản cuối xác nhận các ý rộng của C2-13, nhưng bản `leonardi2024` vẫn là phiên bản được đọc và có mốc trang trong Ch2. Chưa thay sang bản tạp chí khi các đoạn cụ thể chưa đối chiếu.',
    '', '## Bản đồ đủ J01–J42','',
    '| Dòng sổ | Khóa hoặc nguồn nội bộ | Được dự kiến trong phạm vi đề cương? |','|---|---|---|']
for j,keys in sorted(mapping.items()):
    note=', '.join('`'+k+'`' for k in keys) if keys else 'Văn bản ranh giới/mã nội bộ; không tạo bibitem ngoài'
    if j in {'J05','J11'}:note+='; phần so với luật khóa luận là suy luận/nội bộ'
    if j=='J38':note+='; tổng hợp nhiều công trình đã lập bản đồ ở các hàng khác'
    if j=='J35':note+='; `deepeta2022` chỉ đối chiếu blog'
    md.append('| '+j+' | '+note+' | '+('Có' if j in planned_ids else 'Không; hoặc trích do bản nháp nếu có')+' |')
md+=['','## Các khóa cũ cân nhắc bỏ','',
    f'**{len(drop)} trong 27 mục cũ** không được bản nháp nào trong phạm vi quét trích và không được các hàng đề cương dự kiến. Chỉ là đề nghị cho lần ghép, chưa xóa hay sửa tệp luận văn:',
    '',', '.join('`'+k+'`' for k in drop)+'.',
    '', '`fleetpy2022` là bản tiền ấn bảy tác giả khác bài ETRR 2026 mười tác giả; bài hiện được trích là `engelhardt2026`. `fielbaum2022scale` đã sửa đúng nhận dạng bản công bố nhưng không có câu đang trích. Mức “tám mục” trong đề cương là ước lượng cũ; vòng quét này cho 18 mục với hợp mọi bản Ch2, hoặc 20 mục khi chỉ tính Ch2-v4.',
    '', '## Tiêu đề và nhóm ngôn ngữ','',
    'Đã đọc `ridebound/main.tex`: lớp `report`, gói `hyperref`, không đổi `\\bibname`, không có định nghĩa nhóm ngôn ngữ hay yêu cầu của trường về tách thư mục. Đọc `noi-dung/10-tai-lieu.tex`: có `\\chapter*{Tài liệu tham khảo}` rồi mới `thebibliography`, nên môi trường tự mở thêm chương mang tên mặc định Bibliography.',
    '', 'Đã đọc nguyên trang tài liệu tham khảo của mẫu DACN: **PDF trang 49, trang in 37**, tiêu đề “Tài liệu tham khảo”, sau đó nhóm **“Tiếng Việt”** và **“Tiếng Anh”**. Đây là chứng cứ về mẫu của chủ nghiên cứu, phù hợp STYLE quy tắc 35; không phải quy định UET độc lập đã được xác minh. Toàn bộ nguồn được giữ lần này là tiếng Anh; dự thảo chỉ in nhóm Tiếng Anh và ghi chú không có nguồn tiếng Việt, không tạo mục hoặc nhóm trống.',
    '', 'Cách sửa trong tệp dự thảo: đặt `\\renewcommand{\\bibname}{Tài liệu tham khảo}` trước môi trường, bỏ chương sao riêng; đưa đúng một dòng mục lục và mốc `\\phantomsection` vào sau khi mở môi trường. Chỉ cần `\\input` tệp này bằng mẫu hiện tại; không thêm một chương tài liệu tham khảo ở nơi gọi.',
    '', '## Kiểm tra giao nộp','',
    f'Đã kiểm bằng kịch bản chỉ đọc/ghép văn bản đã lưu: đủ 27 khóa cũ, đủ 15 khóa Ch2-v4, đủ 42 dòng J, {len(retain)} bibitem không trùng khóa, không thiếu khóa trích, đúng một môi trường thư mục và một dòng mục lục, cân bằng ngoặc. Không chạy dựng LaTeX vì luật phiên cấm dựng; số trang và việc dàn trang cuối cần kiểm khi người ghép dựng luận văn. Chỉ tạo tệp nhỏ trong `r32-bib`, mọi lần mở ghi dùng chế độ độc quyền.',
    '', 'Các kịch bản và kết quả quét được lưu kèm. Thử API Crossref từ Python bị chặn mạng; không dùng các lần truy cập thất bại đó làm chứng cứ VERIFIED. Bảng dựa vào trang nhà xuất bản, arXiv, kho cơ quan hoặc bản gốc đã mở được, như URL và ghi chú từng dòng.', '']

resolution='''# Hörl–Zwick: giải quyết nhận dạng và phiên bản

Kiểm ngày 12–13/10/2026. **Dùng `horl2022` cho bản hội nghị TRB 2022 lưu ở ETH, DOI 10.3929/ethz-b-000561639.** Chưa tìm thấy bản tạp chí được kiểm chứng của chính công trình này.

## Hai tệp được mở độc lập

1. `C:/PDF/Paper/1-s2.0-S0191261522000716-main.pdf`: 22 trang. Trang đầu là **Sh. Sharif Azadeh, Bilge Atasoy, Moshe E. Ben-Akiva, M. Bierlaire, M.Y. Maknoon**, *Choice-driven dial-a-ride problem for demand responsive mobility service*, **Transportation Research Part B: Methodological 161 (2022), 128–149**, DOI **10.1016/j.trb.2022.04.008**. Tên, tác giả, số tập, trang và DOI hiện trực tiếp trên trang đầu. [Kho MIT của bản xuất bản cuối](https://dspace.mit.edu/entities/publication/024805a3-e5f5-4a58-8519-096c34e2b525) cũng ghi đúng tên tệp này. Đây là `sharifazadeh2022`, không phải Hörl–Zwick.

2. `E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/claude-work/pdf/hoerl-zwick-2022.pdf`: **17 trang vật lý** gồm bìa kho ETH và **16 trang bản thảo đánh số 1–16**. Bìa ghi Sebastian Hörl, Felix Zwick, *Traffic uncertainty in on-demand high-capacity ride-pooling*, loại Conference Paper, năm 2022 và DOI trên. Trang tiêu đề bản thảo ghi ngày nộp 27/10/2021. Đã trích lại chính PDF này, không chỉ đọc `.txt` cũ. Tựa, tác giả, bìa, số trang và các công thức khớp [bản ETH chính thức đã mở](https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/561639/ab1659.pdf?isAllowed=y&sequence=1).

Các đoạn trích nguyên trang và kết quả đếm nằm trong `local-elsevier-excerpts.txt` và `inventory-and-horl-probe-output-v2.txt` cùng thư mục.

## Tên hội nghị và tình trạng bản tạp chí

[ETH IVT, mục AB1659](https://www.ivt.ethz.ch/en/vpl/publications/working-papers.html) xác nhận công trình của S. Hörl và F. Zwick được trình bày tại **101st Annual Meeting of the Transportation Research Board (TRB 2022), Washington, D.C., tháng 1/2022**. [Trang nghiên cứu MATSim của ETH](https://www.ivt.ethz.ch/en/research/matsim.html) cũng ghi hội nghị này và mã TRBAM-22-01001. Mã đó là mã bài, không phải khoảng trang của kỷ yếu.

Đã tìm theo đúng tựa và cặp tác giả, đối chiếu các bản ghi ETH và bản thảo. **Không tìm được bản tạp chí có trang nhà xuất bản, DOI tạp chí hoặc quan hệ phiên bản được xác minh cho chính tựa này.** Kết luận là chưa có bản tạp chí được kiểm chứng trong vòng này; không khẳng định một tìm kiếm âm chứng minh tuyệt đối rằng không thể có bản đổi tựa. Tệp Elsevier được brief đưa ra không phải bằng chứng cho một bản tạp chí của Hörl–Zwick. Không gán tập 161 hoặc trang 128–149 của Sharif Azadeh sang `horl2022`.

## Kiểm số công thức ở phiên bản được chọn

Tất cả các mục dưới nằm ở **trang bản thảo 8, trang PDF vật lý 9** của bản ETH/local đã mở:

| Nhãn | Nội dung được kiểm |
|---|---|
| (7), chiến lược B | Giờ trả bắt buộc bằng giá trị lớn hơn giữa giờ trả cập nhật và giờ trả muộn nhất: `t_required_dropoff = max(t_updated_dropoff, t_latest_dropoff)` |
| (9) | Giờ đón của tuyến đang xét không vượt giờ đón bắt buộc |
| (10) | Giờ trả của tuyến đang xét không vượt giờ trả bắt buộc |
| (11) | Mục tiêu cộng phạt phần vượt các mốc gốc; khác với các ràng buộc trên giờ bắt buộc |

Phần giải thích chiến lược B bắt đầu ở trang bản thảo 7, trang PDF 8: mỗi lượt tính lại các giờ trên tuyến đang gán theo thời gian đi hiện tại. **Công thức (8) thuộc chiến lược C về giờ đón**, không phải công thức B về giờ trả. Vì luận văn viện dẫn chính (7), (9)–(10), bản TRB/ETH đã đọc là lựa chọn có mốc kiểm chứng đầy đủ.

## Dòng thư mục đề nghị

S. Hörl và F. Zwick. *Traffic uncertainty in on-demand high-capacity ride-pooling*. Trong *101st Annual Meeting of the Transportation Research Board*, Washington, D.C., tháng 1/2022. ETH Zurich Research Collection, 2022. DOI: 10.3929/ethz-b-000561639.

Không thêm tập, kỳ hoặc khoảng trang kỷ yếu chưa được xác nhận. Có thể mô tả “bản thảo 16 trang” trong ghi chú kiểm chứng; không dùng “1–16” như trang được nhà xuất bản gán. Năm nộp 2021 không thay năm công bố hội nghị 2022. Giữ đúng khóa `horl2022` của Ch2 và Ch3; dòng đề nghị đã có trong `10-tai-lieu-draft.tex`.
'''
finals={'BIB-VERIFICATION.md':'\n'.join(md),'10-tai-lieu-draft.tex':tex,'HORL-ZWICK-RESOLUTION.md':resolution,'inventory-final-v2.json':json.dumps(inventory,ensure_ascii=False,indent=2)+'\n','verified-records-final-v2.json':json.dumps(rows,ensure_ascii=False,indent=2)+'\n'}
for name in finals:assert not (OUT/name).exists(), 'Refusing overwrite: '+name
for name,contents in finals.items():
    with (OUT/name).open('x',encoding='utf-8',newline='\n') as h:h.write(contents)
qa={'records':len(rows),'statuses':dict(counts),'legacy_count':len(legacy),'draft_bibitems':len(texkeys),'latest_ch2_count':len(latest_ch2['keys']),'missing_cited_keys':sorted(set(inventory['cited_keys'])-set(texkeys)),'duplicate_bibitems':len(texkeys)!=len(set(texkeys)),'register_rows':len(mapping),'legacy_drop_count':len(drop),'corrected_keys':sorted(r['key'] for r in rows if r['status']=='CORRECTED'),'cannot_verify_keys':sorted(r['key'] for r in rows if r['status']=='CANNOT VERIFY'),'final_ch2_files':[Path(f['path']).name for f in inventory['files'] if Path(f['path']).name.startswith('06-')],'no_build':True,'exclusively_new_outputs':True}
with (OUT/'qa-output-v2.json').open('x',encoding='utf-8') as h:json.dump(qa,h,ensure_ascii=False,indent=2)
print(json.dumps(qa,ensure_ascii=False,indent=2))
