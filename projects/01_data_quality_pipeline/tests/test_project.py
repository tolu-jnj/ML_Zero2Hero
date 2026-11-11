import unittest

from run import make_orders, validate_and_clean


class DataQualityTests(unittest.TestCase):
    def test_pipeline_reports_and_removes_invalid_rows(self):
        cleaned, counts = validate_and_clean(make_orders(rows=120))
        self.assertGreater(counts["duplicate_ids"], 0)
        self.assertGreater(counts["missing_targets"], 0)
        self.assertGreater(counts["invalid_targets"], 0)
        self.assertEqual(cleaned["order_id"].nunique(), len(cleaned))
        self.assertTrue((cleaned["lead_time_days"] >= 0).all())

    def test_missing_required_column_fails_clearly(self):
        with self.assertRaisesRegex(ValueError, "Missing columns"):
            validate_and_clean(make_orders().drop(columns="order_id"))


if __name__ == "__main__":
    unittest.main()