#!/data/data/com.termux/files/usr/bin/bash
set -u

# C5V3 VM Native Observer Discovery R1
# Read-only/static discovery only.
# No core/VM/state mutation, no restart, no network, no package action.

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
VM="$ROOT/native/sigma-vm.v09_candidate"
SIGMAC="$ROOT/native/sigmac"
INSTALL="$ROOT/.sigma_c5"
RUNNER="$INSTALL/control/RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh"

EXPECTED_VM_SHA256="029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99"
EXPECTED_SIGMAC_SHA256="65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
EXPECTED_RUNNER_SHA256="092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847"

hash1() {
  sha256sum "$1" 2>/dev/null | awk '{print $1}'
}

printf '%s\n' '=== C5V3 VM NATIVE OBSERVER DISCOVERY R1 ==='
printf 'ROOT=%s\n' "$ROOT"
printf 'MODE=READ_ONLY_STATIC_DISCOVERY\n'
printf 'NETWORK=NO\n'
printf 'PACKAGE_ACTION=NO\n'
printf 'CORE_EXECUTION=NO\n'
printf 'VM_EXECUTION=NO\n'
printf 'STATE_WRITE=NO\n'
printf 'PRODUCTION_MUTATION=NO\n'
printf 'PRODUCTION_BINDING=NO\n'

printf '%s\n' '=== 1. LOCKED RUNTIME IDENTITIES ==='
if [ -f "$VM" ]; then
  VM_SHA=$(hash1 "$VM")
  printf 'VM=%s\nVM_SHA256=%s\n' "$VM" "$VM_SHA"
  if [ "$VM_SHA" = "$EXPECTED_VM_SHA256" ]; then
    printf 'VM_IDENTITY=PASS\n'
  else
    printf 'VM_IDENTITY=HOLD_MISMATCH\n'
  fi
else
  printf 'VM=MISSING\nVM_IDENTITY=HOLD_MISSING\n'
fi

if [ -f "$SIGMAC" ]; then
  SIGMAC_SHA=$(hash1 "$SIGMAC")
  printf 'SIGMAC=%s\nSIGMAC_SHA256=%s\n' "$SIGMAC" "$SIGMAC_SHA"
  if [ "$SIGMAC_SHA" = "$EXPECTED_SIGMAC_SHA256" ]; then
    printf 'SIGMAC_IDENTITY=PASS\n'
  else
    printf 'SIGMAC_IDENTITY=HOLD_MISMATCH\n'
  fi
else
  printf 'SIGMAC=MISSING\nSIGMAC_IDENTITY=HOLD_MISSING\n'
fi

if [ -f "$RUNNER" ]; then
  RUNNER_SHA=$(hash1 "$RUNNER")
  printf 'RUNNER=%s\nRUNNER_SHA256=%s\n' "$RUNNER" "$RUNNER_SHA"
  if [ "$RUNNER_SHA" = "$EXPECTED_RUNNER_SHA256" ]; then
    printf 'RUNNER_IDENTITY=PASS\n'
  else
    printf 'RUNNER_IDENTITY=HOLD_MISMATCH\n'
  fi
else
  printf 'RUNNER=MISSING\nRUNNER_IDENTITY=HOLD_MISSING\n'
fi

