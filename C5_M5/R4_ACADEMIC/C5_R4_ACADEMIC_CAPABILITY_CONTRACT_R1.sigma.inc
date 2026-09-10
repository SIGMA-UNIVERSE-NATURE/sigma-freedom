# C5V3 R4 academic capability contract R1.
# Native selection only: a need is executable only when exactly one admitted capability matches the family.
# Host may transport a registry mechanically but must not choose or reorder a semantic winner for SIGMA.

DEF c5ac1_admitted_family_count(registry, need_family) {
    IF (registry == "") { RETURN 0; }
    IF (c5l2_safe_atom(need_family, 64) == 0) { RETURN 0; }
    ⚡ LINES: H("str_split", registry, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    ⚡ COUNT: 0;
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        IF (c5l2_capability_record_valid(LINE)) {
            IF (c5l2_field(LINE, 2, "FAMILY") == need_family) {
                IF (c5l2_field(LINE, 3, "STATE") == "ADMITTED") { ⚡ COUNT: COUNT + 1; }
            }
        }
        ⚡ I: I + 1;
    }
    RETURN COUNT;
}

DEF c5ac1_unique_admitted_capability(registry, need_family) {
    IF (c5ac1_admitted_family_count(registry, need_family) != 1) { RETURN ""; }
    ⚡ LINES: H("str_split", registry, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        IF (c5l2_capability_record_valid(LINE)) {
            IF (c5l2_field(LINE, 2, "FAMILY") == need_family) {
                IF (c5l2_field(LINE, 3, "STATE") == "ADMITTED") { RETURN LINE; }
            }
        }
        ⚡ I: I + 1;
    }
    RETURN "";
}

DEF c5ac1_request_valid(record) {
    IF (H("str_len", record, NULL, NULL) > 1536) { RETURN 0; }
    IF (c5l2_record_part_count(record) != 7) { RETURN 0; }
    ⚡ TYPE: c5l2_field(record, 0, "TYPE");
    ⚡ ACTION_ID: c5l2_field(record, 1, "ACTION_ID");
    ⚡ CAPABILITY_ID: c5l2_field(record, 2, "CAPABILITY_ID");
    ⚡ NEED_FAMILY: c5l2_field(record, 3, "NEED_FAMILY");
    ⚡ SUBJECT_ID: c5l2_field(record, 4, "SUBJECT_ID");
    ⚡ PASSAGE_ID: c5l2_field(record, 5, "PASSAGE_ID");
    ⚡ BASIS_SHA: c5l2_field(record, 6, "BASIS_SHA");
    IF (TYPE != "ACADEMIC_CAPABILITY_REQUEST") { RETURN 0; }
    IF (c5l2_safe_atom(ACTION_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(CAPABILITY_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(NEED_FAMILY, 64) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(SUBJECT_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(PASSAGE_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_hex64(BASIS_SHA) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5ac1_make_request(action_id, capability, need_family, subject_id, passage) {
    IF (c5l2_safe_atom(action_id, 128) == 0) { RETURN ""; }
    IF (c5l2_capability_record_valid(capability) == 0) { RETURN ""; }
    IF (c5l2_field(capability, 2, "FAMILY") != need_family) { RETURN ""; }
    IF (c5l2_field(capability, 3, "STATE") != "ADMITTED") { RETURN ""; }
    IF (c5l2_safe_atom(subject_id, 128) == 0) { RETURN ""; }
    IF (c5ad1_passage_valid(passage) == 0) { RETURN ""; }
    ⚡ CAPABILITY_ID: c5l2_field(capability, 1, "CAPABILITY_ID");
    ⚡ PASSAGE_ID: c5l2_field(passage, 1, "PASSAGE_ID");
    ⚡ BASIS_SHA: c5l2_field(passage, 5, "CONTENT_SHA");
    RETURN "TYPE=ACADEMIC_CAPABILITY_REQUEST || ACTION_ID=" + action_id + " || CAPABILITY_ID=" + CAPABILITY_ID + " || NEED_FAMILY=" + need_family + " || SUBJECT_ID=" + subject_id + " || PASSAGE_ID=" + PASSAGE_ID + " || BASIS_SHA=" + BASIS_SHA;
}

DEF c5ac1_text_result_valid(record) {
    IF (H("str_len", record, NULL, NULL) > 3072) { RETURN 0; }
    IF (c5l2_record_part_count(record) != 6) { RETURN 0; }
    ⚡ TYPE: c5l2_field(record, 0, "TYPE");
    ⚡ CAPABILITY_ID: c5l2_field(record, 1, "CAPABILITY_ID");
    ⚡ SUBJECT_ID: c5l2_field(record, 2, "SUBJECT_ID");
    ⚡ PASSAGE_ID: c5l2_field(record, 3, "PASSAGE_ID");
    ⚡ BASIS_SHA: c5l2_field(record, 4, "BASIS_SHA");
    ⚡ CONTENT: c5l2_field(record, 5, "CONTENT");
    IF (TYPE != "ACADEMIC_TEXT_RESULT") { RETURN 0; }
    IF (c5l2_safe_atom(CAPABILITY_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(SUBJECT_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(PASSAGE_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_hex64(BASIS_SHA) == 0) { RETURN 0; }
    IF (c5d1_payload_valid(CONTENT, 512) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5ac1_result_matches_request(result, request) {
    IF (c5ac1_text_result_valid(result) == 0) { RETURN 0; }
    IF (c5ac1_request_valid(request) == 0) { RETURN 0; }
    IF (c5l2_field(result, 1, "CAPABILITY_ID") != c5l2_field(request, 2, "CAPABILITY_ID")) { RETURN 0; }
    IF (c5l2_field(result, 2, "SUBJECT_ID") != c5l2_field(request, 4, "SUBJECT_ID")) { RETURN 0; }
    IF (c5l2_field(result, 3, "PASSAGE_ID") != c5l2_field(request, 5, "PASSAGE_ID")) { RETURN 0; }
    IF (c5l2_field(result, 4, "BASIS_SHA") != c5l2_field(request, 6, "BASIS_SHA")) { RETURN 0; }
    RETURN 1;
}

DEF c5ac1_result_to_observation(result, request, observation_id, result_artifact_sha) {
    IF (c5ac1_result_matches_request(result, request) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(observation_id, 128) == 0) { RETURN ""; }
    IF (c5l2_hex64(result_artifact_sha) == 0) { RETURN ""; }
    ⚡ CAPABILITY_ID: c5l2_field(result, 1, "CAPABILITY_ID");
    ⚡ SUBJECT_ID: c5l2_field(result, 2, "SUBJECT_ID");
    ⚡ PASSAGE_ID: c5l2_field(result, 3, "PASSAGE_ID");
    ⚡ BASIS_SHA: c5l2_field(result, 4, "BASIS_SHA");
    ⚡ CONTENT: c5l2_field(result, 5, "CONTENT");
    RETURN "TYPE=ACADEMIC_OBSERVATION || OBS_ID=" + observation_id + " || SUBJECT_ID=" + SUBJECT_ID + " || PASSAGE_ID=" + PASSAGE_ID + " || CONTENT=" + CONTENT + " || CAPABILITY_ID=" + CAPABILITY_ID + " || RESULT_SHA=" + result_artifact_sha + " || BASIS_SHA=" + BASIS_SHA;
}
