# C5V3 native learning state substrate R2.
# Supersedes R1 before runtime admission.
# Exact schema parsing, fixed field order, byte bounds, native-supplied capability selection.
# Pure state transforms only: no filesystem, transport, persistence, host semantic selection, or source choice.

DEF c5l2_present(value) {
    IF (value == "") { RETURN 0; }
    IF (value == "NONE") { RETURN 0; }
    RETURN 1;
}

DEF c5l2_digits_only(value) {
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

DEF c5l2_hex64(value) {
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

DEF c5l2_safe_atom(value, max_len) {
    IF (value == "") { RETURN 0; }
    ⚡ N: H("str_len", value, NULL, NULL);
    IF (max_len < N) { RETURN 0; }
    ⚡ X: H("str_replace", value, "\n", "");
    IF (X != value) { RETURN 0; }
    ⚡ X: H("str_replace", value, "\r", "");
    IF (X != value) { RETURN 0; }
    ⚡ X: H("str_replace", value, "\t", "");
    IF (X != value) { RETURN 0; }
    ⚡ X: H("str_replace", value, "=", "");
    IF (X != value) { RETURN 0; }
    ⚡ X: H("str_replace", value, " || ", "");
    IF (X != value) { RETURN 0; }
    RETURN 1;
}

DEF c5l2_record_part_count(record) {
    IF (record == "") { RETURN 0; }
    ⚡ PARTS: H("str_split", record, " || ", NULL);
    RETURN H("list_len", PARTS, NULL, NULL);
}

DEF c5l2_field(record, index, key) {
    IF (c5l2_safe_atom(key, 64) == 0) { RETURN ""; }
    ⚡ PARTS: H("str_split", record, " || ", NULL);
    ⚡ N: H("list_len", PARTS, NULL, NULL);
    IF (N <= index) { RETURN ""; }
    ⚡ FIELD: H("list_get", PARTS, index, NULL);
    ⚡ KV: H("str_split", FIELD, "=", NULL);
    ⚡ KN: H("list_len", KV, NULL, NULL);
    IF (KN != 2) { RETURN ""; }
    ⚡ K: H("list_get", KV, 0, NULL);
    IF (K != key) { RETURN ""; }
    RETURN H("list_get", KV, 1, NULL);
}

DEF c5l2_epistemic_class_valid(value) {
    IF (value == "OBSERVED") { RETURN 1; }
    IF (value == "DERIVED") { RETURN 1; }
    IF (value == "HYPOTHESIS") { RETURN 1; }
    IF (value == "UNRESOLVED") { RETURN 1; }
    IF (value == "CONTRADICTED") { RETURN 1; }
    RETURN 0;
}

DEF c5l2_gap_kind_valid(value) {
    IF (value == "EVIDENCE") { RETURN 1; }
    IF (value == "CONFLICT") { RETURN 1; }
    IF (value == "CAPABILITY") { RETURN 1; }
    IF (value == "MEMORY") { RETURN 1; }
    IF (value == "STRUCTURE") { RETURN 1; }
    RETURN 0;
}

DEF c5l2_stance_valid(value) {
    IF (value == "SUPPORT") { RETURN 1; }
    IF (value == "CONTRARY") { RETURN 1; }
    IF (value == "NEUTRAL") { RETURN 1; }
    RETURN 0;
}

DEF c5l2_claim_valid(record) {
    IF (H("str_len", record, NULL, NULL) > 1024) { RETURN 0; }
    IF (c5l2_record_part_count(record) != 6) { RETURN 0; }
    ⚡ TYPE: c5l2_field(record, 0, "TYPE");
    ⚡ CLAIM_ID: c5l2_field(record, 1, "CLAIM_ID");
    ⚡ SUBJECT_ID: c5l2_field(record, 2, "SUBJECT_ID");
    ⚡ CLASS: c5l2_field(record, 3, "CLASS");
    ⚡ REVISION: c5l2_field(record, 4, "REVISION");
    ⚡ UNCERTAINTY: c5l2_field(record, 5, "UNCERTAINTY");
    IF (TYPE != "CLAIM") { RETURN 0; }
    IF (c5l2_safe_atom(CLAIM_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(SUBJECT_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_epistemic_class_valid(CLASS) == 0) { RETURN 0; }
    IF (c5l2_digits_only(REVISION) == 0) { RETURN 0; }
    IF (c5l2_digits_only(UNCERTAINTY) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5l2_gap_valid(record) {
    IF (H("str_len", record, NULL, NULL) > 1536) { RETURN 0; }
    IF (c5l2_record_part_count(record) != 8) { RETURN 0; }
    ⚡ TYPE: c5l2_field(record, 0, "TYPE");
    ⚡ GAP_ID: c5l2_field(record, 1, "GAP_ID");
    ⚡ OBJECTIVE_ID: c5l2_field(record, 2, "OBJECTIVE_ID");
    ⚡ KIND: c5l2_field(record, 3, "KIND");
    ⚡ SUBJECT_ID: c5l2_field(record, 4, "SUBJECT_ID");
    ⚡ STATE: c5l2_field(record, 5, "STATE");
    ⚡ NEED_FAMILY: c5l2_field(record, 6, "NEED_FAMILY");
    ⚡ PRIORITY: c5l2_field(record, 7, "PRIORITY");
    IF (TYPE != "GAP") { RETURN 0; }
    IF (c5l2_safe_atom(GAP_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(OBJECTIVE_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_gap_kind_valid(KIND) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(SUBJECT_ID, 128) == 0) { RETURN 0; }
    IF (STATE != "OPEN") {
        IF (STATE != "RESOLVED") {
            IF (STATE != "HELD") { RETURN 0; }
        }
    }
    IF (c5l2_safe_atom(NEED_FAMILY, 64) == 0) { RETURN 0; }
    IF (c5l2_digits_only(PRIORITY) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5l2_evidence_valid(record) {
    IF (H("str_len", record, NULL, NULL) > 1024) { RETURN 0; }
    IF (c5l2_record_part_count(record) != 6) { RETURN 0; }
    ⚡ TYPE: c5l2_field(record, 0, "TYPE");
    ⚡ EVIDENCE_ID: c5l2_field(record, 1, "EVIDENCE_ID");
    ⚡ SOURCE_ID: c5l2_field(record, 2, "SOURCE_ID");
    ⚡ SOURCE_VERSION_SHA: c5l2_field(record, 3, "SOURCE_VERSION_SHA");
    ⚡ ARTIFACT_SHA: c5l2_field(record, 4, "ARTIFACT_SHA");
    ⚡ SUBJECT_ID: c5l2_field(record, 5, "SUBJECT_ID");
    IF (TYPE != "EVIDENCE") { RETURN 0; }
    IF (c5l2_safe_atom(EVIDENCE_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(SOURCE_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_hex64(SOURCE_VERSION_SHA) == 0) { RETURN 0; }
    IF (c5l2_hex64(ARTIFACT_SHA) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(SUBJECT_ID, 128) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5l2_evaluation_valid(record) {
    IF (H("str_len", record, NULL, NULL) > 1024) { RETURN 0; }
    IF (c5l2_record_part_count(record) != 7) { RETURN 0; }
    ⚡ TYPE: c5l2_field(record, 0, "TYPE");
    ⚡ EVAL_ID: c5l2_field(record, 1, "EVAL_ID");
    ⚡ CLAIM_ID: c5l2_field(record, 2, "CLAIM_ID");
    ⚡ EVIDENCE_ID: c5l2_field(record, 3, "EVIDENCE_ID");
    ⚡ SOURCE_ID: c5l2_field(record, 4, "SOURCE_ID");
    ⚡ STANCE: c5l2_field(record, 5, "STANCE");
    ⚡ BASIS_SHA: c5l2_field(record, 6, "BASIS_SHA");
    IF (TYPE != "EVALUATION") { RETURN 0; }
    IF (c5l2_safe_atom(EVAL_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(CLAIM_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(EVIDENCE_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(SOURCE_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_stance_valid(STANCE) == 0) { RETURN 0; }
    IF (c5l2_hex64(BASIS_SHA) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5l2_request_valid(record) {
    IF (H("str_len", record, NULL, NULL) > 1024) { RETURN 0; }
    IF (c5l2_record_part_count(record) != 5) { RETURN 0; }
    ⚡ TYPE: c5l2_field(record, 0, "TYPE");
    ⚡ REQUEST_ID: c5l2_field(record, 1, "REQUEST_ID");
    ⚡ GAP_ID: c5l2_field(record, 2, "GAP_ID");
    ⚡ NEED_FAMILY: c5l2_field(record, 3, "NEED_FAMILY");
    ⚡ PAYLOAD_SHA: c5l2_field(record, 4, "PAYLOAD_SHA");
    IF (TYPE != "REQUEST") { RETURN 0; }
    IF (c5l2_safe_atom(REQUEST_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(GAP_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(NEED_FAMILY, 64) == 0) { RETURN 0; }
    IF (c5l2_hex64(PAYLOAD_SHA) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5l2_capability_record_valid(record) {
    IF (H("str_len", record, NULL, NULL) > 512) { RETURN 0; }
    IF (c5l2_record_part_count(record) != 4) { RETURN 0; }
    ⚡ TYPE: c5l2_field(record, 0, "TYPE");
    ⚡ CAPABILITY_ID: c5l2_field(record, 1, "CAPABILITY_ID");
    ⚡ FAMILY: c5l2_field(record, 2, "FAMILY");
    ⚡ STATE: c5l2_field(record, 3, "STATE");
    IF (TYPE != "CAPABILITY") { RETURN 0; }
    IF (c5l2_safe_atom(CAPABILITY_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(FAMILY, 64) == 0) { RETURN 0; }
    IF (STATE != "ADMITTED") {
        IF (STATE != "LATENT") {
            IF (STATE != "HOLD") { RETURN 0; }
        }
    }
    RETURN 1;
}

DEF c5l2_bank_count(bank) {
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

DEF c5l2_bank_find_at(bank, index, key, value) {
    IF (bank == "") { RETURN ""; }
    IF (c5l2_safe_atom(key, 64) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(value, 128) == 0) { RETURN ""; }
    ⚡ LINES: H("str_split", bank, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        IF (LINE != "") {
            ⚡ V: c5l2_field(LINE, index, key);
            IF (V == value) { RETURN LINE; }
        }
        ⚡ I: I + 1;
    }
    RETURN "";
}

DEF c5l2_bank_append_bounded(bank, record, max_count, max_bytes) {
    IF (record == "") { RETURN ""; }
    ⚡ R: H("str_replace", record, "\n", "");
    IF (R != record) { RETURN ""; }
    ⚡ COUNT: c5l2_bank_count(bank);
    IF (max_count <= COUNT) { RETURN ""; }
    ⚡ NEW: record;
    IF (bank != "") { ⚡ NEW: bank + "\n" + record; }
    IF (max_bytes < H("str_len", NEW, NULL, NULL)) { RETURN ""; }
    RETURN NEW;
}

DEF c5l2_source_seen_for_claim(eval_bank, claim_id, source_id, stance) {
    IF (eval_bank == "") { RETURN 0; }
    ⚡ LINES: H("str_split", eval_bank, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        IF (LINE != "") {
            IF (c5l2_evaluation_valid(LINE)) {
                ⚡ C: c5l2_field(LINE, 2, "CLAIM_ID");
                ⚡ S: c5l2_field(LINE, 4, "SOURCE_ID");
                ⚡ T: c5l2_field(LINE, 5, "STANCE");
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

DEF c5l2_distinct_source_count_for_stance(eval_bank, claim_id, stance) {
    IF (eval_bank == "") { RETURN 0; }
    ⚡ LINES: H("str_split", eval_bank, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    ⚡ SEEN: "";
    ⚡ COUNT: 0;
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        IF (LINE != "") {
            IF (c5l2_evaluation_valid(LINE)) {
                ⚡ C: c5l2_field(LINE, 2, "CLAIM_ID");
                ⚡ S: c5l2_field(LINE, 4, "SOURCE_ID");
                ⚡ T: c5l2_field(LINE, 5, "STANCE");
                IF (C == claim_id) {
                    IF (T == stance) {
                        ⚡ MARK: "[" + S + "]";
                        ⚡ REMOVED: H("str_replace", SEEN, MARK, "");
                        IF (REMOVED == SEEN) {
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

DEF c5l2_evidence_posture(eval_bank, claim_id) {
    ⚡ SUPPORT: c5l2_distinct_source_count_for_stance(eval_bank, claim_id, "SUPPORT");
    ⚡ CONTRARY: c5l2_distinct_source_count_for_stance(eval_bank, claim_id, "CONTRARY");
    IF (SUPPORT == 0) {
        IF (CONTRARY == 0) { RETURN "UNRESOLVED"; }
        RETURN "CONTRARY_ONLY";
    }
    IF (CONTRARY == 0) { RETURN "SUPPORTED_ONLY"; }
    RETURN "CONTESTED";
}

DEF c5l2_claim_revision_record(old_claim, new_class, uncertainty, new_revision) {
    IF (c5l2_claim_valid(old_claim) == 0) { RETURN ""; }
    IF (c5l2_epistemic_class_valid(new_class) == 0) { RETURN ""; }
    IF (c5l2_digits_only(uncertainty) == 0) { RETURN ""; }
    IF (c5l2_digits_only(new_revision) == 0) { RETURN ""; }
    ⚡ CLAIM_ID: c5l2_field(old_claim, 1, "CLAIM_ID");
    ⚡ SUBJECT_ID: c5l2_field(old_claim, 2, "SUBJECT_ID");
    RETURN "TYPE=CLAIM || CLAIM_ID=" + CLAIM_ID + " || SUBJECT_ID=" + SUBJECT_ID + " || CLASS=" + new_class + " || REVISION=" + new_revision + " || UNCERTAINTY=" + uncertainty;
}

DEF c5l2_capability_registry_has(registry, capability_id, need_family) {
    IF (registry == "") { RETURN 0; }
    IF (c5l2_safe_atom(capability_id, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(need_family, 64) == 0) { RETURN 0; }
    ⚡ LINES: H("str_split", registry, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        IF (c5l2_capability_record_valid(LINE)) {
            ⚡ CAP: c5l2_field(LINE, 1, "CAPABILITY_ID");
            ⚡ FAMILY: c5l2_field(LINE, 2, "FAMILY");
            ⚡ STATE: c5l2_field(LINE, 3, "STATE");
            IF (CAP == capability_id) {
                IF (FAMILY == need_family) {
                    IF (STATE == "ADMITTED") { RETURN 1; }
                }
            }
        }
        ⚡ I: I + 1;
    }
    RETURN 0;
}

DEF c5l2_agenda_get_open_gap(gap_bank, gap_id) {
    IF (c5l2_safe_atom(gap_id, 128) == 0) { RETURN ""; }
    ⚡ GAP: c5l2_bank_find_at(gap_bank, 1, "GAP_ID", gap_id);
    IF (GAP == "") { RETURN ""; }
    IF (c5l2_gap_valid(GAP) == 0) { RETURN ""; }
    ⚡ STATE: c5l2_field(GAP, 5, "STATE");
    IF (STATE != "OPEN") { RETURN ""; }
    RETURN GAP;
}

DEF c5l2_claim_bank_valid(bank) {
    IF (bank == "") { RETURN 1; }
    ⚡ LINES: H("str_split", bank, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        IF (LINE != "") {
            IF (c5l2_claim_valid(LINE) == 0) { RETURN 0; }
        }
        ⚡ I: I + 1;
    }
    RETURN 1;
}

DEF c5l2_gap_bank_valid(bank) {
    IF (bank == "") { RETURN 1; }
    ⚡ LINES: H("str_split", bank, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        IF (LINE != "") {
            IF (c5l2_gap_valid(LINE) == 0) { RETURN 0; }
        }
        ⚡ I: I + 1;
    }
    RETURN 1;
}

DEF c5l2_evidence_ref_bank_valid(bank) {
    IF (bank == "") { RETURN 1; }
    ⚡ LINES: H("str_split", bank, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        IF (LINE != "") {
            IF (c5l2_evidence_valid(LINE) == 0) { RETURN 0; }
        }
        ⚡ I: I + 1;
    }
    RETURN 1;
}

DEF c5l2_memory_pack(work_id, claim_bank, gap_bank, evidence_ref_bank, revision) {
    IF (c5l2_safe_atom(work_id, 128) == 0) { RETURN ""; }
    IF (c5l2_digits_only(revision) == 0) { RETURN ""; }
    IF (64 < c5l2_bank_count(claim_bank)) { RETURN ""; }
    IF (64 < c5l2_bank_count(gap_bank)) { RETURN ""; }
    IF (128 < c5l2_bank_count(evidence_ref_bank)) { RETURN ""; }
    IF (c5l2_claim_bank_valid(claim_bank) == 0) { RETURN ""; }
    IF (c5l2_gap_bank_valid(gap_bank) == 0) { RETURN ""; }
    IF (c5l2_evidence_ref_bank_valid(evidence_ref_bank) == 0) { RETURN ""; }
    IF (16384 < H("str_len", claim_bank, NULL, NULL)) { RETURN ""; }
    IF (16384 < H("str_len", gap_bank, NULL, NULL)) { RETURN ""; }
    IF (32768 < H("str_len", evidence_ref_bank, NULL, NULL)) { RETURN ""; }
    ⚡ MEMORY: "TYPE=NATIVE_LEARNING_MEMORY\nWORK_ID=" + work_id + "\nREVISION=" + revision + "\nCLAIMS_BEGIN\n" + claim_bank + "\nCLAIMS_END\nGAPS_BEGIN\n" + gap_bank + "\nGAPS_END\nEVIDENCE_REFS_BEGIN\n" + evidence_ref_bank + "\nEVIDENCE_REFS_END";
    IF (65536 < H("str_len", MEMORY, NULL, NULL)) { RETURN ""; }
    RETURN MEMORY;
}
