# C5V3 R4 academic state substrate R1.
# Pure academic records only. No I/O, transport, source selection, query generation, or host semantic authority.
# Semantic observations and judgments must bind a native capability result SHA before entering this layer.

DEF c5as1_work_state_valid(value) {
    IF (value == "OPEN") { RETURN 1; }
    IF (value == "EVIDENCE_BUILDING") { RETURN 1; }
    IF (value == "HELD") { RETURN 1; }
    IF (value == "STRUCTURALLY_COVERED") { RETURN 1; }
    RETURN 0;
}

DEF c5as1_question_kind_valid(value) {
    IF (value == "EVIDENCE") { RETURN 1; }
    IF (value == "CONFLICT") { RETURN 1; }
    IF (value == "CITATION") { RETURN 1; }
    IF (value == "TEXT_CAPABILITY") { RETURN 1; }
    IF (value == "STRUCTURE") { RETURN 1; }
    RETURN 0;
}

DEF c5as1_question_state_valid(value) {
    IF (value == "OPEN") { RETURN 1; }
    IF (value == "RESOLVED") { RETURN 1; }
    IF (value == "HELD") { RETURN 1; }
    RETURN 0;
}

DEF c5as1_work_valid(record) {
    IF (H("str_len", record, NULL, NULL) > 1536) { RETURN 0; }
    IF (c5l2_record_part_count(record) != 6) { RETURN 0; }
    ⚡ TYPE: c5l2_field(record, 0, "TYPE");
    ⚡ WORK_ID: c5l2_field(record, 1, "WORK_ID");
    ⚡ STATE: c5l2_field(record, 2, "STATE");
    ⚡ SUBJECT_ID: c5l2_field(record, 3, "SUBJECT_ID");
    ⚡ OBJECTIVE_ID: c5l2_field(record, 4, "OBJECTIVE_ID");
    ⚡ REVISION: c5l2_field(record, 5, "REVISION");
    IF (TYPE != "ACADEMIC_WORK") { RETURN 0; }
    IF (c5l2_safe_atom(WORK_ID, 128) == 0) { RETURN 0; }
    IF (c5as1_work_state_valid(STATE) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(SUBJECT_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(OBJECTIVE_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_digits_only(REVISION) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5as1_make_work(work_id, state, subject_id, objective_id, revision) {
    IF (c5l2_safe_atom(work_id, 128) == 0) { RETURN ""; }
    IF (c5as1_work_state_valid(state) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(subject_id, 128) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(objective_id, 128) == 0) { RETURN ""; }
    IF (c5l2_digits_only(revision) == 0) { RETURN ""; }
    RETURN "TYPE=ACADEMIC_WORK || WORK_ID=" + work_id + " || STATE=" + state + " || SUBJECT_ID=" + subject_id + " || OBJECTIVE_ID=" + objective_id + " || REVISION=" + revision;
}

DEF c5as1_question_valid(record) {
    IF (H("str_len", record, NULL, NULL) > 1792) { RETURN 0; }
    IF (c5l2_record_part_count(record) != 8) { RETURN 0; }
    ⚡ TYPE: c5l2_field(record, 0, "TYPE");
    ⚡ QUESTION_ID: c5l2_field(record, 1, "QUESTION_ID");
    ⚡ WORK_ID: c5l2_field(record, 2, "WORK_ID");
    ⚡ SUBJECT_ID: c5l2_field(record, 3, "SUBJECT_ID");
    ⚡ KIND: c5l2_field(record, 4, "KIND");
    ⚡ STATE: c5l2_field(record, 5, "STATE");
    ⚡ NEED_FAMILY: c5l2_field(record, 6, "NEED_FAMILY");
    ⚡ PRIORITY: c5l2_field(record, 7, "PRIORITY");
    IF (TYPE != "ACADEMIC_QUESTION") { RETURN 0; }
    IF (c5l2_safe_atom(QUESTION_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(WORK_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(SUBJECT_ID, 128) == 0) { RETURN 0; }
    IF (c5as1_question_kind_valid(KIND) == 0) { RETURN 0; }
    IF (c5as1_question_state_valid(STATE) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(NEED_FAMILY, 64) == 0) { RETURN 0; }
    IF (c5l2_digits_only(PRIORITY) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5as1_make_question(question_id, work_id, subject_id, kind, need_family, priority) {
    IF (c5l2_safe_atom(question_id, 128) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(work_id, 128) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(subject_id, 128) == 0) { RETURN ""; }
    IF (c5as1_question_kind_valid(kind) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(need_family, 64) == 0) { RETURN ""; }
    IF (c5l2_digits_only(priority) == 0) { RETURN ""; }
    RETURN "TYPE=ACADEMIC_QUESTION || QUESTION_ID=" + question_id + " || WORK_ID=" + work_id + " || SUBJECT_ID=" + subject_id + " || KIND=" + kind + " || STATE=OPEN || NEED_FAMILY=" + need_family + " || PRIORITY=" + priority;
}

DEF c5as1_observation_valid(record) {
    IF (H("str_len", record, NULL, NULL) > 3072) { RETURN 0; }
    IF (c5l2_record_part_count(record) != 8) { RETURN 0; }
    ⚡ TYPE: c5l2_field(record, 0, "TYPE");
    ⚡ OBS_ID: c5l2_field(record, 1, "OBS_ID");
    ⚡ SUBJECT_ID: c5l2_field(record, 2, "SUBJECT_ID");
    ⚡ PASSAGE_ID: c5l2_field(record, 3, "PASSAGE_ID");
    ⚡ CONTENT: c5l2_field(record, 4, "CONTENT");
    ⚡ CAPABILITY_ID: c5l2_field(record, 5, "CAPABILITY_ID");
    ⚡ RESULT_SHA: c5l2_field(record, 6, "RESULT_SHA");
    ⚡ BASIS_SHA: c5l2_field(record, 7, "BASIS_SHA");
    IF (TYPE != "ACADEMIC_OBSERVATION") { RETURN 0; }
    IF (c5l2_safe_atom(OBS_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(SUBJECT_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(PASSAGE_ID, 128) == 0) { RETURN 0; }
    IF (c5d1_payload_valid(CONTENT, 512) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(CAPABILITY_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_hex64(RESULT_SHA) == 0) { RETURN 0; }
    IF (c5l2_hex64(BASIS_SHA) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5as1_make_observation(obs_id, subject_id, passage_id, content, capability_id, result_sha) {
    IF (c5l2_safe_atom(obs_id, 128) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(subject_id, 128) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(passage_id, 128) == 0) { RETURN ""; }
    IF (c5d1_payload_valid(content, 512) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(capability_id, 128) == 0) { RETURN ""; }
    IF (c5l2_hex64(result_sha) == 0) { RETURN ""; }
    RETURN "TYPE=ACADEMIC_OBSERVATION || OBS_ID=" + obs_id + " || SUBJECT_ID=" + subject_id + " || PASSAGE_ID=" + passage_id + " || CONTENT=" + content + " || CAPABILITY_ID=" + capability_id + " || RESULT_SHA=" + result_sha + " || BASIS_SHA=" + result_sha;
}

DEF c5as1_judgment_valid(record) {
    IF (H("str_len", record, NULL, NULL) > 2048) { RETURN 0; }
    IF (c5l2_record_part_count(record) != 9) { RETURN 0; }
    ⚡ TYPE: c5l2_field(record, 0, "TYPE");
    ⚡ JUDGMENT_ID: c5l2_field(record, 1, "JUDGMENT_ID");
    ⚡ CLAIM_ID: c5l2_field(record, 2, "CLAIM_ID");
    ⚡ EVIDENCE_ID: c5l2_field(record, 3, "EVIDENCE_ID");
    ⚡ SOURCE_ID: c5l2_field(record, 4, "SOURCE_ID");
    ⚡ STANCE: c5l2_field(record, 5, "STANCE");
    ⚡ BASIS_SHA: c5l2_field(record, 6, "BASIS_SHA");
    ⚡ CAPABILITY_ID: c5l2_field(record, 7, "CAPABILITY_ID");
    ⚡ RESULT_SHA: c5l2_field(record, 8, "RESULT_SHA");
    IF (TYPE != "ACADEMIC_JUDGMENT") { RETURN 0; }
    IF (c5l2_safe_atom(JUDGMENT_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(CLAIM_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(EVIDENCE_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(SOURCE_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_stance_valid(STANCE) == 0) { RETURN 0; }
    IF (c5l2_hex64(BASIS_SHA) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(CAPABILITY_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_hex64(RESULT_SHA) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5as1_make_judgment(judgment_id, claim_id, evidence_id, source_id, stance, capability_result) {
    IF (c5l2_safe_atom(judgment_id, 128) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(claim_id, 128) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(evidence_id, 128) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(source_id, 128) == 0) { RETURN ""; }
    IF (c5l2_stance_valid(stance) == 0) { RETURN ""; }
    IF (c5l2_record_part_count(capability_result) != 3) { RETURN ""; }
    ⚡ CAPABILITY_ID: c5l2_field(capability_result, 0, "CAPABILITY_ID");
    ⚡ RESULT_SHA: c5l2_field(capability_result, 1, "RESULT_SHA");
    ⚡ BASIS_SHA: c5l2_field(capability_result, 2, "BASIS_SHA");
    IF (c5l2_safe_atom(CAPABILITY_ID, 128) == 0) { RETURN ""; }
    IF (c5l2_hex64(RESULT_SHA) == 0) { RETURN ""; }
    IF (c5l2_hex64(BASIS_SHA) == 0) { RETURN ""; }
    RETURN "TYPE=ACADEMIC_JUDGMENT || JUDGMENT_ID=" + judgment_id + " || CLAIM_ID=" + claim_id + " || EVIDENCE_ID=" + evidence_id + " || SOURCE_ID=" + source_id + " || STANCE=" + stance + " || BASIS_SHA=" + BASIS_SHA + " || CAPABILITY_ID=" + CAPABILITY_ID + " || RESULT_SHA=" + RESULT_SHA;
}

DEF c5as1_synthesis_state_valid(value) {
    IF (value == "UNRESOLVED") { RETURN 1; }
    IF (value == "EVIDENCE_SUPPORTED") { RETURN 1; }
    IF (value == "EVIDENCE_CONTRADICTED") { RETURN 1; }
    IF (value == "CONTESTED") { RETURN 1; }
    RETURN 0;
}

DEF c5as1_synthesis_valid(record) {
    IF (H("str_len", record, NULL, NULL) > 1536) { RETURN 0; }
    IF (c5l2_record_part_count(record) != 8) { RETURN 0; }
    ⚡ TYPE: c5l2_field(record, 0, "TYPE");
    ⚡ CLAIM_ID: c5l2_field(record, 1, "CLAIM_ID");
    ⚡ STATE: c5l2_field(record, 2, "STATE");
    ⚡ SUPPORT_SOURCES: c5l2_field(record, 3, "SUPPORT_SOURCES");
    ⚡ CONTRARY_SOURCES: c5l2_field(record, 4, "CONTRARY_SOURCES");
    ⚡ NEUTRAL_SOURCES: c5l2_field(record, 5, "NEUTRAL_SOURCES");
    ⚡ EVALUATION_COUNT: c5l2_field(record, 6, "EVALUATION_COUNT");
    ⚡ REVISION: c5l2_field(record, 7, "REVISION");
    IF (TYPE != "ACADEMIC_SYNTHESIS") { RETURN 0; }
    IF (c5l2_safe_atom(CLAIM_ID, 128) == 0) { RETURN 0; }
    IF (c5as1_synthesis_state_valid(STATE) == 0) { RETURN 0; }
    IF (c5l2_digits_only(SUPPORT_SOURCES) == 0) { RETURN 0; }
    IF (c5l2_digits_only(CONTRARY_SOURCES) == 0) { RETURN 0; }
    IF (c5l2_digits_only(NEUTRAL_SOURCES) == 0) { RETURN 0; }
    IF (c5l2_digits_only(EVALUATION_COUNT) == 0) { RETURN 0; }
    IF (c5l2_digits_only(REVISION) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5as1_make_synthesis(claim_id, state, support_sources, contrary_sources, neutral_sources, revision) {
    IF (c5l2_safe_atom(claim_id, 128) == 0) { RETURN ""; }
    IF (c5as1_synthesis_state_valid(state) == 0) { RETURN ""; }
    IF (c5l2_digits_only(support_sources) == 0) { RETURN ""; }
    IF (c5l2_digits_only(contrary_sources) == 0) { RETURN ""; }
    IF (c5l2_digits_only(neutral_sources) == 0) { RETURN ""; }
    IF (c5l2_digits_only(revision) == 0) { RETURN ""; }
    ⚡ TOTAL: support_sources + contrary_sources + neutral_sources;
    RETURN "TYPE=ACADEMIC_SYNTHESIS || CLAIM_ID=" + claim_id + " || STATE=" + state + " || SUPPORT_SOURCES=" + support_sources + " || CONTRARY_SOURCES=" + contrary_sources + " || NEUTRAL_SOURCES=" + neutral_sources + " || EVALUATION_COUNT=" + TOTAL + " || REVISION=" + revision;
}

DEF c5as1_question_bank_valid(bank) {
    IF (bank == "") { RETURN 1; }
    IF (64 < c5l2_bank_count(bank)) { RETURN 0; }
    ⚡ LINES: H("str_split", bank, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        IF (LINE != "") { IF (c5as1_question_valid(LINE) == 0) { RETURN 0; } }
        ⚡ I: I + 1;
    }
    RETURN 1;
}

DEF c5as1_synthesis_bank_valid(bank) {
    IF (bank == "") { RETURN 1; }
    IF (64 < c5l2_bank_count(bank)) { RETURN 0; }
    ⚡ LINES: H("str_split", bank, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        IF (LINE != "") { IF (c5as1_synthesis_valid(LINE) == 0) { RETURN 0; } }
        ⚡ I: I + 1;
    }
    RETURN 1;
}
