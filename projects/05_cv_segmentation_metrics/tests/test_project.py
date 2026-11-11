import unittest

import numpy as np

from run import make_masks, segmentation_metrics


class SegmentationMetricTests(unittest.TestCase):
    def test_perfect_prediction_scores_one(self):
        truth, _ = make_masks()
        result = segmentation_metrics(truth, truth.copy(), num_classes=2)
        self.assertAlmostEqual(result["pixel_accuracy"], 1.0)
        self.assertAlmostEqual(result["mean_iou"], 1.0)

    def test_overlap_metrics_decrease_for_shifted_mask(self):
        truth, prediction = make_masks()
        result = segmentation_metrics(truth, prediction, num_classes=2)
        self.assertLess(result["mean_iou"], 1.0)
        self.assertGreaterEqual(result["mean_iou"], 0.0)

    def test_shape_mismatch_fails_clearly(self):
        with self.assertRaisesRegex(ValueError, "same shape"):
            segmentation_metrics(np.zeros((2, 2)), np.zeros((3, 3)), num_classes=2)


if __name__ == "__main__":
    unittest.main()