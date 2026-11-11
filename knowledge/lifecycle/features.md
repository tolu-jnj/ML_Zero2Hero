# Features

## Course Grounding

- Week 2 introduces categorical encoding, numerical scaling, imbalance, noise/outliers, and regularization. [COURSE: 02 Expert Guide C2 W2 Live Event.pdf#slides 5-7]
- The transcript names one-hot, label, and ordinal encoding, embeddings, normalization, and standardization as transformations. [COURSE: 02_Week_2_Transcript.txt#lines 191-244]
- The lead-time case uses time features, operational metrics, lag/rolling statistics, correlation, mutual information, and permutation importance in its illustrated pipeline. [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slide 6]

## Apply It

1. Define each feature's meaning, source, timestamp availability, and allowed values. [EXTERNAL: official feature-engineering and data-contract references]
2. Fit encoders, imputers, scalers, and resampling only on training data or training folds. [EXTERNAL: official scikit-learn pipeline documentation]
3. Create features using only information available at prediction time; for time series, verify every lag/window boundary. [EXTERNAL: authoritative time-series ML references]
4. Compare a compact, domain-informed feature set with broader alternatives using held-out evaluation. [COURSE: 01_Week_1_Transcript.txt#lines 90-111] [EXTERNAL: official scikit-learn model-selection documentation]

## Checklist

- [ ] Feature definitions and prediction-time availability documented.
- [ ] Training-only transforms are encapsulated in a pipeline.
- [ ] Target leakage and post-outcome features checked.
- [ ] Rare categories, missing values, and drift considered.
- [ ] Feature changes evaluated against a baseline.

## Go Deeper

- [GAP] The course does not provide leakage-safe reusable code or production feature-store patterns.
- [EXTERNAL: official scikit-learn preprocessing documentation and authoritative time-series feature-engineering references]