from pathlib import Path
import subprocess, json

OUT = Path(__file__).resolve().parent
POPPLER = r'C:/Program Files/Git/mingw64/bin/pdftotext.exe'
S = Path('E:/Code/Report_INT3508/ridebound-scratchpad')
TEMP = Path('C:/Users/quang/AppData/Local/Temp/claude/e--Code-RideBound/4f238113-dd3b-4bd1-b13f-53613b57f0e6/scratchpad')
sources = {
    'AM17': (Path('E:/RideBoundData/literature-survey-2026-10-06/pdf/alonso-mora-pnas2017.pdf'), [3,4,5]),
    'FAM': (Path('C:/PDF/Paper/Unreliability_in_ridesharing_systems_Measuring_cha.pdf'), [1,4,5,7,9,17,18]),
    'FLEET': (S/'optimize/codex-debate/claude-work/pdf/fleetpy-etrr-2026.pdf', [10,11]),
    'MOL': (Path('C:/PDF/Paper/OperationalEffectsofServiceLevelVariations-publication151005.pdf'), [3,5]),
    'LEO': (S/'optimize/codex-debate/claude-work/pdf/leonardi-2024.pdf', [2,4]),
    'LUK': (S/'optimize/codex-debate/claude-work/pdf/lu-kuehnel-2024.pdf', [4]),
    'DRE': (TEMP/'ch2/dl-deepreta/2206.02127.pdf', [1,3]),
    'WAR': (Path('C:/PDF/Paper/1-s2.0-S0965856426000662-main.pdf'), [2,3,10]),
    'AGZ': (Path('C:/PDF/Paper/Value_of_time_and_reliability_for_urban_pooled_on-.pdf'), [1,11,13]),
}
manifest = []
for key, (path, pages) in sources.items():
    parts = [f'Source: {path.as_posix()}\nMode: pdftotext -layout; PDF page numbers\n']
    for page in pages:
        r = subprocess.run([POPPLER, '-layout', '-enc', 'UTF-8', '-f', str(page), '-l', str(page), str(path), '-'], capture_output=True)
        if r.returncode:
            parts.append(f'\n[PDF page {page}: ERROR]\n{r.stderr.decode("utf-8", errors="replace")}')
        else:
            parts.append(f'\n[PDF page {page}]\n{r.stdout.decode("utf-8").replace(chr(12), "")}')
    target = OUT/f'r35-source-{key}.txt'
    with target.open('x', encoding='utf-8', newline='\n') as f:
        f.write(''.join(parts))
    manifest.append({'key':key, 'source':str(path), 'exists':path.exists(), 'pages':pages, 'output':str(target)})
    print(key, path.exists(), len(''.join(parts)))
with (OUT/'r35-extraction-manifest.json').open('x', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2)
