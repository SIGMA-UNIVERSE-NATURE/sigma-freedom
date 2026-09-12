#!/data/data/com.termux/files/usr/bin/bash
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/../.." && pwd)"
EXEC="$ROOT/.sigma_exec/T10A_BOUNDED_ARCHIVE_MANIFEST_GATE_RECONSTRUCTION_V1_R3"
IN="$EXEC/input"; OUT="$EXEC/vm"; CASES="$EXEC/cases"
SRC="$HERE/SIGMA_T10A_BOUNDED_ARCHIVE_MANIFEST_GATE_RECONSTRUCTION_V1.sigma"
SIGMAC="$ROOT/native/sigmac"; VM="$ROOT/native/sigma-vm.v09_candidate"
BC="$EXEC/T10A_BOUNDED_ARCHIVE_MANIFEST_GATE_RECONSTRUCTION_V1.sigmab"
PROFILE_FILE="$HERE/PROFILES/T10A_RECONSTRUCTION_EXECUTION_ENVELOPE_V2.txt"
INPUT_SCHEMA_FILE="$HERE/SCHEMAS/T10A_RECONSTRUCTION_INPUT_SCHEMA_V2.txt"
OUTPUT_SCHEMA_FILE="$HERE/SCHEMAS/T10A_RECONSTRUCTION_OUTPUT_SCHEMA_V2.txt"
ABI_FILE="$HERE/CONTRACTS/T10A_RECONSTRUCTION_HOST_ABI_V1.txt"
BUILD_RECIPE_FILE="$HERE/CONTRACTS/T10A_RECONSTRUCTION_BUILD_RECIPE_V2.txt"
SIGMAC_X=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_X=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
SRC_X=953df93174d314354542daae66842652e30e13d9b92950bc997d08fbb9e15ee4
PROFILE_X=e31e59fcf2f2348cea8d071eb7fb4758c55f3c509321e2f8c8dbffbeb1381376
INPUT_SCHEMA_X=2831c11c6a49e179adf85e90ddf2201edddf183642655852768b156ab06e6dc9
OUTPUT_SCHEMA_X=94cdcfa86eb5ec40434523a1ef005efde5295fc5462337ea72410bfe6babafdc
ABI_X=b1f9229a23a366ea2ef8339725bf66b7013c8924d3dac629b610d74d509abf97
BUILD_RECIPE_X=06819e07c5280eba57b0681264df55697d3eb30feaa7414705a8789cc3b111a6
MAX_E=8; MAX_ONE=1048576; MAX_ALL=4194304; PROFILE=T10A_RECONSTRUCTION_RESOURCE_PROFILE_V1
MAX_ID_BYTES=128; MAX_NUMERIC_BYTES=32; MAX_FLAG_BYTES=8; MAX_TOTAL_INPUT_BYTES=1024; MAX_INPUT_FILES=12
SENTINEL=T10A_BOUNDED_ARCHIVE_MANIFEST_GATE_RECONSTRUCTION_V1
FORB_API='understand|summarize|translate|semantic_embedding|is_paraphrase|find_synonym|infer_intent|infer_motive|detect_theme|detect_value|semantic_role|coreference_resolve|choose_evidence|choose_important_memory|choose_training_examples|decide_support|decide_contradiction|decide_truth|generate_search_query|generate_answer|select_best_interpretation|parse_english_sentence|subject_object_detector'
sha(){ sha256sum "$1" | awk '{print $1}'; }
rh(){ od -An -N8 -tx1 /dev/urandom | tr -d ' \n'; }
rm6(){ local v; v="$(od -An -N2 -tu2 /dev/urandom | tr -d ' ')"; echo $((v%60000)); }
fail(){ echo ADMISSION=FAIL; echo "RESULT=$1"; exit "${2:-1}"; }
nv(){ awk -v x="$1" 'BEGIN{if(x=="")print "__EMPTY";else printf "%.0f",x+0}'; }
val(){ awk -v k="$1" 'NR==1{next}{key=$0;if(getline v){if(key==k){print v;exit}}}' "$2"; }
fbytes(){ wc -c <"$1" | tr -d ' '; }
safe_id_file(){
    local f="$1" n safe
    n="$(fbytes "$f")"
    [ "$n" -ge 1 ] && [ "$n" -le "$MAX_ID_BYTES" ] || return 1
    safe="$(LC_ALL=C tr -cd 'A-Za-z0-9._:-' <"$f" | wc -c | tr -d ' ')"
    [ "$safe" -eq "$n" ]
}
source_forbidden_count(){
    local call_re
    call_re="(^|[^A-Za-z0-9_])(${FORB_API})[[:space:]]*\\(|host[[:space:]]*\\([[:space:]]*\\\"(${FORB_API})\\\"|DEF[[:space:]]+(${FORB_API})[[:space:]]*\\("
    grep -Eic "$call_re" "$SRC" 2>/dev/null || true
}
bytecode_forbidden_count(){
    grep -aEic "(^|[^A-Za-z0-9_])(${FORB_API})([^A-Za-z0-9_]|$)" "$BC" 2>/dev/null || true
}

