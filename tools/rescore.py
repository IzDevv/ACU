#!/usr/bin/env python3
"""Stricter scoring: title match + language match + public-domain date.

Keyword-presence in the body is near-worthless on its own (a study ABOUT a
work contains the work's name). An actual edition almost always carries the
work's name in its TITLE, is in the work's LANGUAGE, and is old enough to be
public domain.
"""
import json, sys, re, unicodedata

LANGMAP = {
 "welsh":{"wel","cym","welsh"}, "latin":{"lat","latin"},
 "old french":{"fre","fra","french","old french"}, "middle french":{"fre","fra","french"},
 "anglo-norman":{"fre","fra","french","eng"}, "occitan":{"oci","pro","provencal","occitan"},
 "irish":{"gle","iri","irish","gae"}, "middle english":{"eng","enm","english"},
 "early modern english":{"eng","enm","english"}, "english":{"eng","english"},
 "middle high german":{"ger","gmh","deu","german"}, "early new high german":{"ger","deu","german"},
 "german":{"ger","deu","german"}, "italian":{"ita","italian"}, "spanish":{"spa","spanish"},
 "portuguese":{"por","portuguese"}, "middle dutch":{"dut","nld","dum","dutch"},
 "dutch":{"dut","nld","dutch"}, "byzantine greek":{"gre","grc","greek"},
 "old norse":{"non","ice","nor","icelandic"}, "czech":{"cze","ces"}, "hebrew":{"heb"},
 "early middle english":{"eng","enm"}, "old english":{"ang","eng"},
}
STUDY = re.compile(r"\b(a study|studies in|the concept|essay|essays|introduction to|"
                   r"life and letters|bibliograph|dissertation|a critical|criticism|"
                   r"handbook|companion to|lectures|review of)\b", re.I)

def norm(s):
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii","ignore").decode()
    return re.sub(r"[^a-z0-9 ]", " ", s.lower())

def toks(s):
    stop = set("the of and a an in on to le la les de du des el los las il et or der die das "
               "von zu y e o del della di dei from with for".split())
    return {w for w in norm(s).split() if len(w) > 3 and w not in stop}

def year(c):
    m = re.search(r"(1[4-9]\d\d|20\d\d)", str(c.get("date") or ""))
    return int(m.group(1)) if m else None

def langs(c):
    v = c.get("language")
    v = v if isinstance(v, list) else [v]
    return {norm(x).strip() for x in v if x}

def score(target_work, target_lang, c):
    tw, reasons = toks(target_work), []
    ct = toks(c.get("title"))
    overlap = len(tw & ct) / max(1, len(tw))
    pts = 0
    if overlap >= 0.6: pts += 4; reasons.append(f"title {int(overlap*100)}%")
    elif overlap >= 0.35: pts += 2; reasons.append(f"title {int(overlap*100)}%")
    else: reasons.append(f"title only {int(overlap*100)}%")

    want = set()
    for k, v in LANGMAP.items():
        if k in target_lang.lower(): want |= v
    have = langs(c)
    if want:
        if any(any(w in h or h in w for w in want) for h in have):
            pts += 3; reasons.append("language match")
        elif have:
            pts -= 2; reasons.append(f"language MISMATCH ({'/'.join(sorted(have))[:20]})")

    y = year(c)
    if y and y <= 1929: pts += 2; reasons.append(f"PD era {y}")
    elif y and y > 1929: pts -= 3; reasons.append(f"modern {y} (likely in copyright)")

    if STUDY.search(str(c.get("title") or "")):
        pts -= 4; reasons.append("looks like a STUDY not an edition")
    if c.get("rights") == "NOT_IN_COPYRIGHT": pts += 1
    if c.get("has_text_layer"): pts += 1
    return pts, reasons

ver = json.load(open(sys.argv[1]))
out = []
for r in ver:
    b = r.get("best")
    if not b: continue
    pts, why = score(r["work"], r["lang"], b)
    out.append({**r, "strict_score": pts, "reasons": why})
out.sort(key=lambda x: -x["strict_score"])
json.dump(out, open(sys.argv[2], "w"), indent=1)

good = [r for r in out if r["strict_score"] >= 7]
maybe = [r for r in out if 4 <= r["strict_score"] < 7]
bad = [r for r in out if r["strict_score"] < 4]
print(f"strong {len(good)} | needs review {len(maybe)} | reject {len(bad)}")
