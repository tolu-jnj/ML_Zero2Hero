# Regularization and Overfitting

## Course Grounding

- Week 2 presents regularization as loss plus penalty and describes L1/L2 at an introductory level. [COURSE: 02 Expert Guide C2 W2 Live Event.pdf#slide 7]
- The transcript connects overfitting to strong training performance and weaker validation performance, and says regularization can help in some cases. [COURSE: 02_Week_2_Transcript.txt#lines 245-287]
- The instructor says feature usefulness and data should be investigated when a model cannot fit the training examples as expected. [COURSE: 03_Week_3_Transcript.txt#lines 210-275]

## Practical Reading

- Regularization strength is a hyperparameter and must be selected using training/validation procedures, not the held-out test set. [EXTERNAL: official scikit-learn model-selection documentation]
- Compare learning behavior and data/feature quality before treating a penalty as a universal fix. [COURSE: 03_Week_3_Transcript.txt#lines 210-275]

## Minimal Pattern

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(penalty="l2", C=1.0, max_iter=1000)
model.fit(train_features, train_labels)
```

The meaning of `C` and supported penalties depend on the estimator and scikit-learn version. [EXTERNAL: official scikit-learn LogisticRegression documentation]

## Checklist and Pitfalls

- [ ] Compare training and validation metrics.
- [ ] Tune regularization only within the training/validation process.
- [ ] Check data volume, label quality, and feature relevance.
- [ ] Do not assume L1 always improves feature selection or L2 always prevents overfitting. [EXTERNAL: official scikit-learn documentation]
- [GAP] The course does not teach regularization paths, estimator-specific penalties, or uncertainty estimates.

## Go Deeper

- [EXTERNAL: official scikit-learn linear-model documentation and an established statistical-learning textbook]