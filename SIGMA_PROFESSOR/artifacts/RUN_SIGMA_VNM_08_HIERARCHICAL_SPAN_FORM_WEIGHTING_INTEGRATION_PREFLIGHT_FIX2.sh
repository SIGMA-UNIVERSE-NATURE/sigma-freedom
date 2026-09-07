#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="${SIGMA_REPO:-$HOME_SIGMA/sigma-freedom-write}"

PARENT_REL="SIGMA_PROFESSOR/artifacts/RUN_SIGMA_VNM_08_HIERARCHICAL_SPAN_FORM_WEIGHTING_INTEGRATION_PREFLIGHT.sh"
FIX1_REL="SIGMA_PROFESSOR/artifacts/RUN_SIGMA_VNM_08_HIERARCHICAL_SPAN_FORM_WEIGHTING_INTEGRATION_PREFLIGHT_FIX1.sh"
VNM07_REL="SIGMA_PROFESSOR/artifacts/RUN_SIGMA_VNM_07_NATIVE_SPAN_OBSERVATION_TO_FORM_OBSERVATION_ADAPTER_PREFLIGHT.sh"
PARENT="$REPO/$PARENT_REL"
FIX1="$REPO/$FIX1_REL"
VNM07="$REPO/$VNM07_REL"

EXPECTED_PARENT_GIT_BLOB=ebb17737ce9119e609ef9d83e29db4039f0ac6eb
EXPECTED_FIX1_GIT_BLOB=9fdd179853a7f9eedefd934f143b0d958a9ff1fb
EXPECTED_VNM07_GIT_BLOB=840d6d86e11b7bc8fc8e881ee7dc5cb26e9c5ee3
OLD_WRONG_VNM07_SHA256=ef2fe0776de85622b737a9161b4959ff4b6bba28832ac483a6a129d42463327a
CORRECT_VNM07_SHA256=53fe674e377439146078994c4ba6af3215c96bd966f470d9bbac74bc383e1921

sha_of() {
    "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'
}

blob_of() {
    git -C "$REPO" hash-object "$1"
}

printf 'SIGMA_PHASE=VNM_08_FIX2_NEGATIVE_SUPPORT_FAULT_FRAMING_REPAIR\n'
printf 'REPAIR_CLASS=RUNNER_ONLY_MECHANICAL_FAULT_INJECTION_REPAIR\n'
printf 'NATIVE_SOURCE_CHANGED=NO\n'
printf 'VNM07_RUNNER_BYTES_CHANGED=NO\n'
printf 'VNM08_PARENT_RUNNER_CHANGED=NO\n'
printf 'COGNITIVE_POLICY_CHANGED=NO\n'
printf 'CASE_MATRIX_CHANGED=NO\n'
printf 'PASS_DEFINITION_WEAKENED=NO\n'
printf 'FULL_REQUIRED_SUITE_RERUN=YES\n'

[ -f "$PARENT" ] || { printf 'HOLD=VNM08_PARENT_RUNNER_MISSING\n'; exit 20; }
[ -f "$FIX1" ] || { printf 'HOLD=VNM08_FIX1_WRAPPER_MISSING\n'; exit 21; }
[ -f "$VNM07" ] || { printf 'HOLD=VNM07_RUNNER_MISSING\n'; exit 22; }

parent_blob=$(blob_of "$PARENT")
fix1_blob=$(blob_of "$FIX1")
vnm07_blob=$(blob_of "$VNM07")
vnm07_sha=$(sha_of "$VNM07")
printf 'PARENT_GIT_BLOB=%s\n' "$parent_blob"
printf 'FIX1_GIT_BLOB=%s\n' "$fix1_blob"
printf 'VNM07_RUNNER_GIT_BLOB=%s\n' "$vnm07_blob"
printf 'VNM07_RUNNER_SHA256=%s\n' "$vnm07_sha"

