#!/usr/bin/env bash
# Build a manifest of the local source collection, for committing to git
# in place of the source files themselves.
#
# Usage:  tools/make_manifest.sh /path/to/sources [outdir]
#
# Emits:
#   manifest.tsv   relpath, bytes, sha256, pages (PDFs, if pdfinfo present)
#   summary.txt    totals by extension and by top-level directory
#
# Needs: bash, find, sha256sum (or shasum). pdfinfo (poppler-utils) optional.

set -euo pipefail
SRC="${1:?usage: make_manifest.sh /path/to/sources [outdir]}"
OUT="${2:-.}"
[ -d "$SRC" ] || { echo "not a directory: $SRC" >&2; exit 1; }
mkdir -p "$OUT"

if command -v sha256sum >/dev/null; then HASH() { sha256sum "$1" | cut -d' ' -f1; }
elif command -v shasum   >/dev/null; then HASH() { shasum -a 256 "$1" | cut -d' ' -f1; }
else echo "no sha256sum or shasum found" >&2; exit 1; fi

HAVE_PDFINFO=0
command -v pdfinfo >/dev/null && HAVE_PDFINFO=1 || \
  echo "note: pdfinfo not found — page counts will be blank (install poppler-utils)" >&2

printf 'relpath\tbytes\tsha256\tpages\n' > "$OUT/manifest.tsv"

# -print0 / read -d '' so paths with spaces, quotes or newlines survive
find "$SRC" -type f -print0 | sort -z | while IFS= read -r -d '' f; do
  rel="${f#"$SRC"/}"
  bytes=$(wc -c < "$f" | tr -d ' ')
  sum=$(HASH "$f")
  pages=""
  if [ "$HAVE_PDFINFO" = 1 ] && [ "${f##*.}" = "pdf" ]; then
    # pdfinfo fails on corrupt/encrypted PDFs; swallow that inside the group
    # so pipefail+errexit cannot abort the whole scan on one bad file.
    pages=$( { pdfinfo "$f" 2>/dev/null || true; } | awk '/^Pages:/{print $2}' )
    [ -n "$pages" ] || pages="?"
  fi
  printf '%s\t%s\t%s\t%s\n' "$rel" "$bytes" "$sum" "$pages" >> "$OUT/manifest.tsv"
done

{
  echo "Source collection manifest — $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "Root: $SRC"
  echo
  n=$(( $(wc -l < "$OUT/manifest.tsv") - 1 ))
  echo "Files: $n"
  awk -F'\t' 'NR>1{t+=$2} END{printf "Total bytes: %d (%.2f GiB)\n", t, t/1073741824}' "$OUT/manifest.tsv"
  echo
  echo "By extension (count, bytes):"
  awk -F'\t' 'NR>1{n=split($1,p,"."); e=(n>1)?tolower(p[n]):"(none)"; c[e]++; b[e]+=$2}
              END{for(e in c) printf "  %-10s %6d  %12d\n", e, c[e], b[e]}' \
      "$OUT/manifest.tsv" | sort -k3 -nr
  echo
  echo "By top-level directory (count, bytes):"
  awk -F'\t' 'NR>1{split($1,p,"/"); d=(p[2]!="")?p[1]:"(root)"; c[d]++; b[d]+=$2}
              END{for(d in c) printf "  %-40s %6d  %12d\n", d, c[d], b[d]}' \
      "$OUT/manifest.tsv" | sort -k3 -nr
  echo
  echo "Files over 100 MiB (would be REJECTED by github.com):"
  awk -F'\t' 'NR>1 && $2>104857600 {printf "  %12d  %s\n", $2, $1}' "$OUT/manifest.tsv" \
    | sort -nr || true
  awk -F'\t' 'NR>1 && $2>104857600' "$OUT/manifest.tsv" | grep -q . || echo "  (none)"
} > "$OUT/summary.txt"

echo "wrote $OUT/manifest.tsv and $OUT/summary.txt"
