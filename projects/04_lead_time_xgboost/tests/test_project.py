import unittest

from run import make_orders, train_and_evaluate


class LeadTimeTests(unittest.TestCase):
    def test_synthetic_data_is_ordered_and_positive(self):
        features, target = make_orders(rows=100)
        self.assertEqual(features["created_day"].tolist(), list(range(100)))
        self.assertTrue((target > 0).all())

    def test_temporal_holdout_model_beats_mean_baseline(self):
        features, target = make_orders()
        split = int(len(features) * 0.8)
        baseline = abs(target[split:] - target[:split].mean()).mean()
        _, model_mae = train_and_evaluate()
        self.assertLess(model_mae, baseline)


if __name__ == "__main__":
    unittest.main()