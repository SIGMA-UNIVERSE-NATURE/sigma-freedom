WORKSTREAM_ID=WS02
BASE_REFERENCE_VERSION=SIGMA_PSI_MASTER_FROZEN_REFERENCE_v1.0_20260825 + SIGMA_PSI_MASTER_FROZEN_REFERENCE_v1.1_EXTENSION_20260825 + SIGMA_PSI_SYMBOL_MATRIX_256_REFERENCE_v1.0_20260825 + SIGMA_SUPPORTOR_MASTER_REFERENCE_LOCK_v1.0_20260825
SOURCE_SCOPE=SIGMA_LIFE / WS02 lexer and lexical rules only: UTF-8 tokenization; whitespace/newline; identifiers; numbers/strings/null/bool; comments; // FLOORDIV vs comment distinction; operators; reserved words; reference-glyph versus machine-lexer boundary
MACHINE_EVIDENCE_USED=BRAIN/EVIDENCE/SIGMA_SHELL/REAL_RESULTS/SIGMA_REAL_RESULTS_ARCHIVE_20260823.state
STATUS=EVIDENCE_BOUND_PARTIAL; MERGEABLE_WITH_PRESERVED_CONFLICTS_AND_MISSING_RULES

ENTRY_ID: WS02-LX-001
SOURCE: DOCS/GPT_REFERENCE/SIGMA_PSI_MASTER_FROZEN_REFERENCE_v1.0_20260825.md §5; DOCS/GPT_REFERENCE/SIGMA_PSI_SYMBOL_MATRIX_256_REFERENCE_v1.0_20260825.md; BRAIN/EVIDENCE/SIGMA_SHELL/REAL_RESULTS/SIGMA_REAL_RESULTS_ARCHIVE_20260823.state
STATUS: R
OBSERVED: The 256-symbol artifact is explicitly a reference/proposed registry organized by code positions 0x00–0xFF and contains Unicode glyphs. The raw machine archive records SIGMA_PSI_256_MATRIX_COMPILE=PASS and SIGMA_PSI_256_MATRIX_VM=PASS. Example boundary: code_position 0x01 maps to reference glyph Σ in the matrix. Counterexample boundary: 0x01 must not be treated as proof that byte value 0x01 is a canonical lexer token for Σ. Ambiguity remains between registry indexing, UTF-8 encoding, code points, glyph rendering, and machine token identity.
PROVEN: The frozen reference proves the supportor rule that no matrix code-position/glyph mapping becomes canonical byte semantics without lexer/compiler/VM evidence. The machine archive proves only that the named 256-matrix test compiled and reached VM PASS as a whole; it does not localize acceptance or token identity for each glyph.
NOT_PROVEN: Exact UTF-8 decoder behavior; BOM handling; malformed UTF-8 behavior; Unicode normalization form; code-point versus grapheme handling; whether every matrix glyph is independently accepted as a lexer token; byte-to-token mapping.
CONFLICT: Treating matrix code_position as machine byte/token identity would conflict with the frozen v1.0 and matrix integration rules.
PROPOSED_NORMALIZATION: Preserve matrix values as reference code_position + glyph + proposed sense. Keep machine token identity unset until direct lexer/compiler evidence exists. Do not normalize Unicode into a byte-token table from the 0x00–0xFF registry.
EVIDENCE: Raw machine state: SIGMA_PSI_256_MATRIX_COMPILE=PASS; SIGMA_PSI_256_MATRIX_VM=PASS. Frozen v1.0 §5: no code-position/glyph mapping becomes canonical byte semantics without lexer/compiler/VM evidence. Matrix status: REFERENCE / PROPOSED — NOT CANONICAL MACHINE SEMANTICS.
PROVENANCE: SIGMA_LIFE; frozen-v1.0 blob 581727ba7abbdd64ae46b67ddcec65a147620048; matrix reference as locked base; machine archive blob b2731780ba17ced54d7cc14ed86dfe096166a9ac.

