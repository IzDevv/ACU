# BATCH 9 - Latin. Six downloads, seven catalog entries.
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
 ('giraldus_opera_v8_de_principis', 'giraldicambrensi08gira', 'ACU-0028 De Principis Instructione - VERIFIED: Rolls Series vol 8, 556pp. Principis=213, Instructione=154, Arthur=24, Glaston=15 (the exhumation)'),
 ('giraldus_opera_v4_speculum_ecclesiae', 'giraldicambrensi04gira', 'ACU-0029 Speculum Ecclesiae - VERIFIED: Rolls Series vol 4, 534pp. Speculum=140, Ecclesiae=22, Arthur=15, Glaston=10. NB an earlier candidate by Nicolaus de Clemangis was a DIFFERENT work with the same title; this is Gerald of Wales'),
 ('giraldus_opera_v6_itinerarium', 'giraldicambrensi06gira', 'ACU-0030 Itinerarium + Descriptio Kambriae - VERIFIED: Rolls Series vol 6, 376pp. Itinerarium=38, Descriptio=93, Kambriae=7, Arthur=18'),
 ('forbes_ninian_kentigern_1874', 'livesofsniniansk00forb', "ACU-0048 Jocelin's Life of Kentigern + ACU-0049 Lailoken - VERIFIED: Forbes 1874, 510pp, PD. Kentigern=352, Jocelin=68, Lailoken=5, Laloecen=2, Meldred=1"),
 ('kittredge_arthur_and_gorlagon_1903', 'cu31924027098072', 'ACU-0037 Narratio de Arturo Rege et Rege Gorlagon - VERIFIED: Kittredge 1903, 146pp. Gorlagon=115, Arthur=157'),
 ('liber_landavensis_1840', 'liberlandavensi00reesgoog', 'ACU-0015 Vita Sancti Dubricii - VERIFIED: Liber Landavensis 1840, 707pp, PD, Latin. Dubricius=289, Dubricii=65'),
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
