from pathlib import Path
import re, json, hashlib, ast
ROOT=Path(__file__).resolve().parent
files=[ROOT/"R13-SURVEY-CODEX.md",ROOT/"R13-PROPOSALS-CODEX.md"]
errors=[];links=[];texts={}
for p in files:
 text=p.read_text(encoding="utf-8");texts[p.name]=text
 assert "\ufffd" not in text and "\u00c3" not in text and "\u00e2\u0080" not in text,p
 for label,target in re.findall(r"\[([^\]]+)\]\((<[^>]+>|[^)]+)\)",text):
  target=target.strip("<>")
  if target.startswith(("http://","https://","#")):continue
  m=re.fullmatch(r"(.*?)(?::(\d+))?",target);path=Path(m[1]);n=int(m[2]) if m[2] else None
  if not path.is_file():errors.append({"document":p.name,"target":target,"error":"missing file"});continue
  if n:
   contents=path.read_text(encoding="utf-8-sig").splitlines()
   if not 1<=n<=len(contents):errors.append({"document":p.name,"target":target,"error":"invalid line"})
  if "claude-work" in path.parts and path.name.startswith("R13-"):errors.append({"error":"forbidden citation","target":str(path)})
  links.append({"document":p.name,"label":label,"file":str(path),"line":n})
headings=re.findall(r"^### Rank (\d+) \u2014 (P\d+):",texts["R13-PROPOSALS-CODEX.md"],re.M)
assert len(headings)==7 and {i for _,i in headings}=={f"P{i}" for i in range(7)},headings
assert len(json.loads((ROOT/"R13-paper-index.json").read_text()))==13
expected={
("w07","U"):[665,11,74.7,68.3,208.2,None,0],
("w07","C-30"):[660,2,6.0,2.0,10.0,0,0],
("w07","C-60"):[661,3,18.0,10.0,41.9,0,0],
("w07","C-90"):[664,7,49.7,68.3,86.9,1,0],
("w07","C-120"):[666,9,56.2,68.3,96.7,0,0],
("w07","C-150"):[666,9,56.2,68.3,96.7,0,0],
("w07","C-180"):[666,9,56.2,68.3,96.7,0,0],
("w07","C-240"):[665,11,74.7,68.3,208.2,0,0],
("w07","C-300"):[665,11,74.7,68.3,208.2,0,0],
("t38","U"):[2434,174,137.7,117.0,590.1,None,12],
("t38","C-30"):[2338,33,10.9,8.3,29.2,4,0]
}
raw=json.loads((ROOT/"R13-raw-verification.json").read_text());extra=json.loads((ROOT/"R13-extra-raw-verification-v2.json").read_text())
checked=[]
for s in raw["summaries"]:
 key=s["population"],s["arm"]
 if key not in expected:continue
 actual=[s["riders"],s["exposed"],round(s["S_exposed_mean_s"],1),round(s["S_exposed_p50_nearest_s"],1),round(s["S_exposed_max_s"],1),s["at_least_90pct_cap"],s["two_or_more_changes"]]
 assert actual==expected[key],(key,actual,expected[key])
 checked.append({"population":key[0],"arm":key[1],"nearest_rank_table":"MATCH","conventional_median_s":s["S_exposed_median_conventional_s"],"conventional_median_matches_p50_rounding":round(s["S_exposed_median_conventional_s"],1)==round(s["S_exposed_p50_nearest_s"],1)})
assert all(x["exact_identity"] for x in raw["budget_vector_identity"])
assert raw["existence"]=={"w07_C120_runs":8,"t38_C120_folders":0,"synthetic_C120_transcripts":13}
assert {(s["population"],s["arm"]):s["runs"] for s in extra["summary"]}=={("WP14r","C-120"):16,("WP14r","FREE"):16,("synthetic","C-120"):13}
ast_checks=[]
for p in sorted(ROOT.glob("R13-*.py")):
 ast.parse(p.read_text(encoding="utf-8"));ast_checks.append(p.name)
inventory=[]
for p in sorted(ROOT.glob("R13-*")):
 if p.is_file():inventory.append({"name":p.name,"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()})
for folder in ["r13-paper-text","r13-paper-images"]:
 for p in sorted((ROOT/folder).iterdir()):
  if p.is_file():inventory.append({"name":p.relative_to(ROOT).as_posix(),"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()})
assert not errors,errors
result={"local_links_checked":len(links),"link_errors":errors,"papers":13,"ranked_proposals":headings,"main_raw_runs":len(raw["runs"]),"extra_raw_runs":len(extra["runs"]),"verified_frames":raw["total_verified_frames"]+extra["verified_frames"],"budget_rows":checked,"script_syntax_checked":ast_checks,"outputs":inventory,"limitations":"Checks validate links, arithmetic, UTF8 and script syntax; they do not validate every substantive literature inference, certify future proposals, or execute builds/simulations."}
with (ROOT/"R13-final-qa.json").open("x",encoding="utf-8",newline="\n") as f:json.dump(result,f,indent=2)
print(json.dumps({k:v for k,v in result.items() if k not in ["outputs","budget_rows","script_syntax_checked"]}),flush=True)
