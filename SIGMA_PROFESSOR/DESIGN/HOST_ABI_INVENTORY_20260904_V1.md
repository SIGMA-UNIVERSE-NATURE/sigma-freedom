# SIGMA HOST ABI INVENTORY — 2026-09-04 V1

## Evidence status

Source inspected by device-side grep: `~/SIGMA/sigma_genesis1/sigma_vm.c`.

`HOST_OP_COUNT=93`.

Presence in `sigma_vm.c` is **SOURCE_EVIDENCE**, not automatically locked-binary/runtime proof. Important operations must still be exercised from `.sigma` through the locked VM before promotion.

Locked runtime identities currently used by the learning lane:

- SIGMAC SHA-256: `65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- VM SHA-256: `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

## 93 host operations found in source

### Containers

- `list_new`
- `list_len`
- `list_push`
- `list_get`
- `list_set`
- `list_pop`
- `list_shift`
- `list_unshift`
- `list_reverse`
- `list_slice`
- `list_sort`
- `map_new`
- `map_set`
- `map_get`
- `map_has`
- `map_delete`
- `map_keys`
- `map_values`
- `map_items`

### Bytes

- `bytes_new`
- `bytes_len`
- `bytes_get`
- `bytes_slice_string`
- `bytes_u8`
- `bytes_u16`
- `bytes_u32`
- `bytes_i64`
- `bytes_f64`
- `bytes_get_f64`
- `bytes_raw_utf8`
- `bytes_write`

### String / conversion / character

- `str_len`
- `str_byte`
- `str_starts`
- `str_slice`
- `str_find`
- `str_upper`
- `str_lower`
- `str_strip`
- `str_capitalize`
- `str_title`
- `str_contains`
- `str_ends`
- `str_replace`
- `str_split`
- `str_join`
- `is_alpha`
- `is_digit`
- `value_type`
- `numeric_to_int`
- `to_int`
- `to_float`

### Filesystem / persistence

- `read_bytes`
- `read_text`
- `write_text`
- `append_text`
- `file_exists`
- `mkdir`
- `rmdir`
- `listdir`
- `pwd`
- `getenv`

### JSON / encoding / digest

- `json_decode`
- `json_encode`
- `json_load`
- `json_dump`
- `base64_decode`
- `base64_encode`
- `crypto_digest`

### Time / random

- `time_now`
- `time_sleep`
- `time_strftime`
- `random_bytes`
- `random_choice`
- `random_float`
- `random_int`
- `random_shuffle`
- `random_uuid`

### Network

- `net_fetch`
- `net_ping`
- `dns_lookup`

### Math

- `math_abs`
- `math_ceil`
- `math_cos`
- `math_exp`
- `math_floor`
- `math_log`
- `math_pow`
- `math_round`
- `math_sin`
- `math_sqrt`
- `math_tan`

### Interactive

- `input`

## Already materially useful to the native-learning roadmap

The source inventory shows that proposed additions should NOT duplicate existing container, map, append, directory, clock, string-search, JSON, network, or digest facilities before their exact semantics are inspected and runtime-tested.

In particular:

- native set/dedup does not require a new `set_*` ABI immediately; SIGMA can represent a set mechanically using `map_set(key, TRUE)` + `map_has(key)`;
- `map_has/map_keys/map_values/map_items/map_delete` already exist in source;
- `append_text` already exists in source;
- `listdir` already exists in source;
- `time_now` already exists and returns `time(NULL)` according to the inspected source excerpt;
- `str_find` already exists;
- direct network primitives already exist in source and may potentially allow SIGMA itself to invoke mechanical transport, subject to runtime and boundary admission tests;
- `crypto_digest` may already satisfy stable SHA-256 identity requirements, but algorithm/signature/return encoding must be inspected before claiming that.

## High-priority unknown semantics to inspect next

1. `read_bytes`: determine whether it supports offset/count bounded reads or always reads the full file.
2. `crypto_digest`: determine supported algorithms, exact arguments, and output encoding; test SHA-256 if available.
3. `write_text`: determine crash/partial-write behavior; determine whether an atomic replacement primitive is still needed.
4. `net_fetch`: determine exact protocol/schemes, redirects, size/time limits, and whether returned bytes/text are mechanically exposed without semantic processing.
5. `json_decode/json_load`: determine whether they can replace the current Python Wikimedia protocol decoder without moving semantic policy to host.
6. `list_sort`: determine ordering semantics and whether sorting is stable/deterministic.
7. Unicode behavior: current `str_len` uses `strlen` and `str_upper/str_lower` use C character functions, therefore Unicode-awareness is NOT proven.

## Likely remaining ABI additions — NOT YET APPROVED

Do not implement until the unknown semantics above are resolved.

Potentially still needed:

- bounded file-range/line read if existing `read_bytes/read_text` always load whole files;
- crash-safe atomic state replacement if `write_text` is not atomic enough for persistent curriculum state;
- possibly file metadata such as size/mtime if curriculum/revalidation cannot obtain it otherwise;
- only if necessary, a purely mechanical Unicode normalization primitive.

No `set_*` addition is currently necessary because native maps can implement set membership.

## Forbidden semantic host additions

Do not add host operations that summarize, classify topics, form concepts, compute semantic similarity, select learning candidates, score knowledge, detect semantic gaps, choose research goals, decide truth, or generate lessons.

Invariant:

`HOST_LEARNING=NO`

`HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN`
