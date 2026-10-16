from pathlib import Path
import urllib.request, urllib.parse, json, concurrent.futures, datetime, re
OUT=Path(__file__).resolve().parent
existing=Path('E:/Code/Report_INT3508/ridebound/noi-dung/10-tai-lieu.tex').read_text(encoding='utf-8')
dois=re.findall(r'https://doi.org/([^}\s]+)',existing)
dois+=['10.1016/j.tra.2026.104925','10.1016/j.trc.2020.102621','10.1016/j.tbs.2023.100616','10.1007/s10100-015-0422-7','10.1080/23249935.2026.2650136','10.1016/j.cstp.2025.101499','10.1287/mnsc.2022.4448','10.1007/s00291-025-00809-y','10.1002/net.22063','10.1287/trsc.2018.0837','10.1287/mnsc.2021.3991','10.1016/j.tra.2011.06.010','10.1287/mnsc.31.10.1237','10.3389/ffutr.2021.681451','10.1186/s12544-026-00823-3','10.1016/j.trc.2026.105645','10.1016/j.ecotra.2023.100313']
def fetch(doi):
    url='https://api.crossref.org/works/'+urllib.parse.quote(doi,safe='')
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Round32 bibliography verification (read-only)'})
        with urllib.request.urlopen(req,timeout=18) as r:data=json.load(r)['message']
        fields=['DOI','title','author','container-title','volume','issue','page','article-number','published','published-online','published-print','publisher','type','URL','link']
        return {'doi':doi,'url_opened':url,'checked_at':datetime.datetime.now().astimezone().isoformat(),'status':'FETCHED','metadata':{k:data[k] for k in fields if k in data}}
    except Exception as e:return {'doi':doi,'url_opened':url,'status':'FETCH FAILED','error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:rows=list(pool.map(fetch,sorted(set(dois))))
with (OUT/'primary-metadata-v2.json').open('x',encoding='utf-8') as h:json.dump(rows,h,ensure_ascii=False,indent=2)
summary='\n'.join(r['doi']+' '+r['status'] for r in rows)
with (OUT/'primary-metadata-fetch-output-v2.txt').open('x',encoding='utf-8') as h:h.write(summary+'\n')
print(summary)
