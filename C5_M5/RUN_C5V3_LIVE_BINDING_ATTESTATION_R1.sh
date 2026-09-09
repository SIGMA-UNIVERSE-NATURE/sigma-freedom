#!/data/data/com.termux/files/usr/bin/bash
# SIGMA C5V3 live-binding attestation R1.
# READ-ONLY COLLECTION ONLY: no restart, kill, chmod, cp, mv, rm, network,
# package action, state write, production mutation, or binding change.

set -u
export LC_ALL=C

ROOT="${1:-${HOME}/SIGMA/sigma_genesis1}"

PRODUCTION_CORE_SHA256="23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc"
PRODUCTION_RUNNER_SHA256="092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847"
PRODUCTION_INGRESS_SHA256="22901ffce990a38163e2d2db2ef85a9e553c252159386baf136874daf9d7139c"
SIGMAC_SHA256="65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
VM_SHA256="029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99"
R6_SOURCE_SHA256="dde709a25d8e2f2626c299ad4d5c40562e2bcc253cf9bb63aef17e44f02943ac"
R6_BYTECODE_SHA256="dcb4f0ed9c637e368d396214471ae4c8fd67bc6622b02f133e867d2bab8b6693"
T1_SOURCE_SHA256="d92bbd5bc36d798496fd04191e3d385e668cc4e5d1d37b59c25567b77a7091ca"
T1_BYTECODE_SHA256="e43d983806936599eafb507872784b578a1cfa95a1f47425b730d52e2d2a9562"
T2_SOURCE_SHA256="81bc18d6ce7c8c9a2cd54324360a948257074d60f5fa864d4951e8d5e4a3e135"
T2_BYTECODE_SHA256="1c80fc66bf8e0326a7ce0fd21235b39c445f68841ee8442b53a20902174d8f5b"
T3_SOURCE_SHA256="ed46788b55bea3e39c2c5c46bae28d2d9a077ff4cf70a08bc9dfdbb88fb33955"
T3_BYTECODE_SHA256="1828dcd53d1f062a785329bab3c88e135d8f5e4779976c8c128933bee6f9801e"
COMBINED_SOURCE_SHA256="14f280342ba9e7925aecdcef47a0861aea56667c0bb28463fcfa4e75990e83c6"
COMBINED_BYTECODE_SHA256="79bdde5548548c570a7d33ab880f50f3c1bbf106a283a16ad9a6a2b5193180a4"

collection_errors=0
candidate_count=0
known_match_count=0
sigma_process_count=0
state_root_count=0

emit() {
    printf '%s\n' "$*"
}

safe_realpath() {
    local p="$1"
    if command -v realpath >/dev/null 2>&1; then
        realpath -e -- "$p" 2>/dev/null || realpath -- "$p" 2>/dev/null || printf '%s\n' "$p"
    else
        printf '%s\n' "$p"
    fi
}

safe_sha256() {
    local f="$1"
    if [ ! -f "$f" ] || [ ! -r "$f" ]; then
        return 1
    fi
    sha256sum -- "$f" 2>/dev/null | awk '{print $1}'
}

known_label_for_hash() {
    case "$1" in
        "$PRODUCTION_CORE_SHA256") printf '%s\n' 'PRODUCTION_CORE' ;;
        "$PRODUCTION_RUNNER_SHA256") printf '%s\n' 'PRODUCTION_RUNNER' ;;
        "$PRODUCTION_INGRESS_SHA256") printf '%s\n' 'PRODUCTION_INGRESS' ;;
        "$SIGMAC_SHA256") printf '%s\n' 'SIGMAC' ;;
        "$VM_SHA256") printf '%s\n' 'VM' ;;
        "$R6_SOURCE_SHA256") printf '%s\n' 'R6_SOURCE' ;;
        "$R6_BYTECODE_SHA256") printf '%s\n' 'R6_BYTECODE' ;;
        "$T1_SOURCE_SHA256") printf '%s\n' 'T1_SOURCE' ;;
        "$T1_BYTECODE_SHA256") printf '%s\n' 'T1_BYTECODE' ;;
        "$T2_SOURCE_SHA256") printf '%s\n' 'T2_SOURCE' ;;
        "$T2_BYTECODE_SHA256") printf '%s\n' 'T2_BYTECODE' ;;
        "$T3_SOURCE_SHA256") printf '%s\n' 'T3_SOURCE' ;;
        "$T3_BYTECODE_SHA256") printf '%s\n' 'T3_BYTECODE' ;;
        "$COMBINED_SOURCE_SHA256") printf '%s\n' 'T1_T2_T3_COMBINED_SOURCE' ;;
        "$COMBINED_BYTECODE_SHA256") printf '%s\n' 'T1_T2_T3_COMBINED_BYTECODE' ;;
        *) printf '%s\n' 'UNKNOWN' ;;
    esac
}

