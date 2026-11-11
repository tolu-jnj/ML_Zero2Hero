import unittest

from run import Evidence, gate_action, guard_response


class LocalGuardrailTests(unittest.TestCase):
    def setUp(self):
        self.evidence = [Evidence("DOC-1", "Synthetic evidence.", True)]

    def test_abstains_without_evidence(self):
        result = guard_response("An answer", [], self.evidence)
        self.assertEqual(result["status"], "abstain")

    def test_rejects_unknown_or_unauthorized_citations(self):
        unknown = guard_response("An answer", ["DOC-X"], self.evidence)
        restricted = guard_response(
            "An answer", ["SECRET"], [Evidence("SECRET", "Private.", False)]
        )
        self.assertEqual(unknown["status"], "reject")
        self.assertEqual(restricted["status"], "reject")

    def test_consequential_action_waits_for_approval(self):
        self.assertEqual(gate_action("change_order", False)["status"], "approval_required")
        self.assertEqual(gate_action("change_order", True)["status"], "approved")


if __name__ == "__main__":
    unittest.main()
