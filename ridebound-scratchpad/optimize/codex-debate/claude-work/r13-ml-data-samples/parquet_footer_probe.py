"""R13 (2026-10-09): read ONLY the parquet footer (file metadata) of TLC monthly files via HTTP range requests,
then list column names and the total row count. No row data is downloaded.
Parquet layout: ... <FileMetaData (thrift compact)> <4-byte LE metadata length> b"PAR1".
The thrift compact decoder below handles exactly the FileMetaData fields needed (1 version, 2 schema list,
3 num_rows) and skips everything else generically.
Usage: python -I -B parquet_footer_probe.py <out-file> <url> [<url> ...]   (mode "x"; saves nothing else)
"""
import struct, sys, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) research-footer-probe"}


def get_range(url, start, end=None):
    rng = f"bytes={start}-" if end is None else f"bytes={start}-{end}"
    req = urllib.request.Request(url, headers={**UA, "Range": rng})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def size_of(url):
    req = urllib.request.Request(url, headers=UA, method="HEAD")
    with urllib.request.urlopen(req, timeout=60) as r:
        return int(r.headers["Content-Length"])


class R:
    def __init__(self, b):
        self.b, self.i = b, 0

    def byte(self):
        v = self.b[self.i]; self.i += 1; return v

    def varint(self):
        s = v = 0
        while True:
            x = self.byte(); v |= (x & 0x7F) << s; s += 7
            if not x & 0x80:
                return v

    def zz(self):
        v = self.varint(); return (v >> 1) ^ -(v & 1)

    def binary(self):
        n = self.varint(); v = self.b[self.i:self.i + n]; self.i += n; return v

    def skip(self, t):
        if t in (1, 2):
            return
        if t in (3, 4, 5, 6):
            self.varint() if t != 3 else self.byte(); return
        if t == 7:
            self.i += 8; return
        if t == 8:
            self.binary(); return
        if t in (9, 10):
            h = self.byte(); n = h >> 4; et = h & 0x0F
            if n == 15:
                n = self.varint()
            for _ in range(n):
                self.skip(et)
            return
        if t == 11:
            n = self.varint()
            if n:
                kv = self.byte()
                for _ in range(n):
                    self.skip(kv >> 4); self.skip(kv & 0x0F)
            return
        if t == 12:
            self.struct(lambda fid, ft: False); return
        raise ValueError(f"type {t}")

    def struct(self, handler):
        last = 0
        while True:
            h = self.byte()
            if h == 0:
                return
            t = h & 0x0F; d = h >> 4
            fid = last + d if d else self.zz()
            last = fid
            if not handler(fid, t):
                self.skip(t)


def file_meta(buf):
    r = R(buf); out = {"schema": [], "num_rows": None}

    def schema_elem():
        el = {}

        def h(fid, t):
            if fid == 1 and t == 5:
                el["type"] = r.zz(); return True
            if fid == 4 and t == 8:
                el["name"] = r.binary().decode("utf-8", "replace"); return True
            if fid == 6 and t == 5:
                el["converted"] = r.zz(); return True
            return False
        r.struct(h)
        return el

    def top(fid, t):
        if fid == 2 and t == 9:
            h = r.byte(); n = h >> 4
            if n == 15:
                n = r.varint()
            for _ in range(n):
                out["schema"].append(schema_elem())
            return True
        if fid == 3 and t == 6:
            out["num_rows"] = r.zz(); return True
        return False
    r.struct(top)
    return out


PTYPE = {0: "BOOLEAN", 1: "INT32", 2: "INT64", 3: "INT96", 4: "FLOAT", 5: "DOUBLE", 6: "BYTE_ARRAY", 7: "FIXED"}
lines = []
for url in sys.argv[2:]:
    n = size_of(url)
    tail = get_range(url, n - 8)
    assert tail[4:] == b"PAR1", tail
    mlen = struct.unpack("<I", tail[:4])[0]
    meta = get_range(url, n - 8 - mlen, n - 9)
    m = file_meta(meta)
    cols = [f"{e.get('name')}:{PTYPE.get(e.get('type'), '-')}" for e in m["schema"][1:]]
    lines.append(f"{url.rsplit('/', 1)[-1]}: bytes {n}; footer {mlen} B; rows {m['num_rows']}; columns {len(cols)}: "
                 + ", ".join(cols))
text = "\n".join(lines) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text)
print(text)