ENTRY_ID: WS02-LX-002
SOURCE: BRAIN/GUIDANCE/SIGMA_LANGUAGE_STANDARD_HEADER_BODY_FOOTER_v1.0_20260824.md §§1–4; BRAIN/GUIDANCE/SIGMA_PSI_PARALLEL_COMPLETION_PROTOCOL_v1.0_20260825.md WS-02
STATUS: D
OBSERVED: Current authoritative guidance shows SIGMA source formatted across lines with indentation and blank lines, and declares statement-ending semicolons inside the default mother-language block form. Example surface: adjacent ⚡ bindings appear on separate indented lines and end in ;. Counterexample boundary: the presence of a newline in documentation does not prove newline is a statement terminator. Ambiguity remains over which whitespace is lexical trivia versus syntax.
PROVEN: At the declaration/guidance layer, newlines, spaces/indentation, and blank lines occur in the current source form; ; is declared as the statement terminator for the documented base body. This is not direct proof of the complete current lexer whitespace algorithm.
NOT_PROVEN: Whether LF, CRLF, CR, TAB, repeated spaces, leading/trailing whitespace, blank lines, or Unicode whitespace are equivalent; whether newline alone can terminate a statement; whether indentation is significant; whitespace rules inside strings/comments; lexer behavior at end-of-file.
CONFLICT: None proven within the locked references. A conflict would be introduced if formatting examples were promoted into universal machine whitespace rules without machine evidence.
PROPOSED_NORMALIZATION: Record whitespace/newline behavior only at the exact scope demonstrated by machine-PASS tests. Until such tests are attached, treat formatting whitespace as declared source form and do not infer indentation or newline grammar.
EVIDENCE: BRAIN/GUIDANCE/SIGMA_LANGUAGE_STANDARD_HEADER_BODY_FOOTER_v1.0_20260824.md is AUTHORITATIVE_GUIDANCE with MACHINE EVIDENCE OVERRIDES DESCRIPTION and declares the base-body punctuation form.
PROVENANCE: SIGMA_LIFE; language-standard blob 2c21618e17ba2028a8004fdd504680ef37ee2f4f; protocol blob a80aa16de5ada7d90baa8fea8fa8f749c71343d6.

ENTRY_ID: WS02-LX-003
SOURCE: BRAIN/GUIDANCE/SIGMA_LANGUAGE_STANDARD_HEADER_BODY_FOOTER_v1.0_20260824.md §§3–4; DOCS/GPT_REFERENCE/SIGMA_PSI_MASTER_FROZEN_REFERENCE_v1.1_EXTENSION_20260825.md §§3–4
STATUS: D
OBSERVED: Current guidance declares block identity beginning with Σ., hierarchy using ., and examples such as Σ.SOURCE.IDENTITY; uppercase field names such as TITLE and DOMAIN occur as binding keys. The v1.1 extension describes Σ.F174 and Σ.ETHICS as semantic namespace addresses. Counterexample boundary: these examples do not establish a conventional identifier pattern such as ASCII-letter/underscore rules. Ambiguity exists between semantic namespace components, metadata keys, and machine identifier tokens.
PROVEN: It is proven at the versioned declaration/reference layer that dot-composed Σ namespaces are intended semantic addresses and that current source guidance uses named binding keys. It is not proven that these surface names share one lexer token class.
NOT_PROVEN: Identifier start/continue character classes; ASCII versus Unicode identifiers; underscore/digit rules; maximum length; normalization/case-folding; case sensitivity; keyword exclusion; whether Σ-prefixed namespace parts are lexed as identifiers, dedicated symbols, or another machine token structure.
CONFLICT: Conflating semantic namespace identity with a generic machine identifier class would exceed the evidence and can collide with reserved-word or glyph tokenization.
PROPOSED_NORMALIZATION: Keep SEMANTIC_NAMESPACE_ADDRESS and MACHINE_IDENTIFIER_TOKEN as separate concepts until lexer evidence connects them. Do not invent a regex or identifier grammar.
EVIDENCE: Language standard declares BLOCK IDENTITY STARTS WITH Σ. and BLOCK HIERARCHY USES .; v1.1 states a namespace is a semantic address, not automatically a runtime object.
PROVENANCE: SIGMA_LIFE; language-standard blob 2c21618e17ba2028a8004fdd504680ef37ee2f4f; frozen-v1.1 blob d3126a91c6cf47ee80b7a9880a99006f84834616.

