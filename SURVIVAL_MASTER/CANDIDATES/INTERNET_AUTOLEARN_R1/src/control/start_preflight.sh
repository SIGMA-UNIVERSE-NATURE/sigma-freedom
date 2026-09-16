#!/usr/bin/env bash
set -euo pipefail
umask 077
hold(){ printf 'HOLD=%s\n' "$1"; exit 2; }
sha(){ sha256sum "$1" | awk '{print $1}'; }
HERE="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
ROOT="${ROOT:-$HOME/SIGMA/sigma_genesis1}"

[ "${SURVIVAL_REVIEW_VERDICT:-}" = APPROVE_FOR_OPPO_PREFLIGHT_ONLY ] || hold SURVIVAL_MASTER_PREFLIGHT_APPROVAL_MISSING
"$HERE/control/session_guard.sh"
"$HERE/verify/manifest_verify.sh"
[ "$(sha "$ROOT/native/sigmac")" = 65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71 ] || hold SIGMAC_SHA256_MISMATCH
[ "$(sha "$ROOT/native/sigma-vm.v09_candidate")" = 029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99 ] || hold VM_SHA256_MISMATCH

# Exact native dependency bytes/interfaces are deliberately not guessed by this package.
# A reviewer-approved dependency-resolution receipt must exist before any native runtime step.
DEP_RECEIPT="${SIGMA_DEPENDENCY_RECEIPT:-}"
[ -n "$DEP_RECEIPT" ] || hold EXACT_NATIVE_DEPENDENCY_RECEIPT_REQUIRED
[ -f "$DEP_RECEIPT" ] || hold EXACT_NATIVE_DEPENDENCY_RECEIPT_MISSING
grep -Fqx 'EXACT_NATIVE_DEPENDENCIES_VERIFIED=YES' "$DEP_RECEIPT" || hold EXACT_NATIVE_DEPENDENCIES_NOT_VERIFIED
grep -Fqx 'GENERAL_ARBITRARY_WEBSITE_NATIVE_SELECTION=PROVEN_FOR_THIS_INTERFACE' "$DEP_RECEIPT" || hold GENERAL_NATIVE_SELECTION_INTERFACE_NOT_PROVEN
grep -Fqx 'NATIVE_CONDENSER_INTERFACE=PROVEN_FOR_THIS_INTERFACE' "$DEP_RECEIPT" || hold NATIVE_CONDENSER_INTERFACE_NOT_PROVEN

printf 'OPPO_PREFLIGHT_ENTRY_GUARDS=PASS\n'
printf 'PRODUCTION_ENABLEMENT=NO\n'
printf 'NEXT=REVIEWER_CONTROLLED_NATIVE_COMPILE_AND_DYNAMIC_PREFLIGHT_ONLY\n'