[ -f "$SIGMAC" ] && [ -f "$VM" ] && [ -f "$SRC" ] && [ -f "$PROFILE_FILE" ] && [ -f "$INPUT_SCHEMA_FILE" ] && [ -f "$OUTPUT_SCHEMA_FILE" ] && [ -f "$ABI_FILE" ] && [ -f "$BUILD_RECIPE_FILE" ] || fail REQUIRED_FILE_MISSING 2
[ "$(sha "$SIGMAC")" = "$SIGMAC_X" ] || fail SIGMAC_HASH_MISMATCH 3
[ "$(sha "$VM")" = "$VM_X" ] || fail VM_HASH_MISMATCH 4
[ "$(sha "$SRC")" = "$SRC_X" ] || fail SOURCE_HASH_MISMATCH 5
[ "$(sha "$PROFILE_FILE")" = "$PROFILE_X" ] || fail RESOURCE_PROFILE_HASH_MISMATCH 51
[ "$(sha "$INPUT_SCHEMA_FILE")" = "$INPUT_SCHEMA_X" ] || fail INPUT_SCHEMA_HASH_MISMATCH 52
[ "$(sha "$OUTPUT_SCHEMA_FILE")" = "$OUTPUT_SCHEMA_X" ] || fail OUTPUT_SCHEMA_HASH_MISMATCH 53
[ "$(sha "$ABI_FILE")" = "$ABI_X" ] || fail ABI_HASH_MISMATCH 54
[ "$(sha "$BUILD_RECIPE_FILE")" = "$BUILD_RECIPE_X" ] || fail BUILD_RECIPE_HASH_MISMATCH 55

while IFS= read -r fn; do
    grep -Fq "readv(BASE, \"$fn\")" "$SRC" || fail INPUT_SCHEMA_SOURCE_ALIGNMENT_FAIL 56
done < <(awk -F'[=|]' '/^FIELD=/{print $2}' "$INPUT_SCHEMA_FILE")
EXPECTED_KEYS="$EXEC.output.keys.expected"
awk -F'[=|]' '/^KEY=/{print $2}' "$OUTPUT_SCHEMA_FILE" >"$EXPECTED_KEYS"
KEY_COUNT="$(awk 'END{print NR+0}' "$EXPECTED_KEYS")"
[ "$KEY_COUNT" -gt 0 ] || fail OUTPUT_SCHEMA_EMPTY 57
prev=0
while IFS= read -r key; do
    lines="$(grep -nF "print(\"$key\")" "$SRC" | cut -d: -f1)"
    count="$(printf '%s\n' "$lines" | awk 'NF{n++}END{print n+0}')"
    [ "$count" -eq 1 ] || fail OUTPUT_SCHEMA_SOURCE_KEY_COUNT_FAIL 58
    ln="$(printf '%s\n' "$lines" | head -n1)"
    [ "$ln" -gt "$prev" ] || fail OUTPUT_SCHEMA_SOURCE_ORDER_FAIL 59
    prev="$ln"
