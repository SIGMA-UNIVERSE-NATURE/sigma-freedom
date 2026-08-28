from __future__ import annotations

import base64
import copy
import contextlib
import hashlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import zai_core as ZAI  # noqa: E402
import validate_zai_bundle as ZAI_CLI  # noqa: E402


ANSWER = "ORBITAL ANSWER 731"
FORBIDDEN_MATERIAL = [
    {
        "material_id": "supportor-answer",
        "class": "SUPPORTOR_ANSWER",
        "text": ANSWER,
    },
    {
        "material_id": "prewritten-answer",
        "class": "PREWRITTEN_ANSWER",
        "text": "FINAL TOKEN OMEGA 842",
    },
    {
        "material_id": "prewritten-hypothesis",
        "class": "PREWRITTEN_HYPOTHESIS",
        "text": "HYPOTHESIS BLUE SPIRAL 953",
    },
    {
        "material_id": "prewritten-reasoning",
        "class": "PREWRITTEN_REASONING_PATH",
        "text": "REASONING STEP DELTA 164",
    },
    {
        "material_id": "prewritten-conclusion",
        "class": "PREWRITTEN_CONCLUSION",
        "text": "CONCLUSION NORTH STAR 275",
    },
]

CLAIMS = [
    "SIGMA_SOURCE_LANGUAGE_BOUND_FOR_LOCKED_SOURCE",
    "REGISTERED_PREOUTPUT_INJECTION_SCAN_CLEAN",
    "DECLARED_SIGMAC_SIGMA_VM_EVENT_CHAIN_RAW_STDOUT_BOUND",
    "NO_DETECTED_PROHIBITED_ANSWER_INJECTION_WITHIN_DECLARED_MATERIALIZED_BOUNDARY",
]

ZERO_SHA256 = "0" * 64

CHANNELS = [
    "SOURCE",
    "BYTECODE",
    "STATE",
    "STDIN",
    "ARGV",
    "ENVIRONMENT",
    "FILES",
    "FILENAMES",
    "DIRECTORY_ORDER",
    "HOST_RESULTS",
    "TOOL_MAP",
    "TOOL_RESULTS",
    "NETWORK",
    "CLOCK",
    "RNG",
    "CACHE",
    "STDERR",
    "EXIT_CODE",
    "RESOURCE_LIMIT_SIGNAL",
]
CRITICAL_CHANNELS = {"SOURCE", "BYTECODE", "STDIN", "STDERR", "EXIT_CODE"}


def json_bytes(value: object) -> bytes:
    return ZAI.canonical_json_bytes(value)


def digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