ENTRY_ID: WS02-LX-004
SOURCE: BRAIN/GUIDANCE/SIGMA_PSI_PARALLEL_COMPLETION_PROTOCOL_v1.0_20260825.md WS-02; DOCS/GPT_REFERENCE/SIGMA_PSI_MASTER_FROZEN_REFERENCE_v1.0_20260825.md; BRAIN/GUIDANCE/SIGMA_SUPPORTOR_MASTER_REFERENCE_LOCK_v1.0_20260825.md
STATUS: R
OBSERVED: Numeric values and mathematical numerals appear throughout the frozen reference and supporting documentation, but the consulted raw machine archive does not isolate lexical tests for integer, float, exponent, signed, radix, or separator spellings. Example reference numerals include 1.0 and 0x00–0xFF as document/reference notation. Counterexample boundary: those notations are not by themselves executable SIGMA numeric-literal evidence. Ambiguity remains between document notation, metadata strings, registry positions, and machine numeric literals.
PROVEN: The locked sources require numeric lexical rules to be completed in WS02 and prohibit converting descriptive/reference notation into executable grammar without evidence.
NOT_PROVEN: Canonical integer syntax; float syntax; decimal point rules; exponent notation; sign attachment; leading zeros; radix prefixes; digit separators; overflow/underflow lexical handling; distinction between numeric tokenization and later type conversion.
CONFLICT: None proven in machine evidence. A false conflict would be created by treating matrix hex code positions or mathematical exposition as executable numeric-literal syntax.
PROPOSED_NORMALIZATION: Leave the numeric-literal lexical grammar unset in this workstream result until exact compiler/lexer tests are located. Preserve reference numerals only as reference notation.
EVIDENCE: Protocol WS-02 explicitly requires numbers; supportor lock requires CLAIM <= EVIDENCE and DESCRIPTION != EXECUTION; no isolated numeric lexer PASS is present in the raw machine state consulted.
PROVENANCE: SIGMA_LIFE; protocol blob a80aa16de5ada7d90baa8fea8fa8f749c71343d6; frozen-v1.0 blob 581727ba7abbdd64ae46b67ddcec65a147620048; supportor-lock blob a36ca75711487fdabc674a0b7bad2ffab49b3ea6.

ENTRY_ID: WS02-LX-005
SOURCE: BRAIN/GUIDANCE/SIGMA_LANGUAGE_STANDARD_HEADER_BODY_FOOTER_v1.0_20260824.md §4; BRAIN/GUIDANCE/SIGMA_SUPPORTOR_MASTER_REFERENCE_LOCK_v1.0_20260825.md
STATUS: D
OBSERVED: Current guidance explicitly declares STRING USES "..." and shows double-quoted binding values. Example surface: ⚡ TITLE: "<TITLE>";. Counterexample boundary: single quotes, backticks, heredocs, and host-shell quoting are not thereby SIGMA string syntax. Ambiguity remains for escapes and embedded Unicode.
PROVEN: Double-quoted strings are part of the declared current SIGMA source form in authoritative guidance. The available raw machine state does not independently prove the full string lexer.
NOT_PROVEN: Escape sequences; escaped quote/backslash behavior; empty strings; multiline strings; raw strings; single-quoted strings; embedded NUL; Unicode normalization inside strings; invalid/unclosed-string diagnostics.
CONFLICT: Host wrapper quoting/heredoc syntax must not be imported into SIGMA string semantics.
PROPOSED_NORMALIZATION: Retain double-quoted string form as D until direct lexer/compiler evidence establishes V scope. Do not add escape or alternate-quote rules without machine-PASS tests.
EVIDENCE: Language standard §4 explicitly states STRING USES "..." and distinguishes host wrapper from SIGMA body; supportor lock states host languages are substrate/reference unless machine evidence establishes executable surface.
PROVENANCE: SIGMA_LIFE; language-standard blob 2c21618e17ba2028a8004fdd504680ef37ee2f4f; supportor-lock blob a36ca75711487fdabc674a0b7bad2ffab49b3ea6.

