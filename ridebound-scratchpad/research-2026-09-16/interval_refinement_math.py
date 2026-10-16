"""Standalone interval arithmetic research prototype; not a RideBound dispatcher/simulator.
A color denotes a sampled future request type/scenario, not a probability unless
weights have been independently justified. Several ETA options of one color count once.
"""
from collections import defaultdict
import json, random, hashlib
from pathlib import Path

def choose_window(old, band, width, options, weights):
    L,U=old; a,b=band
    if not (L<=a<=b<=U and b-a<=width<=U-L):
        return None
    low=max(L,b-width); high=min(a,U-width)
    events=defaultdict(lambda:[[],[]])
    events[low]; events[high]
    for color,t in options:
        assert weights[color]>=0
        enter=max(low,t-width); leave=min(high,t)
        if enter<=leave:
            events[enter][0].append(color)
            events[leave][1].append(color)
    counts=defaultdict(int);score=0;best=None
    for left,(enters,leaves) in sorted(events.items()):
        for color in enters:
            if counts[color]==0:score+=weights[color]
            counts[color]+=1
        if best is None or score>best['score']:
            best={'left':left,'right':left+width,'score':score}
        # Closed intervals: remove only AFTER evaluating both endpoint groups.
        for color in leaves:
            counts[color]-=1
            if counts[color]==0:score-=weights[color]
    return best

def oracle(old,band,width,options,weights):
    L,U=old;a,b=band
    good=[]
    for left in range(L,U-width+1):
        if not left<=a<=b<=left+width:continue
        colors={c for c,t in options if left<=t<=left+width}
        good.append({'left':left,'right':left+width,'score':sum(weights[c] for c in colors)})
    return max(good,key=lambda z:(z['score'],-z['left'])) if good else None

def verify():
    rng=random.Random(20260920)
    for k in range(1000):
        L=0;U=rng.randint(1,30);a=rng.randint(L,U);b=rng.randint(a,U)
        width=rng.randint(0,U)
        weights={c:rng.randint(0,5) for c in range(5)}
        options=[(rng.randrange(5),rng.randint(-5,U+5)) for _ in range(rng.randint(0,30))]
        got=choose_window((L,U),(a,b),width,options,weights)
        expected=oracle((L,U),(a,b),width,options,weights)
        assert got==expected,(k,got,expected)
    # Many duplicate ETA plans must not count as many independently served requests.
    duplicate=[('a',7)]*100+[('b',11),('c',12)]
    got=choose_window((0,20),(10,10),3,duplicate,{'a':1,'b':1,'c':1})
    assert got['score']==2 and got['left']==9
    assert choose_window((0,20),(5,15),3,[],{}) is None
    # A genuine width/notice tradeoff example, purely mathematical.
    sample=choose_window((600,900),(700,700),60,[('r1',710),('r1',715),('r2',740),('r3',750)],{'r1':1,'r2':1,'r3':1})
    assert sample['score']==3
    return {'randomDifferentialCases':1000,'duplicatesCase':'pass','oversizeFallbackBand':'correctlyRejected',
            'example':sample,'scope':'Exact best weighted distinct-color coverage on supplied scalar ETA options with one fixed fallback band; not a global multi-rider or closed-loop optimum.',
            'novelty':'Sweep-line maximum coverage is standard; contribution of a future research method cannot be claimed from this primitive alone.'}
if __name__=='__main__':
    report=verify();report['scriptSha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    Path(__file__).with_name('interval-refinement-math-checks.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))
