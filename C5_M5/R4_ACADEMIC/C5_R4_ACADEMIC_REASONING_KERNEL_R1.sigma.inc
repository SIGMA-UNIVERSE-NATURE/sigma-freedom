# C5V3 R4 academic reasoning kernel R1.
# Pure transforms only. No I/O, transport, query generation, source selection, or host semantic substitution.
# Academic synthesis reports evidence posture, not truth. Native capability outputs must retain basis/result hashes.

DEF c5ak1_observation_bank_valid(bank) {
    IF (bank == "") { RETURN 1; }
    IF (128 < c5l2_bank_count(bank)) { RETURN 0; }
    ⚡ LINES: H("str_split", bank, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        IF (LINE != "") { IF (c5as1_observation_valid(LINE) == 0) { RETURN 0; } }
        ⚡ I: I + 1;
    }
    RETURN 1;
}

DEF c5ak1_judgment_bank_valid(bank) {
    IF (bank == "") { RETURN 1; }
    IF (128 < c5l2_bank_count(bank)) { RETURN 0; }
    ⚡ LINES: H("str_split", bank, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        IF (LINE != "") { IF (c5as1_judgment_valid(LINE) == 0) { RETURN 0; } }
        ⚡ I: I + 1;
    }
    RETURN 1;
}

DEF c5ak1_make_passage_observation(obs_id, subject_id, passage, content, capability_result) {
    IF (c5l2_safe_atom(obs_id, 128) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(subject_id, 128) == 0) { RETURN ""; }
    IF (c5ad1_passage_valid(passage) == 0) { RETURN ""; }
    IF (c5d1_payload_valid(content, 512) == 0) { RETURN ""; }
    IF (c5as1_capability_result_valid(capability_result) == 0) { RETURN ""; }
    ⚡ PASSAGE_ID: c5l2_field(passage, 1, "PASSAGE_ID");
    ⚡ CONTENT_SHA: c5l2_field(passage, 5, "CONTENT_SHA");
    ⚡ CAPABILITY_ID: c5l2_field(capability_result, 0, "CAPABILITY_ID");
    ⚡ RESULT_SHA: c5l2_field(capability_result, 1, "RESULT_SHA");
    ⚡ BASIS_SHA: c5l2_field(capability_result, 2, "BASIS_SHA");
    IF (BASIS_SHA != CONTENT_SHA) { RETURN ""; }
    RETURN "TYPE=ACADEMIC_OBSERVATION || OBS_ID=" + obs_id + " || SUBJECT_ID=" + subject_id + " || PASSAGE_ID=" + PASSAGE_ID + " || CONTENT=" + content + " || CAPABILITY_ID=" + CAPABILITY_ID + " || RESULT_SHA=" + RESULT_SHA + " || BASIS_SHA=" + BASIS_SHA;
}

DEF c5ak1_passage_observation_valid(observation, passage) {
    IF (c5as1_observation_valid(observation) == 0) { RETURN 0; }
    IF (c5ad1_passage_valid(passage) == 0) { RETURN 0; }
    IF (c5l2_field(observation, 3, "PASSAGE_ID") != c5l2_field(passage, 1, "PASSAGE_ID")) { RETURN 0; }
    IF (c5l2_field(observation, 7, "BASIS_SHA") != c5l2_field(passage, 5, "CONTENT_SHA")) { RETURN 0; }
    RETURN 1;
}

DEF c5ak1_observation_to_claim(observation, claim_id, revision, uncertainty) {
    IF (c5as1_observation_valid(observation) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(claim_id, 128) == 0) { RETURN ""; }
    IF (c5l2_digits_only(revision) == 0) { RETURN ""; }
    IF (c5l2_digits_only(uncertainty) == 0) { RETURN ""; }
    ⚡ SUBJECT_ID: c5l2_field(observation, 2, "SUBJECT_ID");
    ⚡ CONTENT: c5l2_field(observation, 4, "CONTENT");
    RETURN c5d1_make_claim(claim_id, SUBJECT_ID, CONTENT, "OBSERVED", revision, uncertainty);
}

