# C5V3 R4 durable learning model R1.
# Adds claim content and evaluation history required for source-removal + restart reasoning.
# Depends on R4 R2 state/transitions. Pure transforms only; no direct I/O.

DEF c5d1_payload_valid(value, max_len) {
    IF (value == "") { RETURN 0; }
    IF (max_len < H("str_len", value, NULL, NULL)) { RETURN 0; }
    ⚡ X: H("str_replace", value, "\n", "");
    IF (X != value) { RETURN 0; }
    ⚡ X: H("str_replace", value, "\r", "");
    IF (X != value) { RETURN 0; }
    ⚡ X: H("str_replace", value, "\t", "");
    IF (X != value) { RETURN 0; }
    ⚡ X: H("str_replace", value, " || ", "");
    IF (X != value) { RETURN 0; }
    ⚡ X: H("str_replace", value, "=", "");
    IF (X != value) { RETURN 0; }
    RETURN 1;
}

DEF c5d1_claim_valid(record) {
    IF (H("str_len", record, NULL, NULL) > 2048) { RETURN 0; }
    IF (c5l2_record_part_count(record) != 7) { RETURN 0; }
    ⚡ TYPE: c5l2_field(record, 0, "TYPE");
    ⚡ CLAIM_ID: c5l2_field(record, 1, "CLAIM_ID");
    ⚡ SUBJECT_ID: c5l2_field(record, 2, "SUBJECT_ID");
    ⚡ CONTENT: c5l2_field(record, 3, "CONTENT");
    ⚡ CLASS: c5l2_field(record, 4, "CLASS");
    ⚡ REVISION: c5l2_field(record, 5, "REVISION");
    ⚡ UNCERTAINTY: c5l2_field(record, 6, "UNCERTAINTY");
    IF (TYPE != "DURABLE_CLAIM") { RETURN 0; }
    IF (c5l2_safe_atom(CLAIM_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(SUBJECT_ID, 128) == 0) { RETURN 0; }
    IF (c5d1_payload_valid(CONTENT, 512) == 0) { RETURN 0; }
    IF (c5l2_epistemic_class_valid(CLASS) == 0) { RETURN 0; }
    IF (c5l2_digits_only(REVISION) == 0) { RETURN 0; }
    IF (c5l2_digits_only(UNCERTAINTY) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5d1_make_claim(claim_id, subject_id, content, class_name, revision, uncertainty) {
    IF (c5l2_safe_atom(claim_id, 128) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(subject_id, 128) == 0) { RETURN ""; }
    IF (c5d1_payload_valid(content, 512) == 0) { RETURN ""; }
    IF (c5l2_epistemic_class_valid(class_name) == 0) { RETURN ""; }
    IF (c5l2_digits_only(revision) == 0) { RETURN ""; }
    IF (c5l2_digits_only(uncertainty) == 0) { RETURN ""; }
    RETURN "TYPE=DURABLE_CLAIM || CLAIM_ID=" + claim_id + " || SUBJECT_ID=" + subject_id + " || CONTENT=" + content + " || CLASS=" + class_name + " || REVISION=" + revision + " || UNCERTAINTY=" + uncertainty;
}

DEF c5d1_claim_revision_record(old_claim, new_class, uncertainty, new_revision) {
    IF (c5d1_claim_valid(old_claim) == 0) { RETURN ""; }
    IF (c5l2_epistemic_class_valid(new_class) == 0) { RETURN ""; }
    IF (c5l2_digits_only(uncertainty) == 0) { RETURN ""; }
    IF (c5l2_digits_only(new_revision) == 0) { RETURN ""; }
    ⚡ CLAIM_ID: c5l2_field(old_claim, 1, "CLAIM_ID");
    ⚡ SUBJECT_ID: c5l2_field(old_claim, 2, "SUBJECT_ID");
    ⚡ CONTENT: c5l2_field(old_claim, 3, "CONTENT");
    RETURN c5d1_make_claim(CLAIM_ID, SUBJECT_ID, CONTENT, new_class, new_revision, uncertainty);
}

DEF c5d1_claim_bank_valid(bank) {
    IF (bank == "") { RETURN 1; }
    ⚡ LINES: H("str_split", bank, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        IF (LINE != "") { IF (c5d1_claim_valid(LINE) == 0) { RETURN 0; } }
        ⚡ I: I + 1;
    }
    RETURN 1;
}

DEF c5d1_evaluation_bank_valid(bank) {
    IF (bank == "") { RETURN 1; }
    ⚡ LINES: H("str_split", bank, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        IF (LINE != "") { IF (c5l2_evaluation_valid(LINE) == 0) { RETURN 0; } }
        ⚡ I: I + 1;
    }
    RETURN 1;
}

DEF c5d1_memory_pack(work_id, claim_bank, gap_bank, evidence_ref_bank, evaluation_bank, revision) {
    IF (c5l2_safe_atom(work_id, 128) == 0) { RETURN ""; }
    IF (c5l2_digits_only(revision) == 0) { RETURN ""; }
    IF (64 < c5l2_bank_count(claim_bank)) { RETURN ""; }
    IF (64 < c5l2_bank_count(gap_bank)) { RETURN ""; }
    IF (128 < c5l2_bank_count(evidence_ref_bank)) { RETURN ""; }
    IF (128 < c5l2_bank_count(evaluation_bank)) { RETURN ""; }
    IF (c5d1_claim_bank_valid(claim_bank) == 0) { RETURN ""; }
    IF (c5l2_gap_bank_valid(gap_bank) == 0) { RETURN ""; }
    IF (c5l2_evidence_ref_bank_valid(evidence_ref_bank) == 0) { RETURN ""; }
    IF (c5d1_evaluation_bank_valid(evaluation_bank) == 0) { RETURN ""; }
    IF (24576 < H("str_len", claim_bank, NULL, NULL)) { RETURN ""; }
    IF (16384 < H("str_len", gap_bank, NULL, NULL)) { RETURN ""; }
    IF (32768 < H("str_len", evidence_ref_bank, NULL, NULL)) { RETURN ""; }
    IF (32768 < H("str_len", evaluation_bank, NULL, NULL)) { RETURN ""; }
    ⚡ MEMORY: "TYPE=NATIVE_DURABLE_LEARNING_MEMORY\nWORK_ID=" + work_id + "\nREVISION=" + revision + "\nCLAIMS_BEGIN\n" + claim_bank + "\nCLAIMS_END\nGAPS_BEGIN\n" + gap_bank + "\nGAPS_END\nEVIDENCE_REFS_BEGIN\n" + evidence_ref_bank + "\nEVIDENCE_REFS_END\nEVALUATIONS_BEGIN\n" + evaluation_bank + "\nEVALUATIONS_END";
    IF (98304 < H("str_len", MEMORY, NULL, NULL)) { RETURN ""; }
    RETURN MEMORY;
}

DEF c5d1_memory_recall_claim(memory, claim_id) {
    ⚡ CLAIMS: c5t2_memory_section(memory, "CLAIMS_BEGIN\n", "\nCLAIMS_END");
    IF (CLAIMS == "") { RETURN ""; }
    ⚡ CLAIM: c5l2_bank_find_at(CLAIMS, 1, "CLAIM_ID", claim_id);
    IF (CLAIM == "") { RETURN ""; }
    IF (c5d1_claim_valid(CLAIM) == 0) { RETURN ""; }
    RETURN CLAIM;
}

DEF c5d1_memory_recall_evaluations(memory, claim_id) {
    ⚡ EVALS: c5t2_memory_section(memory, "EVALUATIONS_BEGIN\n", "\nEVALUATIONS_END");
    IF (EVALS == "") { RETURN ""; }
    ⚡ LINES: H("str_split", EVALS, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    ⚡ OUT: "";
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        IF (LINE != "") {
            IF (c5l2_evaluation_valid(LINE)) {
                IF (c5l2_field(LINE, 2, "CLAIM_ID") == claim_id) {
                    IF (OUT == "") { ⚡ OUT: LINE; }
                    IF (OUT != "") { IF (OUT != LINE) { ⚡ OUT: OUT + "\n" + LINE; } }
                }
            }
        }
        ⚡ I: I + 1;
    }
    RETURN OUT;
}

DEF c5d1_memory_evidence_posture(memory, claim_id) {
    ⚡ EVALS: c5d1_memory_recall_evaluations(memory, claim_id);
    IF (EVALS == "") { RETURN "UNRESOLVED"; }
    RETURN c5l2_evidence_posture(EVALS, claim_id);
}