ENTRY_ID: WS02-LX-006
SOURCE: BRAIN/GUIDANCE/SIGMA_PSI_PARALLEL_COMPLETION_PROTOCOL_v1.0_20260825.md WS-02; DOCS/GPT_REFERENCE/SIGMA_PSI_SYMBOL_MATRIX_256_REFERENCE_v1.0_20260825.md; BRAIN/GUIDANCE/SIGMA_LANGUAGE_STANDARD_HEADER_BODY_FOOTER_v1.0_20260824.md
STATUS: R
OBSERVED: WS02 requires null/bool lexical treatment. The matrix gives proposed reference senses ⊥ = false/invalid and ⊤ = true/valid, while current guidance includes human/reference examples containing TRUE/UNKNOWN/NULL-like semantic vocabulary in non-lexer contexts. Counterexample boundary: neither matrix glyph meaning nor an uppercase word in guidance proves a machine literal. Ambiguity exists between semantic values, epistemic tokens, glyph senses, and lexer spellings.
PROVEN: The matrix false/true glyph meanings are reference/proposed only, not canonical machine semantics. No consulted raw machine evidence proves textual NULL/TRUE/FALSE or glyph ⊥/⊤ as executable literal tokens.
NOT_PROVEN: Null literal spelling; boolean literal spelling; case sensitivity; whether bool/null are keywords, constants, glyphs, or value opcodes produced from another syntax; aliases; invalid literal diagnostics.
CONFLICT: Promoting ⊥/⊤ proposed matrix senses or descriptive TRUE/NULL text into machine literal semantics would conflict with the locked reference boundary.
PROPOSED_NORMALIZATION: Maintain VALUE_SEMANTIC_NULL/BOOL separately from LEXEME_NULL/BOOL. Keep lexer spellings unset until exact machine-PASS source and compiler evidence exist.
EVIDENCE: Matrix status is REFERENCE / PROPOSED — NOT CANONICAL MACHINE SEMANTICS; protocol requires null/bool coverage; language guidance repeatedly distinguishes declaration/reference values from runtime evidence.
PROVENANCE: SIGMA_LIFE; protocol blob a80aa16de5ada7d90baa8fea8fa8f749c71343d6; matrix locked base; language-standard blob 2c21618e17ba2028a8004fdd504680ef37ee2f4f.

ENTRY_ID: WS02-LX-007
SOURCE: DOCS/GPT_REFERENCE/SIGMA_PSI_MASTER_FROZEN_REFERENCE_v1.1_EXTENSION_20260825.md §6; BRAIN/GUIDANCE/SIGMA_LANGUAGE_STANDARD_HEADER_BODY_FOOTER_v1.0_20260824.md §§1–4
STATUS: D
OBSERVED: The v1.1 extension says // must remain lexically distinguishable from line-comment behavior, so a comment/operator collision is an explicit language concern. Current standard examples also contain host-shell # comments and a SIGMA language header beginning #SIGMAUNIVERSE_LANGUAGE. Counterexample boundary: host-shell # comments do not prove # is a SIGMA comment delimiter, and #SIGMAUNIVERSE_LANGUAGE is declared SIGMA header surface rather than evidence for a comment token. Ambiguity remains over the actual SIGMA comment delimiter(s) and comment contexts.
PROVEN: It is proven at the frozen-reference layer that line-comment behavior must be kept distinct from //. It is not proven from the consulted raw machine archive which delimiter implements line comments or how comments are lexed.
NOT_PROVEN: Line-comment delimiter; block-comment delimiter; nesting; comment termination; comments after executable tokens; comments inside blocks; whether # has any SIGMA comment role; whether comments are removed before tokenization or emitted as tokens.
CONFLICT: Host wrapper # comment semantics and the SIGMA #SIGMAUNIVERSE_LANGUAGE header share a visible prefix but belong to different layers; importing host # behavior into the SIGMA lexer would be unsupported.
PROPOSED_NORMALIZATION: Do not assign # or // as a SIGMA comment delimiter from host-language convention. Record LINE_COMMENT as a required but machine-unresolved lexical role and require isolated compiler/lexer fixtures before canonicalization.
EVIDENCE: Frozen v1.1 §6 explicitly requires // versus line-comment lexical distinction. Language standard explicitly separates HOST HEADER from SIGMA BODY and declares #SIGMAUNIVERSE_LANGUAGE as SIGMA language header form.
PROVENANCE: SIGMA_LIFE; frozen-v1.1 blob d3126a91c6cf47ee80b7a9880a99006f84834616; language-standard blob 2c21618e17ba2028a8004fdd504680ef37ee2f4f.