DEF c5ak1_observation_to_evidence(observation, passage, document, evidence_id) {
    IF (c5ak1_passage_observation_valid(observation, passage) == 0) { RETURN ""; }
    IF (c5ad1_document_valid(document) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(evidence_id, 128) == 0) { RETURN ""; }
    IF (c5l2_field(passage, 2, "DOCUMENT_ID") != c5l2_field(document, 1, "DOCUMENT_ID")) { RETURN ""; }
    ⚡ SUBJECT_ID: c5l2_field(observation, 2, "SUBJECT_ID");
    ⚡ SOURCE_ID: c5l2_field(document, 2, "SOURCE_ID");
    ⚡ SOURCE_VERSION_SHA: c5l2_field(document, 3, "SOURCE_VERSION_SHA");
    ⚡ CONTENT_SHA: c5l2_field(passage, 5, "CONTENT_SHA");
    RETURN c5t2_make_evidence(evidence_id, SOURCE_ID, SOURCE_VERSION_SHA, CONTENT_SHA, SUBJECT_ID);
}

DEF c5ak1_judgment_to_evaluation(judgment, claim, evidence) {
    IF (c5as1_judgment_valid(judgment) == 0) { RETURN ""; }
    IF (c5d1_claim_valid(claim) == 0) { RETURN ""; }
    IF (c5l2_evidence_valid(evidence) == 0) { RETURN ""; }
    ⚡ CLAIM_ID: c5l2_field(claim, 1, "CLAIM_ID");
    ⚡ CLAIM_SUBJECT: c5l2_field(claim, 2, "SUBJECT_ID");
    ⚡ EVIDENCE_ID: c5l2_field(evidence, 1, "EVIDENCE_ID");
    ⚡ EVIDENCE_SOURCE: c5l2_field(evidence, 2, "SOURCE_ID");
    ⚡ EVIDENCE_SHA: c5l2_field(evidence, 4, "ARTIFACT_SHA");
    ⚡ EVIDENCE_SUBJECT: c5l2_field(evidence, 5, "SUBJECT_ID");
    IF (c5l2_field(judgment, 2, "CLAIM_ID") != CLAIM_ID) { RETURN ""; }
    IF (c5l2_field(judgment, 3, "EVIDENCE_ID") != EVIDENCE_ID) { RETURN ""; }
    IF (c5l2_field(judgment, 4, "SOURCE_ID") != EVIDENCE_SOURCE) { RETURN ""; }
    IF (c5l2_field(judgment, 6, "BASIS_SHA") != EVIDENCE_SHA) { RETURN ""; }
    IF (CLAIM_SUBJECT != EVIDENCE_SUBJECT) { RETURN ""; }
    ⚡ EVAL_ID: c5l2_field(judgment, 1, "JUDGMENT_ID");
    ⚡ STANCE: c5l2_field(judgment, 5, "STANCE");
    RETURN c5t2_make_evaluation(EVAL_ID, CLAIM_ID, EVIDENCE_ID, EVIDENCE_SOURCE, STANCE, EVIDENCE_SHA);
}

DEF c5ak1_evaluation_count(evaluation_bank, claim_id) {
    IF (c5d1_evaluation_bank_valid(evaluation_bank) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(claim_id, 128) == 0) { RETURN 0; }
    ⚡ LINES: H("str_split", evaluation_bank, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    ⚡ COUNT: 0;
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        IF (LINE != "") {
            IF (c5l2_evaluation_valid(LINE)) {
                IF (c5l2_field(LINE, 2, "CLAIM_ID") == claim_id) { ⚡ COUNT: COUNT + 1; }
            }
        }
        ⚡ I: I + 1;
    }
    RETURN COUNT;
}

