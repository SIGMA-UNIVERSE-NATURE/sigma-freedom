import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("hka_autopilot.py")
spec = importlib.util.spec_from_file_location("hka_autopilot", MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class AutopilotTests(unittest.TestCase):
    def test_request_id_is_deterministic(self):
        validation = {"control_plane_sha": "abc"}
        first = mod.make_request("RUN_WORKER", "WORKER", "W1", "b1", ["x"], validation)
        second = mod.make_request("RUN_WORKER", "WORKER", "W1", "b1", ["x"], validation)
        self.assertEqual(first["request_id"], second["request_id"])
        self.assertTrue(first["guardrails"]["worker_cannot_self_accept"])

    def test_hold_does_not_dispatch_without_network(self):
        result = mod.dispatch({"request_id": "1", "action": "HOLD_LOCKED"})
        self.assertFalse(result["dispatched"])


if __name__ == "__main__":
    unittest.main()
