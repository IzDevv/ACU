# Final statistics — session of 2026-10-11

## Coverage

| | start | end | change |
|---|---|---|---|
| Original-language source held | 233 | **341** | +108 |
| Translation only | 34 | **6** | −28 |
| **Any coverage** | **267 (49.2%)** | **347 (63.9%)** | **+80** |
| Nothing held | 276 | 187 | −89 |
| Lost / hypothetical | 9 | 9 | — |
| Total catalog | 543 | 543 | — |

**80 catalog entries gained coverage.** Of those, 28 were entries that had
only an English translation and now have the text in its original language —
Welsh, Latin, Old French, Middle Dutch, Middle High German, Italian,
Icelandic, Spanish and Portuguese.

## Files

- ~150 files downloaded into Google Drive, roughly 3 GB
- Every `ACU_sources/<slug>/` folder holds a PDF, a text layer, and a
  `_source.txt` naming the source and the entry it serves
- 14 Colab batches, all idempotent — re-running verifies rather than repeats
- 1 manual transcription, explicitly marked a sample, not coverage

## How the 80 were found

| route | entries |
|---|---|
| archive.org, searched by English title | ~45 |
| archive.org, searched in the work's own language | ~12 |
| Already inside a volume previously downloaded | 6 |
| Wikisource transcriptions | 6 |
| maryjones.us (a personal scholarly site) | 5 |
| Right edition, wrong volume — corrected | 3 |
| Gutenberg via its archive.org mirror | 2 |
| DBNL (Dutch national library) | 1 |

The last five rows are the interesting ones: a third of the gains came from
routes that were not tried until the approach was challenged.

## Corrections made to my own work

Eight, all recorded with evidence in VERDICTS.md:

1. Claimed five entries already covered by one volume; only two were.
2. Swapped the IDs of ACU-0051 and ACU-0052.
3. Mislabelled ACU-0066 and ACU-0067, so two searches hunted the wrong works.
4. Downloaded Gale vol. 1 for ACU-0017; the text is in vol. 3.
5. Downloaded the Norse *Tristrams saga* for ACU-0460, which wants the
   Icelandic *Saga af Tristram ok Ísodd*.
6. Accepted a scan for ACU-0506 whose OCR was pure noise.
7. Said the remainder was blocked by copyright. Mostly wrong — the works are
   public domain; the blocker is usually host access.
8. Declared seven entries unavailable that were later found.

## What is actually left

**187 with nothing, 6 translation-only.** Treat that as an upper bound on
what is missing, not a count of what is unavailable — see the false-negative
table in HANDOFF.md.

By kind:

1. **Browser-recoverable** — public domain, digitised, hosted somewhere that
   refuses automated requests (Persée, TEAMS, Gallica, HathiTrust, Google
   Books). Unmeasured, probably the largest tractable group. Two confirmed
   examples are listed in HANDOFF.md with URLs.
2. **Permission required** — three Irish texts on CELT.
3. **Only ever edited in a modern edition** — the Norse rímur are the clear
   case: every prose saga is held, no verse retelling is.
4. **Never edited; manuscript only** — chiefly the Italian Tristan versions.
5. **Lost** — 9.

## Method notes worth keeping

- **Reading beats scoring.** A keyword scorer rated a 1983 journal article a
  perfect match for a medieval Welsh poem. Opening each candidate's first
  page caught every false positive.
- **Search in the work's own language.** English-title searches had
  exhausted archive.org; Dutch, French and Italian queries then found a
  dozen more entries on the same site.
- **Automated title-variant generation does not work.** Tried over 30
  entries, returned essentially nothing: "Glastonbury" matched festival
  pass-outs. The recoveries came from knowing edition history.
- **Check what you already own first.** Six entries were already inside
  volumes downloaded earlier.
