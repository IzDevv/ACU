# BATCH 12 - ACU-0066 Peiryan Vaban, the last missing Welsh text.
DEST = '/content/drive/MyDrive/ACU_sources/_celtic_lit_collective'

import os, re, time, html as H, urllib.request
UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
      'Accept-Language': 'en-GB,en;q=0.9'}
os.makedirs(DEST, exist_ok=True)

def get(url, tries=4):
    for i in range(tries):
        try: return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=45).read()
        except Exception as e:
            print('      try %d/%d: %s' % (i+1, tries, e)); time.sleep(2 ** i)
    return None

def totext(raw):
    h = raw.decode('utf-8', 'replace')
    h = re.sub(r'(?is)<(script|style|head)[^>]*>.*?</\1>', ' ', h)
    h = H.unescape(re.sub(r'<[^>]+>', '\n', h))
    return re.sub(r'\n\s*\n+', '\n\n', h).strip()

JOBS = [
 ('ACU-0066', 'peiryan_vaban_welsh', ['peirian'], "Peiryan Vaban, Peniarth 50 ff.36-38, attributed to Myrddin. VERIFIED here: Welsh text, opens 'Peiryan vaban peit ti ath ietkynt. / A ddifero di duw rae gwyddyl gynt.' This was the last Welsh entry I had declared genuinely missing - the page exists but the site index does not link it. Standard edition is A.O.H. Jarman, Bulletin of the Board of Celtic Studies 14.2 (1951) 104-8; the site warns no English translation is known to it"),
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
        if len(t) < 200: print('   too short', p); continue
        parts.append('\n\n===== %s =====\n\n%s' % (p, t)); urls.append(url)
    if not parts: print('   nothing retrieved'); fail += 1; continue
    body = ''.join(parts)
    hdr = ('# ' + acu + ' - ' + slug + '\n# source: Celtic Literature Collective, maryjones.us\n'
           '# pages: ' + '; '.join(urls) + '\n# note: ' + note + '\n'
           '# retrieved: ' + time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()) + '\n'
           '# PROVENANCE: existing editorial transcription from a personal\n'
           '# scholarly website. Not OCR, not transcribed by this process.\n'
           '# Spelling and lineation may differ from Jarman 1951.\n\n')
    open(os.path.join(DEST, slug + '.txt'), 'w', encoding='utf-8').write(hdr + body)
    print('   saved %d chars' % len(body)); ok += 1

print('\nsaved %d | failed %d' % (ok, fail))
