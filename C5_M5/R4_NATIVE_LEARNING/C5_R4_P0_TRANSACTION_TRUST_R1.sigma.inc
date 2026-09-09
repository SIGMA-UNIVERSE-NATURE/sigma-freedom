# C5V3 R4 transaction trust/state substrate R1.
# Mechanical trust only. No cognition, source choice, query generation, capability choice, or learning decisions.

DEF p0r4_H(op, a, b, c) {
    RETURN host(op, a, b, c);
}

DEF p0r4_safe_atom(value, max_len) {
    IF (value == "") { RETURN 0; }
    IF (max_len < p0r4_H("str_len", value, NULL, NULL)) { RETURN 0; }
    ⚡ X: p0r4_H("str_replace", value, "\n", "");
    IF (X != value) { RETURN 0; }
    ⚡ X: p0r4_H("str_replace", value, "\r", "");
    IF (X != value) { RETURN 0; }
    ⚡ X: p0r4_H("str_replace", value, "\t", "");
    IF (X != value) { RETURN 0; }
    ⚡ X: p0r4_H("str_replace", value, "=", "");
    IF (X != value) { RETURN 0; }
    ⚡ X: p0r4_H("str_replace", value, " || ", "");
    IF (X != value) { RETURN 0; }
    RETURN 1;
}

DEF p0r4_hex64(value) {
    IF (p0r4_H("str_len", value, NULL, NULL) != 64) { RETURN 0; }
    ⚡ REST: p0r4_H("str_lower", value, NULL, NULL);
    ⚡ REST: p0r4_H("str_replace", REST, "0", "");
    ⚡ REST: p0r4_H("str_replace", REST, "1", "");
    ⚡ REST: p0r4_H("str_replace", REST, "2", "");
    ⚡ REST: p0r4_H("str_replace", REST, "3", "");
    ⚡ REST: p0r4_H("str_replace", REST, "4", "");
    ⚡ REST: p0r4_H("str_replace", REST, "5", "");
    ⚡ REST: p0r4_H("str_replace", REST, "6", "");
    ⚡ REST: p0r4_H("str_replace", REST, "7", "");
    ⚡ REST: p0r4_H("str_replace", REST, "8", "");
    ⚡ REST: p0r4_H("str_replace", REST, "9", "");
    ⚡ REST: p0r4_H("str_replace", REST, "a", "");
    ⚡ REST: p0r4_H("str_replace", REST, "b", "");
    ⚡ REST: p0r4_H("str_replace", REST, "c", "");
    ⚡ REST: p0r4_H("str_replace", REST, "d", "");
    ⚡ REST: p0r4_H("str_replace", REST, "e", "");
    ⚡ REST: p0r4_H("str_replace", REST, "f", "");
    IF (REST == "") { RETURN 1; }
    RETURN 0;
}

DEF p0r4_none_or_atom(value, max_len) {
    IF (value == "NONE") { RETURN 1; }
    RETURN p0r4_safe_atom(value, max_len);
}

DEF p0r4_none_or_hex64(value) {
    IF (value == "NONE") { RETURN 1; }
    RETURN p0r4_hex64(value);
}

DEF p0r4_exact_field(line, key) {
    ⚡ PARTS: p0r4_H("str_split", line, "=", NULL);
    IF (p0r4_H("list_len", PARTS, NULL, NULL) != 2) { RETURN ""; }
    IF (p0r4_H("list_get", PARTS, 0, NULL) != key) { RETURN ""; }
    RETURN p0r4_H("list_get", PARTS, 1, NULL);
}

DEF p0r4_state_value(snapshot, index, key) {
    ⚡ LINES: p0r4_H("str_split", snapshot, "\n", NULL);
    IF (p0r4_H("list_len", LINES, NULL, NULL) != 20) { RETURN ""; }
    RETURN p0r4_exact_field(p0r4_H("list_get", LINES, index, NULL), key);
}

DEF p0r4_phase_valid(value) {
    IF (value == "GENESIS") { RETURN 1; }
    IF (value == "IDLE") { RETURN 1; }
    IF (value == "WAIT_REQUEST_BIND") { RETURN 1; }
    IF (value == "WAIT_EVIDENCE") { RETURN 1; }
    IF (value == "WAIT_MEMORY_BIND") { RETURN 1; }
    IF (value == "WAIT_CAPABILITY") { RETURN 1; }
    RETURN 0;
}

