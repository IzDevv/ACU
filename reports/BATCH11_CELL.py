# BATCH 11 - Welsh texts from the Celtic Literature Collective (maryjones.us).
# These are HTML pages, not archive.org items, so this cell strips the markup
# and saves plain text with provenance.
DEST = '/content/drive/MyDrive/ACU_sources/_celtic_lit_collective'

import os, re, time, html as H, urllib.request
UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
      'Accept-Language': 'en-GB,en;q=0.9'}
os.makedirs(DEST, exist_ok=True)

def get(url, tries=4):
    for i in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=45).read()
        except Exception as e:
            print('      try %d/%d: %s' % (i+1, tries, e)); time.sleep(2 ** i)
    return None

def totext(raw):
    h = raw.decode('utf-8', 'replace')
    h = re.sub(r'(?is)<(script|style|head)[^>]*>.*?</\1>', ' ', h)
    h = H.unescape(re.sub(r'<[^>]+>', '\n', h))
    return re.sub(r'\n\s*\n+', '\n\n', h).strip()

JOBS = [
 ('ACU-0082', 'ystoria_trystan_welsh', ['trystan-w'], "Ystori Trystan, Cardiff MS 43. VERIFIED here: Welsh text, opens 'Yn y cyfamser yr aeth Trystan ap Tallwch ag Esyllt, gwraig March y Meirchion'. Was translation-only"),
 ('ACU-0090', 'buchedd_collen_welsh', ['collen-w'], "Buchedd Collen, Hafod MS 19 (1536) p.141. VERIFIED here: Welsh, opens 'Llyma ystoria kollen ai vVchedd'. Was translation-only"),
 ('ACU-0056', 'ymddiddan_melwas_gwenhwyfar_welsh', ['melwas-w', 'melwas2-w'], 'Ymddiddan rhwng Arthur a Gwenhwyfar, AKA Ymddiddan Melwas a Gwenhwyfar, Llanstephan 122. VERIFIED here: Welsh verse. Two versions on the site. Was translation-only'),
 ('ACU-0088', 'ymddiddan_arthur_gwenhwyfar_welsh', ['melwas-w', 'melwas2-w'], "SAME TEXT as ACU-0056 - the site states 'Ymddiddan rhwng Arthur a Gwenhwyfar / AKA: Ymddiddan Melwas a Gwenhwyfar'. Catalogues them separately; they may be one work. Resolve before filing both"),
]

ok = fail = 0
for acu, slug, pages, note in JOBS:
    print('==', acu, slug); print('   ', note)
    parts, urls = [], []
    for p in pages:
        url = 'https://www.maryjones.us/ctexts/%s.html' % p
        raw = get(url); time.sleep(1.5)
        if not raw: print('   FAILED', url); continue
        t = totext(raw)
        if len(t) < 200: print('   too short, skipping', p); continue
        parts.append('\n\n===== %s =====\n\n%s' % (p, t)); urls.append(url)
    if not parts: print('   nothing retrieved'); fail += 1; continue
    body = ''.join(parts)
    hdr = ('# ' + acu + ' - ' + slug + '\n'
           '# source: Celtic Literature Collective, maryjones.us\n'
           '# pages: ' + '; '.join(urls) + '\n'
           '# note: ' + note + '\n'
           '# retrieved: ' + time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()) + '\n'
           '# PROVENANCE: an existing editorial transcription from a personal\n'
           '# scholarly website, not OCR and not transcribed by this process.\n'
           '# The site states its TRANSLATIONS mostly follow Skene (1868); the\n'
           '# Welsh texts are its own transcriptions from the named manuscripts.\n'
           '# Verify against a print edition before citing.\n\n')
    open(os.path.join(DEST, slug + '.txt'), 'w', encoding='utf-8').write(hdr + body)
    print('   saved %d chars from %d page(s)' % (len(body), len(urls))); ok += 1

print('\nsaved %d | failed %d' % (ok, fail))
