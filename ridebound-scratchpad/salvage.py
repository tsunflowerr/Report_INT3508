import json, os, re, sys

D = r"C:\Users\quang\.claude\projects\e--Code-RideBound\c0a62edb-0448-4938-91bf-6a1fb8378ce9\subagents\workflows\wf_96d9b11d-16e"
OUT = r"C:\Users\quang\AppData\Local\Temp\claude\e--Code-RideBound\c0a62edb-0448-4938-91bf-6a1fb8378ce9\scratchpad\salvage"
os.makedirs(OUT, exist_ok=True)

ANGLE_RE = re.compile(r"# YOUR TASK -- literature angle: ([a-z\-]+)")
LENS_RE = re.compile(r"# YOUR TASK\n(LENS: [A-Z][^\n]*)")


def blocks(msg):
    c = msg.get("content")
    if isinstance(c, str):
        return [{"type": "text", "text": c}]
    if isinstance(c, list):
        return c
    return []


def text_of(b):
    if isinstance(b, dict):
        if b.get("type") == "text":
            return b.get("text", "")
        if b.get("type") == "tool_result":
            c = b.get("content")
            if isinstance(c, str):
                return c
            if isinstance(c, list):
                return "\n".join(
                    x.get("text", "") for x in c if isinstance(x, dict)
                )
    return ""


index = []

for fn in sorted(os.listdir(D)):
    if not fn.endswith(".jsonl") or fn == "journal.jsonl":
        continue
    path = os.path.join(D, fn)
    rows = []
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except Exception:
                pass
    if not rows:
        continue

    # identify the agent from its first user prompt
    first = ""
    for r in rows:
        if r.get("type") == "user":
            first = "".join(text_of(b) for b in blocks(r.get("message", {})))
            break
    m = ANGLE_RE.search(first)
    if m:
        label = "lit-" + m.group(1)
    else:
        m2 = LENS_RE.search(first)
        label = ("design-" + m2.group(1)[6:40].lower().replace(" ", "-").replace("/", "-")) if m2 else "unknown-" + fn[6:14]

    searches = []      # (query, [urls])
    fetches = []       # (url, prompt, answer)
    notes = []         # assistant prose
    pending = {}       # tool_use_id -> (kind, meta)

    for r in rows:
        msg = r.get("message", {})
        role = msg.get("role")
        for b in blocks(msg):
            if not isinstance(b, dict):
                continue
            t = b.get("type")
            if role == "assistant" and t == "text":
                s = (b.get("text") or "").strip()
                if len(s) > 40:
                    notes.append(s)
            elif t == "tool_use":
                name = b.get("name")
                inp = b.get("input") or {}
                if name == "WebSearch":
                    pending[b.get("id")] = ("search", inp.get("query", ""))
                elif name == "WebFetch":
                    pending[b.get("id")] = ("fetch", (inp.get("url", ""), inp.get("prompt", "")))
            elif t == "tool_result":
                tid = b.get("tool_use_id")
                if tid not in pending:
                    continue
                kind, meta = pending.pop(tid)
                body = text_of(b)
                if kind == "search":
                    urls = re.findall(r'"url":"([^"]+)"', body)
                    if not urls:
                        urls = re.findall(r"https?://[^\s\"')\]]+", body)
                    searches.append((meta, urls[:14], body))
                else:
                    fetches.append((meta[0], meta[1], body))

    out_path = os.path.join(OUT, label + ".md")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("# " + label + "  (source: " + fn + ")\n\n")
        fh.write("## Searches (%d)\n\n" % len(searches))
        for q, urls, _ in searches:
            fh.write("### QUERY: " + q + "\n")
            for u in urls:
                fh.write("  - " + u + "\n")
            fh.write("\n")
        fh.write("\n## Papers actually FETCHED and READ (%d)\n\n" % len(fetches))
        for url, prompt, body in fetches:
            fh.write("\n" + "=" * 78 + "\n")
            fh.write("URL: " + url + "\n")
            fh.write("ASKED: " + prompt[:300].replace("\n", " ") + "\n")
            fh.write("-" * 78 + "\n")
            fh.write(body.strip()[:9000] + "\n")
        fh.write("\n\n## Agent prose notes (%d)\n\n" % len(notes))
        for n in notes:
            fh.write("- " + n[:2500] + "\n\n")

    index.append((label, len(searches), len(fetches), len(notes), os.path.getsize(out_path)))

print("%-34s %8s %8s %7s %10s" % ("LABEL", "searches", "fetched", "notes", "bytes"))
for row in sorted(index):
    print("%-34s %8d %8d %7d %10d" % row)
print("\nwrote to", OUT)
