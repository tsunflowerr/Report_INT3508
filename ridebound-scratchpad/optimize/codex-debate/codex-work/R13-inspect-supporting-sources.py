"""Source-inspection helpers used for Round13. Run only in a fresh output state.
Downloads are separate; this reads the saved HTTP responses and creates new extracts.
"""
from pathlib import Path
from html.parser import HTMLParser
import re
ROOT=Path(__file__).resolve().parent
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.bits=[];self.skip=0
 def handle_starttag(self,tag,attrs):
  if tag in ["script","style"]:self.skip+=1
  if tag in ["p","h1","h2","h3","li","br"]:self.bits.append("\n")
 def handle_endtag(self,tag):
  if tag in ["script","style"]:self.skip-=1
 def handle_data(self,s):
  if not self.skip:self.bits.append(s)
for name in ["lyft-help","grubhub-terms"]:
 p=Parser();p.feed((ROOT/("R13-public-"+name+".txt")).read_text(encoding="utf-8"))
 text="\n".join(re.sub(r"\s+"," ",v).strip() for v in "".join(p.bits).splitlines() if v.strip())
 with (ROOT/("R13-public-"+name+"-clean.txt")).open("x",encoding="utf-8") as f:f.write(text+"\n")
 for n,line in enumerate(text.splitlines(),1):
  if any(s in line.lower() for s in ["latest","original","delivery estimate","late","credits","guarantee","minutes"]):print(name,n,line[:1600])
s=(ROOT/"R13-public-nyc-tlc-page.txt").read_text()
for url in re.findall(r'href="([^"]+)"',s):
 if any(x in url for x in ["2018-10","2018-11","2019-02","user_guide"]):print("TLC_LINK",url)
