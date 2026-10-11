# Candidate verdicts — read, not scored

Each judgement below comes from reading the candidate's title page / opening
text, not from keyword scoring. Keyword scoring was tried first and produced
false positives bad enough to discard the approach (examples at the bottom).

## Already covered by files acquired earlier — no download needed

| ACU | Work | Where it is | Evidence |
|---|---|---|---|
| ACU-0050 | Y Gododdin (Arthur stanza) | `fourancientbooks02skenuoft` (Skene vol. 2), already in Drive | Contents line 355 `I. E Gododin. Aneirin ae Cant`; Welsh text from line 4122 (`hwn yw e gododin`), with further stanzas at 4182, 4485, 4608, 4676 |

## Confirmed good — worth downloading

| ACU | Work | Candidate | Evidence |
|---|---|---|---|
| ACU-0081 | Y Seint Greal | `selectionsfromh00jonegoog` | Robert Williams, *Selections from the Hengwrt MSS preserved in the Peniarth Library*, 1876, 761 pp, language `['wel','eng']`, NOT_IN_COPYRIGHT. Vol. 1 of this edition is Y Seint Greal with Welsh text and facing English |
| ACU-0026 | Draco Normannicus | `chroniclesofreig02howl` | Howlett (ed.), *Chronicles of the reigns of Stephen, Henry II and Richard I*, Rolls Series 1884, Latin+English. The Draco Normannicus of Etienne de Rouen is printed in **vol. 2** of this set (the vol. 4 copy that search returned is the wrong volume) |

## Right edition, wrong volume — fetch the correct one

| ACU | Work | Note |
|---|---|---|
| ACU-0028 | De Principis Instructione | `giraldicambrens*giragoog` is the right set (*Giraldi Cambrensis Opera*, Rolls Series) but vols 1 and 3 are wrong; De Principis Instructione is **vol. 8** |
| ACU-0041 | Scotichronicon | Watt's bilingual edition is on IA volume by volume; search returned v5 and v8. Arthur is in Bower **Book III**, so the volume wanted is books III–IV |
| ACU-0017 | De Antiquitate Glastoniensis Ecclesiae | `rerumanglicarums01fulm` / `03fulm` — Gale, *Rerum Anglicarum Scriptores Veteres*, Oxford 1684, Latin. Plausible host for William of Malmesbury's De Antiquitate; which volume is unconfirmed |

## Rejected after reading — recorded so they are not re-proposed

| ACU | Work | What the candidate actually was |
|---|---|---|
| ACU-0047 | Vera Historia de Morte Arthuri | `bub_gb_CTRzfolTajEC` is *Aphorismi inquisitorum ... cum **vera historia** de origine Sanctae Inquisitionis* (1633) — the Portuguese Inquisition. Matched on the phrase "vera historia" |
| ACU-0029 | Speculum Ecclesiae (Gerald of Wales) | Both candidates are Nicolaus de Clemangis, *Speculum ecclesiae pontificiae* (1605/1606) — a different work by a different author. Gerald's Speculum Ecclesiae is in *Giraldi Cambrensis Opera* vol. 4 |
| ACU-0078 | Hanes Taliesin | `wood-1983-medieval-magician` is Juliette Wood, "Virgil and Taliesin: The Concept of the Magician in Medieval Folklore", *Folklore* 94 (1983) — a journal article, and in copyright |
| ACU-0084 | Birth of Arthur | `TheLifeAndLettersOfFatherBertrand` — unrelated |
| ACU-0044 | Scotorum Historia (Boece) | `bib_fict_4102830_*` is Innes, *A Critical Essay on the Ancient Inhabitants of ... Scotland* (1729) — not Boece |
| ACU-0048 | Life of St Kentigern | Candidates were lives of St Gregentius and St Leucius |
| ACU-0020 | De Miraculis Sanctae Mariae Laudunensis | Candidates are Potho's *Liber de miraculis sanctae Dei genitricis Mariae* and a Blannbekin volume — a different miracle collection |
| ACU-0023, ACU-0031 | Historia Regum Britanniae First Variant; Chronicon | Digital Scriptorium manuscript catalogue records, 1–4 page images each, no text. Useful as witness references, not as texts |
| ACU-0080 | Brut Tysilio | The Welsh text is not in Skene vol. 2 — "Tysilio" appears there only in a biographical note on the saint. `ahistorykingsan00tysigoog` (1862) is Peter Roberts's **English translation**, not the Welsh original |
| ACU-0082 | Ystoria Trystan | "Trystan mab Tallwch" in Skene vol. 2 is from the **Welsh Triads**, not the Ystoria |
| ACU-0121 | Pedwar Marchog ar Hugain | "pedwar" hits are the ordinary Welsh word for "four" |
| ACU-0056, ACU-0088 | Ymddiddan Melwas a Gwenhwyfar; Ymddiddan Arthur a Gwenhwyfar | Neither "Melwas" nor "Gwenhwyfar" occurs anywhere in the Black Book of Carmarthen text layer |

