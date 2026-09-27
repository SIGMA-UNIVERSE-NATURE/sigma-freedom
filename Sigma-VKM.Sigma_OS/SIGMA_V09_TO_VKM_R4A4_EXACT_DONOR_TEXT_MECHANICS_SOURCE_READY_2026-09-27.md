# SIGMA V09 -> VKM R4A4 Exact Donor Text Mechanics — Source Ready

Date: 2026-09-27
Branch: SIGMA_LIFE
Mode: NATIVE_TEXT_MECHANICS_EQUIVALENCE
Rule: CLAIM <= EVIDENCE

## Scope

R4A4 ports the exact frozen donor R13-R6 word-tokenization and sentence-splitting behavior into Sigma/VKM mechanics and tests it over:
- all 1152 donor pretraining text files;
- 12 adversarial ASCII probes.

Total cases:
1164

Frozen donor function identities:
DONOR_WORDS_FUNCTION_SHA256=
54745e0eef2fd5d0b8685fdc6dd808b8b27a8f85d390f5bb23448c3310d3f3aa

DONOR_SENTENCES_FUNCTION_SHA256=
4d97c58345ab752d90db8745a3dcc223af8b5c4e0aea372556f8224644fcf3f2

Reference TSV SHA256:
b273326b845f27ffa71e02e75f24045ebad93bf64bc970a33c9292b335143ac6

Donor bundle SHA256:
f5e72217d6c26b55d3fad7185e9e007814271b577e64f9ca2d658b7a604426fc

## Donor scope audit

DONOR_PRETRAINING_TEXT_COUNT=1152
DONOR_PRETRAINING_NON_ASCII_CODEPOINT_COUNT=0
DONOR_PRETRAINING_WHITESPACE_CODEPOINTS=10,32
DONOR_PRETRAINING_PIPE_CHARACTER_PRESENT=NO

Thus the byte-oriented ASCII implementation is exact for the declared donor pretraining corpus. This does not claim general Unicode regex equivalence.

## Native evidence used

R4A3 FIX1 proved:
- str_len
- str_slice
- str_byte
- direct string SHA-256 through crypto_digest
- numeric mechanics required later

R4A4 uses only native VKM text/list mechanics and direct native SHA-256 to compare serialized token/sentence outputs.

## Safety ceiling

CANONICAL_MUTATION_ALLOWED=NO
OWNER_REBIND_ALLOWED=NO
OWNERSHIP_PROMOTION_ALLOWED=NO
DNA15_ALLOWED=NO

R4A4 does not prove:
- full feature-vector equivalence;
- frozen encoder equivalence;
- semantic behavior revalidation;
- native ownership.

## Release

BUNDLE=
SIGMA_V09_TO_VKM_R4A4_EXACT_DONOR_TEXT_MECHANICS_BUNDLE.zip

BUNDLE_SHA256=
7e87054e154809a38174d85be8babba472cac769512168bc510991822f27d356

R4A4_RELEASE_VERIFY=PASS
RUNTIME_STATUS=NOT_YET_RUN

NEXT=RUN_R4A4
