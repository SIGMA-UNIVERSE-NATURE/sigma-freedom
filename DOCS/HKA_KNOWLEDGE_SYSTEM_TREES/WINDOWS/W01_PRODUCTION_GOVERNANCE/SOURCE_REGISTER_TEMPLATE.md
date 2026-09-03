---
title: "HKA SOURCE_REGISTER.md Template"
version: "1.1"
status: "PROPOSED REFERENCE TEMPLATE — ARCHITECT REVIEW REQUIRED"
---

# HKA SOURCE REGISTER

## 1. Principle: source fitness by claim type

Không dùng một universal numbered hierarchy cho mọi lĩnh vực. Nguồn tốt nhất phụ thuộc loại claim.

| Claim type | Preferred evidence/source roles | Common secondary support | Notes |
|---|---|---|---|
| Scientific state-of-evidence / medical consensus | systematic review, meta-analysis, consensus/guideline, authoritative synthesis | strong primary studies | một study riêng lẻ không đại diện toàn field |
| Scientific mechanism / emerging research | primary peer-reviewed research + replication/corroboration | review/synthesis | certainty phải phản ánh maturity |
| Official statistics / measured public data | responsible official dataset/agency, exact dataset version | methodological reports | ghi table/series/version |
| Historical event / contemporaneous evidence | primary historical sources, archives, material evidence | scholarly editions/research | primary source không tự động là interpretation đúng nhất |
| Historical interpretation | peer-reviewed scholarly interpretation using primary evidence | authoritative monographs/reviews | distinguish evidence from interpretation |
| Law / regulation / policy in force | current authoritative legal text, official regulator/court source where applicable | legal commentary | currentness/jurisdiction critical |
| Philosophy / humanities | primary text/work + scholarly interpretation | authoritative reference works | representation of competing readings may be required |
| Institutional/technical standard | current issuing-body standard/specification | official implementation guidance | exact version required |
| Definition / taxonomy | authoritative standard, disciplinary reference, consensus classification | scholarly reference | record scope and version |

Source fitness is evaluated per claim, not per source globally.

## 2. Source record

### SOURCE: <SOURCE ID>

```text
SOURCE ID:
TITLE:
AUTHOR / INSTITUTION:
YEAR / VERSION:
SOURCE TYPE:
PUBLISHER / JOURNAL / ISSUING BODY:
URL / DOI / IDENTIFIER:
ACCESS DATE:
LANGUAGE:
PRIMARY DOMAIN:
JURISDICTION / POPULATION / TIME RANGE, IF RELEVANT:
RETRACTION / SUPERSESSION STATUS:
```

### Source limitations

```text
KNOWN LIMITATIONS:
CONFLICT OF INTEREST / BIAS NOTES:
FRESHNESS REQUIREMENT:
WHAT THIS SOURCE CANNOT ESTABLISH:
```

## 3. Stable claim record

Every material/high-risk claim must have a stable Claim ID.

```text
CLAIM ID:
NODE ID:
CLAIM TEXT / SCOPE:
CERTAINTY:
CONTENT CLASS:
CONTEXT DEPENDENCE:
NORMATIVE STATUS:
MODEL STATUS / APPROXIMATION:
HIGH-RISK CLAIM: YES/NO
```

## 4. Claim-to-source mapping record

```text
CLAIM ID:
SOURCE ID:
SOURCE LOCATION / SECTION / PAGE / TABLE / DATASET VERSION:
SUPPORT TYPE: SUPPORTS / QUALIFIES / CONTRADICTS / CONTEXT
EVIDENCE ROLE:
SOURCE FITNESS FOR THIS CLAIM: HIGH / MEDIUM / LOW / NOT_FIT
RATIONALE FOR FITNESS:
CROSS-CHECK STATUS: NOT_REQUIRED / PENDING / PASS / CONFLICT_RECORDED
RETRACTION / SUPERSESSION STATUS VERIFIED: YES/NO/NOT_APPLICABLE
```

Free-text `SUPPORTED CLAIMS` alone is not sufficient for high-risk claims.

## 5. High-risk claim rule

High-risk claims require:

```text
STABLE CLAIM ID
EXPLICIT CLAIM-TO-SOURCE MAP
SOURCE LOCATION
FITNESS = HIGH or justified MEDIUM
CROSS-CHECK = PASS unless Window Contract explicitly accepts single-authority source
EXPERT REVIEW STATUS when domain requires it
```

Examples include medical/safety, legal, contested historical attribution, high-impact statistical claims, sensitive social claims and claims with serious visual-misrepresentation risk.

## 6. Conflicting sources

Khi nguồn phù hợp mâu thuẫn:

1. không chọn nguồn thuận ý;
2. xác định khác biệt về data/method/definition/jurisdiction/time period;
3. map `SUPPORTS / QUALIFIES / CONTRADICTS` per claim;
4. update certainty/content class if needed;
5. record conflict in node and Academic QA Report;
6. nếu ảnh hưởng core claim, không prompt-lock cho tới khi representation trung thực được xác định.

## 7. Freshness

Fast-changing claims phải ghi access date, source version và supersession status. Historical/classic primary sources không bị loại chỉ vì cũ khi claim chính là historical/foundational.

## 8. Completion metrics

```text
TOTAL SOURCES:
TOTAL MATERIAL CLAIM IDS:
CLAIMS WITH >=1 FIT SOURCE:
HIGH-RISK CLAIMS:
HIGH-RISK CLAIMS WITH REQUIRED CROSS-CHECK:
CLAIMS WITH UNRESOLVED SOURCE CONFLICT:
RETRACTED/SUPERSEDED SOURCE DEPENDENCIES:
EXPERT REVIEW ITEMS:
CLAIM-TO-SOURCE COVERAGE: <percent>
READY FOR ACADEMIC QA: YES/NO
```

Director Academic Gate cannot PASS with unsupported high-risk claims or unresolved source-fitness failures.