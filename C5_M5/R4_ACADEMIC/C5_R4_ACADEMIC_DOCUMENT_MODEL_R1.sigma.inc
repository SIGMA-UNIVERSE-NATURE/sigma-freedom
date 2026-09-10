# C5V3 R4 academic document/provenance model R1.
# Pure structural model. EOF means byte exhaustion only; it never means understood, summarized, or learned.
# Source identity, version, artifact hashes, passage offsets, and citations remain explicit.

DEF c5ad1_content_kind_valid(value) {
    IF (value == "TEXT") { RETURN 1; }
    IF (value == "HTML") { RETURN 1; }
    IF (value == "XML") { RETURN 1; }
    IF (value == "JSON") { RETURN 1; }
    IF (value == "PDF") { RETURN 1; }
    IF (value == "EPUB") { RETURN 1; }
    IF (value == "AUDIO") { RETURN 1; }
    IF (value == "BINARY") { RETURN 1; }
    IF (value == "UNKNOWN") { RETURN 1; }
    RETURN 0;
}

DEF c5ad1_eof_state_valid(value) {
    IF (value == "MORE") { RETURN 1; }
    IF (value == "EOF") { RETURN 1; }
    RETURN 0;
}

DEF c5ad1_none_or_hex64(value) {
    IF (value == "NONE") { RETURN 1; }
    RETURN c5l2_hex64(value);
}

