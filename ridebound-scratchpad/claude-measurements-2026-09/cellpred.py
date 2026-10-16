import base64,json,os,collections
root=r"E:/RideBoundData/wp14/drift-v1"
for arm in ("dr-conduct-k0","dr-conduct-k1"):
    cells=[d for d in sorted(os.listdir(root)) if d.startswith(arm+"-d") and os.path.exists(os.path.join(root,d,"summary.json"))]
    cellmax={}
    for c in cells:
        first={}; last={}
        with open(os.path.join(root,c,"transcript-00.ndjson"),encoding="utf-8") as h:
            for line in h:
                fr=json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
                if fr.get("messageType")!="decision": continue
                for a in fr["payload"].get("actions",[]):
                    if a["decisionType"]!="promisePublished": continue
                    pl=a["payload"]; rid=pl["promise"]["requestId"]; q=pl["promise"]["dropEtaMs"]
                    first.setdefault(rid,q); last[rid]=q
        # max over riders of prefix displacement would need full path; use endpoint D+ and E as proxy
        dplus=[max(0,last[r]-first[r])/1000 for r in first]
        cellmax[c]=max(dplus) if dplus else 0
    print(f"=== {arm}: {len(cells)} o hoan tat ===")
    print(f"  max D+ theo o (s): " + ", ".join(f"{v:.0f}" for v in sorted(cellmax.values())))
    for l in (30,60,120,300,600):
        ok=sum(1 for v in cellmax.values() if v<=l)
        print(f"  du doan nhanh han-chot l={l:>3}s : {ok}/{len(cells)} o KHA THI  (o nao co khach D+>l se vo nghiem)")
