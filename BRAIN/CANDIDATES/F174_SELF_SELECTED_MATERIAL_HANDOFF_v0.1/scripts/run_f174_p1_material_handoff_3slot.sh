#!/usr/bin/env bash
set -euo pipefail

SIGMA_ROOT="${SIGMA_ROOT:-$HOME/SIGMA/sigma_genesis1}"
cd "$SIGMA_ROOT"

RAW_RANKING="${1:-}"
if [[ -z "$RAW_RANKING" || ! -f "$RAW_RANKING" ]]; then
    printf 'Usage: bash %s <sigma-produced-ranking.raw.tsv>\n' "$0" >&2
    printf 'Input must be TSV: material_id<TAB>numeric_score. This script does not sort or choose.\n' >&2
    exit 2
fi

RUN_ID="${RUN_ID:-f174_p1_material_handoff_$(date +%Y%m%d_%H%M%S)}"
BASE="BRAIN/CANDIDATES/F174_SELF_SELECTED_MATERIAL_HANDOFF_v0.1"
TEMPLATE="$BASE/F174_MATERIAL_SELF_SELECTOR_3SLOT_TEMPLATE_v0_2.sigma.tpl"
READBACK_SRC="$BASE/F174_SELECTED_MATERIAL_READBACK_v0_1.sigma"

TMP_DIR=".sigma_tmp/F174_P1_MATERIAL_HANDOFF/$RUN_ID"
AUDIT_DIR=".sigma_audit/F174_P1_MATERIAL_HANDOFF/$RUN_ID"
mkdir -p "$TMP_DIR" "$AUDIT_DIR" ".sigma_exec"

LOG="$AUDIT_DIR/run.log"
exec > >(tee "$LOG") 2>&1

finish() {
    local rc=$?
    printf 'RUN_ID=%s\n' "$RUN_ID"
    printf 'SCRIPT_RC=%s\n' "$rc"
    printf 'AUDIT_DIR=%s\n' "$AUDIT_DIR"
    printf '===== 📤 SIGMA OUTPUT END =====\n'
}
trap finish EXIT

printf '===== 📤 SIGMA OUTPUT BEGIN =====\n'

hash_file() {
    if command -v sha256sum >/dev/null 2>&1; then
        sha256sum "$1" | cut -d ' ' -f 1
    elif command -v shasum >/dev/null 2>&1; then
        shasum -a 256 "$1" | cut -d ' ' -f 1
    else
        printf 'NO_SHA256_TOOL\n' >&2
        return 70
    fi
}

EXPECTED_SIGMAC_SHA="65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
EXPECTED_VM_SHA="029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99"

SIGMAC="${SIGMA_SIGMAC:-./native/sigmac}"
VM="${SIGMA_VM:-./native/sigma-vm.v09_candidate}"
if [[ ! -x "$VM" && -x "./native/sigma-vm" ]]; then
    VM="./native/sigma-vm"
fi

if [[ ! -x "$SIGMAC" ]]; then
    printf 'SIGMAC_NOT_EXECUTABLE=%s\n' "$SIGMAC"
    exit 10
fi
if [[ ! -x "$VM" ]]; then
    printf 'VM_NOT_EXECUTABLE=%s\n' "$VM"
    exit 10
fi
if [[ ! -f "$TEMPLATE" ]]; then
    printf 'TEMPLATE_NOT_FOUND=%s\n' "$TEMPLATE"
    exit 10
fi
if [[ ! -f "$READBACK_SRC" ]]; then
    printf 'READBACK_SRC_NOT_FOUND=%s\n' "$READBACK_SRC"
    exit 10
fi

SIGMAC_SHA="$(hash_file "$SIGMAC")"
VM_SHA="$(hash_file "$VM")"
RAW_SHA="$(hash_file "$RAW_RANKING")"

printf 'RUN_ID=%s\n' "$RUN_ID"
printf 'SIGMA_ROOT=%s\n' "$SIGMA_ROOT"
printf 'RAW_RANKING=%s\n' "$RAW_RANKING"
printf 'RAW_RANKING_SHA256=%s\n' "$RAW_SHA"
printf 'SIGMAC=%s\n' "$SIGMAC"
printf 'SIGMAC_SHA256=%s\n' "$SIGMAC_SHA"
printf 'VM=%s\n' "$VM"
printf 'VM_SHA256=%s\n' "$VM_SHA"
printf 'HOST_ARGMAX_USED=NO\n'
printf 'HOST_SORT_USED=NO\n'
printf 'ASSISTANT_WINNER_USED=NO\n'
printf 'API_USED=NO\n'
printf 'STABLE_GATES_RERUN=NO\n'