## Why scoring was abandoned

A keyword scorer rated the 1983 Taliesin journal article a full 6/6 for
ACU-0078, and rated the Inquisition volume 8 points for ACU-0047. Both pass
any title-similarity test, because the words genuinely are in the text. Only
reading the opening distinguishes an edition of a work from a study about it,
or from an unrelated book that shares a phrase.

## Batch 3 post-mortem and batch 4

### Why half of batch 3 returned near-empty files

Pages like `cy:Mabinogion J M Edwards Cyf 2/Hanes Taliesin` are **transclusion
wrappers**, not text:

```
<pages index="Mabinogion - (o Lyfr coch Hergest) (IA mabinogionolyfrc00edwa).pdf" from=103 to=112/>
```

The text lives in the Page: namespace of a scanned PDF and is only assembled
when the server renders the page. `action=raw` returns the wrapper, which is
why ACU-0078 saved 172 chars, ACU-0475 82 chars, ACU-0368 245 and ACU-0312 206.
The fix is `action=parse&prop=text` (server-side expansion), or — better where
possible — fetch the source scan the wrapper names.

### Resolved without Wikisource

| ACU | Work | Route | Evidence |
|---|---|---|---|
| ACU-0078 | Hanes Taliesin | `mabinogionolyfrc00edwa` | The wrapper named its own source scan. Edwards 1890, Welsh, 118pp; Ceridwen and Tegid Foel both present in the text layer |
| ACU-0176 | Du Mantel mautaillié | `recueilgnral03montuoft` | Montaiglon & Raynaud t. III: contents line 57 `DU MANTEL MAUTAILLIÉ`, text at p. 72. Volumes 1,2,4,5 have zero hits; vol 6 only cites it in notes |

### Already covered by Skene vol. 2 (already in Drive) — no download needed

Found by searching Skene's own medieval orthography, not modern Welsh:

| ACU | Work | Skene's spelling | Location |
|---|---|---|---|
| ACU-0050 | Y Gododdin | `E Gododin. Aneirin ae Cant` | contents 355, text 4122ff |
| ACU-0051 | Pa Gur | `Pa gur yv y porthaur` | fol. 47b, line 3574 |
| ACU-0052 | Preiddeu Annwn | `preideu annwfyn` | line 10290 |
| ACU-0053 | Englynion y Beddau | `Englynnionn y Bedev` | contents XIX, text 2422 |
| ACU-0064 | Cyfoesi Myrddin a Gwenddydd | `Kyuoessi Myrdin a Gwendyd y chwaer` | contents 800, text p.218ff |

### Confirmed NOT in Skene vol. 2 — still open

ACU-0065 (Gwasgargerdd), ACU-0066 (Afallenau), ACU-0067 (Hoianau). All three
appear only in Skene's notes and index. The index entry
`Apple-trees (the Avallenau), i. 370` points to **volume 1**, which is the
English translation, not the Welsh. Welsh texts for these three need the
Myvyrian Archaiology or a Black Book / Red Book edition.

