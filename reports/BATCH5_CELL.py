# BATCH 5 - two verified additions.
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
 ('coggeshall_chronicon_anglicanum_1875', 'ChroniconAnglicanum', "ACU-0031 VERIFIED: 'Quomodo ossa regis Arturi reperta sunt ... apud Glastingeberiam ... Hic jacet inclitus rex Arturius, in insula Avallonis sepultus'. Latin, Rolls Series 1875"),
 ('myvyrian_archaiology_1870', 'myvyrianarchaiol00joneuoft', 'ACU-0065 VERIFIED: Gwasgargerdd Fyrddin yn y Bedd at p.105 (OCR mangles it to GWASGARGEED). Welsh original for a translation-only entry. 1302pp, also carries Afallenau Myrddin p.115 and Hoianau p.106'),
]

ok = skip = fail = 0
for slug, ident, note in ITEMS:
    d = os.path.join(DEST, slug); os.makedirs(d, exist_ok=True)
    print('==', slug); print('   ', note)
    try:
        md = json.load(get('https://archive.org/metadata/' + ident))
    except Exception as e:
        print('   metadata failed:', e); fail += 1; continue
    files = md.get('files', []); want = []
    for f in files:
        if f.get('format') in ('Text PDF','Image Container PDF') and not any(x['name'].endswith('.pdf') for x in want):
            want.append(f)
        if f.get('format') == 'DjVuTXT': want.append(f)
    if not want:
        for f in files:
            if f.get('format') == 'Text' and f['name'].lower().endswith('.txt'): want.append(f); break
    if not want: print('   no usable derivative'); fail += 1; continue
    for f in want:
        name = f['name']; path = os.path.join(d, name); size = int(f.get('size', 0) or 0)
        if os.path.exists(path) and os.path.getsize(path) == size:
            print('   have', name); skip += 1; continue
        url = 'https://archive.org/download/' + ident + '/' + urllib.parse.quote(name)
        if fetch(url, path): print('   got  %s  %.1f MB' % (name, os.path.getsize(path)/1e6)); ok += 1
        else: print('   STILL FAILING', name); fail += 1
    with open(os.path.join(d, '_source.txt'), 'w') as fh: fh.write(ident + '\t' + note + '\n')

print('\ndownloaded %d | already had %d | failed %d' % (ok, skip, fail))
