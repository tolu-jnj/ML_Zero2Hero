# Project 01: Data Quality Pipeline

This example profiles a synthetic order table and reports duplicate identifiers, missing targets, and invalid lead times before filtering rows. The covered dimensions and pipeline stages are grounded in the Week 1 deck. [COURSE: 01 Expert Guide C2 W1 Live Event.pdf#slides 7-8]

Run from the repository root with `make run-01`. Run tests with `make test-01`.

The data is generated in memory and is not written to disk. The filtering policy is an exercise, not a universal rule; real data requires domain-owner validation. [EXTERNAL: established data-quality engineering references]