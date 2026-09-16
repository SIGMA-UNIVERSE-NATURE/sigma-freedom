#!/usr/bin/env bash
set -euo pipefail
umask 077
hold(){ printf 'HOLD=%s\n' "$1"; exit 2; }
kv(){ awk -F= -v K="$1" '$1==K{sub(/^[^=]*=/,"");print;exit}' "$2"; }
sha(){ sha256sum "$1" | awk '{print $1}'; }

# Mechanical worker only. It never chooses a semantic action. It requires the exact
# already-recorded native event and dispatches only its mechanical operation class.
[ "$#" -eq 1 ] || hold DESCRIPTOR_ARGUMENT_REQUIRED
DESC="$1"
EVENT="$(kv NATIVE_EVENT_PATH "$DESC")"
[ -f "$EVENT" ] || hold NATIVE_EVENT_MISSING
OWNER="$(kv OWNER "$EVENT")"
ACTION="$(kv ACTION "$EVENT")"
CANON="$(kv CANONICAL_MUTATION "$EVENT")"
PAYLOAD="$(kv PAYLOAD_PATH "$EVENT")"
PAYLOAD_SHA="$(kv PAYLOAD_SHA256 "$EVENT")"
[ "$OWNER" = SIGMA_NATIVE_VM ] || hold NATIVE_EVENT_OWNER_MISMATCH
[ "$CANON" = NO ] || hold NATIVE_EVENT_REQUESTS_CANONICAL_MUTATION
[ -f "$PAYLOAD" ] || hold NATIVE_EVENT_PAYLOAD_MISSING
[ "$(sha "$PAYLOAD")" = "$PAYLOAD_SHA" ] || hold NATIVE_EVENT_PAYLOAD_HASH_MISMATCH

case "$ACTION" in
  HTTP_GET|HTTP_HEAD|SEAL_NATIVE_OUTPUT|NOOP_COMPLETE)
    printf 'MECHANICAL_ACTION_ACCEPTED=%s\n' "$ACTION"
    ;;
  *) hold UNKNOWN_MECHANICAL_ACTION_CLASS ;;
esac

# This generic candidate deliberately stops here until exact native dependency
# interfaces are resolved and reviewed. It does not guess how to invoke them.
hold UNRESOLVED_EXACT_NATIVE_CONTROLLER_INTERFACE
