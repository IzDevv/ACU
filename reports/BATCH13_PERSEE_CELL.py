# BATCH 13 - Persee articles. Persee 403s PDF downloads from the research
# container; it may not from Colab. If it does 403 here too, open the two
# landing-page URLs in a normal browser - Persee is free and open access,
# and both articles are long out of copyright.
DEST = '/content/drive/MyDrive/ACU_sources'

import os, time, urllib.request

ITEMS = [
 ('donnei_des_amants_romania25_1896',
  'https://www.persee.fr/docAsPDF/roma_0035-8029_1896_num_25_100_5472.pdf',
  'https://www.persee.fr/doc/roma_0035-8029_1896_num_25_100_5472',
  'ACU-0169 Donnei des Amants (contains the Tristan Rossignol episode). Gaston Paris, Romania 25 (1896) pp.497-541. Sole MS: Phillipps 3713, Cheltenham'),
 ('enfances_gauvain_romania39_1910',
  'https://www.persee.fr/docAsPDF/roma_0035-8029_1910_num_39_153_5096.pdf',
  'https://www.persee.fr/doc/roma_0035-8029_1910_num_39_153_5096',
  'ACU-0196 Les Enfances Gauvain, fragment d un poeme perdu. Paul Meyer, Romania 39 (1910) pp.1-32. MS found at the Bibliotheque Sainte-Genevieve'),
]

UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
      'Accept': 'application/pdf,*/*;q=0.8', 'Accept-Language': 'fr,en;q=0.9'}

ok = fail = 0
for slug, pdf, landing, note in ITEMS:
    d = os.path.join(DEST, slug); os.makedirs(d, exist_ok=True)
    print('==', slug); print('   ', note)
    path = os.path.join(d, slug + '.pdf')
    if os.path.exists(path) and os.path.getsize(path) > 20000:
        print('   have it'); continue
    req = urllib.request.Request(pdf, headers={**UA, 'Referer': landing})
    try:
        with urllib.request.urlopen(req, timeout=120) as r, open(path, 'wb') as w:
            while True:
                c = r.read(1 << 20)
                if not c: break
                w.write(c)
        if open(path, 'rb').read(4) == b'%PDF':
            print('   got %.2f MB' % (os.path.getsize(path)/1e6)); ok += 1
        else:
            os.remove(path); print('   served HTML, not a PDF - open in a browser:'); print('   ', landing); fail += 1
    except Exception as e:
        if os.path.exists(path): os.remove(path)
        print('   blocked (%s) - open in a browser:' % e); print('   ', landing); fail += 1
    with open(os.path.join(d, '_source.txt'), 'w') as fh:
        fh.write(landing + '\t' + note + '\n')
    time.sleep(2)

print('\ndownloaded %d | blocked %d' % (ok, fail))
