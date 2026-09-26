# SIGMA Global Durable Head + Accepted State — Gen3

Date: 2026-09-26
Source: user-supplied Termux runtime output.

## 0. Durable head bootstrap precheck

PRECHECK=PASS

## 1. Global durable head + accepted state

DURABLE_HEAD_RECORD_ID=
0db2aa08a8ab62e8026ee0f4ced7556aace674106d9f83079967de8ab6461715

DURABLE_HEAD_RECORD=
/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_ail/SIGMA_HEAD/records/0db2aa08a8ab62e8026ee0f4ced7556aace674106d9f83079967de8ab6461715.env

DURABLE_HEAD_RECORD_SHA256=
cb8b9930b84947fd6f3a73a446c14d38dcffc941cc25075fed4c99ced6c25633

ACCEPTED_STATE_RECORD=
/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_ail/SIGMA_VKM_927_ACCEPTED_STATE/records/0db2aa08a8ab62e8026ee0f4ced7556aace674106d9f83079967de8ab6461715.env

ACCEPTED_STATE_RECORD_SHA256=
f27dd17ad949e8a5aa7ed9a79905a7e3f9edafe3243d3d94e09c5950dc2affcc

GLOBAL_DURABLE_HEAD=PASS
ACCEPTED_STATE_AUTHORITY=PASS

## 2. Current durable head pointer

SCHEMA=SIGMA_DURABLE_HEAD_POINTER_V1

CURRENT_RECORD=
/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_ail/SIGMA_HEAD/records/0db2aa08a8ab62e8026ee0f4ced7556aace674106d9f83079967de8ab6461715.env

CURRENT_RECORD_SHA256=
cb8b9930b84947fd6f3a73a446c14d38dcffc941cc25075fed4c99ced6c25633

BRAIN_HEAD=
599c639a3a58c7971518727c303c876e

MODEL_GENERATION=3

MODEL_ID=
4e28b7b00428271a4d09f1791d5d46fb

## 3. Accepted-state pointer

SCHEMA=SIGMA_VKM_927_ACCEPTED_STATE_POINTER_V1

CURRENT_RECORD=
/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_ail/SIGMA_VKM_927_ACCEPTED_STATE/records/0db2aa08a8ab62e8026ee0f4ced7556aace674106d9f83079967de8ab6461715.env

CURRENT_RECORD_SHA256=
f27dd17ad949e8a5aa7ed9a79905a7e3f9edafe3243d3d94e09c5950dc2affcc

BRAIN_HEAD=
599c639a3a58c7971518727c303c876e

MODEL_GENERATION=3

MODEL_ID=
4e28b7b00428271a4d09f1791d5d46fb

## 4. Canonical verification

CANONICAL_HEAD=
599c639a3a58c7971518727c303c876e

CANONICAL_MODEL_GENERATION=3

DNA15_STEP=6

GLOBAL_DURABLE_HEAD=PASS
ACCEPTED_STATE_POINTER=PASS

MODEL_MUTATION=NO
DNA15_MUTATION=NO

NEXT=BIND_FROZEN_EVALUATOR_TO_DURABLE_HEAD

TERMUX_PARENT_SHELL_STILL_ALIVE=YES

## Interpretation boundary

This checkpoint records that canonical Gen3 now has:
- a durable global head record;
- a matching accepted-state authority record;
- current pointers for both durable-head and accepted-state authorities;
- matching brain head, generation, and model ID across the canonical state and both pointers;
- no model mutation and no DNA15 mutation during bootstrap.

This is pointer/authority bootstrap evidence. It does not itself prove the frozen evaluator is already bound; the next recorded action is BIND_FROZEN_EVALUATOR_TO_DURABLE_HEAD.