emit 'SIGMA_C5V3_LIVE_BINDING_ATTESTATION_R1'
emit 'MODE=READ_ONLY_COLLECTION'
emit 'NETWORK_REQUIRED=NO'
emit 'PRODUCTION_STATE_WRITE=NO'
emit 'PRODUCTION_MUTATION=NO'
emit 'PRODUCTION_RESTART=NO'
emit 'PRODUCTION_BINDING_CHANGE=NO'
emit "ROOT_REQUESTED=$ROOT"

if [ ! -d "$ROOT" ]; then
    emit 'ATTESTATION_COLLECTION=PARTIAL'
    emit 'HOLD=ROOT_NOT_FOUND'
    emit 'LIVE_BINDING_DECISION=REQUIRES_SYNCHRONIZATION_RECONCILIATION'
    exit 0
fi

ROOT_RESOLVED="$(safe_realpath "$ROOT")"
emit "ROOT_RESOLVED=$ROOT_RESOLVED"

emit '--- KNOWN_IDENTITY_TARGETS ---'
emit "KNOWN_PRODUCTION_CORE_SHA256=$PRODUCTION_CORE_SHA256"
emit "KNOWN_PRODUCTION_RUNNER_SHA256=$PRODUCTION_RUNNER_SHA256"
emit "KNOWN_PRODUCTION_INGRESS_SHA256=$PRODUCTION_INGRESS_SHA256"
emit "KNOWN_SIGMAC_SHA256=$SIGMAC_SHA256"
emit "KNOWN_VM_SHA256=$VM_SHA256"
emit "KNOWN_R6_SOURCE_SHA256=$R6_SOURCE_SHA256"
emit "KNOWN_R6_BYTECODE_SHA256=$R6_BYTECODE_SHA256"
emit "KNOWN_T1_SOURCE_SHA256=$T1_SOURCE_SHA256"
emit "KNOWN_T1_BYTECODE_SHA256=$T1_BYTECODE_SHA256"
emit "KNOWN_T2_SOURCE_SHA256=$T2_SOURCE_SHA256"
emit "KNOWN_T2_BYTECODE_SHA256=$T2_BYTECODE_SHA256"
emit "KNOWN_T3_SOURCE_SHA256=$T3_SOURCE_SHA256"
emit "KNOWN_T3_BYTECODE_SHA256=$T3_BYTECODE_SHA256"
emit "KNOWN_COMBINED_SOURCE_SHA256=$COMBINED_SOURCE_SHA256"
emit "KNOWN_COMBINED_BYTECODE_SHA256=$COMBINED_BYTECODE_SHA256"

emit '--- R6_FROZEN_CANDIDATE_PATHS ---'
R6_ROOT="$ROOT/.sigma_c5v3_sync/OFFLINE_PRODUCTION_LINEAGE_LATENT_GRAFT_R6_20260909T184734"
for f in "$R6_ROOT/candidate/core.sigma" "$R6_ROOT/candidate/core.sigmab"; do
    if [ -f "$f" ]; then
        h="$(safe_sha256 "$f" || true)"
        emit "R6_PATH_PRESENT=$f"
        emit "R6_PATH_RESOLVED=$(safe_realpath "$f")"
        emit "R6_PATH_SHA256=${h:-UNREADABLE}"
    else
        emit "R6_PATH_MISSING=$f"
    fi
done

emit '--- STATE_ROOT_DISCOVERY ---'
while IFS= read -r -d '' d; do
    state_root_count=$((state_root_count + 1))
    resolved="$(safe_realpath "$d")"
    meta="$(stat -c '%d:%i:%a:%U:%G' -- "$d" 2>/dev/null || printf '%s' 'STAT_UNAVAILABLE')"
    emit "STATE_ROOT_CANDIDATE=$d"
    emit "STATE_ROOT_RESOLVED=$resolved"
    emit "STATE_ROOT_STAT=$meta"
