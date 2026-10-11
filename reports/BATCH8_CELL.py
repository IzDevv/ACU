# BATCH 8 - Italian cantari and an Icelandic ballad collection.
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
 ('fiore_di_leggende_levi_1914', '064FioreDiLeggendeSi113', "ACU-0475 Gismirante + ACU-0478 Liombruno - VERIFIED: Levi, Fiore di Leggende: cantari antichi, 1914. Prints 'VII GISMIRANTE / PRIMO CANTARE' and 'III LIOMBRUNO / CANTARE PRIMO' with the verse. 67 / 111 hits"),
 ('islenzk_fornkvaedi_1854_v1', 'slenzkfornkvi01littgoog', "ACU-0461 Tristrams kvaedi - VERIFIED: Islenzk fornkvaedi 1854, 737pp, PD. Prints '23. Tristrams kvaedi'; 18 'Tristrams kv' and 57 'Isodd' hits"),
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
