"""Synthetic order anomaly detection using Isolation Forest."""

import numpy as np
from sklearn.ensemble import IsolationForest


def make_orders(rows: int = 300, seed: int = 7) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    normal = rng.normal(loc=0.0, scale=1.0, size=(rows, 2))
    unusual = np.array([[6.0, 6.0], [-6.0, 5.0], [5.0, -6.0]])
    features = np.vstack([normal, unusual])
    labels = np.concatenate([np.zeros(rows, dtype=int), np.ones(len(unusual), dtype=int)])
    return features, labels


def detect(seed: int = 7) -> dict[str, object]:
    features, truth = make_orders(seed=seed)
    detector = IsolationForest(contamination=0.02, random_state=seed)
    detector.fit(features)
    predicted = (detector.predict(features) == -1).astype(int)
    scores = -detector.score_samples(features)
    true_positive = int(((predicted == 1) & (truth == 1)).sum())
    false_positive = int(((predicted == 1) & (truth == 0)).sum())
    return {
        "true_positive": true_positive,
        "known_anomalies": int(truth.sum()),
        "false_positive": false_positive,
        "top_scores": np.sort(scores)[-5:].round(3).tolist(),
    }


def run_demo() -> dict[str, object]:
    result = detect()
    print("Known synthetic anomalies detected:", result["true_positive"], "/", result["known_anomalies"])
    print("Normal points flagged:", result["false_positive"])
    print("Top anomaly scores:", result["top_scores"])
    return result


if __name__ == "__main__":
    run_demo()