printf '%s\n' '=== 2. NATIVE DIRECTORY SHALLOW INVENTORY ==='
if [ -d "$ROOT/native" ]; then
  for f in "$ROOT"/native/*; do
    [ -e "$f" ] || continue
    if [ -f "$f" ]; then
      printf 'NATIVE_FILE=%s SHA256=%s\n' "$f" "$(hash1 "$f")"
    elif [ -L "$f" ]; then
      printf 'NATIVE_SYMLINK=%s TARGET=%s\n' "$f" "$(readlink "$f" 2>/dev/null || true)"
    fi
  done
else
  printf 'NATIVE_DIRECTORY=MISSING\n'
fi

printf '%s\n' '=== 3. VM ASCII OBSERVER/TRACE TOKENS ==='
if [ -f "$VM" ]; then
  if command -v strings >/dev/null 2>&1; then
    strings "$VM" 2>/dev/null \
      | grep -E -i 'trace|debug|opcode|instruction|dispatch|host.?call|host.?op|profile|dump|step|event|log|observer' \
      | head -n 250 \
      || true
  else
    printf 'STRINGS_AVAILABLE=NO\n'
    LC_ALL=C grep -aEo -i '[A-Za-z0-9_./:-]{0,40}(trace|debug|opcode|instruction|dispatch|host.?call|host.?op|profile|dump|step|event|log|observer)[A-Za-z0-9_./:-]{0,80}' "$VM" 2>/dev/null \
      | head -n 250 \
      || true
  fi
fi

printf '%s\n' '=== 4. VM FLAG-LIKE TOKENS ==='
if [ -f "$VM" ]; then
  if command -v strings >/dev/null 2>&1; then
    strings "$VM" 2>/dev/null | grep -E -- '--[A-Za-z0-9][A-Za-z0-9_-]{1,60}' | sort -u | head -n 200 || true
  else
    printf 'FLAG_SCAN=SKIPPED_NO_STRINGS\n'
  fi
fi

printf '%s\n' '=== 5. VM SIGMA ENV-LIKE TOKENS ==='
if [ -f "$VM" ]; then
  if command -v strings >/dev/null 2>&1; then
    strings "$VM" 2>/dev/null | grep -Eo 'SIGMA_[A-Z0-9_]{2,80}' | sort -u | head -n 250 || true
  else
    printf 'ENV_TOKEN_SCAN=SKIPPED_NO_STRINGS\n'
  fi
fi

printf '%s\n' '=== 6. ELF/SYMBOL OBSERVER HINTS IF TOOLS EXIST ==='
if [ -f "$VM" ]; then
  if command -v readelf >/dev/null 2>&1; then
    printf 'READELF_AVAILABLE=YES\n'
    readelf -Ws "$VM" 2>/dev/null \
      | grep -E -i 'trace|debug|opcode|instruction|dispatch|host|profile|dump|step|event|log|observer' \
      | head -n 250 \
      || true
  else
    printf 'READELF_AVAILABLE=NO\n'
  fi

  if command -v objdump >/dev/null 2>&1; then
    printf 'OBJDUMP_AVAILABLE=YES\n'
    objdump -t "$VM" 2>/dev/null \
      | grep -E -i 'trace|debug|opcode|instruction|dispatch|host|profile|dump|step|event|log|observer' \
      | head -n 250 \
      || true
  else
    printf 'OBJDUMP_AVAILABLE=NO\n'
  fi
fi

printf '%s\n' '=== 7. RUNNER OBSERVER/DEBUG REFERENCES ==='
if [ -f "$RUNNER" ]; then
  grep -nE -i 'trace|debug|opcode|instruction|dispatch|host.?call|profile|dump|SIGMA_MAX_STEPS|step|observer' "$RUNNER" 2>/dev/null || true
fi

printf '%s\n' '=== 8. CONTROL-SCRIPT OBSERVER REFERENCES ==='
if [ -d "$INSTALL/control" ]; then
  for f in "$INSTALL"/control/*; do
    [ -f "$f" ] || continue
    HITS=$(grep -nE -i 'trace|debug|opcode|instruction|dispatch|host.?call|profile|dump|SIGMA_MAX_STEPS|observer' "$f" 2>/dev/null | head -n 40 || true)
    if [ -n "$HITS" ]; then
      printf 'CONTROL_FILE=%s\n' "$f"
      printf '%s\n' "$HITS"
    fi
  done
fi

printf '%s\n' '=== 9. DISCOVERY DECISION BOUNDARY ==='
printf 'OBSERVER_DISCOVERY_RESULT=REQUIRES_SYNCHRONY_RECONCILIATION\n'
printf 'OBSERVER_PASS_NOT_CLAIMED_BY_PROBE=YES\n'
printf 'R11_ACTIVATION_PASS_NOT_CLAIMED=YES\n'
printf 'CORE_WRITE_ALLOWED_FROM_OUTPUT_ALONE=NO\n'
printf 'VM_PATCH_ALLOWED_FROM_OUTPUT_ALONE=NO\n'
printf 'PRODUCTION_BINDING=NO\n'
printf 'PRODUCTION_MUTATION=NO\n'
printf '%s\n' '=== END ==='
