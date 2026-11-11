# Project 03: Isolation Forest

This example generates synthetic 2D order-like observations and uses Isolation Forest to rank/flag unusual points. The course explains short isolation paths and a separate case-specific score threshold. [COURSE: 03 Expert Guide C2 W3 Live Event.pdf#slides 5-7]

Run from the repository root with `make run-03`. Run tests with `make test-03`.

The demo uses estimator contamination to keep the runnable example compact; it does not implement the course Gamma-fit method or a production threshold policy. [GAP] [EXTERNAL: official scikit-learn IsolationForest documentation]