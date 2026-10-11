#!/usr/bin/env python3
"""Score candidates by fetching metadata + the head of the text layer.

For each ACU target, picks the best downloadable candidate and checks that
the text actually contains distinctive words from the work's title.
Usage: auto_verify.py cand.json out.json
"""
import json, sys, re, time, urllib.request, urllib.parse, concurrent.futures as cf

UA = {"User-Agent": "ACU-acquisition/1.0"}
STOP = set("the of and a an in on to le la les de du des el los las il i "
           "et and or der die das von zu y e a o del della di dei".split())

def get(url, timeout=40, tries=2):
    for i in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read()
        except Exception:
            if i < tries - 1: time.sleep(1)
    return None

def keywords(title):
    t = re.sub(r"[^\w\s'’-]", " ", re.sub(r"\(.*?\)", " ", title), flags=re.U)
    ws = [w for w in t.split() if len(w) > 3 and w.lower() not in STOP]
    return ws[:6]

def check(job):
    acu, work, lang, cands = job["acu"], job["work"], job["lang"], job["candidates"]
    kws = keywords(work)
    best = None
    for c in cands:
        if c.get("_lending"): continue
        ident = c["identifier"]
        raw = get(f"https://archive.org/metadata/{ident}")
        if not raw: continue
        try: md = json.loads(raw)
        except Exception: continue
        m = md.get("metadata", {})
        files = md.get("files", [])
        if m.get("access-restricted-item") in ("true", True): continue
        has_pdf = any(f.get("format") in ("Text PDF","Image Container PDF") for f in files)
        txtf = next((f["name"] for f in files if f.get("format") == "DjVuTXT"), None)
        if not has_pdf: continue
        score, hits, head = 0, [], ""
        if txtf:
            body = get(f"https://archive.org/download/{ident}/{urllib.parse.quote(txtf)}", timeout=60)
            if body:
                head = body[:400000].decode("utf-8", "replace")
                hits = [k for k in kws if re.search(re.escape(k), head, re.I)]
                score = len(hits)
        cand = {"identifier": ident, "title": m.get("title"), "creator": m.get("creator"),
                "date": m.get("date"), "language": m.get("language"),
                "rights": m.get("possible-copyright-status"), "pages": m.get("imagecount"),
                "has_text_layer": bool(txtf), "kw_hits": hits, "kw_total": len(kws),
                "score": score}
        if best is None or score > best["score"]:
            best = cand
        if kws and score == len(kws):
            break           # perfect match, stop early
    return {"acu": acu, "work": work, "lang": lang, "keywords": kws, "best": best}

jobs = [j for j in json.load(open(sys.argv[1])) if j["candidates"]]
out = []
with cf.ThreadPoolExecutor(max_workers=5) as ex:
    for i, r in enumerate(ex.map(check, jobs), 1):
        out.append(r)
        if i % 10 == 0: print(f"  ...{i}/{len(jobs)}", flush=True)
json.dump(out, open(sys.argv[2], "w"), indent=1)

strong = [r for r in out if r["best"] and r["keywords"] and r["best"]["score"] >= max(2, len(r["keywords"])//2)]
weak   = [r for r in out if r["best"] and r not in strong]
print(f"verified-strong {len(strong)} | weak {len(weak)} | no usable candidate {len(jobs)-len(out)+sum(1 for r in out if not r['best'])}")
