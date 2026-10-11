# Results report — 2026-10-11

## Headline

**No files were downloaded and no text was inspected.** This environment
cannot reach any text repository, so the acquisition task as specified could
not be carried out. What I produced instead is the authorized fallback: a
queue of exact, actionable download links, with the bibliographic evidence
behind each one and an honest label on how far it has been verified.

## Why nothing could be downloaded

Outbound HTTPS from this session passes through a policy-enforcing egress
proxy. Every text repository I probed was refused at the tunnel with
`403 CONNECT` — an organization egress-policy denial, not a site error:

> archive.org · www.gutenberg.org · gallica.bnf.fr · en.wikisource.org ·
> fr.wikisource.org · babel.hathitrust.org · books.google.com ·
> celt.ucc.ie · quod.lib.umich.edu · daten.digitale-sammlungen.de ·
> dla.library.upenn.edu · www.rialto.unina.it · huggingface.co

Only `github.com` and package registries pass. WebFetch fails on the same
hosts with `getaddrinfo ENOTFOUND`, so I could not even open a landing page,
title page or contents list — which also means **no transcription was
possible**. Only one environment exists on this account, so there was no
alternative to run from.

To lift this: in the cloud environment's settings (environment menu in the
session title bar → Edit), either raise **Network access** to a broader
level or add these hosts under **Allowed domains**, leaving "Allow package
managers" ticked. The relevant page is
<https://code.claude.com/docs/en/cloud-environments#network-access>.
`archive.org` alone would unblock most of the queue below.

I also could not read the existing collection: `/home/user/ACU` was an empty
git repository with no commits, so none of the previously acquired files were
present. I did not inspect any local copy and make no claim about their
contents. Everything about current coverage comes from the two documents you
supplied.

## What I did instead

WebSearch does work. I ran 20 domain-restricted searches against the
priority queue and recovered real catalogue records — editor, date, series,
imprint, and the archive.org identifier — for the standard editions of the
highest-value gaps. Each is recorded with the search evidence that supports
it and an explicit limitation.

## Counts

Using your taxonomy, strictly:

| Outcome | Count |
|---|---|
| Verified downloads | **0** |
| Verified readable primary text | **0** |
| Unverified leads | **38 catalog entries** |
| Failed access | every target (see above); 3 entries where the standard edition could not even be located |

Breaking the 38 down:

- **Newly covered catalog entries: 0.** Nothing was acquired, so coverage is
  unchanged at 267.
- **Entries that would newly gain coverage if the queue is downloaded: 17** —
  ACU-0041, 0129, 0146, 0190, 0249, 0251, 0259, 0274, 0275, 0277, 0279, 0305,
  0388, 0423, 0506, 0511, 0519.
- **Originals recovered for translation-only entries: 0 recovered; 18 with
  solid original-language leads** — ACU-0001, 0007, 0008, 0009, 0014, 0071,
  0072, 0073, 0074, 0075, 0076, 0077, 0172, 0173, 0174, 0179 (partial), 0213,
  0240. Three more (ACU-0055, 0064, 0065) have weak leads only.
- **Partial gaps filled: 0.** One upgrade lead (ACU-0003, Mommsen's critical
  text). The other 232 partially-covered entries need a local-file audit,
  which needs the files.
- **Additional editions beyond the primary lead: 19** alternate copies or
  second witnesses, listed in the queue.
- **Files: 0 downloaded, 0 bytes.** 5 documents written to the repository.

## Findings worth more than a link

Five results change the shape of the remaining work:

1. **Seven translation-only Welsh entries collapse into one download.**
   Rhys & Evans's 1887 *Text of the Mabinogion* from the Red Book of Hergest
   supplies the Welsh originals for ACU-0071 through 0077 in a single volume,
   with a CC0 copy available.
2. **Four translation-only Latin Vitae collapse into one download.** Rees's
   1853 *Lives of the Cambro British Saints* prints Latin with facing
   English for Cadoc, Carantoc, Paternus and Illtud. Worth a caveat: a
   scholarly judgement quoted in the search calls Rees's Latin "teeming with
   blunders", so Wade-Evans's *VSBG* (1944) is the sound text if obtainable.
3. **Three of the 34 translation-only entries are not gaps at all.**
   ACU-0368, 0369 and 0370 *are* translations — Guest's *Mabinogion*,
   Evans's *High History*, Weston's versions — catalogued as
   reception-history works. "Original still sought" cannot be satisfied for
   them, because their language of composition is English. Reclassifying
   these three takes the real translation-only figure from 34 to 31.
4. **ACU-0251 may duplicate ACU-0249.** The Middle English prose *Brut*
   circulated as "The Chronicles of England", which is ACU-0251's title.
   Worth settling before spending effort on it as a separate acquisition.
5. **One download serves ACU-0001 and ACU-0003 together.** Mommsen's
   *Chronica minora* vol. 3 (MGH AA XIII) prints Gildas's *De excidio* and
   the *Historia Brittonum* in the same volume.

Two cautions on specific items:

- The Bonilla 1912 Spanish *Tristán* is a strong find but must be filed
  against **either** ACU-0511 or ACU-0515, not both.
- A Furnivall *Le Morte Arthur* of 1864 surfaced while searching for
  ACU-0246's *Arthur* (Liber Rubeus Bathoniae). These are different works —
  do not let the date coincidence merge them.

## Cost

This platform does not expose spend to me. I cannot report actual
expenditure and did not estimate it. What I can report is volume: 20 web
searches and no downloads, which is a small fraction of a $100 ceiling.

## Next actions, in order

1. **Unblock `archive.org`** in the environment's network settings — that
   single change converts most of this queue into real downloads.
2. **Commit the existing collection** to this repository, or point a session
   at wherever the files live. Without them, the 233 partially-covered
   entries cannot be assessed at all, and that is the largest band in the
   catalog.
3. Then work the queue in the order given: Tier 1 first (five downloads
   covering roughly twenty entries), then Tier 2, then verify Tier 3's
   contents before trusting them.

## Files in this repository

- `reports/RESULTS_REPORT.md` — this report
- `reports/FINDINGS.csv` — 45 rows, 44 catalog entries, full schema
- `reports/MANUAL_DOWNLOAD_QUEUE.md` — tiered exact links + failure table
- `reports/REMAINING_WORK.md` — the six categories you asked for
- `reports/PROGRESS_LOG.md` — constraints, method, resumption point
- `ACQUISITION_INDEX.md`, `RESEARCH_REGISTER.md` — your documents, unmodified