class EvidenceFixture:
    """Create a fully materialized, internally bound ZAI evidence fixture."""

    def __init__(
        self,
        root: Path,
        *,
        source_suffix: str = "",
        blind_input_path: str = "artifacts/blind-input.txt",
        key_visible: bool = False,
        key_time_equals_output: bool = False,
        host_semantic_derivation: bool = False,
        output_rewrite: bool = False,
        role_collision: bool = False,
        task_status: str = "PASS",
    ) -> None:
        self.root = root
        self.run_id = "ZAI-UNIT-RUN-001"
        self.case_id = "ZAI-UNIT-CASE-001"
        self.roles = {
            "candidate_builder": "ROLE-CANDIDATE-BUILDER",
            "test_designer": "ROLE-TEST-DESIGNER",
            "key_custodian": "ROLE-KEY-CUSTODIAN",
            "runner": "ROLE-RUNNER",
            "evaluator": "ROLE-EVALUATOR",
            "auditor": "ROLE-AUDITOR",
        }
        if role_collision:
            self.roles["evaluator"] = self.roles["runner"]

        self.protocol = self._protocol()
        self.specs = self._artifact_specs(blind_input_path, key_visible)
        self.scan_surface = {
            artifact_id
            for artifact_id, spec in self.specs.items()
            if spec[5]
        }
        self.contents = self._artifact_contents(
            source_suffix=source_suffix,
            host_semantic_derivation=host_semantic_derivation,
            output_rewrite=output_rewrite,
            task_status=task_status,
        )
        self.run = self._run(
            key_time_equals_output=key_time_equals_output,
            host_semantic_derivation=host_semantic_derivation,
            output_rewrite=output_rewrite,
            task_status=task_status,
        )
        self._materialize()
        self._bind_protocol_and_run()

    def _protocol(self) -> dict[str, object]:
        return {
            "standard_version": "SLARS-1.1-ZAI",
            "artifact_status": "LOCKED_PROTOCOL",
            "protocol_id": "ZAI-UNIT-PROTOCOL-001",
            "profile": "SIGMA_LANGUAGE_ZERO_ANSWER_INJECTION",
            "locked_at_utc": "2026-08-28T00:00:00Z",
            "evidence_limits": {
                "relative_paths_only": True,
                "symlinks_allowed": False,
                "hardlinks_allowed": False,
                "max_artifacts": 64,
                "max_artifact_bytes": 1_048_576,
                "max_total_artifact_bytes": 16_777_216,
                "max_forbidden_material_items": 32,
                "max_forbidden_material_bytes_total": 1_048_576,
                "max_scan_product_bytes": 67_108_864,
            },
            "candidate": {
                "candidate_id": "SIGMA-ZAI-UNIT-CANDIDATE",
                "source_artifact_id": "candidate_source",
                "source_language_policy": "SIGMA_ONLY",
                "required_header_prefix": "#SIGMAUNIVERSE_LANGUAGE[",
                "frozen_at_utc": "2026-08-28T00:00:01Z",
                "provenance_class": "SUPPORTOR_AUTHORED_GENERIC_CANDIDATE",
                "human_language_as_sigma_cognition": "FORBIDDEN_UNTIL_PROVEN",
            },
            "roles": copy.deepcopy(self.roles),
            "blind_case": {
                "case_id": self.case_id,
                "input_artifact_id": "blind_input",
                "answer_key_artifact_id": "answer_key",
                "visibility_manifest_artifact_id": "visibility_manifest",
                "case_committed_at_utc": "2026-08-28T00:00:02Z",
                "case_created_after_candidate_freeze": True,
            },
            "runtime": {
                "sigmac_artifact_id": "sigmac_binary",
                "sigma_vm_artifact_id": "sigma_vm_binary",
                "runner_source_artifact_id": "runner_source",
                "host_trace_artifact_id": "host_trace",
                "raw_stdout_artifact_id": "raw_stdout",
                "raw_stderr_artifact_id": "raw_stderr",
                "native_chain_required": True,
                "host_semantic_transformation_allowed": False,
                "retry_policy": "SINGLE_ATTEMPT_NO_SELECTION",
                "max_attempts": 1,
            },
            "review": {
                "semantic_review_artifact_id": "semantic_review",
                "evaluation_rubric_artifact_id": "evaluation_rubric",
                "external_evaluation_artifact_id": "external_evaluation",
            },
            "committed_artifacts": {
                name: {"artifact_id": artifact_id, "sha256": ZERO_SHA256}
                for name, artifact_id in {
                    "candidate_source": "candidate_source",
                    "sigmac_binary": "sigmac_binary",
                    "sigma_vm_binary": "sigma_vm_binary",
                    "runner_source": "runner_source",
                    "evaluation_rubric": "evaluation_rubric",
                }.items()
            },
            "policy_locks": copy.deepcopy(ZAI.REQUIRED_POLICY_LOCKS),
            "claims_requested": list(CLAIMS),
        }

    @staticmethod
    def _artifact_specs(
        blind_input_path: str,
        key_visible: bool,
    ) -> dict[str, tuple[str, str, str, str, bool, bool]]:
        # relative_path, media_type, semantic_role, origin_role,
        # candidate_visible, pre_output_reachable
        return {
            "candidate_source": (
                "artifacts/candidate.sigma",
                "text/plain",
                "CANDIDATE_SOURCE",
                "CANDIDATE_BUILDER",
                False,
                True,
            ),
            "sigmac_binary": (
                "artifacts/sigmac",
                "application/octet-stream",
                "SIGMAC_BINARY",
                "RUNNER",
                False,
                True,
            ),
            "sigma_vm_binary": (
                "artifacts/sigma-vm",
                "application/octet-stream",
                "SIGMA_VM_BINARY",
                "RUNNER",
                False,
                True,
            ),
            "blind_input": (
                blind_input_path,
                "text/plain",
                "BLIND_INPUT",
                "TEST_DESIGNER",
                True,
                True,
            ),
            "answer_key": (
                "artifacts/answer-key.json",
                "application/json",
                "ANSWER_KEY",
                "KEY_CUSTODIAN",
                key_visible,
                key_visible,
            ),
            "evaluation_rubric": (
                "artifacts/evaluation-rubric.json",
                "application/json",
                "EVALUATION_RUBRIC",
                "TEST_DESIGNER",
                False,
                False,
            ),
            "visibility_manifest": (
                "artifacts/visibility.json",
                "application/json",
                "VISIBILITY_MANIFEST",
                "AUDITOR",
                False,
                True,
            ),
            "channel_evidence": (
                "artifacts/channel-evidence.json",
                "application/json",
                "CHANNEL_EVIDENCE",
                "AUDITOR",
                False,
                True,
            ),
            "runner_source": (
                "artifacts/runner.sh",
                "text/x-shellscript",
                "RUNNER_SOURCE",
                "RUNNER",
                False,
                True,
            ),
            "bytecode": (
                "artifacts/candidate.sigmab",
                "application/octet-stream",
                "RUN_SPECIFIC_BYTECODE",
                "SIGMAC",
                False,
                True,
            ),
            "host_trace": (
                "artifacts/host-trace.json",
                "application/json",
                "HOST_TRACE",
                "RUNNER",
                False,
                False,
            ),
            "raw_stdout": (
                "artifacts/raw.stdout",
                "application/octet-stream",
                "RAW_STDOUT",
                "SIGMA_VM",
                False,
                False,
            ),
            "raw_stderr": (
                "artifacts/raw.stderr",
                "application/octet-stream",
                "RAW_STDERR",
                "SIGMA_VM",
                False,
                False,
            ),
            "semantic_review": (
                "artifacts/semantic-review.json",
                "application/json",
                "SEMANTIC_REVIEW",
                "AUDITOR",
                False,
                False,
            ),
            "external_evaluation": (
                "artifacts/external-evaluation.json",
                "application/json",
                "EXTERNAL_EVALUATION",
                "EVALUATOR",
                False,
                False,
            ),
        }

    def _artifact_contents(
        self,
        *,
        source_suffix: str,
        host_semantic_derivation: bool,
        output_rewrite: bool,
        task_status: str,
    ) -> dict[str, bytes]:
        source = (
            "#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.ZAI.UNIT][VERSION=1.0]\n"
            "\n"
            "⟡(Σ.ZAI_UNIT) {\n"
            "    ⚡ INPUT_POLICY: \"UNSEEN\";\n"
            "}\n"
            + source_suffix
        ).encode("utf-8")
        answer_key = json_bytes(
            {
                "schema_version": "slars-zai-answer-key/v1",
                "case_id": self.case_id,
                "forbidden_material": FORBIDDEN_MATERIAL,
            }
        )
        evaluation_rubric = json_bytes(
            {
                "schema_version": "slars-zai-rubric/v1",
                "rubric_id": "ZAI-UNIT-EXACT-RUBRIC-001",
                "task_scoring": "EXACT_BOUND_OUTPUT",
            }
        )
        channel_captures = []
        for channel in sorted(set(CHANNELS) - CRITICAL_CHANNELS):
            observation = f"UNIT_DECLARED_CAPTURE:{channel}"
            observation_bytes = observation.encode("utf-8")
            channel_captures.append(
                {
                    "channel_id": channel,
                    "status": "CAPTURED",
                    "evidence_class": "DECLARED_CAPTURE_RECORD",
                    "observation_utf8": observation,
                    "observation_byte_count": len(observation_bytes),
                    "observation_sha256": digest(observation_bytes),
                }
            )
        channel_evidence = json_bytes(
            {
                "schema_version": "slars-zai-channel-evidence/v2",
                "run_id": self.run_id,
                "captures": channel_captures,
            }
        )
        visibility = json_bytes(
            {
                "schema_version": "slars-zai-visibility/v1",
                "case_id": self.case_id,
                "candidate_visible_artifact_ids": sorted(
                    artifact_id
                    for artifact_id, spec in self.specs.items()
                    if spec[4]
                ),
                "pre_output_reachable_artifact_ids": sorted(self.scan_surface),
                "candidate_forbidden_artifact_ids": [
                    "answer_key",
                    "evaluation_rubric",
                    "semantic_review",
                    "external_evaluation",
                ],
                "channels": [
                    {
                        "channel_id": channel,
                        "status": "CAPTURED",
                        "evidence_artifact_ids": [
                            {
                                "SOURCE": "candidate_source",
                                "BYTECODE": "bytecode",
                                "STDIN": "blind_input",
                                "STDERR": "raw_stderr",
                                "EXIT_CODE": "host_trace",
                            }.get(channel, "channel_evidence")
                        ],
                    }
                    for channel in CHANNELS
                ],
                "undeclared_readable_channels": [],
            }
        )
        host_trace = json_bytes(
            {
                "schema_version": "slars-zai-host-trace/v1",
                "run_id": self.run_id,
                "host_semantic_transformation_observed": host_semantic_derivation,
                "output_selection_or_rewrite_observed": output_rewrite,
                "operations": [
                    {
                        "sequence": 1,
                        "op": "HASH_BYTES",
                        "input_artifact_ids": ["candidate_source"],
                        "output_artifact_ids": [],
                    },
                    {
                        "sequence": 2,
                        "op": "EXEC_SIGMAC",
                        "input_artifact_ids": ["candidate_source", "sigmac_binary"],
                        "output_artifact_ids": ["bytecode"],
                    },
                    {
                        "sequence": 3,
                        "op": "EXEC_SIGMA_VM",
                        "input_artifact_ids": ["bytecode", "blind_input", "sigma_vm_binary"],
                        "output_artifact_ids": ["raw_stdout", "raw_stderr"],
                    },
                    {
                        "sequence": 4,
                        "op": "CAPTURE_STDOUT",
                        "input_artifact_ids": ["raw_stdout"],
                        "output_artifact_ids": [],
                    },
                    {
                        "sequence": 5,
                        "op": "CAPTURE_STDERR",
                        "input_artifact_ids": ["raw_stderr"],
                        "output_artifact_ids": [],
                    },
                    {
                        "sequence": 6,
                        "op": "FREEZE_BYTES",
                        "input_artifact_ids": ["raw_stdout", "raw_stderr"],
                        "output_artifact_ids": [],
                    },
                ],
            }
        )
        raw_stdout = (
            ANSWER.encode("utf-8") + b"\n"
            if task_status == "PASS"
            else b"CLEAN BUT WRONG OUTPUT\n"
        )
        contents = {
            "candidate_source": source,
            "sigmac_binary": b"\x7fELF SIGMAC UNIT FIXTURE\x00",
            "sigma_vm_binary": b"\x7fELF SIGMA VM UNIT FIXTURE\x00",
            "blind_input": b"17 23 29 35 41\n",
            "answer_key": answer_key,
            "evaluation_rubric": evaluation_rubric,
            "visibility_manifest": visibility,
            "channel_evidence": channel_evidence,
            "runner_source": b"#!/bin/sh\n# mechanical native-chain fixture\n",
            "bytecode": b"SIGMAB\x00UNIT-FIXTURE\x01",
            "host_trace": host_trace,
            "raw_stdout": raw_stdout,
            "raw_stderr": b"",
        }
        reviewed_artifacts = [
            {"artifact_id": artifact_id, "sha256": digest(contents[artifact_id])}
            for artifact_id in sorted(self.scan_surface)
        ]
        semantic_review = json_bytes(
            {
                "schema_version": "slars-zai-semantic-review/v2",
                "run_id": self.run_id,
                "reviewer_id": self.roles["auditor"],
                "status": "PASS",
                "reviewed_artifacts": reviewed_artifacts,
                "scan_surface_sha256": digest(json_bytes(reviewed_artifacts)),
                "findings": {
                    "supportor_answer_observed": False,
                    "prewritten_answer_observed": False,
                    "prewritten_hypothesis_observed": False,
                    "prewritten_reasoning_path_observed": False,
                    "prewritten_conclusion_observed": False,
                    "semantic_equivalent_injection_observed": False,
                    "host_semantic_transformation_observed": False,
                    "output_selection_or_rewrite_observed": False,
                    "unknown_readable_channel_observed": False,
                },
            }
        )
        external = json_bytes(
            {
                "schema_version": "slars-zai-external-evaluation/v1",
                "run_id": self.run_id,
                "evaluator_id": self.roles["evaluator"],
                "raw_stdout_sha256": digest(raw_stdout),
                "answer_key_sha256": digest(answer_key),
                "rubric_sha256": digest(evaluation_rubric),
                "status": task_status,
            }
        )
        contents["semantic_review"] = semantic_review
        contents["external_evaluation"] = external
        return contents

    def _run(
        self,
        *,
        key_time_equals_output: bool,
        host_semantic_derivation: bool,
        output_rewrite: bool,
        task_status: str,
    ) -> dict[str, object]:
        return {
            "standard_version": "SLARS-1.1-ZAI",
            "artifact_status": "RUN_EVIDENCE",
            "run_id": self.run_id,
            "run_status": "COMPLETE",
            "protocol_sha256": ZERO_SHA256,
            "artifacts": [],
            "events": self._events(key_time_equals_output),
            "execution": {
                "attempt_count": 1,
                "bytecode_artifact_id": "bytecode",
                "sigmac_rc": 0,
                "vm_rc": 0,
                "raw_stdout_artifact_id": "raw_stdout",
                "raw_stderr_artifact_id": "raw_stderr",
                "host_trace_artifact_id": "host_trace",
                "host_semantic_transformation_observed": host_semantic_derivation,
                "candidate_output_is_raw_vm_stdout": True,
                "output_selection_or_rewrite_observed": output_rewrite,
            },
            "scan": {
                "scan_surface_artifact_ids": sorted(self.scan_surface),
                "semantic_review_status": "PASS",
                "semantic_review_artifact_id": "semantic_review",
            },
            "external_evaluation": {
                "status": task_status,
                "evaluator_id": self.roles["evaluator"],
                "report_artifact_id": "external_evaluation",
                "bound_raw_stdout_sha256": digest(self.contents["raw_stdout"]),
                "bound_answer_key_sha256": digest(self.contents["answer_key"]),
                "bound_rubric_sha256": digest(self.contents["evaluation_rubric"]),
            },
            "claims": [
                {"claim_id": claim_id, "value": True}
                for claim_id in CLAIMS
            ],
            "reported_status": "PASS",
        }

    def _events(self, key_time_equals_output: bool) -> list[dict[str, object]]:
        event_specs = [
            (
                "PROTOCOL_FREEZE",
                self.roles["test_designer"],
                "2026-08-28T00:00:00Z",
                [],
                ["evaluation_rubric"],
                None,
                [],
                None,
            ),
            (
                "CANDIDATE_FREEZE",
                self.roles["candidate_builder"],
                "2026-08-28T00:00:01Z",
                [],
                ["candidate_source"],
                None,
                [],
                None,
            ),
            (
                "BLIND_CASE_COMMIT",
                self.roles["test_designer"],
                "2026-08-28T00:00:02Z",
                [],
                ["blind_input", "answer_key"],
                None,
                [],
                None,
            ),
            (
                "CHANNEL_SNAPSHOT",
                self.roles["auditor"],
                "2026-08-28T00:00:03Z",
                [],
                ["visibility_manifest", "channel_evidence"],
                None,
                [],
                None,
            ),
            (
                "RUN_START",
                self.roles["runner"],
                "2026-08-28T00:00:04Z",
                [
                    "candidate_source",
                    "blind_input",
                    "runner_source",
                    "sigmac_binary",
                    "sigma_vm_binary",
                ],
                [],
                None,
                [],
                None,
            ),
            (
                "SIGMAC_COMPLETE",
                self.roles["runner"],
                "2026-08-28T00:00:05Z",
                ["candidate_source"],
                ["bytecode"],
                "sigmac_binary",
                ["artifacts/candidate.sigma", "artifacts/candidate.sigmab"],
                0,
            ),
            (
                "VM_OUTPUT_FROZEN",
                self.roles["runner"],
                "2026-08-28T00:00:06Z",
                ["bytecode", "blind_input"],
                ["raw_stdout", "raw_stderr", "host_trace"],
                "sigma_vm_binary",
                ["artifacts/candidate.sigmab"],
                0,
            ),
            (
                "KEY_FIRST_ACCESS",
                self.roles["key_custodian"],
                (
                    "2026-08-28T00:00:06Z"
                    if key_time_equals_output
                    else "2026-08-28T00:00:07Z"
                ),
                ["answer_key"],
                [],
                None,
                [],
                None,
            ),
            (
                "SEMANTIC_REVIEW",
                self.roles["auditor"],
                "2026-08-28T00:00:08Z",
                sorted(self.scan_surface | {"answer_key", "raw_stdout"}),
                ["semantic_review"],
                None,
                [],
                None,
            ),
            (
                "EXTERNAL_EVALUATION",
                self.roles["evaluator"],
                "2026-08-28T00:00:09Z",
                ["answer_key", "evaluation_rubric", "raw_stdout"],
                ["external_evaluation"],
                None,
                [],
                None,
            ),
        ]
        events = []
        for sequence, spec in enumerate(event_specs, start=1):
            event_type, actor, occurred, inputs, outputs, process, argv, rc = spec
            events.append(
                {
                    "sequence": sequence,
                    "run_id": self.run_id,
                    "event_type": event_type,
                    "actor_id": actor,
                    "occurred_at_utc": occurred,
                    "input_artifact_ids": inputs,
                    "output_artifact_ids": outputs,
                    "process_artifact_id": process,
                    "argv": argv,
                    "rc": rc,
                    "artifact_bindings_sha256": ZERO_SHA256,
                    "previous_event_sha256": None,
                    "event_sha256": ZERO_SHA256,
                }
            )
            events[-1]["artifact_bindings_sha256"] = self._event_binding_hash(events[-1])
        self.rehash_events(events)
        return events

    def _event_binding_hash(self, event: dict[str, object]) -> str:
        bindings: list[dict[str, object]] = []
        for direction, key in (("INPUT", "input_artifact_ids"), ("OUTPUT", "output_artifact_ids")):
            for artifact_id in event[key]:
                data = self.contents[artifact_id]
                bindings.append(
                    {
                        "direction": direction,
                        "artifact_id": artifact_id,
                        "sha256": digest(data),
                        "byte_count": len(data),
                    }
                )
        process_id = event["process_artifact_id"]
        if process_id is not None:
            data = self.contents[process_id]
            bindings.append(
                {
                    "direction": "PROCESS",
                    "artifact_id": process_id,
                    "sha256": digest(data),
                    "byte_count": len(data),
                }
            )
        bindings.sort(key=lambda item: (item["direction"], item["artifact_id"]))
        return digest(json_bytes(bindings))

    @staticmethod
    def rehash_events(events: list[dict[str, object]]) -> None:
        previous = None
        for event in events:
            event["previous_event_sha256"] = previous
            value = dict(event)
            value.pop("event_sha256", None)
            event["event_sha256"] = digest(json_bytes(value))
            previous = event["event_sha256"]

    def _materialize(self) -> None:
        records = []
        for artifact_id, spec in self.specs.items():
            relative_path, media_type, semantic_role, origin_role, visible, reachable = spec
            data = self.contents[artifact_id]
            path = self.root.joinpath(*relative_path.split("/"))
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
            records.append(
                {
                    "artifact_id": artifact_id,
                    "relative_path": relative_path,
                    "media_type": media_type,
                    "semantic_role": semantic_role,
                    "origin_role": origin_role,
                    "stage": {
                        "ANSWER_KEY": "POST_OUTPUT_KEY",
                        "HOST_TRACE": "OUTPUT",
                        "RAW_STDOUT": "OUTPUT",
                        "RAW_STDERR": "OUTPUT",
                        "SEMANTIC_REVIEW": "EVALUATION",
                        "EXTERNAL_EVALUATION": "EVALUATION",
                    }.get(
                        semantic_role,
                        "PRE_FREEZE"
                        if semantic_role in {
                            "CANDIDATE_SOURCE",
                            "SIGMAC_BINARY",
                            "SIGMA_VM_BINARY",
                            "RUNNER_SOURCE",
                            "EVALUATION_RUBRIC",
                        }
                        else "PRE_OUTPUT",
                    ),
                    "candidate_visible": visible,
                    "pre_output_reachable": reachable,
                    "byte_count": len(data),
                    "sha256": digest(data),
                }
            )
        self.run["artifacts"] = records

    def _bind_protocol_and_run(self) -> None:
        records = {record["artifact_id"]: record for record in self.run["artifacts"]}
        for commitment in self.protocol["committed_artifacts"].values():
            commitment["sha256"] = records[commitment["artifact_id"]]["sha256"]
        self.run["protocol_sha256"] = digest(json_bytes(self.protocol))

    def record(self, artifact_id: str) -> dict[str, object]:
        return next(
            record
            for record in self.run["artifacts"]
            if record["artifact_id"] == artifact_id
        )

    def replace_artifact(self, artifact_id: str, data: bytes) -> None:
        record = self.record(artifact_id)
        path = self.root.joinpath(*record["relative_path"].split("/"))
        path.write_bytes(data)
        record["byte_count"] = len(data)
        record["sha256"] = digest(data)
        self.contents[artifact_id] = data
        for commitment in self.protocol["committed_artifacts"].values():
            if commitment["artifact_id"] == artifact_id:
                commitment["sha256"] = record["sha256"]
        self.run["protocol_sha256"] = digest(json_bytes(self.protocol))

    def rebind_event_artifacts_and_rehash(self) -> None:
        for event in self.run["events"]:
            event["artifact_bindings_sha256"] = self._event_binding_hash(event)
        self.rehash_events(self.run["events"])

    def refresh_semantic_review_bindings(self) -> None:
        review = json.loads(self.contents["semantic_review"])
        reviewed_artifacts = [
            {"artifact_id": artifact_id, "sha256": digest(self.contents[artifact_id])}
            for artifact_id in sorted(self.scan_surface)
        ]
        review["reviewed_artifacts"] = reviewed_artifacts
        review["scan_surface_sha256"] = digest(json_bytes(reviewed_artifacts))
        self.replace_artifact("semantic_review", json_bytes(review))


class ZAIValidatorMutationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.protocol_schema = ZAI.load_json_file(
            ROOT / "schemas" / "zai_protocol.schema.json",
            "zai_protocol_schema",
        )
        cls.run_schema = ZAI.load_json_file(
            ROOT / "schemas" / "zai_run_bundle.schema.json",
            "zai_run_schema",
        )

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="slars-zai-test-")
        self.evidence_root = Path(self.temporary.name)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def evaluate(self, fixture: EvidenceFixture) -> ZAI.Report:
        report = ZAI.Report()
        self.assertTrue(
            ZAI.strict_schema_check(
                fixture.protocol,
                self.protocol_schema,
                report,
                "protocol",
            ),
            report.errors,
        )
        self.assertTrue(
            ZAI.strict_schema_check(
                fixture.run,
                self.run_schema,
                report,
                "run",
            ),
            report.errors,
        )
        ZAI.evaluate_evidence(
            fixture.protocol,
            fixture.run,
            json_bytes(fixture.protocol),
            fixture.root,
            report,
        )
        return report

    def assert_invalid_with(self, report: ZAI.Report, code: str) -> None:
        self.assertEqual("INVALID", report.status, report.errors)
        self.assertIn(code, {item[1] for item in report.errors}, report.errors)
        self.assertNotEqual("PASS", report.gates.get("ZAI"), report.gates)

    def test_clean_materialized_bundle_passes(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        report = self.evaluate(fixture)
        self.assertEqual([], report.errors)
        self.assertEqual("PASS", report.gates["ZAI"])
        self.assertEqual("PASS", report.task_outcome)
        self.assertEqual([], report.scan_matches)

    def test_clean_task_failure_remains_zai_pass(self) -> None:
        fixture = EvidenceFixture(self.evidence_root, task_status="FAIL")
        report = self.evaluate(fixture)
        self.assertEqual([], report.errors)
        self.assertEqual("PASS", report.gates["ZAI"])
        self.assertEqual("FAIL", report.task_outcome)

    def test_exact_answer_leak_is_invalid(self) -> None:
        fixture = EvidenceFixture(self.evidence_root, source_suffix=f'\n⚡ LEAK: "{ANSWER}";\n')
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "FORBIDDEN_MATERIAL_MATCH")
        self.assertTrue(any(item["mode"] == "EXACT_UTF8" for item in report.scan_matches))

    def test_normalized_unicode_answer_leak_is_invalid(self) -> None:
        leak = "ＯＲＢＩＴＡＬ\n   answer  731"
        fixture = EvidenceFixture(self.evidence_root, source_suffix=f'\n⚡ LEAK: "{leak}";\n')
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "FORBIDDEN_MATERIAL_MATCH")
        self.assertTrue(
            any(
                item["mode"] == "UNICODE_NFKC_CASEFOLD_WHITESPACE_COLLAPSE"
                for item in report.scan_matches
            )
        )

    def test_base64_answer_leak_is_invalid(self) -> None:
        leak = base64.b64encode(ANSWER.encode("utf-8")).decode("ascii")
        fixture = EvidenceFixture(self.evidence_root, source_suffix=f'\n⚡ LEAK: "{leak}";\n')
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "FORBIDDEN_MATERIAL_MATCH")
        self.assertTrue(any(item["mode"] == "BASE64_STANDARD" for item in report.scan_matches))

    def test_hex_answer_leak_is_invalid(self) -> None:
        leak = ANSWER.encode("utf-8").hex()
        fixture = EvidenceFixture(self.evidence_root, source_suffix=f'\n⚡ LEAK: "{leak}";\n')
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "FORBIDDEN_MATERIAL_MATCH")
        self.assertTrue(any(item["mode"] == "HEX_LOWER" for item in report.scan_matches))

    def test_filename_answer_leak_is_invalid(self) -> None:
        fixture = EvidenceFixture(
            self.evidence_root,
            blind_input_path=f"artifacts/{ANSWER}.txt",
        )
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "FORBIDDEN_MATERIAL_MATCH")
        self.assertTrue(
            any(item["artifact_id"] == "blind_input" for item in report.scan_matches)
        )

    def test_key_visibility_is_invalid(self) -> None:
        fixture = EvidenceFixture(self.evidence_root, key_visible=True)
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "FORBIDDEN_ARTIFACT_REACHABLE")

    def test_key_must_open_strictly_after_output_freeze(self) -> None:
        fixture = EvidenceFixture(self.evidence_root, key_time_equals_output=True)
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "OUTPUT_KEY_EVALUATION_ORDER_INVALID")

    def test_host_semantic_derivation_is_invalid(self) -> None:
        fixture = EvidenceFixture(self.evidence_root, host_semantic_derivation=True)
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "HOST_SEMANTIC_TRANSFORMATION_DETECTED")

    def test_output_rewrite_or_selection_is_invalid(self) -> None:
        fixture = EvidenceFixture(self.evidence_root, output_rewrite=True)
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "OUTPUT_SELECTION_OR_REWRITE_DETECTED")

    def test_role_collision_is_invalid(self) -> None:
        fixture = EvidenceFixture(self.evidence_root, role_collision=True)
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "ROLE_COLLISION")

    def test_path_traversal_is_invalid(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.record("blind_input")["relative_path"] = "../blind-input.txt"
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "UNSAFE_RELATIVE_PATH")

    def test_control_character_path_is_invalid_without_report_injection(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.record("blind_input")["relative_path"] = "artifacts/bad\nERROR=FAKE"
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "UNSAFE_RELATIVE_PATH")
        self.assertTrue(all("\n" not in detail for _, _, detail in report.errors))

    def test_materialized_hash_mismatch_is_invalid(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.record("blind_input")["sha256"] = "f" * 64
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "ARTIFACT_SHA256_MISMATCH")

    def test_event_hash_chain_tampering_is_invalid(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.run["events"][5]["event_sha256"] = "e" * 64
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "EVENT_HASH_MISMATCH")

    def test_event_order_mutation_is_invalid(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.run["events"][6], fixture.run["events"][7] = (
            fixture.run["events"][7],
            fixture.run["events"][6],
        )
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "REQUIRED_EVENT_ORDER_MISMATCH")

    def test_event_run_id_replay_is_invalid(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.run["events"][4]["run_id"] = "REPLAYED-RUN-ID"
        EvidenceFixture.rehash_events(fixture.run["events"])
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "EVENT_RUN_ID_MISMATCH")

    def test_vm_argv_binding_failure_is_invalid(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.run["events"][6]["argv"] = ["artifacts/not-the-frozen-bytecode.sigmab"]
        EvidenceFixture.rehash_events(fixture.run["events"])
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "VM_ARGV_BINDING_FAIL")

    def test_external_output_hash_binding_failure_is_invalid(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.run["external_evaluation"]["bound_raw_stdout_sha256"] = "d" * 64
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "RUN_EXTERNAL_HASH_BINDING_MISMATCH")

    def test_external_rubric_hash_binding_failure_is_invalid(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.run["external_evaluation"]["bound_rubric_sha256"] = "c" * 64
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "RUN_EXTERNAL_HASH_BINDING_MISMATCH")

    def test_host_trace_cannot_read_answer_key(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        trace = json.loads(fixture.contents["host_trace"])
        trace["operations"].append(
            {
                "sequence": len(trace["operations"]) + 1,
                "op": "READ_BYTES",
                "input_artifact_ids": ["answer_key"],
                "output_artifact_ids": [],
            }
        )
        fixture.replace_artifact("host_trace", json_bytes(trace))
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "HOST_TRACE_REFERENCES_POSTOUTPUT_SECRET")

    def test_host_trace_cannot_rewrite_raw_stdout_with_flags_false(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        trace = json.loads(fixture.contents["host_trace"])
        trace["operations"].append(
            {
                "sequence": len(trace["operations"]) + 1,
                "op": "WRITE_BYTES",
                "input_artifact_ids": ["blind_input"],
                "output_artifact_ids": ["raw_stdout"],
            }
        )
        fixture.replace_artifact("host_trace", json_bytes(trace))
        report = self.evaluate(fixture)
        self.assertEqual("INVALID", report.status, report.errors)
        self.assertNotEqual("PASS", report.gates.get("ZAI"), report.gates)

    def test_host_trace_cannot_hide_second_vm_execution(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        trace = json.loads(fixture.contents["host_trace"])
        duplicate = copy.deepcopy(
            next(item for item in trace["operations"] if item["op"] == "EXEC_SIGMA_VM")
        )
        duplicate["sequence"] = len(trace["operations"]) + 1
        trace["operations"].append(duplicate)
        fixture.replace_artifact("host_trace", json_bytes(trace))
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "HOST_OPERATION_CARDINALITY_INVALID")

    def test_host_vm_operation_rejects_extra_raw_stdout_input(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        trace = json.loads(fixture.contents["host_trace"])
        vm_operation = next(
            item for item in trace["operations"] if item["op"] == "EXEC_SIGMA_VM"
        )
        vm_operation["input_artifact_ids"].append("raw_stdout")
        fixture.replace_artifact("host_trace", json_bytes(trace))
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "HOST_OPERATION_TOPOLOGY_MISMATCH")

    def test_prekey_vm_argv_cannot_reference_answer_key_path(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.run["events"][6]["argv"].append(
            fixture.record("answer_key")["relative_path"]
        )
        EvidenceFixture.rehash_events(fixture.run["events"])
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "POSTOUTPUT_SECRET_IN_PREKEY_ARGV")

    def test_prekey_vm_argv_cannot_decorate_answer_key_path(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.run["events"][6]["argv"].append(
            "--key=" + fixture.record("answer_key")["relative_path"]
        )
        EvidenceFixture.rehash_events(fixture.run["events"])
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "POSTOUTPUT_SECRET_IN_PREKEY_ARGV")

    def test_prekey_vm_argv_is_scanned_for_answer_material(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.run["events"][6]["argv"].append(ANSWER)
        EvidenceFixture.rehash_events(fixture.run["events"])
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "FORBIDDEN_MATERIAL_MATCH")

    def test_vm_event_must_bind_blind_input(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.run["events"][6]["input_artifact_ids"].remove("blind_input")
        EvidenceFixture.rehash_events(fixture.run["events"])
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "EVENT_REQUIRED_INPUT_MISSING")

    def test_vm_event_rejects_extra_raw_stdout_input(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.run["events"][6]["input_artifact_ids"].append("raw_stdout")
        EvidenceFixture.rehash_events(fixture.run["events"])
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "EVENT_INPUT_SET_MISMATCH")

    def test_vm_event_rejects_extra_semantic_review_input(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.run["events"][6]["input_artifact_ids"].append("semantic_review")
        EvidenceFixture.rehash_events(fixture.run["events"])
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "EVENT_INPUT_SET_MISMATCH")

    def test_disabled_channel_requires_disable_evidence(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        visibility = json.loads(fixture.contents["visibility_manifest"])
        channel = next(
            item for item in visibility["channels"] if item["channel_id"] == "NETWORK"
        )
        channel["status"] = "DISABLED"
        channel["evidence_artifact_ids"] = []
        fixture.replace_artifact("visibility_manifest", json_bytes(visibility))
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "CHANNEL_STATUS_WITHOUT_EVIDENCE")

    def test_empty_channel_evidence_cannot_cover_declared_channels(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        empty = json_bytes(
            {
                "schema_version": "slars-zai-channel-evidence/v2",
                "run_id": fixture.run_id,
                "captures": [],
            }
        )
        fixture.replace_artifact("channel_evidence", empty)
        fixture.refresh_semantic_review_bindings()
        fixture.rebind_event_artifacts_and_rehash()
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "CHANNEL_CAPTURE_SET_INVALID")

    def test_disabled_channel_requires_matching_materialized_record(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        visibility = json.loads(fixture.contents["visibility_manifest"])
        channel = next(item for item in visibility["channels"] if item["channel_id"] == "NETWORK")
        channel["status"] = "DISABLED"
        evidence = json.loads(fixture.contents["channel_evidence"])
        capture = next(item for item in evidence["captures"] if item["channel_id"] == "NETWORK")
        observation = "UNIT_DECLARED_DISABLEMENT_RECORD:NETWORK"
        capture.update(
            {
                "status": "DISABLED",
                "evidence_class": "DECLARED_DISABLEMENT_RECORD",
                "observation_utf8": observation,
                "observation_byte_count": len(observation.encode("utf-8")),
                "observation_sha256": digest(observation.encode("utf-8")),
            }
        )
        fixture.replace_artifact("visibility_manifest", json_bytes(visibility))
        fixture.replace_artifact("channel_evidence", json_bytes(evidence))
        fixture.refresh_semantic_review_bindings()
        fixture.rebind_event_artifacts_and_rehash()
        report = self.evaluate(fixture)
        self.assertEqual("PASS", report.gates["ZAI"], report.errors)

    def test_malformed_internal_visibility_json_is_invalid_not_a_crash(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        visibility = json.loads(fixture.contents["visibility_manifest"])
        visibility["channels"][0]["channel_id"] = []
        fixture.replace_artifact("visibility_manifest", json_bytes(visibility))
        try:
            report = self.evaluate(fixture)
        except Exception as exc:  # pragma: no cover - assertion documents fail-closed contract
            self.fail(f"validator crashed on malformed internal JSON: {exc!r}")
        self.assert_invalid_with(report, "CHANNEL_ID_INVALID")

    def test_malformed_internal_answer_key_is_invalid_not_a_crash(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        answer_key = json.loads(fixture.contents["answer_key"])
        answer_key["forbidden_material"][0]["class"] = []
        fixture.replace_artifact("answer_key", json_bytes(answer_key))
        try:
            report = self.evaluate(fixture)
        except Exception as exc:  # pragma: no cover - assertion documents fail-closed contract
            self.fail(f"validator crashed on malformed answer key: {exc!r}")
        self.assert_invalid_with(report, "MATERIAL_CLASS_INVALID")

    def test_duplicate_json_key_is_rejected_before_schema_or_evidence(self) -> None:
        duplicate = (
            b'{"standard_version":"SLARS-1.1-ZAI",'
            b'"standard_version":"MUTATED"}'
        )
        with self.assertRaisesRegex(ZAI.StrictJSONError, "duplicate JSON key"):
            ZAI.parse_json_bytes(duplicate, "duplicate-run")

    def test_bool_is_not_accepted_as_json_schema_integer(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.run["execution"]["sigmac_rc"] = True
        report = ZAI.Report()
        self.assertFalse(
            ZAI.strict_schema_check(
                fixture.run,
                self.run_schema,
                report,
                "run",
            )
        )
        self.assertIn("SCHEMA_VIOLATION", {item[1] for item in report.errors})

    def test_unpaired_surrogate_json_is_rejected_without_crash(self) -> None:
        malformed = b'{"value":"\\ud800"}'
        with self.assertRaisesRegex(ZAI.StrictJSONError, "unpaired surrogate"):
            ZAI.parse_json_bytes(malformed, "surrogate-run")

    def test_oversized_and_nonfinite_json_numbers_are_rejected(self) -> None:
        with self.assertRaises(ZAI.StrictJSONError):
            ZAI.parse_json_bytes(b'{"value":' + b"9" * 5000 + b"}", "huge-int")
        with self.assertRaisesRegex(ZAI.StrictJSONError, "non-finite"):
            ZAI.parse_json_bytes(b'{"value":1e400}', "infinite-float")

    def test_protocol_max_artifacts_cannot_be_below_required_roles(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.protocol["evidence_limits"]["max_artifacts"] = 14
        report = ZAI.Report()
        self.assertFalse(
            ZAI.strict_schema_check(fixture.protocol, self.protocol_schema, report, "protocol")
        )

    def test_total_artifact_bytes_limit_is_enforced(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.protocol["evidence_limits"]["max_total_artifact_bytes"] = 15
        fixture.run["protocol_sha256"] = digest(json_bytes(fixture.protocol))
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "TOTAL_ARTIFACT_BYTES_LIMIT_EXCEEDED")

    def test_forbidden_material_count_limit_is_enforced(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.protocol["evidence_limits"]["max_forbidden_material_items"] = 5
        answer_key = json.loads(fixture.contents["answer_key"])
        answer_key["forbidden_material"].append(
            {
                "material_id": "extra-supportor-answer",
                "class": "SUPPORTOR_ANSWER",
                "text": "EXTRA DISTINCTIVE MATERIAL 4862",
            }
        )
        fixture.replace_artifact("answer_key", json_bytes(answer_key))
        fixture.rebind_event_artifacts_and_rehash()
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "FORBIDDEN_MATERIAL_COUNT_LIMIT_EXCEEDED")

    def test_scan_product_limit_is_enforced(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.protocol["evidence_limits"]["max_scan_product_bytes"] = 1
        fixture.run["protocol_sha256"] = digest(json_bytes(fixture.protocol))
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "SCAN_PRODUCT_LIMIT_EXCEEDED")

    def test_invalid_utf8_sigmac_binary_does_not_disable_normalized_scan(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.replace_artifact("sigmac_binary", b"\xffPREFIX orbital\t answer 731")
        fixture.rebind_event_artifacts_and_rehash()
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "FORBIDDEN_MATERIAL_MATCH")
        self.assertTrue(
            any(
                item["artifact_id"] == "sigmac_binary"
                and "ASCII_BYTE" in item["mode"]
                for item in report.scan_matches
            )
        )

    def test_invalid_utf8_bytecode_does_not_disable_normalized_scan(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.replace_artifact("bytecode", b"\xffPREFIX orbital\t answer 731")
        fixture.rebind_event_artifacts_and_rehash()
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "FORBIDDEN_MATERIAL_MATCH")
        self.assertTrue(
            any(
                item["artifact_id"] == "bytecode" and "ASCII_BYTE" in item["mode"]
                for item in report.scan_matches
            )
        )

    def test_fully_percent_encoded_answer_is_detected(self) -> None:
        encoded = "".join(f"%{byte:02x}" for byte in ANSWER.encode("utf-8"))
        fixture = EvidenceFixture(self.evidence_root, source_suffix="\n" + encoded + "\n")
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "FORBIDDEN_MATERIAL_MATCH")
        self.assertTrue(any("URL_PERCENT" in item["mode"] for item in report.scan_matches))

    def test_fully_json_unicode_escaped_answer_is_detected(self) -> None:
        encoded = "".join(f"\\u{ord(character):04x}" for character in ANSWER)
        fixture = EvidenceFixture(self.evidence_root, source_suffix="\n" + encoded + "\n")
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "FORBIDDEN_MATERIAL_MATCH")
        self.assertTrue(
            any("JSON_UNICODE_ESCAPE" in item["mode"] for item in report.scan_matches)
        )

    def test_normalized_forbidden_material_fingerprint_collision_is_rejected(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        answer_key = json.loads(fixture.contents["answer_key"])
        answer_key["forbidden_material"][1]["text"] = "ＯＲＢＩＴＡＬ   ANSWER 731"
        fixture.replace_artifact("answer_key", json_bytes(answer_key))
        fixture.rebind_event_artifacts_and_rehash()
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "MATERIAL_NORMALIZED_FINGERPRINT_COLLISION")

    def test_semantic_review_event_must_receive_full_scan_surface(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        event = fixture.run["events"][8]
        event["input_artifact_ids"].remove("candidate_source")
        event["artifact_bindings_sha256"] = fixture._event_binding_hash(event)
        fixture.rehash_events(fixture.run["events"])
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "EVENT_REQUIRED_INPUT_MISSING")

    def test_semantic_review_binds_each_reviewed_artifact_hash(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        review = json.loads(fixture.contents["semantic_review"])
        review["reviewed_artifacts"][0]["sha256"] = "f" * 64
        review["scan_surface_sha256"] = digest(json_bytes(review["reviewed_artifacts"]))
        fixture.replace_artifact("semantic_review", json_bytes(review))
        fixture.rebind_event_artifacts_and_rehash()
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "SEMANTIC_REVIEW_SURFACE_OR_HASH_MISMATCH")

    def test_event_hash_chain_binds_referenced_artifact_bytes(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.replace_artifact("raw_stdout", b"MUTATED AFTER EVENT FREEZE\n")
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "EVENT_ARTIFACT_BINDINGS_MISMATCH")

    def test_forbidden_manifest_set_cannot_overlap_any_preoutput_artifact(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        visibility = json.loads(fixture.contents["visibility_manifest"])
        visibility["candidate_forbidden_artifact_ids"].append("bytecode")
        fixture.replace_artifact("visibility_manifest", json_bytes(visibility))
        fixture.rebind_event_artifacts_and_rehash()
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "FORBIDDEN_ARTIFACT_REACHABLE")

    def test_canonical_artifact_origin_and_stage_are_enforced(self) -> None:
        for field, value in (("origin_role", "EVALUATOR"), ("stage", "OUTPUT")):
            with self.subTest(field=field):
                subroot = self.evidence_root / field
                subroot.mkdir()
                fixture = EvidenceFixture(subroot)
                fixture.record("candidate_source")[field] = value
                report = self.evaluate(fixture)
                self.assert_invalid_with(report, "ARTIFACT_METADATA_MISMATCH")

    def test_protocol_freeze_timestamp_is_exactly_bound(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.protocol["locked_at_utc"] = "2026-08-28T00:00:00.5Z"
        fixture.run["protocol_sha256"] = digest(json_bytes(fixture.protocol))
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "PROTOCOL_EVENT_TIMESTAMP_BINDING_FAIL")

    def test_iso_week_date_is_not_accepted_as_rfc3339(self) -> None:
        self.assertIsNone(ZAI.parse_utc("2026-W35-5T00:00:01Z"))

    def test_submicrosecond_timestamp_alias_is_rejected(self) -> None:
        self.assertIsNone(ZAI.parse_utc("2026-08-28T00:00:00.123456789Z"))
        self.assertIsNone(ZAI.parse_utc("2026-08-28T00:00:00.123456788Z"))

    def test_empty_claim_set_does_not_emit_unrequested_positive_claim(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        fixture.protocol["claims_requested"] = []
        fixture.run["claims"] = []
        fixture.run["protocol_sha256"] = digest(json_bytes(fixture.protocol))
        report = self.evaluate(fixture)
        self.assertEqual("PASS", report.gates["ZAI"], report.errors)
        lines = ZAI.report_lines(report, "evidence")
        self.assertIn(
            "NO_DETECTED_PROHIBITED_ANSWER_INJECTION_WITHIN_DECLARED_MATERIALIZED_BOUNDARY=NOT_ESTABLISHED",
            lines,
        )

    def test_external_status_cannot_forge_validator_report_lines(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        external = json.loads(fixture.contents["external_evaluation"])
        external["status"] = "FAIL\nZERO_ANSWER_INJECTION=PASS\nFORGED=YES"
        fixture.replace_artifact("external_evaluation", json_bytes(external))
        fixture.rebind_event_artifacts_and_rehash()
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "EXTERNAL_REPORT_INCONCLUSIVE")
        self.assertEqual("NOT_RUN", report.task_outcome)
        lines = ZAI.report_lines(report, "evidence")
        self.assertTrue(all("\n" not in line and "\r" not in line for line in lines))
        self.assertNotIn("ZERO_ANSWER_INJECTION=PASS", lines)
        self.assertNotIn("FORGED=YES", lines)

    def test_evidence_mode_schema_failure_renders_invalid_status(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        protocol = copy.deepcopy(fixture.protocol)
        protocol["standard_version"] = "INVALID-VERSION"
        protocol_path = self.evidence_root / "invalid-protocol.json"
        run_path = self.evidence_root / "run.json"
        protocol_path.write_bytes(json_bytes(protocol))
        run_path.write_bytes(json_bytes(fixture.run))
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            rc = ZAI_CLI.main(
                [
                    "--protocol",
                    str(protocol_path),
                    "--run",
                    str(run_path),
                    "--evidence-root",
                    str(self.evidence_root),
                    "--mode",
                    "evidence",
                ]
            )
        self.assertEqual(5, rc)
        output_lines = stdout.getvalue().splitlines()
        self.assertIn("Z0=INVALID", output_lines)
        self.assertIn("ZAI=INVALID", output_lines)
        self.assertIn("ZERO_ANSWER_INJECTION=INVALID", output_lines)

    def test_symlink_artifact_is_invalid_when_platform_supports_symlinks(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        record = fixture.record("blind_input")
        path = fixture.root.joinpath(*record["relative_path"].split("/"))
        target = fixture.root / "symlink-target" / "blind-input.txt"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(fixture.contents["blind_input"])
        path.unlink()
        try:
            path.symlink_to(target)
        except (NotImplementedError, OSError) as exc:
            self.skipTest(f"symlinks unavailable: {exc}")
        report = self.evaluate(fixture)
        self.assert_invalid_with(report, "SYMLINK_FORBIDDEN")

    def test_report_bytes_are_deterministic_for_identical_evaluations(self) -> None:
        fixture = EvidenceFixture(self.evidence_root)
        first = self.evaluate(fixture)
        second = self.evaluate(fixture)
        first_bytes = ("\n".join(ZAI.report_lines(first, "evidence")) + "\n").encode("utf-8")
        second_bytes = ("\n".join(ZAI.report_lines(second, "evidence")) + "\n").encode("utf-8")
        self.assertEqual(first_bytes, second_bytes)

    def test_package_manifest_has_exact_distribution_coverage(self) -> None:
        manifest = (ROOT / "MANIFEST.sha256").read_bytes()
        report = ZAI.Report()
        self.assertTrue(ZAI.verify_package_manifest(ROOT, manifest, report), report.errors)

    def test_package_manifest_hash_mutation_is_rejected(self) -> None:
        manifest = (ROOT / "MANIFEST.sha256").read_bytes()
        first = manifest[:1]
        replacement = b"0" if first != b"0" else b"1"
        mutated = replacement + manifest[1:]
        report = ZAI.Report()
        self.assertFalse(ZAI.verify_package_manifest(ROOT, mutated, report))
        self.assertIn("PACKAGE_FILE_SHA256_MISMATCH", {item[1] for item in report.errors})


if __name__ == "__main__":
    unittest.main()