DEF c5ak1_unique_source_count(evaluation_bank, claim_id, stance) {
    IF (c5d1_evaluation_bank_valid(evaluation_bank) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(claim_id, 128) == 0) { RETURN 0; }
    IF (c5l2_stance_valid(stance) == 0) { RETURN 0; }
    ⚡ LINES: H("str_split", evaluation_bank, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    ⚡ COUNT: 0;
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        ⚡ MATCH: 0;
        IF (LINE != "") {
            IF (c5l2_evaluation_valid(LINE)) {
                IF (c5l2_field(LINE, 2, "CLAIM_ID") == claim_id) {
                    IF (c5l2_field(LINE, 5, "STANCE") == stance) { ⚡ MATCH: 1; }
                }
            }
        }
        IF (MATCH) {
            ⚡ SOURCE_ID: c5l2_field(LINE, 4, "SOURCE_ID");
            ⚡ J: 0;
            ⚡ SEEN: 0;
            WHILE (J < I) {
                ⚡ PRIOR: H("list_get", LINES, J, NULL);
                IF (PRIOR != "") {
                    IF (c5l2_evaluation_valid(PRIOR)) {
                        IF (c5l2_field(PRIOR, 2, "CLAIM_ID") == claim_id) {
                            IF (c5l2_field(PRIOR, 5, "STANCE") == stance) {
                                IF (c5l2_field(PRIOR, 4, "SOURCE_ID") == SOURCE_ID) { ⚡ SEEN: 1; }
                            }
                        }
                    }
                }
                ⚡ J: J + 1;
            }
            IF (SEEN == 0) { ⚡ COUNT: COUNT + 1; }
        }
        ⚡ I: I + 1;
    }
    RETURN COUNT;
}

DEF c5ak1_counts_for_claim(evaluation_bank, claim_id) {
    IF (c5d1_evaluation_bank_valid(evaluation_bank) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(claim_id, 128) == 0) { RETURN ""; }
    ⚡ SUPPORT: c5ak1_unique_source_count(evaluation_bank, claim_id, "SUPPORT");
    ⚡ CONTRARY: c5ak1_unique_source_count(evaluation_bank, claim_id, "CONTRARY");
    ⚡ NEUTRAL: c5ak1_unique_source_count(evaluation_bank, claim_id, "NEUTRAL");
    ⚡ TOTAL: c5ak1_evaluation_count(evaluation_bank, claim_id);
    ⚡ SUPPORT_TEXT: "" + SUPPORT;
    ⚡ CONTRARY_TEXT: "" + CONTRARY;
    ⚡ NEUTRAL_TEXT: "" + NEUTRAL;
    ⚡ TOTAL_TEXT: "" + TOTAL;
    RETURN c5as1_make_evidence_counts(SUPPORT_TEXT, CONTRARY_TEXT, NEUTRAL_TEXT, TOTAL_TEXT);
}

DEF c5ak1_synthesis_state(evaluation_bank, claim_id) {
    IF (c5d1_evaluation_bank_valid(evaluation_bank) == 0) { RETURN "UNRESOLVED"; }
    IF (c5l2_safe_atom(claim_id, 128) == 0) { RETURN "UNRESOLVED"; }
    ⚡ SUPPORT: c5ak1_unique_source_count(evaluation_bank, claim_id, "SUPPORT");
    ⚡ CONTRARY: c5ak1_unique_source_count(evaluation_bank, claim_id, "CONTRARY");
    IF (SUPPORT == 0) {
        IF (CONTRARY == 0) { RETURN "UNRESOLVED"; }
        IF (0 < CONTRARY) { RETURN "EVIDENCE_CONTRADICTED"; }
    }
    IF (0 < SUPPORT) {
        IF (CONTRARY == 0) { RETURN "EVIDENCE_SUPPORTED"; }
        IF (0 < CONTRARY) { RETURN "CONTESTED"; }
    }
    RETURN "UNRESOLVED";
}

DEF c5ak1_synthesis_for_claim(evaluation_bank, claim_id, revision) {
    IF (c5l2_digits_only(revision) == 0) { RETURN ""; }
    ⚡ COUNTS: c5ak1_counts_for_claim(evaluation_bank, claim_id);
    IF (c5as1_evidence_counts_valid(COUNTS) == 0) { RETURN ""; }
    ⚡ STATE: c5ak1_synthesis_state(evaluation_bank, claim_id);
    RETURN c5as1_make_synthesis(claim_id, STATE, COUNTS, revision);
}

