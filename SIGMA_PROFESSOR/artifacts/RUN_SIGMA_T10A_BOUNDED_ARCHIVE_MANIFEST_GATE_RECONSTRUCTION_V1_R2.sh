#!/data/data/com.termux/files/usr/bin/bash
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"; ROOT="$(cd "$HERE/../.." && pwd)"
EXEC="$ROOT/.sigma_exec/T10A_BOUNDED_ARCHIVE_MANIFEST_GATE_RECONSTRUCTION_V1"; IN="$EXEC/input"; OUT="$EXEC/vm"; CASES="$EXEC/cases"
SRC="$HERE/SIGMA_T10A_BOUNDED_ARCHIVE_MANIFEST_GATE_RECONSTRUCTION_V1.sigma"; SIGMAC="$ROOT/native/sigmac"; VM="$ROOT/native/sigma-vm.v09_candidate"; BC="$EXEC/T10A_BOUNDED_ARCHIVE_MANIFEST_GATE_RECONSTRUCTION_V1.sigmab"
PROFILE_FILE="$HERE/PROFILES/T10A_RECONSTRUCTION_EXECUTION_ENVELOPE_V1.txt"; INPUT_SCHEMA_FILE="$HERE/SCHEMAS/T10A_RECONSTRUCTION_INPUT_SCHEMA_V1.txt"; OUTPUT_SCHEMA_FILE="$HERE/SCHEMAS/T10A_RECONSTRUCTION_OUTPUT_SCHEMA_V1.txt"; BUILD_RECIPE_FILE="$HERE/CONTRACTS/T10A_RECONSTRUCTION_BUILD_RECIPE_V1.txt"
SIGMAC_X=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_X=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
SRC_X=953df93174d314354542daae66842652e30e13d9b92950bc997d08fbb9e15ee4
PROFILE_X=3c4cd792a3822d471e63b169b87a965633c4b7ec10b79e145e5d574868f36aaa
INPUT_SCHEMA_X=5ab9065dd453bf6a93c6fb5a82d0e291d18133d589fd8b2e9d5869c50c9bde68
OUTPUT_SCHEMA_X=a1f2cb024998c7ded00ac48d2269cb5debb5e8b399164d8c15752f4d88a4c1cf
BUILD_RECIPE_X=39ad157a3d02a366bf2543c5bb62538a29b219b70a13eaca21ba2bbcd825a69d
MAX_E=8; MAX_ONE=1048576; MAX_ALL=4194304; PROFILE=T10A_RECONSTRUCTION_RESOURCE_PROFILE_V1
MAX_ID_BYTES=128; MAX_NUMERIC_BYTES=32; MAX_FLAG_BYTES=8; MAX_TOTAL_INPUT_BYTES=1024; MAX_INPUT_FILES=12
sha(){ sha256sum "$1"|awk '{print $1}'; }; rh(){ od -An -N8 -tx1 /dev/urandom|tr -d ' \n'; }; rm6(){ local v; v="$(od -An -N2 -tu2 /dev/urandom|tr -d ' ')"; echo $((v%60000)); }
fail(){ echo ADMISSION=FAIL; echo "RESULT=$1"; exit "${2:-1}"; }; nv(){ awk -v x="$1" 'BEGIN{if(x=="")print "__EMPTY";else printf "%.0f",x+0}'; }; val(){ awk -v k="$1" '$0==k{getline;print;exit}' "$2"; }
[ -f "$SIGMAC" ]&&[ -f "$VM" ]&&[ -f "$SRC" ]&&[ -f "$PROFILE_FILE" ]&&[ -f "$INPUT_SCHEMA_FILE" ]&&[ -f "$OUTPUT_SCHEMA_FILE" ]&&[ -f "$BUILD_RECIPE_FILE" ]||fail REQUIRED_FILE_MISSING 2
[ "$(sha "$SIGMAC")" = "$SIGMAC_X" ]||fail SIGMAC_HASH_MISMATCH 3; [ "$(sha "$VM")" = "$VM_X" ]||fail VM_HASH_MISMATCH 4; [ "$(sha "$SRC")" = "$SRC_X" ]||fail SOURCE_HASH_MISMATCH 5
[ "$(sha "$PROFILE_FILE")" = "$PROFILE_X" ]||fail RESOURCE_PROFILE_HASH_MISMATCH 51
[ "$(sha "$INPUT_SCHEMA_FILE")" = "$INPUT_SCHEMA_X" ]||fail INPUT_SCHEMA_HASH_MISMATCH 52
[ "$(sha "$OUTPUT_SCHEMA_FILE")" = "$OUTPUT_SCHEMA_X" ]||fail OUTPUT_SCHEMA_HASH_MISMATCH 53
[ "$(sha "$BUILD_RECIPE_FILE")" = "$BUILD_RECIPE_X" ]||fail BUILD_RECIPE_HASH_MISMATCH 54
while IFS= read -r fn; do grep -Fq "readv(BASE, \"$fn\")" "$SRC"||fail INPUT_SCHEMA_SOURCE_ALIGNMENT_FAIL 55; done < <(awk -F'[=|]' '/^FIELD=/{print $2}' "$INPUT_SCHEMA_FILE")
while IFS= read -r key; do grep -Fq "print(\"$key\")" "$SRC"||fail OUTPUT_SCHEMA_SOURCE_ALIGNMENT_FAIL 56; done < <(awk -F'[=|]' '/^KEY=/{print $2}' "$OUTPUT_SCHEMA_FILE")
grep -Fq '"T10A_RECONSTRUCTION_RESOURCE_PROFILE_V1"' "$SRC"||fail RESOURCE_PROFILE_SOURCE_ALIGNMENT_FAIL 57
grep -Fq 'IF (entry_count > 8)' "$SRC"||fail RESOURCE_BOUND_SOURCE_ALIGNMENT_FAIL 58
grep -Fq 'IF (max_entry_bytes > 1048576)' "$SRC"||fail RESOURCE_BOUND_SOURCE_ALIGNMENT_FAIL 59
grep -Fq 'IF (total_bytes > 4194304)' "$SRC"||fail RESOURCE_BOUND_SOURCE_ALIGNMENT_FAIL 60
ABI="$(grep -oE 'H\("[a-zA-Z0-9_]+' "$SRC"|sed 's/^H("//'|sort -u|paste -sd, -)"; [ "$ABI" = read_text,str_replace,to_float ]||fail HOST_ABI_LOCK_FAIL 6
FORB='summarize|translate|semantic_embedding|infer_intent|detect_theme|semantic_role|choose_evidence|choose_training_examples|decide_support|generate_search_query|select_best_interpretation'; FC="$(grep -Eic "$FORB" "$SRC"||true)"; [ "$FC" -eq 0 ]||fail SEMANTIC_ORACLE_TOKEN_FOUND 7
printf '%s\n' '=== T10A RECONSTRUCTION V1 R2 ===' "SIGMAC_SHA256=$(sha "$SIGMAC")" "VM_SHA256=$(sha "$VM")" "SOURCE_SHA256=$(sha "$SRC")" "RESOURCE_PROFILE_SHA256=$(sha "$PROFILE_FILE")" "INPUT_SCHEMA_SHA256=$(sha "$INPUT_SCHEMA_FILE")" "OUTPUT_SCHEMA_SHA256=$(sha "$OUTPUT_SCHEMA_FILE")" "BUILD_RECIPE_SHA256=$(sha "$BUILD_RECIPE_FILE")" 'CURRENT_TOOLCHAIN_IDENTITY_MATCH=YES' 'CONTRACT_IDENTITY_LOCK=PASS' 'SOURCE_CONTRACT_ALIGNMENT=PASS' 'HOST_MECHANICAL_ABI_STATIC_LOCK=PASS' "HOST_MECHANICAL_ABI=$ABI" "FORBIDDEN_SEMANTIC_ORACLE_TOKEN_COUNT_IN_SOURCE=$FC" 'HISTORICAL_T10A_BOUNDS_IMPORTED=NO'
rm -rf "$EXEC"; mkdir -p "$EXEC"; echo "DYNAMIC_INPUT_PRESENT_AT_COMPILE_TIME=$([ -e "$IN/case_id.txt" ]&&echo YES||echo NO)"; [ ! -e "$IN/case_id.txt" ]||fail INPUT_BEFORE_COMPILE 8
"$SIGMAC" "$SRC" "$BC" >"$EXEC/compile.stdout" 2>"$EXEC/compile.stderr"; CRC=$?; echo "COMPILE_RC=$CRC"; echo "COMPILE_STDOUT_SHA256=$(sha "$EXEC/compile.stdout")"; echo "COMPILE_STDERR_SHA256=$(sha "$EXEC/compile.stderr")"; cat "$EXEC/compile.stdout"; cat "$EXEC/compile.stderr"; [ "$CRC" -eq 0 ]&&[ -f "$BC" ]||fail COMPILE_FAILED 9
SF="$(sha "$SRC")"; BF="$(sha "$BC")"; echo "SOURCE_SHA256_AFTER_COMPILE=$SF"; echo "BYTECODE_SHA256_AFTER_COMPILE=$BF"; FCB="$(grep -aEic "$FORB" "$BC"||true)"; echo "FORBIDDEN_SEMANTIC_ORACLE_TOKEN_COUNT_IN_BYTECODE=$FCB"; [ "$FCB" -eq 0 ]||fail SEMANTIC_ORACLE_TOKEN_FOUND_IN_BYTECODE 61; mkdir -p "$IN" "$OUT" "$CASES"
N=0; P=0; F=0; NZ=0; SL=0; SENT=0; LEAK=0; CFA=''; CFB=''; RIA=''; RSA=''; RP=YES; PRE=0; PREP=0
base(){ C="C_$(rh)"; A="A_$(rh)"; M="M_$(rh)"; E=3; ONE=262144; ALL=524288; S=0; T=0; X=0; D=0; Q=0; U=0; }
writein(){ printf %s "$C">"$IN/case_id.txt"; printf %s "$A">"$IN/archive_id.txt"; printf %s "$M">"$IN/manifest_id.txt"; printf %s "$E">"$IN/entry_count.txt"; printf %s "$ONE">"$IN/max_entry_declared_bytes.txt"; printf %s "$ALL">"$IN/total_declared_bytes.txt"; printf %s "$S">"$IN/symlink_present.txt"; printf %s "$T">"$IN/traversal_present.txt"; printf %s "$X">"$IN/absolute_path_present.txt"; printf %s "$D">"$IN/duplicate_path_present.txt"; printf %s "$Q">"$IN/encrypted_entry_present.txt"; printf %s "$U">"$IN/unsupported_entry_type_present.txt"; }
fbytes(){ wc -c <"$1"|tr -d ' '; }
pre_gate(){
 local total=0 f n count
 count="$(find "$IN" -maxdepth 1 -type f | wc -l | tr -d ' ')"; [ "$count" -eq "$MAX_INPUT_FILES" ]||return 1
 for f in case_id.txt archive_id.txt manifest_id.txt; do n="$(fbytes "$IN/$f")"; [ "$n" -le "$MAX_ID_BYTES" ]||return 1; total=$((total+n)); done
 for f in entry_count.txt max_entry_declared_bytes.txt total_declared_bytes.txt; do n="$(fbytes "$IN/$f")"; [ "$n" -le "$MAX_NUMERIC_BYTES" ]||return 1; total=$((total+n)); done
 for f in symlink_present.txt traversal_present.txt absolute_path_present.txt duplicate_path_present.txt encrypted_entry_present.txt unsupported_entry_type_present.txt; do n="$(fbytes "$IN/$f")"; [ "$n" -le "$MAX_FLAG_BYTES" ]||return 1; total=$((total+n)); done
 [ "$total" -le "$MAX_TOTAL_INPUT_BYTES" ]||return 1
 return 0
}
pre_refusal(){ local L="$1"; PRE=$((PRE+1)); writein; if pre_gate; then echo "PRE_GATE_${PRE}_LABEL=$L"; echo "PRE_GATE_${PRE}_REFUSAL=NO"; return 1; else echo "PRE_GATE_${PRE}_LABEL=$L"; echo "PRE_GATE_${PRE}_REFUSAL=YES"; PREP=$((PREP+1)); return 0; fi; }
run(){
 local L="$1" I O ER RC SE IS OS core=1 ints=1 flags=1 iv=0 cons=0 res=0 haz=0 acc=0 st G
 N=$((N+1)); I="$(printf %03d "$N")"; O="$OUT/$I.out"; ER="$OUT/$I.err"; G="$CASES/$I.txt"
 printf 'C=%s\nA=%s\nM=%s\nE=%s\nONE=%s\nALL=%s\nS=%s\nT=%s\nX=%s\nD=%s\nQ=%s\nU=%s\n' "$C" "$A" "$M" "$E" "$ONE" "$ALL" "$S" "$T" "$X" "$D" "$Q" "$U">"$G"; writein; pre_gate||{ echo "CASE_${I}_PRE_EXECUTION_RESOURCE_GATE=UNEXPECTED_REFUSAL"; F=$((F+1)); return; }; echo "CASE_${I}_PRE_EXECUTION_RESOURCE_GATE=PASS"
 for z in "$C" "$A" "$M"; do [ "$z" = NONE ]&&continue; grep -aFq "$z" "$SRC" 2>/dev/null&&LEAK=$((LEAK+1)); grep -aFq "$z" "$BC" 2>/dev/null&&LEAK=$((LEAK+1)); done
 (cd "$ROOT"&&"$VM" "$BC" >"$O" 2>"$ER"); RC=$?; [ "$RC" -eq 0 ]||NZ=$((NZ+1)); grep -qi 'step limit' "$O" "$ER"&&SL=$((SL+1)); SE="$(grep -c '^T10A_BOUNDED_ARCHIVE_MANIFEST_GATE_RECONSTRUCTION_V1$' "$O"||true)"; [ "$SE" = 1 ]||SENT=$((SENT+1)); IS="$(sha "$G")"; OS="$(sha "$O")"
 echo "CASE_${I}_LABEL=$L"; echo "CASE_${I}_INPUT_SHA256=$IS"; echo "CASE_${I}_VM_RC=$RC"; echo "CASE_${I}_VM_STDOUT_SHA256=$OS"; echo "CASE_${I}_VM_STDERR_SHA256=$(sha "$ER")"; echo "--- RAW SIGMA VM CASE $I STDOUT ---"; cat "$O"; echo "--- RAW SIGMA VM CASE $I STDERR ---"; cat "$ER"; echo "CASE_${I}_POST_VM_TEST_ORACLE_STARTED=YES"
 [ -n "$C" ]&&[ "$C" != NONE ]&&[ -n "$A" ]&&[ "$A" != NONE ]&&[ -n "$M" ]&&[ "$M" != NONE ]||core=0
 [[ "$E" =~ ^[0-9]+$ ]]&&[[ "$ONE" =~ ^[0-9]+$ ]]&&[[ "$ALL" =~ ^[0-9]+$ ]]||ints=0
 for z in "$S" "$T" "$X" "$D" "$Q" "$U"; do { [ "$z" = 0 ]||[ "$z" = 1 ]; }||flags=0; done
 [ "$core" -eq 1 ]&&[ "$ints" -eq 1 ]&&[ "$flags" -eq 1 ]&&iv=1
 if [ "$ints" -eq 1 ]; then if [ "$E" -eq 0 ]; then [ "$ONE" -eq 0 ]&&[ "$ALL" -eq 0 ]&&cons=1; elif [ "$ONE" -le "$ALL" ]; then cons=1; fi; fi
 [ "$iv" -eq 1 ]&&[ "$E" -le "$MAX_E" ]&&[ "$ONE" -le "$MAX_ONE" ]&&[ "$ALL" -le "$MAX_ALL" ]&&res=1
 [ "$flags" -eq 1 ]&&{ [ "$S" = 1 ]||[ "$T" = 1 ]||[ "$X" = 1 ]||[ "$D" = 1 ]||[ "$Q" = 1 ]||[ "$U" = 1 ]; }&&haz=1
 [ "$iv" -eq 1 ]&&[ "$cons" -eq 1 ]&&[ "$res" -eq 1 ]&&[ "$haz" -eq 0 ]&&acc=1
 if [ "$iv" -eq 0 ];then st=INPUT_BINDING_INVALID;elif [ "$cons" -eq 0 ];then st=MANIFEST_NUMERIC_INCONSISTENT;elif [ "$res" -eq 0 ];then st=RESOURCE_BOUND_VIOLATION;elif [ "$haz" -eq 1 ];then st=ARCHIVE_HAZARD_OBSERVED;else st=BOUNDED_MANIFEST_ACCEPTED;fi
 AL=YES; [ "$RC" -eq 0 ]&&[ "$SE" = 1 ]||AL=NO; [ "$(val INPUT_CASE_ID "$O")" = "$C" ]||AL=NO; [ "$(val ARCHIVE_ID "$O")" = "$A" ]||AL=NO; [ "$(val MANIFEST_ID "$O")" = "$M" ]||AL=NO; [ "$(nv "$(val INPUT_BINDING_VALID "$O")")" = "$iv" ]||AL=NO; [ "$(nv "$(val MANIFEST_NUMERIC_CONSISTENT "$O")")" = "$cons" ]||AL=NO; [ "$(nv "$(val RESOURCE_WITHIN_BOUNDS "$O")")" = "$res" ]||AL=NO; [ "$(nv "$(val HAZARD_PRESENT "$O")")" = "$haz" ]||AL=NO; [ "$(nv "$(val ARCHIVE_MANIFEST_GATE_ACCEPTED "$O")")" = "$acc" ]||AL=NO; [ "$(val STATUS "$O")" = "$st" ]||AL=NO; [ "$(val RESOURCE_PROFILE_ID "$O")" = "$PROFILE" ]||AL=NO; [ "$(val HISTORICAL_T10A_BOUNDS_IMPORTED "$O")" = NO ]||AL=NO; [ "$(val HOST_MECHANICAL_ABI "$O")" = read_text,to_float,str_replace ]||AL=NO; [ "$(val RAW_ARCHIVE_FORMAT_PARSING "$O")" = NOT_PROVEN ]||AL=NO; [ "$(val ARCHIVE_HAZARD_DETECTION_FROM_RAW_BYTES "$O")" = NOT_PROVEN ]||AL=NO; [ "$(val ACTUAL_ARCHIVE_EXTRACTION "$O")" = NOT_EXECUTED ]||AL=NO; [ "$(val DOCUMENT_CONTENT_READING "$O")" = NOT_PROVEN ]||AL=NO; [ "$(val DOCUMENT_UNDERSTANDING "$O")" = NOT_PROVEN ]||AL=NO; [ "$(val SEMANTIC_UNDERSTANDING "$O")" = NOT_PROVEN ]||AL=NO; [ "$(val PRODUCTION_STATE_MUTATED "$O")" = NO ]||AL=NO; [ "$(val T10B_UNLOCKED_BY_THIS_INVOCATION "$O")" = NO ]||AL=NO
 [ "$AL" = YES ]&&P=$((P+1))||F=$((F+1)); echo "CASE_${I}_POST_VM_ALIGNMENT=$AL"; [ "$L" = CFA ]&&CFA="$acc"; [ "$L" = CFB ]&&CFB="$acc"; [ "$L" = REPLAY_A ]&&{ RIA="$IS"; RSA="$OS"; }; if [ "$L" = REPLAY_B ];then if [ "$IS" != "$RIA" ]||[ "$OS" != "$RSA" ];then RP=NO; F=$((F+1));fi;fi
}
base; E="$(printf '9%.0s' $(seq 1 64))"; pre_refusal OVERSIZE_NUMERIC_TOKEN||fail PRE_EXECUTION_GATE_FAILED 62
base; C="$(printf 'C%.0s' $(seq 1 256))"; pre_refusal OVERSIZE_ID_TOKEN||fail PRE_EXECUTION_GATE_FAILED 63
base; S="$(printf '1%.0s' $(seq 1 32))"; pre_refusal OVERSIZE_FLAG_TOKEN||fail PRE_EXECUTION_GATE_FAILED 64
base; E=1; ONE=1; ALL=1; run MIN
base; E=8; ONE=1048576; ALL=4194304; run EXACT_BOUNDS
base; E=0; ONE=0; ALL=0; run ZERO
base; E=9; run ENTRIES_OVER
base; ONE=1048577; run ENTRY_BYTES_OVER
base; ALL=4194305; run TOTAL_OVER
base; S=1; run SYMLINK
base; T=1; run TRAVERSAL
base; X=1; run ABSOLUTE
base; D=1; run DUPLICATE
base; Q=1; run ENCRYPTED
base; U=1; run UNSUPPORTED
base; S=1; T=1; Q=1; run MULTI_HAZARD
base; S=X; run BAD_FLAG
base; E=3x; run BAD_INTEGER
base; M=NONE; run MISSING_MANIFEST
base; ONE=600000; ALL=500000; run INCONSISTENT_MAX
base; E=0; ONE=0; ALL=1; run INCONSISTENT_ZERO
base; ALL=4194304; run CFA; ALL=4194305; run CFB
for i in $(seq 1 16);do base; E=$((RANDOM%9)); ONE=$((1+$(rm6))); ALL=$((ONE+$(rm6))); if [ $((i%2)) -eq 1 ];then m=$((RANDOM%4)); [ "$m" -eq 0 ]&&E=9; [ "$m" -eq 1 ]&&ONE=1048577; [ "$m" -eq 2 ]&&ALL=4194305; [ "$m" -eq 3 ]&&T=1;fi; run "RANDOM_$i";done
base; C="R_$(rh)"; A="RA_$(rh)"; M="RM_$(rh)"; E=7; ONE=777777; ALL=3333333; run REPLAY_A; run REPLAY_B
SA="$(sha "$SRC")"; BA="$(sha "$BC")"; CF=NO; [ "$CFA" = 1 ]&&[ "$CFB" = 0 ]&&CF=YES
printf '%s\n' "RESOURCE_PROFILE_SHA256=$PROFILE_X" "INPUT_SCHEMA_SHA256=$INPUT_SCHEMA_X" "OUTPUT_SCHEMA_SHA256=$OUTPUT_SCHEMA_X" "BUILD_RECIPE_SHA256=$BUILD_RECIPE_X" "PRE_VM_RESOURCE_REFUSAL_CASES=$PRE" "PRE_VM_RESOURCE_REFUSAL_PASS_COUNT=$PREP" "PRE_EXECUTION_INPUT_BYTE_BOUND=$([ "$PRE" -eq 3 ]&&[ "$PREP" -eq 3 ]&&echo PASS||echo FAIL)" "SOURCE_SHA256_AFTER_ALL_RUNS=$SA" "BYTECODE_SHA256_AFTER_ALL_RUNS=$BA" "SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=$([ "$SA" = "$SF" ]&&echo YES||echo NO)" "BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=$([ "$BA" = "$BF" ]&&echo YES||echo NO)" "UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=$LEAK" "TOTAL_VM_INVOCATIONS=$N" "POST_VM_ALIGNMENT_PASS_COUNT=$P" "POST_VM_ALIGNMENT_FAIL_COUNT=$F" "VM_NONZERO_COUNT=$NZ" "STEP_LIMIT_HIT_COUNT=$SL" "SENTINEL_FAIL_COUNT=$SENT" "COUNTERFACTUAL_RESOURCE_BOUND_DECISION=$CF" "REPLAY_IDENTICAL_INPUT_DECISION=$RP" 'DYNAMIC_INPUT=YES' 'PERSISTENT_STATE=NA' 'HOST_LEARNING=NO' 'HOST_SEMANTIC_SUBSTITUTION=NO' 'HOST_POST_VM_TEST_ORACLE_ONLY=YES' 'PYTHON_USED=NO' 'RAW_ARCHIVE_FORMAT_PARSING=NOT_PROVEN' 'ARCHIVE_HAZARD_DETECTION_FROM_RAW_BYTES=NOT_PROVEN' 'ACTUAL_ARCHIVE_EXTRACTION=NOT_EXECUTED' 'DOCUMENT_CONTENT_READING=NOT_PROVEN' 'DOCUMENT_UNDERSTANDING=NOT_PROVEN' 'SEMANTIC_UNDERSTANDING=NOT_PROVEN' 'T10B_UNLOCKED=NO' 'PRODUCTION_STATE_MUTATED=NO'
if [ "$PRE" -eq 3 ]&&[ "$PREP" -eq 3 ]&&[ "$N" -eq 38 ]&&[ "$P" -eq 38 ]&&[ "$F" -eq 0 ]&&[ "$NZ" -eq 0 ]&&[ "$SL" -eq 0 ]&&[ "$SENT" -eq 0 ]&&[ "$LEAK" -eq 0 ]&&[ "$CF" = YES ]&&[ "$RP" = YES ]&&[ "$SA" = "$SF" ]&&[ "$BA" = "$BF" ];then echo T10A_NATIVE_BOUNDED_ARCHIVE_MANIFEST_GATE=PASS_IN_EXACT_TESTED_RECONSTRUCTION_SCOPE; echo T10A_EXECUTION_ENVELOPE=PASS_IN_EXACT_TESTED_R2_SCOPE; echo ADMISSION=PASS; echo RESULT=PASS_IN_EXACT_TESTED_RECONSTRUCTION_R2_SCOPE;else echo ADMISSION=FAIL; echo RESULT=FAIL_IN_TESTED_RECONSTRUCTION_R2_SCOPE; exit 1;fi
