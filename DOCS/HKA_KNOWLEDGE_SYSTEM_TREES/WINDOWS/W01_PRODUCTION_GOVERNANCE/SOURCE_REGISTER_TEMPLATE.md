---
title: "HKA SOURCE_REGISTER.md Template"
version: "1.0"
status: "PROPOSED REFERENCE TEMPLATE"
---

# HKA SOURCE REGISTER

## 1. Source hierarchy

Ưu tiên theo claim và lĩnh vực:

1. standards, official datasets, primary sources, peer-reviewed primary research;
2. systematic reviews, consensus reports, authoritative reference works;
3. university/academy/museum/professional-society resources;
4. high-quality secondary explanatory sources;
5. tertiary/popular sources chỉ dùng cho orientation, không khóa high-risk claim.

Không bắt buộc mọi node dùng nguồn cấp 1; bắt buộc nguồn phải phù hợp loại claim.

## 2. Source record

### SOURCE: <SOURCE ID>

```text
SOURCE ID:
TITLE:
AUTHOR / INSTITUTION:
YEAR / VERSION:
SOURCE TYPE:
PUBLISHER / JOURNAL:
URL / DOI / IDENTIFIER:
ACCESS DATE:
LANGUAGE:
AUTHORITY LEVEL:
PRIMARY DOMAIN:
```

### Use

```text
SUPPORTED NODE IDS:
SUPPORTED CLAIMS:
WHAT THIS SOURCE DOES NOT ESTABLISH:
KNOWN LIMITATIONS:
CONFLICT OF INTEREST / BIAS NOTES:
FRESHNESS REQUIREMENT:
```

### Verification

```text
SOURCE EXISTS: YES/NO
CLAIM MATCH: YES/NO
CURRENT ENOUGH FOR CLAIM: YES/NO/NOT_APPLICABLE
CROSS-CHECK REQUIRED: YES/NO
EXPERT REVIEW REQUIRED: YES/NO
```

## 3. Conflicting sources

Khi nguồn đáng tin cậy mâu thuẫn:

- không chọn nguồn thuận ý;
- xác định khác biệt về dữ liệu/method/definition/time period;
- ghi uncertainty trong node;
- nếu ảnh hưởng claim core, Director không cho prompt lock cho tới khi cách trình bày trung thực được xác định.

## 4. Freshness

Các lĩnh vực thay đổi nhanh phải có source-access date và version/date của dữ liệu. Nguồn lịch sử/classic không bị loại chỉ vì cũ khi claim là historical/foundational.

## 5. Completion

```text
TOTAL SOURCES:
CORE NODES WITHOUT SUPPORTING SOURCE:
HIGH-RISK CLAIMS WITHOUT CROSS-CHECK:
EXPERT REVIEW ITEMS:
READY FOR DIRECTOR REVIEW: YES/NO
```