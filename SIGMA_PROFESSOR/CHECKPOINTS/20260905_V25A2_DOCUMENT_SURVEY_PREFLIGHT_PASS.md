# SIGMA V2.5A.2 DOCUMENT SURVEY PREFLIGHT — PASS

Date: 2026-09-05 (Asia/Ho_Chi_Minh)

## Admission result

V25A_2_DOCUMENT_SURVEY_PREFLIGHT=PASS

Locked compiler:

SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71

Locked VM:

VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

Native source:

SIGMA_PROFESSOR/artifacts/SIGMA_DOCUMENT_SURVEY_V2_5A_2.sigma

SOURCE_SHA256=153431aa3f78e282ddf0b2ddd73be993440abd9ce4118d4e717aa5ce83f14eb8

Compiled bytecode on device:

BYTECODE_SHA256=d1c68fbfb929326c2051754db75570d4711746b7ebe75d68f494131c9c28fb9b

## Runtime evidence

QA corpus contained exactly three `.document` files:

1. `0a7410aa3d627753302469a32fc70485059468de8ed08ede9a74dca82ad03bb4.document`
2. `c40f0bb8c9ca36d2f5b9a62a8c5a488a12b32ac3f7bac4e03b7037f9ff236930.document`
3. `d891e5ff25d3c9d390d6ab383e6bc0d90bc740b0397e47f6f88bc5fcc6a626de.document`

Run 1:

- VM_RC=0
- SIGMA selected `0a7410...`
- LINE_TOTAL=10
- SURVEY_LINE_LIMIT=10
- SAMPLE_TOKEN_COUNT=520
- RELATION_OCCURRENCES=510
- UNIQUE_RELATIONS=429
- RECURRING_RELATIONS=45
- BEST_LOCAL_RELATION=`in => the`
- BEST_LOCAL_SUPPORT=6

Run 2:

- VM_RC=0
- SIGMA selected `c40f0b...`
- LINE_TOTAL=10
- SURVEY_LINE_LIMIT=10
- SAMPLE_TOKEN_COUNT=427
- RELATION_OCCURRENCES=417
- UNIQUE_RELATIONS=383
- RECURRING_RELATIONS=19
- BEST_LOCAL_RELATION=`The => film`
- BEST_LOCAL_SUPPORT=5

Run 3:

- VM_RC=0
- SIGMA selected `d891e5...`
- LINE_TOTAL=9
- SURVEY_LINE_LIMIT=9
- SAMPLE_TOKEN_COUNT=774
- RELATION_OCCURRENCES=765
- UNIQUE_RELATIONS=668
- RECURRING_RELATIONS=52
- BEST_LOCAL_RELATION=`the => Moon`
- BEST_LOCAL_SUPPORT=12

Run 4:

- VM_RC=0
- SURVEY_COMPLETE=YES
- RAW_FILE_COUNT=3

Final runner evidence:

- V25A_SURVEYED_COUNT=3
- V25A_RECORD_COUNT=3
- V25A_COMPLETE_SENTINEL=1
- V25A_WRITES_PRODUCTION_NAMESPACE=NO
- HOST_LEARNING=NO
- SEMANTIC_UNDERSTANDING=NOT_PROVEN

## What is proven

Within the tested QA scope, native SIGMA can:

- enumerate a corpus through mechanical `listdir`;
- deterministically sort the corpus through `list_sort`;
- read persistent surveyed-document state;
- select the first unsurveyed `.document` itself;
- perform a bounded structural survey;
- build native map/list state for relation counts/order;
- compute local recurrence statistics;
- select the strongest local relation natively;
- persist a survey record and surveyed-document marker;
- continue on the next invocation from persisted state;
- recognize completion after all eligible QA documents have been surveyed.

This proves native structural document-survey behavior in the tested scope. It does NOT prove semantic document understanding, semantic topic classification, or semantic curriculum priority.

## Host boundary

HOST_LEARNING=NO
HOST_DOCUMENT_SELECTION=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_SEMANTIC_SUBSTITUTION=NO

The host/runner only prepared an isolated QA corpus, compiled/invoked the locked runtime, and inspected exact outputs/state.

## Observability note

`SURVEYED_ENTRY_COUNT=4` printed by the fourth VM invocation is an implementation-count artifact from splitting a newline-terminated surveyed-document file: the trailing newline produces an empty fourth split element. The authoritative persisted document count is 3 and the runner independently confirmed `V25A_SURVEYED_COUNT=3`.

This does not invalidate the PASS, but future versions should avoid presenting the raw split length as a document count.

## Next action

NEXT_ACTION=BUILD_V25_FULL_CORPUS_SURVEY_RUNNER

Requirements for the next stage:

- keep V2.4 production learner running independently;
- do not mutate V2.4 learning namespace during survey preflight/development;
- move from the 3-document QA corpus to the real existing raw corpus;
- keep each survey bounded;
- preserve crash/restart resumability;
- do not claim semantic grouping or priority yet;
- after full-corpus survey stabilization, proceed to bounded segment/cursor + crash-resume.