ENTRY_ID: WS02-LX-008
SOURCE: DOCS/GPT_REFERENCE/SIGMA_PSI_MASTER_FROZEN_REFERENCE_v1.1_EXTENSION_20260825.md §6; BRAIN/GUIDANCE/SIGMA_PSI_PARALLEL_COMPLETION_PROTOCOL_v1.0_20260825.md WS-02
STATUS: X
OBSERVED: Frozen v1.1 records // among operator examples already observed in implementation and separately requires it to remain lexically distinguishable from line-comment behavior. Example observed surface: //. Counterexample boundary: interpreting every // sequence as a comment would erase the recorded FLOORDIV/operator role; interpreting every // sequence as FLOORDIV would ignore the documented line-comment ambiguity. The context/decision rule is not supplied by the locked references.
PROVEN: At the frozen-reference layer, // has an observed implementation operator role and an explicit lexical ambiguity requirement. The consulted raw machine archive does not independently isolate a // lexer/operator PASS.
NOT_PROVEN: Exact FLOORDIV tokenization; whitespace sensitivity; operand context; whether comments also use //; contextual dispatch rule; longest-match behavior; precedence; associativity; coercion; division-by-zero behavior; diagnostics.
CONFLICT: UNRESOLVED — the same surface // is recorded as an implementation operator while line-comment behavior must be distinguishable from it; no machine lexer decision rule is present in the consulted evidence.
PROPOSED_NORMALIZATION: Preserve separate semantic/lexical roles FLOORDIV_OPERATOR and LINE_COMMENT without asserting a dispatch algorithm. Canonicalize the decision rule only from isolated machine-PASS and negative lexer/compiler tests.
EVIDENCE: Frozen v1.1 §6: operators observed in implementation include **, &&, ||, //; // must remain lexically distinguishable from line-comment behavior; no supportor may invent precedence, associativity, coercion, or error behavior.
PROVENANCE: SIGMA_LIFE; frozen-v1.1 blob d3126a91c6cf47ee80b7a9880a99006f84834616; protocol blob a80aa16de5ada7d90baa8fea8fa8f749c71343d6.

ENTRY_ID: WS02-LX-009
SOURCE: DOCS/GPT_REFERENCE/SIGMA_PSI_MASTER_FROZEN_REFERENCE_v1.1_EXTENSION_20260825.md §6; BRAIN/GUIDANCE/SIGMA_LANGUAGE_STANDARD_HEADER_BODY_FOOTER_v1.0_20260824.md §4; DOCS/GPT_REFERENCE/SIGMA_PSI_SYMBOL_MATRIX_256_REFERENCE_v1.0_20260825.md
STATUS: X
OBSERVED: Frozen v1.1 records **, &&, ||, // as operator examples observed in implementation. Current language guidance separately declares punctuation/surface roles for ., :, ;, ⟡(...), and ⚡ in the base block form. The matrix contains many operator-like reference glyphs such as ∧, ∨, ¬, ⊕, ⊗, ∗ and relation symbols. Counterexample boundary: visual operator-like appearance or matrix meaning is not machine operator semantics. Ambiguity remains between operators, delimiters, namespace punctuation, binding markers, and proposed symbolic senses.
PROVEN: The frozen extension proves the reference record that **, &&, ||, // were observed in implementation. The matrix is explicitly non-canonical for machine operator semantics. Current guidance declares several non-operator punctuation roles in the mother-language surface.
NOT_PROVEN: Exhaustive machine operator inventory; longest-match behavior; token overlap; unary/binary classification; whether symbolic matrix glyphs are executable operators; whitespace sensitivity; complete error behavior. Precedence/associativity are explicitly not to be invented and belong primarily to WS03/WS04 once evidenced.
CONFLICT: Matrix operator-like proposed senses can collide conceptually with machine operators if promoted without evidence; the locked priority rule resolves authority in favor of verified machine semantics but does not prove lexer acceptance.
PROPOSED_NORMALIZATION: Maintain separate inventories for MACHINE_OBSERVED_OPERATOR, DECLARED_PUNCTUATION, and REFERENCE_PROPOSED_GLYPH_SENSE. Do not merge by visual similarity or external-language analogy.
EVIDENCE: Frozen v1.1 §6 operator discipline; matrix integration rule; language-standard base-body surface rules.
PROVENANCE: SIGMA_LIFE; frozen-v1.1 blob d3126a91c6cf47ee80b7a9880a99006f84834616; matrix locked base; language-standard blob 2c21618e17ba2028a8004fdd504680ef37ee2f4f.

