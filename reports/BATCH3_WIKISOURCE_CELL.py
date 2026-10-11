# BATCH 3 - Wikisource transcriptions (existing editorial text, not OCR).
# Colab's IP is not rate-limited the way this session's was; still polite (3s gap).
DEST = '/content/drive/MyDrive/ACU_sources/_wikisource'

import os, re, json, time, urllib.request, urllib.parse, urllib.error
UA = {'User-Agent': 'ACU-text-collection/1.0 (scholarly Arthurian corpus)'}
DELAY = 3.0
os.makedirs(DEST, exist_ok=True)

def _get(url, tries=5):
    for i in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=50).read()
        except urllib.error.HTTPError as e:
            w = 60 if e.code == 429 else 3*(i+1)
            print('    HTTP %d -> wait %ds' % (e.code, w)); time.sleep(w)
        except Exception as e:
            print('   ', e); time.sleep(5)
    return None

def exists(wiki, titles):
    p = {'action':'query','format':'json','titles':'|'.join(titles),'redirects':'1','prop':'info'}
    raw = _get('https://%s.wikisource.org/w/api.php?' % wiki + urllib.parse.urlencode(p))
    time.sleep(DELAY)
    if not raw: return []
    d = json.loads(raw)['query']
    return [pg['title'] for pid, pg in d['pages'].items() if int(pid) > 0]

def wikitext(wiki, title):
    u = 'https://%s.wikisource.org/w/index.php?title=' % wiki + urllib.parse.quote(title.replace(' ','_')) + '&action=raw'
    raw = _get(u); time.sleep(DELAY)
    return raw.decode('utf-8','replace') if raw else ''

def strip(wt):
    s = re.sub(r'<ref[^>]*>.*?</ref>', '', wt, flags=re.S)
    for _ in range(3): s = re.sub(r'\{\{[^{}]*\}\}', '', s)
    s = re.sub(r'\{\|.*?\|\}', '', s, flags=re.S)
    s = re.sub(r'<[^>]+>', '', s)
    s = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]', r'\1', s)
    s = re.sub(r'^[:;#*]+', '', s, flags=re.M)
    s = re.sub(r"'{2,}", '', s)
    return re.sub(r'\n{3,}', '\n\n', s).strip()

JOBS = [
 ('ACU-0532', 'es', ['Romance de don Tristán'], 'romance_don_tristan', "VERIFIED here: opens 'Herido está don Tristán / de una muy mala lanzada'"),
 ('ACU-0531', 'es', ['El romancero viejo'], 'romancero_viejo_lanzarote', "contains 'Nunca fuera caballero' - Lanzarote romances"),
 ('ACU-0060', 'cy', ['Marwnad Cynddylan'], 'marwnad_cynddylan', 'VERIFIED here: 2460 chars Welsh, was translation-only'),
 ('ACU-0078', 'cy', ['Mabinogion J M Edwards Cyf 2/Hanes Taliesin'], 'hanes_taliesin', 'Welsh, 2036 words, was translation-only'),
 ('ACU-0050', 'cy', ['Y Gododdin'], 'y_gododdin', 'clean Welsh transcription; also in Skene vol 2 already held'),
 ('ACU-0026', 'la', ['Draco Normannicus'], 'draco_normannicus', 'full Latin text 29851 words - better than the Rolls Series scan'),
 ('ACU-0022', 'la', ['Historia Regum Britanniae/Liber VII'], 'prophetiae_merlini_hrb7', 'Prophetiae Merlini = HRB Book VII'),
 ('ACU-0475', 'it', ['Gismirante/Cantare primo', 'Gismirante/Cantare secondo'], 'cantare_gismirante', 'Antonio Pucci, both cantari'),
 ('ACU-0176', 'fr', ['Du Mantel mautaillié'], 'mantel_mautaillie', 'Old French, in Recueil general des fabliaux'),
 ('ACU-0368', 'en', ['The Mabinogion (Guest 1877)'], 'mabinogion_guest_1877', 'Guest translation, full'),
 ('ACU-0312', 'en', ['The Renowned History of the Seven Champions of Christendom'], 'seven_champions_ws', 'supplements the 1670 print'),
 ('ACU-0051', 'cy', ['Pa gur yv y porthaur', 'Pa Gur'], 'pa_gur', 'probe'),
 ('ACU-0052', 'cy', ['Preiddeu Annwn'], 'preiddeu_annwn', 'probe'),
 ('ACU-0053', 'cy', ['Englynion y Beddau'], 'englynion_y_beddau', 'probe'),
 ('ACU-0063', 'cy', ['Ymddiddan Myrddin a Thaliesin'], 'ymddiddan_myrddin_taliesin', 'probe'),
 ('ACU-0066', 'cy', ['Afallennau'], 'afallennau', 'probe'),
 ('ACU-0067', 'cy', ['Oianau'], 'oianau', 'probe'),
 ('ACU-0068', 'cy', ['Trioedd Ynys Prydein'], 'trioedd_ynys_prydein', 'probe'),
 ('ACU-0064', 'cy', ['Cyfoesi Myrddin a Gwenddydd'], 'cyfoesi_myrddin', 'probe - print text confirmed in Skene vol 2 p.218ff'),
 ('ACU-0065', 'cy', ['Gwasgargerdd Fyrddin yn y Bedd'], 'gwasgargerdd_fyrddin', 'probe - NOT in Skene, still unresolved'),
 ('ACU-0082', 'cy', ['Ystorya Trystan'], 'ystorya_trystan', 'probe'),
 ('ACU-0121', 'cy', ['Pedwar Marchog ar Hugain Llys Arthur'], 'pedwar_marchog', 'probe'),
 ('ACU-0071', 'cy', ['Culhwch ac Olwen'], 'culhwch_ac_olwen', 'probe'),
 ('ACU-0081', 'cy', ['Y Seint Greal'], 'y_seint_greal', 'probe'),
]

saved = absent = 0
for acu, wiki, titles, slug, note in JOBS:
    print('==', acu, slug, '|', note)
    real = exists(wiki, titles)
    if not real:
        print('   no such page:', titles); absent += 1; continue
    parts, urls = [], []
    for t in real:
        wt = wikitext(wiki, t)
        if not wt: continue
        parts.append('\n\n===== ' + t + ' =====\n\n' + strip(wt))
        urls.append('https://%s.wikisource.org/wiki/' % wiki + urllib.parse.quote(t.replace(' ','_')))
    if not parts:
        print('   fetch failed'); absent += 1; continue
    body = ''.join(parts)
    hdr = ('# ' + acu + ' - ' + slug + '\n# source: ' + wiki + '.wikisource.org\n'
           '# pages: ' + '; '.join(urls) + '\n'
           '# note: ' + note + '\n'
           '# retrieved: ' + time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()) + '\n'
           '# PROVENANCE: existing editorial transcription from Wikisource.\n'
           '# Not OCR, and not transcribed by this process. Wikisource pages can\n'
           '# be partial or unsourced - verify against a print edition.\n\n')
    open(os.path.join(DEST, slug + '.txt'), 'w', encoding='utf-8').write(hdr + body)
    print('   saved %d chars from %d page(s)' % (len(body), len(real))); saved += 1

print('\nsaved %d | absent or failed %d' % (saved, absent))
