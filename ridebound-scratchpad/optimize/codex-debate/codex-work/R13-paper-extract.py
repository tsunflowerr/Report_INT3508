from pathlib import Path
import hashlib, json, subprocess
ROOT=Path(__file__).resolve().parent
PAPERS=Path("C:/PDF/Paper")
OUT=ROOT/"r13-paper-text"
OUT.mkdir(exist_ok=False)
index=[]
for pdf in sorted(PAPERS.glob("*.pdf")):
    process=subprocess.run(["C:/Program Files/Git/mingw64/bin/pdftotext.exe","-layout","-enc","UTF-8",str(pdf),"-"],capture_output=True,check=True)
    text=process.stdout.decode("utf-8")
    pages=text.split("\f")
    if not pages[-1].strip():pages.pop()
    target=OUT/(pdf.stem+".txt")
    parts=[f"Source: {pdf.as_posix()}\nSHA256: {hashlib.sha256(pdf.read_bytes()).hexdigest()}\nPage locations below are PDF page numbers, not inferred printed pagination.\n"]
    anchors=[]
    for n,page in enumerate(pages,1):
        anchors.append({"pdf_page":n,"line":sum(part.count("\n") for part in parts)+2})
        parts.append(f"\n[PDF page {n}]\n{page.rstrip()}\n")
    with target.open("x",encoding="utf-8",newline="\n") as out:out.write("".join(parts))
    index.append({"pdf":str(pdf),"pdf_sha256":hashlib.sha256(pdf.read_bytes()).hexdigest(),"text":str(target),"pages":len(pages),"page_anchors":anchors,"extract_stderr":process.stderr.decode("utf-8",errors="replace")})
    print(pdf.name,len(pages),flush=True)
with (ROOT/"R13-paper-index.json").open("x",encoding="utf-8",newline="\n") as out:json.dump(index,out,indent=2);out.write("\n")
