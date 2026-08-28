from __future__ import annotations

import copy
import contextlib
import hashlib
import importlib.util
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_bundle", ROOT / "tools" / "validate_bundle.py"
)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)


def fake_sha(label: str) -> str:
    return hashlib.sha256(label.encode("utf-8")).hexdigest()


def load_template(name: str) -> dict:
    with (ROOT / "templates" / name).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def make_items(prefix: str, track: str, count: int = 2) -> list[dict]:
    return [
        {
            "item_id": f"{prefix}-{track}-{index:03d}",
            "family_id": f"FAMILY-{track}-{index:03d}",
            "track": track,
        }
        for index in range(1, count + 1)
    ]


def make_set(set_id: str, phase: str, tracks: list[str], cycle_number: int | None = None) -> dict:
    item_set = {
        "set_id": set_id,
        "phase": phase,
        "sha256": fake_sha(f"set:{set_id}"),
        "key_sha256": fake_sha(f"key:{set_id}"),
        "candidate_can_access_key": False,
        "items": [],
    }
    if cycle_number is not None:
        item_set["cycle_number"] = cycle_number
    prefix = {
        "BASELINE": "BASE",
        "IMMEDIATE": "POST",
        "DEVELOPMENT_RETEST": f"DEV{cycle_number}",
        "REASONING": "REASON",
        "DELAYED": "DELAY",
    }[phase]
    for track in tracks:
        item_set["items"].extend(make_items(prefix, track))
    return item_set


def build_synthetic_protocol() -> dict:
    protocol = load_template("protocol.template.json")
    protocol["artifact_status"] = "LOCKED_PROTOCOL"
    protocol["protocol_id"] = "SYNTHETIC-TEST-PROTOCOL"
    protocol["protocol_lock"] = {
        "status": "LOCKED",
        "locked_at_utc": "2026-08-25T00:00:00Z",
    }
    protocol["lesson"]["original_sha256"] = fake_sha("original")
    protocol["lesson"]["translation_sha256"] = fake_sha("translation")
    protocol["item_sets"] = [
        make_set("BASELINE", "BASELINE", ["D", "R"]),
        make_set("IMMEDIATE", "IMMEDIATE", ["D"]),
        make_set("DEVELOPMENT-1", "DEVELOPMENT_RETEST", ["D"], cycle_number=1),
        make_set("REASONING", "REASONING", ["R"]),
        make_set("DELAYED", "DELAYED", ["D", "R"]),
    ]
    protocol["track_policies"] = [
        {
            "track": "D",
            "baseline_phase": "BASELINE",
            "assessment_phase": "IMMEDIATE",
            "mandatory": True,
            "min_items": 2,
            "absolute_floor": 0.75,
            "min_effect": 0.20,
            "ci_lower_floor": 0.00,
            "retention_required": True,
        },
        {
            "track": "R",
            "baseline_phase": "BASELINE",
            "assessment_phase": "REASONING",
            "mandatory": True,
            "min_items": 2,
            "absolute_floor": 0.75,
            "min_effect": 0.20,
            "ci_lower_floor": 0.00,
            "retention_required": True,
        },
    ]
    protocol["statistics"]["bootstrap_iterations"] = 1000
    return protocol