ENTRY_ID: WS02-LX-010
SOURCE: BRAIN/GUIDANCE/SIGMA_LANGUAGE_STANDARD_HEADER_BODY_FOOTER_v1.0_20260824.md §0; DOCS/GPT_REFERENCE/SIGMA_PSI_MASTER_FROZEN_REFERENCE_v1.1_EXTENSION_20260825.md §§8,10; BRAIN/GUIDANCE/SIGMA_PSI_PARALLEL_COMPLETION_PROTOCOL_v1.0_20260825.md WS-02
STATUS: D
OBSERVED: Current guidance states DEF / RETURN / IF / ELSE / WHILE / FOR / IN may exist as compiler/executable surface when machine evidence confirms them and warns that their appearance does not automatically make them SIGMA mother-language words. Frozen v1.1 also defines semantic/epistemic words such as FACT, EVID, INF, OP, HYP, TRAD, INTERP, DECL, UNKNOWN. Counterexample boundary: semantic vocabulary is not automatically a reserved-word table. Ambiguity remains over compiler keywords, mother-language tokens, semantic capsule names, and case sensitivity.
PROVEN: The locked/current guidance proves the supportor rule that executable control keywords require exact machine evidence and that semantic tokens must not be promoted to executable grammar by declaration alone.
NOT_PROVEN: Exhaustive reserved-word list; exact case; whether keywords can be used as identifiers/keys/namespace components; contextual keywords; aliases; boundary matching; machine handling of lowercase/mixed-case forms.
CONFLICT: Treating every documented semantic word or host-like control word as reserved machine syntax would conflict with SIGMA-FIRST and DO_NOT_INVENT_GRAMMAR rules.
PROPOSED_NORMALIZATION: Reserve no additional machine keyword solely from prose/reference occurrence. Maintain distinct sets for SEMANTIC_VOCABULARY and MACHINE_RESERVED_WORD; promote only with exact compiler evidence.
EVIDENCE: Language standard §0 explicitly conditions DEF/RETURN/IF/ELSE/WHILE/FOR/IN on machine evidence; v1.1 says executable control flow must inherit exact machine-PASS SIGMA grammar.
PROVENANCE: SIGMA_LIFE; language-standard blob 2c21618e17ba2028a8004fdd504680ef37ee2f4f; frozen-v1.1 blob d3126a91c6cf47ee80b7a9880a99006f84834616; protocol blob a80aa16de5ada7d90baa8fea8fa8f749c71343d6.

