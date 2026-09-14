# G5B Candidate Protocol

The learner input is `corpus/g5b_frozen_sandbox_learner_input_v1.jsonl`. It contains raw text, language tag, split, group id for training alignment, context, and provenance. It does not contain sealed held-out expected correspondences.

The evaluator input is `corpus/g5b_sealed_eval_v1.json`. It is used only after representation creation and replay.

Candidate requirements:

1. Learn from the training portion.
2. Persist one shared representation format for Vietnamese and English.
3. Replay from a fresh process.
4. Process held-out examples.
5. Show output changes when learner input is perturbed.
6. Preserve ambiguity and provenance.
7. Keep host cognition out of the answer path.

The sandbox may report only `PASS_IN_DEFINED_SANDBOX_SCOPE`. It must not claim general semantic understanding, human-language understanding, Vietnamese deep understanding, multilingual understanding, or G5 promotion.
