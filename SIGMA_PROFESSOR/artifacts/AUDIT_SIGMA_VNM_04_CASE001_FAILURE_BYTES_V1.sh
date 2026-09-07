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
V1_HYP="$B1/input/hypothesis.memory"
V1_EVID="$B1/input/evidence.memory"
V4_LOG="$ROOT/log/CASE_001_FULL_CHAIN_SUPPORT2_CASE01_V4.log"
V1_LOG="$ROOT/log/CASE_001_FULL_CHAIN_SUPPORT2_CASE01_V1.log"
AUDIT="$HOME_SIGMA/VNM04_CASE001_BYTE_AUDIT_$(date +%Y%m%d_%H%M%S)"

"$P/bin/mkdir" -p "$AUDIT"

printf 'SIGMA_PHASE=VNM04_CASE001_FAILURE_BYTE_AUDIT\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_SEMANTIC_SUBSTITUTION=NO\n'
printf 'AUDIT_MUTATES_FAILED_CASE=NO\n'
printf 'AUDIT_DIR=%s\n' "$AUDIT"

FILES_OK=YES
for F in "$BUNDLE" "$V1_HYP" "$V1_EVID" "$V4_LOG" "$V1_LOG"; do
    if [ ! -f "$F" ]; then
        printf 'MISSING_FILE=%s\n' "$F"
        FILES_OK=NO
    fi
done

printf 'FILES_OK=%s\n' "$FILES_OK"

if [ "$FILES_OK" = YES ]; then
    for F in "$BUNDLE" "$V1_HYP" "$V1_EVID" "$V4_LOG" "$V1_LOG"; do
        printf 'FILE=%s\n' "$F"
        printf 'SIZE=%s\n' "$("$P/bin/wc" -c < "$F")"
        printf 'SHA256=%s\n' "$("$P/bin/sha256sum" "$F" | "$P/bin/awk" '{print $1}')"
    done

    "$P/bin/sed" -n '1p' "$BUNDLE" > "$AUDIT/expected_hypothesis_from_bundle.memory"
    "$P/bin/tail" -n +2 "$BUNDLE" > "$AUDIT/expected_evidence_from_bundle.memory"

    if "$P/bin/cmp" -s "$AUDIT/expected_hypothesis_from_bundle.memory" "$V1_HYP"; then
        printf 'BUNDLE_LINE1_EQUALS_VNM01_HYPOTHESIS=YES\n'
    else
        printf 'BUNDLE_LINE1_EQUALS_VNM01_HYPOTHESIS=NO\n'
    fi

    if "$P/bin/cmp" -s "$AUDIT/expected_evidence_from_bundle.memory" "$V1_EVID"; then
        printf 'BUNDLE_LINES2N_EQUALS_VNM01_EVIDENCE=YES\n'
    else
        printf 'BUNDLE_LINES2N_EQUALS_VNM01_EVIDENCE=NO\n'
    fi

    printf '\n=== VNM04 BUNDLE LINE-NUMBERED ===\n'
    "$P/bin/nl" -ba "$BUNDLE"

    printf '\n=== VNM01 HYPOTHESIS LINE-NUMBERED ===\n'
    "$P/bin/nl" -ba "$V1_HYP"

    printf '\n=== VNM01 EVIDENCE LINE-NUMBERED ===\n'
    "$P/bin/nl" -ba "$V1_EVID"

    printf '\n=== VNM04 BUNDLE HEX ===\n'
    "$P/bin/od" -An -tx1 -v "$BUNDLE"

    printf '\n=== VNM01 EVIDENCE HEX ===\n'
    "$P/bin/od" -An -tx1 -v "$V1_EVID"

    printf '\n=== VNM04 CASE001 RAW LOG ===\n'
    "$P/bin/cat" "$V4_LOG"

    printf '\n=== VNM01 CASE001 RAW LOG ===\n'
    "$P/bin/cat" "$V1_LOG"

    "$P/bin/cp" -f -- "$BUNDLE" "$AUDIT/vnm04_bundle.memory"
    "$P/bin/cp" -f -- "$V1_HYP" "$AUDIT/vnm01_hypothesis.memory"
    "$P/bin/cp" -f -- "$V1_EVID" "$AUDIT/vnm01_evidence.memory"
    "$P/bin/cp" -f -- "$V4_LOG" "$AUDIT/vnm04.log"
    "$P/bin/cp" -f -- "$V1_LOG" "$AUDIT/vnm01.log"

    printf '\n=== AUDIT RESULT ===\n'
    printf 'AUDIT_DIR=%s\n' "$AUDIT"
    printf 'FAILED_CASE_PRESERVED=YES\n'
    printf 'PRODUCTION_STATE_MUTATED=NO\n'
else
    printf 'AUDIT_RESULT=HOLD_FAILED_CASE_FILES_MISSING\n'
fi
