---
name: hyperparameter-tuning
description: "Use when searching model settings with a reproducible validation strategy and controlled compute budget."
---

# Hyperparameter Tuning

## Course Grounding

The Week 4 pipeline slide mentions Bayesian search; the instructor emphasizes comparing models against business needs. [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slide 6] [COURSE: 04_Week_4_Transcript.txt#lines 190-228]

## Workflow

1. Fix the data split, metric, baseline, and resource budget.
2. Search a small, justified parameter space using cross-validation on training data. [EXTERNAL: official scikit-learn search documentation]
3. Log parameters, fold scores, runtime, and code/data versions. [EXTERNAL: official MLflow documentation]
4. Select once using validation evidence; evaluate final performance on the untouched test set.

```python
from sklearn.model_selection import RandomizedSearchCV

search = RandomizedSearchCV(model, param_distributions, n_iter=20, cv=cv, scoring="neg_mean_absolute_error")
search.fit(train_features, train_target)
best_model = search.best_estimator_
```

## Checklist

- [ ] Search space and budget are documented.
- [ ] Split is leakage-safe and deployment-relevant.
- [ ] All trials are logged consistently.
- [ ] Test set remains untouched during search.

## Common Pitfalls

- Increasing search effort before establishing a useful baseline.
- Selecting among many trials on the test set. [EXTERNAL: official scikit-learn model-selection documentation]

## Go Deeper

- [GAP] The course does not teach a repeatable tuning or nested-validation protocol.
- [EXTERNAL: official scikit-learn search documentation and official XGBoost tuning documentation]