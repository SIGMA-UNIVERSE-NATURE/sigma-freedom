# SIGMA VM â€” WINDOW ASSIGNMENTS v1.0

Use one block per chat window. Do not combine blocks.

---

## WINDOW W01 â€” BOUNDARY AUDITOR

```text
INHERIT SIGMA VM EXPERIMENT MAP v1.0.
WINDOW_ID=W01_BOUNDARY_AUDITOR
NODE_ID=E04_BOUNDARY_BASELINE_005
MODE=READ_ONLY
ONE_TASK_ONLY=exact inventory of the five remaining trusted custom C primitives.

Read current SIGMA VM candidate, current adapter source, and current compiled host binary.
Pin every input SHA before analysis.
Record exact primitive names, definitions, call sites, semantic category, bootstrap dependency, source presence, and binary presence.
Independently confirm math_floordiv is absent.
Measure whether bytes_f64_le_at is present; do not assume it.
Do not patch, rename, remove, add, compile a new candidate, or alter ABI/Foundation/corpus.
Return TRUSTED_HOST_BOUNDARY_BASELINE_005.json, callsite map, binary audit, and W01_HANDOFF.md.
End with exactly W01_RESULT_PASS or W01_RESULT_HOLD: <exact reason>.
```

---

## WINDOW W02 â€” FLOAT64 CORPUS CURATOR

```text
INHERIT SIGMA VM EXPERIMENT MAP v1.0.
WINDOW_ID=W02_F64_CORPUS_CURATOR
NODE_ID=E05_FLOAT64_CORPUS_FREEZE_001
MODE=CORPUS_ONLY
ONE_TASK_ONLY=freeze an independent FLOAT64 raw-bit corpus and oracle contract.

Preserve the historical v13a failures:
qnan_payload1
qnan_neg_payload
snan_payload1

Create a versioned public corpus covering signed zero, finite extrema, normals, subnormals, infinities, qNaN payload/sign variants, and sNaN payload variants.
Every case must contain the exact expected 64-bit pattern.
Define a deterministic withheld-corpus generator whose seed is derived from the future frozen candidate source SHA.
The oracle must be independent from the candidate implementation.
Do not edit VM source, adapter source, frozen ABI, Foundation, or ledger.
Return corpus files, oracle contract, checksums, and W02_HANDOFF.md.
End with exactly W02_RESULT_FROZEN_PASS or W02_RESULT_HOLD: <exact reason>.
```

---

## WINDOW W03 â€” FLOAT64 IMPLEMENTER

**Do not open until W01 and W02 PASS.**

```text
INHERIT SIGMA VM EXPERIMENT MAP v1.0.
WINDOW_ID=W03_F64_IMPLEMENTER
NODE_ID=E06_FLOAT64_REPRESENTATION_CANDIDATE_001
MODE=ONE_CANDIDATE_ONLY

Inputs must include W01 PASS and W02 FROZEN_PASS with exact hashes.
Implement exactly one SIGMA-native representation candidate.
Primary hypothesis: preserve raw 64-bit payload beside the numeric view so untouched constants remain bit-exact while numeric operators use the numeric view.
Do not retry numeric-only reconstruction already rejected by v13a.
Do not add a target-specific C FLOAT64 decoder/bitcast and call the reduction complete.
Do not edit corpus, evaluator, ABI, Foundation, canonical state, or 512 ledger.
Do not claim PASS.
Return one candidate, minimal diff, compile result, artifact hashes, and W03_HANDOFF.md.
End with exactly W03_CANDIDATE_READY, W03_RESULT_HOLD: <reason>, or W03_RESULT_REJECT: <reason>.
```

---

## WINDOW W04 â€” CANDIDATE FREEZER