[ "$parent_blob" = "$EXPECTED_PARENT_GIT_BLOB" ] || { printf 'HOLD=VNM08_PARENT_RUNNER_IDENTITY_MISMATCH\n'; exit 23; }
[ "$fix1_blob" = "$EXPECTED_FIX1_GIT_BLOB" ] || { printf 'HOLD=VNM08_FIX1_WRAPPER_IDENTITY_MISMATCH\n'; exit 24; }
[ "$vnm07_blob" = "$EXPECTED_VNM07_GIT_BLOB" ] || { printf 'HOLD=VNM07_RUNNER_GIT_BLOB_MISMATCH\n'; exit 25; }
[ "$vnm07_sha" = "$CORRECT_VNM07_SHA256" ] || { printf 'HOLD=VNM07_RUNNER_SHA256_MISMATCH\n'; exit 26; }

OLD_META="EXPECTED_VNM07_RUNNER=$OLD_WRONG_VNM07_SHA256"
NEW_META="EXPECTED_VNM07_RUNNER=$CORRECT_VNM07_SHA256"
old_meta_count=$("$P/bin/grep" -F -x -c "$OLD_META" "$PARENT" || true)
new_meta_count=$("$P/bin/grep" -F -x -c "$NEW_META" "$PARENT" || true)
negative_case_count=$("$P/bin/grep" -F -c 'CASE_NAME=NEGATIVE_SUPPORT_MISMATCH' "$PARENT" || true)

printf 'OLD_METADATA_LINE_MATCH_COUNT=%s\n' "$old_meta_count"
printf 'CORRECTED_METADATA_LINE_MATCH_COUNT_BEFORE=%s\n' "$new_meta_count"
printf 'NEGATIVE_SUPPORT_CASE_LINE_MATCH_COUNT=%s\n' "$negative_case_count"

[ "$old_meta_count" -eq 1 ] || { printf 'HOLD=OLD_METADATA_LINE_MATCH_COUNT_NOT_ONE\n'; exit 27; }
[ "$new_meta_count" -eq 0 ] || { printf 'HOLD=CORRECTED_METADATA_ALREADY_PRESENT_IN_PARENT\n'; exit 28; }
[ "$negative_case_count" -eq 1 ] || { printf 'HOLD=NEGATIVE_SUPPORT_CASE_LINE_MATCH_COUNT_NOT_ONE\n'; exit 29; }

FIXROOT="$HOME_SIGMA/SIGMA_VNM_08_FIX2_NEGATIVE_SUPPORT_FAULT_FRAMING_REPAIR"
MAT1="$FIXROOT/metadata_fixed.tmp"
MAT="$FIXROOT/RUN_SIGMA_VNM_08_HIERARCHICAL_SPAN_FORM_WEIGHTING_INTEGRATION_PREFLIGHT_FIX2_MATERIALIZED.sh"
"$P/bin/mkdir" -p "$FIXROOT"

"$P/bin/awk" -v old="$OLD_META" -v new="$NEW_META" '
    $0 == old { print new; next }
    { print }
' "$PARENT" > "$MAT1" || { printf 'HOLD=METADATA_MATERIALIZATION_FAILED\n'; exit 30; }

