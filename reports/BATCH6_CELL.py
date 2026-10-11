# BATCH 6 - Middle Dutch. Found by looking beyond archive.org.
# Mixes archive.org items with one direct PDF from dbnl.org.
DEST = '/content/drive/MyDrive/ACU_sources'

import os, json, time, urllib.request, urllib.parse
UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
      'Accept': 'text/html,application/xhtml+xml,*/*;q=0.8', 'Accept-Language': 'nl,en;q=0.9'}

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

IA_ITEMS = [
 ('lancelotcompilatie_jonckbloet_1846_v1', 'romanvanlancelo01joncgoog', "ACU-0439 Perchevael - VERIFIED: 59 'Perchevael' hits, 54 'Moriaen', 826 'Lanceloet'. Jonckbloet 1846, Dutch, 404pp, PD. Also an extra witness for ACU-0432 Lancelot-compilatie"),
 ('lancelotcompilatie_jonckbloet_1846_v2', 'romanvanlancelo00joncgoog', "ACU-0439 companion volume of the same edition (the Wrake van Ragisel sits in the second volume; vol 1 had 0 'Ragisel' hits)"),
 ('merlijn_steinfort_1880', 'merlijnnaarhete00robegoog', "ACU-0442 + ACU-0443 - VERIFIED: Merlijn naar het Steinforter handschrift, 1880, Dutch, 430pp, PD. 82 'Merlijn', 74 'Merline', 667 'Artur', 35 'Maerlant', 7 'Velthem', 25 'Grale'"),
]

DIRECT = [
 ('wrake_van_ragisel_gysseling', 'https://www.dbnl.org/tekst/_wra001mgys01_01/_wra001mgys01_01.pdf', 'wrake_van_ragisel_gysseling.pdf', 'ACU-0438 - VERIFIED: Middle Dutch text, ed. M. Gysseling, from Cd-rom Middelnederlands 1998. 20pp. COPYRIGHT CAUTION: DBNL warns works published under 140 years ago may be protected; this is a 1998 edition. For personal study only - check dbnl.org terms before any reuse'),
]

ok = skip = fail = 0
for slug, ident, note in IA_ITEMS:
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

for slug, url, fname, note in DIRECT:
    d = os.path.join(DEST, slug); os.makedirs(d, exist_ok=True)
    print('==', slug); print('   ', note)
    path = os.path.join(d, fname)
    if os.path.exists(path) and os.path.getsize(path) > 1000:
        print('   have', fname); skip += 1
    elif fetch(url, path):
        print('   got  %s  %.2f MB' % (fname, os.path.getsize(path)/1e6)); ok += 1
    else: print('   STILL FAILING', fname); fail += 1
    with open(os.path.join(d, '_source.txt'), 'w') as fh: fh.write(url + '\t' + note + '\n')

print('\ndownloaded %d | already had %d | failed %d' % (ok, skip, fail))
