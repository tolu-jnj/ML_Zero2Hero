---
name: baseline-modeling
description: "Use before training complex models to define a transparent heuristic, dummy estimator, or simple statistical baseline."
---

# Baseline Modeling

## Course Grounding

The lead-time presentation compares a baseline XGBoost model with engineered and graph-based candidates, while the expert recommends starting with a simpler model. [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slides 6-8] [COURSE: 04_Week_4_Transcript.txt#lines 158-188]

## Workflow

1. Define a simple business rule or naive estimator that matches the current process.
2. Use the same target, split, and metric planned for candidate models.
3. Record performance, coverage, cost, and limitations.
4. Add complexity only when it improves the intended decision enough to justify it. [COURSE: 04_Week_4_Transcript.txt#lines 158-188]

```python
from sklearn.dummy import DummyRegressor

baseline = DummyRegressor(strategy="median")
baseline.fit(train_features, train_target)
baseline_predictions = baseline.predict(valid_features)
```

## Checklist

- [ ] Baseline reflects a plausible no-ML/current process.
- [ ] Candidate comparison uses identical validation data.
- [ ] Business users understand the baseline result.
- [ ] Improvement is measured in operational as well as model terms.

## Common Pitfalls

- Using a weak strawman baseline to make a complex model look valuable. [EXTERNAL: established ML evaluation references]
- Comparing models on different data splits.

## Go Deeper

- [GAP] Course cases do not provide a reusable baseline-selection protocol.
- [EXTERNAL: established statistical-learning and ML evaluation textbooks]