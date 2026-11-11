# Lead-Time Regression Playbook

## Use When

Predicting a continuous time-to-event or delivery/lead-time value from historical operational records.

## Course Connection

The ATP case predicts shipping lead time, engineers time/operational features, and compares XGBoost with a graph model. [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slides 4-8]

## Workflow

1. Define target timestamps, units, issue time, and business acceptance with `problem-framing`.
2. Profile censoring, backorders, missingness, data freshness, and entity/time structure.
3. Split chronologically or by deployment-relevant entities; compute lag features from past data only. [EXTERNAL: official scikit-learn/time-series validation documentation]
4. Establish a simple baseline with `baseline-modeling`.
5. Engineer time/operational features with `regression-forecasting`; record availability timestamps.
6. Train XGBoost using `gradient-boosting-xgboost`; tune under a fixed validation budget.
7. Compare MAE/RMSE and operational error bands by cohort; inspect chart metric definitions before interpreting case-study values. [?] [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slides 6-8]
8. Package approved model; monitor outcomes and data changes.

## Exit Criteria

- [ ] Target and prediction horizon are unambiguous.
- [ ] No future data leaks into features or splits.
- [ ] Baseline and candidate errors are reported in time units.
- [ ] Cost, latency, limits, and retraining owner are documented.

## Handoff

Give pipeline, split definition, error slices, model artifact, and monitoring signals to `mlops-deployer`.

## Go Deeper

- [GAP] Forecast uncertainty, robust backtesting, production retraining, and graph-model reproduction are not covered.
- [EXTERNAL: official XGBoost docs and established forecasting references]