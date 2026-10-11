# BATCH 2 - 35 items read and judged individually (not keyword-scored).
# Paste as a new cell and run. Skips anything already downloaded.
DEST = '/content/drive/MyDrive/ACU_sources'

import os, json, time, urllib.request, urllib.parse
UA = {'User-Agent': 'ACU-acquisition/1.0'}

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
 ('draco_normannicus_howlett_rs_v2', 'chroniclesofreig02howl', 'ACU-0026 - Draco Normannicus in Rolls Series vol 2'),
 ('y_seint_greal_williams_1876', 'selectionsfromh00jonegoog', 'ACU-0081 - Welsh+English, Hengwrt/Peniarth selections'),
 ('folie_tristan_bedier_1907', 'lesdeuxpomesde00bduoft', 'ACU-0167 - covers BOTH ACU-0167 Oxford and ACU-0168 Berne'),
 ('queste_saint_graal_1864', 'laquestedelsain00clubgoog', 'ACU-0157 - CAUTION: likely the Vulgate Queste, catalog wants Post-Vulgate'),
 ('mort_artu_bruce_1910', 'MortArtuOldFrenchBruce', 'ACU-0158 - CAUTION: Vulgate Mort Artu; catalog wants Post-Vulgate'),
 ('beaudous_robert_de_blois_ulrich_1889', 'robert_von_blois_sammtliche_werke_1', 'ACU-0195 - Beaudous in Ulrich vol 1'),
 ('sone_de_nansay_goldschmidt_1899', 'SoneVonNausayGoldschmidtB', 'ACU-0199 - standard edition'),
 ('artus_de_bretagne_1503', 'LePreuxEtVaillantChevallierArtus1503', 'ACU-0207 - 1503 Paris print; also relevant to ACU-0231'),
 ('huon_de_bordeaux_1586', 'HuonDeBordeaux1586', 'ACU-0210 - 1586 French prose print'),
 ('bataille_loquifer_runeberg_1913', 'RunebergLaBatailleLoquifer', 'ACU-0238 - critical edition from Arsenal/Boulogne MSS'),
 ('joseph_of_arimathie_skeat_eets', 'JosephOfArimathie', 'ACU-0286 - enm+eng; EETS'),
 ('lydgate_siege_of_thebes_erdmann_1911', 'lydgatessiegeoft00lydgrich', 'ACU-0289 - Chaucer Society/EETS'),
 ('assertio_robinson_1582', 'bim_early-english-books-1475-1640_a-learned-and-true-asser_leyland-john_1582', 'ACU-0303 - the 1582 Learned and True Assertion itself'),
 ('mirror_for_magistrates_1607', 'bim_early-english-books-1475-1640_a-mirror-for-magistrates_higgins-john_1607', 'ACU-0306 - 1607, 895pp'),
 ('tom_a_lincolne_1635', 'bim_early-english-books-1475-1640_the-most-pleasant-histor_johnson-richard_1635', 'ACU-0310 - 1635 print, 99pp'),
 ('seven_champions_1670', 'gpl_1837738', 'ACU-0312 - 1670, 384pp'),
 ('brittains_ida_1628', 'bim_early-english-books-1475-1640_brittains-ida_fletcher-giles-the-you_1628', "ACU-0317 - Brittain's Ida only; Chinon of England NOT included"),
 ('prince_arthur_1634', 'bim_early-english-books-1475-1640_the-most-ancient-and-fam_arthur-king_1634', 'ACU-0338 - 1634 Stansby Malory, 941pp'),
 ('mabinogion_guest_1838', 'b22012515_0004', 'ACU-0368 - Guest part-issue, eng+wel'),
 ('high_history_holy_graal_evans_1898', 'highhistoryofhol01perliala', 'ACU-0369 - Sebastian Evans trans'),
 ('tennyson_holy_grail_1870', 'holygrailandoth02tenngoog', 'ACU-0371 - 241pp'),
 ('romance_king_arthur_pollard_1917', 'romanceofkingart00malorich', 'ACU-0385 - Pollard abridgement'),
 ('diu_crone_scholl_1852', 'diucrnevonheinr00trgoog', 'ACU-0400 - Heinrich von dem Tuerlin, standard ed'),
 ('garel_bluenden_tal_walz_1892', '00080681bsb', 'ACU-0403 - der Pleier, full edition 375pp'),
 ('segremors_fragmente_1909', 'DieMitteldeutschenSegremorsfragmente', 'ACU-0410 - dissertation that prints the fragments - VERIFY'),
 ('wigoleis_vom_rade_1910', 'dasvolksbuchvonw00weid', 'ACU-0427 - Volksbuch, 72pp'),
 ('saga_tristram_isond_1878', 'rssagaaftristram00norduoft', 'ACU-0460 - + Moettuls saga; CAUTION: Tristrams saga vs Saga af Tristram ok Isodd'),
 ('ivan_loveridder_brandt_1869', 'RomantiskDigtningFraMiddelalderen1', 'ACU-0466 - Brandt, Romantisk digtning'),
 ('vita_di_merlino_1554', 'hin-wel-all-00002399-001', 'ACU-0494 - 1554 Italian, 460pp'),
 ('storia_di_merlino_pieri_sanesi_1898', 'lastoriadimerlinodipaolinopi', 'ACU-0494 - Paolino Pieri ed. Sanesi'),
 ('demanda_santo_graal_portuguese', 'a-demanda-do-santo-graal-as-maravilhas-da-besta-ladrador-da-fonte-da-guaricom-e-da-dona-da-capela', 'ACU-0506 - Portuguese - VERIFY against ACU-0506'),
 ('de_antiquitate_gale_1684_v1', 'rerumanglicarums01fulm', 'ACU-0017 - Gale Rerum Anglicarum; volume unconfirmed'),
 ('blandin_cornoalha_arthur_trans', 'blandin-de-cornoalha', 'ACU-0214 - TRANSLATION ONLY - English, not the Occitan original'),
 ('folie_lancelot_farra_trans', 'lfarra-fl-complet-v-1', 'ACU-0234 - TRANSLATION ONLY - modern French from Bogdanow'),
 ('tristan_als_moench_regis_1910', 'IA41538725_0108', 'ACU-0424 - REASSIGNED from ACU-0445 search hit; MHG, not Middle Dutch'),
]

ok = skip = fail = 0
for slug, ident, note in ITEMS:
    d = os.path.join(DEST, slug); os.makedirs(d, exist_ok=True)
    print('==', slug, '|', note)
    try:
        md = json.load(get('https://archive.org/metadata/' + ident))
    except Exception as e:
        print('   metadata failed:', e); fail += 1; continue
    want = []
    for f in md.get('files', []):
        if f.get('format') in ('Text PDF','Image Container PDF') and not any(x['name'].endswith('.pdf') for x in want):
            want.append(f)
        if f.get('format') == 'DjVuTXT':
            want.append(f)
    if not want:
        print('   no pdf/text derivative'); fail += 1; continue
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
