# Where things stand — in plain English

No jargon. For the technical record with evidence, see `VERDICTS.md`.

## What your project is

You have a catalog of **543 Arthurian works** — every text from the 500s to
the modern era that touches the King Arthur story. The goal is to actually
possess each one, preferably in the language it was written in rather than
in English translation.

## What happened today

You started with **267 of 543** having some file attached.

Today added roughly **50 more** works, and found **5 you already had
without realising it**.

Those five are worth explaining, because it's the most useful kind of find.
You own a book called *The Four Ancient Books of Wales*. Five catalog
entries — five separate Welsh poems — are printed inside it. Nobody had
noticed, because the book spells their titles in medieval Welsh and the
catalog spells them in modern Welsh. Searching for `Pa Gur` finds nothing;
searching for `Pa gur yv y porthaur` finds the poem. Five entries closed,
nothing downloaded.

## The three kinds of thing I hand you

1. **A Colab cell** — a block of code you paste into that notebook and run.
   It downloads files into your Google Drive. You've run two; batch 4 is
   waiting. That's all they do.
2. **Notes in the repo** — my reasoning, so a mistake can be traced.
3. **Warnings** — when something is probably wrong. Read these.

## What to actually watch for

I can be wrong in ways you can't easily catch, so these are the things worth
your attention:

- **"Wrong volume."** Old books come in sets. Getting volume 1 when the text
  is in volume 3 looks like success but isn't. This happened three times
  today; I caught them by checking the downloaded files afterwards.
- **"Wrong work."** Two different medieval texts often share nearly the same
  title. One download today was a Norwegian Tristan story where the catalog
  wanted an Icelandic one. Related, not the same.
- **"Bad scan."** Some old books were photographed but the computer couldn't
  read the text. You get a file, but it's a picture, not searchable words.
  One today was pure noise.
- **"Translation, not original."** Your goal is original languages. Some
  finds are only English versions. I label these; they're worth having but
  they don't close the entry.

## What is still missing

About **190** of the 543 entries still have nothing. Honestly, many never
will — they survive only in manuscripts that were never photographed, or in
modern scholarly editions still under copyright. The previous research in
your register was broadly right that most of these are dead ends.

Three Welsh poems about Merlin (ACU-0065, 0066, 0067) are close but not
found: they're printed in an old collection called the *Myvyrian Archaiology*,
which is the next thing to chase.

Three Irish texts were found but need **your** permission request — the
university that hosts them asks people to write first. They're in
`sources/_celt/README_PERMISSION_REQUIRED.md`. I did not put them in your
Drive, because that would be redistributing something I wasn't licensed to.

## If you only remember one thing

Run the Colab cells I send. Read the warnings. Ignore the rest unless you
want it.