"$P/bin/awk" '
    index($0, "CASE_NAME=NEGATIVE_SUPPORT_MISMATCH") == 1 {
        print "CASE_NAME=NEGATIVE_SUPPORT_MISMATCH"
        print "BN=\"$CASES/neg04\""
        print "XN=\"$BN/.sigma_exec/SIGMA_VNM_04_PAIR_CANDIDATE_TO_WEIGHT_INPUT_BRIDGE_V1\""
        print "mkdir -p \"$XN/input\" \"$XN/output\""
        print "fault_candidate=$(cat \"$CAND\")"
        print "fault_suffix=\x27||SUPPORT||2\x27"
        print "case \"$fault_candidate\" in"
        print "    *\"$fault_suffix\") ;;"
        print "    *) fail 62 NEGATIVE_FAULT_PRECONDITION_SUPPORT2_MISSING ;;"
        print "esac"
        print "fault_prefix=\"${fault_candidate%$fault_suffix}\""
        print "printf \x27%s||SUPPORT||3\x27 \"$fault_prefix\" > \"$XN/input/candidate.memory\""
        print "fault_after=$(cat \"$XN/input/candidate.memory\")"
        print "[ \"$fault_after\" = \"${fault_prefix}||SUPPORT||3\" ] || fail 63 NEGATIVE_FAULT_WRITE_READBACK_MISMATCH"
        print "cp \"$OBS\" \"$XN/input/observations.memory\""
        print "printf \x27SENTINEL\x27 > \"$XN/output/vnm01_input_bundle.memory\""
        print "before=$(sha_of \"$XN/output/vnm01_input_bundle.memory\")"
        print "runvm VNM04 \"$BN\" \"$BC04\" \"$LOG/neg04.log\""
        print "expect SUPPORT_PAIR_COUNT 2"
        print "expect SUPPORT_MATCH 0"
        print "expect OUTPUT_ALLOWED 0"
        print "expect BRIDGE_STATUS REFUSED_CANDIDATE_SUPPORT_MISMATCH"
        print "after=$(sha_of \"$XN/output/vnm01_input_bundle.memory\")"
        print "[ \"$before\" = \"$after\" ] || fail 61 REFUSAL_MUTATED_OUTPUT"
        print "ALIGN=$((ALIGN+1))"
        print "NEG=$((NEG+1))"
        next
    }
    { print }
' "$MAT1" > "$MAT" || { printf 'HOLD=FAULT_FIX_MATERIALIZATION_FAILED\n'; exit 31; }

"$P/bin/rm" -f -- "$MAT1"
"$P/bin/chmod" 0700 "$MAT" || exit 32

old_after=$("$P/bin/grep" -F -x -c "$OLD_META" "$MAT" || true)
new_after=$("$P/bin/grep" -F -x -c "$NEW_META" "$MAT" || true)
precondition_after=$("$P/bin/grep" -F -c 'NEGATIVE_FAULT_PRECONDITION_SUPPORT2_MISSING' "$MAT" || true)

printf 'OLD_METADATA_LINE_COUNT_AFTER=%s\n' "$old_after"
printf 'CORRECTED_METADATA_LINE_COUNT_AFTER=%s\n' "$new_after"
printf 'NEGATIVE_FAULT_PRECONDITION_COUNT_AFTER=%s\n' "$precondition_after"

[ "$old_after" -eq 0 ] || { printf 'HOLD=OLD_METADATA_LINE_REMAINS_AFTER\n'; exit 33; }
[ "$new_after" -eq 1 ] || { printf 'HOLD=CORRECTED_METADATA_LINE_COUNT_AFTER_NOT_ONE\n'; exit 34; }
[ "$precondition_after" -eq 1 ] || { printf 'HOLD=NEGATIVE_FAULT_PRECONDITION_COUNT_AFTER_NOT_ONE\n'; exit 35; }

bash -n "$MAT" || { printf 'HOLD=MATERIALIZED_RUNNER_BASH_SYNTAX_FAIL\n'; exit 36; }

mat_sha=$(sha_of "$MAT")
printf 'MATERIALIZED_RUNNER_SHA256=%s\n' "$mat_sha"
printf 'CORRECTED_VNM07_RUNNER_SHA256=%s\n' "$CORRECT_VNM07_SHA256"
printf 'FULL_29_VM_GATE_START=YES\n'

bash "$MAT"
RC=$?

printf '\n=== VNM08 FIX2 WRAPPER RESULT ===\n'
printf 'MATERIALIZED_RUNNER_SHA256=%s\n' "$mat_sha"
printf 'FULL_GATE_RC=%s\n' "$RC"

exit "$RC"
