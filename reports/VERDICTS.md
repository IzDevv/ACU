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
