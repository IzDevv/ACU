#!/usr/bin/env python3
"""Keep only variant-search hits that share a DISTINCTIVE word with the work.

The raw variant search returns noise because short generic variants
("Glastonbury", "Thirteen Treasures") match anything. A real edition almost
always repeats an uncommon word from the work's own title.
"""
import json, re, sys, unicodedata
from collections import Counter

COMMON = set("""the of and a an in on to le la les de du des el los las il i et
der die das von zu y e o del della di dei from with for a saint st book
livre libro roman romance history historia chronicle chronicon vita life
quest queste story tale tales poem poems arthur arthurian king merlin
tristan lancelot gawain grail graal holy great old new first second third
volume vol part parts fragment fragments edition text texts""".split())

def norm(s):
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii","ignore").decode()
    return re.sub(r"[^a-z0-9 ]", " ", s.lower())

def distinctive(title):
    return {w for w in norm(title).split() if len(w) > 4 and w not in COMMON}

def lending(i):
    return bool(re.search(r"000\d[a-z0-9_]*$", i)) or i.startswith("bwb_")

rows = []
for f in sys.argv[1:-1]:
    try: rows += json.load(open(f))
    except Exception: pass
kept = []
for r in rows:
    want = distinctive(r["work"])
    if not want: continue
    good = []
    for h in r["hits"]:
        if h.get("lending") or lending(h["identifier"]): continue
        have = distinctive(h["title"])
        shared = want & have
        if not shared: continue
        y = h.get("year")
        try: y = int(y)
        except Exception: y = None
        if y and y > 1929: continue          # modern edition, likely restricted
        good.append({**h, "shared": sorted(shared)})
    if good: kept.append({**r, "hits": good})
json.dump(kept, open(sys.argv[-1], "w"), indent=1)
print(f"{len(rows)} searched -> {len(kept)} with a distinctive, downloadable, pre-1930 hit")
for r in kept:
    print(f"\n=== {r['acu']}  {r['work'][:54]}")
    for h in r["hits"][:3]:
        print(f"    {h['identifier'][:40]:40s} {str(h['year']):5s} {h['title'][:42]}")
        print(f"       shares: {','.join(h['shared'][:4])}")
