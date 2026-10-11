# OCR quality of the downloaded text layers

Measured on a 300 KB sample of each `_djvu.txt`, counting tokens that are
1–2 characters or have no vowel — a rough proxy for scanner noise. Healthy
prose OCR sits around 12–20%. Above roughly 30% the text layer is largely
unusable for searching or quotation.

This matters because the text layer is what makes a holding **searchable**.
A high score does not mean the PDF is bad — the page images are fine in
every case below. It means you should not trust a keyword search against
that item, and should read the scan instead.

| junk % | item | serves | note |
|---|---|---|---|
| 37.8 | `recueilgnral03montuoft` | ACU-0176 Mantel mautaillié | worst in the collection; 13th-c. French with heavy abbreviation |
| 33.3 | `LePreuxEtVaillantChevallierArtus1503` | ACU-0207 Artus de Bretagne | 1503 blackletter |
| 30.3 | `lesdeuxpomesde00bduoft` | ACU-0167 + 0168 Folie Tristan | short text, so the worst case for searching |
| 30.3 | `hin-wel-all-00002399-001` | ACU-0494 Vita di Merlino | 1554 Italian print |
| 28.6 | `bim_…the-most-ancient-and-fam_arthur-king_1634` | ACU-0338 Prince Arthur | 941pp of blackletter |
| 28.2 | `slenzkfornkvi01littgoog` | ACU-0461 Tristrams kvæði | Icelandic diacritics confuse the scanner |
| 25.5 | `HuonDeBordeaux1586` | ACU-0210 Huon de Bordeaux | |
| 24.8 | `sirtristremamet00scotgoog` | ACU-0348 Sir Tristrem | |
| 24.1 | `bib_fict_4103138_1` | ACU-0335 Percy's Reliques | |
| 21.6 | `bub_gb_XCTIrJ7jeVUC` | ACU-0423 Fastnachtspiele | |
| 21.4 | `holinshedschroni01holi` | ACU-0305 Holinshed | acceptable |

Not measurable: `bim_…brittains-ida…_1628` (ACU-0317). Its text layer is
only 29 KB for 39 pages, too small to sample at the offset used. Inspection
of the page images shows the OCR renders "Edmond Spencer" as "EDpwonD
SeuncaR" and "Brittaines Burse. 1628" as "Brittames Banſe. I 648". Treat
its text layer as worthless.

## A caution about a metric that did not work

The first attempt ranked items by bytes-of-text per page, assuming sparse
text meant failed OCR. It does not: **verse** is naturally sparse. That
method put *Íslenzk fornkvæði* (933 B/page) at the top purely because it is
poetry, and would have sent transcription effort at a perfectly good scan.
The junk-token measure above separates the two.

## On hand transcription

Tried, and abandoned as not worth the rate at this scale. It remains the
right tool for a **short** text that is legible but undownloadable, or for a
single key passage. It is not a way to rescue a 156-page volume.
`transcriptions/ACU-0317_brittains_ida_1628_prelims.txt` is kept as a
worked sample and is explicitly marked as not constituting coverage.
