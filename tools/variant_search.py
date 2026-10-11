#!/usr/bin/env python3
"""Search archive.org under TITLE VARIANTS, not just the catalog's wording.

Every false negative in this project came from one spelling being searched.
Medieval titles vary by editor, language and century, so this generates
several forms per work and tries each.

Usage: variant_search.py rem.json out.json [start] [end]
"""
import json, sys, re, time, unicodedata, urllib.request, urllib.parse
import concurrent.futures as cf

UA = {"User-Agent": "ACU-text-collection/1.0"}

def strip_acc(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()

def variants(work):
    """Several plausible catalogue forms of one title."""
    out = []
    base = work
    # alternates the catalog itself gives, in ( ) or after /
    alts = re.findall(r"\(([^)]+)\)", base)
    head = re.sub(r"\([^)]*\)", " ", base)
    for part in head.split("/"):
        p = " ".join(part.split())
        if p: out.append(p)
    for a in alts:
        a = " ".join(a.split())
        # skip glosses like "Arthur sections", "fragments", MS shelfmarks
        if a and not re.match(r"(?i)^(arthur|incl|from|trans|print|the )", a) and len(a) > 5:
            out.append(a)
    base_forms = list(out)
    for b in base_forms:
        na = strip_acc(b)
        if na != b: out.append(na)
        # medieval orthography swaps, both directions
        for a_, b_ in (("v","u"),("u","v"),("c","k"),("k","c"),("y","i"),("i","y"),("ff","f"),("w","gw")):
            sw = na.replace(a_, b_)
            if sw != na and len(sw) > 5: out.append(sw)
        # drop a leading article
        d = re.sub(r"(?i)^(the|le|la|les|el|los|il|i|der|die|das|den|het|een|y|yr|an) ", "", na)
        if d != na: out.append(d)
    # dedupe, keep order, drop very short
    seen, final = set(), []
    for v in out:
        k = v.lower().strip()
        if k and k not in seen and len(k) > 5:
            seen.add(k); final.append(v.strip())
    return final[:7]

def api(q, rows=4):
    p = {"q": "mediatype:texts AND " + q, "fl[]": ["identifier","title","year","language"],
         "rows": rows, "output": "json"}
    u = "https://archive.org/advancedsearch.php?" + urllib.parse.urlencode(p, doseq=True)
    for i in range(2):
        try:
            return json.loads(urllib.request.urlopen(
                urllib.request.Request(u, headers=UA), timeout=35).read())
        except Exception:
            time.sleep(1.5)
    return None

def lending(i):
    return bool(re.search(r"000\d[a-z0-9_]*$", i)) or i.startswith("bwb_")

def one(t):
    hits, tried = [], []
    for v in variants(t["work"]):
        vq = v.replace('"', "").replace("'", " ")
        if len(vq) < 6: continue
        tried.append(vq)
        d = api('title:("%s")' % vq)
        n = (d or {}).get("response", {}).get("numFound", 0)
        if not n or n > 2000:      # 0 = nothing; huge = malformed query
            continue
        for x in (d or {}).get("response", {}).get("docs", []):
            ident = x.get("identifier", "")
            if any(h["identifier"] == ident for h in hits): continue
            hits.append({"identifier": ident, "title": str(x.get("title"))[:70],
                         "year": x.get("year"), "language": str(x.get("language"))[:12],
                         "via": vq, "lending": lending(ident)})
        if len(hits) >= 6: break
    return {"acu": t["id"], "work": t["work"], "lang": t["lang"],
            "tried": tried, "hits": hits}

targets = json.load(open(sys.argv[1]))
a = int(sys.argv[3]) if len(sys.argv) > 3 else 0
b = int(sys.argv[4]) if len(sys.argv) > 4 else len(targets)
targets = targets[a:b]
res = []
with cf.ThreadPoolExecutor(max_workers=5) as ex:
    for i, r in enumerate(ex.map(one, targets), 1):
        res.append(r)
        if i % 20 == 0: print(f"  ...{i}/{len(targets)}", flush=True)
json.dump(res, open(sys.argv[2], "w"), indent=1)
withhits = [r for r in res if r["hits"]]
dl = [r for r in withhits if any(not h["lending"] for h in r["hits"])]
print(f"searched {len(res)} | any hit {len(withhits)} | downloadable hit {len(dl)}")