if [[ "$SIGMAC_SHA" != "$EXPECTED_SIGMAC_SHA" ]]; then
    printf 'SIGMAC_SHA_MISMATCH_EXPECTED=%s\n' "$EXPECTED_SIGMAC_SHA"
    exit 11
fi
if [[ "$VM_SHA" != "$EXPECTED_VM_SHA" ]]; then
    printf 'VM_SHA_MISMATCH_EXPECTED=%s\n' "$EXPECTED_VM_SHA"
    exit 11
fi

PACKET="$TMP_DIR/ranking_packet.bindings.sigma"
SRC="$TMP_DIR/material_selector.full.sigma"
BIN="$TMP_DIR/material_selector.sigmab"
READBACK_BIN="$TMP_DIR/selected_material_readback.sigmab"
SELECTED_STATE=".sigma_exec/F174_SELECTED_MATERIAL_STATE_v0_1.txt"
SUMMARY="$AUDIT_DIR/summary.txt"

: > "$PACKET"
row_count=0

while IFS=$'\t' read -r material_id score rest || [[ -n "${material_id:-}" ]]; do
    material_id="${material_id//$'\r'/}"
    score="${score//$'\r'/}"

    if [[ -z "$material_id" || "${material_id:0:1}" == "#" ]]; then
        continue
    fi
    if [[ "$material_id" == *'"'* || "$material_id" == *'\\'* ]]; then
        continue
    fi
    if [[ ! "$score" =~ ^-?[0-9]+([.][0-9]+)?$ ]]; then
        continue
    fi

    printf '    ⚡ MATERIAL_ID_%d: "%s";\n' "$row_count" "$material_id" >> "$PACKET"
    printf '    ⚡ MATERIAL_SCORE_%d: %s;\n' "$row_count" "$score" >> "$PACKET"

    row_count=$((row_count + 1))
    if [[ "$row_count" -eq 3 ]]; then
        break
    fi
done < "$RAW_RANKING"

printf 'PACKET_ROWS=%s\n' "$row_count"
if [[ "$row_count" -ne 3 ]]; then
    printf 'PACKET_BUILD_STATUS=INSUFFICIENT_3_VALID_ROWS\n'
    exit 12
fi

PACKET_SHA="$(hash_file "$PACKET")"
printf 'PACKET=%s\n' "$PACKET"
printf 'PACKET_SHA256=%s\n' "$PACKET_SHA"

: > "$SRC"
while IFS= read -r line || [[ -n "$line" ]]; do
    if [[ "$line" == "__SIGMA_PACKET_BINDINGS__" ]]; then
        cat "$PACKET" >> "$SRC"
    else
        printf '%s\n' "$line" >> "$SRC"
    fi
done < "$TEMPLATE"

SRC_SHA="$(hash_file "$SRC")"
printf 'SELECTOR_SOURCE=%s\n' "$SRC"
printf 'SELECTOR_SOURCE_SHA256=%s\n' "$SRC_SHA"

set +e
"$SIGMAC" "$SRC" "$BIN" > "$AUDIT_DIR/compile.stdout" 2> "$AUDIT_DIR/compile.stderr"
COMPILE_RC=$?
set -e

printf 'COMPILE_RC=%s\n' "$COMPILE_RC"
printf 'COMPILE_STDOUT_SHA256=%s\n' "$(hash_file "$AUDIT_DIR/compile.stdout")"
printf 'COMPILE_STDERR_SHA256=%s\n' "$(hash_file "$AUDIT_DIR/compile.stderr")"
if [[ "$COMPILE_RC" -ne 0 ]]; then
    printf 'SELECTOR_COMPILE_STATUS=FAILED_EVIDENCE_CAPTURED\n'
    exit 20
fi

BIN_SHA="$(hash_file "$BIN")"
printf 'SELECTOR_BYTECODE=%s\n' "$BIN"
printf 'SELECTOR_BYTECODE_SHA256=%s\n' "$BIN_SHA"

set +e
"$VM" "$BIN" > "$AUDIT_DIR/vm.stdout" 2> "$AUDIT_DIR/vm.stderr"
VM_RC=$?
set -e

