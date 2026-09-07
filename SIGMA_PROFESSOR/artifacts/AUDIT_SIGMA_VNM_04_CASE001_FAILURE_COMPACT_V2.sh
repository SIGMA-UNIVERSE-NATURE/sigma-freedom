#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
ROOT="$HOME_SIGMA/SIGMA_VNM_04_PAIR_CANDIDATE_TO_WEIGHT_INPUT_BRIDGE_V1_PREFLIGHT"
CASE="$ROOT/cases/CASE_001_FULL_CHAIN_SUPPORT2"
B4="$CASE/.sigma_exec/SIGMA_VNM_04_PAIR_CANDIDATE_TO_WEIGHT_INPUT_BRIDGE_V1"
B1="$CASE/.sigma_exec/SIGMA_VNM_01_SURFACE_FORM_EVIDENCE_WEIGHTING_V1"
BUNDLE="$B4/output/vnm01_input_bundle.memory"
HYP="$B1/input/hypothesis.memory"
EVID="$B1/input/evidence.memory"
V4LOG="$ROOT/log/CASE_001_FULL_CHAIN_SUPPORT2_CASE01_V4.log"
V1LOG="$ROOT/log/CASE_001_FULL_CHAIN_SUPPORT2_CASE01_V1.log"

printf 'SIGMA_PHASE=VNM04_CASE001_COMPACT_BYTE_AUDIT_V2\n'
printf 'AUDIT_MUTATES_FAILED_CASE=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_SEMANTIC_SUBSTITUTION=NO\n'

FILES_OK=YES
for F in "$BUNDLE" "$HYP" "$EVID" "$V4LOG" "$V1LOG"; do
    if [ ! -f "$F" ]; then
        printf 'MISSING_FILE=%s\n' "$F"
        FILES_OK=NO
    fi
done
printf 'FILES_OK=%s\n' "$FILES_OK"

if [ "$FILES_OK" = YES ]; then
    TMP="$HOME_SIGMA/.vnm04_case001_compact_$$"
    "$P/bin/mkdir" -p "$TMP"
    "$P/bin/sed" -n '1p' "$BUNDLE" > "$TMP/hyp.expected"
    "$P/bin/tail" -n +2 "$BUNDLE" > "$TMP/evid.expected"

    if "$P/bin/cmp" -s "$TMP/hyp.expected" "$HYP"; then
        printf 'BUNDLE_LINE1_EQUALS_VNM01_HYPOTHESIS=YES\n'
    else
        printf 'BUNDLE_LINE1_EQUALS_VNM01_HYPOTHESIS=NO\n'
    fi

    if "$P/bin/cmp" -s "$TMP/evid.expected" "$EVID"; then
        printf 'BUNDLE_LINES2N_EQUALS_VNM01_EVIDENCE=YES\n'
    else
        printf 'BUNDLE_LINES2N_EQUALS_VNM01_EVIDENCE=NO\n'
    fi

    printf 'BUNDLE_SHA256=%s\n' "$("$P/bin/sha256sum" "$BUNDLE" | "$P/bin/awk" '{print $1}')"
    printf 'HYP_SHA256=%s\n' "$("$P/bin/sha256sum" "$HYP" | "$P/bin/awk" '{print $1}')"
    printf 'EVID_SHA256=%s\n' "$("$P/bin/sha256sum" "$EVID" | "$P/bin/awk" '{print $1}')"

    CAND_A=$("$P/bin/sed" -n 's/^CANDIDATE_FORM_A //p' "$V4LOG")
    CAND_B=$("$P/bin/sed" -n 's/^CANDIDATE_FORM_B //p' "$V4LOG")
    SUPPORT=$("$P/bin/sed" -n 's/^SUPPORT_PAIR_COUNT //p' "$V4LOG")
    COMPETING=$("$P/bin/sed" -n 's/^COMPETING_RAW_PAIR_COUNT //p' "$V4LOG")
    ELIGIBLE=$("$P/bin/sed" -n 's/^ELIGIBLE_EVIDENCE_COUNT //p' "$V4LOG")

    printf 'VNM04_CANDIDATE_FORM_A=%s\n' "$CAND_A"
    printf 'VNM04_CANDIDATE_FORM_B=%s\n' "$CAND_B"
    printf 'VNM04_SUPPORT_PAIR_COUNT=%s\n' "$SUPPORT"
    printf 'VNM04_COMPETING_RAW_PAIR_COUNT=%s\n' "$COMPETING"
    printf 'VNM04_ELIGIBLE_EVIDENCE_COUNT=%s\n' "$ELIGIBLE"

    printf '\n=== BUNDLE ===\n'
    "$P/bin/nl" -ba "$BUNDLE"
    printf '\n=== VNM01_HYPOTHESIS ===\n'
    "$P/bin/nl" -ba "$HYP"
    printf '\n=== VNM01_EVIDENCE ===\n'
    "$P/bin/nl" -ba "$EVID"

    INDEX=0
    while IFS= read -r LINE; do
        [ -n "$LINE" ] || continue
        INDEX=$((INDEX + 1))
        F1=$(printf '%s\n' "$LINE" | "$P/bin/awk" -F'\\|\\|' '{print $3}')
        F2=$(printf '%s\n' "$LINE" | "$P/bin/awk" -F'\\|\\|' '{print $4}')
        PAIR=NO
        if [ "$F1" = "$CAND_A" ] && [ "$F2" = "$CAND_B" ]; then PAIR=YES; fi
        if [ "$F1" = "$CAND_B" ] && [ "$F2" = "$CAND_A" ]; then PAIR=YES; fi
        printf 'EVIDENCE_%s_FORM_A=%s\n' "$INDEX" "$F1"
        printf 'EVIDENCE_%s_FORM_B=%s\n' "$INDEX" "$F2"
        printf 'EVIDENCE_%s_EQUALS_VNM04_CANDIDATE_PAIR=%s\n' "$INDEX" "$PAIR"
    done < "$EVID"

    printf '\n=== VNM01_NATIVE_COUNTS ===\n'
    "$P/bin/grep" -E '^(FORM_A|FORM_B|NEW_EVIDENCE_LINE_COUNT|NEW_SUPPORT_COUNT|NEW_COMPETING_COUNT|NEW_UNRELATED_COUNT|WEIGHT_BEFORE|PROPOSED_WEIGHT|WEIGHT_AFTER) ' "$V1LOG" || true

    "$P/bin/rm" -rf -- "$TMP"
    printf 'FAILED_CASE_PRESERVED=YES\n'
    printf 'PRODUCTION_STATE_MUTATED=NO\n'
else
    printf 'AUDIT_RESULT=HOLD_FAILED_CASE_FILES_MISSING\n'
fi
