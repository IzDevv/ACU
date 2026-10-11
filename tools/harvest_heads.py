#!/usr/bin/env python3
"""Fetch the opening of each candidate's text layer so a human can judge it.

Uses HTTP Range to pull only the first chunk. Strips scanning boilerplate
(Google notices, library date-due stamps) to reach the actual title page.
Usage: harvest_heads.py cand.json out.json [max_candidates_per_target]
"""
import json, sys, re, time, urllib.request, urllib.parse, concurrent.futures as cf

UA = {"User-Agent": "ACU-acquisition/1.0"}
MAXC = int(sys.argv[3]) if len(sys.argv) > 3 else 3

BOILER = re.compile(
    r"(this is a digital copy|google book search|about google book|public domain|"
    r"digitized by|date due|please note: this item is subject to recall|"
    r"university of california|presented to the library|"
    r"https?://books\.google|usage guidelines|we also ask that you)", re.I)

def req(url, rng=None, timeout=35):
    h = dict(UA)
    if rng: h["Range"] = f"bytes=0-{rng}"
    try:
        return urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=timeout).read()
    except Exception:
        return None

def opening(ident, txtname, want=900):
    raw = req(f"https://archive.org/download/{ident}/{urllib.parse.quote(txtname)}", rng=120000)
    if not raw: return ""
    text = raw.decode("utf-8", "replace")
    lines = [l.strip() for l in text.splitlines()]
    keep, skipped = [], 0
    for l in lines:
        if not l: continue
        if BOILER.search(l) and skipped < 400:
            skipped += 1; continue
        if len(l) < 3: continue
        keep.append(l)
        if sum(len(x) for x in keep) > want: break
    return " / ".join(keep)[:want]

def one(job):
    out = []
    for c in job["candidates"][:8]:
        if c.get("_lending"): continue
        ident = c["identifier"]
        raw = req(f"https://archive.org/metadata/{ident}")
        if not raw: continue
        try: md = json.loads(raw)
        except Exception: continue
        m, files = md.get("metadata", {}), md.get("files", [])
        if str(m.get("access-restricted-item")).lower() == "true": continue
        if not any(f.get("format") in ("Text PDF","Image Container PDF") for f in files): continue
        txt = next((f["name"] for f in files if f.get("format") == "DjVuTXT"), None)
        out.append({
            "identifier": ident, "title": m.get("title"), "creator": m.get("creator"),
            "date": m.get("date"), "language": m.get("language"),
            "rights": m.get("possible-copyright-status"), "pages": m.get("imagecount"),
            "opening": opening(ident, txt) if txt else "(no text layer - page images only)",
        })
        if len(out) >= MAXC: break
    return {"acu": job["acu"], "work": job["work"], "lang": job["lang"],
            "status": job["status"], "cands": out}

jobs = [j for j in json.load(open(sys.argv[1])) if j["candidates"]]
res = []
with cf.ThreadPoolExecutor(max_workers=10) as ex:
    for i, r in enumerate(ex.map(one, jobs), 1):
        res.append(r)
        if i % 20 == 0: print(f"  ...{i}/{len(jobs)}", flush=True)
json.dump(res, open(sys.argv[2], "w"), indent=1)
print("targets with at least one readable candidate:",
      sum(1 for r in res if r["cands"]))