DEF p0r4_event_valid(value) {
    IF (value == "BOOTSTRAP") { RETURN 1; }
    IF (value == "TICK") { RETURN 1; }
    IF (value == "LEARNING_INPUT_READY") { RETURN 1; }
    IF (value == "REQUEST_BOUND") { RETURN 1; }
    IF (value == "EVIDENCE_READY") { RETURN 1; }
    IF (value == "MEMORY_BOUND") { RETURN 1; }
    IF (value == "RESTART_READY") { RETURN 1; }
    IF (value == "CAPABILITY_RESULT_READY") { RETURN 1; }
    RETURN 0;
}

DEF p0r4_receipt_kind_valid(value) {
    IF (value == "GENESIS") { RETURN 1; }
    IF (value == "TICK") { RETURN 1; }
    IF (value == "LEARNING_INPUT") { RETURN 1; }
    IF (value == "REQUEST_BIND") { RETURN 1; }
    IF (value == "EVIDENCE") { RETURN 1; }
    IF (value == "MEMORY_BIND") { RETURN 1; }
    IF (value == "RESTART") { RETURN 1; }
    IF (value == "CAPABILITY_RESULT") { RETURN 1; }
    RETURN 0;
}

DEF p0r4_event_receipt_kind_matches(event_type, receipt_kind) {
    IF (event_type == "BOOTSTRAP") { IF (receipt_kind == "GENESIS") { RETURN 1; } RETURN 0; }
    IF (event_type == "TICK") { IF (receipt_kind == "TICK") { RETURN 1; } RETURN 0; }
    IF (event_type == "LEARNING_INPUT_READY") { IF (receipt_kind == "LEARNING_INPUT") { RETURN 1; } RETURN 0; }
    IF (event_type == "REQUEST_BOUND") { IF (receipt_kind == "REQUEST_BIND") { RETURN 1; } RETURN 0; }
    IF (event_type == "EVIDENCE_READY") { IF (receipt_kind == "EVIDENCE") { RETURN 1; } RETURN 0; }
    IF (event_type == "MEMORY_BOUND") { IF (receipt_kind == "MEMORY_BIND") { RETURN 1; } RETURN 0; }
    IF (event_type == "RESTART_READY") { IF (receipt_kind == "RESTART") { RETURN 1; } RETURN 0; }
    IF (event_type == "CAPABILITY_RESULT_READY") { IF (receipt_kind == "CAPABILITY_RESULT") { RETURN 1; } RETURN 0; }
    RETURN 0;
}

