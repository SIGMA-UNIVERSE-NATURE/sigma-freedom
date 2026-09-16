#!/usr/bin/env bash
set -euo pipefail

# Mechanical session-transfer helper only.
# It does not implement SIGMA cognition, learning, semantic scoring, or canonical mutation.

EXPECTED_SESSION_CODE="S346B02B82354"
EXPECTED_RUN_ID="SESSION_S346B02B82354"
EXPECTED_ARTIFACT_ROOT="/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_ail/coordination/SESSION_R4/WORKSPACES/S346B02B82354/artifacts"

FROZEN_SESSION_CODE="SF07900DEB302"
FROZEN_SOURCE_SHA256="f00d09b2eeb96adfeb9f2db300806a6355c120baab9da434e84129ed3b9ef451"
FROZEN_RUNNER_SHA256="fff2987e9a2144bbf2755de366df5bf71ae8d0d3af8aaad88d0552b118b6fee3"
FROZEN_MANIFEST_SHA256="b731bf8a15c361e26d935f64d2b50d5f5f2fb9c5239c032853d591245501c17c"
FROZEN_BYTECODE_SHA256="04fca906804778f7660b2e5a70c885f1b8e7ac55158d51be26f7fd27e204b323"
FROZEN_BUNDLE_SHA256="3f0c53fd57b74ff52704de521fad55ff4bcfaafb9e3770c0350b201e551d8b51"

SOURCE_NAME="SIGMA_G3C_EVIDENCE_PROFILE_R3H_CANDIDATE.sigma"
RUNNER_NAME="RUN_G3C_R3H.sh"
MANIFEST_NAME="MANIFEST.sha256"
BUNDLE_NAME="SIGMA_G3C_EVIDENCE_PROFILE_R3H_CANDIDATE"

die() {
  printf 'HOLD=%s\n' "$1" >&2
  return "${2:-1}"
}

sha_of() {
  sha256sum "$1" | awk '{print $1}'
}

verify_file_hash() {
  local file="$1"
  local expected="$2"
  local label="$3"
  local got
  [[ -f "$file" ]] || { die "${label}_MISSING" 20; return $?; }
  got="$(sha_of "$file")"
  printf '%s=%s\n' "${label}_SHA256" "$got"
  [[ "$got" == "$expected" ]] || { die "${label}_HASH_MISMATCH" 21; return $?; }
}

find_hash_match() {
  local root="$1"
  local expected="$2"
  local file got
  while IFS= read -r -d '' file; do
    got="$(sha_of "$file")"
    if [[ "$got" == "$expected" ]]; then
      printf '%s\n' "$file"
      return 0
    fi
  done < <(find "$root" -type f -print0)
  return 1
}

verify_bundle_dir() {
  local dir="$1"
  local bytecode_match
  verify_file_hash "$dir/$SOURCE_NAME" "$FROZEN_SOURCE_SHA256" "SOURCE"
  verify_file_hash "$dir/$RUNNER_NAME" "$FROZEN_RUNNER_SHA256" "RUNNER"
  verify_file_hash "$dir/$MANIFEST_NAME" "$FROZEN_MANIFEST_SHA256" "MANIFEST"

  bytecode_match="$(find_hash_match "$dir" "$FROZEN_BYTECODE_SHA256" || true)"
  [[ -n "$bytecode_match" ]] || { die "BYTECODE_HASH_NOT_FOUND_IN_BUNDLE" 22; return $?; }
  printf 'BYTECODE_MATCH=%s\n' "$bytecode_match"

  if (cd "$dir" && sha256sum -c "$MANIFEST_NAME" >/dev/null 2>&1); then
    printf 'MANIFEST_INTERNAL_VERIFY=PASS\n'
  else
    # The manifest identity itself is frozen, but its paths may be packaging-relative.
    # Fail closed instead of rewriting the manifest.
    die "MANIFEST_INTERNAL_VERIFY_FAIL" 23
    return $?
  fi
}

