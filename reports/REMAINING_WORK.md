# Remaining work

Totals are the 543 entries as classified in the supplied `ACQUISITION_INDEX.md`.
"New lead" means this session found a real catalogue record for it — never a
downloaded or inspected text.

| Category | Entries | New lead this session | Still untouched |
|---|---|---|---|
| No primary text recovered (searched, nothing found) | 212 | 0 | 212 |
| No primary text recovered (candidate found, identity/access unverified) | 55 | 18 | 37 |
| Translation only | 34 | 25 | 9 |
| Partial original-language coverage | 233 | 1 | 232 |
| Access blocked | — | see below | — |
| Identity unresolved | 4 | 4 | — |
| Lost / hypothetical / mixed | 9 | 0 | 9 |

## 1. No primary text recovered

**212 entries** carry "Searched Archive; no candidate from these queries,
unresolved" or "Search reviewed: displayed hits unsuitable". I did not reach
any of these — the session's search effort went to the two higher-priority
bands first, and without the ability to open a page there was no way to
convert a weak candidate into a verified text anyway.

**37 further entries** have a prior metadata candidate but got no new lead
from me:
ACU-0084, 0113, 0148, 0160, 0164, 0167, 0168, 0194, 0197, 0207, 0208, 0211,
0215, 0222, 0226, 0229, 0231, 0238, 0245, 0246, 0286, 0289, 0291, 0303, 0310,
0311, 0312, 0313, 0348, 0373, 0383, 0427, 0494, 0514, 0515, 0532, 0537.

Of these, the ones I judge most likely to yield quickly to an unblocked
session, because a public-domain edition almost certainly exists:
ACU-0291 (Chaucer, *Wife of Bath's Tale*), ACU-0289 (Lydgate, *Siege of
Thebes*), ACU-0303 (Robinson's *Learned and True Assertion*), ACU-0310,
0312, 0313 (Early Modern English prose chapbooks), ACU-0348 (Scott's *Sir
Tristrem*, 1804), ACU-0373 (Tennyson, *Merlin and the Gleam*), ACU-0245
(*Short English Metrical Chronicle*, EETS), ACU-0246 (*Arthur*, EETS OS 2).

## 2. Translation only

**9 entries** still have no original-language lead at all:
ACU-0056, 0060, 0078, 0080, 0082, 0090, 0121, 0214, 0234.
Seven of those nine are Welsh (0056, 0060, 0078, 0080, 0082, 0090, 0121);
ACU-0214 is Occitan (*Blandin de Cornoalha*) and ACU-0234 Old French
(*Folie Lancelot*, ed. Bogdanow 1965 — modern and probably in copyright).

**3 entries are not real gaps** and I recommend reclassifying them:
ACU-0368 (*The Mabinogion*, Guest trans.), ACU-0369 (*The High History of
the Holy Graal*, Evans trans.), ACU-0370 (Weston trans.). In each case the
catalogued work **is** a translation, treated as a reception-history item,
so "original still sought" cannot be satisfied — the Welsh and Old French
source texts are separately catalogued elsewhere. Correcting these three
would reduce the translation-only count from 34 to 31.

**3 entries have only weak leads**: ACU-0055, 0064, 0065 (Welsh Arthur and
Myrddin poems). Neither the Black Book of Carmarthen nor Skene's *Four
Ancient Books* was confirmed to contain them.

## 3. Partial original-language coverage

**233 entries** are marked "Original-language source downloaded; coverage
notes apply". I could not assess any of them: the working directory held no
commits and none of the previously acquired files were present, so I never
saw a local copy and make no claim about what any of them contains. Only
ACU-0003 picked up a new lead (a better critical text, Mommsen's MGH).

This band needs a local-file audit, not web searching. The right next step
is to list, for each of the 233, which volume/section is actually on disk
and what the catalog entry requires — work that needs the files.

### Possible already-covered excerpts (to check against existing holdings)

I could not inspect local copies, so I record these as possibilities only:

- ACU-0251 (*Chronicle of England*) may be the same text as ACU-0249
  (prose *Brut*) — the Middle English prose Brut circulated under that
  title. If ACU-0249's holdings arrive first, 0251 may need no separate
  acquisition, or may need to be redefined as Caxton's 1480 print.
- ACU-0001 and ACU-0003: Mommsen's *Chronica minora* vol. 3 prints Gildas
  and the *Historia Brittonum* together, so the Historia copy already held
  (Gunn/Nennius 1819) sits beside a Gildas Latin text in the same critical
  volume.
- ACU-0179's Guingamor may already be inside a Warnke *Lais* copy, if any
  Warnke volume was among the Marie de France material acquired earlier.

## 4. Access blocked

Everything in this session, for one reason: the environment's egress policy.
No source-specific block (paywall, CAPTCHA, login) was encountered, because
no request reached a repository. See `MANUAL_DOWNLOAD_QUEUE.md` for the host
list and the per-target failure table.

Two genuine source-side restrictions were identified by search, and will
still apply in an unblocked session:

- **CELT's electronic Stokes *Acallamh na Senórach*** (ACU-0113) is marked
  **[RESTRICTED]** — available only by prior consent for academic research
  and teaching. Needs a permission request, not a download.
- **Lending-only archive.org scans** (identifiers ending `0000…`) are
  borrow-only: ACU-0167's `lafolietristando0000erne`, ACU-0164's Kuhse
  dissertation, the Tolkien–Gordon SGGK, and others. Borrowing gives
  reading access, never a file.

## 5. Identity unresolved

- **ACU-0506** *A Demanda do Santo Graal* — the one candidate's evidence is
  self-contradictory (title names the Portuguese editor Megale; the item was
  described as Spanish). The Spanish Demanda is a separate work.
- **ACU-0511 vs ACU-0515** — the Bonilla 1912 reprint of the Valladolid 1501
  *Tristán* is a strong find, but which of these two entries it belongs to
  (*Cuento de Tristán* vs *Libro de Tristán*, fragments) is not settled. It
  must be filed against one, not both.
- **ACU-0251** — see above.

## 6. Lost / hypothetical / mixed

**9 entries**, untouched this session. These need a different treatment from
acquisition: for each, the collectable object is the set of surviving
*references* in other texts, not an edition of the work. That work is best
done once the chronicle and romance holdings are readable, since the
references live inside texts the catalog already covers. I did not attempt
any reconstruction, and no text should be supplied for these entries.
