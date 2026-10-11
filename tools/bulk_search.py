#!/usr/bin/env python3
"""Query archive.org's search API for each catalog target. Emits candidates.

Usage: bulk_search.py targets.json out.json [start] [end]
"""
import json, sys, re, time, urllib.request, urllib.parse, concurrent.futures as cf

UA = {"User-Agent": "ACU-acquisition/1.0"}
SEARCH = "https://archive.org/advancedsearch.php"

def api(params, tries=3):
    url = SEARCH + "?" + urllib.parse.urlencode(params, doseq=True)
    for i in range(tries):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=45)
            return json.loads(r.read())
        except Exception:
            if i < tries - 1: time.sleep(1.5 * (i + 1))
    return None

def clean(title):
    t = re.sub(r"\(.*?\)", " ", title)           # drop parentheticals
    t = re.sub(r"\[.*?\]", " ", t)
    t = t.split("/")[0]                           # drop "X / Y" alternates
    t = re.sub(r"[^\w\s'’-]", " ", t, flags=re.U)
    return " ".join(t.split())

def queries(work):
    """Several shots per work, broad to narrow."""
    base = clean(work)
    qs = []
    if base:
        qs.append(f'mediatype:texts AND title:("{base}")')
        words = base.split()
        if len(words) > 3:                        # first significant chunk
            qs.append(f'mediatype:texts AND title:("{" ".join(words[:3])}")')
        qs.append(f'mediatype:texts AND ("{base}")')
    # alternate title after a slash, if any
    if "/" in work:
        alt = clean(work.split("/", 1)[1])
        if alt and alt != base:
            qs.append(f'mediatype:texts AND title:("{alt}")')
    return qs

FIELDS = ["identifier","title","creator","date","language","year"]

def search_one(t):
    seen, out = set(), []
    for q in queries(t["work"]):
        d = api({"q": q, "fl[]": FIELDS, "rows": 12, "page": 1,
                 "output": "json", "sort[]": "date asc"})
        if not d: continue
        for doc in d.get("response", {}).get("docs", []):
            ident = doc.get("identifier")
            if not ident or ident in seen: continue
            seen.add(ident)
            # lending-library scans can't be downloaded
            if re.search(r"0000[a-z0-9_]*$", ident) or ident.startswith("bwb_"):
                doc["_lending"] = True
            out.append(doc)
        if len(out) >= 14: break
    return {"acu": t["id"], "work": t["work"], "lang": t["lang"],
            "status": t["status"], "candidates": out}

targets = json.load(open(sys.argv[1]))
a = int(sys.argv[3]) if len(sys.argv) > 3 else 0
b = int(sys.argv[4]) if len(sys.argv) > 4 else len(targets)
targets = targets[a:b]

res = []
with cf.ThreadPoolExecutor(max_workers=6) as ex:
    for i, r in enumerate(ex.map(search_one, targets), 1):
        res.append(r)
        if i % 25 == 0: print(f"  ...{i}/{len(targets)}", flush=True)

json.dump(res, open(sys.argv[2], "w"), indent=1)
hit = sum(1 for r in res if r["candidates"])
dl  = sum(1 for r in res if any(not c.get("_lending") for c in r["candidates"]))
print(f"searched {len(res)} | any candidate {hit} | downloadable candidate {dl}")
