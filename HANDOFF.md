# Handoff — for a session that has a browser

Written at the end of a cloud session that had **no browser access**. That
turned out to be the binding constraint. Anything below marked "browser"
is public domain, already digitised, and blocked only because the host
refuses automated requests. A human with a browser — or an agent driving
one — gets them in minutes.

## State

| | |
|---|---|
| Catalog entries | 543 |
| Covered at session start | 267 |
| Covered now | ~350 |
| Remaining | ~191 (an upper bound; see "false negatives" below) |
| Lost / hypothetical | 9 — not acquirable, only referenceable |

Files live in Google Drive under `ACU_sources/<work_slug>/`, each folder
holding a PDF, a text layer, and `_source.txt` recording which archive.org
item it came from and what it serves.

## Do these first — they need only a browser

Each is free, out of copyright, and confirmed to exist. Each 403s or
challenges automated clients.

| ACU | Work | URL |
|---|---|---|
| ACU-0169 | Donnei des Amants (Tristan Rossignol episode) — Gaston Paris, *Romania* 25 (1896) 497–541 | https://www.persee.fr/doc/roma_0035-8029_1896_num_25_100_5472 |
| ACU-0196 | Les Enfances Gauvain — Paul Meyer, *Romania* 39 (1910) 1–32 | https://www.persee.fr/doc/roma_0035-8029_1910_num_39_153_5096 |

Hosts that block automation but serve browsers, each holding public-domain
Arthurian material still missing here:

- **Persée** — the complete *Romania* run 1872–2020. archive.org has only
  1872–1888 and 1920+, so **1889–1919 is reachable nowhere else I tried.**
  Many Old French texts were first printed in those volumes.
- **TEAMS / d.lib.rochester.edu** — free scholarly editions of many Middle
  English Arthurian romances. Cloudflare interstitial on every path. This is
  probably the single richest blocked source for the English entries.
- **Gallica**, **HathiTrust**, **Biblioteca Digital Hispánica**, **Europeana**
  — all 403.
- **Google Books** — reachable, but the API's daily quota for shared cloud
  IPs is exhausted. An API key or a browser session fixes it.
- **DBNL** — serves pages to a full browser header set, but 403s its own
  search endpoint. Discovery has to come from elsewhere.

## Read this before trusting any "not available" verdict

Every false negative in this project came from one mistake: **treating an
unmatched title search as proof of absence.** Confirmed cases where the text
was present all along:

| Work | Why the search missed it |
|---|---|
| Lai de Tyolet | Not a book — an article inside *Romania* vol. 8 |
| Peiryan Vaban | On a site whose index lists it without a link |
| Gerald's *Speculum Ecclesiae* | Volume 4 of a set I'd already taken four volumes from |
| Rigomer Band I | My first search of the session said it didn't exist |
| La Mule sans frein | Both editions are titled "La mule sanz **frain**" |
| Cyfoesi Myrddin | Skene prints "Kyuoessi Myrdin a Gwendyd y chOaer" |
| Gwasgargerdd | The scanner read the running head as "GWASGARGEED" |

**Automating around this does not work.** A variant generator (accent
stripping, orthography swaps, dropped articles) was tried over 30 entries
and returned essentially nothing: "Glastonbury" matched festival
pass-outs, "Thirteen Treasures" a children's novel. The recoveries came
from knowing edition history, which is per-entry work.

## Outstanding, by kind

1. **Browser-recoverable** — the Persée items above, plus whatever TEAMS
   holds. Unmeasured, probably the largest tractable group.
2. **Needs a permission email** — three Irish texts on CELT (*Acallamh na
   Senórach*, Tadhg Dall Ó hUiginn, *Annals of Tigernach*). Downloaded but
   deliberately kept out of Drive; see `sources/_celt/README_PERMISSION_REQUIRED.md`.
3. **Genuinely restricted** — only ever edited in 20th-century series. The
   Norse rímur are the clear case: every prose saga is held, no verse
   retelling is.
4. **Never edited / manuscript only** — chiefly the Italian Tristan versions.
5. **Lost** — 9 entries.

## Unresolved identity questions

- **ACU-0056 vs ACU-0088** — maryjones.us heads this one text "Ymddiddan
  rhwng Arthur a Gwenhwyfar / AKA: Ymddiddan Melwas a Gwenhwyfar". The
  catalog lists them separately. Possibly one work.
- **ACU-0511 vs ACU-0515** — Bonilla's 1912 reprint of the 1501 *Tristán*
  may belong to either.
- **ACU-0157 / ACU-0158** — what is filed is the **Vulgate** Queste and
  Mort Artu; the catalog wants the **Post-Vulgate**. Related, not identical.
- **ACU-0251** — may duplicate ACU-0249 (the prose *Brut* circulated as
  "The Chronicles of England").
- **ACU-0146** — vol. 1 of Hucher is held; the Perceval text is in vol. 2.
- **ACU-0213** — Jaufre tome II only.
- **ACU-0179** — four of its five named lais; *l'Espine* still missing.

## Quality caveat

`reports/OCR_QUALITY.md` lists four holdings whose text layers are too
corrupt to search (worst: the *Mantel mautaillié* volume at 38% junk). The
page images are fine. Don't conclude a text is absent because a search of
the collection missed it.

## Where the detail is

- `reports/VERDICTS.md` — every accept and reject, with the evidence
- `reports/OCR_QUALITY.md` — which text layers are unreliable
- `reports/PLAIN_ENGLISH_STATUS.md` — the same story without jargon
- `reports/BATCH*_CELL.py` — every download batch, re-runnable and idempotent
- `ACQUISITION_INDEX.md` — the catalog, updated with this session's results