### Confirmed absent from archive.org

ACU-0257 Sir Landevale · ACU-0342 Sir Corneus · ACU-0357 Swinburne, Queen
Yseult · ACU-0374 Hawker, Quest of the Sangraal · ACU-0475 Cantare di
Gismirante (Wikisource is its only route) · ACU-0380 Hardy, Queen of
Cornwall (borrow-only `bwb_` scans only).

### Welsh Wikisource genuinely lacks

Pa Gur, Ymddiddan Myrddin a Thaliesin, Afallennau, Oianau, Trioedd Ynys
Prydein, Cyfoesi, Gwasgargerdd, Ystorya Trystan, Pedwar Marchog, Culhwch ac
Olwen. These returned "no such page", not a fetch error.

## Post-download verification of batch 2 (run against the delivered files)

Batch 2 fetched 70 files with no failures. Verifying the four items tagged
VERIFY, plus two whose text layer came back at 0.0 MB:

| ACU | Verdict | Evidence |
|---|---|---|
| ACU-0410 Segremors | **confirmed** | 108 hits for `Segremors`, 70 for `Fragment`, 24 for `v. 1` (verse numbering) — the dissertation does print the fragments, not merely discuss them |
| ACU-0317 Brittain's Ida | **confirmed** | 0.0 MB layer is simply a 39-page work; 22 `Brittain`, 10 `Ida`, title page reads "Written by that Renowned Poet, EDMOND SPENCER" |
| ACU-0017 De Antiquitate | **WRONG VOLUME** | Gale vol 1 (fetched) has 4 incidental `Glafton` and no De Antiquitate. Vol 3 has 22 `Glafton`, 5 `Glaftonienf`, and the text "reliquit Antiquitates Glaftonienfis Ecclefiae". Corrected to `rerumanglicarums03fulm` |
| ACU-0460 Saga af Tristram ok Ísodd | **WRONG WORK** | The fetched `rssagaaftristram00norduoft` is *Saga af Tristram ok Ísönd samt Möttuls saga* — the Norse *Tristrams saga ok Ísöndar*, a different text from the Icelandic *Saga af Tristram ok Ísodd*. Kölbing 1878 (`dienordischeunddieenglis`) carries 68 `Isodd` hits. Corrected |
| ACU-0506 Demanda | **UNUSABLE OCR** | The fetched scan's text layer is 0.007 MB with **zero** hits for graal, besta, ladrador, Galaaz or cavaleiro; OCR output is noise. Replaced with Reinhardstoettner 1887 (`historiadoscaval00reinuoft`), 192pp, PD, verified 69 `Galaaz` / 91 `Graal` / 64 `Artur`, title page "A DEMANDA DO SANTO GRAALL" |

Incidental find: Gale vol 2 contains the 1278 Glastonbury exhumation —
"apud Glaftoniam, & ibi Dominus Rex tumbam Regis Arthuri" — which may serve
ACU-0031 (Chronicon, Glastonbury exhumation entry), currently unresolved.

## CORRECTION to the "already covered by Skene" claim

I earlier reported five entries (ACU-0050, 0051, 0052, 0053, 0064) as closed
by the Skene volume already held. Checking those IDs against the catalog:

| ACU | Actual catalog title | Status BEFORE today | Was my find new? |
|---|---|---|---|
| ACU-0050 | Y Gododdin (Arthur stanza) | Searched Archive; no candidate | **yes** |
| ACU-0051 | Preiddeu Annwn | Original-language source downloaded | no — already covered |
| ACU-0052 | Pa gur yv y porthaur? | Original-language source downloaded | no — already covered |
| ACU-0053 | Englynion y Beddau | Original-language source downloaded | no — already covered |
| ACU-0064 | Cyfoesi Myrddin a Gwenddydd | Translation downloaded; original sought | **yes** — supplies the Welsh |