main() {
  local root old_artroot src_bundle dst_bundle tmp_dir receipt receipt_tmp receipt_sha
  local src_bytecode dst_bytecode source_run

  if ! declare -F sigma-session >/dev/null 2>&1; then
    die "SIGMA_SESSION_FUNCTION_NOT_LOADED" 10
    return $?
  fi

  printf '%s\n' '--- SIGMA SESSION STATUS ---'
  sigma-session status
  printf '%s\n' '--- END SESSION STATUS ---'

  [[ "${SESSION_CODE:-}" == "$EXPECTED_SESSION_CODE" ]] || { die "SESSION_CODE_MISMATCH_EXPECTED_${EXPECTED_SESSION_CODE}" 11; return $?; }
  if [[ -n "${RUN_ID:-}" ]]; then
    [[ "$RUN_ID" == "$EXPECTED_RUN_ID" ]] || { die "RUN_ID_MISMATCH_EXPECTED_${EXPECTED_RUN_ID}" 12; return $?; }
  fi
  [[ "${ARTIFACT_ROOT:-}" == "$EXPECTED_ARTIFACT_ROOT" ]] || { die "ARTIFACT_ROOT_MISMATCH" 13; return $?; }

  root="$HOME/SIGMA/sigma_genesis1"
  old_artroot="$root/.sigma_ail/coordination/SESSION_R4/WORKSPACES/$FROZEN_SESSION_CODE/artifacts"
  src_bundle="$old_artroot/$BUNDLE_NAME"
  dst_bundle="$EXPECTED_ARTIFACT_ROOT/$BUNDLE_NAME"
  source_run="$old_artroot/SIGMA_G3C_STATE_TRACKING_PILOT_R2_FIX1_FULL_CONTROLS_CANDIDATE/runs/sigma_curriculum_with_replay_seed130363_20260915_234242_14859"

  [[ -d "$src_bundle" ]] || { die "FROZEN_R3H_BUNDLE_MISSING" 30; return $?; }
  [[ -d "$source_run" ]] || { die "SEED130363_SOURCE_RUN_MISSING" 31; return $?; }
  mkdir -p "$EXPECTED_ARTIFACT_ROOT"

  printf 'TRANSFER_MODE=EXACT_BYTES_COPY_ONLY\n'
  printf 'CANONICAL_MUTATION=NO\n'
  printf 'HOST_COGNITION=NO\n'
  printf 'FROZEN_BUNDLE_DECLARED_SHA256=%s\n' "$FROZEN_BUNDLE_SHA256"
  printf 'SOURCE_BUNDLE=%s\n' "$src_bundle"
  printf 'DEST_BUNDLE=%s\n' "$dst_bundle"
  printf 'SEED130363_SOURCE_RUN=%s\n' "$source_run"

  printf '%s\n' '--- VERIFY FROZEN SOURCE BUNDLE ---'
  verify_bundle_dir "$src_bundle"

  if [[ -e "$dst_bundle" ]]; then
    [[ -d "$dst_bundle" ]] || { die "DESTINATION_EXISTS_NOT_DIRECTORY" 32; return $?; }
    printf 'DESTINATION_ALREADY_EXISTS=YES\n'
    printf '%s\n' '--- VERIFY EXISTING DESTINATION ---'
    verify_bundle_dir "$dst_bundle"
    printf 'DESTINATION_REUSED_WITHOUT_OVERWRITE=YES\n'
  else
    tmp_dir="$EXPECTED_ARTIFACT_ROOT/.${BUNDLE_NAME}.transfer.$$"
    if [[ -e "$tmp_dir" ]]; then
      die "TRANSFER_TEMP_ALREADY_EXISTS" 33
      return $?
    fi
    mkdir "$tmp_dir"
    trap 'rm -rf -- "${tmp_dir:-}"' RETURN

    cp -a "$src_bundle/." "$tmp_dir/"
    printf '%s\n' '--- VERIFY TEMP COPY ---'
    verify_bundle_dir "$tmp_dir"

    mv "$tmp_dir" "$dst_bundle"
    tmp_dir=""
    trap - RETURN

    printf 'EXACT_BYTES_COPY_COMPLETE=YES\n'
    printf '%s\n' '--- VERIFY FINAL DESTINATION ---'
    verify_bundle_dir "$dst_bundle"
  fi

  src_bytecode="$(find_hash_match "$src_bundle" "$FROZEN_BYTECODE_SHA256")"
  dst_bytecode="$(find_hash_match "$dst_bundle" "$FROZEN_BYTECODE_SHA256")"

  receipt="$EXPECTED_ARTIFACT_ROOT/G3C_R3H_SESSION_${EXPECTED_SESSION_CODE}_TRANSFER_RECEIPT.txt"
  receipt_tmp="${receipt}.tmp.$$"

  {
    printf 'RESULT=G3C_R3H_FROZEN_BUNDLE_SESSION_TRANSFER_COMPLETE\n'
    printf 'SYSTEM_IDENTITY=SIGMA.AIL\n'
    printf 'SESSION_CODE=%s\n' "$EXPECTED_SESSION_CODE"
    printf 'RUN_ID=%s\n' "$EXPECTED_RUN_ID"
    printf 'ACCESS=READ_PLUS_ARTIFACT_WRITE\n'
    printf 'ARTIFACT_ROOT=%s\n' "$EXPECTED_ARTIFACT_ROOT"
    printf 'CANONICAL_MUTATION=NO\n'
    printf 'HOST_COGNITION=NO\n'
    printf 'TRANSFER_MODE=EXACT_BYTES_COPY_ONLY\n'
    printf 'FROM_SESSION=%s\n' "$FROZEN_SESSION_CODE"
    printf 'SOURCE_BUNDLE=%s\n' "$src_bundle"
    printf 'DEST_BUNDLE=%s\n' "$dst_bundle"
    printf 'FROZEN_BUNDLE_DECLARED_SHA256=%s\n' "$FROZEN_BUNDLE_SHA256"
    printf 'SOURCE_SHA256=%s\n' "$(sha_of "$dst_bundle/$SOURCE_NAME")"
    printf 'RUNNER_SHA256=%s\n' "$(sha_of "$dst_bundle/$RUNNER_NAME")"
    printf 'MANIFEST_SHA256=%s\n' "$(sha_of "$dst_bundle/$MANIFEST_NAME")"
    printf 'BYTECODE_SHA256=%s\n' "$FROZEN_BYTECODE_SHA256"
    printf 'SOURCE_BYTECODE_MATCH=%s\n' "$src_bytecode"
    printf 'DEST_BYTECODE_MATCH=%s\n' "$dst_bytecode"
    printf 'SEED130363_SOURCE_RUN=%s\n' "$source_run"
    printf 'BLIND_USED=NO\n'
    printf 'SEALED_R4_USED=NO\n'
    printf 'R3H_RUNTIME_EXECUTED_BY_THIS_TRANSFER=NO\n'
    printf 'G3_PROMOTION=NO\n'
  } > "$receipt_tmp"

  mv "$receipt_tmp" "$receipt"
  receipt_sha="$(sha_of "$receipt")"

  printf 'TRANSFER_RECEIPT=%s\n' "$receipt"
  printf 'TRANSFER_RECEIPT_SHA256=%s\n' "$receipt_sha"
  printf 'RESULT=PASS_EXACT_FROZEN_BYTES_COPIED_TO_SESSION_ARTIFACT_ROOT\n'
  printf 'NEXT_RUNTIME_GATE=G3C_R3H_EVIDENCE_PROFILE_READOUT_DEV_ONLY_SEED130363\n'
}

main "$@"