DEF c5ak1_revise_claim_from_synthesis(claim, synthesis, new_revision, uncertainty) {
    IF (c5d1_claim_valid(claim) == 0) { RETURN ""; }
    IF (c5as1_synthesis_valid(synthesis) == 0) { RETURN ""; }
    IF (c5l2_digits_only(new_revision) == 0) { RETURN ""; }
    IF (c5l2_digits_only(uncertainty) == 0) { RETURN ""; }
    IF (c5l2_field(claim, 1, "CLAIM_ID") != c5l2_field(synthesis, 1, "CLAIM_ID")) { RETURN ""; }
    ⚡ STATE: c5l2_field(synthesis, 2, "STATE");
    ⚡ NEXT_CLASS: "UNRESOLVED";
    IF (STATE == "EVIDENCE_SUPPORTED") { ⚡ NEXT_CLASS: "HYPOTHESIS"; }
    IF (STATE == "EVIDENCE_CONTRADICTED") { ⚡ NEXT_CLASS: "CONTRADICTED"; }
    IF (STATE == "CONTESTED") { ⚡ NEXT_CLASS: "HYPOTHESIS"; }
    RETURN c5d1_claim_revision_record(claim, NEXT_CLASS, uncertainty, new_revision);
}

DEF c5ak1_next_question(work, synthesis, question_id, priority) {
    IF (c5as1_work_valid(work) == 0) { RETURN ""; }
    IF (c5as1_synthesis_valid(synthesis) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(question_id, 128) == 0) { RETURN ""; }
    IF (c5l2_digits_only(priority) == 0) { RETURN ""; }
    ⚡ WORK_ID: c5l2_field(work, 1, "WORK_ID");
    ⚡ SUBJECT_ID: c5l2_field(work, 3, "SUBJECT_ID");
    ⚡ STATE: c5l2_field(synthesis, 2, "STATE");
    IF (STATE == "UNRESOLVED") { RETURN c5as1_make_question(question_id, WORK_ID, SUBJECT_ID, "EVIDENCE", "EVIDENCE_SEARCH", priority); }
    IF (STATE == "EVIDENCE_CONTRADICTED") { RETURN c5as1_make_question(question_id, WORK_ID, SUBJECT_ID, "EVIDENCE", "CLAIM_REVISION_EVIDENCE", priority); }
    IF (STATE == "CONTESTED") { RETURN c5as1_make_question(question_id, WORK_ID, SUBJECT_ID, "CONFLICT", "CONFLICT_RESOLUTION_EVIDENCE", priority); }
    RETURN "";
}

DEF c5ak1_text_capability_question(work, document, cursor, question_id, priority) {
    IF (c5as1_work_valid(work) == 0) { RETURN ""; }
    IF (c5ad1_document_valid(document) == 0) { RETURN ""; }
    IF (c5ad1_cursor_valid(cursor) == 0) { RETURN ""; }
    IF (c5l2_field(document, 1, "DOCUMENT_ID") != c5l2_field(cursor, 1, "DOCUMENT_ID")) { RETURN ""; }
    IF (c5ad1_document_exhausted(cursor)) { RETURN ""; }
    ⚡ WORK_ID: c5l2_field(work, 1, "WORK_ID");
    ⚡ SUBJECT_ID: c5l2_field(work, 3, "SUBJECT_ID");
    RETURN c5as1_make_question(question_id, WORK_ID, SUBJECT_ID, "TEXT_CAPABILITY", "TEXT_INTERPRETATION", priority);
}

DEF c5ak1_citation_question(work, citation, question_id, priority) {
    IF (c5as1_work_valid(work) == 0) { RETURN ""; }
    IF (c5ad1_citation_valid(citation) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(question_id, 128) == 0) { RETURN ""; }
    IF (c5l2_digits_only(priority) == 0) { RETURN ""; }
    ⚡ TARGET_KIND: c5l2_field(citation, 3, "TARGET_KIND");
    ⚡ TARGET_SHA: c5l2_field(citation, 5, "TARGET_SHA");
    IF (TARGET_KIND != "UNRESOLVED") { IF (TARGET_SHA != "NONE") { RETURN ""; } }
    ⚡ WORK_ID: c5l2_field(work, 1, "WORK_ID");
    ⚡ SUBJECT_ID: c5l2_field(work, 3, "SUBJECT_ID");
    RETURN c5as1_make_question(question_id, WORK_ID, SUBJECT_ID, "CITATION", "CITATION_RESOLUTION", priority);
}

