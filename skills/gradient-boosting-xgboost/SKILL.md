---
name: gradient-boosting-xgboost
description: "Use when building, tuning, and evaluating XGBoost models for tabular classification or regression."
---

# Gradient Boosting with XGBoost

## Course Grounding

The shipping case uses XGBoost and lists preprocessing, engineered features, feature selection, tuning, and comparison with a graph model. [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slides 6-8]

## Workflow

1. Confirm target, baseline, split, metric, and prediction-time feature availability.
2. Prepare categorical/missing values according to the chosen XGBoost version and API. [EXTERNAL: official XGBoost documentation]
3. Train a conservative baseline; tune only within the training/validation procedure.
4. Evaluate error slices, calibration if relevant, inference latency, and cost.
5. Save model and training metadata using the project experiment-tracking workflow. [EXTERNAL: official MLflow documentation]

```python
from xgboost import XGBClassifier

model = XGBClassifier(n_estimators=200, max_depth=4, learning_rate=0.05, random_state=7)
model.fit(train_features, train_labels)
probabilities = model.predict_proba(valid_features)[:, 1]
```

Parameters are illustrative, not course-prescribed defaults. [EXTERNAL: official XGBoost Python API documentation]

## Checklist

- [ ] Metric and class threshold match the decision.
- [ ] Split and feature construction prevent leakage.
- [ ] Candidate selection uses validation data only.
- [ ] Training artifacts and parameters are recorded.

## Common Pitfalls

- Assuming tree models eliminate the need for feature/time leakage checks. [EXTERNAL: authoritative ML evaluation references]
- Treating feature importance as causal explanation.

## Go Deeper

- [GAP] Reproducible tuning, model registry, and production serving are not covered.
- [EXTERNAL: official XGBoost, scikit-learn, and MLflow documentation]