# Manual download queue

Every item here is blocked for me and actionable for you. Nothing in this
session was downloaded or opened: this environment's egress policy denied
every text repository, so each line is an **unverified lead** — a real
catalogue record found by search, not an inspected text.

Blocked hosts (all returned `403 CONNECT`, organization egress policy):
`archive.org`, `www.gutenberg.org`, `gallica.bnf.fr`, `en.wikisource.org`,
`fr.wikisource.org`, `babel.hathitrust.org`, `books.google.com`,
`celt.ucc.ie`, `quod.lib.umich.edu`, `daten.digitale-sammlungen.de`,
`dla.library.upenn.edu`, `www.rialto.unina.it`.

On archive.org, `https://archive.org/details/<id>` is the landing page;
the download formats are listed there. Items whose identifier ends in
`0000...` are lending-library scans — borrow-only, not downloadable.

## Tier 1 — one download covers several catalog entries

| Download | Covers | Why it is worth doing first |
|---|---|---|
| [textofmabinogion00rhysiala](https://archive.org/details/textofmabinogion00rhysiala) — Rhys & Evans, *The Text of the Mabinogion … from the Red Book of Hergest*, Oxford 1887 | ACU-0071, 0072, 0073, 0074, 0075, 0076, 0077 | Supplies the **Welsh originals** for seven entries currently held in translation only. Alternate copies: [textofmabinogion00evanuoft](https://archive.org/details/textofmabinogion00evanuoft), [TextOfTheMabinogion](https://archive.org/details/TextOfTheMabinogion) (CC0, full-text download) |
| [livesofthecambro00reesuoft](https://archive.org/details/livesofthecambro00reesuoft) — W. J. Rees, *Lives of the Cambro British Saints*, Llandovery 1853 | ACU-0007, 0008, 0009, 0014 | Latin texts with facing English for four Vitae now held in translation only. Second copy: [cu31924029417924](https://archive.org/details/cu31924029417924). Caveat: Rees's Latin is textually poor — Wade-Evans, *VSBG* (1944) is the sound edition if you can get it |
| [bishoppercysfoli01percuoft](https://archive.org/details/bishoppercysfoli01percuoft) — Hales & Furnivall, *Bishop Percy's Folio Manuscript*, vol. 1, 1867–68 | ACU-0274, 0275, 0277, (0279?) | Three Early Modern English ballads in one volume. The two Arthur ballads run together in the MS near p. 497 — separate them carefully. Other copies: [bishoppercysfol00halegoog](https://archive.org/details/bishoppercysfol00halegoog), [percyfolioolden00furngoog](https://archive.org/details/percyfolioolden00furngoog) |
| [dielaisdermarie01khgoog](https://archive.org/details/dielaisdermarie01khgoog) — Warnke, *Die Lais der Marie de France*, 3rd rev. edn 1925 | ACU-0172, 0173, 0174, part of 0179 | Anglo-Norman originals for three translation-only entries, plus the Guingamor appendix (ed. Kusel) for 0179. Also [mariedefrancelaiswarnketroed](https://archive.org/details/mariedefrancelaiswarnketroed); 1900 edn [dielaisdermaried00mariuoft](https://archive.org/details/dielaisdermaried00mariuoft); 1885 edn [dielaisdermarie00khgoog](https://archive.org/details/dielaisdermarie00khgoog) |
| [chronicaminorasa00momm](https://archive.org/details/chronicaminorasa00momm) — Mommsen, *Chronica minora* vol. 3 = MGH AA XIII | ACU-0001, ACU-0003 | Critical Latin texts of **both** Gildas *De excidio* and the *Historia Brittonum* in one volume. Second copy: [chronicaminorasa09momm](https://archive.org/details/chronicaminorasa09momm). Volume numbering differs between scans — check the title page |

## Tier 2 — single-entry, well-evidenced

| ACU ID | Work | Download |
|---|---|---|
| ACU-0001 | Gildas, *De excidio* (Latin + English) | [gildaedeexcidiob00gilduoft](https://archive.org/details/gildaedeexcidiob00gilduoft) — Hugh Williams, Cymmrodorion Record Series 1899; marked NOT_IN_COPYRIGHT |
| ACU-0259 | *Sir Gawain and the Green Knight* | [SirGawayneAndTheGreenKnight1915](https://archive.org/details/SirGawayneAndTheGreenKnight1915) — Morris EETS, re-edited from Cotton Nero A.x, rev. Gollancz 1912. Also [sirgawayneandgr00unkngoog](https://archive.org/details/sirgawayneandgr00unkngoog) (Morris 1869) |
| ACU-0388 | SGGK retold in modern prose | [SirGawainAndTheGreenKnightWeston1898](https://archive.org/details/SirGawainAndTheGreenKnightWeston1898) — Weston 1898. **Exact title match** for this entry |
| ACU-0129 | *Scalacronica* | [scalacronica00mait](https://archive.org/details/scalacronica00mait) — Stevenson, Maitland Club 1836; catalogue note "108 copies printed French text" = the Anglo-Norman original. Also [scalacronica00unkngoog](https://archive.org/details/scalacronica00unkngoog). Maxwell's 1907 English version [scalacronicareig01grayuoft](https://archive.org/details/scalacronicareig01grayuoft) is a fallback only |
| ACU-0249 | Prose *Brut* | [brutorchronicles00brieuoft](https://archive.org/details/brutorchronicles00brieuoft) — Brie, EETS 1906–08, 656 pp. |
| ACU-0305 | Holinshed, *Chronicles* | 1587 original: [bim_early-english-books-1475-1640_the-first-and-second-vol_holinshed-raphael_1587](https://archive.org/details/bim_early-english-books-1475-1640_the-first-and-second-vol_holinshed-raphael_1587). Readable Ellis 1807 reprint with the Privy Council excisions restored: [holinshedschroni01holi](https://archive.org/details/holinshedschroni01holi) |
| ACU-0511 *or* 0515 | Spanish *Tristán* | [librodelesforado00boni](https://archive.org/details/librodelesforado00boni) — Bonilla y San Martín 1912, reproducing the Valladolid 1501 princeps from the unique British Museum copy |
| ACU-0240 | Layamon, *Brut* | [layamonsbrutorc00maddgoog](https://archive.org/details/layamonsbrutorc00maddgoog) (vol. 1), [layamonsbrutorch03layauoft](https://archive.org/details/layamonsbrutorch03layauoft) (vol. 3), [LayamonSBrutMadden1](https://archive.org/details/LayamonSBrutMadden1), [bub_gb_AIIlAAAAMAAJ](https://archive.org/details/bub_gb_AIIlAAAAMAAJ) — Madden 1847. The Arthurian section (lines 9229–14297) falls in vols 2–3 |
| ACU-0213 | *Jaufre* | [JaufreTomeII](https://archive.org/details/JaufreTomeII) — Brunel 1943, **tome II only**; tome I still to find. Extracts in Raynouard, *Lexique roman* vol. 1 pp. 48–173 |
| ACU-0423 | Arthurian *Fastnachtspiele* | [bub_gb_XCTIrJ7jeVUC](https://archive.org/details/bub_gb_XCTIrJ7jeVUC) — Keller 1853, 121 plays continuously paged; plus the *Nachlese* [fastnachtspiele01kellgoog](https://archive.org/details/fastnachtspiele01kellgoog) |
| ACU-0041 | *Scotichronicon* | [bim_eighteenth-century_johannis-de-fordun-scoti_fordun-john_1752_2](https://archive.org/details/bim_eighteenth-century_johannis-de-fordun-scoti_fordun-john_1752_2) — Goodall's Latin Fordun/Bower, vol. 2. Watt's bilingual Aberdeen edition is also on IA by volume, e.g. [scotichronicon-v-1-bks-1-2](https://archive.org/details/scotichronicon-v-1-bks-1-2); Arthur is in Bower **Book III** |
| ACU-0146 | Didot *Perceval* | [lesaintgraaloule01huchuoft](https://archive.org/details/lesaintgraaloule01huchuoft) — Hucher 1875 vol. 1. **The prose Perceval text is in vol. 2**, whose identifier I could not pin down; [lesaintgraaloul03robegoog](https://archive.org/details/lesaintgraaloul03robegoog) is another volume of the set |

## Tier 3 — weak leads, check contents before trusting

| ACU ID | Work | Lead and what is unconfirmed |
|---|---|---|
| ACU-0055, 0064, 0065 | Welsh Arthur/Myrddin poems | [blackbookofcarma00evanuoft](https://archive.org/details/blackbookofcarma00evanuoft) (Evans 1906); Skene, *Four Ancient Books of Wales* 1868 — Welsh text is **vol. 2**: [fourancientbooks01skenuoft](https://archive.org/details/fourancientbooks01skenuoft), [four-ancient-books-of-wales](https://archive.org/details/four-ancient-books-of-wales), [fourancientbook04skengoog](https://archive.org/details/fourancientbook04skengoog). No search confirmed these particular poems are in either volume |
| ACU-0519 | *Livro de Linhagens* | [portugaliaemonumentahistoricascrv1](https://archive.org/details/portugaliaemonumentahistoricascrv1), [portugaliae-monumenta-historica-scriptores-volume-1-fasc-1](https://archive.org/details/portugaliae-monumenta-historica-scriptores-volume-1-fasc-1). Which PMH volume carries the Linhagens is unconfirmed. PMH is also served by the Biblioteca Nacional de Portugal |
| ACU-0190 | *La Mule sans frein* | [NouveauRecueilFabliauxVol1A1823](https://archive.org/details/NouveauRecueilFabliauxVol1A1823) (Méon 1823 vol. 1); [RecueilGeneralDesFabliaux3](https://archive.org/details/RecueilGeneralDesFabliaux3) (Montaiglon & Raynaud). Search found **no evidence either way** that the text is in Méon |
| ACU-0279 | *Sir Lionel* | Percy Folio, volume not established — nothing in search mentioned this ballad. Check the index across all four volumes |
| ACU-0506 | *A Demanda do Santo Graal* | [a-demanda-do-santo-graal-manuscrito-do-seculo-13-…](https://archive.org/details/a-demanda-do-santo-graal-manuscrito-do-seculo-13-texto-megale-heitor-texto-sob-o). Evidence is self-contradictory: the title names Megale (the Portuguese editor) but the item was described as Spanish. The **Spanish** Demanda print is a different work: [primeroysegundolibrodegria](https://archive.org/details/primeroysegundolibrodegria) |
| ACU-0179 (rest) | Espine / Graelent / Doon / Tydorel | [lelaideguingamor00mari](https://archive.org/details/lelaideguingamor00mari) covers Guingamor + Tydorel. Gaston Paris, "Lais inédits", *Romania* 8 (1879) prints Tyolet/Doon/Espine but no archive.org copy of that volume surfaced — try Gallica or Persée |

## Recorded failures — exact route and reason

| Target | Route tried | Reason |
|---|---|---|
| Every download in this file | direct HTTPS via the session proxy | `403 CONNECT` — organization egress policy. Not retried, per the proxy's own guidance |
| Any page inspection | WebFetch | `getaddrinfo ENOTFOUND` for all these hosts |
| ACU-0113 *Acallam na Senórach* | CELT (celt.ucc.ie), Stokes, *Irische Texte* IV i (Leipzig 1900) | CELT host blocked; and CELT's own electronic Stokes text is marked **[RESTRICTED]** — academic use by prior consent. The *Irische Texte* volume itself was not located on an open repository |
| ACU-0177 *Lai de Tyolet* | archive.org search for *Romania* vol. 8 | No copy of that volume surfaced |
| ACU-0415 *Prosa-Lancelot* | archive.org search for Kluge / Deutsche Texte des Mittelalters | Edition not located; DTM Lancelot volumes are modern and likely in copyright |
| ACU-0246 *Arthur* (Liber Rubeus Bathoniae) | archive.org search for Furnivall EETS 1864 | Not located under that description. A Furnivall *Le Morte Arthur* 1864 ([lemortearthur00brituoft](https://archive.org/details/lemortearthur00brituoft)) surfaced instead — a **different work**, do not confuse them |
| ACU-0506 Magne edition | archive.org | Augusto Magne's Rio de Janeiro edition not located; try the Biblioteca Nacional do Brasil |

No CAPTCHA or client-block was encountered, because no request ever reached
a repository.
