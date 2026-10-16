import csv, json, hashlib, math, sys, platform
from pathlib import Path
from collections import defaultdict
import numpy as np
import sklearn
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import QuantileRegressor

ROOT=Path(r'E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work')
SOURCE=Path(r'C:/RideBoundData/research/ml-pilot-v1/riders-causal-2026-10-08.csv')
SEAL=ROOT.parent/'claude-work'/'ML-PILOT-SEALED.md'
BASE=['clock_min','horizon_s','pick_s','fc_ext_s','maxride_s','room_s']
STATE=['other_assigned','other_onboard']
METHODS=['uniform','fc+uniform','HGB','HGB-nostate','LinQR']
NUM=BASE+STATE+['P0','D0','t0','A','resid_s']
rows=list(csv.DictReader(SOURCE.open(newline='',encoding='utf8')))
for row in rows:
    for field in NUM: row[field]=float(row[field])
    row['day']='2018-'+row['cell'][5:7]+'-'+row['cell'][7:9]

def dump_tsv(path, items):
    with path.open('x',newline='',encoding='utf8') as handle:
        if items:
            writer=csv.DictWriter(handle,fieldnames=list(items[0]),delimiter='\t',lineterminator='\n'); writer.writeheader(); writer.writerows(items)

def metrics(selected, quotes):
    err=np.array([(r['A']-q)/1000 for r,q in zip(selected,quotes)])
    ext=np.array([(q-r['P0'])/1000 for r,q in zip(selected,quotes)])
    horizon=np.array([(q-r['t0'])/1000 for r,q in zip(selected,quotes)])
    n=len(selected)
    return dict(n=n,late60=int(np.sum(err>60)),early60=int(np.sum(err< -60)),within60=int(np.sum(np.abs(err)<=60)),Y60_pct=float(np.mean(err>60)*100),early60_pct=float(np.mean(err< -60)*100),symmetric_pct=float(np.mean(np.abs(err)<=60)*100),mean_extension_s=float(np.mean(ext)),p90_extension_s=float(np.sort(ext)[math.ceil(.9*n)-1]),mean_horizon_s=float(np.mean(horizon)))