done <"$EXPECTED_KEYS"
grep -Fq '"T10A_RECONSTRUCTION_RESOURCE_PROFILE_V1"' "$SRC" || fail RESOURCE_PROFILE_SOURCE_ALIGNMENT_FAIL 60
grep -Fq 'IF (entry_count > 8)' "$SRC" || fail RESOURCE_BOUND_SOURCE_ALIGNMENT_FAIL 61
grep -Fq 'IF (max_entry_bytes > 1048576)' "$SRC" || fail RESOURCE_BOUND_SOURCE_ALIGNMENT_FAIL 62
grep -Fq 'IF (total_bytes > 4194304)' "$SRC" || fail RESOURCE_BOUND_SOURCE_ALIGNMENT_FAIL 63
ABI="$(grep -oE 'H\("[a-zA-Z0-9_]+' "$SRC" | sed 's/^H("//' | sort -u | paste -sd, -)"
[ "$ABI" = read_text,str_replace,to_float ] || fail HOST_ABI_LOCK_FAIL 64
grep -Fq 'ABI_VERSION=T10A_RECONSTRUCTION_HOST_ABI_V1' "$ABI_FILE" || fail ABI_VERSION_LOCK_FAIL 65
FC="$(source_forbidden_count)"
[ "$FC" -eq 0 ] || fail SEMANTIC_ORACLE_API_FOUND_IN_SOURCE 66

printf '%s\n' \
'=== T10A RECONSTRUCTION V1 R3 ===' \
"SIGMAC_SHA256=$(sha "$SIGMAC")" \
"VM_SHA256=$(sha "$VM")" \
"SOURCE_SHA256=$(sha "$SRC")" \
"RESOURCE_PROFILE_SHA256=$(sha "$PROFILE_FILE")" \
"INPUT_SCHEMA_SHA256=$(sha "$INPUT_SCHEMA_FILE")" \
"OUTPUT_SCHEMA_SHA256=$(sha "$OUTPUT_SCHEMA_FILE")" \
"ABI_SHA256=$(sha "$ABI_FILE")" \
"BUILD_RECIPE_SHA256=$(sha "$BUILD_RECIPE_FILE")" \
'CURRENT_TOOLCHAIN_IDENTITY_MATCH=YES' \
'CONTRACT_IDENTITY_LOCK=PASS' \
'SOURCE_CONTRACT_ALIGNMENT=PASS' \
'OUTPUT_SCHEMA_SOURCE_ORDER=PASS' \
'HOST_MECHANICAL_ABI_STATIC_LOCK=PASS' \
"HOST_MECHANICAL_ABI=$ABI" \
"FORBIDDEN_SEMANTIC_ORACLE_API_COUNT_IN_SOURCE=$FC" \
'HISTORICAL_T10A_BOUNDS_IMPORTED=NO'

rm -rf "$EXEC"
mkdir -p "$EXEC"
echo "DYNAMIC_INPUT_PRESENT_AT_COMPILE_TIME=$([ -e "$IN/case_id.txt" ] && echo YES || echo NO)"
[ ! -e "$IN/case_id.txt" ] || fail INPUT_BEFORE_COMPILE 67
"$SIGMAC" "$SRC" "$BC" >"$EXEC/compile.stdout" 2>"$EXEC/compile.stderr"
CRC=$?
echo "COMPILE_RC=$CRC"
echo "COMPILE_STDOUT_SHA256=$(sha "$EXEC/compile.stdout")"
echo "COMPILE_STDERR_SHA256=$(sha "$EXEC/compile.stderr")"
cat "$EXEC/compile.stdout"; cat "$EXEC/compile.stderr"
[ "$CRC" -eq 0 ] && [ -f "$BC" ] || fail COMPILE_FAILED 68
SF="$(sha "$SRC")"; BF="$(sha "$BC")"
echo "SOURCE_SHA256_AFTER_COMPILE=$SF"
echo "BYTECODE_SHA256_AFTER_COMPILE=$BF"
FCB="$(bytecode_forbidden_count)"
echo "FORBIDDEN_SEMANTIC_ORACLE_API_COUNT_IN_BYTECODE=$FCB"
[ "$FCB" -eq 0 ] || fail SEMANTIC_ORACLE_API_FOUND_IN_BYTECODE 69
mkdir -p "$IN" "$OUT" "$CASES"

N=0; P=0; F=0; NZ=0; SL=0; SCHEMA_FAIL=0; LEAK=0; CFA=''; CFB=''; RIA=''; RSA=''; RP=YES; PRE=0; PREP=0
base(){ C="C_$(rh)"; A="A_$(rh)"; M="M_$(rh)"; E=3; ONE=262144; ALL=524288; S=0; T=0; X=0; D=0; Q=0; U=0; }
writein(){
    printf %s "$C">"$IN/case_id.txt"; printf %s "$A">"$IN/archive_id.txt"; printf %s "$M">"$IN/manifest_id.txt"
    printf %s "$E">"$IN/entry_count.txt"; printf %s "$ONE">"$IN/max_entry_declared_bytes.txt"; printf %s "$ALL">"$IN/total_declared_bytes.txt"
    printf %s "$S">"$IN/symlink_present.txt"; printf %s "$T">"$IN/traversal_present.txt"; printf %s "$X">"$IN/absolute_path_present.txt"
    printf %s "$D">"$IN/duplicate_path_present.txt"; printf %s "$Q">"$IN/encrypted_entry_present.txt"; printf %s "$U">"$IN/unsupported_entry_type_present.txt"
}
pre_gate(){
    local total=0 f n count
    count="$(find "$IN" -maxdepth 1 -type f | wc -l | tr -d ' ')"
    [ "$count" -eq "$MAX_INPUT_FILES" ] || return 1
    for f in case_id.txt archive_id.txt manifest_id.txt; do
        safe_id_file "$IN/$f" || return 1
        n="$(fbytes "$IN/$f")"; total=$((total+n))
    done
    for f in entry_count.txt max_entry_declared_bytes.txt total_declared_bytes.txt; do
        n="$(fbytes "$IN/$f")"; [ "$n" -ge 1 ] && [ "$n" -le "$MAX_NUMERIC_BYTES" ] || return 1; total=$((total+n))
    done
    for f in symlink_present.txt traversal_present.txt absolute_path_present.txt duplicate_path_present.txt encrypted_entry_present.txt unsupported_entry_type_present.txt; do
        n="$(fbytes "$IN/$f")"; [ "$n" -ge 1 ] && [ "$n" -le "$MAX_FLAG_BYTES" ] || return 1; total=$((total+n))
    done
    [ "$total" -le "$MAX_TOTAL_INPUT_BYTES" ] || return 1
    return 0
}
record_pre_refusal(){
    local L="$1"
    PRE=$((PRE+1))
    if pre_gate; then
        echo "PRE_GATE_${PRE}_LABEL=$L"; echo "PRE_GATE_${PRE}_REFUSAL=NO"; return 1
    fi
    echo "PRE_GATE_${PRE}_LABEL=$L"; echo "PRE_GATE_${PRE}_REFUSAL=YES"; PREP=$((PREP+1)); return 0
}
pre_refusal(){ local L="$1"; writein; record_pre_refusal "$L"; }
schema_runtime_ok(){
    local o="$1" actual="$2" lines expected_lines
    [ "$(head -n1 "$o")" = "$SENTINEL" ] || return 1
    tail -n +2 "$o" | awk 'NR%2==1{print}' >"$actual"
    cmp -s "$EXPECTED_KEYS" "$actual" || return 1
    lines="$(awk 'END{print NR+0}' "$o")"; expected_lines=$((1 + 2 * KEY_COUNT))
    [ "$lines" -eq "$expected_lines" ] || return 1
    return 0
}
run(){
    local L="$1" I O ER RC IS OS SCHEMA_OK=0 core=1 ints=1 flags=1 iv=0 cons=0 res=0 haz=0 acc=0 st G ACTUAL_KEYS en=0 eone=0 eall=0 AL
    N=$((N+1)); I="$(printf %03d "$N")"; O="$OUT/$I.out"; ER="$OUT/$I.err"; G="$CASES/$I.txt"; ACTUAL_KEYS="$OUT/$I.keys"
    printf 'C=%s\nA=%s\nM=%s\nE=%s\nONE=%s\nALL=%s\nS=%s\nT=%s\nX=%s\nD=%s\nQ=%s\nU=%s\n' "$C" "$A" "$M" "$E" "$ONE" "$ALL" "$S" "$T" "$X" "$D" "$Q" "$U">"$G"
    writein
    if ! pre_gate; then echo "CASE_${I}_PRE_EXECUTION_RESOURCE_GATE=UNEXPECTED_REFUSAL"; F=$((F+1)); return; fi
    echo "CASE_${I}_PRE_EXECUTION_RESOURCE_GATE=PASS"
    for z in "$C" "$A" "$M"; do
        [ "$z" = NONE ] && continue
        grep -aFq "$z" "$SRC" 2>/dev/null && LEAK=$((LEAK+1))
        grep -aFq "$z" "$BC" 2>/dev/null && LEAK=$((LEAK+1))
    done
    (cd "$ROOT" && "$VM" "$BC" >"$O" 2>"$ER"); RC=$?
    [ "$RC" -eq 0 ] || NZ=$((NZ+1))
    grep -qi 'step limit' "$O" "$ER" && SL=$((SL+1))
    IS="$(sha "$G")"; OS="$(sha "$O")"
    echo "CASE_${I}_LABEL=$L"; echo "CASE_${I}_INPUT_SHA256=$IS"; echo "CASE_${I}_VM_RC=$RC"; echo "CASE_${I}_VM_STDOUT_SHA256=$OS"; echo "CASE_${I}_VM_STDERR_SHA256=$(sha "$ER")"
    echo "--- RAW SIGMA VM CASE $I STDOUT ---"; cat "$O"; echo "--- RAW SIGMA VM CASE $I STDERR ---"; cat "$ER"; echo "CASE_${I}_POST_VM_TEST_ORACLE_STARTED=YES"
    schema_runtime_ok "$O" "$ACTUAL_KEYS" && SCHEMA_OK=1 || { SCHEMA_FAIL=$((SCHEMA_FAIL+1)); SCHEMA_OK=0; }
    echo "CASE_${I}_OUTPUT_SCHEMA_ALIGNMENT=$([ "$SCHEMA_OK" -eq 1 ] && echo YES || echo NO)"
    [ -n "$C" ] && [ "$C" != NONE ] && [ -n "$A" ] && [ "$A" != NONE ] && [ -n "$M" ] && [ "$M" != NONE ] || core=0
    [[ "$E" =~ ^[0-9]+$ ]] && [[ "$ONE" =~ ^[0-9]+$ ]] && [[ "$ALL" =~ ^[0-9]+$ ]] || ints=0
    for z in "$S" "$T" "$X" "$D" "$Q" "$U"; do { [ "$z" = 0 ] || [ "$z" = 1 ]; } || flags=0; done
    [ "$core" -eq 1 ] && [ "$ints" -eq 1 ] && [ "$flags" -eq 1 ] && iv=1
    if [ "$ints" -eq 1 ]; then
        en="$(nv "$E")"; eone="$(nv "$ONE")"; eall="$(nv "$ALL")"
        if [ "$en" -eq 0 ]; then [ "$eone" -eq 0 ] && [ "$eall" -eq 0 ] && cons=1; elif [ "$eone" -le "$eall" ]; then cons=1; fi
    fi
    [ "$iv" -eq 1 ] && [ "$en" -le "$MAX_E" ] && [ "$eone" -le "$MAX_ONE" ] && [ "$eall" -le "$MAX_ALL" ] && res=1
    [ "$flags" -eq 1 ] && { [ "$S" = 1 ] || [ "$T" = 1 ] || [ "$X" = 1 ] || [ "$D" = 1 ] || [ "$Q" = 1 ] || [ "$U" = 1 ]; } && haz=1
    [ "$iv" -eq 1 ] && [ "$cons" -eq 1 ] && [ "$res" -eq 1 ] && [ "$haz" -eq 0 ] && acc=1
    if [ "$iv" -eq 0 ]; then st=INPUT_BINDING_INVALID; elif [ "$cons" -eq 0 ]; then st=MANIFEST_NUMERIC_INCONSISTENT; elif [ "$res" -eq 0 ]; then st=RESOURCE_BOUND_VIOLATION; elif [ "$haz" -eq 1 ]; then st=ARCHIVE_HAZARD_OBSERVED; else st=BOUNDED_MANIFEST_ACCEPTED; fi
    AL=YES
    [ "$RC" -eq 0 ] && [ "$SCHEMA_OK" -eq 1 ] || AL=NO
    [ "$(val INPUT_CASE_ID "$O")" = "$C" ] || AL=NO
    [ "$(val ARCHIVE_ID "$O")" = "$A" ] || AL=NO
    [ "$(val MANIFEST_ID "$O")" = "$M" ] || AL=NO
    [ "$(nv "$(val CORE_PRESENT "$O")")" = "$core" ] || AL=NO
    [ "$(nv "$(val INTEGER_FIELDS_VALID "$O")")" = "$ints" ] || AL=NO
    [ "$(nv "$(val FLAGS_VALID "$O")")" = "$flags" ] || AL=NO
    [ "$(nv "$(val INPUT_BINDING_VALID "$O")")" = "$iv" ] || AL=NO
    [ "$(nv "$(val ENTRY_COUNT "$O")")" = "$en" ] || AL=NO
    [ "$(nv "$(val MAX_ENTRY_DECLARED_BYTES "$O")")" = "$eone" ] || AL=NO
    [ "$(nv "$(val TOTAL_DECLARED_BYTES "$O")")" = "$eall" ] || AL=NO
    [ "$(nv "$(val MAX_ENTRIES_BOUND "$O")")" = 8 ] || AL=NO
    [ "$(nv "$(val MAX_ENTRY_DECLARED_BYTES_BOUND "$O")")" = 1048576 ] || AL=NO
    [ "$(nv "$(val MAX_TOTAL_DECLARED_BYTES_BOUND "$O")")" = 4194304 ] || AL=NO
    [ "$(nv "$(val MANIFEST_NUMERIC_CONSISTENT "$O")")" = "$cons" ] || AL=NO
    [ "$(nv "$(val RESOURCE_WITHIN_BOUNDS "$O")")" = "$res" ] || AL=NO
    [ "$(val SYMLINK_PRESENT "$O")" = "$S" ] || AL=NO
    [ "$(val TRAVERSAL_PRESENT "$O")" = "$T" ] || AL=NO
    [ "$(val ABSOLUTE_PATH_PRESENT "$O")" = "$X" ] || AL=NO
    [ "$(val DUPLICATE_PATH_PRESENT "$O")" = "$D" ] || AL=NO
    [ "$(val ENCRYPTED_ENTRY_PRESENT "$O")" = "$Q" ] || AL=NO
    [ "$(val UNSUPPORTED_ENTRY_TYPE_PRESENT "$O")" = "$U" ] || AL=NO
    [ "$(nv "$(val HAZARD_PRESENT "$O")")" = "$haz" ] || AL=NO
    [ "$(nv "$(val ARCHIVE_MANIFEST_GATE_ACCEPTED "$O")")" = "$acc" ] || AL=NO
    [ "$(val STATUS "$O")" = "$st" ] || AL=NO
    [ "$(val RESOURCE_PROFILE_ID "$O")" = "$PROFILE" ] || AL=NO
    [ "$(val HISTORICAL_T10A_BOUNDS_IMPORTED "$O")" = NO ] || AL=NO
    [ "$(val HOST_MECHANICAL_ABI "$O")" = read_text,to_float,str_replace ] || AL=NO
    [ "$(val PERSISTENT_STATE "$O")" = NA ] || AL=NO
    [ "$(val RAW_ARCHIVE_FORMAT_PARSING "$O")" = NOT_PROVEN ] || AL=NO
    [ "$(val ARCHIVE_HAZARD_DETECTION_FROM_RAW_BYTES "$O")" = NOT_PROVEN ] || AL=NO
    [ "$(val ACTUAL_ARCHIVE_EXTRACTION "$O")" = NOT_EXECUTED ] || AL=NO
    [ "$(val DOCUMENT_CONTENT_READING "$O")" = NOT_PROVEN ] || AL=NO
    [ "$(val DOCUMENT_UNDERSTANDING "$O")" = NOT_PROVEN ] || AL=NO
    [ "$(val SEMANTIC_UNDERSTANDING "$O")" = NOT_PROVEN ] || AL=NO
    [ "$(val PRODUCTION_STATE_MUTATED "$O")" = NO ] || AL=NO
    [ "$(val T10B_UNLOCKED_BY_THIS_INVOCATION "$O")" = NO ] || AL=NO
    if [ "$AL" = YES ]; then P=$((P+1)); else F=$((F+1)); fi
    echo "CASE_${I}_POST_VM_ALIGNMENT=$AL"
    [ "$L" = CFA ] && CFA="$acc"; [ "$L" = CFB ] && CFB="$acc"
    [ "$L" = REPLAY_A ] && { RIA="$IS"; RSA="$OS"; }
    if [ "$L" = REPLAY_B ]; then if [ "$IS" != "$RIA" ] || [ "$OS" != "$RSA" ]; then RP=NO; F=$((F+1)); fi; fi
}

base; E="$(printf '9%.0s' $(seq 1 64))"; pre_refusal OVERSIZE_NUMERIC_TOKEN || fail PRE_EXECUTION_GATE_FAILED 70
base; C="$(printf 'C%.0s' $(seq 1 256))"; pre_refusal OVERSIZE_ID_TOKEN || fail PRE_EXECUTION_GATE_FAILED 71
base; S="$(printf '1%.0s' $(seq 1 32))"; pre_refusal OVERSIZE_FLAG_TOKEN || fail PRE_EXECUTION_GATE_FAILED 72
base; C=$'BAD\nSTATUS'; pre_refusal ID_LINE_BREAK_INJECTION || fail PRE_EXECUTION_GATE_FAILED 73
base; writein; : >"$IN/unexpected_extra_file"; record_pre_refusal EXTRA_INPUT_FILE || fail PRE_EXECUTION_GATE_FAILED 74; rm -f "$IN/unexpected_extra_file"

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
base; ALL=4194304; run CFA
base; ALL=4194305; run CFB
for i in $(seq 1 16); do
    base; E=$((RANDOM%9)); ONE=$((1+$(rm6))); ALL=$((ONE+$(rm6)))
    if [ $((i%2)) -eq 1 ]; then m=$((RANDOM%4)); [ "$m" -eq 0 ] && E=9; [ "$m" -eq 1 ] && ONE=1048577; [ "$m" -eq 2 ] && ALL=4194305; [ "$m" -eq 3 ] && T=1; fi
    run "RANDOM_$i"
done
base; C="R_$(rh)"; A="RA_$(rh)"; M="RM_$(rh)"; E=7; ONE=777777; ALL=3333333; run REPLAY_A; run REPLAY_B

SA="$(sha "$SRC")"; BA="$(sha "$BC")"; CF=NO
[ "$CFA" = 1 ] && [ "$CFB" = 0 ] && CF=YES
printf '%s\n' \
"RESOURCE_PROFILE_SHA256=$PROFILE_X" \
"INPUT_SCHEMA_SHA256=$INPUT_SCHEMA_X" \
"OUTPUT_SCHEMA_SHA256=$OUTPUT_SCHEMA_X" \
"ABI_SHA256=$ABI_X" \
"BUILD_RECIPE_SHA256=$BUILD_RECIPE_X" \
"PRE_VM_RESOURCE_REFUSAL_CASES=$PRE" \
"PRE_VM_RESOURCE_REFUSAL_PASS_COUNT=$PREP" \
"PRE_EXECUTION_INPUT_TRANSPORT_GATE=$([ "$PRE" -eq 5 ] && [ "$PREP" -eq 5 ] && echo PASS || echo FAIL)" \
"OUTPUT_SCHEMA_RUNTIME_FAIL_COUNT=$SCHEMA_FAIL" \
"SOURCE_SHA256_AFTER_ALL_RUNS=$SA" \
"BYTECODE_SHA256_AFTER_ALL_RUNS=$BA" \
"SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=$([ "$SA" = "$SF" ] && echo YES || echo NO)" \
"BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=$([ "$BA" = "$BF" ] && echo YES || echo NO)" \
"UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=$LEAK" \
"TOTAL_VM_INVOCATIONS=$N" \
"POST_VM_ALIGNMENT_PASS_COUNT=$P" \
"POST_VM_ALIGNMENT_FAIL_COUNT=$F" \
"VM_NONZERO_COUNT=$NZ" \
"STEP_LIMIT_HIT_COUNT=$SL" \
"COUNTERFACTUAL_RESOURCE_BOUND_DECISION=$CF" \
"REPLAY_IDENTICAL_INPUT_DECISION=$RP" \
'DYNAMIC_INPUT=YES' \
'PERSISTENT_STATE=NA' \
'HOST_LEARNING=NO' \
'HOST_SEMANTIC_SUBSTITUTION=NO' \
'HOST_TOOL_SELECTION=NO' \
'HOST_POST_VM_TEST_ORACLE_ONLY=YES' \
'PYTHON_USED=NO' \
'RAW_ARCHIVE_FORMAT_PARSING=NOT_PROVEN' \
'ARCHIVE_HAZARD_DETECTION_FROM_RAW_BYTES=NOT_PROVEN' \
'ACTUAL_ARCHIVE_EXTRACTION=NOT_EXECUTED' \
'DOCUMENT_CONTENT_READING=NOT_PROVEN' \
'DOCUMENT_UNDERSTANDING=NOT_PROVEN' \
'SEMANTIC_UNDERSTANDING=NOT_PROVEN' \
'PRIOR_LAYER_REGRESSION=NOT_RUN' \
'COMBINED_COMPATIBILITY=NOT_RUN' \
'R7_FAMILY_ADMISSION=NOT_RUN' \
'T10B_UNLOCKED=NO_PENDING_SEPARATE_ADMISSION_RECEIPT' \
'PRODUCTION_STATE_MUTATED=NO'

if [ "$PRE" -eq 5 ] && [ "$PREP" -eq 5 ] && [ "$N" -eq 38 ] && [ "$P" -eq 38 ] && [ "$F" -eq 0 ] && [ "$NZ" -eq 0 ] && [ "$SL" -eq 0 ] && [ "$SCHEMA_FAIL" -eq 0 ] && [ "$LEAK" -eq 0 ] && [ "$CF" = YES ] && [ "$RP" = YES ] && [ "$SA" = "$SF" ] && [ "$BA" = "$BF" ]; then
    echo T10A_NATIVE_BOUNDED_ARCHIVE_MANIFEST_GATE=PASS_IN_EXACT_TESTED_RECONSTRUCTION_R3_SCOPE
    echo T10A_EXECUTION_ENVELOPE=PASS_IN_EXACT_TESTED_R3_SCOPE
    echo T10A_RECONSTRUCTION_RESOURCE_PROFILE_ADMISSION=PASS_IN_EXACT_TESTED_R3_SCOPE
    echo T10A_RECONSTRUCTION_R3_PREFLIGHT=PASS
    echo ADMISSION=PASS_IN_EXACT_TESTED_RECONSTRUCTION_R3_SCOPE
    echo RESULT=PASS_IN_EXACT_TESTED_RECONSTRUCTION_R3_SCOPE
else
    echo ADMISSION=FAIL
    echo RESULT=FAIL_IN_TESTED_RECONSTRUCTION_R3_SCOPE
    exit 1
fi
