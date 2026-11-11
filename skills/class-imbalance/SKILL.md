---
name: class-imbalance
description: "Use when target classes are uneven and accuracy or model behavior may hide minority-class failures."
---

# Class Imbalance

## Course Grounding

Week 2 shows how majority-only predictions can look accurate and discusses over/undersampling and hybrid approaches. [COURSE: 02_Week_2_Transcript.txt#lines 100-121]

## Workflow

1. Count classes overall and by important time/group slices.
2. Select metrics and operating thresholds from error costs; include precision/recall or a confusion matrix. [COURSE: 05_Week_5_Transcript.txt#lines 150-180]
3. Establish an unresampled baseline.
4. If resampling is justified, apply it inside training folds only. [EXTERNAL: official imbalanced-learn and scikit-learn documentation]
5. Compare thresholded and ranking metrics on untouched validation/test data.

```python
from imblearn.pipeline import make_pipeline
from imblearn.over_sampling import SMOTE
from sklearn.linear_model import LogisticRegression

model = make_pipeline(SMOTE(random_state=7), LogisticRegression(max_iter=1000))
model.fit(train_features, train_labels)
```

## Checklist

- [ ] Baseline includes class-wise metrics.
- [ ] Resampling is confined to training folds.
- [ ] Synthetic samples are plausible for feature types and domain.
- [ ] Threshold is selected on validation data and documented.

## Common Pitfalls

- Balancing the test set or resampling before splitting. [EXTERNAL: official imbalanced-learn documentation]
- Treating 50/50 as a universal target; course explicitly notes balance depends on the use case. [COURSE: 02_Week_2_Transcript.txt#lines 109-121]

## Go Deeper

- [GAP] Group-aware evaluation, calibration, cost-sensitive learning, and synthetic-data validation are not developed.
- [EXTERNAL: official imbalanced-learn documentation and authoritative classification evaluation references]