from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/"r13-pdf-deps-manual"))
import pypdfium2 as pdfium
OUT=ROOT/"r13-paper-images"
OUT.mkdir(exist_ok=False)
pdf=pdfium.PdfDocument("C:/PDF/Paper/21020283-3476 (1).pdf")
for page in [46,47,48,49]:
    bitmap=pdf[page-1].render(scale=1.6)
    image=bitmap.to_pil()
    with (OUT/f"example-thesis-p{page}.png").open("xb") as stream:image.save(stream,format="PNG")
    print(page,image.size,flush=True)
