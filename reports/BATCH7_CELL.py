# BATCH 7 - Old French, from Romania and a 1928 lais edition.
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
 ('romania_v8_1879_lais_inedits', 'romania_1879_8', "ACU-0177 Tyolet + ACU-0179 (Doon, Tydorel) - VERIFIED: Romania vol 8 1879, 646pp, carries Gaston Paris, 'LAIS INEDITS DE TYOLET, DE GUINGAMOR, DE DOON, DU LECHEOR ET DE TYDOREL' pp.29-72. Corrects my earlier 'failed access' verdict on ACU-0177"),
 ('lays_desire_graelent_melion_1928', 'thelaysofdesiregraelentandmelion', "ACU-0178 Melion + ACU-0179 (Graelent) + ACU-0239 (Desire) - VERIFIED: Grimes 1928, 162pp, 'edition of the texts'. 75 Melion / 77 Graelent / 20 Desire hits"),
 ('prophecies_de_merlin_paton_1927', 'lespropheciesdemerlinpatt2', 'ACU-0232 - Paton, Les Prophecies de Merlin, edited from MS, 1927. CAUTION: catalog entry names the PRINTED Prophesies; this is the manuscript edition. Related, verify which the entry wants. An incunable also exists at ita-bnc-in2-00001949-001 (1480)'),
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
    if not want:
        for f in md.get('files', []):
            if f.get('format') == 'Text' and f['name'].lower().endswith('.txt'): want.append(f); break
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
