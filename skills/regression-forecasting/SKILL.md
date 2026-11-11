---
name: regression-forecasting
description: "Use for continuous-value prediction, lead-time estimation, and time-dependent forecasting with appropriate baselines and validation."
---

# Regression and Forecasting

## Course Grounding

The course distinguishes continuous prediction from classification and presents an XGBoost lead-time case with time features and operational context. [COURSE: 01_Week_1_Transcript.txt#lines 84-96] [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slides 4-6]

## Workflow

1. Define target units, prediction horizon, issue time, and acceptable error.
2. Build a naive or business baseline.
3. Use a chronological or otherwise deployment-faithful split; compute lags using past data only. [EXTERNAL: official scikit-learn and time-series validation documentation]
4. Compare MAE/RMSE and error slices in units stakeholders understand. [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slide 6]
5. Report uncertainty or prediction ranges when point estimates are insufficient. [EXTERNAL: authoritative forecasting references]

```python
from sklearn.metrics import mean_absolute_error, root_mean_squared_error

mae = mean_absolute_error(actual, predicted)
rmse = root_mean_squared_error(actual, predicted)
```

## Checklist

- [ ] Target definition and horizon match the decision.
- [ ] Validation preserves time and entity constraints.
- [ ] Features use only information known at prediction time.
- [ ] Error metrics and slices are communicated in target units.

## Common Pitfalls

- Randomly shuffling time-dependent observations. [EXTERNAL: authoritative time-series validation references]
- Treating the course case's unlabeled chart scores as a known metric. [?] [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slide 8]

## Go Deeper

- [GAP] Forecast intervals, backtesting design, and production retraining policy are not taught.
- [EXTERNAL: official forecasting-library documentation and established forecasting textbooks]