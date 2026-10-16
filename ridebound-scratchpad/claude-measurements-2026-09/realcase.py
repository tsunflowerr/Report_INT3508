import base64,json,os
def hms(ms):
    s=ms//1000; return f"{s//3600:02d}:{(s%3600)//60:02d}:{s%60:02d}.{ms%1000:03d}"
root=r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2"
cell="p-d20181114-s10-r1-b1-tight-s7"
prev={}   # rid -> last published drop eta
viol=[]; normal=[]
with open(os.path.join(root,cell,"transcript-00.ndjson"),encoding="utf-8") as h:
    for line in h:
        fr=json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
        if fr.get("messageType")!="decision": continue
        t=fr.get("simTimeMs",0)
        for a in fr["payload"].get("actions",[]):
            if a["decisionType"]!="promisePublished": continue
            p=a["payload"]; pr=p["promise"]; rid=pr["requestId"]
            newp=pr["dropEtaMs"]
            A=p["decisionDelta"]["dropEtaTotalMs"]
            d=p["exogenousDelta"]["dropEtaTotalMs"]
            B=p["visibleDelta"]["dropEtaTotalMs"]
            v=prev.get(rid)
            if v is not None and A>0 and d>0:
                # reconstruct e
                e = v - d if (A > B) else (v + d if newp>=v else v - d)
                rec=dict(rid=rid[:12],t=t,v=v,e=e,p=newp,A=A,d=d,B=B,ver=p.get("promiseVersion"))
                (viol if A>B else normal).append(rec)
            prev[rid]=newp
def show(r,title):
    print(f"\n--- {title} ---")
    print(f"  khach {r['rid']}...   luc sim-time {hms(r['t'])}  (lan cong bo thu {r['ver']})")
    print(f"    v (da hua lan truoc)          = {hms(r['v'])}")
    print(f"    e (neu KHONG lam gi, tu vi tri that) = {hms(r['e'])}   -> {'SOM hon' if r['e']<r['v'] else 'MUON hon'} v {abs(r['e']-r['v'])/1000:.3f}s")
    print(f"    p (neu nhan them khach moi)   = {hms(r['p'])}")
    print(f"    A = |p-e| = {r['A']/1000:>9.3f}s   (do nha xe)")
    print(f"    d = |e-v| = {r['d']/1000:>9.3f}s   (do giao thong)")
    print(f"    B = |p-v| = {r['B']/1000:>9.3f}s   (khach nhin thay)")
    print(f"    => A + d = {(r['A']+r['d'])/1000:.3f}s  vs  B = {r['B']/1000:.3f}s   {'KHIT' if r['A']+r['d']==r['B'] else 'HUT '+str((r['A']+r['d']-r['B'])/1000)+'s'}")
print(f"O {cell}:  {len(normal)} ca thuong,  {len(viol)} ca A>B")
if normal: show(sorted(normal,key=lambda r:-r['A'])[0],"CA THUONG (cong khit): giao thong va quyet dinh CUNG chieu")
if viol:   show(sorted(viol,key=lambda r:-(r['A']-r['B']))[0],"CA A>B: giao thong THUAN chieu, hap thu bot cu day")