```text
WINDOW_ID=W04_CANDIDATE_FREEZER
NODE_ID=E07_CANDIDATE_FREEZE_001
MODE=NO_SOURCE_PATCH
ONE_TASK_ONLY=freeze identity and deterministic compilation.

Compile the exact W03 source at least twice from clean outputs.
Pin source, bytecode, adapter, host binary, ABI, Foundation, and corptÈ\Ú\Ë‚”ØØ[ˆ[\[Y[][Ûˆ›ÜˆÛÜœ\ÈX™[È[™^XİYİ]]\Ú\Ë‚‘È›İ]Ú[HÛİ\˜ÙK‚”™]\›ˆĞS‘QUWÑ”‘QV‘WÓPS’Q‘TÕšœÛÛˆ[™ÌÒS‘Ñ‘‹›Y‚‘[™Ú]^XİHÌÔ‘TÕSÔTÔÈÜˆÌÔ‘TÕSÒS•SQˆ^Xİ™X\ÛÛ‹‚˜‚‹KKB‚ˆÈÈÒS‘ÕÈÌH8 %S‘TS‘S•“ĞUUSPUÔ‚‚˜^•ÒS‘Õ×ÒQUÌWÑÑUSPUÔ‚““ÑWÒQQLÒS‘TS‘S•Ñ“ĞUÑUSPUSÓ—ÌB“SÑOT‘PQÓÓ“WÑUSPUÔ‚“Ó‘WÕTÒ×ÓÓ“OXš]Y^Xİ]˜[X][Û‹‚‚•™\šYHØ[™Y]HÒHYØZ[œİÌ‚”[ˆX›XÈÛÜœ\È[™]\›Z[š\İXÈÚ][ÛÜœ\Ë‚ÛÛ\\™H˜]ÈXš]]\›œË›İ›Ü›X]Y[Y\šXÈ˜[Y\Ë‚”›İ™H]\×ÙÛWØ]XœÙ[˜ÙHœ›ÛHY\\ˆÛİ\˜ÙH[™ÛÛ\[YÜİš[˜\K‚‘È›İ]Ú‚[HZ\ÛX]ÚZY[È‘R‘PÕÚ]HZ[š[X[Ûİ[\™^[\K‚‘[™Ú]^XİHÌWÔ‘TÕSÔTÔÈÜˆÌWÔ‘TÕSÔ‘R‘PÕˆ^Xİ™X\ÛÛ‹‚˜‚‹KKB‚ˆÈÈÒS‘ÕÈÌˆ8 %‘QÔ‘TÔÒSÓˆ•S“‘T‚‚˜^•ÒS‘Õ×ÒQUÌ—Ô‘QÔ‘TÔÒSÓ—Ô•S“‘T‚““ÑWÒQQLWÑ•SÕ“WÔ‘QÔ‘TÔÒSÓ—ÌB“SÑOT‘PQÓÓ“WÕTÕ“Ó‘WÕTÒ×ÓÓ“OY[[[]]X›H™YÜ™\ÜÚ[Û‹‚‚”[ˆÜÚ]]™HLKÌLKÒQÓPHX[›Ü›YY˜Z[XÛÜÙYNKÌNKÈX[›Ü›YYYÜ™Y[Y[MËÌNHÚ]HØ[YHÛÈÛ\ÜÚYšYY]™\™Ù[˜Ù\Ë“ÓÔ‘UˆMËÌMË[™ÛÛ\]HÛİ™\˜YÙHØ]\Ë‚Ø\\™HËÜİİ]Üİ\œˆ›Üˆ]™\HØ\ÙK‚‘È›İ]Ú‚‘[™Ú]^XİHÌ—Ô‘TÕSÔTÔÈÜˆÌ—Ô‘TÕSÔ‘R‘PÕˆ^Xİ™X\ÛÛ‹‚˜‚‹KKB‚ˆÈÈÒS‘ÕÈÌÈ8 %ÓÓ“ÓÕÕT•S“‘T‚‚˜^•ÒS‘Õ×ÒQUÌ×ĞÓÓĞ“ÓÕÕTÔ•S“‘T‚““ÑWÒQQLLÕÓ×ĞÖPÓWĞÓÓĞ“ÓÕÕTÌB“SÑOQÑS‘TUQÓÕUU×ÓÓ“B“Ó‘WÕTÒ×ÓÓ“O]ÛËXŞXÛHš^YÚ[‚‚”™[[İ™Hİ[Hİ]]È™Y›Ü™HXXÚŞXÛK‚ŞXÛHˆ]\İÛÛœİ[YHŞXÛHHİ]]‚›İİ]]È]\İ\]X[ÒKLMˆ™YŒÎMXLÌŒNYYMÙ˜ÌŒŒ˜Y™ŒŒNMÌ˜ÍÍLŒNLÌÎYNMË‚Ø\\™HÛÛ[X[™ËËİİ]İ\œ‹[™Ù[™\˜]Y\Y˜Xİ\Ú\Ë‚‘È›İ]Ú‚‘[™Ú]^XİHÌ×Ô‘TÕSÔTÔËÌ×Ô‘TÕSÒÓˆ™X\ÛÛ‹ÜˆÌ×Ô‘TÕSÔ‘R‘PÕˆ™X\ÛÛ‹‚˜‚‹KKB‚ˆÈÈÒS‘ÕÈÌ8 %Ô•P’SUH•S“‘T‚‚˜^•ÒS‘Õ×ÒQUÌÔÔ•P’SUWÔ•S“‘T‚““ÑWÒQQLLWĞÔ“ÔÔ×ÔÕP”ÕUWÔ‘TVWÌB“SÑOT‘PQÓÓ“WÔ‘TVB“Ó‘WÕTÒ×ÓÓ“OXÜ›ÜÜË\İXœİ˜]H™\^K‚‚•\ÙHHØ[YHœ›Ş™[ˆØ[™Y]HÛİ\˜ÙKP’K[™ÛÜœ\ÈÛˆÔÈ[™Û™H[™\[™[—ÍİXœİ˜]K‚ÛÛ\\™HÙ[X[XÜÈ[™š^Y\Ú[ÒK‚‘È›İ™\]Z\™H˜]]™H^Xİ]X›HÒH\]X[]HXÜ›ÜÜÈ\˜Ú]Xİ\™\Ë‚‘È›İ]Ú‚‘[™Ú]^XİHÌÔ‘TÕSÔTÔÈÜˆÌÔ‘TÕSÒÓÔ‘R‘PÕˆ^Xİ™X\ÛÛ‹‚˜‚‹KKB‚ˆÈÈÒS‘ÕÈÌH8 %‘T‘PÕUSPUÔ‚‚˜^•ÒS‘Õ×ÒQUÌWÕ‘T‘PÕÑUSPUÔ‚““ÑWÒQQLL—Ô‘QPÕSÓ—Õ‘T‘PÕÌ‚“SÑOU‘T‘PÕÓÓ“B“Ó‘WÕTÒ×ÓÓ“OXÛ\ÜÚYH™YXİ[ÛˆÌ‹‚‚”™XY[\İ™X[H]šY[˜ÙNÈ™\Z\ˆ›İ[™Ë‚•™\šYHYX\İ\™Y\İYİ\İÛHš[Z]]™HÛİ[Ú[™Ù\ÈHOˆÚ]›ÈY[ˆ™\XÙ[Y[‚’\ÜİYHÛ›HTÔ×ÕÒUÑQ’S‘QÔĞÓÔKÓÜˆ‘R‘PÕ‚‘^XÚ]HÙY\•SĞ×Ñ”‘QWÓUU‘WÔÕPÒÏRÓ[›\ÜÈÙ\\˜][H›İ™[‹‚‘[™Ú]^XİHÌWÕ‘T‘PÕˆİ]\Ïˆ8 %ØÛÜKÜ™X\ÛÛ‹‚˜‚‹KKB‚ˆÈÈÒS‘ÕÈÌL8 %‘V’SRUU‘HÑSPÕÔ‚‚˜^•ÒS‘Õ×ÒQUÌLÓ‘VÔ’SRUU‘WÔÑSPÕÔ‚““ÑWÒQQLL×Ó‘VÔ’SRUU‘WÔÑSPÕSÓ—ÌB“SÑOPSSTÒT×ÓÓ“B“Ó‘WÕTÒ×ÓÓ“O\Ù[Xİ^XİHÛ™H™^š[Z]]™K‚‚•\ÙHHYX\İ\™Y™[XZ[š[™È[™[ÜHÛ›K‚Z[]È\[™[˜ŞHÜ˜\[™]˜[X]ÜˆÛÛ˜Xİ‚ÚÛÜÙHÛ™Hš[Z]]™KÛ™H\İ\Ú\ËÛ™H^\š[Y[Û™H›Û˜XÚÈÜš]\š[Û‹‚‘È›İ[\[Y[]‚‘[™Ú]^XİHÌLÔÑSPÕSÓ—Ô‘PQHÜˆÌLÔ‘TÕSÒÓˆ^Xİ™X\ÛÛ‹‚˜