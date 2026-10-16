"""R16: independent first-quote arrival metrics from existing w07 transcripts.
Read-only inputs; every decoded frame hash checked; all outputs exclusive-created.
No simulation, build or new model fitting. Forecast inactive on 12/13 November under
the existing causal-no15 rule (display_layer.py:10-12).
"""
import base64,collections,concurrent.futures,hashlib,json,pathlib,re
HERE=pathlib.Path(__file__).resolve().parent
def scan(job):
    arrivals={};last=None;frames=0;digest=hashlib.sha256()
    with pathlib.Path(job["transcript"]).open("rb") as f:
        for line in f:
            digest.update(line)
            if not line.strip():continue
            rec=json.loads(line);raw=base64.b64decode(rec["frameBase64"],validate=True)
            assert len(raw)==rec["frameLengthBytes"]
            assert hashlib.sha256(raw).hexdigest()==rec["frameSha256"]
            frames+=1
            match=re.search(rb'"messageType":"([^"]+)"',raw[:256]);assert match
            typ=match.group(1)
            if typ==b'eventBatch':
                env=json.loads(raw)
                for e in env["payload"].get("events",[]):
                    if e.get("eventType")=="passengerAlighted":
                        rid=e["payload"]["requestId"]
                        if rid in arrivals:assert arrivals[rid]==env["simTimeMs"]
                        arrivals[rid]=env["simTimeMs"]
            elif typ==b'checkpoint' and rec["direction"]=="runnerToAdapter":
                last=raw
    assert digest.hexdigest()==job["sha256"]
    assert last is not None
    state=json.loads(last)["payload"]["content"]["onlineState"]
    completed={r["requestId"] for r in state["requests"] if r["lifecycle"]=="completed"}
    assert len(state["requests"])==108
    assert set(r["lifecycle"] for r in state["requests"])<=set(("completed","rejected"))
    stats=collections.Counter();smax=0
    for ledger in state["commitmentLedger"]:
        rid=ledger["requestId"];assert rid in completed and rid in arrivals
        es=ledger["entries"];assert es[0]["kind"]=="initialPromise"
        q=es[0]["publishedPromise"]["projection"]["dropEtaMs"]
        err=arrivals[rid]-q
        changes=[e["publishedPromise"]["projection"]["dropEtaMs"]-e["exogenousProjection"]["dropEtaMs"] for e in es[1:]]
        spent=sum(map(abs,changes));smax=max(smax,spent)
        stats["served"]+=1;stats["late60"]+=err>60000;stats["late120"]+=err>120000
        stats["early60"]+=err< -60000;stats["exposed"]+=spent>0
        stats["repeated"]+=sum(c!=0 for c in changes)>=2;stats["S_sum_ms"]+=spent
        if job["arm"].startswith("C-"):assert spent<=int(job["arm"][2:])*1000
    assert stats["served"]==len(completed)==job["completed"]
    return dict(arm=job["arm"],cell=job["cell"],path=job["transcript"],frames=frames,sha256=digest.hexdigest(),stats=dict(stats),S_max_ms=smax)
def main():
    source=json.loads((HERE/"R13-raw-verification.json").read_text(encoding="utf-8"))
    jobs=[r for r in source["runs"] if r["population"]=="w07" and (r["arm"]=="U" or r["arm"].startswith("C-"))]
    assert len(jobs)==72
    assert all(r["cell"].startswith(("d20181112","d20181113")) for r in jobs)
    results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        for i,r in enumerate(pool.map(scan,jobs),1):
            results.append(r)
            if i%8==0:print("Hash-checked existing transcripts",i,"/72",flush=True)
    audit=json.loads((HERE/"R15-audit.json").read_text(encoding="utf-8"))
    groups=[]
    for arm in ["U"]+["C-"+str(b) for b in (30,60,90,120,150,180,240,300)]:
        rows=[r for r in results if r["arm"]==arm];assert len(rows)==8
        stats=collections.Counter()
        for r in rows:stats.update(r["stats"])
        s=stats["served"];row=dict(arm=arm,runs=8,requests=864,**dict(stats),S_max_ms=max(r["S_max_ms"] for r in rows),timely60=s-stats["late60"],timely120=s-stats["late120"],Y60_percent=100*stats["late60"]/s,Y120_percent=100*stats["late120"]/s,forecast_active=False)
        if arm!="U":
            prior=next(g for g in audit["groups"] if g["pop"]=="w07" and g["arm"]==arm)
            for k in ("served","exposed","repeated"):assert row[k]==prior["ledger"][k]
            assert row["S_max_ms"]==prior["ledger"]["S_max_ms"]
            row["budget_prune_records"]=sum(prior["candidates"].values())
            row["cumulative_only_records"]=prior["candidates"].get("cumulative-reported",0)
        groups.append(row)
    output=dict(scope="72 existing w07 C/U transcripts; independent arrivals vs initial quote; frame+file hashes checked; no forecast active under original rule",groups=groups,runs=results)
    with (HERE/"R16-cap-outcomes.json").open("x",encoding="utf-8",newline="\n") as f:json.dump(output,f,indent=2);f.write("\n")
    lines=["# R16 existing cap dial: independent w07 first-quote outcomes","Forecast column equals naive: existing causal-no15 rule inactive on 12/13 November; no new forecast fitted."]
    lines.extend(json.dumps(g,sort_keys=True) for g in groups)
    with (HERE/"R16-cap-outcomes.txt").open("x",encoding="utf-8",newline="\n") as f:f.write("\n".join(lines)+"\n")
    print("\n".join(lines),flush=True)
if __name__=="__main__":main()