DEF c5ak1_pack_assessment(observation_bank, judgment_bank, evaluation_bank, synthesis_bank) {
    IF (c5ak1_observation_bank_valid(observation_bank) == 0) { RETURN ""; }
    IF (c5ak1_judgment_bank_valid(judgment_bank) == 0) { RETURN ""; }
    IF (c5d1_evaluation_bank_valid(evaluation_bank) == 0) { RETURN ""; }
    IF (c5as1_synthesis_bank_valid(synthesis_bank) == 0) { RETURN ""; }
    IF (16384 < H("str_len", observation_bank, NULL, NULL)) { RETURN ""; }
    IF (16384 < H("str_len", judgment_bank, NULL, NULL)) { RETURN ""; }
    IF (16384 < H("str_len", evaluation_bank, NULL, NULL)) { RETURN ""; }
    IF (12288 < H("str_len", synthesis_bank, NULL, NULL)) { RETURN ""; }
    ⚡ OUT: "TYPE=ACADEMIC_ASSESSMENT_MEMORY\nOBSERVATIONS_BEGIN\n" + observation_bank + "\nOBSERVATIONS_END\nJUDGMENTS_BEGIN\n" + judgment_bank + "\nJUDGMENTS_END\nEVALUATIONS_BEGIN\n" + evaluation_bank + "\nEVALUATIONS_END\nSYNTHESES_BEGIN\n" + synthesis_bank + "\nSYNTHESES_END";
    IF (65536 < H("str_len", OUT, NULL, NULL)) { RETURN ""; }
    RETURN OUT;
}