# Two independent readings expose serialization rounding instead of silently adopting an analysis choice.
# canonical follows target/quote equations exactly; stored uses the CSV's rounded target and delta features.
allmetrics=[]; allcal=[]; allquotes=[]; allgains=[]; verdicts={}; metadata={}
for version in ['canonical','stored']:
    summary={}; quote_lookup={}
    for world,arm in sorted(set((r['world'],r['arm']) for r in rows)):
        group=[r for r in rows if (r['world'],r['arm'])==(world,arm)]
        fit=[r for r in group if r['role']=='fit']; cal=[r for r in group if r['role']=='calibration']; test=[r for r in group if r['role'].startswith('test')]
        if not cal: # Accept the concrete CSV spelling, preserving its roles in metadata.
            cal=[r for r in group if r['role']=='cal']
        assert fit and cal and test,(world,arm,sorted(set(r['role'] for r in group)))
        delta=np.array([(r['D0']-r['P0'])/1000 if version=='canonical' else r['fc_ext_s'] for r in cal])
        mean_delta=float(np.mean(delta)); target=np.array([(r['A']-r['D0'])/1000 if version=='canonical' else r['resid_s'] for r in fit])
        rules={'uniform':(None, None),'fc+uniform':(None,None)}
        for name in ['HGB','HGB-nostate','LinQR']:
            features=BASE if name=='HGB-nostate' else BASE+STATE
            X=np.array([[r[f] for f in features] for r in fit]); XC=np.array([[r[f] for f in features] for r in cal]); XT=np.array([[r[f] for f in features] for r in test])
            if name=='LinQR': model=make_pipeline(StandardScaler(),QuantileRegressor(quantile=.9,alpha=1.,solver='highs'))
            else: model=HistGradientBoostingRegressor(loss='quantile',quantile=.9,learning_rate=.05,max_iter=100,max_leaf_nodes=7,min_samples_leaf=20,l2_regularization=1.,random_state=7,early_stopping=False)
            model.fit(X,target); wc=np.maximum(0,model.predict(XC)); wt=np.maximum(0,model.predict(XT)); meanw=float(np.mean(wc))
            assert mean_delta<=30,(world,arm,mean_delta)
            rho=(30-mean_delta)/meanw if meanw else None
            rules[name]=(rho,wt)
            allcal.append(dict(version=version,world=world,arm=arm,method=name,E=30,n_fit=len(fit),n_cal=len(cal),n_test=len(test),mean_delta_s=mean_delta,mean_w_s=meanw,rho='' if rho is None else rho,fallback=meanw==0))
        for name in METHODS:
            if name=='uniform': quotes=np.array([r['P0']+30000 for r in test])
            elif name=='fc+uniform': quotes=np.array([r['D0']+(30-mean_delta)*1000 for r in test])
            else:
                rho,w=rules[name]
                quotes=np.array([r['D0'] for r in test])+1000*(rho*w if rho is not None else np.repeat(30-mean_delta,len(test)))
            for r,q in zip(test,quotes):
                key=(world,arm,r['cell'],r['rider'],name); quote_lookup[key]=float(q)
                allquotes.append(dict(version=version,world=world,arm=arm,cell=r['cell'],day=r['day'],window=r['window'],rider=r['rider'],method=name,E=30,F_ms=float(q),A_ms=r['A'],P0_ms=r['P0'],D0_ms=r['D0'],error_s=(r['A']-q)/1000,extension_s=(q-r['P0'])/1000))
            for day in sorted(set(r['day'] for r in test)):
                for window in ['ALL']+sorted(set(r['window'] for r in test if r['day']==day)):
                    inds=[i for i,r in enumerate(test) if r['day']==day and (window=='ALL' or r['window']==window)]
                    selected=[test[i] for i in inds]; vals=metrics(selected,quotes[inds]); record=dict(version=version,world=world,arm=arm,day=day,window=window,cohort='own',method=name,E=30,**vals)
                    allmetrics.append(record); summary[(world,arm,day,window,name)]=record
    # Common-completed intersections use immutable request ID plus cell, not dataframe row alignment.
    for world,day in sorted(set((r['world'],r['day']) for r in rows if r['role'].startswith('test'))):
        arms=sorted(set(r['arm'] for r in rows if r['world']==world and r['day']==day and r['role'].startswith('test')))
        byarm={a:{(r['cell'],r['rider']):r for r in rows if r['world']==world and r['day']==day and r['arm']==a and r['role'].startswith('test')} for a in arms}
        common=set.intersection(*(set(v) for v in byarm.values()))
        for arm in arms:
            selected=[byarm[arm][k] for k in sorted(common)]
            for name in METHODS:
                quotes=np.array([quote_lookup[(world,arm,r['cell'],r['rider'],name)] for r in selected])
                allmetrics.append(dict(version=version,world=world,arm=arm,day=day,window='ALL',cohort='common',method=name,E=30,**metrics(selected,quotes)))
    def compare(world,arm,day,window,model,control):
        mod=summary[(world,arm,day,window,model)]; ctl=summary[(world,arm,day,window,control)]
        guards=dict(lower_y=mod['Y60_pct']<ctl['Y60_pct'],mean_guard=mod['mean_extension_s']<=ctl['mean_extension_s']+1,p90_guard=mod['p90_extension_s']<=ctl['p90_extension_s']+15,early_guard=mod['early60_pct']<=ctl['early60_pct']+1)
        record=dict(version=version,world=world,arm=arm,day=day,window=window,model=model,control=control,gain_pp=ctl['Y60_pct']-mod['Y60_pct'],**guards,WIN=all(guards.values()))
        allgains.append(record); return record
    mdates=['2018-11-15','2018-11-16']; sday='2018-11-13'
    m1=[compare('measured','C-30',d,'ALL','HGB','fc+uniform') for d in mdates]
    m2=[compare('measured','U',d,'ALL','HGB',c) for d in mdates for c in ['uniform','fc+uniform']]
    m3=compare('static','FREE',sday,'ALL','HGB','uniform')
    m3w=[compare('static','FREE',sday,w,'HGB','uniform') for w in ['w08','w17']]
    m4=[]
    for world,arm,day in [('measured','U',d) for d in mdates]+[('static',a,sday) for a in ['FREE','LOCKS']]:
        c=summary[(world,'C-30',day,'ALL','fc+uniform')]
        for model in ['HGB','HGB-nostate','LinQR']:
            v=summary[(world,arm,day,'ALL',model)]
            m4.append(dict(world=world,arm=arm,day=day,model=model,matches_y=v['Y60_pct']<=c['Y60_pct'],matches_symmetric=v['symmetric_pct']>=c['symmetric_pct'],jointly_matches=v['Y60_pct']<=c['Y60_pct'] and v['symmetric_pct']>=c['symmetric_pct']))
    m5=[]
    for world,arm,day,ctl in [('measured','U',d,'fc+uniform') for d in mdates]+[('static','FREE',sday,'uniform')]:
        full=compare(world,arm,day,'ALL','HGB',ctl)['gain_pp']; nostate=compare(world,arm,day,'ALL','HGB-nostate',ctl)['gain_pp']
        if full>0: m5.append(dict(world=world,arm=arm,day=day,G_full=full,G_nostate=nostate,condition=full-nostate>=full/2))
    verdicts[version]=dict(ML1=all(x['gain_pp']<1 for x in m1),ML2=all(x['gain_pp']>=1 and x['WIN'] for x in m2),ML3=m3['gain_pp']>=3 and m3['WIN'] and all(x['gain_pp']>0 for x in m3w),ML4=not any(x['jointly_matches'] for x in m4),ML5=all(x['condition'] for x in m5),ML1_detail=m1,ML2_detail=m2,ML3_detail=m3,ML3_windows=m3w,ML4_detail=m4,ML5_detail=m5)
    verdicts[version]['kill']=not verdicts[version]['ML2'] and not verdicts[version]['ML3']
    metadata[version]=dict(roles={role:sum(r['role']==role for r in rows) for role in sorted(set(r['role'] for r in rows))},world_arm_role_counts={f'{w}/{a}/{role}':sum((r['world'],r['arm'],r['role'])==(w,a,role) for r in rows) for w,a,role in sorted(set((r['world'],r['arm'],r['role']) for r in rows))})
    print(version,{k:v for k,v in verdicts[version].items() if k.startswith('ML') and isinstance(v,bool)},flush=True)

dump_tsv(ROOT/'round11-reproduce-metrics.tsv',allmetrics)
dump_tsv(ROOT/'round11-reproduce-calibration.tsv',allcal)
dump_tsv(ROOT/'round11-reproduce-rider-quotes.tsv',allquotes)
dump_tsv(ROOT/'round11-reproduce-gains-guards.tsv',allgains)
with (ROOT/'round11-reproduce-verdicts.json').open('x',encoding='utf8') as handle: json.dump(verdicts,handle,indent=2)
metadata.update(python=sys.version,sklearn=sklearn.__version__,source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),seal_sha256=hashlib.sha256(SEAL.read_bytes()).hexdigest(),rows=len(rows),distinct_world_arm_cells=len(set((r['world'],r['arm'],r['cell']) for r in rows)),features=BASE+STATE,target_rounding_max_s=max(abs(r['resid_s']-(r['A']-r['D0'])/1000) for r in rows),delta_rounding_max_s=max(abs(r['fc_ext_s']-(r['D0']-r['P0'])/1000) for r in rows))
with (ROOT/'round11-reproduce-meta.json').open('x',encoding='utf8') as handle: json.dump(metadata,handle,indent=2)
print('independent artifacts sealed',len(allmetrics),len(allquotes),flush=True)
