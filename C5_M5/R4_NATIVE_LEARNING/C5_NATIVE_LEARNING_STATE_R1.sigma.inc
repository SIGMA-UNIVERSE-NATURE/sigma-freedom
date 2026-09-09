# C5V3 native learning state substrate R1.
# Pure state transforms only: no filesystem, transport, persistence, host semantic selection, or source choice.
# This module does not claim broad semantic understanding. It provides bounded representation/revision machinery
# for native cognition and exact provenance/evidence accounting.

DEF c5l_present(value) {
    IF (value == "") { RETURN 0; }
    IF (value == "NONE") { RETURN 0; }
    RETURN 1;
}

DEF c5l_digits_only(value) {
    IF (value == "") { RETURN 0; }
    ⚡ REST: value;
    ⚡ REST: H("str_replace", REST, "0", "");
    ⚡ REST: H("str_replace", REST, "1", "");
    ⚡ REST: H("str_replace", REST, "2", "");
    ⚡ REST: H("str_replace", REST, "3", "");
    ⚡ REST: H("str_replace", REST, "4", "");
    ⚡ REST: H("str_replace", REST, "5", "");
    ⚡ REST: H("str_replace", REST, "6", "");
    ⚡ REST: H("str_replace", REST, "7", "");
    ⚡ REST: H("str_replace", REST, "8", "");
    ⚡ REST: H("str_replace", REST, "9", "");
    IF (REST == "") { RETURN 1; }
    RETURN 0;
}

DEF c5l_hex64(value) {
    IF (H("str_len", value, NULL, NULL) != 64) { RETURN 0; }
    ⚡ REST: H("str_lower", value, NULL, NULL);
    ⚡ REST: H("str_replace", REST, "0", "");
    ⚡ REST: H("str_replace", REST, "1", "");
    ⚡ REST: H("str_replace", REST, "2", "");
    ⚡ REST: H("str_replace", REST, "3", "");
    ⚡ REST: H("str_replace", REST, "4", "");
    ⚡ REST: H("str_replace", REST, "5", "");
    ⚡ REST: H("str_replace", REST, "6", "");
    ⚡ REST: H("str_replace", REST, "7", "");
    ⚡ REST: H("str_replace", REST, "8", "");
    ⚡ REST: H("str_replace", REST, "9", "");
    ⚡ REST: H("str_replace", REST, "a", "");
    ⚡ REST: H("str_replace", REST, "b", "");
    ⚡ REST: H("str_replace", REST, "c", "");
    ⚡ REST: H("str_replace", REST, "d", "");
    ⚡ REST: H("str_replace", REST, "e", "");
    ⚡ REST: H("str_replace", REST, "f", "");
    IF (REST == "") { RETURN 1; }
    RETURN 0;
}

DEF c5l_safe_atom(value, max_len) {
    IF (value == "") { RETURN 0; }
    ⚡ N: H("str_len", value, NULL, NULL);
    IF (max_len < N) { RETURN 0; }
    ⚡ X: H("str_replace", value, "\n", "");
    IF (X != value) { RETURN 0; }
    ⚡ X: H("str_replace", value, "\r", "");
    IF (X != value) { RETURN 0; }
    ⚡ X: H("str_replace", value, "\t", "");
    IF (X != value) { RETURN 0; }
    ⚡ X: H("str_replace", value, " || ", "");
    IF (X != value) { RETURN 0; }
    RETURN 1;
}

DEF c5l_field(record, index, prefix) {
    ⚡ PARTS: H("str_split", record, " || ", NULL);
    ⚡ N: H("list_len", PARTS, NULL, NULL);
    IF (N <= index) { RETURN ""; }
    ⚡ FIELD: H("list_get", PARTS, index, NULL);
    ⚡ VALUE: H("str_replace", FIELD, prefix, "");
    IF (VALUE == FIELD) { RETURN ""; }
    RETURN VALUE;
}

DEF c5l_epistemic_class_valid(value) {
    IF (value == "OBSERVED") { RETURN 1; }
    IF (value == "DERIVED") { RETURN 1; }
    IF (value == "HYPOTHESIS") { RETURN 1; }
    IF (value == "UNRESOLVED") { RETURN 1; }
    IF (value == "CONTRADICTED") { RETURN 1; }
    RETURN 0;
}

DEF c5l_gap_kind_valid(value) {
    IF (value == "EVIDENCE") { RETURN 1; }
    IF (value == "CONFLICT") { RETURN 1; }
    IF (value == "CAPABILITY") { RETURN 1; }
    IF (value == "MEMORY") { RETURN 1; }
    IF (value == "STRUCTURE") { RETURN 1; }
    RETURN 0;
}