def build_synthetic_run(protocol: dict, protocol_sha: str) -> dict:
    run = load_template("run_bundle.template.json")
    run.update(
        {
            "artifact_status": "RUN_EVIDENCE",
            "run_id": "SYNTHETIC-TEST-RUN",
            "run_status": "COMPLETE",
            "protocol_sha256": protocol_sha,
        }
    )
    run["timestamps"] = {
        "run_started_at_utc": "2026-08-26T00:00:00Z",
        "run_completed_at_utc": "2026-08-27T04:00:00Z",
        "exposure_started_at_utc": "2026-08-26T01:00:00Z",
        "exposure_completed_at_utc": "2026-08-26T02:00:00Z",
        "delayed_started_at_utc": "2026-08-27T03:00:00Z",
    }
    original_sha = protocol["lesson"]["original_sha256"]
    translation_sha = protocol["lesson"]["translation_sha256"]
    run["identity_bridge"] = {
        "original_sha_auth": original_sha,
        "original_sha_g1_pre": original_sha,
        "original_sha_g1_final": original_sha,
        "original_sha_g3_target": original_sha,
        "original_sha_run_final": original_sha,
        "translation_sha_reviewed": translation_sha,
        "translation_sha_sigmac_input": translation_sha,
        "translation_sha_g3_target": translation_sha,
        "translation_sha_exposed": translation_sha,
        "translation_sha_run_final": translation_sha,
        "protocol_sha_locked": protocol_sha,
        "protocol_sha_at_run_start": protocol_sha,
        "protocol_sha_reported": protocol_sha,
    }
    run["transport_gates"] = {key: "PASS" for key in run["transport_gates"]}
    run["exposure"] = {
        "candidate_input_transcript_sha256": fake_sha("exposure-input"),
        "allowed_context_manifest_matches": True,
        "forbidden_context_match_count": 0,
        "tool_policy_matches": True,
        "evaluator_key_visible": False,
    }
    run["anti_leakage_evidence"] = {
        "scan_policy_sha256": protocol["anti_leakage"]["scan_policy_sha256"],
        "scan_rc": 0,
        "match_count": 0,
        "host_answer_derivation_observed": False,
        "candidate_key_access_observed": False,
        "raw_scanner_transcript_sha256": fake_sha("raw-scan"),
    }

    artifact_by_set = {}
    run["phase_artifacts"] = []
    for item_set in protocol["item_sets"]:
        set_id = item_set["set_id"]
        artifact = {
            "phase": item_set["phase"],
            "set_id": set_id,
            "set_sha256": item_set["sha256"],
            "candidate_input_sha256": fake_sha(f"input:{set_id}"),
            "candidate_output_sha256": fake_sha(f"output:{set_id}"),
            "evaluator_record_sha256": fake_sha(f"evaluation:{set_id}"),
            "rc": 0,
        }
        artifact_by_set[set_id] = artifact
        run["phase_artifacts"].append(artifact)

    phase_scores = {
        "BASELINE": 0.25,
        "IMMEDIATE": 0.75,
        "DEVELOPMENT_RETEST": 1.00,
        "REASONING": 0.75,
        "DELAYED": 0.75,
    }
    run["observations"] = []
    for item_set in protocol["item_sets"]:
        for item in item_set["items"]:
            score = phase_scores[item_set["phase"]]
            observation = {
                "phase": item_set["phase"],
                "set_id": item_set["set_id"],
                "item_id": item["item_id"],
                "family_id": item["family_id"],
                "track": item["track"],
                "external_score": score,
                "correct": score >= 0.5,
                "confidence": 0.80 if score >= 0.5 else 0.20,
                "candidate_output_sha256": artifact_by_set[item_set["set_id"]]["candidate_output_sha256"],
                "evaluator_record_sha256": fake_sha(f"item-eval:{item['item_id']}"),
            }
            if item_set["phase"] == "REASONING":
                observation["audit_record"] = {
                    "premise_ids": ["P1"],
                    "rule_ids": ["R1"],
                    "derived_claim_ids": ["C1"],
                    "constraint_checks": ["CHECK-1"],
                    "counterexample_check": True,
                    "uncertainty": 0.20,
                    "final_answer": "SYNTHETIC TEST ANSWER",
                }
            run["observations"].append(observation)

    run["development_cycles"] = [
        {
            "cycle_number": 1,
            "error_class": "RULE_APPLICATION",
            "error_record_sha256": fake_sha("error-record"),
            "intervention_sha256": fake_sha("intervention"),
            "retest_set_id": "DEVELOPMENT-1",
            "target_tracks": ["D"],
            "no_evaluation_key_leakage": True,
            "rubric_unchanged": True,
        }
    ]
    run["retention_evidence"] = {
        "context_reset_observed": True,
        "allowed_persistence_manifest_sha256": protocol["retention"]["allowed_persistence_manifest_sha256"],
        "hidden_lesson_reinjection_observed": False,
        "candidate_state_pre_delay_sha256": fake_sha("state-pre-delay"),
        "candidate_state_at_delayed_start_sha256": fake_sha("state-at-delayed-start"),
    }
    run["reported_gate_results"] = {key: "PASS" for key in run["reported_gate_results"]}
    run["external_verdict"] = {
        "status": "PASS",
        "evaluator_identity": protocol["actors"]["evaluator"]["identity"],
        "rubric_sha256": protocol["actors"]["evaluator"]["rubric_sha256"],
        "report_sha256": fake_sha("external-report"),
        "bound_to_candidate_output_hashes": True,
    }
    run["claims"] = ["POST_LESSON_FRESH_ITEM_PERFORMANCE_OBSERVED=YES"]
    return run


