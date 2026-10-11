# PROBE - does archive.org's SEARCH-INSIDE-BOOKS work from Colab?
# This container gets 502 on these endpoints. Colab's IP may not.
# It downloads nothing. It prints whether the API answers, and what it finds
# for eight works that are still missing from the catalog.
#
# If this works, it is a different kind of search: it looks INSIDE scanned
# books for a phrase, which is how to find short texts printed inside
# anthologies. Every search so far has only matched TITLES.

import json, urllib.request, urllib.parse, time

UA = {'User-Agent': 'ACU-text-collection/1.0 (scholarly Arthurian corpus)'}

ENDPOINTS = [
    ('ia-pub-fts-api', 'https://ia-pub-fts-api.archive.org/search/v1/scrape?q=%s&count=10'),
    ('ia-fts',         'https://ia-fts.archive.org/api/v1/search/hits?q=%s&size=10'),
]

# still-missing works, with a distinctive phrase or name to search for
TARGETS = [
    ('ACU-0066', 'Peiryan Vaban',            '"Peiryan Vaban"'),
    ('ACU-0480', 'Cantare di Lasancis',      '"Lasancis"'),
    ('ACU-0185', 'Yder (Old French romance)', '"roman d\'Yder"'),
    ('ACU-0196', 'Les Enfances Gauvain',     '"Enfances Gauvain"'),
    ('ACU-0012', 'Vita Sancti Efflami',      '"Efflam"'),
    ('ACU-0013', 'Legenda Sancti Goeznovii', '"Goeznovii"'),
    ('ACU-0019', 'Epistola ad Warinum',      '"ad Warinum"'),
    ('ACU-0518', 'Lais de Bretanha',         '"Lais de Bretanha"'),
]

def try_get(url):
    try:
        r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=45)
        return r.getcode(), r.read()
    except Exception as e:
        return None, str(e).encode()

working = None
print('--- testing endpoints ---')
for name, tmpl in ENDPOINTS:
    code, raw = try_get(tmpl % urllib.parse.quote('"Peiryan Vaban"'))
    print('  %-16s -> %s' % (name, code if code else raw[:70].decode('utf-8', 'replace')))
    if code == 200:
        working = tmpl
        print('     WORKS. Sample response:', raw[:200].decode('utf-8', 'replace'))
        break

if not working:
    print('\nNo full-text endpoint reachable from Colab either.')
    print('That closes the question: search-inside-books is not available to us.')
else:
    print('\n--- searching for still-missing works ---')
    for acu, name, q in TARGETS:
        code, raw = try_get(working % urllib.parse.quote(q))
        print('\n== %s  %s   query %s' % (acu, name, q))
        if code != 200:
            print('   failed:', code); time.sleep(1); continue
        try:
            d = json.loads(raw)
        except Exception:
            print('   (unparseable response)'); time.sleep(1); continue
        items = d.get('items') or d.get('hits') or []
        print('   total reported:', d.get('total', '?'), '| returned:', len(items))
        for it in items[:6]:
            ident = it.get('identifier') or it.get('id') or '?'
            print('     ', ident)
        time.sleep(1.5)

print('\nDone. Paste the whole output back - nothing was downloaded.')
