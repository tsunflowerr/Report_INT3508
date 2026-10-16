import base64,json,os,re
root=r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2"
known_infeasible={"d20181116-s10-r2","d20181116-s10-r4","d20181117-s10-r1","d20181117-s10-r3"}
pred=set(); cellmaxV={}
for c in sorted(d for d in os.listdir(root) if "-c1-tight-s7" in d):
    cell=re.search(r"(d\d{8}-s10-r\d)",c).group(1)
    V={}
    with open(os.path.join(root,c,"transcript-00.ndjson"),encoding="utf-8") as h:
        for line in h:
            fr=json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
            if fr.get("messageType")!="decision": continue
            for a in fr["payload"].get("actions",[]):
                if a["decisionType"]!="promisePublished": continue
                p=a["payload"]; r=p["promise"]["requestId"]
                V[r]=V.get(r,0)+p["visibleDelta"]["dropEtaTotalMs"]
    m=max(V.values())/1000 if V else 0
    cellmaxV[cell]=m
    if m>30: pred.add(cell)
print("Du doan (o co khach V>30s duoi nhanh hanh vi):", sorted(pred))
print("Da biet (o vo nghiem duoi co so ket qua 30s):  ", sorted(known_infeasible))
print("Trung khop:", pred==known_infeasible, "| giao:", len(pred&known_infeasible), "/", len(known_infeasible))
print("Cuc dai V theo o (s):", {k:round(v,1) for k,v in sorted(cellmaxV.items()) if v>20})