done < <(find "$ROOT" -xdev -maxdepth 5 -type d \( -name state -o -name STATE \) -print0 2>/dev/null)
emit "STATE_ROOT_CANDIDATE_COUNT=$state_root_count"

emit '--- RELEVANT_SYMLINKS ---'
while IFS= read -r -d '' lnk; do
    target="$(readlink -- "$lnk" 2>/dev/null || true)"
    case "${lnk}|${target}" in
        *core*|*CORE*|*runner*|*RUNNER*|*ingress*|*INGRESS*|*sigmac*|*SIGMAC*|*vm*|*VM*|*state*|*STATE*|*current*|*CURRENT*|*live*|*LIVE*|*prod*|*PROD*)
            emit "SYMLINK=$lnk"
            emit "SYMLINK_TARGET=${target:-UNRESOLVED}"
            emit "SYMLINK_RESOLVED=$(safe_realpath "$lnk")"
            ;;
    esac
done < <(find "$ROOT" -xdev -maxdepth 8 -type l -print0 2>/dev/null)

emit '--- CODE_AND_RUNTIME_CANDIDATE_HASH_SCAN ---'
while IFS= read -r -d '' f; do
    candidate_count=$((candidate_count + 1))
    h="$(safe_sha256 "$f" || true)"
    if [ -z "$h" ]; then
        collection_errors=$((collection_errors + 1))
        emit "CANDIDATE_UNREADABLE=$f"
        continue
    fi
    label="$(known_label_for_hash "$h")"
    emit "CANDIDATE_PATH=$f"
    emit "CANDIDATE_RESOLVED=$(safe_realpath "$f")"
    emit "CANDIDATE_SHA256=$h"
    emit "CANDIDATE_KNOWN_IDENTITY=$label"
    if [ "$label" != 'UNKNOWN' ]; then
        known_match_count=$((known_match_count + 1))
    fi
done < <(
    find "$ROOT" -xdev -maxdepth 10 -type f \
        \( -name 'core.sigma' -o -name 'core.sigmab' -o -name '*.sigma' -o -name '*.sigmab' \
           -o -name 'sigmac' -o -name '*runner*' -o -name '*ingress*' -o -name '*supervisor*' \
           -o -name '*service*' -o -name '*launcher*' -o -name '*launch*' -o -name 'vm' \
           -o -name 'vm.sh' -o -name 'vm.py' -o -name 'sigma_vm' -o -name 'sigma-vm' \) \
        ! -path '*/.git/*' ! -path '*/cache/*' ! -path '*/CACHE/*' -print0 2>/dev/null
)
emit "CANDIDATE_FILE_COUNT=$candidate_count"
emit "KNOWN_IDENTITY_MATCH_COUNT=$known_match_count"

emit '--- STATIC_BINDING_REFERENCE_DISCOVERY ---'
while IFS= read -r -d '' f; do
    [ -r "$f" ] || continue
    grep -Iq . -- "$f" 2>/dev/null || continue
    for key in 'core.sigma' 'core.sigmab' 'sigmac' 'ingress' '/state' '/STATE' '.sigma_c5v3_sync'; do
        if grep -Fq -- "$key" "$f" 2>/dev/null; then
            emit "REFERENCE_FILE=$f"
            emit "REFERENCE_KEY=$key"
        fi
    done
done < <(
    find "$ROOT" -xdev -maxdepth 10 -type f \
        \( -name '*runner*' -o -name '*supervisor*' -o -name '*service*' -o -name '*launcher*' \
           -o -name '*launch*' -o -name '*start*' -o -name '*ingress*' -o -name '*.sh' \) \
        ! -path '*/.git/*' ! -path '*/cache/*' ! -path '*/CACHE/*' -print0 2>/dev/null
)

