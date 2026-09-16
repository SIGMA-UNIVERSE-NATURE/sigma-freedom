#!/usr/bin/env bash
set -euo pipefail
HERE="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
printf 'raw bytes\n' > "$TMP/raw"
printf 'native bytes\n' > "$TMP/native"
printf 'OWNER=SIGMA_NATIVE_VM\nACTION=SEAL_NATIVE_OUTPUT\nCANONICAL_MUTATION=NO\n' > "$TMP/event"
printf '{"transport":"mechanical"}\n' > "$TMP/receipt"
A="$(python3 "$HERE/host/seal_queue.py" --queue-root "$TMP/q" --raw-content "$TMP/raw" --native-output "$TMP/native" --native-event "$TMP/event" --transport-receipt "$TMP/receipt" --native-input-sha256 "$(sha256sum "$TMP/raw"|awk '{print $1}')" --native-output-mode TEST_NATIVE_BYTES)"
B="$(python3 "$HERE/host/seal_queue.py" --queue-root "$TMP/q" --raw-content "$TMP/raw" --native-output "$TMP/native" --native-event "$TMP/event" --transport-receipt "$TMP/receipt" --native-input-sha256 "$(sha256sum "$TMP/raw"|awk '{print $1}')" --native-output-mode TEST_NATIVE_BYTES)"
printf '%s\n%s\n' "$A" "$B"
printf '%s\n' "$A" | grep -Fq 'QUEUE_COMMIT=PASS'
printf '%s\n' "$B" | grep -Fq 'QUEUE_COMMIT=IDEMPOTENT_REUSE'
COUNT="$(find "$TMP/q/sealed" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')"
[ "$COUNT" -eq 1 ]
[ -z "$(find "$TMP/q/staging" -mindepth 1 -maxdepth 1 -type d -name '*.partial.*' -print -quit)" ]
printf 'MECHANICAL_RECOVERY_IDEMPOTENCY_VERIFY=PASS\n'
