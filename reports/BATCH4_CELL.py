# BATCH 4 (REVISED) - supersedes the earlier BATCH4_CELL.py.
# 14 English entries + 3 corrections to items batch 2 got wrong.
# Handles Gutenberg-mirror items, which carry .txt but no PDF.
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
 ('gale_rerum_anglicarum_1684_v3', 'rerumanglicarums03fulm', "ACU-0017 CORRECTION to batch 2, which fetched vol 1 (wrong). Vol 3 has 'Antiquitates Glaftonienfis Ecclefiae' - VERIFIED here. 874pp"),
 ('kolbing_tristram_isodd_1878', 'dienordischeunddieenglis', "ACU-0460 CORRECTION to batch 2. That fetched Tristrams saga ok Isondar, a DIFFERENT work. Kolbing 1878 has 68 'Isodd' hits - VERIFIED here"),
 ('demanda_santo_graal_reinhardstoettner_1887', 'historiadoscaval00reinuoft', "ACU-0506 CORRECTION to batch 2, whose scan had unusable OCR (0 hits for 'graal'). VERIFIED here: 1887, por, 192pp, PD, 69 Galaaz / 91 Graal / 64 Artur"),
 ('mabinogion_edwards_1890_welsh', 'mabinogionolyfrc00edwa', 'ACU-0078 Hanes Taliesin - VERIFIED here: Welsh, 1890, Ceridwen/Tegid Foel present. Supersedes the Wikisource page, which was only a transclusion wrapper'),
 ('fabliaux_recueil_t3_mantel', 'recueilgnral03montuoft', 'ACU-0176 Du Mantel mautaillie - VERIFIED here: contents p.57, text p.72, Montaiglon & Raynaud t.III'),
 ('heywood_life_of_merlin_1813', 'lifeofmerlinsurn00heyw', 'ACU-0324 Heywood, Life of Merlin surnamed Ambrosius, 348pp'),
 ('polydore_vergil_english_history_1844', 'threebookspolyd00socigoog', 'ACU-0304 Camden Society 1844, 294pp, NOT_IN_COPYRIGHT'),
 ('polychronicon_higden_trevisa_rs', 'polychroniconran09higd', 'ACU-0250 Higden + Trevisa English, Rolls Series 1865, 650pp, lat+eng'),
 ('percy_reliques_1765_v1', 'bib_fict_4103138_1', "ACU-0335 King Ryence's Challenge is in Percy's Reliques, 1765, 388pp"),
 ('deloney_garland_good_will_1631', 'bim_early-english-books-1475-1640_the-garland-of-good-will_deloney-thomas_1631', "ACU-0336 VERIFIED here: opens 'Good Will. Diuided into three parts', 1631, 117pp"),
 ('scott_sir_tristrem_1819', 'sirtristremamet00scotgoog', 'ACU-0348 Scott, Sir Tristrem, 1819, 539pp, NOT_IN_COPYRIGHT'),
 ('wordsworth_yarrow_revisited_1835', 'yarrowrevisitedo00word', 'ACU-0377 The Egyptian Maid is in Yarrow Revisited, 1835, 254pp'),
 ('camden_britannia_1722', 'gri_33125011116247', 'ACU-0323 Britannia English trans, 1722, 718pp, NOT_IN_COPYRIGHT'),
 ('chaucer_canterbury_tales_skeat_v4', 'chaucersworksvol22120gut', "ACU-0291 Wife of Bath's Tale - Skeat vol 4. GUTENBERG MIRROR: .txt only, no PDF"),
 ('chaucer_works_skeat_v6', 'chaucersworksvol43097gut', "ACU-0292 Squire's Tale etc - Skeat vol 6. GUTENBERG MIRROR: .txt only"),
 ('short_english_metrical_chronicle_1935', 'anonymousshorten0000ewal', 'ACU-0245 CAUTION: 0000-style id, may be borrow-only; will fail cleanly if so'),
 ('milton_history_of_britain_1671', 'bim_early-english-books-1641-1700_the-history-of-britain-_milton-john_1671', 'ACU-0326 Milton, History of Britain, 1671 EEBO'),
]

ok = skip = fail = 0
for slug, ident, note in ITEMS:
    d = os.path.join(DEST, slug); os.makedirs(d, exist_ok=True)
    print('==', slug)
    print('   ', note)
    try:
        md = json.load(get('https://archive.org/metadata/' + ident))
    except Exception as e:
        print('   metadata failed:', e); fail += 1; continue
    files = md.get('files', [])
    want = []
    for f in files:
        if f.get('format') in ('Text PDF','Image Container PDF') and not any(x['name'].endswith('.pdf') for x in want):
            want.append(f)
        if f.get('format') == 'DjVuTXT':
            want.append(f)
    # Gutenberg-mirror items have no PDF/DjVuTXT - take the plain .txt
    if not want:
        for f in files:
            if f.get('format') == 'Text' and f['name'].lower().endswith('.txt'):
                want.append(f); break
    if not want:
        print('   no usable derivative'); fail += 1; continue
    for f in want:
        name = f['name']; path = os.path.join(d, name)
        size = int(f.get('size', 0) or 0)
        if os.path.exists(path) and os.path.getsize(path) == size:
            print('   have', name); skip += 1; continue
        url = 'https://archive.org/download/' + ident + '/' + urllib.parse.quote(name)
        if fetch(url, path):
            print('   got  %s  %.1f MB' % (name, os.path.getsize(path)/1e6)); ok += 1
        else:
            print('   STILL FAILING', name); fail += 1
    with open(os.path.join(d, '_source.txt'), 'w') as fh:
        fh.write(ident + '\t' + note + '\n')

print('\ndownloaded %d | already had %d | failed %d' % (ok, skip, fail))
