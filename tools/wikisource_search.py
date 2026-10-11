#!/usr/bin/env python3
"""Search Wikisource (several languages) for catalog targets.

Wikisource pages ARE transcriptions, so a hit is a usable text, not a scan.
Usage: wikisource_search.py targets.json out.json
"""
import json, sys, re, urllib.request, urllib.parse, concurrent.futures as cf

UA = {"User-Agent": "ACU-acquisition/1.0 (scholarly text collection)"}
# catalog language -> wikisource subdomains worth trying, best first
WIKIS = {
 "welsh": ["cy", "en"], "latin": ["la", "en"], "irish": ["ga", "en"],
 "old french": ["fr"], "middle french": ["fr"], "anglo-norman": ["fr", "en"],
 "occitan": ["oc", "fr"], "middle english": ["en"], "early modern english": ["en"],
 "early middle english": ["en"], "english": ["en"], "middle high german": ["de"],
 "early new high german": ["de"], "german": ["de"], "italian": ["it"],
 "spanish": ["es"], "portuguese": ["pt"], "middle dutch": ["nl"], "dutch": ["nl"],
 "old norse": ["is", "no"], "icelandic": ["is"], "old swedish": ["sv"],
 "old danish": ["da"], "byzantine greek": ["el"], "greek": ["el"],
 "scottish gaelic": ["gd", "en"], "middle scots": ["en"], "venetian": ["it"],
 "czech": ["cs"], "hebrew": ["he"], "old english": ["en"], "navarrese spanish": ["es"],
}

def api(wiki, params):
    url = f"https://{wiki}.wikisource.org/w/api.php?" + urllib.parse.urlencode(params)
    try:
        r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=35)
        return json.loads(r.read())
    except Exception:
        return None

def clean(t):
    t = re.sub(r"\(.*?\)", " ", t)
    t = t.split("/")[0]
    return " ".join(t.split())

def one(t):
    wikis = []
    for k, v in WIKIS.items():
        if k in t["lang"].lower():
            wikis = v; break
    if not wikis: wikis = ["en"]
    hits = []
    q = clean(t["work"])
    for w in wikis:
        d = api(w, {"action": "query", "list": "search", "srsearch": q,
                    "srlimit": 5, "srnamespace": 0, "format": "json"})
        if not d: continue
        for s in d.get("query", {}).get("search", []):
            hits.append({
                "wiki": w, "title": s["title"],
                "url": f"https://{w}.wikisource.org/wiki/" + urllib.parse.quote(s["title"].replace(" ", "_")),
                "words": s.get("wordcount"),
                "snippet": re.sub(r"<[^>]+>", "", s.get("snippet", ""))[:180],
            })
        if hits: break
    return {"acu": t["id"], "work": t["work"], "lang": t["lang"], "hits": hits}

targets = json.load(open(sys.argv[1]))
res = []
with cf.ThreadPoolExecutor(max_workers=8) as ex:
    for i, r in enumerate(ex.map(one, targets), 1):
        res.append(r)
        if i % 40 == 0: print(f"  ...{i}/{len(targets)}", flush=True)
json.dump(res, open(sys.argv[2], "w"), indent=1)
print("targets with wikisource hits:", sum(1 for r in res if r["hits"]))
