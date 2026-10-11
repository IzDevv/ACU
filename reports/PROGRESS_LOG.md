# Progress log — Arthurian primary-text acquisition (session 2026-10-11)

## Environment constraint (established at session start, verified)

This session CANNOT download files and CANNOT fetch/inspect web pages.

- Outbound HTTPS goes through a policy-enforcing egress proxy. Every text
  repository probed returned `403 CONNECT` (organization egress policy):
  archive.org, www.gutenberg.org, gallica.bnf.fr, fr.wikisource.org,
  en.wikisource.org, babel.hathitrust.org, books.google.com, celt.ucc.ie,
  quod.lib.umich.edu, daten.digitale-sammlungen.de, dla.library.upenn.edu,
  www.rialto.unina.it, huggingface.co.
  Only github.com / raw.githubusercontent.com and package registries pass.
- WebFetch also fails on these hosts (`getaddrinfo ENOTFOUND`), so no page,
  scan, title page or contents list can be opened and inspected.
- Only one environment exists on this account ("Default"), so there is no
  alternative environment to run from.

Consequence for outcome labels: NO result in this session can be a
"verified download" or a "verified readable primary text". Everything is an
"unverified lead" or a "failed access". No transcription was possible.

## Local-holdings constraint

The working directory /home/user/ACU was an empty git repository with no
commits. None of the previously acquired files are present. I therefore did
NOT inspect any local copy, and make no claim about local file contents.
Statements about existing coverage come from the two supplied documents only.

## Method actually used

WebSearch (which does work) with domain-restricted queries, to recover exact
landing-page URLs and bibliographic detail for standard editions. Leads are
recorded with the search evidence that supports them. Cost/expenditure is not
exposed to me by this platform, so I report no spend figure.
