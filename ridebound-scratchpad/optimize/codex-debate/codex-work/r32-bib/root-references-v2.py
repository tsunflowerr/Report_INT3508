from pathlib import Path
import json
OUT=Path(__file__).resolve().parent
rows=[]
def add(key,status,authors,title,venue,url,notes,ids,link=None,body='METADATA VERIFIED'):
    tex='\\bibitem{'+key+'}\n'+authors+'\n\\newblock '+title+'.\n\\newblock '+venue+'\n\\newblock \\url{'+(link or url.split(' ; ')[0])+'}'
    rows.append(dict(key=key,status=status,metadata=authors.replace('~',' ')+' '+title+'. '+venue.replace('\\emph{','').replace('}','').replace('--','–'),url=url,notes=notes,tex=tex,register_ids=ids,body_status=body))
add('alonsogonzalez2020','CORRECTED','M.~J. Alonso-González, N.~van Oort, O.~Cats, S.~Hoogendoorn-Lanser, and S.~Hoogendoorn.',
    'Value of time and reliability for urban pooled on-demand services',r'\emph{Transportation Research Part C: Emerging Technologies}, 115:102621, 2020.',
    'https://repository.tudelft.nl/file/File_1217abf5-bc01-4227-ba39-21878929e291?preview=1',
    'Old authors M.J. Alonso-González, S. van Cranenburgh, O. Cats, N. van Oort, S. Hoogendoorn → María J. Alonso-González, Niels van Oort, Oded Cats, Sascha Hoogendoorn-Lanser, Serge Hoogendoorn. Read final-published article first page, not only repository cover. DOI10.1016/j.trc.2020.102621. Independently agrees with C2-18.', ['J24','C2-18'],'https://doi.org/10.1016/j.trc.2020.102621')
add('wardman2026','VERIFIED','M.~Wardman, P.~Murphy, M.~Ojeda-Cabral, A.~Mitrani, K.~Neki, and R.~M.~Humphreys.',
    'Value of time multipliers for walk time, wait time, service headway, displacement time, reliability and congested travel time: review and meta-analysis of worldwide evidence',
    r'\emph{Transportation Research Part A: Policy and Practice}, 207:104925, 2026.',
    'https://eprints.whiterose.ac.uk/id/eprint/239301/1/1-s2.0-S0965856426000662-main.pdf',
    'Read institutional final PDF first page: Mark Wardman, Paul Murphy, Manuel Ojeda-Cabral, Alex Mitrani, Kazuyuki Neki, Richard Martin Humphreys, in order. DOI10.1016/j.tra.2026.104925. Online8March2026. Metadata agrees with C2-17; no issue assigned in article.', ['J23','C2-17'],'https://doi.org/10.1016/j.tra.2026.104925')
add('leonardi2024','VERIFIED','P.~Leonardi, V.~Torrisi, A.~Araldo, and M.~Ignaccolo.',
    'Data-driven assessment for the predictability of On-Demand Responsive Transit','arXiv:2411.11899v1, 2024. EURO Working Group on Transportation, Lund, tháng 9/2024.',
    'https://arxiv.org/abs/2411.11899',
    'Pierfrancesco Leonardi, Vincenza Torrisi, Andrea Araldo, Matteo Ignaccolo. Submitted14November2024; official arXiv comments identify EWGT September2024. DOI10.48550/arXiv.2411.11899. Preserve the exact2024version read for C2-13. A later2026Transportmetrica A title differs; publisher DOI10.1080/23249935.2026.2650136 was attempted but direct fetch failed in root, so do not silently replace the version or invent journal pagination.', ['J21','C2-13'],'https://doi.org/10.48550/arXiv.2411.11899')
