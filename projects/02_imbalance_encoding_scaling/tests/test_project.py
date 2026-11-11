import unittest

from run import make_data, train_and_evaluate


class ImbalancePipelineTests(unittest.TestCase):
    def test_synthetic_target_is_imbalanced(self):
        _, target = make_data(rows=500)
        self.assertGreater((target == 0).sum(), 5 * (target == 1).sum())

    def test_pipeline_returns_finite_score_and_preserves_heldout_classes(self):
        result = train_and_evaluate()
        self.assertGreaterEqual(result["balanced_accuracy"], 0.0)
        self.assertLessEqual(result["balanced_accuracy"], 1.0)
        self.assertEqual(len(result["class_counts"]), 2)


if __name__ == "__main__":
    unittest.main()