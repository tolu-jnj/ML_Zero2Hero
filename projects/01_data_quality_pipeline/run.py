"""Synthetic data-quality pipeline example.

Course grounding: Week 1 names data-quality dimensions and a collection-to-analysis
pipeline. [COURSE: 01 Expert Guide C2 W1 Live Event.pdf#slides 7-8]
"""

import numpy as np
import pandas as pd


def make_orders(rows: int = 120, seed: int = 7) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    frame = pd.DataFrame(
        {
            "order_id": [f"O-{index:04d}" for index in range(rows)],
            "created_day": rng.integers(1, 366, size=rows),
            "lead_time_days": rng.integers(1, 22, size=rows),
        }
    )
    frame.loc[frame.index[::29], "lead_time_days"] = -1
    frame.loc[frame.index[1::31], "lead_time_days"] = np.nan
    frame = pd.concat([frame, frame.iloc[[3]]], ignore_index=True)
    return frame


def validate_and_clean(frame: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, int]]:
    required = {"order_id", "created_day", "lead_time_days"}
    missing_columns = required - set(frame.columns)
    if missing_columns:
        raise ValueError(f"Missing columns: {sorted(missing_columns)}")

    counts = {
        "input_rows": len(frame),
        "duplicate_ids": int(frame["order_id"].duplicated().sum()),
        "missing_targets": int(frame["lead_time_days"].isna().sum()),
        "invalid_targets": int((frame["lead_time_days"] < 0).sum()),
    }
    cleaned = frame.drop_duplicates(subset="order_id", keep="first").copy()
    valid_target = cleaned["lead_time_days"].notna() & (cleaned["lead_time_days"] >= 0)
    cleaned = cleaned.loc[valid_target].reset_index(drop=True)
    counts["output_rows"] = len(cleaned)
    return cleaned, counts


def run_demo() -> dict[str, object]:
    orders, counts = validate_and_clean(make_orders())
    print("Quality counts:", counts)
    print("Clean rows:", len(orders))
    return {"orders": orders, "counts": counts}


if __name__ == "__main__":
    run_demo()