#!/usr/bin/env python3
"""Download an archive.org item's PDF + text layer and record verification facts.

Usage: ia_get.py <identifier> <dest_dir>
Writes <dest_dir>/<identifier>/{<id>.pdf,<id>_djvu.txt,_meta.json}
Prints one JSON line of verification evidence.
"""
import json, sys, os, urllib.request, hashlib

UA = {"User-Agent": "ACU-acquisition/1.0 (scholarly text collection)"}

def fetch(url, timeout=180):
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req, timeout=timeout)

def main():
    ident, dest = sys.argv[1], sys.argv[2]
    out = os.path.join(dest, ident)
    os.makedirs(out, exist_ok=True)

    md = json.load(fetch(f"https://archive.org/metadata/{ident}"))
    m = md.get("metadata", {})
    files = md.get("files", [])

    want = {}
    for f in files:
        fmt, name = f.get("format"), f.get("name", "")
        if fmt in ("Text PDF", "Image Container PDF") and "pdf" not in want:
            want["pdf"] = f
        if fmt == "DjVuTXT" and "txt" not in want:
            want["txt"] = f

    got = {}
    for kind, f in want.items():
        name = f["name"]
        path = os.path.join(out, name)
        url = f"https://archive.org/download/{ident}/{urllib.parse.quote(name)}"
        if os.path.exists(path) and str(os.path.getsize(path)) == str(f.get("size", -1)):
            got[kind] = path  # already complete
            continue
        h = hashlib.sha1()
        with fetch(url) as r, open(path, "wb") as w:
            while True:
                chunk = r.read(1 << 20)
                if not chunk:
                    break
                w.write(chunk); h.update(chunk)
        exp = f.get("sha1")
        if exp and h.hexdigest() != exp:
            print(json.dumps({"id": ident, "error": f"sha1 mismatch on {name}"}))
            sys.exit(2)
        got[kind] = path

    json.dump(md, open(os.path.join(out, "_meta.json"), "w"), indent=1)

    # verification evidence: first real lines of the text layer
    head = ""
    if "txt" in got:
        with open(got["txt"], encoding="utf-8", errors="replace") as fh:
            lines = [l.strip() for l in fh.read(20000).splitlines() if l.strip()]
        head = " / ".join(lines[:12])[:600]

    print(json.dumps({
        "id": ident,
        "title": m.get("title"),
        "creator": m.get("creator"),
        "date": m.get("date"),
        "language": m.get("language"),
        "rights": m.get("possible-copyright-status"),
        "pages": m.get("imagecount"),
        "files": {k: (os.path.relpath(v), os.path.getsize(v)) for k, v in got.items()},
        "text_head": head,
    }, ensure_ascii=False))

if __name__ == "__main__":
    import urllib.parse
    main()