emit '--- ACTIVE_PROCESS_BINDING_DISCOVERY ---'
if command -v ps >/dev/null 2>&1; then
    while IFS= read -r line; do
        [ -n "$line" ] || continue
        pid="$(printf '%s\n' "$line" | awk '{print $1}')"
        ppid="$(printf '%s\n' "$line" | awk '{print $2}')"
        args="$(printf '%s\n' "$line" | cut -d' ' -f3-)"
        case "$args" in
            *SIGMA*|*sigma*|*sigmac*|*runner*|*RUNNER*|*core.sigma*|*core.sigmab*)
                sigma_process_count=$((sigma_process_count + 1))
                emit "SIGMA_PROCESS_PID=$pid"
                emit "SIGMA_PROCESS_PPID=$ppid"
                if [ -e "/proc/$pid/exe" ]; then
                    exe="$(readlink -f "/proc/$pid/exe" 2>/dev/null || true)"
                    emit "SIGMA_PROCESS_EXE=${exe:-UNRESOLVED}"
                    if [ -n "$exe" ] && [ -f "$exe" ]; then
                        exeh="$(safe_sha256 "$exe" || true)"
                        emit "SIGMA_PROCESS_EXE_SHA256=${exeh:-UNREADABLE}"
                        if [ -n "$exeh" ]; then
                            emit "SIGMA_PROCESS_EXE_KNOWN_IDENTITY=$(known_label_for_hash "$exeh")"
                        fi
                    fi
                fi
                if [ -r "/proc/$pid/cmdline" ]; then
                    while IFS= read -r -d '' tok; do
                        case "$tok" in
                            "$ROOT"/*|"$ROOT")
                                if [ -e "$tok" ]; then
                                    emit "SIGMA_PROCESS_ROOT_ARG=$tok"
                                    if [ -f "$tok" ]; then
                                        th="$(safe_sha256 "$tok" || true)"
                                        emit "SIGMA_PROCESS_ROOT_ARG_SHA256=${th:-UNREADABLE}"
                                        if [ -n "$th" ]; then
                                            emit "SIGMA_PROCESS_ROOT_ARG_KNOWN_IDENTITY=$(known_label_for_hash "$th")"
                                        fi
                                    else
                                        emit "SIGMA_PROCESS_ROOT_ARG_RESOLVED=$(safe_realpath "$tok")"
                                    fi
                                fi
                                ;;
                        esac
                    done < "/proc/$pid/cmdline"
                fi
                ;;
        esac
    done < <(ps -A -o pid=,ppid=,args= 2>/dev/null || ps -ef 2>/dev/null || true)
else
    collection_errors=$((collection_errors + 1))
    emit 'PROCESS_DISCOVERY=PS_UNAVAILABLE'
fi
emit "SIGMA_RELATED_PROCESS_COUNT=$sigma_process_count"
emit 'COGNITIVE_WRITER_PROOF=REQUIRES_SYNCHRONIZATION_RECONCILIATION'

emit '--- GENERIC_DEF_DUPLICATE_SCAN_FOR_KNOWN_CORE_IDENTITIES ---'
while IFS= read -r -d '' f; do
    [ -r "$f" ] || continue
    h="$(safe_sha256 "$f" || true)"
    case "$h" in
        "$PRODUCTION_CORE_SHA256"|"$R6_SOURCE_SHA256")
            emit "DEF_SCAN_CORE=$f"
            emit "DEF_SCAN_CORE_SHA256=$h"
            awk '
                /^[[:space:]]*DEF[[:space:]]+/ {
                    name=$2; count[name]++; total++
                }
                END {
                    dup=0
                    for (n in count) if (count[n] > 1) { print "DEF_DUPLICATE=" n ":" count[n]; dup++ }
                    print "DEF_TOTAL=" (total+0)
                    print "DEF_DUPLICATE_NAME_COUNT=" dup
                }
            ' "$f" 2>/dev/null || {
                collection_errors=$((collection_errors + 1))
                emit "DEF_SCAN_ERROR=$f"
            }
            ;;
    esac
done < <(find "$ROOT" -xdev -maxdepth 10 -type f -name 'core.sigma' ! -path '*/.git/*' -print0 2>/dev/null)

emit '--- ATTESTATION_SUMMARY ---'
if [ "$collection_errors" -eq 0 ]; then
    emit 'ATTESTATION_COLLECTION=COMPLETE'
else
    emit 'ATTESTATION_COLLECTION=PARTIAL'
    emit "ATTESTATION_COLLECTION_ERROR_COUNT=$collection_errors"
fi
emit 'LIVE_BINDING_DECISION=REQUIRES_SYNCHRONIZATION_RECONCILIATION'
emit 'LIVE_BINDING_PASS_NOT_CLAIMED_BY_PROBE=YES'
emit 'CORE_WRITE_ALLOWED_FROM_PROBE_OUTPUT_ALONE=NO'
emit 'PRODUCTION_BINDING=NO'
emit 'PRODUCTION_MUTATION=NO'
