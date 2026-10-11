#!/usr/bin/env python3
"""Check native-title Wikisource pages and download the real ones as text.

Serial, long backoff on 429. Wikimedia asks for a descriptive UA and no
parallel hammering; this obeys both.
"""
import json, os, re, sys, time, urllib.request, urllib.parse, urllib.error

UA = {"User-Agent": "ACU-text-collection/1.0 (scholarly Arthurian corpus; contact github.com/IzDevv/ACU)"}
OUT = sys.argv[1] if len(sys.argv) > 1 else "sources/_wikisource"
DELAY = 3.0

def _get(url, tries=6):
    for i in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=50).read()
        except urllib.error.HTTPError as e:
            wait = 60 if e.code == 429 else 3 * (i + 1)
            print(f"    HTTP {e.code} -> wait {wait}s", flush=True); time.sleep(wait)
        except Exception as e:
            print(f"    {e}", flush=True); time.sleep(5)
    return None

def exists(wiki, titles):
    p = {"action":"query","format":"json","titles":"|".join(titles),"redirects":"1","prop":"info"}
    raw = _get(f"https://{wiki}.wikisource.org/w/api.php?" + urllib.parse.urlencode(p))
    time.sleep(DELAY)
    if not raw: return {}
    d = json.loads(raw)
    norm = {n["from"]: n["to"] for n in d["query"].get("normalized", [])}
    red  = {r["from"]: r["to"] for r in d["query"].get("redirects", [])}
    found = {pg["title"] for pid, pg in d["query"]["pages"].items() if int(pid) > 0}
    out = {}
    for t in titles:
        t2 = red.get(norm.get(t, t), norm.get(t, t))
        out[t] = t2 if t2 in found else None
    return out

def wikitext(wiki, title):
    u = f"https://{wiki}.wikisource.org/w/index.php?title=" + \
        urllib.parse.quote(title.replace(" ", "_")) + "&action=raw"
    raw = _get(u); time.sleep(DELAY)
    return raw.decode("utf-8", "replace") if raw else ""

def strip(wt):
    s = re.sub(r"<ref[^>]*>.*?</ref>", "", wt, flags=re.S)
    s = re.sub(r"\{\{[^{}]*\}\}", "", s)
    s = re.sub(r"\{\{[^{}]*\}\}", "", s)
    s = re.sub(r"\{\|.*?\|\}", "", s, flags=re.S)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", s)
    s = re.sub(r"^[:;#*]+", "", s, flags=re.M)
    s = re.sub(r"'{2,}", "", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()

# (ACU, wiki, [candidate titles], slug)
JOBS = [
 ("ACU-0532","es",["Romance de don Tristán"],"romance_don_tristan"),
 ("ACU-0531","es",["El romancero viejo"],"romancero_viejo_lanzarote"),
 ("ACU-0060","cy",["Marwnad Cynddylan"],"marwnad_cynddylan"),
 ("ACU-0078","cy",["Mabinogion J M Edwards Cyf 2/Hanes Taliesin"],"hanes_taliesin"),
 ("ACU-0050","cy",["Y Gododdin"],"y_gododdin"),
 ("ACU-0026","la",["Draco Normannicus"],"draco_normannicus"),
 ("ACU-0022","la",["Historia Regum Britanniae/Liber VII"],"prophetiae_merlini_hrb7"),
 ("ACU-0475","it",["Gismirante/Cantare primo","Gismirante/Cantare secondo"],"cantare_gismirante"),
 ("ACU-0176","fr",["Du Mantel mautaillié"],"mantel_mautaillie"),
 # native-title probes for entries the English-title search could not reach
 ("ACU-0051","cy",["Pa gur yv y porthaur","Pa Gur"],"pa_gur"),
 ("ACU-0052","cy",["Preiddeu Annwn"],"preiddeu_annwn"),
 ("ACU-0053","cy",["Englynion y Beddau"],"englynion_y_beddau"),
 ("ACU-0063","cy",["Ymddiddan Myrddin a Thaliesin"],"ymddiddan_myrddin_taliesin"),
 ("ACU-0066","cy",["Afallennau"],"afallennau"),
 ("ACU-0067","cy",["Oianau"],"oianau"),
 ("ACU-0068","cy",["Trioedd Ynys Prydein"],"trioedd_ynys_prydein"),
 ("ACU-0064","cy",["Cyfoesi Myrddin a Gwenddydd"],"cyfoesi_myrddin"),
 ("ACU-0065","cy",["Gwasgargerdd Fyrddin yn y Bedd"],"gwasgargerdd_fyrddin"),
 ("ACU-0082","cy",["Ystorya Trystan"],"ystorya_trystan"),
 ("ACU-0121","cy",["Pedwar Marchog ar Hugain Llys Arthur"],"pedwar_marchog"),
 ("ACU-0071","cy",["Culhwch ac Olwen"],"culhwch_ac_olwen"),
 ("ACU-0081","cy",["Y Seint Greal"],"y_seint_greal"),
]

os.makedirs(OUT, exist_ok=True)
log = []
for acu, wiki, titles, slug in JOBS:
    print("==", acu, slug, flush=True)
    res = exists(wiki, titles)
    real = [v for v in res.values() if v]
    if not real:
        print("   no such page", flush=True)
        log.append({"acu": acu, "slug": slug, "wiki": wiki, "status": "no page", "tried": titles})
        continue
    parts, urls = [], []
    for t in real:
        wt = wikitext(wiki, t)
        if not wt: continue
        parts.append(f"\n\n===== {t} =====\n\n" + strip(wt))
        urls.append(f"https://{wiki}.wikisource.org/wiki/" + urllib.parse.quote(t.replace(" ", "_")))
    if not parts:
        log.append({"acu": acu, "slug": slug, "wiki": wiki, "status": "fetch failed", "tried": titles}); continue
    body = "".join(parts)
    hdr = (f"# {acu} — {slug}\n# source: {wiki}.wikisource.org\n"
           f"# pages: {'; '.join(urls)}\n"
           f"# retrieved: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n"
           f"# NOTE: existing editorial transcription from Wikisource, NOT OCR and\n"
           f"# NOT a transcription made by this process. Verify against a print\n"
           f"# edition before citing; Wikisource pages can be partial or unsourced.\n\n")
    p = os.path.join(OUT, slug + ".txt")
    open(p, "w", encoding="utf-8").write(hdr + body)
    print(f"   saved {len(body)} chars <- {len(real)} page(s)", flush=True)
    log.append({"acu": acu, "slug": slug, "wiki": wiki, "status": "saved",
                "chars": len(body), "urls": urls, "file": p})

json.dump(log, open(os.path.join(OUT, "_log.json"), "w"), indent=1)
print("\nsaved:", sum(1 for l in log if l["status"] == "saved"), "/", len(JOBS))
