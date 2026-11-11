import unittest

from run import detect, make_orders


class IsolationForestTests(unittest.TestCase):
    def test_data_contains_expected_labeled_outliers(self):
        features, labels = make_orders(rows=50)
        self.assertEqual(features.shape, (53, 2))
        self.assertEqual(int(labels.sum()), 3)

    def test_detector_finds_synthetic_outliers(self):
        result = detect()
        self.assertGreaterEqual(result["true_positive"], 2)
        self.assertLessEqual(result["true_positive"], result["known_anomalies"])


if __name__ == "__main__":
    unittest.main()