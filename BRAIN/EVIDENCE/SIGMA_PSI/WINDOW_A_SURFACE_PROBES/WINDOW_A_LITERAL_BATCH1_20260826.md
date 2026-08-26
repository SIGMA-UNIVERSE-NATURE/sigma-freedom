# WINDOW A — BLACK-BOX DIFFERENTIAL GRAMMAR EVIDENCE — LITERAL BATCH 1

ROLE=WINDOW_A_ONLY
DATE=2026-08-26
PRIMARY_ROOT=~/SIGMA/sigma_genesis1
PROBE_DIR=.sigma_tmp/WINDOW_A_SURFACE_PROBES_LIT1_20260826_135415
COMPILER_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_EXECUTION_USED=NO
NO_EXPECTED_SEMANTIC_ANSWER=YES
PRIVATE_SOURCE_INSPECTED=NO
PRIVATE_SOURCE_PUBLISHED=NO
DO_NOT_RERUN_CAPABILITIES_PRESERVED=21

Evidence target for this batch is compiler acceptance only:
SOURCE FORM → CURRENT COMPILER RC → BYTECODE CREATED OR NOT.

No runtime type semantics, null semantics, cognition, understanding, or universal grammar claim is made.

## TEST WA-LIT-01

TEST_ID=WA-LIT-01
QUESTION=In the exact neutral binding context, does candidate decimal float literal `1.5` compile compared with evidenced integer literal `1`?
VARIANT_A=Header + `⟡(Σ.MAIN) { ⚡ a: 1; }`
VARIANT_B=Same exact form with `⚡ a: 1.5;`
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=9e663743c008d54674f4c5abd581ed3547095769e6e5c0b8297c5ccd626b48c8
SOURCE_SHA256_B=b534dca02db25fe8f6e0462cdcaf638799b3225441ad2c6ef6c370e03f71b7ca
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=26984037391df0e06a01185177261a99fc4b7e6f6ab3998b3158a49ab7283875
BYTECODE_SIZE_A=53
COMPILER_STDOUT_SIZE_A=153
COMPILER_STDERR_SIZE_A=0
COMPILER_RC_B=0
BYTECODE_CREATED_B=YES
BYTECODE_SHA256_B=e481e5dabd0d2d5f55ae98d0b6610ddbf9ba4d7d1c12bb4d1cf653856dcbd290
BYTECODE_SIZE_B=53
COMPILER_STDOUT_SIZE_B=153
COMPILER_STDERR_SIZE_B=0
OBSERVATION=Both exact forms were accepted and emitted bytecode; the bytecode hashes differ.
PROVEN_SCOPE=Exact lexical/source acceptance of `1` and `1.5` in this neutral binding context under the identified current compiler.
NOT_PROVEN_BEYOND=No numeric runtime type, precision, coercion, range, exponent grammar, sign grammar, or arithmetic semantics are established.

## TEST WA-LIT-02

TEST_ID=WA-LIT-02
QUESTION=In the exact neutral binding context, do double-quoted and single-quoted one-character string forms both compile?
VARIANT_A=Header + `⟡(Σ.MAIN) { ⚡ a: "x"; }`
VARIANT_B=Same exact form with `⚡ a: 'x';`
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=e18e784c6baf2a361b58174ff11f97ed73df485adfca508708d8d528d497241c
SOURCE_SHA256_B=a57a7b8a08bb28db27c766b5575be8e1f160f55d6901c4ac908af210148f9a02
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=47422d47b738c1cdccfc05b5c00a76e30b076007727c728866f3b49e7f3fdf27
BYTECODE_SIZE_A=50
COMPILER_STDOUT_SIZE_A=153
COMPILER_STDERR_SIZE_A=0
COMPILER_RC_B=0
BYTECODE_CREATED_B=YES
BYTECODE_SHA256_B=47422d47b738c1cdccfc05b5c00a76e30b076007727c728866f3b49e7f3fdf27
BYTECODE_SIZE_B=50
COMPILER_STDOUT_SIZE_B=153
COMPILER_STDERR_SIZE_B=0
OBSERVATION=Both quote forms were accepted and emitted bytecode with identical bytecode hash and size.
PROVEN_SCOPE=Exact compiler acceptance of the tested `"x"` and `'x'` forms in this neutral binding context.
NOT_PROVEN_BEYOND=Identical bytecode is not interpreted here as proof of identical runtime semantics; no escape, multiline, interpolation, encoding, or general string grammar is established.

## TEST WA-LIT-03

TEST_ID=WA-LIT-03
QUESTION=In the exact neutral binding context, do uppercase `NULL` and lowercase `null` both compile?
VARIANT_A=Header + `⟡(Σ.MAIN) { ⚡ a: NULL; }`
VARIANT_B=Same exact form with `⚡ a: null;`
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=0caa59382cc763d2c44741b11ee5c18f44eea847eacb9965c0bcb408c4c0d5e5
SOURCE_SHA256_B=8b0f4ae5a1d4d7cdf990615627b34d13e986b5dc2b5a5023860d050b9cc8588d
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=2ef18fb15a74ea4207a46341ab47d3c0d308346af1bd72222c3d2d43b6c41261
BYTECODE_SIZE_A=45
COMPILER_STDOUT_SIZE_A=153
COMPILER_STDERR_SIZE_A=0
COMPILER_RC_B=0
BYTECODE_CREATED_B=YES
BYTECODE_SHA256_B=ba54d93c157fa95b03a9c3b851144df59f4bb854d5f7e974af1e60716616f978
BYTECODE_SIZE_B=52
COMPILER_STDOUT_SIZE_B=153
COMPILER_STDERR_SIZE_B=0
OBSERVATION=Both exact token spellings were accepted and emitted bytecode; their bytecode hashes and sizes differ.
PROVEN_SCOPE=Exact compiler acceptance of tested uppercase `NULL` and lowercase `null` spellings in this neutral binding context.
NOT_PROVEN_BEYOND=No claim that the two spellings have the same token class or runtime meaning; no null semantics or general case-insensitivity rule is inferred.

## BOOL BOUNDARY

BOOL_PROBE_RUN=NO
REASON=Window A evidence set did not localize an exact current BOOL source spelling suitable as an evidence-grounded control. Choosing a spelling from GPT expectation would violate the anti-imposition rule.
STATUS=NOT_PROVEN

## BATCH SUMMARY

DIFFERENTIAL_PROBES_RUN=3
COMPILER_VARIANTS_RUN=6
COMPILER_ACCEPT_CASES=6
COMPILER_REJECT_CASES=0
TIMEOUT_CASES=0
GPT_ANSWER_IMPOSITION_USED=NO
CAPABILITY_RESEARCH_RERUNS=0
