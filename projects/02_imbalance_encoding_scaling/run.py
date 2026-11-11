"""Synthetic imbalanced-classification pipeline with fold-local resampling."""

import numpy as np
import pandas as pd
from imblearn.over_sampling import RandomOverSampler
from imblearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def make_data(rows: int = 800, seed: int = 7) -> tuple[pd.DataFrame, np.ndarray]:
    rng = np.random.default_rng(seed)
    labels = (rng.random(rows) < 0.08).astype(int)
    frame = pd.DataFrame(
        {
            "volume": rng.normal(loc=labels * 1.8, scale=1.0, size=rows),
            "age_days": rng.integers(1, 100, size=rows),
            "region": rng.choice(["north", "south", "west"], size=rows),
        }
    )
    return frame, labels


def train_and_evaluate(seed: int = 7) -> dict[str, object]:
    features, target = make_data(seed=seed)
    numeric = ["volume", "age_days"]
    categorical = ["region"]
    preprocess = ColumnTransformer(
        [
            ("numeric", StandardScaler(), numeric),
            ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical),
        ]
    )
    model = Pipeline(
        [
            ("preprocess", preprocess),
            ("oversample", RandomOverSampler(random_state=seed)),
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )
    x_train, x_test, y_train, y_test = train_test_split(
        features, target, test_size=0.25, stratify=target, random_state=seed
    )
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    score = balanced_accuracy_score(y_test, predictions)
    return {
        "balanced_accuracy": float(score),
        "report": classification_report(y_test, predictions, zero_division=0),
        "class_counts": np.bincount(y_test).tolist(),
    }


def run_demo() -> dict[str, object]:
    results = train_and_evaluate()
    print("Test class counts:", results["class_counts"])
    print("Balanced accuracy:", round(results["balanced_accuracy"], 3))
    print(results["report"])
    return results


if __name__ == "__main__":
    run_demo()