add('lu2024','VERIFIED','C.~Lu and N.~Kühnel.',
    'To Wait or to Cruise: The Trade-Off Between Waiting Time and Detours for Service Efficiency in Ride-pooling Systems',
    'Bản tiền ấn, Technische Universität Berlin, DepositOnce, 2024.',
    'https://depositonce.tu-berlin.de/items/fa1164ba-ed61-4775-a1ac-253d80e1758a',
    'Chengqi Lu, Nico Kühnel. Official DepositOnce page: issued1October2024; deposited14October2024; submitted preprint, DOI10.14279/depositonce-21472. Metadata agrees with C2-14. Later final2025Case Studies on Transport Policy21:101499, DOI10.1016/j.cstp.2025.101499, discovered on official publisher search index; direct DOI/full text fetch failed in root. Cite exact2024version until the final passages are checked.', ['J22','C2-14'],'https://doi.org/10.14279/depositonce-21472')
add('hu2022','VERIFIED','X.~Hu, T.~Binaykiya, E.~Frank, and O.~Cirit.',
    'DeeprETA: An ETA Post-processing System at Scale','arXiv:2206.02127v1, 2022.',
    'https://arxiv.org/abs/2206.02127 ; https://arxiv.org/html/2206.02127v1',
    'Ordered authors Xinyu Hu, Tanmay Binaykiya, Eric Frank, Olcay Cirit. Submitted5June2022; DOI10.48550/arXiv.2206.02127; no journal-ref. Full official HTML read: user-facing quantiles/expectiles and residual correction of route-engine ETA. The replacement of the blog by a full paper is valid. The correct current DeepETA blog URL was reachable in this audit, so its alleged dead link does not invalidate hu2022.', ['J35','C2-15'],'https://doi.org/10.48550/arXiv.2206.02127','VERIFIED')
add('molenbruch2017','CORRECTED','Y.~Molenbruch, K.~Braekers, and A.~Caris.',
    'Operational effects of service level variations for the dial-a-ride problem',
    r'\emph{Central European Journal of Operations Research}, 25(1):71--90, 2017.',
    'https://link.springer.com/article/10.1007/s10100-015-0422-7',
    'Register J25 year2015 → journal issue year2017. Published online5October2015, issueMarch2017. Authors Yves Molenbruch, Kris Braekers, An Caris; DOI10.1007/s10100-015-0422-7. Ch2BIB and C2-12 already use correct2017; no correction to that writer entry. Do not create molenbruch2015 alias.', ['J25','C2-12'],'https://doi.org/10.1007/s10100-015-0422-7')
add('bansal2019','VERIFIED','P.~Bansal, Y.~Liu, R.~Daziano, and S.~Samaranayake.',
    'Can Mobility-on-Demand services do better after discerning reliability preferences of riders?','arXiv:1904.07987v1, 2019.',
    'https://arxiv.org/abs/1904.07987',
    'Ordered authors Prateek Bansal, Yang Liu, Ricardo Daziano, Samitha Samaranayake; official arXiv submitted16April2019. Existing reference matches apart from harmless title capitalisation. Archival DOI10.48550/arXiv.1904.07987; no journal pagination claimed. Legacy only; not an active or planned citation.', [],'https://arxiv.org/abs/1904.07987')
add('syed2021','VERIFIED','A.~A.~Syed, F.~Dandl, B.~Kaltenhäuser, and K.~Bogenberger.',
    'Density Based Distribution Model for Repositioning Strategies of Ride Hailing Services',
    r'\emph{Frontiers in Future Transportation}, 2:681451, 2021.',
    'https://www.frontiersin.org/journals/future-transportation/articles/10.3389/ffutr.2021.681451/full',
    'Arslan Ali Syed, Florian Dandl, Bernd Kaltenhäuser, Klaus Bogenberger; publisher full text opened;14June2021; DOI10.3389/ffutr.2021.681451. J19 identifies paper correctly. No thesis-specific forecast formula verified here. Register-only; not added to draft without a citation.', ['J19'],'https://doi.org/10.3389/ffutr.2021.681451')