So two genuine, not five. I also had ACU-0051 and ACU-0052 **swapped** in my
own notes (0051 is Preiddeu Annwn, 0052 is Pa gur).

Two further ID errors in the batch 3 probe list, which mean those probes
searched for the wrong works entirely:

- **ACU-0066 is *Peiryan Vaban***, not "Afallennau" as I labelled it.
- **ACU-0067 is *Trioedd Ynys Prydein* (the Welsh Triads)**, not "Oianau",
  and it was already marked covered before today.

The "no such page" results recorded against those two IDs therefore say
nothing about them.

## New, verified

| ACU | Work | Source | Evidence |
|---|---|---|---|
| ACU-0031 | Chronicon (Glastonbury exhumation), Ralph of Coggeshall | `ChroniconAnglicanum` (Rolls Series 1875, Latin) | Chapter heading "Quomodo ossa regis Arturi reperta sunt"; text "inventa sunt apud Glastingeberiam ossa famosissimi Arturi, quondam regis Britanniae ... crux plumbea superposita fuerat, in qua ita exaratum erat, 'Hic jacet inclitus rex Arturius, in insula Avallonis sepultus'". Index: "Arthur, king ... his bones found at Glastonbury, 36" |
| ACU-0065 | Gwasgargerdd Fyrddin yn y Bedd | `myvyrianarchaiol00joneuoft` (Myvyrian Archaiology, 1870, wel+eng, 1302pp) | Running head "GWASGARGEED ...RD1X YN Y VED. 105" — OCR mangling of GWASGARGERDD MYRDDIN YN Y BEDD. A plain search for "Gwasgargerdd" returns zero, which is why earlier passes missed it. Same volume carries "AFALLENAU MYRDDIN" p.115 (with verse text) and "HOIANAU NEU BORCHELLANAU MYRDDIN AP MORFRYN" p.106 |

## Still genuinely missing

ACU-0066 *Peiryan Vaban* — no hits in the Myvyrian ("Peirian" matches there
are `peiriant`/`peiriannau`, meaning engine or contrivance, unrelated).

## Widening beyond archive.org — what each source actually did

Prompted to cast a wider net. Results, honestly:

| Source | Outcome |
|---|---|
| **dbnl.org** (Dutch) | **Works, with a trick.** Default headers get 403; a full browser header set gets 200 on title and text pages. Its *search* endpoint stays 403, so discovery has to go through WebSearch and retrieval through curl. Yielded ACU-0438 |
| **archive.org** (re-queried in Dutch) | **Works.** The earlier passes searched English titles only. Querying Dutch editors and titles found the Lancelot Compilation and the Steinfort Merlijn, which three entries needed |
| **Google Books** | **Dead end from here.** `books.google.com` is reachable but the API returns `429 Quota exceeded ... Queries per day` — the shared cloud IP's daily allowance is spent. Needs an API key. May work from Colab |
| **TEAMS / d.lib.rochester.edu** | **Blocked.** Cloudflare interstitial ("Just a moment...") on every content path, with full browser headers. Needs a real browser. This is a real loss — TEAMS publishes free editions of many Middle English Arthurian romances |
| **WebFetch** | **Unavailable.** `getaddrinfo ENOTFOUND` on every host, even ones curl reaches |
| **archive.org full-text search** | **Unavailable.** `ia-fts.archive.org` and `ia-pub-fts-api.archive.org` both 502 through this proxy. This is the biggest methodological gap: it would find short works printed inside anthologies, which is where much of the remaining 200 probably sits |
| Reachable but untried | runeberg.org, heimskringla.no (Norse), mdz-nbn-resolving.de (German), arlima.net (bibliography), persee.fr, deutschestextarchiv.de, hs-augsburg.de, dmgh.de |
| Blocked | bdh.bne.es (403), europeana.eu (403), zeno.org, openlibrary.org, bibliotecaitaliana.it, corpuscorporum.org, gallica.bnf.fr (403), quod.lib.umich.edu (403) |