DEF c5ak1_assessment_valid(memory) {
    IF (memory == "") { RETURN 0; }
    IF (65536 < H("str_len", memory, NULL, NULL)) { RETURN 0; }
    ⚡ PREFIX: H("str_split", memory, "TYPE=ACADEMIC_ASSESSMENT_MEMORY\n", NULL);
    IF (H("list_len", PREFIX, NULL, NULL) != 2) { RETURN 0; }
    IF (H("list_get", PREFIX, 0, NULL) != "") { RETURN 0; }
    ⚡ OBSERVATIONS: c5t2_memory_section(memory, "OBSERVATIONS_BEGIN\n", "\nOBSERVATIONS_END");
    ⚡ JUDGMENTS: c5t2_memory_section(memory, "JUDGMENTS_BEGIN\n", "\nJUDGMENTS_END");
    ⚡ EVALUATIONS: c5t2_memory_section(memory, "EVALUATIONS_BEGIN\n", "\nEVALUATIONS_END");
    ⚡ SYNTHESES: c5t2_memory_section(memory, "SYNTHESES_BEGIN\n", "\nSYNTHESES_END");
    IF (c5ak1_observation_bank_valid(OBSERVATIONS) == 0) { RETURN 0; }
    IF (c5ak1_judgment_bank_valid(JUDGMENTS) == 0) { RETURN 0; }
    IF (c5d1_evaluation_bank_valid(EVALUATIONS) == 0) { RETURN 0; }
    IF (c5as1_synthesis_bank_valid(SYNTHESES) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5ak1_memory_section(memory, begin_marker, end_marker) {
    IF (memory == "") { RETURN ""; }
    IF (196608 < H("str_len", memory, NULL, NULL)) { RETURN ""; }
    ⚡ A: H("str_split", memory, begin_marker, NULL);
    IF (H("list_len", A, NULL, NULL) != 2) { RETURN ""; }
    ⚡ AFTER: H("list_get", A, 1, NULL);
    ⚡ B: H("str_split", AFTER, end_marker, NULL);
    IF (H("list_len", B, NULL, NULL) != 2) { RETURN ""; }
    RETURN H("list_get", B, 0, NULL);
}

DEF c5ak1_pack_academic_memory(work, structure_memory, claim_bank, question_bank, evidence_bank, assessment_memory) {
    IF (c5as1_work_valid(work) == 0) { RETURN ""; }
    IF (c5ad1_structure_memory_valid(structure_memory) == 0) { RETURN ""; }
    IF (c5d1_claim_bank_valid(claim_bank) == 0) { RETURN ""; }
    IF (c5as1_question_bank_valid(question_bank) == 0) { RETURN ""; }
    IF (c5l2_evidence_ref_bank_valid(evidence_bank) == 0) { RETURN ""; }
    IF (c5ak1_assessment_valid(assessment_memory) == 0) { RETURN ""; }
    IF (24576 < H("str_len", claim_bank, NULL, NULL)) { RETURN ""; }
    IF (16384 < H("str_len", question_bank, NULL, NULL)) { RETURN ""; }
    IF (32768 < H("str_len", evidence_bank, NULL, NULL)) { RETURN ""; }
    ⚡ OUT: "TYPE=NATIVE_ACADEMIC_MEMORY\nWORK_BEGIN\n" + work + "\nWORK_END\nSTRUCTURE_BEGIN\n" + structure_memory + "\nSTRUCTURE_END\nCLAIMS_BEGIN\n" + claim_bank + "\nCLAIMS_END\nQUESTIONS_BEGIN\n" + question_bank + "\nQUESTIONS_END\nEVIDENCE_REFS_BEGIN\n" + evidence_bank + "\nEVIDENCE_REFS_END\nASSESSMENT_BEGIN\n" + assessment_memory + "\nASSESSMENT_END";
    IF (196608 < H("str_len", OUT, NULL, NULL)) { RETURN ""; }
    RETURN OUT;
}

DEF c5ak1_academic_memory_valid(memory) {
    IF (memory == "") { RETURN 0; }
    IF (196608 < H("str_len", memory, NULL, NULL)) { RETURN 0; }
    ⚡ PREFIX: H("str_split", memory, "TYPE=NATIVE_ACADEMIC_MEMORY\n", NULL);
    IF (H("list_len", PREFIX, NULL, NULL) != 2) { RETURN 0; }
    IF (H("list_get", PREFIX, 0, NULL) != "") { RETURN 0; }
    ⚡ WORK: c5ak1_memory_section(memory, "WORK_BEGIN\n", "\nWORK_END");
    ⚡ STRUCTURE: c5ak1_memory_section(memory, "STRUCTURE_BEGIN\n", "\nSTRUCTURE_END");
    ⚡ CLAIMS: c5ak1_memory_section(memory, "CLAIMS_BEGIN\n", "\nCLAIMS_END");
    ⚡ QUESTIONS: c5ak1_memory_section(memory, "QUESTIONS_BEGIN\n", "\nQUESTIONS_END");
    ⚡ EVIDENCE: c5ak1_memory_section(memory, "EVIDENCE_REFS_BEGIN\n", "\nEVIDENCE_REFS_END");
    ⚡ ASSESSMENT: c5ak1_memory_section(memory, "ASSESSMENT_BEGIN\n", "\nASSESSMENT_END");
    IF (c5as1_work_valid(WORK) == 0) { RETURN 0; }
    IF (c5ad1_structure_memory_valid(STRUCTURE) == 0) { RETURN 0; }
    IF (c5d1_claim_bank_valid(CLAIMS) == 0) { RETURN 0; }
    IF (c5as1_question_bank_valid(QUESTIONS) == 0) { RETURN 0; }
    IF (c5l2_evidence_ref_bank_valid(EVIDENCE) == 0) { RETURN 0; }
    IF (c5ak1_assessment_valid(ASSESSMENT) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5ak1_memory_recall_claim(memory, claim_id) {
    IF (c5ak1_academic_memory_valid(memory) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(claim_id, 128) == 0) { RETURN ""; }
    ⚡ CLAIMS: c5ak1_memory_section(memory, "CLAIMS_BEGIN\n", "\nCLAIMS_END");
    ⚡ CLAIM: c5l2_bank_find_at(CLAIMS, 1, "CLAIM_ID", claim_id);
    IF (c5d1_claim_valid(CLAIM) == 0) { RETURN ""; }
    RETURN CLAIM;
}

DEF c5ak1_memory_recall_synthesis(memory, claim_id) {
    IF (c5ak1_academic_memory_valid(memory) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(claim_id, 128) == 0) { RETURN ""; }
    ⚡ ASSESSMENT: c5ak1_memory_section(memory, "ASSESSMENT_BEGIN\n", "\nASSESSMENT_END");
    ⚡ SYNTHESES: c5t2_memory_section(ASSESSMENT, "SYNTHESES_BEGIN\n", "\nSYNTHESES_END");
    ⚡ SYNTHESIS: c5l2_bank_find_at(SYNTHESES, 1, "CLAIM_ID", claim_id);
    IF (c5as1_synthesis_valid(SYNTHESIS) == 0) { RETURN ""; }
    RETURN SYNTHESIS;
}