add('gardner1985','VERIFIED','E.~S.~Gardner, Jr., and E.~McKenzie.',
    'Forecasting Trends in Time Series',r'\emph{Management Science}, 31(10):1237--1246, 1985.',
    'https://pubsonline.informs.org/doi/10.1287/mnsc.31.10.1237',
    'Publisher names Everette S. Gardner, Jr., Ed. McKenzie; printedOctober1985; DOI10.1287/mnsc.31.10.1237. J20 metadata confirmed. Register-only, not planned in outline Ch1–Ch2 or cited in scanned drafts.', ['J20'],'https://doi.org/10.1287/mnsc.31.10.1237')
add('uberxshare','VERIFIED','Uber.', 'Share a Ride with UberX Share - Save Up to 20%',
    'Trang sản phẩm UberX Share; không ghi năm xuất bản. Truy cập ngày 13/10/2026.',
    'https://www.uber.com/us/en/ride/uberx-share/',
    'Official page opened13October2026. FAQ explicitly qualifies arrival times and states8minutes average added time. No per-rider8minute guarantee inferred. Corporate author; volume/issue/pages/DOI not applicable. Proposed canonical key for outline J28.', ['J28'],body='VERIFIED')
add('moiaexpress','VERIFIED','MOIA.', 'MOIA Express booking',
    'Trung tâm trợ giúp MOIA; không ghi năm xuất bản. Truy cập ngày 13/10/2026.',
    'https://help.moia.io/hc/en-us/articles/360020795318-MOIA-Express-booking',
    'Official help page opened; optional paid upgrade and shorter arrival window confirmed. No quantified width or deterministic arrival guarantee given. Corporate author, no DOI or pagination. Proposed canonical key for planned J31.', ['J31'],body='VERIFIED')
add('doordash2024','VERIFIED','C.~Zhang, L.~Warne, Z.~Jiang, Q.~Xu, H.~Jenq, J.~Luo, and P.~Varma.',
    'Improving ETAs with multi-task models, deep learning, and probabilistic forecasts',
    'DoorDash, ngày 12/3/2024. Truy cập ngày 13/10/2026.',
    'https://careersatdoordash.com/blog/improving-etas-with-multi-task-models-deep-learning-and-probabilistic-forecasts/',
    'Official byline order Chi Zhang, Lewis Warne, Ziqi Jiang, Qingyang Xu, Hubert Jenq, Jianzhe Luo, Pradeep Varma. Publisher date12March2024. Read two-layer distribution-prediction and decision architecture and ETA consistency guardrail. Proposed key for J35 DoorDash example; no DOI,volume,issue,pages.', ['J35'],body='VERIFIED')
add('deepeta2022','VERIFIED','T.~Binaykiya, X.~Hu, O.~Cirit, and R.~Hora.',
    'DeepETA: How Uber Predicts Arrival Times Using Deep Learning','Uber, ngày 10/2/2022. Truy cập ngày 13/10/2026.',
    'https://www.uber.com/us/en/blog/deepeta-how-uber-predicts-arrival-times/',
    'Official byline Tanmay Binaykiya, Xinyu Hu, Olcay Cirit, Ramit Hora; date10February2022. Correct current URL opened successfully; this differs from the dead URL reported by Ch2 writer. Do not add a redundant blog bibitem: hu2022 fulfils the Uber technical-source role and is the version cited by Ch2.', ['J35'])
add('ortools','CORRECTED','L.~Perron and V.~Furnon.', 'OR-Tools, phiên bản 9.15',
    'Google, 2026. Gói Google.OrTools 9.15.6755; truy cập ngày 13/10/2026.',
    'https://developers.google.com/optimization/support/cite ; https://github.com/google/or-tools/releases/tag/v9.15 ; https://www.nuget.org/packages/Google.OrTools/9.15.6755',
    'Old unversioned software year2024 → explicitly version9.15(2026). Official suite citation authors Laurent Perron, Vincent Furnon; official release/NuGet dated12January2026. Read C:/Code/RideBound-noworse/src/RideBound.Solvers.OrTools/RideBound.Solvers.OrTools.csproj:9: package9.15.6755. This verifies current project dependency, not every historical binary. No DOI/pages. Keep suite key, do not mislabel as routing library or CP-SAT-specific paper.', [],'https://developers.google.com/optimization')
