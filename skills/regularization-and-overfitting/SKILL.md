---
name: regularization-and-overfitting
description: "Use when training scores are much stronger than validation scores or when selecting L1/L2 penalties and model complexity."
---

# Regularization and Overfitting

## Course Grounding

The course presents L1/L2 penalties and describes overfitting as strong training performance with weaker validation/test behavior. [COURSE: 02 Expert Guide C2 W2 Live Event.pdf#slide 7] [COURSE: 02_Week_2_Transcript.txt#lines 245-287]

## Workflow

1. Compare training and validation metrics and inspect learning curves.
2. Check split quality, leakage, data volume, label quality, and feature relevance before tuning penalties. [COURSE: 03_Week_3_Transcript.txt#lines 210-275]
3. Tune regularization on training folds only.
4. Re-evaluate the selected model once on the held-out test set.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

search = GridSearchCV(LogisticRegression(max_iter=1000), {"C": [0.01, 0.1, 1, 10]}, cv=5)
search.fit(train_features, train_labels)
```

The parameter grid and validation plan are illustrative; adapt the estimator and split to the task. [EXTERNAL: official scikit-learn model-selection documentation]

## Checklist

- [ ] Training/validation gap is quantified.
- [ ] Split and preprocessing leakage are ruled out.
- [ ] Regularization is tuned without test-set feedback.
- [ ] Error slices are reviewed after selection.

## Common Pitfalls

- Treating regularization as a universal repair for bad data or invalid splits. [COURSE: 03_Week_3_Transcript.txt#lines 210-275]
- Reporting cross-validation performance as final test performance.

## Go Deeper

- [GAP] Estimator-specific penalties and calibration are not taught.
- [EXTERNAL: official scikit-learn linear models and model-selection documentation]