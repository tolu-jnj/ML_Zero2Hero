---
name: data-profiling-eda
description: "Use when exploring a new tabular dataset, assessing quality, distributions, missingness, outliers, target balance, and potential leakage."
---

# Data Profiling and EDA

## Course Grounding

The course names data completeness, accuracy, timeliness, consistency, validity, uniqueness, bias, imbalance, noise, and outliers. [COURSE: 01 Expert Guide C2 W1 Live Event.pdf#slide 7] [COURSE: 02 Expert Guide C2 W2 Live Event.pdf#slide 5]

## Workflow

1. Confirm source, row grain, keys, time coverage, target, and allowed-use constraints.
2. Profile schema, nulls, duplicates, cardinalities, ranges, and class counts.
3. Compare distributions across time and relevant groups; investigate unexpected patterns with domain owners. [EXTERNAL: official pandas documentation]
4. Check target leakage candidates and features unavailable at prediction time. [EXTERNAL: official scikit-learn model-selection documentation]
5. Write findings, limitations, and follow-up checks before modeling.

```python
summary = df.describe(include="all").T
missing_rate = df.isna().mean().sort_values(ascending=False)
duplicate_rows = int(df.duplicated().sum())
class_counts = df["target"].value_counts(dropna=False)
```

## Checklist

- [ ] Unit of analysis and target are verified.
- [ ] Missingness, duplicates, ranges, and categories summarized.
- [ ] Time and group slices inspected.
- [ ] Outliers reviewed, not silently deleted.
- [ ] Findings linked to data owners and business rules.

## Common Pitfalls

- Assuming every extreme observation is erroneous. [EXTERNAL: authoritative data-quality references]
- Reporting aggregate quality while missing subgroup underrepresentation. [COURSE: 01_Week_1_Transcript.txt#lines 117-123]

## Go Deeper

- [GAP] The course does not teach a repeatable profiling report or leakage audit.
- [EXTERNAL: official pandas user guide and established data-quality engineering references]