add('tlc','VERIFIED','New York City Taxi \\& Limousine Commission.', 'TLC Trip Record Data',
    'Trang dữ liệu; không ghi năm xuất bản. Truy cập ngày 13/10/2026.',
    'https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page',
    'Official title and corporate author opened independently. No volume/issue/pages/DOI; add current access date. C2-16 writer12October2026 access is valid for that earlier retrieval; this entry records this audit13October2026.', ['C2-16'])
add('horl2022','CORRECTED','S.~Hörl and F.~Zwick.', 'Traffic uncertainty in on-demand high-capacity ride-pooling',
    r'Trong \emph{101st Annual Meeting of the Transportation Research Board}, Washington, D.C., tháng 1/2022. ETH Zurich Research Collection, 2022.',
    'https://www.ivt.ethz.ch/en/vpl/publications/working-papers.html ; https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/561639/ab1659.pdf?isAllowed=y&sequence=1',
    'Sebastian Hörl, Felix Zwick, in order; ETH AB1659 and repository cover agree2022conference paper; DOI10.3929/ethz-b-000561639. Brief candidate Elsevier file → Sharif Azadeh2022, not Hörl–Zwick. Correct local ETH PDF confirmed independently;17physical pages including cover,16numbered manuscript pages. Equation7 and constraints9–10 match manuscriptp8. No verified journal version found; do not invent journal volume or proceedings pagination. See HORL-ZWICK-RESOLUTION.md.', ['J01','J02','J03','J04','J05','C2-01','C2-04'],'https://doi.org/10.3929/ethz-b-000561639','VERIFIED')
add('yu2022','VERIFIED','Q.~Yu, Y.~Zhang, and Y.-P.~Zhou.',
    'Delay Information in Virtual Queues: A Large-Scale Field Experiment on a Major Ride-Sharing Platform',
    r'\emph{Management Science}, 68(8):5745--5757, 2022.',
    'https://pubsonline.informs.org/doi/10.1287/mnsc.2022.4448',
    'Qiuping Yu,Yiming Zhang,Yong-Pin Zhou; publisher metadata and abstract opened independently. DOI10.1287/mnsc.2022.4448; online8June2022,issueAugust2022. Confirms C2-19 bibliographic identity and abstract scope only; do not imply full-body reading.', ['J33','C2-19'],'https://doi.org/10.1287/mnsc.2022.4448','ABSTRACT ONLY')
add('cohen2022','VERIFIED','M.~C.~Cohen, M.~D.~Fiszer, and B.~J.~Kim.',
    'Frustration-Based Promotions: Field Experiments in Ride-Sharing',r'\emph{Management Science}, 68(4):2432--2464, 2022.',
    'https://pubsonline.informs.org/doi/10.1287/mnsc.2021.3991',
    'Maxime C.Cohen,Michael D.Fiszer,Baek Jung Kim. Publisher issueApril2022; first online31August2021, so2021in DOI/online citation does not change issue year2022. DOI10.1287/mnsc.2021.3991. J27 register-only; abstract/metadata read, not used to extend business-value claims.', ['J27'],'https://doi.org/10.1287/mnsc.2021.3991','ABSTRACT ONLY')
