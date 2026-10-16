"""Checks isolated forecast/gate functions, never imports or runs the Stage1a analyzer."""
import ast, hashlib, json, pathlib, types
H=pathlib.Path(__file__).resolve().parent;P=H/"R19-stage1a-analyze-v2.py"
source=P.read_text(encoding="utf-8");tree=ast.parse(source);compile(source,str(P),"exec")
class EvidenceError(RuntimeError):pass
def require(ok,why):
 if not ok:raise EvidenceError(why)
nodes=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name in ("forecast","completion_gate")]
require(len(nodes)==2,"missing isolated functions")
ns=dict(EvidenceError=EvidenceError,require=require,json=json)
exec(compile(ast.Module(body=nodes,type_ignores=[]),str(P),"exec"),ns)
cells=["cell-"+str(i) for i in range(34)]
data={}
class FakePath:
 def __init__(self,key=""):self.key=key
 def __truediv__(self,name):return FakePath(self.key+"/"+name)
 def is_file(self):return data.get(self.key,{}).get("exists",False)
 def stat(self):return types.SimpleNamespace(st_size=data[self.key].get("size",1))
ns["C120"]=FakePath()
def fake_json(p):return data[p.key]["summary"]
ns["read_json"]=fake_json
def complete():
 data.clear()
 for c in cells:
  base="/C-120-"+c
  data[base+"/summary.json"]=dict(exists=True,summary=dict(status="pass",repeatCount=1))
  for name in ("run-00.json","transcript-00.ndjson"):data[base+"/"+name]=dict(exists=True,size=10)
complete();ns["completion_gate"](cells);checks=[dict(name="all 34 completed metadata passes",pass_=True)]
cases=[("missing summary","summary.json","exists",False),("failed summary","summary.json","status","fail"),("two repeats","summary.json","repeatCount",2),("empty transcript","transcript-00.ndjson","size",0),("missing run artifact","run-00.json","exists",False)]
for name,file,key,value in cases:
 complete();q=data["/C-120-"+cells[-1]+"/"+file]
 if key in ("status","repeatCount"):q["summary"][key]=value
 else:q[key]=value
 try:ns["completion_gate"](cells)
 except EvidenceError as e:require("NOT READY" in str(e),"wrong gate failure")
 else:raise EvidenceError("gate allowed "+name)
 checks.append(dict(name=name+" refused",pass_=True))
# Independent inverse-integral oracle, bisection rather than the analyzer's work-consumption loop.
f={d:{k*900:1+(.01*(k%9))+(i*.003) for k in range(96)} for i,d in enumerate(("2018-11-12","2018-11-13","2018-11-14"))}
def reference(t,p,cell):
 day="2018-11-"+cell[7:9]
 src=[d for d in f if d<day] if day in ("2018-11-14","2018-11-15","2018-11-16") else []
 if len(src)<2 or p<=t:return float(p)
 start={"w07":25200,"w08":28800,"w17":61200}[cell[-3:]]
 prof=[sum(f[d][start+900*b] for d in src)/len(src) for b in range(9)]
 b0=t//900000
 def work(arrival):
  at=float(t);v=0.
  while at<arrival:
   b=int(at//900000);end=min(arrival,(b+1)*900000)
   w=1. if b==b0 else prof[min(b,8)]/prof[min(b0,8)]
   v+=(end-at)/w;at=end
  return v
 lo=float(t);hi=t+(p-t)*4+1
 for _ in range(80):
  mid=(lo+hi)/2
  if work(mid)<p-t:lo=mid
  else:hi=mid
 return max(float(p),(lo+hi)/2)
cases=0;max_error=0.
for day in (14,15,16,17,18):
 for win in ("w07","w08","w17"):
  cell="d201811"+str(day)+"-s10-r1-"+win
  for t in (0,899999,900000,7199000,7200000):
   for duration in (0,1,900001,3600000):
    p=t+duration;a=ns["forecast"](t,p,cell,f);b=reference(t,p,cell)
    error=abs(a-b);max_error=max(max_error,error);require(error<1e-7,"forecast mismatch");cases+=1
checks.append(dict(name="independent inverse-integral comparison",cases=cases,max_error_ms=max_error,pass_=True))
result=dict(scope="AST syntax and isolated pure-function checks with synthetic metadata; zero C120 outcome reads, zero analyzer imports/main calls",analyzer_sha256=hashlib.sha256(P.read_bytes()).hexdigest(),checks=checks)
with (H/"R19-analyzer-checks.json").open("x",encoding="utf-8") as out:json.dump(result,out,indent=2)
print(json.dumps(result,sort_keys=True))