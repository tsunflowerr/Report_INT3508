"""R16 (2026-10-10): read ONLY the parquet footer of one Azure Open Datasets nyctlc blob, with CLOSED byte ranges and
the x-ms-version header (an earlier attempt with the R13 probe got the whole object back because the open-ended range
was ignored; nothing was saved to disk by that attempt except the tool's own console capture). Every response is
refused if it is larger than 2 MB. Reuses the thrift decoder of r13-ml-data-samples/parquet_footer_probe.py by
executing only its decoder part (the text before its I/O loop).
Usage: python -I -B azure_footer_probe.py <out-file> <blob-url>   (mode "x")
"""
import importlib.util
import pathlib
import struct
import sys
import urllib.request

CAP = 2_000_000
HDR = {"User-Agent": "Mozilla/5.0 research-footer-probe", "x-ms-version": "2020-10-02"}


def head_size(url):
    req = urllib.request.Request(url, headers=HDR, method="HEAD")
    with urllib.request.urlopen(req, timeout=60) as r:
        return int(r.headers["Content-Length"])


def get(url, start, end):
    req = urllib.request.Request(url, headers={**HDR, "Range": f"bytes={start}-{end}"})
    with urllib.request.urlopen(req, timeout=60) as r:
        length = int(r.headers.get("Content-Length", "0"))
        if r.status != 206 or length > CAP:
            raise SystemExit(f"refused: status {r.status}, length {length}")
        return r.read(CAP)


def main(out, url):
    probe_path = pathlib.Path(__file__).resolve().parents[1] / "r13-ml-data-samples" / "parquet_footer_probe.py"
    source = probe_path.read_text(encoding="utf-8")
    source = source[:source.index("lines = []")]        # decoder only; the probe's own I/O loop is NOT executed
    mod = type(sys)("probe")
    exec(compile(source, str(probe_path), "exec"), mod.__dict__)
    n = head_size(url)
    tail = get(url, n - 8, n - 1)
    assert tail[4:] == b"PAR1", tail[:16]
    mlen = struct.unpack("<I", tail[:4])[0]
    if mlen > CAP:
        raise SystemExit(f"footer too large {mlen}")
    meta = get(url, n - 8 - mlen, n - 9)
    m = mod.file_meta(meta)
    cols = [f"{e.get('name')}:{mod.PTYPE.get(e.get('type'), '-')}" for e in m["schema"][1:]]
    text = (f"{url.rsplit('/', 1)[-1]}: bytes {n}; footer {mlen} B; rows {m['num_rows']}; columns {len(cols)}: "
            + ", ".join(cols) + "\n")
    with open(out, "x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(text)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
