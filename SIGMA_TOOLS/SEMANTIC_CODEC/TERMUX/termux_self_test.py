#!/data/data/com.termux/files/usr/bin/python
# -*- coding: utf-8 -*-
from sigma_semantic_codec_termux import (
    LANGUAGES,
    GRAPH_SCHEMA,
    encode_payload,
    decode_payload,
    verify_payload,
    map_languages_payload,
)


def main() -> None:
    raw = "SIGMA preserves meaning across languages while keeping provenance. / SIGMA giữ nghĩa và provenance."
    graph = {
        "schema": GRAPH_SCHEMA,
        "propositions": [
            {
                "id": "P001",
                "epistemic": "DECL",
                "subject_id": "SIGMA.SEMANTIC_CODEC",
                "predicate_id": "PRESERVES",
                "object_id": "SEMANTIC_IDENTITY",
                "negated": False,
                "modality": "required",
                "conditions": [],
                "quantities": [],
                "scope": {"test": "TERMUX"},
                "provenance_refs": ["SRC_TEST"],
            },
            {
                "id": "P002",
                "epistemic": "DECL",
                "subject_id": "SIGMA.SEMANTIC_CODEC",
                "predicate_id": "PRESERVES",
                "object_id": "PROVENANCE",
                "negated": False,
                "modality": "required",
                "conditions": [],
                "quantities": [],
                "scope": {"test": "TERMUX"},
                "provenance_refs": ["SRC_TEST"],
            },
        ],
        "relations": [],
        "uncertainties": [],
    }
    package = encode_payload({
        "text": raw,
        "source_language": "vi",
        "semantic_graph": graph,
        "provenance": [{"id": "SRC_TEST", "source": "TERMUX_SELF_TEST"}],
        "preserve_exact_raw": True,
        "store": False,
    })
    decoded = decode_payload({"package": package, "mode": "exact"})
    assert decoded["text"] == raw
    assert decoded["exact_roundtrip_verified"] is True

    verified = verify_payload({"package": package})
    assert verified["pass"] is True
    assert verified["exact_raw_roundtrip"] is True

    clause_map = [{"clause_id": "C1", "proposition_ids": ["P001", "P002"]}]
    views = [
        {"language": lang, "text": f"TERMUX structural view {lang}", "clause_map": clause_map}
        for lang in LANGUAGES
    ]
    mapped = map_languages_payload({"package": package, "views": views})
    assert mapped["target_language_count"] >= 10
    assert mapped["all_structural_coverage_pass"] is True
    assert len(LANGUAGES) == 12

    print("PASS exact_raw_roundtrip")
    print("PASS graph_integrity")
    print("PASS multilingual_structural_coverage=12")
    print("NOTE semantic equivalence requires render->re-extract provider round-trip")


if __name__ == "__main__":
    main()