printf 'VM_RC=%s\n' "$VM_RC"
printf 'VM_STDOUT_SHA256=%s\n' "$(hash_file "$AUDIT_DIR/vm.stdout")"
printf 'VM_STDERR_SHA256=%s\n' "$(hash_file "$AUDIT_DIR/vm.stderr")"
if [[ "$VM_RC" -ne 0 ]]; then
    printf 'SELECTOR_VM_STATUS=FAILED_EVIDENCE_CAPTURED\n'
    exit 21
fi

if [[ ! -f "$SELECTED_STATE" ]]; then
    printf 'SELECTED_STATE_FILE_CREATED=NO\n'
    exit 22
fi
SELECTED_SHA="$(hash_file "$SELECTED_STATE")"
printf 'SELECTED_STATE_FILE=%s\n' "$SELECTED_STATE"
printf 'SELECTED_STATE_SHA256=%s\n' "$SELECTED_SHA"

set +e
"$SIGMAC" "$READBACK_SRC" "$READBACK_BIN" > "$AUDIT_DIR/readback_compile.stdout" 2> "$AUDIT_DIR/readback_compile.stderr"
READBACK_COMPILE_RC=$?
set -e

printf 'READBACK_COMPILE_RC=%s\n' "$READBACK_COMPILE_RC"
printf 'READBACK_COMPILE_STDOUT_SHA256=%s\n' "$(hash_file "$AUDIT_DIR/readback_compile.stdout")"
printf 'READBACK_COMPILE_STDERR_SHA256=%s\n' "$(hash_file "$AUDIT_DIR/readback_compile.stderr")"
if [[ "$READBACK_COMPILE_RC" -ne 0 ]]; then
    printf 'READBACK_COMPILE_STATUS=FAILED_EVIDENCE_CAPTURED\n'
    exit 23
fi

set +e
"$VM" "$READBACK_BIN" > "$AUDIT_DIR/readback_vm.stdout" 2> "$AUDIT_DIR/readback_vm.stderr"
READBACK_VM_RC=$?
set -e

printf 'READBACK_VM_RC=%s\n' "$READBACK_VM_RC"
printf 'READBACK_VM_STDOUT_SHA256=%s\n' "$(hash_file "$AUDIT_DIR/readback_vm.stdout")"
printf 'READBACK_VM_STDERR_SHA256=%s\n' "$(hash_file "$AUDIT_DIR/readback_vm.stderr")"
if [[ "$READBACK_VM_RC" -ne 0 ]]; then
    printf 'READBACK_VM_STATUS=FAILED_EVIDENCE_CAPTURED\n'
    exit 24
fi

{
    printf 'RUN_ID=%s\n' "$RUN_ID"
    printf 'RAW_RANKING=%s\n' "$RAW_RANKING"
    printf 'RAW_RANKING_SHA256=%s\n' "$RAW_SHA"
    printf 'PACKET=%s\n' "$PACKET"
    printf 'PACKET_SHA256=%s\n' "$PACKET_SHA"
    printf 'SELECTOR_SOURCE=%s\n' "$SRC"
    printf 'SELECTOR_SOURCE_SHA256=%s\n' "$SRC_SHA"
    printf 'SELECTOR_BYTECODE=%s\n' "$BIN"
    printf 'SELECTOR_BYTECODE_SHA256=%s\n' "$BIN_SHA"
    printf 'SELECTED_STATE_FILE=%s\n' "$SELECTED_STATE"
    printf 'SELECTED_STATE_SHA256=%s\n' "$SELECTED_SHA"
    printf 'COMPILE_RC=%s\n' "$COMPILE_RC"
    printf 'VM_RC=%s\n' "$VM_RC"
    printf 'READBACK_COMPILE_RC=%s\n' "$READBACK_COMPILE_RC"
    printf 'READBACK_VM_RC=%s\n' "$READBACK_VM_RC"
    printf 'HOST_ARGMAX_USED=NO\n'
    printf 'HOST_SORT_USED=NO\n'
    printf 'ASSISTANT_WINNER_USED=NO\n'
    printf 'API_USED=NO\n'
    printf 'STABLE_GATES_RERUN=NO\n'
    printf 'P1_STATUS=EVIDENCE_CAPTURED_REQUIRES_REVIEW\n'
} > "$SUMMARY"

printf 'SUMMARY=%s\n' "$SUMMARY"
printf 'P1_SCRIPT_STATUS=EVIDENCE_CAPTURED_REQUIRES_REVIEW\n'