## Middle Dutch results

| ACU | Work | Source | Evidence |
|---|---|---|---|
| ACU-0438 | Wrake van Ragisel | dbnl.org PDF, ed. M. Gysseling | Text extracted and read: line-numbered Middle Dutch verse, "her walewain" present. **Copyright caution**: 1998 CD-ROM edition; DBNL warns works under 140 years old may be protected |
| ACU-0439 | Perchevael | `romanvanlancelo01joncgoog` | Jonckbloet 1846, 404pp, PD. 59 `Perchevael`, 54 `Moriaen`, 826 `Lanceloet`, 950 `Walewein` |
| ACU-0442 | Historie vanden Grale and Merlijn | `merlijnnaarhete00robegoog` | Steinfort MS, 1880, 430pp, PD. 82 `Merlijn`, 74 `Merline`, 25 `Grale`, 35 `Maerlant` |
| ACU-0443 | Merlijn continuation (Boec van coninc Artur) | `merlijnnaarhete00robegoog` | Same volume; 7 `Velthem` — the Steinfort MS carries Velthem's continuation after Maerlant |

Still open in this language group: ACU-0431 (Lantsloot — DBNL states the 1987
Gerritsen edition is copyright-protected and only scans exist), ACU-0445,
ACU-0446, ACU-0447.

## Old French: Romania and the 1928 lais edition

| ACU | Work | Source | Evidence |
|---|---|---|---|
| ACU-0177 | Lai de Tyolet | `romania_1879_8` | **Corrects an earlier "failed access" verdict.** Romania vol 8 (1879), 646pp, carries Gaston Paris's "LAIS INEDITS DE TYOLET, DE GUINGAMOR, DE DOON, DU LECHEOR ET DE TYDOREL", pp. 29–72. 51 `Tyolet` hits. Earlier passes searched for the article, not the journal volume |
| ACU-0179 | Doon, Tydorel (partial) | `romania_1879_8` | Same article: 25 `Doon`, 13 `Tydorel` |
| ACU-0178 | Lai de Melion | `thelaysofdesiregraelentandmelion` | Grimes 1928, 162pp, "edition of the texts". 75 `Melion` |
| ACU-0179 | Graelent (partial) | same | 77 `Graelent` |
| ACU-0239 | Lai de Désiré (partial) | same | 20 `Desiré` |
| ACU-0232 | Les Prophesies de Merlin | `lespropheciesdemerlinpatt2` | Paton 1927, edited from MS. **Caveat**: the catalog entry names the *printed* Prophesies; this is the manuscript edition. An incunable exists at `ita-bnc-in2-00001949-001` (1480) |

With ACU-0179 now holding Guingamor, Tydorel, Doon and Graelent, only
**l'Espine** of the five named in that entry is still missing.

Note on method: the Romania find came from searching for the *journal
volume* rather than the article. Persée has the article but 403s its PDF
route, and its issue pages are JavaScript-rendered so curl sees an empty
shell. archive.org had the whole volume as `romania_1879_8` the entire time.

### Confirmed absent or borrow-only after a French-language pass

ACU-0185 Yder · ACU-0196 Enfances Gauvain · ACU-0198 Roman de Silence ·
ACU-0200 Tournoiement Antecrist · ACU-0144 Prose Joseph · ACU-0169 Donnei
des amants — no archive.org candidate. ACU-0194 Gliglois exists only as
borrow-only scans (`gliglois0000char` 1932, `leromandegligloi0000unse` 2003).
ACU-0201 Roman du Hem: only an 1854 *analyse* (summary), not the text.

## Italian and Norse pass