class ValidatorTests(unittest.TestCase):
    def test_shipped_templates_are_structurally_valid_but_unverified(self) -> None:
        protocol = load_template("protocol.template.json")
        run = load_template("run_bundle.template.json")
        report = VALIDATOR.Report()
        VALIDATOR.validate_structure(protocol, run, report)
        self.assertEqual([], report.errors)
        self.assertEqual("DRAFT", protocol["protocol_lock"]["status"])
        self.assertEqual("UNVERIFIED", run["reported_gate_results"]["full_slars"])

    def test_reused_item_id_is_rejected(self) -> None:
        protocol = load_template("protocol.template.json")
        run = load_template("run_bundle.template.json")
        duplicate_id = protocol["item_sets"][0]["items"][0]["item_id"]
        protocol["item_sets"][1]["items"][0]["item_id"] = duplicate_id
        report = VALIDATOR.Report()
        VALIDATOR.validate_structure(protocol, run, report)
        self.assertTrue(any(error.startswith("ITEM_ID_REUSED") for error in report.errors))

    def test_synthetic_complete_bundle_is_legacy_pass_not_slars_1_1_pass(self) -> None:
        protocol = build_synthetic_protocol()
        with tempfile.TemporaryDirectory() as directory:
            protocol_path = Path(directory) / "protocol.json"
            protocol_path.write_text(
                json.dumps(protocol, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            protocol_sha = VALIDATOR.file_sha256(protocol_path)
            run = build_synthetic_run(protocol, protocol_sha)
            report = VALIDATOR.Report()
            VALIDATOR.validate_structure(protocol, run, report)
            self.assertEqual([], report.errors)
            VALIDATOR.evaluate_evidence(protocol, run, protocol_sha, report)
            self.assertEqual([], report.errors)
            self.assertTrue(report.gates["FULL_SLARS"])
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                VALIDATOR.print_report("evidence", report)
            lines = stdout.getvalue().splitlines()
            self.assertIn("LEGACY_SLARS_1_0_CORE_PACKAGE_PASS=YES", lines)
            self.assertIn("SLARS_1_1_ZAI_INTEGRATION=NOT_EVALUATED", lines)
            self.assertIn("FULL_SLARS_1_1_PACKAGE_PASS=NO", lines)
            self.assertFalse(any(line.startswith("FULL_SLARS_PACKAGE_PASS=") for line in lines))
            self.assertFalse(any(line.startswith("FULL_SLARS=") for line in lines))

    def test_protocol_hash_tampering_breaks_a0(self) -> None:
        protocol = build_synthetic_protocol()
        run = build_synthetic_run(protocol, fake_sha("wrong-protocol"))
        report = VALIDATOR.Report()
        VALIDATOR.validate_structure(protocol, run, report)
        self.assertEqual([], report.errors)
        VALIDATOR.evaluate_evidence(protocol, run, fake_sha("actual-protocol"), report)
        self.assertFalse(report.gates["A0"])
        self.assertTrue(any(error.startswith("PROTOCOL_FILE_SHA_MISMATCH") for error in report.errors))


if __name__ == "__main__":
    unittest.main()
