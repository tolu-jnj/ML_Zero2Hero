"""Synthetic lead-time regression tracked locally with MLflow."""

from pathlib import Path

import mlflow
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor


def make_orders(rows: int = 600, seed: int = 7) -> tuple[pd.DataFrame, np.ndarray]:
    rng = np.random.default_rng(seed)
    day = np.arange(rows)
    backlog = rng.poisson(lam=3.0, size=rows)
    material_group = rng.integers(0, 5, size=rows)
    noise = rng.normal(0.0, 1.2, size=rows)
    lead_time = 3.0 + 0.015 * day + 0.6 * backlog + 1.1 * material_group + noise
    features = pd.DataFrame(
        {"created_day": day, "backlog": backlog, "material_group": material_group}
    )
    return features, np.maximum(lead_time, 0.25)


def train_and_evaluate(seed: int = 7) -> tuple[XGBRegressor, float]:
    features, target = make_orders(seed=seed)
    split = int(len(features) * 0.8)
    x_train, x_test = features.iloc[:split], features.iloc[split:]
    y_train, y_test = target[:split], target[split:]
    model = XGBRegressor(
        n_estimators=80,
        max_depth=3,
        learning_rate=0.05,
        objective="reg:squarederror",
        n_jobs=2,
        random_state=seed,
    )
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    return model, float(mean_absolute_error(y_test, predictions))


def run_demo() -> float:
    model, mae = train_and_evaluate()
    tracking_db = Path(__file__).parent / "mlflow.db"
    mlflow.set_tracking_uri("sqlite:///" + str(tracking_db.resolve()))
    mlflow.set_experiment("synthetic-lead-time")
    with mlflow.start_run():
        mlflow.log_param("model", "XGBRegressor")
        mlflow.log_param("n_estimators", model.n_estimators)
        mlflow.log_metric("test_mae_days", mae)
        mlflow.set_tag("data", "synthetic")
    print("Temporal holdout MAE (days):", round(mae, 3))
    print("MLflow tracking database:", tracking_db)
    return mae


if __name__ == "__main__":
    run_demo()