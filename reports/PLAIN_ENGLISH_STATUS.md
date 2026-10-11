# Where things stand — in plain English

No jargon. For the technical record with evidence, see `VERDICTS.md`.

## What your project is

You have a catalog of **543 Arthurian works** — every text from the 500s to
the modern era that touches the King Arthur story. The goal is to actually
possess each one, preferably in the language it was written in rather than
in English translation.

## What happened today

You started with **267 of 543** having some file attached.

Today added roughly **50 more** works, and found **2 you already had
without realising it**.

**Correction.** I first told you that was five. It was two. I checked five
Welsh poems against a book you already own, *The Four Ancient Books of
Wales*, and found all five printed inside it — but when I went back to your
catalog, three of them (ACU-0051, 0052, 0053) were already marked as
covered before today. Only ACU-0050 and ACU-0064 were genuine gaps. I had
also swapped two of the ID numbers in my own notes. The underlying find is
real and still useful, but the count was wrong and I'd rather say so.

The find is worth explaining anyway, because it's the most useful kind.
The book spells those poem titles in medieval Welsh and your catalog spells
them in modern Welsh. Searching for `Pa Gur` finds nothing; searching for
`Pa gur yv y porthaur` finds the poem. Same trick found a sixth entry later
in the day: a poem whose title the scanner had misread as `GWASGARGEED`.

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

Of the three Welsh items I said were outstanding, two are now settled:
**ACU-0065** is in the *Myvyrian Archaiology* at page 105, and **ACU-0067**
turned out to be already covered — it isn't a Merlin poem at all, it's the
Welsh Triads, and I had mislabelled it. **ACU-0066** (*Peiryan Vaban*) is
still genuinely missing.

**ACU-0031** is now found too: a Latin chronicle that describes monks
digging up what they claimed was Arthur's grave at Glastonbury in 1191,
including the inscription on the lead cross they said was buried with him.

Three Irish texts were found but need **your** permission request — the
university that hosts them asks people to write first. They're in
`sources/_celt/README_PERMISSION_REQUIRED.md`. I did not put them in your
Drive, because that would be redistributing something I wasn't licensed to.

## If you only remember one thing

Run the Colab cells I send. Read the warnings. Ignore the rest unless you
want it.