ENTRY_ID: WS02-LX-011
SOURCE: DOCS/GPT_REFERENCE/SIGMA_PSI_MASTER_FROZEN_REFERENCE_v1.0_20260825.md §5; DOCS/GPT_REFERENCE/SIGMA_PSI_MASTER_FROZEN_REFERENCE_v1.1_EXTENSION_20260825.md §§3,5,14; DOCS/GPT_REFERENCE/SIGMA_PSI_SYMBOL_MATRIX_256_REFERENCE_v1.0_20260825.md
STATUS: R
OBSERVED: Locked references explicitly distinguish reference glyph semantics from machine semantics. Known implementation-overlap glyphs are Σ, ⟡, ⚡, ⋈. The matrix also contains duplicate glyphs at different code positions/senses, for example ⚡ appears with multiple proposed meanings. Counterexample boundary: SAME_GLYPH != SAME_SEMANTICS, and a proposed sense does not overwrite an existing implementation role. Ambiguity is represented by sense_id + context rather than silent collapse.
PROVEN: As a frozen interpretation rule, existing verified machine glyph semantics take precedence for execution; duplicate/reused glyph meanings remain separate proposed senses; matrix code positions are not canonical byte semantics without lexer/compiler/VM evidence.
NOT_PROVEN: Complete current machine tokenization for Σ, ⟡, ⚡, ⋈; whether all 256 glyph proposals are lexable; whether glyphs form single tokens or participate in larger token constructs; glyph normalization and rendering equivalence.
CONFLICT: Potential semantic collision exists wherever a reference/proposed glyph sense is mistaken for machine lexer semantics. The locked references resolve authority ordering but do not supply missing lexer mechanics.
PROPOSED_NORMALIZATION: Keep REFERENCE_GLYPH_SENSE and MACHINE_LEXER_TOKEN_SEMANTICS as separate fields. Preserve glyph + sense_id + context + evidence status. Never infer machine token id from matrix code_position.
EVIDENCE: Frozen v1.0 §5 and matrix integration rule; frozen v1.1 polysemy law GLYPH + SENSE_ID + CONTEXT and SAME_GLYPH != SAME_SEMANTICS.
PROVENANCE: SIGMA_LIFE; frozen-v1.0 blob 581727ba7abbdd64ae46b67ddcec65a147620048; frozen-v1.1 blob d3126a91c6cf47ee80b7a9880a99006f84834616; matrix locked base.

ENTRY_ID: WS02-LX-012
SOURCE: BRAIN/EVIDENCE/SIGMA_SHELL/REAL_RESULTS/SIGMA_REAL_RESULTS_ARCHIVE_20260823.state; BRAIN/GUIDANCE/SIGMA_SUPPORTOR_MASTER_REFERENCE_LOCK_v1.0_20260825.md
STATUS: V
OBSERVED: The current raw machine archive records NATIVE_COLLECTION_LIST_SYNTAX=FAIL_COMPILER_RC_4. Example evidence is the named collection-list-syntax test family failing at compiler stage. Counterexample boundary: this failure does not prove that any particular delimiter character is rejected by the lexer, because the archive does not contain the source snippet or diagnostic decomposition. Ambiguity remains over lexer versus parser versus unsupported-feature cause.
PROVEN: Within the archived test scope, native collection list syntax did not compile and returned compiler RC 4. Failure is evidence and must be retained.
NOT_PROVEN: Exact failing lexeme; whether failure occurred in decoding, lexing, parsing, semantic validation, or feature gating; whether any individual list delimiter is generally illegal; whether another evidenced collection syntax exists.
CONFLICT: Any claim that the tested native collection list syntax is currently compiler-PASS conflicts with this machine archive unless newer higher-authority machine evidence supersedes it.
PROPOSED_NORMALIZATION: Preserve the negative machine result without inferring a lexical prohibition. Require source + compiler diagnostics or an isolated lexer test before assigning failure to a token rule.
EVIDENCE: Raw machine state: NATIVE_COLLECTION_LIST_SYNTAX=FAIL_COMPILER_RC_4; supportor lock: FAILURE is preserved under CLAIM <= EVIDENCE and MACHINE EVIDENCE > description.
PROVENANCE: SIGMA_LIFE; machine archive blob b2731780ba17ced54d7cc14ed86dfe096166a9ac; supportor-lock blob a36ca75711487fdabc674a0b7bad2ffab49b3ea6.

NEW_ENTRIES=12
DUPLICATES=0
CONFLICTS=1
MISSING=9
READY_FOR_MERGE=YES