DEF c5l_stance_valid(value) {
    IF (value == "SUPPORT") { RETURN 1; }
    IF (value == "CONTRARY") { RETURN 1; }
    IF (value == "NEUTRAL") { RETURN 1; }
    RETURN 0;
}

DEF c5l_claim_valid(record) {
    ⚡ TYPE: c5l_field(record, 0, "TYPE=");
    ⚡ CLAIM_ID: c5l_field(record, 1, "CLAIM_ID=");
    ⚡ SUBJECT_ID: c5l_field(record, 2, "SUBJECT_ID=");
    ⚡ CLASS: c5l_field(record, 3, "CLASS=");
    ⚡ REVISION: c5l_field(record, 4, "REVISION=");
    ⚡ UNCERTAINTY: c5l_field(record, 5, "UNCERTAINTY=");
    IF (TYPE != "CLAIM") { RETURN 0; }
    IF (c5l_safe_atom(CLAIM_ID, 128) == 0) { RETURN 0; }
    IF (c5l_safe_atom(SUBJECT_ID, 128) == 0) { RETURN 0; }
    IF (c5l_epistemic_class_valid(CLASS) == 0) { RETURN 0; }
    IF (c5l_digits_only(REVISION) == 0) { RETURN 0; }
    IF (c5l_digits_only(UNCERTAINTY) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5l_gap_valid(record) {
    ⚡ TYPE: c5l_field(record, 0, "TYPE=");
    ⚡ GAP_ID: c5l_field(record, 1, "GAP_ID=");
    ⚡ OBJECTIVE_ID: c5l_field(record, 2, "OBJECTIVE_ID=");
    ⚡ KIND: c5l_field(record, 3, "KIND=");
    ⚡ SUBJECT_ID: c5l_field(record, 4, "SUBJECT_ID=");
    ⚡ STATE: c5l_field(record, 5, "STATE=");
    ⚡ NEED_FAMILY: c5l_field(record, 6, "NEED_FAMILY=");
    ⚡ PRIORITY: c5l_field(record, 7, "PRIORITY=");
    IF (TYPE != "GAP") { RETURN 0; }
    IF (c5l_safe_atom(GAP_ID, 128) == 0) { RETURN 0; }
    IF (c5l_safe_atom(OBJECTIVE_ID, 128) == 0) { RETURN 0; }
    IF (c5l_gap_kind_valid(KIND) == 0) { RETURN 0; }
    IF (c5l_safe_atom(SUBJECT_ID, 128) == 0) { RETURN 0; }
    IF (STATE != "OPEN") {
        IF (STATE != "RESOLVED") {
            IF (STATE != "HELD") { RETURN 0; }
        }
    }
    IF (c5l_safe_atom(NEED_FAMILY, 64) == 0) { RETURN 0; }
    IF (c5l_digits_only(PRIORITY) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5l_evidence_valid(record) {
    ⚡ TYPE: c5l_field(record, 0, "TYPE=");
    ⚡ EVIDENCE_ID: c5l_field(record, 1, "EVIDENCE_ID=");
    ⚡ SOURCE_ID: c5l_field(record, 2, "SOURCE_ID=");
    ⚡ SOURCE_VERSION_SHA: c5l_field(record, 3, "SOURCE_VERSION_SHA=");
    ⚡ ARTIFACT_SHA: c5l_field(record, 4, "ARTIFACT_SHA=");
    ⚡ SUBJECT_ID: c5l_field(record, 5, "SUBJECT_ID=");
    IF (TYPE != "EVIDENCE") { RETURN 0; }
    IF (c5l_safe_atom(EVIDENCE_ID, 128) == 0) { RETURN 0; }
    IF (c5l_safe_atom(SOURCE_ID, 128) == 0) { RETURN 0; }
    IF (c5l_hex64(SOURCE_VERSION_SHA) == 0) { RETURN 0; }
    IF (c5l_hex64(ARTIFACT_SHA) == 0) { RETURN 0; }
    IF (c5l_safe_atom(SUBJECT_ID, 128) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5l_evaluation_valid(record) {
    ⚡ TYPE: c5l_field(record, 0, "TYPE=");
    ⚡ EVAL_ID: c5l_field(record, 1, "EVAL_ID=");
    ⚡ CLAIM_ID: c5l_field(record, 2, "CLAIM_ID=");
    ⚡ EVIDENCE_ID: c5l_field(record, 3, "EVIDENCE_ID=");
    ⚡ SOURCE_ID: c5l_field(record, 4, "SOURCE_ID=");
    ⚡ STANCE: c5l_field(record, 5, "STANCE=");
    ⚡ BASIS_SHA: c5l_field(record, 6, "BASIS_SHA=");
    IF (TYPE != "EVALUATION") { RETURN 0; }
    IF (c5l_safe_atom(EVAL_ID, 128) == 0) { RETURN 0; }
    IF (c5l_safe_atom(CLAIM_ID, 128) == 0) { RETURN 0; }
    IF (c5l_safe_atom(EVIDENCE_ID, 128) == 0) { RETURN 0; }
    IF (c5l_safe_atom(SOURCE_ID, 128) == 0) { RETURN 0; }
    IF (c5l_stance_valid(STANCE) == 0) { RETURN 0; }
    IF (c5l_hex64(BASIS_SHA) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5l_bank_count(bank) {
    IF (bank == "") { RETURN 0; }
    ⚡ LINES: H("str_split", bank, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    ⚡ COUNT: 0;
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        IF (LINE != "") { ⚡ COUNT: COUNT + 1; }
        ⚡ I: I + 1;
    }
    RETURN COUNT;
}

DEF c5l_bank_find(bank, id_prefix, id_value) {
    IF (bank == "") { RETURN ""; }
    ⚡ LINES: H("str_split", bank, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    ⚡ FOUND: "";
    WHILE (I < N) {
        IF (FOUND == "") {
            ⚡ LINE: H("list_get", LINES, I, NULL);
            IF (LINE != "") {
                ⚡ PARTS: H("str_split", LINE, " || ", NULL);
                ⚡ P: H("list_len", PARTS, NULL, NULL);
                ⚡ J: 0;
                WHILE (J < P) {
                    IF (FOUND == "") {
                        ⚡ F: H("list_get", PARTS, J, NULL);
                        ⚡ V: H("str_replace", F, id_prefix, "");
                        IF (V != F) {
                            IF (V == id_value) { ⚡ FOUND: LINE; }
                        }
                    }
                    ⚡ J: J + 1;
                }
            }
        }
        ⚡ I: I + 1;
    }
    RETURN FOUND;
}

DEF c5l_bank_append_bounded(bank, record, max_count) {
    ⚡ COUNT: c5l_bank_count(bank);
    IF (max_count <= COUNT) { RETURN ""; }
    IF (bank == "") { RETURN record; }
    RETURN bank + "\n" + record;
}

DEF c5l_source_seen_for_claim(eval_bank, claim_id, source_id, stance) {
    IF (eval_bank == "") { RETURN 0; }
    ⚡ LINES: H("str_split", eval_bank, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        IF (LINE != "") {
            IF (c5l_evaluation_valid(LINE)) {
                ⚡ C: c5l_field(LINE, 2, "CLAIM_ID=");
                ⚡ S: c5l_field(LINE, 4, "SOURCE_ID=");
                ⚡ T: c5l_field(LINE, 5, "STANCE=");
                IF (C == claim_id) {
                    IF (S == source_id) {
                        IF (T == stance) { RETURN 1; }
                    }
                }
            }
        }
        ⚡ I: I + 1;
    }
    RETURN 0;
}

DEF c5l_distinct_source_count_for_stance(eval_bank, claim_id, stance) {
    IF (eval_bank == "") { RETURN 0; }
    ⚡ LINES: H("str_split", eval_bank, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    ⚡ SEEN: "";
    ⚡ COUNT: 0;
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        IF (LINE != "") {
            IF (c5l_evaluation_valid(LINE)) {
                ⚡ C: c5l_field(LINE, 2, "CLAIM_ID=");
                ⚡ S: c5l_field(LINE, 4, "SOURCE_ID=");
                ⚡ T: c5l_field(LINE, 5, "STANCE=");
                IF (C == claim_id) {
                    IF (T == stance) {
                        ⚡ MARK: "[" + S + "]";
                        ⚡ LEFT: H("str_replace", SEEN, MARK, "");
                        IF (LEFT == SEEN) {
                            ⚡ SEEN: SEEN + MARK;
                            ⚡ COUNT: COUNT + 1;
                        }
                    }
                }
            }
        }
        ⚡ I: I + 1;
    }
    RETURN COUNT;
}

DEF c5l_evidence_posture(eval_bank, claim_id) {
    ⚡ SUPPORT: c5l_distinct_source_count_for_stance(eval_bank, claim_id, "SUPPORT");
    ⚡ CONTRARY: c5l_distinct_source_count_for_stance(eval_bank, claim_id, "CONTRARY");
    IF (SUPPORT == 0) {
        IF (CONTRARY == 0) { RETURN "UNRESOLVED"; }
        IF (0 < CONTRARY) { RETURN "CONTRARY_ONLY"; }
    }
    IF (0 < SUPPORT) {
        IF (CONTRARY == 0) { RETURN "SUPPORTED_ONLY"; }
        IF (0 < CONTRARY) { RETURN "CONTESTED"; }
    }
    RETURN "UNRESOLVED";
}

DEF c5l_claim_revision_record(old_claim, new_class, uncertainty, new_revision) {
    IF (c5l_claim_valid(old_claim) == 0) { RETURN ""; }
    IF (c5l_epistemic_class_valid(new_class) == 0) { RETURN ""; }
    IF (c5l_digits_only(uncertainty) == 0) { RETURN ""; }
    ⚡ CLAIM_ID: c5l_field(old_claim, 1, "CLAIM_ID=");
    ⚡ SUBJECT_ID: c5l_field(old_claim, 2, "SUBJECT_ID=");
    IF (c5l_digits_only(new_revision) == 0) { RETURN ""; }
    RETURN "TYPE=CLAIM || CLAIM_ID=" + CLAIM_ID + " || SUBJECT_ID=" + SUBJECT_ID + " || CLASS=" + new_class + " || REVISION=" + new_revision + " || UNCERTAINTY=" + uncertainty;
}

DEF c5l_request_valid(record) {
    ⚡ TYPE: c5l_field(record, 0, "TYPE=");
    ⚡ REQUEST_ID: c5l_field(record, 1, "REQUEST_ID=");
    ⚡ GAP_ID: c5l_field(record, 2, "GAP_ID=");
    ⚡ NEED_FAMILY: c5l_field(record, 3, "NEED_FAMILY=");
    ⚡ PAYLOAD_SHA: c5l_field(record, 4, "PAYLOAD_SHA=");
    IF (TYPE != "REQUEST") { RETURN 0; }
    IF (c5l_safe_atom(REQUEST_ID, 128) == 0) { RETURN 0; }
    IF (c5l_safe_atom(GAP_ID, 128) == 0) { RETURN 0; }
    IF (c5l_safe_atom(NEED_FAMILY, 64) == 0) { RETURN 0; }
    IF (c5l_hex64(PAYLOAD_SHA) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5l_capability_registry_select(registry, need_family) {
    IF (registry == "") { RETURN ""; }
    IF (c5l_safe_atom(need_family, 64) == 0) { RETURN ""; }
    ⚡ LINES: H("str_split", registry, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    ⚡ SELECTED: "";
    WHILE (I < N) {
        IF (SELECTED == "") {
            ⚡ LINE: H("list_get", LINES, I, NULL);
            IF (LINE != "") {
                ⚡ TYPE: c5l_field(LINE, 0, "TYPE=");
                ⚡ CAP_ID: c5l_field(LINE, 1, "CAPABILITY_ID=");
                ⚡ FAMILY: c5l_field(LINE, 2, "FAMILY=");
                ⚡ STATE: c5l_field(LINE, 3, "STATE=");
                IF (TYPE == "CAPABILITY") {
                    IF (FAMILY == need_family) {
                        IF (STATE == "ADMITTED") {
                            IF (c5l_safe_atom(CAP_ID, 128)) { ⚡ SELECTED: CAP_ID; }
                        }
                    }
                }
            }
        }
        ⚡ I: I + 1;
    }
    RETURN SELECTED;
}

DEF c5l_agenda_get_open_gap(gap_bank, gap_id) {
    IF (c5l_safe_atom(gap_id, 128) == 0) { RETURN ""; }
    ⚡ GAP: c5l_bank_find(gap_bank, "GAP_ID=", gap_id);
    IF (GAP == "") { RETURN ""; }
    IF (c5l_gap_valid(GAP) == 0) { RETURN ""; }
    ⚡ STATE: c5l_field(GAP, 5, "STATE=");
    IF (STATE != "OPEN") { RETURN ""; }
    RETURN GAP;
}

DEF c5l_memory_pack(work_id, claim_bank, gap_bank, evidence_ref_bank, revision) {
    IF (c5l_safe_atom(work_id, 128) == 0) { RETURN ""; }
    IF (c5l_digits_only(revision) == 0) { RETURN ""; }
    IF (64 < c5l_bank_count(claim_bank)) { RETURN ""; }
    IF (64 < c5l_bank_count(gap_bank)) { RETURN ""; }
    IF (128 < c5l_bank_count(evidence_ref_bank)) { RETURN ""; }
    RETURN "TYPE=NATIVE_LEARNING_MEMORY\nWORK_ID=" + work_id + "\nREVISION=" + revision + "\nCLAIMS_BEGIN\n" + claim_bank + "\nCLAIMS_END\nGAPS_BEGIN\n" + gap_bank + "\nGAPS_END\nEVIDENCE_REFS_BEGIN\n" + evidence_ref_bank + "\nEVIDENCE_REFS_END";
}
