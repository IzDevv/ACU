#!/usr/bin/env python3
"""Fetch Wikisource pages as plain text. Serial, rate-limited, polite UA."""
import json, sys, time, os, urllib.request, urllib.parse

UA = {"User-Agent": "ACU-text-collection/1.0 (scholarly Arthurian corpus; contact via github.com/IzDevv/ACU)"}
DELAY = 2.0   # seconds between requests - Wikimedia asks for serial access

def _get(url, tries=5):
    for i in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=45).read()
        except urllib.error.HTTPError as e:
            wait = 10 * (i + 1) if e.code == 429 else 2 ** i
            print(f"    HTTP {e.code}, waiting {wait}s", flush=True)
            time.sleep(wait)
        except Exception as e:
            print(f"    {e}", flush=True); time.sleep(2 ** i)
    return None

def fetch(wiki, title):
    p = {"action": "query", "prop": "extracts", "explaintext": "1",
         "format": "json", "titles": title, "redirects": "1"}
    raw = _get(f"https://{wiki}.wikisource.org/w/api.php?" + urllib.parse.urlencode(p))
    time.sleep(DELAY)
    if not raw: return ""
    pg = next(iter(json.loads(raw)["query"]["pages"].values()))
    return pg.get("extract", "")

if __name__ == "__main__":
    t = fetch(sys.argv[1], sys.argv[2])
    print(f"[{len(t)} chars]")
    print(t[:int(sys.argv[3]) if len(sys.argv) > 3 else 500])