DEF c5ad1_document_binding_valid(record) {
    IF (H("str_len", record, NULL, NULL) > 1024) { RETURN 0; }
    IF (c5l2_record_part_count(record) != 5) { RETURN 0; }
    ⚡ TYPE: c5l2_field(record, 0, "TYPE");
    ⚡ SOURCE_ID: c5l2_field(record, 1, "SOURCE_ID");
    ⚡ SOURCE_VERSION_SHA: c5l2_field(record, 2, "SOURCE_VERSION_SHA");
    ⚡ CONTENT_KIND: c5l2_field(record, 3, "CONTENT_KIND");
    ⚡ PROVENANCE_SHA: c5l2_field(record, 4, "PROVENANCE_SHA");
    IF (TYPE != "ACADEMIC_DOCUMENT_BINDING") { RETURN 0; }
    IF (c5l2_safe_atom(SOURCE_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_hex64(SOURCE_VERSION_SHA) == 0) { RETURN 0; }
    IF (c5ad1_content_kind_valid(CONTENT_KIND) == 0) { RETURN 0; }
    IF (c5l2_hex64(PROVENANCE_SHA) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5ad1_make_document_binding(source_id, source_version_sha, content_kind, provenance_sha) {
    IF (c5l2_safe_atom(source_id, 128) == 0) { RETURN ""; }
    IF (c5l2_hex64(source_version_sha) == 0) { RETURN ""; }
    IF (c5ad1_content_kind_valid(content_kind) == 0) { RETURN ""; }
    IF (c5l2_hex64(provenance_sha) == 0) { RETURN ""; }
    RETURN "TYPE=ACADEMIC_DOCUMENT_BINDING || SOURCE_ID=" + source_id + " || SOURCE_VERSION_SHA=" + source_version_sha + " || CONTENT_KIND=" + content_kind + " || PROVENANCE_SHA=" + provenance_sha;
}

DEF c5ad1_document_valid(record) {
    IF (H("str_len", record, NULL, NULL) > 2048) { RETURN 0; }
    IF (c5l2_record_part_count(record) != 8) { RETURN 0; }
    ⚡ TYPE: c5l2_field(record, 0, "TYPE");
    ⚡ DOCUMENT_ID: c5l2_field(record, 1, "DOCUMENT_ID");
    ⚡ SOURCE_ID: c5l2_field(record, 2, "SOURCE_ID");
    ⚡ SOURCE_VERSION_SHA: c5l2_field(record, 3, "SOURCE_VERSION_SHA");
    ⚡ DOCUMENT_SHA: c5l2_field(record, 4, "DOCUMENT_SHA");
    ⚡ BYTE_LEN: c5l2_field(record, 5, "BYTE_LEN");
    ⚡ CONTENT_KIND: c5l2_field(record, 6, "CONTENT_KIND");
    ⚡ PROVENANCE_SHA: c5l2_field(record, 7, "PROVENANCE_SHA");
    IF (TYPE != "ACADEMIC_DOCUMENT") { RETURN 0; }
    IF (c5l2_safe_atom(DOCUMENT_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(SOURCE_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_hex64(SOURCE_VERSION_SHA) == 0) { RETURN 0; }
    IF (c5l2_hex64(DOCUMENT_SHA) == 0) { RETURN 0; }
    IF (c5l2_digits_only(BYTE_LEN) == 0) { RETURN 0; }
    IF (c5ad1_content_kind_valid(CONTENT_KIND) == 0) { RETURN 0; }
    IF (c5l2_hex64(PROVENANCE_SHA) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5ad1_make_document(document_id, document_sha, byte_len, binding) {
    IF (c5l2_safe_atom(document_id, 128) == 0) { RETURN ""; }
    IF (c5l2_hex64(document_sha) == 0) { RETURN ""; }
    IF (c5l2_digits_only(byte_len) == 0) { RETURN ""; }
    IF (c5ad1_document_binding_valid(binding) == 0) { RETURN ""; }
    ⚡ SOURCE_ID: c5l2_field(binding, 1, "SOURCE_ID");
    ⚡ SOURCE_VERSION_SHA: c5l2_field(binding, 2, "SOURCE_VERSION_SHA");
    ⚡ CONTENT_KIND: c5l2_field(binding, 3, "CONTENT_KIND");
    ⚡ PROVENANCE_SHA: c5l2_field(binding, 4, "PROVENANCE_SHA");
    RETURN "TYPE=ACADEMIC_DOCUMENT || DOCUMENT_ID=" + document_id + " || SOURCE_ID=" + SOURCE_ID + " || SOURCE_VERSION_SHA=" + SOURCE_VERSION_SHA + " || DOCUMENT_SHA=" + document_sha + " || BYTE_LEN=" + byte_len + " || CONTENT_KIND=" + CONTENT_KIND + " || PROVENANCE_SHA=" + PROVENANCE_SHA;
}

DEF c5ad1_passage_valid(record) {
    IF (H("str_len", record, NULL, NULL) > 1792) { RETURN 0; }
    IF (c5l2_record_part_count(record) != 7) { RETURN 0; }
    ⚡ TYPE: c5l2_field(record, 0, "TYPE");
    ⚡ PASSAGE_ID: c5l2_field(record, 1, "PASSAGE_ID");
    ⚡ DOCUMENT_ID: c5l2_field(record, 2, "DOCUMENT_ID");
    ⚡ START_OFFSET: c5l2_field(record, 3, "START_OFFSET");
    ⚡ END_OFFSET: c5l2_field(record, 4, "END_OFFSET");
    ⚡ CONTENT_SHA: c5l2_field(record, 5, "CONTENT_SHA");
    ⚡ EOF_STATE: c5l2_field(record, 6, "EOF_STATE");
    IF (TYPE != "ACADEMIC_PASSAGE") { RETURN 0; }
    IF (c5l2_safe_atom(PASSAGE_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(DOCUMENT_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_digits_only(START_OFFSET) == 0) { RETURN 0; }
    IF (c5l2_digits_only(END_OFFSET) == 0) { RETURN 0; }
    IF (START_OFFSET == END_OFFSET) { RETURN 0; }
    IF (c5l2_hex64(CONTENT_SHA) == 0) { RETURN 0; }
    IF (c5ad1_eof_state_valid(EOF_STATE) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5ad1_make_passage(passage_id, document_id, start_offset, end_offset, content_sha, eof_state) {
    IF (c5l2_safe_atom(passage_id, 128) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(document_id, 128) == 0) { RETURN ""; }
    IF (c5l2_digits_only(start_offset) == 0) { RETURN ""; }
    IF (c5l2_digits_only(end_offset) == 0) { RETURN ""; }
    IF (start_offset == end_offset) { RETURN ""; }
    IF (c5l2_hex64(content_sha) == 0) { RETURN ""; }
    IF (c5ad1_eof_state_valid(eof_state) == 0) { RETURN ""; }
    RETURN "TYPE=ACADEMIC_PASSAGE || PASSAGE_ID=" + passage_id + " || DOCUMENT_ID=" + document_id + " || START_OFFSET=" + start_offset + " || END_OFFSET=" + end_offset + " || CONTENT_SHA=" + content_sha + " || EOF_STATE=" + eof_state;
}

DEF c5ad1_cursor_valid(record) {
    IF (H("str_len", record, NULL, NULL) > 1024) { RETURN 0; }
    IF (c5l2_record_part_count(record) != 5) { RETURN 0; }
    ⚡ TYPE: c5l2_field(record, 0, "TYPE");
    ⚡ DOCUMENT_ID: c5l2_field(record, 1, "DOCUMENT_ID");
    ⚡ NEXT_OFFSET: c5l2_field(record, 2, "NEXT_OFFSET");
    ⚡ EOF_STATE: c5l2_field(record, 3, "EOF_STATE");
    ⚡ LAST_PASSAGE_SHA: c5l2_field(record, 4, "LAST_PASSAGE_SHA");
    IF (TYPE != "ACADEMIC_CURSOR") { RETURN 0; }
    IF (c5l2_safe_atom(DOCUMENT_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_digits_only(NEXT_OFFSET) == 0) { RETURN 0; }
    IF (c5ad1_eof_state_valid(EOF_STATE) == 0) { RETURN 0; }
    IF (c5ad1_none_or_hex64(LAST_PASSAGE_SHA) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5ad1_make_cursor(document_id, next_offset, eof_state, last_passage_sha) {
    IF (c5l2_safe_atom(document_id, 128) == 0) { RETURN ""; }
    IF (c5l2_digits_only(next_offset) == 0) { RETURN ""; }
    IF (c5ad1_eof_state_valid(eof_state) == 0) { RETURN ""; }
    IF (c5ad1_none_or_hex64(last_passage_sha) == 0) { RETURN ""; }
    RETURN "TYPE=ACADEMIC_CURSOR || DOCUMENT_ID=" + document_id + " || NEXT_OFFSET=" + next_offset + " || EOF_STATE=" + eof_state + " || LAST_PASSAGE_SHA=" + last_passage_sha;
}

DEF c5ad1_cursor_advance(cursor, passage) {
    IF (c5ad1_cursor_valid(cursor) == 0) { RETURN ""; }
    IF (c5ad1_passage_valid(passage) == 0) { RETURN ""; }
    ⚡ DOCUMENT_ID: c5l2_field(cursor, 1, "DOCUMENT_ID");
    ⚡ NEXT_OFFSET: c5l2_field(cursor, 2, "NEXT_OFFSET");
    ⚡ CURSOR_EOF: c5l2_field(cursor, 3, "EOF_STATE");
    ⚡ PASSAGE_DOCUMENT_ID: c5l2_field(passage, 2, "DOCUMENT_ID");
    ⚡ START_OFFSET: c5l2_field(passage, 3, "START_OFFSET");
    ⚡ END_OFFSET: c5l2_field(passage, 4, "END_OFFSET");
    ⚡ CONTENT_SHA: c5l2_field(passage, 5, "CONTENT_SHA");
    ⚡ EOF_STATE: c5l2_field(passage, 6, "EOF_STATE");
    IF (CURSOR_EOF == "EOF") { RETURN ""; }
    IF (DOCUMENT_ID != PASSAGE_DOCUMENT_ID) { RETURN ""; }
    IF (NEXT_OFFSET != START_OFFSET) { RETURN ""; }
    RETURN c5ad1_make_cursor(DOCUMENT_ID, END_OFFSET, EOF_STATE, CONTENT_SHA);
}

DEF c5ad1_document_exhausted(cursor) {
    IF (c5ad1_cursor_valid(cursor) == 0) { RETURN 0; }
    IF (c5l2_field(cursor, 3, "EOF_STATE") == "EOF") { RETURN 1; }
    RETURN 0;
}

DEF c5ad1_citation_target_kind_valid(value) {
    IF (value == "DOCUMENT") { RETURN 1; }
    IF (value == "PASSAGE") { RETURN 1; }
    IF (value == "EXTERNAL") { RETURN 1; }
    IF (value == "UNRESOLVED") { RETURN 1; }
    RETURN 0;
}

DEF c5ad1_citation_valid(record) {
    IF (H("str_len", record, NULL, NULL) > 1536) { RETURN 0; }
    IF (c5l2_record_part_count(record) != 6) { RETURN 0; }
    ⚡ TYPE: c5l2_field(record, 0, "TYPE");
    ⚡ CITATION_ID: c5l2_field(record, 1, "CITATION_ID");
    ⚡ FROM_PASSAGE_ID: c5l2_field(record, 2, "FROM_PASSAGE_ID");
    ⚡ TARGET_KIND: c5l2_field(record, 3, "TARGET_KIND");
    ⚡ TARGET_ID: c5l2_field(record, 4, "TARGET_ID");
    ⚡ TARGET_SHA: c5l2_field(record, 5, "TARGET_SHA");
    IF (TYPE != "ACADEMIC_CITATION") { RETURN 0; }
    IF (c5l2_safe_atom(CITATION_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(FROM_PASSAGE_ID, 128) == 0) { RETURN 0; }
    IF (c5ad1_citation_target_kind_valid(TARGET_KIND) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(TARGET_ID, 256) == 0) { RETURN 0; }
    IF (c5ad1_none_or_hex64(TARGET_SHA) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5ad1_make_citation(citation_id, from_passage_id, target_kind, target_id, target_sha) {
    IF (c5l2_safe_atom(citation_id, 128) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(from_passage_id, 128) == 0) { RETURN ""; }
    IF (c5ad1_citation_target_kind_valid(target_kind) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(target_id, 256) == 0) { RETURN ""; }
    IF (c5ad1_none_or_hex64(target_sha) == 0) { RETURN ""; }
    RETURN "TYPE=ACADEMIC_CITATION || CITATION_ID=" + citation_id + " || FROM_PASSAGE_ID=" + from_passage_id + " || TARGET_KIND=" + target_kind + " || TARGET_ID=" + target_id + " || TARGET_SHA=" + target_sha;
}

DEF c5ad1_document_bank_valid(bank) {
    IF (bank == "") { RETURN 1; }
    IF (64 < c5l2_bank_count(bank)) { RETURN 0; }
    ⚡ LINES: H("str_split", bank, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        IF (LINE != "") { IF (c5ad1_document_valid(LINE) == 0) { RETURN 0; } }
        ⚡ I: I + 1;
    }
    RETURN 1;
}

DEF c5ad1_passage_bank_valid(bank) {
    IF (bank == "") { RETURN 1; }
    IF (256 < c5l2_bank_count(bank)) { RETURN 0; }
    ⚡ LINES: H("str_split", bank, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        IF (LINE != "") { IF (c5ad1_passage_valid(LINE) == 0) { RETURN 0; } }
        ⚡ I: I + 1;
    }
    RETURN 1;
}

DEF c5ad1_citation_bank_valid(bank) {
    IF (bank == "") { RETURN 1; }
    IF (256 < c5l2_bank_count(bank)) { RETURN 0; }
    ⚡ LINES: H("str_split", bank, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        IF (LINE != "") { IF (c5ad1_citation_valid(LINE) == 0) { RETURN 0; } }
        ⚡ I: I + 1;
    }
    RETURN 1;
}

DEF c5ad1_cursor_bank_valid(bank) {
    IF (bank == "") { RETURN 1; }
    IF (64 < c5l2_bank_count(bank)) { RETURN 0; }
    ⚡ LINES: H("str_split", bank, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    ⚡ I: 0;
    WHILE (I < N) {
        ⚡ LINE: H("list_get", LINES, I, NULL);
        IF (LINE != "") { IF (c5ad1_cursor_valid(LINE) == 0) { RETURN 0; } }
        ⚡ I: I + 1;
    }
    RETURN 1;
}

DEF c5ad1_pack_structure(document_bank, passage_bank, citation_bank, cursor_bank) {
    IF (c5ad1_document_bank_valid(document_bank) == 0) { RETURN ""; }
    IF (c5ad1_passage_bank_valid(passage_bank) == 0) { RETURN ""; }
    IF (c5ad1_citation_bank_valid(citation_bank) == 0) { RETURN ""; }
    IF (c5ad1_cursor_bank_valid(cursor_bank) == 0) { RETURN ""; }
    IF (16384 < H("str_len", document_bank, NULL, NULL)) { RETURN ""; }
    IF (24576 < H("str_len", passage_bank, NULL, NULL)) { RETURN ""; }
    IF (12288 < H("str_len", citation_bank, NULL, NULL)) { RETURN ""; }
    IF (8192 < H("str_len", cursor_bank, NULL, NULL)) { RETURN ""; }
    ⚡ OUT: "TYPE=ACADEMIC_STRUCTURE_MEMORY\nDOCUMENTS_BEGIN\n" + document_bank + "\nDOCUMENTS_END\nPASSAGES_BEGIN\n" + passage_bank + "\nPASSAGES_END\nCITATIONS_BEGIN\n" + citation_bank + "\nCITATIONS_END\nCURSORS_BEGIN\n" + cursor_bank + "\nCURSORS_END";
    IF (65536 < H("str_len", OUT, NULL, NULL)) { RETURN ""; }
    RETURN OUT;
}

DEF c5ad1_structure_memory_valid(memory) {
    IF (memory == "") { RETURN 0; }
    IF (65536 < H("str_len", memory, NULL, NULL)) { RETURN 0; }
    ⚡ DOCUMENTS: c5t2_memory_section(memory, "DOCUMENTS_BEGIN\n", "\nDOCUMENTS_END");
    ⚡ PASSAGES: c5t2_memory_section(memory, "PASSAGES_BEGIN\n", "\nPASSAGES_END");
    ⚡ CITATIONS: c5t2_memory_section(memory, "CITATIONS_BEGIN\n", "\nCITATIONS_END");
    ⚡ CURSORS: c5t2_memory_section(memory, "CURSORS_BEGIN\n", "\nCURSORS_END");
    IF (c5ad1_document_bank_valid(DOCUMENTS) == 0) { RETURN 0; }
    IF (c5ad1_passage_bank_valid(PASSAGES) == 0) { RETURN 0; }
    IF (c5ad1_citation_bank_valid(CITATIONS) == 0) { RETURN 0; }
    IF (c5ad1_cursor_bank_valid(CURSORS) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5ad1_structure_recall_document(memory, document_id) {
    IF (c5ad1_structure_memory_valid(memory) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(document_id, 128) == 0) { RETURN ""; }
    ⚡ DOCUMENTS: c5t2_memory_section(memory, "DOCUMENTS_BEGIN\n", "\nDOCUMENTS_END");
    ⚡ DOCUMENT: c5l2_bank_find_at(DOCUMENTS, 1, "DOCUMENT_ID", document_id);
    IF (c5ad1_document_valid(DOCUMENT) == 0) { RETURN ""; }
    RETURN DOCUMENT;
}

DEF c5ad1_structure_recall_passage(memory, passage_id) {
    IF (c5ad1_structure_memory_valid(memory) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(passage_id, 128) == 0) { RETURN ""; }
    ⚡ PASSAGES: c5t2_memory_section(memory, "PASSAGES_BEGIN\n", "\nPASSAGES_END");
    ⚡ PASSAGE: c5l2_bank_find_at(PASSAGES, 1, "PASSAGE_ID", passage_id);
    IF (c5ad1_passage_valid(PASSAGE) == 0) { RETURN ""; }
    RETURN PASSAGE;
}
