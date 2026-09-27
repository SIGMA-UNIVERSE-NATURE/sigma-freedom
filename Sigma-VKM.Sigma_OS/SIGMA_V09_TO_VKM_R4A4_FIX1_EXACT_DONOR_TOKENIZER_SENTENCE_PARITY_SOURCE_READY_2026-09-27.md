# SIGMA V09 -> VKM R4A4 FIX1 Exact Donor Tokenizer/Sentence Parity — Source Ready

Date: 2026-09-27
Branch: SIGMA_LIFE
Mode: NATIVE_MECHANICAL_PARITY_TEST
Rule: CLAIM <= EVIDENCE

## Why FIX1

The first packaged R4A4 controller used BREAK in loop bodies without prior compiler-language proof for BREAK.

That package was not run and is superseded before runtime.

FIX1 removes every BREAK token and uses only flag-driven WHILE loops, matching the already observed SIGMA control-flow surface.

## Locked identities

TARGET_OWNER_FINGERPRINT=
c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222

EXPECTED_VKM_SOURCE_SHA256=
af918fe8794791d70dcf6fb1b62e1b2fdd075f4ec237a7f3b72b9054e39876c7

PINNED_SIGMAC_VKM_SHA256=
60a5c9028f79d4eca5d0e4859e0c681c276402ac93bbd56e750c2c05a83e2a98

PINNED_SIGMA_VKM_VM_SHA256=
c70bbfc53f70cafd044b61a4ad9d64f1e4ef8e6c13af8371ea8d0773df871d95

DONOR_BUNDLE_SHA256=
f5e72217d6c26b55d3fad7185e9e007814271b577e64f9ca2d658b7a604426fc

DONOR_WORDS_FUNCTION_SHA256=
54745e0eef2fd5d0b8685fdc6dd808b8b27a8f85d390f5bb23448c3310d3f3aa

DONOR_SENTENCES_FUNCTION_SHA256=
4d97c58345ab752d90db8745a3dcc223af8b5c4e0aea372556f8224644fcf3f2

## Exact donor behavior under test

words:
[A-Za-z]+(?:'[A-Za-z]+)?|\d+(?:\.\d+)?
then lowercase

sentences:
split on (?<=[.!?])\s+ or one-or-more newlines;
strip pieces; discard empty pieces.

## Corpus-domain guard

The runtime first audits all 1152 donor pretraining text files and requires:
- text count = 1152;
- non-ASCII character count = 0;
- whitespace codepoints exactly {10,32}.

Therefore the byte-level native implementation is tested as exact for the admitted donor corpus domain, not claimed as a general Unicode regex implementation.

## Native parity fixtures

Synthetic:
- apostrophe
- decimal
- repeated punctuation
- hyphen
- punctuation-driven sentence boundaries
- newline boundaries

Exact donor:
- w001 VIEW_A_BASE
- w003 VIEW_A_BASE
- w003 VIEW_B_BASE

The complete token/sentence sequences are serialized and checked by SHA-256.

## Safety ceiling

CANONICAL_MUTATION_ALLOWED=NO
OWNER_REBIND_ALLOWED=NO
OWNERSHIP_PROMOTION_ALLOWED=NO
DNA15_ALLOWED=NO
SEMANTIC_BEHAVIOR_CLAIM_ALLOWED=NO

## Release

BUNDLE=
SIGMA_V09_TO_VKM_R4A4_FIX1_EXACT_DONOR_TOKENIZER_SENTENCE_PARITY_BUNDLE.zip

BUNDLE_SHA256=
cd4f1bf57fa35f0b02b016d5403cb65bacf1ae9328928fd4320b37ad18ee5bc2

R4A4_FIX1_RELEASE_VERIFY=PASS
NO_BREAK_TOKEN_STATIC=PASS

Runtime status:
NOT_YET_RUN

NEXT=RUN_R4A4_FIX1
