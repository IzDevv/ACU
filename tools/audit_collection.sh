#!/usr/bin/env bash
# Audit the local source collection, one row per WORK FOLDER.
#
# Assumes the layout seen in the collection: <root>/<work_slug>/<files...>
# (files may be nested further inside; all are counted).
#
# Usage:  tools/audit_collection.sh /path/to/sources [outdir]
#
# Emits:
#   works.tsv      one row per work folder: slug, files, bytes, formats, state
#   empty.txt      work folders containing NO files — failed acquisitions
#   files.tsv      per-file detail: relpath, bytes, sha256
#   summary.txt    totals, state counts, format counts, oversize files
#
# States:
#   EMPTY        no files at all — nothing was acquired
#   NO_TEXT      only page-image formats (pdf/djvu/images), no text layer
#   TEXT_ONLY    text present, no page images to check it against
#   TEXT+SCAN    both a text layer and a scan — the target state
#
# Needs: bash, find, sha256sum (or shasum).

set -uo pipefail   # NOT -e: one unreadable file must not abort a 5GB scan
SRC="${1:?usage: audit_collection.sh /path/to/sources [outdir]}"
OUT="${2:-.}"
[ -d "$SRC" ] || { echo "not a directory: $SRC" >&2; exit 1; }
SRC="${SRC%/}"
mkdir -p "$OUT"

if   command -v sha256sum >/dev/null; then HASH() { sha256sum "$1" 2>/dev/null | cut -d' ' -f1; }
elif command -v shasum    >/dev/null; then HASH() { shasum -a 256 "$1" 2>/dev/null | cut -d' ' -f1; }
else echo "no sha256sum or shasum found" >&2; exit 1; fi

TEXT_EXT="txt|text|html|htm|xml|epub|md|json|tei|rtf|docx|csv"
SCAN_EXT="pdf|djvu|jpg|jpeg|png|tif|tiff|gif|jp2"

printf 'relpath\tbytes\tsha256\n' > "$OUT/files.tsv"
printf 'work\tfiles\tbytes\tformats\tstate\n' > "$OUT/works.tsv"
: > "$OUT/empty.txt"

# Iterate immediate child directories of the root = the work folders.
while IFS= read -r -d '' dir; do
  slug="${dir#"$SRC"/}"
  n=0; total=0; exts=""
  while IFS= read -r -d '' f; do
    n=$((n+1))
    b=$(wc -c < "$f" 2>/dev/null | tr -d ' '); b="${b:-0}"
    total=$((total+b))
    printf '%s\t%s\t%s\n' "${f#"$SRC"/}" "$b" "$(HASH "$f")" >> "$OUT/files.tsv"
    base="${f##*/}"
    if [ "$base" != "${base%.*}" ]; then
      e=$(printf '%s' "${base##*.}" | tr '[:upper:]' '[:lower:]')
    else e="(none)"; fi
    exts="$exts $e"
  done < <(find "$dir" -type f -print0 2>/dev/null | sort -z)

  fmts=$(printf '%s' "$exts" | tr ' ' '\n' | grep -v '^$' | sort -u | paste -sd, -)
  if [ "$n" -eq 0 ]; then
    state="EMPTY"; printf '%s\n' "$slug" >> "$OUT/empty.txt"
  else
    has_t=0; has_s=0
    printf '%s' "$fmts" | tr ',' '\n' | grep -qE "^($TEXT_EXT)$" && has_t=1
    printf '%s' "$fmts" | tr ',' '\n' | grep -qE "^($SCAN_EXT)$" && has_s=1
    if   [ $has_t -eq 1 ] && [ $has_s -eq 1 ]; then state="TEXT+SCAN"
    elif [ $has_t -eq 1 ];                     then state="TEXT_ONLY"
    elif [ $has_s -eq 1 ];                     then state="NO_TEXT"
    else                                            state="UNKNOWN"; fi
  fi
  printf '%s\t%s\t%s\t%s\t%s\n' "$slug" "$n" "$total" "${fmts:--}" "$state" >> "$OUT/works.tsv"
done < <(find "$SRC" -mindepth 1 -maxdepth 1 -type d -print0 | sort -z)

# Files sitting loose at the root, outside any work folder.
loose=$(find "$SRC" -mindepth 1 -maxdepth 1 -type f | wc -l | tr -d ' ')

{
  echo "Collection audit — $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "Root: $SRC"
  echo
  w=$(( $(wc -l < "$OUT/works.tsv") - 1 ))
  f=$(( $(wc -l < "$OUT/files.tsv") - 1 ))
  echo "Work folders: $w"
  echo "Files:        $f"
  echo "Loose files at root (not in any work folder): $loose"
  awk -F'\t' 'NR>1{t+=$3} END{printf "Total bytes:  %d (%.2f GiB)\n", t, t/1073741824}' "$OUT/works.tsv"
  echo
  echo "State of each work folder:"
  awk -F'\t' 'NR>1{c[$5]++} END{for(s in c) printf "  %-12s %5d\n", s, c[s]}' "$OUT/works.tsv" | sort -k2 -nr
  echo
  echo "EMPTY work folders — nothing acquired, these are the actionable gaps:"
  if [ -s "$OUT/empty.txt" ]; then sed 's/^/  /' "$OUT/empty.txt"; else echo "  (none)"; fi
  echo
  echo "Format counts across all files:"
  awk -F'\t' 'NR>1{n=split($1,p,"/"); b=p[n]; if(b ~ /\./){n2=split(b,q,"."); e=tolower(q[n2])} else e="(none)"; c[e]++}
              END{for(e in c) printf "  %-10s %6d\n", e, c[e]}' "$OUT/files.tsv" | sort -k2 -nr
  echo
  echo "Files over 100 MiB (github.com rejects these outright):"
  if awk -F'\t' 'NR>1 && $2>104857600' "$OUT/files.tsv" | grep -q .; then
    awk -F'\t' 'NR>1 && $2>104857600 {printf "  %12d  %s\n", $2, $1}' "$OUT/files.tsv" | sort -nr
  else echo "  (none)"; fi
} > "$OUT/summary.txt"

echo "wrote $OUT/works.tsv, $OUT/empty.txt, $OUT/files.tsv, $OUT/summary.txt"