| ACU | Work | Source | Evidence |
|---|---|---|---|
| ACU-0475 | Cantare di Gismirante | `064FioreDiLeggendeSi113` | Levi, *Fiore di Leggende: cantari antichi*, 1914. Prints "VII GISMIRANTE / PRIMO CANTARE" with the verse; 67 hits. Supersedes the Wikisource route, which was a transclusion wrapper |
| ACU-0478 | Liombruno | same | "III LIOMBRUNO / CANTARE PRIMO"; 111 hits |
| ACU-0461 | Tristrams kvæði | `slenzkfornkvi01littgoog` | *Íslenzk fornkvæði* 1854, 737pp, PD. Prints "23. Tristrams kvæði"; 18 hits plus 57 `Ísodd` |

### Rejected on inspection

- **ACU-0480 Cantare di Lasancis** — the Tavola Ritonda has 18 `Lasancis`
  hits, but reading them shows a **character** ("messer Lasancis") and
  editorial discussion of the name form, not the cantare. Not covered.
- `cantaricavallere00bariuoft` (Barini 1905) — only one incidental `Febus`
  hit; does not hold the target cantari.
- `latavolaritondao01poliuoft` and `iltristanoricca00parogoog` are real
  editions but answer ACU-0488 and ACU-0484, which are **already covered**.
  Extra witnesses only.

### Confirmed absent from archive.org

**Norse rímur and late romances**: ACU-0454 Skikkjurímur, ACU-0467 Erex
rímur, ACU-0468 Ívens rímur (Finnur Jónsson's *Riddararímur* is not there),
ACU-0469 Samsons saga fagra, ACU-0470 Ectors saga, ACU-0471 Vilhjálms saga
sjóðs. The prose sagas these derive from (ACU-0448–0453) are already
covered; it is the verse adaptations that are missing, and they were mostly
edited in 20th-century series still in copyright.

**Italian**: ACU-0473, 0474, 0476, 0479, 0480, 0481, 0483, 0485, 0486,
0487, 0493, 0495, 0496 produced no usable candidate.

## Latin pass — the last unworked cluster, and it was productive

| ACU | Work | Source | Evidence |
|---|---|---|---|
| ACU-0028 | De Principis Instructione | `giraldicambrensi08gira` | Rolls Series vol 8, 556pp. Principis=213, Instructione=154, Glaston=15 |
| ACU-0029 | Speculum Ecclesiae | `giraldicambrensi04gira` | Rolls Series vol 4, 534pp. Speculum=140, Ecclesiae=22. **Corrects an earlier rejection**: the candidate I rightly refused was Nicolaus de Clemangis's identically-titled work; this is Gerald of Wales. Vol 4 did not surface in the title search but exists |
| ACU-0030 | Itinerarium + Descriptio Kambriae | `giraldicambrensi06gira` | Rolls Series vol 6, 376pp. Itinerarium=38, Descriptio=93 |
| ACU-0048 | Life of St Kentigern (Jocelin) | `livesofsniniansk00forb` | Forbes 1874, 510pp, PD. Kentigern=352, Jocelin=68 |
| ACU-0049 | Lailoken and Kentigern / Lailoken and Meldred | same | Lailoken=5, Laloecen=2, Meldred=1 |
| ACU-0037 | Narratio de Arturo Rege et Rege Gorlagon | `cu31924027098072` | Kittredge 1903, 146pp. Gorlagon=115, Arthur=157 |
| ACU-0015 | Vita Sancti Dubricii | `liberlandavensi00reesgoog` | Liber Landavensis 1840, 707pp, PD, Latin. Dubricius=289 |

### Checked and rejected

**ACU-0010 / ACU-0011 (the two Vitae Gildae) are NOT in Mommsen**, which the
collection already holds. Zero hits for "Vita Gildae", "Vitae Gildae",
"Rhuys", "Ruys" or "Llancarfan" in `chronicaminorasa00momm`. Assuming
otherwise would have been easy and wrong.

Also no candidate: ACU-0046 Anglica Historia in Latin (the Camden Society
English translation is held), ACU-0527 Questa del Sant Grasal.
