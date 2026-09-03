---
title: "HKA W01 — Prompt Hash Payload Test Vectors"
window_id: "W01"
version: "1.0"
status: "B00 COMPLETE / B01-B02 PRE-PRODUCTION CONDITION"
language: "vi"
date: "2026-09-03"
---

# HKA W01 — PROMPT HASH PAYLOADS

Thư mục này lưu canonical byte payload dùng để tái tính `prompt_sha256` theo profile:

```text
HKA-PROMPT-RECORD-JSON-V1
```

## Canonical serialization

Mỗi payload là một JSON object:

- UTF-8;
- không BOM;
- key sắp xếp lexicographic;
- separator chính xác `,` và `:`;
- không whitespace ngoài string values;
- `ensure_ascii=false`;
- không chứa trường `prompt_sha256`;
- file không có newline cuối.

Lệnh tham chiếu:

```python
import hashlib
import json

canonical = json.dumps(
    record_without_prompt_sha256,
    ensure_ascii=False,
    sort_keys=True,
    separators=(",", ":"),
).encode("utf-8")

print(hashlib.sha256(canonical).hexdigest())
```

## Test vectors hiện có

| Asset ID | Payload file | Expected SHA-256 | Batch |
|---|---|---|---|
| HKA-VIS-W01-0001 | `HKA-VIS-W01-0001.json` | `c5d839c819e5ed185a30033af26bdb5dd79d28c1db00269492ad7d6e9d5dbf38` | B00 |
| HKA-VIS-W01-0002 | `HKA-VIS-W01-0002.json` | `a922ea27d31b9f50803a0ebb48adf59b9fab8ee9449c81c59739d0efd7e89793` | B00 |

Hai test vector bao phủ toàn bộ Calibration Batch B00. Vì vậy, sau Architect Acceptance và một Production Handoff Authorization riêng, B00 có thể xác minh prompt hashes độc lập.

## Authorization boundary

B01 và B02 hiện có prompt hashes trong manifests nhưng chưa có từng canonical payload file riêng trong thư mục này. Do đó:

```text
B00: ELIGIBLE FOR SEPARATE PRODUCTION AUTHORIZATION AFTER ARCHITECT ACCEPTANCE
B01: NOT AUTHORIZED UNTIL PAYLOADS 0003–0008 ARE MATERIALIZED AND VERIFIED
B02: NOT AUTHORIZED UNTIL PAYLOADS 0009–0012 ARE MATERIALIZED AND VERIFIED
```

Đây không phải placeholder và không thay đổi prompt content. Nó là điều kiện tăng cường khả năng tái lập trước khi mở production hàng loạt.

Không được dùng hai test vector B00 để suy ra hoặc tái tạo payload của asset khác.
