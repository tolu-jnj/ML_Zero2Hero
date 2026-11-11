---
name: feature-encoding-scaling
description: "Use when preparing categorical or numeric features with encoding, scaling, imputation, or leakage-safe transforms."
---

# Feature Encoding and Scaling

## Course Grounding

Week 2 discusses one-hot, label, and ordinal encoding, embeddings, normalization, and standardization. [COURSE: 02_Week_2_Transcript.txt#lines 191-244]

## Workflow

1. Classify features by type, cardinality, ordering, missingness, and model family.
2. Select a representation that preserves meaning; do not encode nominal categories as ordered numbers without justification. [EXTERNAL: official scikit-learn preprocessing documentation]
3. Fit imputation, encoding, and scaling within a training pipeline/fold. [EXTERNAL: official scikit-learn Pipeline documentation]
4. Validate unknown categories and missing-value behavior at inference.

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

prep = ColumnTransformer([
    ("num", StandardScaler(), numeric_columns),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_columns),
])
```

## Checklist

- [ ] Category semantics and order are documented.
- [ ] Learned transforms fit only on training data.
- [ ] Unknown and missing values have explicit behavior.
- [ ] Output dimension and sparse/dense format are checked.

## Common Pitfalls

- Fitting encoders before splitting data. [EXTERNAL: official scikit-learn preprocessing documentation]
- Scaling every feature regardless of estimator or data type.

## Go Deeper

- [GAP] The course does not provide fold-safe implementation patterns.
- [EXTERNAL: official scikit-learn preprocessing and pipeline documentation]