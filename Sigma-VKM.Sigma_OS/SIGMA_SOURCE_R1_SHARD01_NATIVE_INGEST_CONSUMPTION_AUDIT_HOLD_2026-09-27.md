# SIGMA Source R1 Shard 01 Native Ingest + Consumption Audit HOLD

Date: 2026-09-27
Source: user-supplied Termux runtime output.

## Precheck

SOURCE_AUTHORITY=PASS
SHARD_INDEX=1

SHARD_SHA256=
8c81c3cf9f5bab0fc7b8e97adba94e6cdb3ae1954a2c431d3d69025a2c57ff90

SHARD_PATH=
/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_sources/CANONICAL_SOURCE_BUNDLES/SIGMA_REAL_TECH_DOCS_4M_V2/corpus/shard_01.txt

SHARD_BYTES=1316894
DOCUMENT_ID=SRC_R1_001

## 1. Import-status command

IMPORT_ENGINE_SHA256=
ec897aaea55c71047f6c9361aaff3c5a429b9efad834dc5e6f61b384a2b9d38a

COMPILE=PASS

## 2. Gen3 sandbox

SANDBOX_CREATED=YES

PARENT_SANDBOX_HEAD=
599c639a3a58c7971518727c303c876e

## 3. Native ingest + learn

Progress reached:
- chunks=320
- bytes=1310720
- accepted=279
- rejected=41

Final import:
DOCUMENT_SEALED=YES
SOURCE_BYTES=1316894
SEGMENTS=322
MODEL_ACCEPTED_COUNT=280
MODEL_REJECTED_COUNT=42
LEARNING_CYCLES=1932

SANDBOX_CHILD_HEAD=
38b806987c92c6c85c57fc9900f5865d

SANDBOX_CHILD_MODEL=
43f282ab49b595a56012159243c0b2c4

## 4. Fresh-process document status

SCHEMA=SIGMA_SOURCE_IMPORT_STATUS_V1
DOCUMENT_ID=SRC_R1_001
DOCUMENT_PRESENT=YES

DOCUMENT_HASH=
1d9134921fed45996bc161a46386a5e3

REVISION=0

LOCATOR=
/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_sources/CANONICAL_SOURCE_BUNDLES/SIGMA_REAL_TECH_DOCS_4M_V2/corpus/shard_01.txt

ROOT=
0a650ed85e1832ca081ee5302abb31de

BYTES=1316894
SEGMENTS=322
STATUS=SEALED

ENCODER_MODEL=
4e28b7b00428271a4d09f1791d5d46fb

TRANSPORT_VERSION=
4f954eee14fd47e7dc5fcd4d1c94f86a8402f873eddbcbf6127f0e51b0c4b3ab

ACTIVE=NONE
PENDING=NONE
PAIR=NONE

REPLAY=
17c7bcb61a9ba6b360ce65951596dd45

MODEL=
43f282ab49b595a56012159243c0b2c4

OWNER_HEAD=
38b806987c92c6c85c57fc9900f5865d

## 5. Native post-import consumption audit

Audit proceeded to shard knowledge-status extraction.

## 6. Final status

HOLD=SHARD01_NOT_CONSUMED:AMBIGUOUS_MULTIPLE_DOCUMENTS

## Interpretation boundary

This checkpoint records that:
- source authority and shard hash precheck passed;
- shard 01 was ingested in a Gen3 sandbox;
- the document was sealed;
- native learning cycles occurred;
- a fresh process could observe the sealed document and child model/head.

However, the native consumption audit did not establish that shard_01 was consumed. The run explicitly failed closed with:
SHARD01_NOT_CONSUMED:AMBIGUOUS_MULTIPLE_DOCUMENTS

Therefore no consumed/learned-from-source claim should be promoted from this run until document ambiguity is resolved by native evidence.
