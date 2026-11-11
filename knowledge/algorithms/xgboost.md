# XGBoost

## Course Grounding

- The Available-to-Promise example compares baseline and re-engineered XGBoost with a Graph Transformer for normal and abnormal backorders. [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slides 6-8]
- The slide lists preprocessing, engineered time/operational features, feature selection, and a Bayesian-search tuning step around model training. [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slide 6]
- The transcript recommends starting with a less complex model and adding complexity only when needed. [COURSE: 04_Week_4_Transcript.txt#lines 158-188]

## Practical Reading

- Build a simple baseline first, choose an objective matching the target, and compare candidates using the same split and metric. [EXTERNAL: official XGBoost and scikit-learn documentation]
- Preserve time-aware validation when engineered features include lags or rolling windows. [EXTERNAL: authoritative time-series ML references]
- The course case's reported chart metric is not labeled; its values must not be interpreted as a named metric. [?] [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slide 8]

## Minimal Pattern

```python
from xgboost import XGBRegressor

model = XGBRegressor(n_estimators=200, max_depth=4, learning_rate=0.05, random_state=7)
model.fit(train_features, train_target)
predictions = model.predict(eval_features)
```

The parameters are illustrative rather than course-recommended defaults. [EXTERNAL: official XGBoost Python API documentation]

## Checklist and Pitfalls

- [ ] Record objective, metric, split, and random seed.
- [ ] Compare against a simple baseline.
- [ ] Check feature availability at prediction time.
- [ ] Inspect errors by relevant groups and time periods.
- [ ] Do not treat feature importance as causal evidence. [EXTERNAL: official XGBoost documentation]
- [GAP] The course does not provide deployable training code or a reproducible tuning protocol.

## Go Deeper

- [EXTERNAL: official XGBoost documentation and official scikit-learn model-selection documentation]