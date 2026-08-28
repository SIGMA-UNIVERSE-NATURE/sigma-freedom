#!/usr/bin/env python3
"""Validate a SLARS-1.1-ZAI protocol and materialized run bundle."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from zai_core import (
    Report,
    StrictJSONError,
    evaluate_evidence,
    parse_json_bytes,
    report_lines,
    sha256_bytes,
    strict_schema_check,
    verify_package_manifest,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--protocol", required=True, type=Path)
    parser.add_argument("--run", required=True, type=Path)
    parser.add_argument("--evidence-root", required=True, type=Path)
    parser.add_argument("--mode", choices=("structure", "evidence"), default="structure")
    args = parser.parse_args(argv)

    root = Path(__file__).resolve().parents[1]
    report = Report()
    receipts: dict[str, str] = {}
    manifest_available = False
    try:
        if args.protocol.is_symlink() or args.run.is_symlink():
            raise StrictJSONError("protocol/run symlinks are forbidden")
        protocol_bytes = args.protocol.read_bytes()
        run_bytes = args.run.read_bytes()
        protocol = parse_json_bytes(protocol_bytes, "protocol")
        run = parse_json_bytes(run_bytes, "run")
        protocol_schema_bytes = (root / "schemas" / "zai_protocol.schema.json").read_bytes()
        run_schema_bytes = (root / "schemas" / "zai_run_bundle.schema.json").read_bytes()
        protocol_schema = parse_json_bytes(protocol_schema_bytes, "protocol_schema")
        run_schema = parse_json_bytes(run_schema_bytes, "run_schema")
        standard_bytes = (root / "ZERO_ANSWER_INJECTION_STANDARD.md").read_bytes()
        manifest_path = root / "MANIFEST.sha256"
        manifest_available = manifest_path.is_file() and not manifest_path.is_symlink()
        manifest_bytes = manifest_path.read_bytes() if manifest_available else b""
        receipts = {
            "PROTOCOL_RAW_SHA256": sha256_bytes(protocol_bytes),
            "RUN_BUNDLE_RAW_SHA256": sha256_bytes(run_bytes),
            "VALIDATOR_SOURCE_SHA256_AT_REPORT": sha256_bytes(Path(__file__).resolve().read_bytes()),
            "CORE_SOURCE_SHA256_AT_REPORT": sha256_bytes((root / "tools" / "zai_core.py").read_bytes()),
            "PROTOCOL_SCHEMA_SHA256": sha256_bytes(protocol_schema_bytes),
            "RUN_SCHEMA_SHA256": sha256_bytes(run_schema_bytes),
            "STANDARD_DOCUMENT_SHA256": sha256_bytes(standard_bytes),
        }
        if manifest_available:
            receipts["PACKAGE_MANIFEST_SHA256"] = sha256_bytes(manifest_bytes)
    except (OSError, StrictJSONError) as exc:
        report.error("LOAD", "STRICT_JSON_ERROR", str(exc))
        if args.mode == "evidence":
            report.set_gate("Z0", "INVALID")
            report.set_gate("ZAI", "INVALID")
        print("\n".join(report_lines(report, args.mode, receipts)))
        return 64

    protocol_valid = strict_schema_check(protocol, protocol_schema, report, "protocol")
    run_valid = strict_schema_check(run, run_schema, report, "run")
    manifest_valid = manifest_available and verify_package_manifest(root, manifest_bytes, report)
    report.package_manifest_status = "PASS" if manifest_valid else "INVALID"
    receipt_valid = manifest_valid
    if not manifest_available:
        report.error("RECEIPT", "PACKAGE_MANIFEST_MISSING", "MANIFEST.sha256")
    if args.mode == "evidence" and protocol_valid and run_valid and receipt_valid:
        evaluate_evidence(protocol, run, protocol_bytes, args.evidence_root, report)
    elif args.mode == "evidence":
        report.set_gate("Z0", "INVALID")
        report.set_gate("ZAI", "INVALID")

    print("\n".join(report_lines(report, args.mode, receipts)))
    if report.errors:
        return 5
    if args.mode == "evidence":
        status = report.gates.get("ZAI", "UNVERIFIED")
        return {"PASS": 0, "FAIL": 2, "INSUFFICIENT_EVIDENCE": 3, "UNVERIFIED": 4, "INVALID": 5}[status]
    return 0


if __name__ == "__main__":
    sys.exit(main())
