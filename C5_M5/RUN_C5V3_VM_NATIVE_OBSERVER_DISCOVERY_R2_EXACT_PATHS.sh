#!/data/data/com.termux/files/usr/bin/bash
set -u

# C5V3 VM Native Observer Discovery R2 — exact paths only.
# Read-only/static inspection. No directory walk, no find, no grep -R,
# no VM/core execution, no network, no package action, no production write.

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
VM="$ROOT/native/sigma-vm.v09_candidate"
SIGMAC="$ROOT/native/sigmac"
RUNNER="$ROOT/.sigma_c5/control/RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh"

EXPECTED_VM_SHA256="029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99"
EXPECTED_SIGMAC_SHA256="65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
EXPECTED_RUNNER_SHA256="092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847"

hash1() {
  sha256sum "$1" 2>/dev/null | awk '{print $1}'
}

size1() {
  if command -v stat >/dev/null 2>&1; then
    stat -c '%s' "$1" 2>/dev/null || printf 'UNKNOWN'
  else
    printf 'UNKNOWN'
  fi
}

printf '%s\n' '=== C5V3 VM NATIVE OBSERVER DISCOVERY R2 EXACT PATHS ==='
printf 'ROOT=%s\n' "$ROOT"
printf 'SCOPE=EXACT_PATHS_ONLY\n'
printf 'DIRECTORY_WALK=NO\n'
printf 'FIND=NO\n'
printf 'GREP_RECURSIVE=NO\n'
printf 'NETWORK=NO\n'
printf 'PACKAGE_ACTION=NO\n'
printf 'VM_EXECUTION=NO\n'
printf 'CORE_EXECUTION=NO\n'
printf 'STATE_WRITE=NO\n'
printf 'PRODUCTION_MUTATION=NO\n'
printf 'PRODUCTION_BINDING=NO\n'

printf '%s\n' '=== 1. EXACT TARGETS ==='
printf 'TARGET_VM=%s\n' "$VM"
printf 'TARGET_SIGMAC=%s\n' "$SIGMAC"
printf 'TARGET_RUNNER=%s\n' "$RUNNER"

IDENTITY_OK=YES

printf '%s\n' '=== 2. EXACT IDENTITY LOCK ==='
if [ -f "$VM" ]; then
  VM_SHA=$(hash1 "$VM")
  printf 'VM_SIZE_BYTES=%s\n' "$(size1 "$VM")"
  printf 'VM_SHA256=%s\n' "$VM_SHA"
  if [ "$VM_SHA" = "$EXPECTED_VM_SHA256" ]; then
    printf 'VM_IDENTITY=PASS\n'
  else
    printf 'VM_IDENTITY=HOLD_MISMATCH\n'
    IDENTITY_OK=NO
  fi
else
  printf 'VM_IDENTITY=HOLD_MISSING\n'
  IDENTITY_OK=NO
fi

if [ -f "$SIGMAC" ]; then
  SIGMAC_SHA=$(hash1 "$SIGMAC")
  printf 'SIGMAC_SIZE_BYTES=%s\n' "$(size1 "$SIGMAC")"
  printf 'SIGMAC_SHA256=%s\n' "$SIGMAC_SHA"
  if [ "$SIGMAC_SHA" = "$EXPECTED_SIGMAC_SHA256" ]; then
    printf 'SIGMAC_IDENTITY=PASS\n'
  else
    printf 'SIGMAC_IDENTITY=HOLD_MISMATCH\n'
    IDENTITY_OK=NO
  fi
else
  printf 'SIGMAC_IDENTITY=HOLD_MISSING\n'
  IDENTITY_OK=NO
fi

if [ -f "$RUNNER" ]; then
  RUNNER_SHA=$(hash1 "$RUNNER")
  printf 'RUNNER_SIZE_BYTES=%s\n' "$(size1 "$RUNNER")"
  printf 'RUNNER_SHA256=%s\n' "$RUNNER_SHA"
  if [ "$RUNNER_SHA" = "$EXPECTED_RUNNER_SHA256" ]; then
    printf 'RUNNER_IDENTITY=PASS\n'
  else
    printf 'RUNNER_IDENTITY=HOLD_MISMATCH\n'
    IDENTITY_OK=NO
  fi
else
  printf 'RUNNER_IDENTITY=HOLD_MISSING\n'
  IDENTITY_OK=NO
fi

if [ "$IDENTITY_OK" != YES ]; then
  printf '%s\n' '=== 3. FAIL-CLOSED ==='
  printf 'OBSERVER_DISCOVERY_SKIPPED=RUNTIME_IDENTITY_NOT_LOCKED\n'
  printf 'R11_ACTIVATION_PASS_NOT_CLAIMED=YES\n'
  printf 'PRODUCTION_BINDING=NO\n'
  printf 'PRODUCTION_MUTATION=NO\n'
  printf '%s\n' '=== END ==='
  exit 0
fi

printf '%s\n' '=== 3. EXACT VM OBSERVER-RELATED ASCII TOKENS ==='
if command -v strings >/dev/null 2>&1; then
  strings "$VM" 2>/dev/null \
    | grep -E -i 'trace|debug|opcode|instruction|dispatch|host.?call|host.?op|profile|dump|step|event|observer|SIGMA_[A-Z0-9_]*(TRACE|DEBUG|DUMP|PROFILE|STEP|DISPATCH|HOST|EVENT)' \
    | head -n 200 \
    || true
else
  printf 'STRINGS_AVAILABLE=NO\n'
fi

printf '%s\n' '=== 4. EXACT VM SYMBOL HINTS IF READELF EXISTS ==='
if command -v readelf >/dev/null 2>&1; then
  printf 'READELF_AVAILABLE=YES\n'
  readelf -Ws "$VM" 2>/dev/null \
    | grep -E -i 'trace|debug|opcode|instruction|dispatch|host|profile|dump|step|event|observer' \
    | head -n 200 \
    || true
else
  printf 'READELF_AVAILABLE=NO\n'
fi

printf '%s\n' '=== 5. EXACT RUNNER OBSERVER REFERENCES ==='
grep -nE -i 'trace|debug|opcode|instruction|dispatch|host.?call|host.?op|profile|dump|SIGMA_MAX_STEPS|observer' "$RUNNER" 2>/dev/null || true

printf '%s\n' '=== 6. DECISION BOUNDARY ==='
printf 'EXACT_FILES_READ_COUNT=3_IDENTITY_PLUS_VM_ANALYSIS\n'
printf 'OTHER_NATIVE_FILES_READ=NO\n'
printf 'OTHER_CONTROL_FILES_READ=NO\n'
printf 'STATE_TREE_READ=NO\n'
printf 'OBSERVER_DISCOVERY_RESULT=REQUIRES_SYNCHRONY_RECONCILIATION\n'
printf 'OBSERVER_PASS_NOT_CLAIMED_BY_PROBE=YES\n'
printf 'R11_ACTIVATION_PASS_NOT_CLAIMED=YES\n'
printf 'CORE_WRITE_ALLOWED_FROM_OUTPUT_ALONE=NO\n'
printf 'VM_PATCH_ALLOWED_FROM_OUTPUT_ALONE=NO\n'
printf 'PRODUCTION_BINDING=NO\n'
printf 'PRODUCTION_MUTATION=NO\n'
printf '%s\n' '=== END ==='
