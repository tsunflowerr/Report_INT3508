from pathlib import Path
import subprocess,json,hashlib,re
root=Path('E:/Code/RideBound')
out=Path('E:/Code/Report_INT3508/ridebound-scratchpad/conduct-outcome-plan-2026-09-22')
raw=subprocess.check_output(['git','ls-files','-z','--cached','--others','--exclude-standard'],cwd=root).decode('utf8').split('\0')
exts={'.cs','.py','.ps1','.sh','.ts','.tsx','.js','.jsx','.yml','.yaml','.csproj','.props','.slnx','.toml'}
files=[]
for rel in sorted(set(raw)):
 p=root/rel
 if not rel or not p.is_file() or p.suffix not in exts: continue
 if any(s in {'bin','obj','__pycache__','.git','vendor','node_modules'} for s in p.parts):continue
 files.append(rel)
priority=['src/RideBound.Domain','src/RideBound.Application','src/RideBound.Algorithms','src/RideBound.Runner','src/RideBound.Contracts','src/RideBound.Benchmarking','src/RideBound.Solvers','src/RideBound.Infrastructure','tests','simulators','tools','scripts','.github']
files.sort(key=lambda x:(next((i for i,k in enumerate(priority) if x.startswith(k)),99),x))
manifest=[];chunks=[];buf=[];size=0;linecount=0
for rel in files:
 p=root/rel;b=p.read_bytes(); lines=b.decode('utf-8-sig').splitlines()
 manifest.append({'path':rel,'bytes':len(b),'lines':len(lines),'sha256':hashlib.sha256(b).hexdigest()})
 for start in range(0,len(lines),180):
  part=lines[start:start+180]
  text=f'\nFILE {rel} L{start+1}-{start+len(part)}\n'+'\n'.join(f'{start+i+1}:{l.rstrip()}' for i,l in enumerate(part) if l.strip())+'\n'
  if size+len(text)>34000 and buf:
   chunks.append(''.join(buf));buf=[];size=0
  buf.append(text);size+=len(text);linecount+=len(part)
if buf:chunks.append(''.join(buf))
(out/'code-reading').mkdir(exist_ok=True)
for i,c in enumerate(chunks,1):(out/'code-reading'/f'{i:03d}.txt').write_text(c,encoding='utf8')
(out/'source-inventory.json').write_text(json.dumps({'root':str(root),'head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=root).decode().strip(),'files':manifest,'chunks':len(chunks),'totalLines':linecount},indent=2),encoding='utf8')
(out/'reading-progress.json').write_text(json.dumps({'readChunks':[],'next':1,'note':'Inventory/snapshot is not reading; acknowledge each chunk only after inspecting its full output.'},indent=2),encoding='utf8')
print(json.dumps({'files':len(files),'lines':linecount,'bytes':sum(x['bytes'] for x in manifest),'chunks':len(chunks)},indent=2))
