# Project 04: Lead-Time Regression with XGBoost

This example trains an XGBoost regressor on synthetic orders using an ordered temporal holdout and reports MAE in days. It follows the lead-time case's regression framing and XGBoost comparison. [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slides 4-6]

Run from the repository root with `make run-04`. Run tests with `make test-04`. The pinned dependency is the CPU-only XGBoost distribution, so this demo does not install GPU/NCCL runtimes.

Runs are logged locally with MLflow in the ignored `mlflow.db` SQLite database. The generated data is not stored. The course chart's reported metric is unlabeled, so this project does not claim to reproduce its values. [?] [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slide 8]