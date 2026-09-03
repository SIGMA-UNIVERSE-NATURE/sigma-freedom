---
title: "HKA W01 — Canonical Prompt Hash Payloads"
window_id: "W01"
version: "2.0"
status: "COMPLETE / 12 OF 12 VERIFIED BY CONSTRUCTION"
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
from pathlib import Path

path = Path("HKA-VIS-W01-0001.json")
raw = path.read_bytes()
record = json.loads(raw.decode("utf-8"))
canonical = json.dumps(
    record,
    ensure_ascii=False,
    sort_keys=True,
    separators=(",", ":"),
).encode("utf-8")

assert raw == canonical
print(hashlib.sha256(raw).hexdigest())
```

## Full registry

| Asset ID | Payload file | Expected SHA-256 | Batch |
|---|---|---|---|
| HKA-VIS-W01-0001 | `HKA-VIS-W01-0001.json` | `c5d839c819e5ed185a30033af26bdb5dd79d28c1db00269492ad7d6e9d5dbf38` | B00 |
| HKA-VIS-W01-0002 | `HKA-VIS-W01-0002.json` | `a922ea27d31b9f50803a0ebb48adf59b9fab8ee9449c81c59739d0efd7e89793` | B00 |
| HKA-VIS-W01-0003 | `HKA-VIS-W01-0003.json` | `0d1477cf80ed5ac70d6f08db0d7c97927d69f521635bfbaf52047a4fc9465a42` | B01 |
| HKA-VIS-W01-0004 | `HKA-VIS-W01-0004.json` | `1d1d6822e4fed507f3c13485ab9227d7f0b440d23b6008b4b10d4fa7ab85fd5a` | B01 |
| HKA-VIS-W01-0005 | `HKA-VIS-W01-0005.json` | `e0f96836a6acfa5491e7bf3fc332c2dec10f34cb8bdac15d7a069685a8f5dff9` | B01 |
| HKA-VIS-W01-0006 | `HKA-VIS-W01-0006.json` | `5241778158c37be1efee79a83f537927ea9664867430ce47c0846473366aaad3` | B01 |
| HKA-VIS-W01-0007 | `HKA-VIS-W01-0007.json` | `5bb0ffeccdadc0dab9c8be096f27e008d5a5e42ff7a1139fab5460dec397f3ef` | B01 |
| HKA-VIS-W01-0008 | `HKA-VIS-W01-0008.json` | `85aeace68eff5312a77b3283e0e4d339b37897f1e773a52669f9e811675f0a71` | B01 |
| HKA-VIS-W01-0009 | `HKA-VIS-W01-0009.json` | `2d3aedd6742607ca71d2e8ebf495960abfc0bb542e9e693c1d1fcfa6712ccb92` | B02 |
| HKA-VIS-W01-0010 | `HKA-VIS-W01-0010.json` | `327994459702f02039131329d3949429fa6e3f5ef7678117247dabab91f4e283` | B02 |
| HKA-VIS-W01-0011 | `HKA-VIS-W01-0011.json` | `067828db12c464f4c9f01f5cc4748ac16d525d90ea374c3aceaefbd7125187bf` | B02 |
| HKA-VIS-W01-0012 | `HKA-VIS-W01-0012.json` | `abba6830e4859fc7506119959a29b93a1a39d2b4916cf7c80840e7eb3f7dca59` | B02 |

## Integrity relationship

For each Asset ID:

```text
SHA256(payload file bytes)
=
prompt_sha256 in BATCH_MANIFEST.json
=
PROMPT_SHA256 in VISUAL_PRODUCTION_MANIFEST.csv
```

A mismatch is P0 and must stop the batch.

## Authorization boundary

```text
B00 HASH PAYLOADS: COMPLETE
B01 HASH PAYLOADS: COMPLETE
B02 HASH PAYLOADS: COMPLETE
```

Hash payload completion removes the previous B01/B02 pre-production condition. Production still requires separate architect acceptance and batch authorization. This directory itself does not authorize image generation, R2 upload, merge or website deployment.
