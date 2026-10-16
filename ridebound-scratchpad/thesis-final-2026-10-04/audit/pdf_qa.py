"""Extract final-size PDF text/bounds and render every page for visual inspection."""
from pathlib import Path
import sys, json, argparse, collections
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'runtime'))
import pymupdf
sys.stdout.reconfigure(encoding='utf-8')
ap = argparse.ArgumentParser()
ap.add_argument('pdf')
ap.add_argument('--out', required=True)
ap.add_argument('--render', action='store_true')
ap.add_argument('--dpi', type=int, default=130)
args = ap.parse_args()
out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
doc = pymupdf.open(args.pdf)
records = []; all_text = []
for index, page in enumerate(doc):
    plain = page.get_text()
    all_text.append(f'\n\n===== PHYSICAL PAGE {index+1} =====\n{plain}')
    fonts = collections.Counter(); overflow = []
    for block in page.get_text('dict')['blocks']:
        if 'lines' not in block: continue
        for line in block['lines']:
            for span in line['spans']:
                fonts[(span['font'], round(span['size'], 2))] += len(span['text'])
                x0,y0,x1,y1 = span['bbox']
                if x0 < 0 or x1 > page.rect.width+.5 or y0 < 0 or y1 > page.rect.height+.5:
                    overflow.append({'text': span['text'], 'bbox': list(span['bbox'])})
    records.append({'physicalPage': index+1, 'textCharacters': len(plain),
                    'fonts': [{'font':k[0],'size':k[1],'characters':v} for k,v in fonts.items()],
                    'outsidePageSpans': overflow})
    if args.render:
        page.get_pixmap(dpi=args.dpi, alpha=False).save(out/f'page-{index+1:03d}.png')
(out/'text.txt').write_text(''.join(all_text), encoding='utf-8')
(out/'pdf-inspection.json').write_text(json.dumps({'path':args.pdf, 'pages':len(doc),
    'pageSizePoints':list(doc[0].rect), 'outline':doc.get_toc(), 'records':records},ensure_ascii=False,indent=1),encoding='utf-8')
print(json.dumps({'pages':len(doc),'outline':doc.get_toc(),
                  'outsidePageSpans':sum(len(x['outsidePageSpans']) for x in records),
                  'emptyPages':[x['physicalPage'] for x in records if x['textCharacters']<20]},ensure_ascii=False))
