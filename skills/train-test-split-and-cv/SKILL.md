---
name: train-test-split-and-cv
description: "Use when designing train, validation, test, grouped, stratified, or temporal cross-validation splits and preventing leakage."
---

# Train/Test Split and Cross-Validation

## Course Grounding

The course discusses training, validation, and test performance and notes that changing patterns can affect future performance. [COURSE: 02 Expert Guide C2 W2 Live Event.pdf#slide 7] [COURSE: 01_Week_1_Transcript.txt#lines 73-84]

## Workflow

1. Identify repeated entities, temporal order, and any grouping that must not cross splits.
2. Choose random, stratified, grouped, or temporal validation to reflect the deployment question. [EXTERNAL: official scikit-learn cross-validation documentation]
3. Keep the final test set untouched until model/threshold decisions are complete.
4. Fit preprocessing and resampling inside each training fold.
5. Record split IDs and random seeds for reproducibility.

```python
from sklearn.model_selection import GroupKFold

cv = GroupKFold(n_splits=5)
for train_idx, valid_idx in cv.split(features, target, groups=entity_ids):
    fit_fold(features.iloc[train_idx], target.iloc[train_idx])
```

## Checklist

- [ ] Split matches the intended future use.
- [ ] Related records cannot leak across folds.
- [ ] Test set is not used for tuning or threshold selection.
- [ ] Preprocessing is fit inside each fold.

## Common Pitfalls

- Randomly splitting a temporal or entity-grouped dataset. [EXTERNAL: official scikit-learn documentation]
- Reusing the test set for repeated model selection.

## Go Deeper

- [GAP] The course does not specify temporal/group split strategy.
- [EXTERNAL: official scikit-learn cross-validation guide and authoritative time-series validation references]