# Project 02: Imbalance, Encoding, and Scaling

This example builds a synthetic imbalanced binary-classification pipeline with numeric scaling, one-hot encoding, and training-only random oversampling. Week 2 introduces imbalance and feature transformations. [COURSE: 02_Week_2_Transcript.txt#lines 100-121, 191-244]

Run from the repository root with `make run-02`. Run tests with `make test-02`.

The oversampling choice is illustrative, not a universal recommendation. The held-out test data is not resampled. [EXTERNAL: official imbalanced-learn and scikit-learn documentation]