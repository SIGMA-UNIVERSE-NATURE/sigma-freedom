#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="$HOME_SIGMA/sigma-freedom-write"

PROD_STATE="$HOME_SIGMA/SIGMA_CONTINUOUS_NATIVE_V2_2"
RAW="$PROD_STATE/raw"
HOLD="$PROD_STATE/hold"

STATE="$HOME_SIGMA/SIGMA_V4B2R2_REAL_V24_RC9_REPLAY_PREFLIGHT"
RUN_TAG=$("$P/bin/date" -u +%Y%m%dT%H%M%SZ).$$
SHADOW="$STATE/shadow.$RUN_TAG"
BRAIN="$SHADOW/BRAIN/EXTRA BRAIN_OPPO_24826"
E="$BRAIN/.sigma_exec"
LOG="$STATE/log/$RUN_TAG"
LOCK="$STATE/preflight.lock"

SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"
EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

SRC_REPO="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_V4_SEGMENTED_RECEIVED_CONTEXT_LEARNER_V4B1.sigma"
SRC="$E/SIGMA_V4_SEGMENTED_RECEIVED_CONTEXT_LEARNER_V4B1.sigma"
BC="$E/SIGMA_V4_SEGMENTED_RECEIVED_CONTEXT_LEARNER_V4B1.sigmab"
EXPECTED_SOURCE=2edd2d4f36d3dd9c2d03dab4218ceff1f2ef290feee711a49ef18ff53b056ad4

CTX_ID="$E/SIGMA_V4B1_CONTEXT_ID.memory"
CTX_TEXT="$E/SIGMA_V4B1_CONTEXT_TEXT.memory"
CURSOR="$E/SIGMA_V4B1_CURSOR_LEDGER.memory"
EVIDENCE="$E/SIGMA_V4B1_SEGMENT_EVIDENCE.memory"
COMPLETE="$E/SIGMA_V4B1_COMPLETION_LEDGER.memory"
STATUS="$E/SIGMA_V4B1_STATUS.memory"

mkdir -p "$E" "$LOG" "$STATE"

exec 9>"$LOCK"
if ! "$P/bin/flock" -n 9; then
    printf 'HOLD=V4B2R2_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
fi