add('watkins2011','VERIFIED','K.~E.~Watkins, B.~Ferris, A.~Borning, G.~S.~Rutherford, and D.~Layton.',
    'Where Is My Bus? Impact of mobile real-time information on the perceived and actual wait time of transit riders',
    r'\emph{Transportation Research Part A: Policy and Practice}, 45(8):839--848, 2011.',
    'https://ojp-content.s3.us-east-2.amazonaws.com/NHI/Old/BaseImages/2014/04/d.pdf',
    'Full article first page opened: Kari Edison Watkins,Brian Ferris,Alan Borning,G.Scott Rutherford,David Layton. DOI10.1016/j.tra.2011.06.010. J37 paper identified as this article, not the separate Ferris-first2011TRB report. Register-only; no new thesis claim inserted.', ['J37'],'https://doi.org/10.1016/j.tra.2011.06.010')
add('uberdelayed2026','VERIFIED','Uber.', 'Introducing Delayed Ride Guarantee',
    'Uber, ngày 3/8/2026. Truy cập ngày 13/10/2026.',
    'https://www.uber.com/us/en/blog/delay-ride-guarantee/',
    'Official current page dated3August2026. Driver fare adjustment after eligible pickup-to-dropoff trip overruns; matched shared rides excluded. J29 optional source, not an arrival-time guarantee for passengers. No DOI or pagination. Do not infer original launch date from current page date.', ['J29'],body='VERIFIED')
add('lyftscheduled','VERIFIED','Lyft.', 'Scheduled rides for riders',
    'Trung tâm trợ giúp Lyft; không ghi năm xuất bản. Truy cập ngày 13/10/2026.',
    'https://help.lyft.com/hc/en-us/all/articles/115013078668-Scheduled-rides-for-passengers',
    'Official help page opened; eligible scheduled rides to airport have tiered Lyft Credits. J30 register-only; market eligibility matters, and pickup promise is distinct from dropoff. No DOI,pagination,publication date invented.', ['J30'],body='VERIFIED')
add('lyftpatent2024','VERIFIED',
    "R.~M.~Ali, N.~C.~Bhupalam, N.~R.~Chainani, V.~C.-j.~Chang, C.~C.~Chheda, P.~Gerstoft, I.~Lobel, J.~Luo, S.~Martin, G.-B.~Richard de Capele d'Hautpoul, and A.~M.~Weinstein.",
    'Systems and methods for enhanced transportation dispatch','Bằng sáng chế US12182741B2, ngày 31/12/2024; Lyft Inc.',
    'https://patents.google.com/patent/US12182741B2/en',
    "Published grant reproduction opened. Ordered inventor names: Rafah Mujtaba Ali; Nihar Chandra Bhupalam; Neil Rajiv Chainani; Vincent Chih-jye Chang; Chirag Chhagan Chheda; Philip Gerstoft; Ilan Lobel; Jianzhe Luo; Sebastien Martin; Guy-Baptiste Richard de Capele d'Hautpoul; Alexander Michael Weinstein. J34 register-only. No journal/DOI/pages; document identity verified, no legal-status or claim-scope conclusion.", ['J34'])
rows.append(dict(key='ecfr37131',status='CANNOT VERIFY',metadata='49 CFR §37.131, Service criteria for complementary paratransit. Current-edition text and full publication metadata not independently retrieved.',url='https://www.ecfr.gov/current/title-49/subtitle-A/part-37/subpart-F/section-37.131',notes='J36 current primary page now redirects to Federal Register request-access page. Tried official URL; do not upgrade register claim from an inaccessible current text or infer current wording from an older FTA report. Optional register-only source; no bibitem included.',tex='',register_ids=['J36'],body_status='CANNOT VERIFY'))
with (OUT/'root-references-v2.json').open('x',encoding='utf-8') as h:json.dump(rows,h,ensure_ascii=False,indent=2)
summary='Root records: '+str(len(rows))+'\n'+ '\n'.join(r['key']+' '+r['status'] for r in rows)
with (OUT/'root-references-output-v2.txt').open('x',encoding='utf-8') as h:h.write(summary+'\n')
print(summary)
