---
name: data-quality-validation
description: "Use when defining repeatable schema, range, uniqueness, freshness, and business-rule checks for ML inputs or labels."
---

# Data Quality Validation

## Course Grounding

Week 1 names six quality dimensions and emphasizes validating incoming data before model use. [COURSE: 01 Expert Guide C2 W1 Live Event.pdf#slide 7] [COURSE: 01_Week_1_Transcript.txt#lines 79-84]

## Workflow

1. Translate business rules into explicit invariants with an owner and severity. [EXTERNAL: established data-contract references]
2. Check schema, required fields, types, key uniqueness, ranges, allowed values, and freshness.
3. Validate target labels and source joins; quarantine violations instead of silently coercing them.
4. Run checks in tests and at ingestion; report counts and sample identifiers without leaking sensitive values. [EXTERNAL: official data-validation library documentation]
5. Define fail, warn, and quarantine actions with the data owner.

```python
required = {"order_id", "created_at", "lead_time_days"}
assert required <= set(df.columns)
assert df["order_id"].notna().all()
assert df["order_id"].is_unique
assert (df["lead_time_days"].dropna() >= 0).all()
```

## Checklist

- [ ] Checks are deterministic and version controlled.
- [ ] Failure severity and owner are documented.
- [ ] Invalid rows are traceable and safely quarantined.
- [ ] Tests cover missing, malformed, stale, and duplicate cases.

## Common Pitfalls

- Validating only types while ignoring business meaning. [EXTERNAL: established data-contract references]
- Silently dropping rows and changing the training population.

## Go Deeper

- [GAP] Data contracts, lineage, and automated quality gates are not implemented in the course.
- [EXTERNAL: official Pandera or Great Expectations documentation and organizational data governance policy]