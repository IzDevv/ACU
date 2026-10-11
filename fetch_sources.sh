#!/usr/bin/env bash
# Fetch verified Arthurian primary texts from archive.org into work folders
# matching the ACU collection layout:  <work_slug>/<files>
#
# Usage:  ./fetch_sources.sh [target_dir]        (default: current directory)
#
# Each item downloads the PDF (page images) and the _djvu.txt (text layer),
# skips anything already complete, and is safe to re-run.
# Needs: bash, curl, python3.

set -uo pipefail
DEST="${1:-.}"
mkdir -p "$DEST"

# slug<TAB>archive.org identifier<TAB>ACU ids covered
ITEMS=$(cat <<'EOF'
mabinogion_red_book_rhys_evans_1887	textofmabinogion00rhysiala	ACU-0071..0077 Welsh originals
cambro_british_saints_rees_1853	livesofthecambro00reesuoft	ACU-0007,0008,0009,0014 Latin vitae
percy_folio_v1_hales_furnivall_1867	bishoppercysfoli01percuoft	ACU-0274,0275,0277,(0279)
marie_de_france_lais_warnke_1925	mariedefrancelaiswarnketroed	ACU-0172,0173,0174,0179
chronica_minora_mommsen_mgh_aa13	chronicaminorasa00momm	ACU-0001,0003 Latin critical
gildas_de_excidio_williams_1899	gildaedeexcidiob00gilduoft	ACU-0001 Latin+English
sggk_morris_eets_gollancz_1912	SirGawayneAndTheGreenKnight1915	ACU-0259 Middle English
sggk_weston_prose_1898	SirGawainAndTheGreenKnightWeston1898	ACU-0388 exact title match
scalacronica_stevenson_1836	scalacronica00mait	ACU-0129 Anglo-Norman
prose_brut_brie_eets_1906	brutorchronicles00brieuoft	ACU-0249 Middle English prose
tristan_leonis_bonilla_1912	librodelesforado00boni	ACU-0511 or 0515 Spanish
jaufre_brunel_1943_t2	JaufreTomeII	ACU-0213 Occitan (tome II only)
saint_graal_hucher_1875_v1	lesaintgraaloule01huchuoft	ACU-0146 (Perceval text is in vol 2)
black_book_carmarthen_evans_1906	blackbookofcarma00evanuoft	ACU-0055 etc Welsh
four_ancient_books_wales_skene_1868	fourancientbooks01skenuoft	ACU-0064,0065 Welsh
lai_guingamor_tydorel	lelaideguingamor00mari	ACU-0179 Old French
meon_nouveau_recueil_fabliaux_1823_v1	NouveauRecueilFabliauxVol1A1823	ACU-0190 (contents unverified)
fastnachtspiele_keller_1853	bub_gb_XCTIrJ7jeVUC	ACU-0423 Early New High German
layamon_brut_madden_1847_v1	layamonsbrutorc00maddgoog	ACU-0240
layamon_brut_madden_1847_v3	layamonsbrutorch03layauoft	ACU-0240
holinshed_chronicles_ellis_1807_v1	holinshedschroni01holi	ACU-0305
portugaliae_mon_hist_scriptores_v1	portugaliaemonumentahistoricascrv1	ACU-0519 (unverified)
demanda_sancto_grial_spanish_print	primeroysegundolibrodegria	Spanish Demanda (distinct from ACU-0506)
EOF
)

ok=0; fail=0
while IFS=$'\t' read -r slug ident note; do
  [ -z "${slug:-}" ] && continue
  dir="$DEST/$slug"; mkdir -p "$dir"
  echo "== $slug  [$note]"
  meta=$(curl -sSL -m 120 "https://archive.org/metadata/$ident") || { echo "   metadata failed"; fail=$((fail+1)); continue; }
  # pick the PDF and the text layer
  names=$(printf '%s' "$meta" | python3 -I -c '
import json,sys
d=json.load(sys.stdin); out=[]
for f in d.get("files",[]):
    if f.get("format") in ("Text PDF","Image Container PDF") and not any(n.endswith(".pdf") for n in out):
        out.append(f["name"])
    if f.get("format")=="DjVuTXT":
        out.append(f["name"])
print("\n".join(out))')
  [ -z "$names" ] && { echo "   no pdf/text found"; fail=$((fail+1)); continue; }
  while IFS= read -r n; do
    [ -z "$n" ] && continue
    if [ -s "$dir/$n" ]; then echo "   have $n"; continue; fi
    echo "   get  $n"
    curl -sSL -m 1800 --retry 3 --retry-delay 2 -C - \
      -o "$dir/$n" "https://archive.org/download/$ident/$n" \
      && ok=$((ok+1)) || { echo "   FAILED $n"; fail=$((fail+1)); }
  done <<< "$names"
  printf '%s\t%s\n' "$ident" "$note" > "$dir/_source.txt"
done <<< "$ITEMS"

echo
echo "files fetched: $ok   failures: $fail"
echo "target: $DEST"