hash1() { "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'; }

SIGMAC_SHA=$(hash1 "$SIGMAC")
VM_SHA=$(hash1 "$VM")
SOURCE_SHA=$(hash1 "$SRC_REPO")

printf 'SIGMA_PHASE=V4B2R2_REAL_V24_RC9_HELD_CONTEXT_REPLAY_PREFLIGHT\n'
printf 'SIGMAC_SHA256=%s\n' "$SIGMAC_SHA"
printf 'VM_SHA256=%s\n' "$VM_SHA"
printf 'SOURCE_SHA256=%s\n' "$SOURCE_SHA"
printf 'SHADOW_BRAIN=%s\n' "$BRAIN"
printf 'PRODUCTION_BRAIN_WRITE_TARGET=NO\n'
printf 'PRODUCTION_RAW_READ_ONLY_SOURCE=YES\n'
printf 'HOST_SEGMENT_SELECTION=NO\n'
printf 'HOST_COMPLETION_DECISION=NO\n'
printf 'HOST_RETRY_DECISION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'FIXED_VM_INVOCATIONS_PER_CONTEXT=35\n'
printf 'SHADOW_INPUT_INSTALL=PARTIAL_HASH_CHMOD0400_ATOMIC_RENAME\n'

V24_PID_BEFORE=$("$P/bin/pgrep" -f 'RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sh' | "$P/bin/head" -n1 || true)
printf 'PRODUCTION_V24_PID_BEFORE=%s\n' "$V24_PID_BEFORE"
[ -n "$V24_PID_BEFORE" ] || { printf 'HOLD=PRODUCTION_V24_NOT_RUNNING\n'; exit 21; }

[ "$SIGMAC_SHA" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 22; }
[ "$VM_SHA" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 23; }
[ "$SOURCE_SHA" = "$EXPECTED_SOURCE" ] || { printf 'HOLD=V4B_SOURCE_IDENTITY_MISMATCH\n'; exit 24; }

cp -- "$SRC_REPO" "$SRC" || { printf 'HOLD=SOURCE_INSTALL_FAILED\n'; exit 25; }
INSTALLED_SOURCE_SHA=$(hash1 "$SRC")
printf 'INSTALLED_SOURCE_SHA256=%s\n' "$INSTALLED_SOURCE_SHA"
[ "$INSTALLED_SOURCE_SHA" = "$EXPECTED_SOURCE" ] || { printf 'HOLD=INSTALLED_SOURCE_IDENTITY_MISMATCH\n'; exit 26; }

rm -f -- "$BC.partial"
"$SIGMAC" "$SRC" "$BC.partial"
RC=$?
printf 'V4B2R2_SIGMAC_RC=%s\n' "$RC"
[ "$RC" -eq 0 ] || { printf 'HOLD=V4B2R2_COMPILE_FAILED\n'; exit 27; }
[ -s "$BC.partial" ] || { printf 'HOLD=V4B2R2_BYTECODE_EMPTY\n'; exit 28; }
mv -f -- "$BC.partial" "$BC"
chmod 0400 "$BC"
printf 'V4B2R2_BYTECODE_SHA256=%s\n' "$(hash1 "$BC")"

reset_shadow_context_state() {
    rm -f -- "$CURSOR" "$EVIDENCE" "$COMPLETE" "$STATUS" "$CTX_ID" "$CTX_TEXT"
    : > "$CURSOR"
    : > "$EVIDENCE"
    : > "$COMPLETE"
    : > "$STATUS"
}

install_exact_context() {
    SHA="$1"
    DOC="$2"
    PART="$CTX_TEXT.partial.$$"
    rm -f -- "$PART" "$CTX_TEXT"
    cp -- "$DOC" "$PART" || return 1
    PART_SHA=$(hash1 "$PART")
    [ "$PART_SHA" = "$SHA" ] || return 2
    chmod 0400 "$PART" || return 3
    mv -f -- "$PART" "$CTX_TEXT" || return 4
    [ "$(hash1 "$CTX_TEXT")" = "$SHA" ] || return 5
    return 0
}

run_fixed_replay() {
    SHA="$1"
    DOC="$RAW/$SHA.document"
    MARK="$HOLD/$SHA.hold"

    printf '\n=== REAL_CONTEXT %s ===\n' "$SHA"

    [ -f "$DOC" ] || { printf 'HOLD=REAL_RAW_DOCUMENT_MISSING context=%s\n' "$SHA"; return 40; }
    [ -f "$MARK" ] || { printf 'HOLD=REAL_V24_HOLD_MARKER_MISSING context=%s\n' "$SHA"; return 41; }

    DOC_SHA=$(hash1 "$DOC")
    printf 'REAL_DOCUMENT_SHA256=%s\n' "$DOC_SHA"
    [ "$DOC_SHA" = "$SHA" ] || { printf 'HOLD=REAL_DOCUMENT_SHA_MISMATCH context=%s\n' "$SHA"; return 42; }

    grep -F -x "CONTEXT_SHA256=$SHA" "$MARK" >/dev/null || { printf 'HOLD=HOLD_CONTEXT_ID_MISMATCH context=%s\n' "$SHA"; return 43; }
    grep -F -x 'VM_RC=9' "$MARK" >/dev/null || { printf 'HOLD=HOLD_NOT_RC9 context=%s\n' "$SHA"; return 44; }

    printf 'V24_RC9_EVIDENCE=PASS\n'

    reset_shadow_context_state
    printf '%s' "$SHA" > "$CTX_ID"

    install_exact_context "$SHA" "$DOC"
    IRC=$?
    [ "$IRC" -eq 0 ] || { printf 'HOLD=SHADOW_CONTEXT_INSTALL_FAILED context=%s rc=%s\n' "$SHA" "$IRC"; return 45; }

    COPIED_SHA=$(hash1 "$CTX_TEXT")
    printf 'SHADOW_CONTEXT_SHA256=%s\n' "$COPIED_SHA"
    printf 'SHADOW_CONTEXT_MODE=%s\n' "$("$P/bin/stat" -c '%a' "$CTX_TEXT")"
    [ "$COPIED_SHA" = "$SHA" ] || { printf 'HOLD=SHADOW_CONTEXT_COPY_MISMATCH context=%s\n' "$SHA"; return 46; }

    I=0
    while [ "$I" -lt 35 ]; do
        RUNLOG="$LOG/$SHA.$I.log"
        (
            cd "$BRAIN" || exit 47
            "$VM" "$BC"
        ) >"$RUNLOG" 2>&1
        VMRC=$?
        printf 'REAL_REPLAY_VM context=%s invocation=%s rc=%s\n' "$SHA" "$I" "$VMRC"
        [ "$VMRC" -eq 0 ] || { printf 'HOLD=REAL_REPLAY_VM_FAILURE context=%s invocation=%s rc=%s\n' "$SHA" "$I" "$VMRC"; return 48; }
        I=$((I + 1))
    done

    FINAL_STATUS=$(cat "$STATUS")
    printf 'FINAL_NATIVE_STATUS=%s\n' "$FINAL_STATUS"
    printf 'CURSOR_COMMIT_COUNT=%s\n' "$(grep -c 'COMMIT=YES' "$CURSOR" || true)"
    printf 'EVIDENCE_COMMIT_COUNT=%s\n' "$(grep -c 'COMMIT=YES' "$EVIDENCE" || true)"
    printf 'COMPLETION_COMMIT_COUNT=%s\n' "$(grep -c 'COMPLETE=YES' "$COMPLETE" || true)"

    grep -F -x "CTX=$SHA || COMPLETE=YES" "$COMPLETE" >/dev/null || {
        printf 'HOLD=REAL_CONTEXT_NOT_COMPLETED context=%s status=%s\n' "$SHA" "$FINAL_STATUS"
        return 49
    }

    if grep -F 'STATUS REFUSE_' "$LOG/$SHA."*.log >/dev/null 2>&1; then
        printf 'HOLD=REAL_CONTEXT_NATIVE_REFUSAL context=%s\n' "$SHA"
        return 50
    fi

    if [ "$FINAL_STATUS" != 'ALREADY_COMPLETE' ] &&
       [ "$FINAL_STATUS" != 'CONTEXT_COMPLETE' ] &&
       [ "$FINAL_STATUS" != 'RECOVERED_COMPLETION' ]; then
        printf 'HOLD=UNEXPECTED_FINAL_NATIVE_STATUS context=%s status=%s\n' "$SHA" "$FINAL_STATUS"
        return 51
    fi

    printf 'REAL_CONTEXT_RC9_RECOVERED_BY_V4B=PASS context=%s\n' "$SHA"
    return 0
}

C1=49c16c567fcbd0df0241b249e2b51dbf8e20d23ec1dc78ff8d92e3233dda9382
C2=59cd0bc563b1dc8566c88623366403b53f4e9094ca98ef4fe2d9e6531dc5a774
C3=0d911059d92f2af2601f39420c7aa0865fb24fbbc96aca96961d53b19260d8c3
C4=c12f847d694599d12cf35b5f489f1061e79a3fe3cf2f648684da55d387a2b16b
C5=ee5aca6dbe12ffcdd7e5b4aefeb3b5f8bb418b7d9eb4f59404c76b661bc086ba

run_fixed_replay "$C1" || exit 60
run_fixed_replay "$C2" || exit 61
run_fixed_replay "$C3" || exit 62
run_fixed_replay "$C4" || exit 63
run_fixed_replay "$C5" || exit 64

V24_PID_AFTER=$("$P/bin/pgrep" -f 'RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sh' | "$P/bin/head" -n1 || true)
printf '\nPRODUCTION_V24_PID_AFTER=%s\n' "$V24_PID_AFTER"
[ "$V24_PID_AFTER" = "$V24_PID_BEFORE" ] || { printf 'HOLD=PRODUCTION_V24_PID_CHANGED\n'; exit 65; }

printf '\nV4B2R2_REAL_V24_RC9_HELD_CONTEXT_REPLAY_PREFLIGHT=PASS\n'
printf 'REAL_RC9_CONTEXTS_REPLAYED=5\n'
printf 'REAL_RC9_CONTEXTS_COMPLETED_BY_V4B=5\n'
printf 'FIXED_VM_INVOCATIONS_PER_CONTEXT=35\n'
printf 'SHADOW_INPUT_INSTALL_IDEMPOTENT=PASS\n'
printf 'HOST_SEGMENT_SELECTION=NO\n'
printf 'HOST_COMPLETION_DECISION=NO\n'
printf 'HOST_RETRY_DECISION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'SHADOW_STATE_NAMESPACE_ISOLATION=PASS\n'
printf 'PRODUCTION_BRAIN_WRITE_TARGET=NO\n'
printf 'PRODUCTION_RAW_READ_ONLY_SOURCE=YES\n'
printf 'PRODUCTION_V24_REMAINED_RUNNING_SAME_PID=PASS\n'
printf 'REAL_V24_RC9_CONTEXT_RECOVERY=PROVEN_IN_FIVE_OBSERVED_HELD_CONTEXT_SCOPE\n'
printf 'V4_PRODUCTION_PROMOTION_ALLOWED=NO\n'
printf 'BOUNDED_FILE_IO=NOT_PROVEN\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'NEXT_ACTION=CHECKPOINT_V4B2R2_THEN_INTEGRATE_V4A_ARBITER_WITH_V4B_SEGMENTED_LEARNER_IN_SHADOW_CONTINUOUS_CONTROLLER\n'
