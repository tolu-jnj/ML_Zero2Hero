---
name: experiment-tracking
description: "Use when recording repeatable ML runs, parameters, metrics, artifacts, and data/code versions with MLflow."
---

# Experiment Tracking

## Course Grounding

The course compares multiple lead-time models and discusses training/serving costs, but does not teach experiment tracking. [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slides 6-8] [GAP]

## Workflow

1. Set a project-local tracking URI and experiment name.
2. Log parameters, split/metric definitions, dependency versions, and model artifacts. [EXTERNAL: official MLflow Tracking documentation]
3. Use a fixed data/code reference; avoid logging sensitive row-level data.
4. Compare runs using the same validation protocol and preserve the final test result separately.

```python
import mlflow

with mlflow.start_run():
    mlflow.log_param("model", "xgboost")
    mlflow.log_metric("validation_mae", validation_mae)
    mlflow.sklearn.log_model(model, name="model")
```

## Checklist

- [ ] Run has a meaningful name and source revision.
- [ ] Parameters, metrics, and artifacts are logged.
- [ ] Dataset identity and split strategy are recorded.
- [ ] Sensitive data and secrets are excluded.

## Common Pitfalls

- Comparing metrics from incompatible splits.
- Logging credentials or identifiable records as artifacts. [EXTERNAL: official MLflow security and artifact documentation]

## Go Deeper

- [GAP] MLflow and reproducibility workflows are outside the course.
- [EXTERNAL: official MLflow Tracking and Model Registry documentation]