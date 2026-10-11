# BATCH 14 - two entries I had wrongly written off, both public domain.
DEST = '/content/drive/MyDrive/ACU_sources'

import os, json, time, urllib.request, urllib.parse
UA = {'User-Agent': 'ACU-text-collection/1.0'}

def get(url, timeout=300):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout)

def fetch(url, path, tries=6):
    for i in range(tries):
        try:
            with get(url) as r, open(path, 'wb') as w:
                while True:
                    c = r.read(1 << 20)
                    if not c: break
                    w.write(c)
            return True
        except Exception as e:
            if os.path.exists(path): os.remove(path)
            print('      try %d/%d failed: %s' % (i+1, tries, e))
            if i < tries - 1: time.sleep(2 ** i)
    return False

ITEMS = [
 ('merveilles_de_rigomer_foerster_1908_v1', 'lesmervellesderi01rigo', 'ACU-0164 Les Merveilles de Rigomer - VERIFIED: Foerster, Gesellschaft fuer romanische Literatur Bd 19, 1908, 538pp. This is BAND I, the Old French TEXT. Rigomer=156, Jehan=25. My first search of the session concluded no Band I scan existed on archive.org; it does'),
 ('merveilles_de_rigomer_foerster_1908_v2', 'lesmervellesderi02rigo', 'ACU-0164 companion: Band II, 306pp - introduction, notes, glossary, name index (German apparatus)'),
 ('mule_sanz_frain_hill_1911', 'lamulesanzfrain00pa', 'ACU-0190 La Mule sans frein - VERIFIED: Hill ed. 1911, 252pp, French. mule=199, frain=47, Gauvain=211, Keu=50. Supersedes the weak Meon lead, whose contents were never confirmed'),
 ('damoisele_a_la_mule_orlowski_1911', 'bnf-bpt6k6534707s', "ACU-0190 second witness: Orlowski's 1911 critical edition, La damoisele a la mule - a BnF scan hosted on archive.org"),
]

ok = skip = fail = 0
for slug, ident, note in ITEMS:
    d = os.path.join(DEST, slug); os.makedirs(d, exist_ok=True)
    print('==', slug); print('   ', note)
    try:
        md = json.load(get('https://archive.org/metadata/' + ident))
    except Exception as e:
        print('   metadata failed:', e); fail += 1; continue
    want = []
    for f in md.get('files', []):
        if f.get('format') in ('Text PDF','Image Container PDF') and not any(x['name'].endswith('.pdf') for x in want):
            want.append(f)
        if f.get('format') == 'DjVuTXT': want.append(f)
    if not want: print('   no usable derivative'); fail += 1; continue
    for f in want:
        name = f['name']; path = os.path.join(d, name); size = int(f.get('size', 0) or 0)
        if os.path.exists(path) and os.path.getsize(path) == size:
            print('   have', name); skip += 1; continue
        if fetch('https://archive.org/download/' + ident + '/' + urllib.parse.quote(name), path):
            print('   got  %s  %.1f MB' % (name, os.path.getsize(path)/1e6)); ok += 1
        else: print('   STILL FAILING', name); fail += 1
    with open(os.path.join(d, '_source.txt'), 'w') as fh: fh.write(ident + '\t' + note + '\n')

print('\ndownloaded %d | already had %d | failed %d' % (ok, skip, fail))
