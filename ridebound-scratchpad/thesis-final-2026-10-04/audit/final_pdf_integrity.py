"""Read-only checks on the final compiled PDF; no experiments or PDF mutation."""
from pathlib import Path
import hashlib, json, re, sys, collections
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'runtime'))
import pymupdf
sys.stdout.reconfigure(encoding='utf-8')
pdf = Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'build'/'main.pdf'
doc = pymupdf.open(pdf)
font_xrefs = {}
for page in doc:
    for entry in page.get_fonts(full=True):
        font_xrefs[entry[0]] = entry
fonts = []
for xref, entry in sorted(font_xrefs.items()):
    name, ext, kind, data = doc.extract_font(xref)
    fonts.append(dict(xref=xref, name=name, extension=ext, kind=kind,
                      embeddedBytes=len(data), embedded=bool(data)))
assert all(f['embedded'] for f in fonts), 'Unembedded font'
links=[]; invalid=[]
for i,page in enumerate(doc,1):
    for link in page.get_links():
        record=dict(physicalPage=i, kind=link['kind'])
        if link['kind'] in (pymupdf.LINK_GOTO, pymupdf.LINK_NAMED) and 'page' in link:
            record['targetPhysicalPage']=link.get('page',-1)+1
            if 'nameddest' in link: record['namedDestination']=link['nameddest']
            if not 0<=link.get('page',-1)<len(doc): invalid.append(record)
        elif link['kind']==pymupdf.LINK_URI:
            record['uri']=link.get('uri','')
            if not re.match(r'https?://',record['uri']): invalid.append(record)
        else:
            record['details']=str(link)
            invalid.append(record)
        links.append(record)
assert not invalid, {'count':len(invalid),'first':invalid[:3]}
toc=doc.get_toc()
assert all(1<=r[2]<=len(doc) for r in toc)
footers=[page.get_text().strip().splitlines()[-1].strip() for page in doc]
assert footers[2:12]==['i','ii','iii','iv','v','vi','vii','viii','ix','x'], footers[2:12]
assert footers[12:]==[str(i) for i in range(1,len(doc)-11)], footers[12:]
assert len(doc)<=80
assert all(abs(page.rect.width-595.276)<1 and abs(page.rect.height-841.89)<1 for page in doc)
texts=[p.get_text() for p in doc]
assert all('??' not in t and '\ufffd' not in t for t in texts)
assert doc.metadata['author']=='Trần Quang Thành', doc.metadata
log=(ROOT/'build'/'main.log').read_text(encoding='utf-8')
log_issues={key:len(re.findall(pattern,log,re.I)) for key,pattern in {
 'overfull':r'Overfull \\hbox', 'underfull':r'Underfull \\hbox',
 'undefinedReference':r'(?:reference|citation).*undefined',
 'missingCharacter':r'Missing character', 'duplicateDestination':r'duplicate.*destination',
 'texError':r'^! '}.items()}
assert not any(log_issues.values()), log_issues
inputs=[]
source=ROOT/'source'
for p in sorted(source.rglob('*.tex')):
    inputs.append(p)
for p in list(inputs):
    for value in re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',p.read_text(encoding='utf-8')):
        image=source/value
        assert image.is_file(), str(image)
        if image not in inputs: inputs.append(image)
input_hashes=[dict(path=str(p.relative_to(source)).replace('\\','/'),bytes=p.stat().st_size,
                   sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in sorted(inputs)]
result=dict(pdf=str(pdf),sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),bytes=pdf.stat().st_size,
            pages=len(doc),metadata=doc.metadata,allFontsEmbedded=True,fonts=fonts,
            links=links,outline=toc,footerSequencePass=True,texLogIssues=log_issues,
            inputHashes=input_hashes,
            environmentNotes=['Tectonic resolves Times New Roman from C:/Windows/fonts.',
                              'Fontconfig reports no default config; actual fonts embedded and rendered.',
                              'Supervisor name/degree await user input on both covers.'])
(ROOT/'audit'/'final-pdf-integrity.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(pages=len(doc),sha256=result['sha256'],fonts=len(fonts),allFontsEmbedded=True,
                     links=len(links),invalidLinks=len(invalid),outlineEntries=len(toc),
                     inputFiles=len(input_hashes),texLogIssues=log_issues),ensure_ascii=False))