DEF p0r4_state_snapshot_valid(snapshot) {
    IF (p0r4_H("str_len", snapshot, NULL, NULL) > 8192) { RETURN 0; }
    ⚡ VERSION: p0r4_state_value(snapshot, 0, "STATE_VERSION");
    ⚡ PHASE: p0r4_state_value(snapshot, 1, "PHASE");
    ⚡ OBJECTIVE_ID: p0r4_state_value(snapshot, 2, "OBJECTIVE_ID");
    ⚡ ACTIVE_GAP_ID: p0r4_state_value(snapshot, 3, "ACTIVE_GAP_ID");
    ⚡ PENDING_ACTION_ID: p0r4_state_value(snapshot, 4, "PENDING_ACTION_ID");
    ⚡ PENDING_REQUEST_ID: p0r4_state_value(snapshot, 5, "PENDING_REQUEST_ID");
    ⚡ PENDING_CAPABILITY_ID: p0r4_state_value(snapshot, 6, "PENDING_CAPABILITY_ID");
    ⚡ PENDING_SUBJECT_ID: p0r4_state_value(snapshot, 7, "PENDING_SUBJECT_ID");
    ⚡ PENDING_PAYLOAD_KIND: p0r4_state_value(snapshot, 8, "PENDING_PAYLOAD_KIND");
    ⚡ PENDING_PAYLOAD_SHA: p0r4_state_value(snapshot, 9, "PENDING_PAYLOAD_SHA");
    ⚡ EPISTEMIC_STATE_SHA: p0r4_state_value(snapshot, 10, "EPISTEMIC_STATE_SHA");
    ⚡ MEMORY_STATE_SHA: p0r4_state_value(snapshot, 11, "MEMORY_STATE_SHA");
    ⚡ LAST_RECEIPT_SHA: p0r4_state_value(snapshot, 12, "LAST_RECEIPT_SHA");
    ⚡ LAST_INVOCATION_ID: p0r4_state_value(snapshot, 13, "LAST_INVOCATION_ID");
    ⚡ LAST_ACTION_ID: p0r4_state_value(snapshot, 14, "LAST_ACTION_ID");
    ⚡ LAST_EVENT: p0r4_state_value(snapshot, 15, "LAST_EVENT");
    ⚡ LAST_SOURCE_ID: p0r4_state_value(snapshot, 16, "LAST_SOURCE_ID");
    ⚡ LAST_SOURCE_VERSION_SHA: p0r4_state_value(snapshot, 17, "LAST_SOURCE_VERSION_SHA");
    ⚡ LAST_ARTIFACT_SHA: p0r4_state_value(snapshot, 18, "LAST_ARTIFACT_SHA");
    ⚡ LAST_EVIDENCE_ID: p0r4_state_value(snapshot, 19, "LAST_EVIDENCE_ID");
    IF (VERSION != "2") { RETURN 0; }
    IF (p0r4_phase_valid(PHASE) == 0) { RETURN 0; }
    IF (p0r4_none_or_atom(OBJECTIVE_ID, 128) == 0) { RETURN 0; }
    IF (p0r4_none_or_atom(ACTIVE_GAP_ID, 128) == 0) { RETURN 0; }
    IF (p0r4_none_or_atom(PENDING_ACTION_ID, 128) == 0) { RETURN 0; }
    IF (p0r4_none_or_atom(PENDING_REQUEST_ID, 128) == 0) { RETURN 0; }
    IF (p0r4_none_or_atom(PENDING_CAPABILITY_ID, 128) == 0) { RETURN 0; }
    IF (p0r4_none_or_atom(PENDING_SUBJECT_ID, 128) == 0) { RETURN 0; }
    IF (p0r4_none_or_atom(PENDING_PAYLOAD_KIND, 64) == 0) { RETURN 0; }
    IF (p0r4_none_or_hex64(PENDING_PAYLOAD_SHA) == 0) { RETURN 0; }
    IF (p0r4_none_or_hex64(EPISTEMIC_STATE_SHA) == 0) { RETURN 0; }
    IF (p0r4_none_or_hex64(MEMORY_STATE_SHA) == 0) { RETURN 0; }
    IF (p0r4_none_or_hex64(LAST_RECEIPT_SHA) == 0) { RETURN 0; }
    IF (p0r4_none_or_atom(LAST_INVOCATION_ID, 128) == 0) { RETURN 0; }
    IF (p0r4_none_or_atom(LAST_ACTION_ID, 128) == 0) { RETURN 0; }
    IF (LAST_EVENT != "NONE") { IF (p0r4_event_valid(LAST_EVENT) == 0) { RETURN 0; } }
    IF (p0r4_none_or_atom(LAST_SOURCE_ID, 128) == 0) { RETURN 0; }
    IF (p0r4_none_or_hex64(LAST_SOURCE_VERSION_SHA) == 0) { RETURN 0; }
    IF (p0r4_none_or_hex64(LAST_ARTIFACT_SHA) == 0) { RETURN 0; }
    IF (p0r4_none_or_atom(LAST_EVIDENCE_ID, 128) == 0) { RETURN 0; }
    RETURN 1;
}

DEF p0r4_stage_write_verify(path, value) {
    ⚡ RC: p0r4_H("write_text", path, value, NULL);
    ⚡ BACK: p0r4_H("read_text", path, NULL, NULL);
    IF (BACK != value) { RETURN 0; }
    RETURN 1;
}

DEF p0r4_zero_state() {
    RETURN "STATE_VERSION=2\nPHASE=IDLE\nOBJECTIVE_ID=NONE\nACTIVE_GAP_ID=NONE\nPENDING_ACTION_ID=NONE\nPENDING_REQUEST_ID=NONE\nPENDING_CAPABILITY_ID=NONE\nPENDING_SUBJECT_ID=NONE\nPENDING_PAYLOAD_KIND=NONE\nPENDING_PAYLOAD_SHA=NONE\nEPISTEMIC_STATE_SHA=NONE\nMEMORY_STATE_SHA=NONE\nLAST_RECEIPT_SHA=NONE\nLAST_INVOCATION_ID=NONE\nLAST_ACTION_ID=NONE\nLAST_EVENT=NONE\nLAST_SOURCE_ID=NONE\nLAST_SOURCE_VERSION_SHA=NONE\nLAST_ARTIFACT_SHA=NONE\nLAST_EVIDENCE_ID=NONE";
}
