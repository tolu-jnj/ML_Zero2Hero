---
name: model-explainability
description: "Use when explaining model behavior, inspecting feature contributions, and communicating limits without implying causality."
---

# Model Explainability

## Course Grounding

Week 1 discusses redundant/correlated features and the need to understand which inputs are useful; it does not teach a formal explainability method. [COURSE: 01_Week_1_Transcript.txt#lines 99-111] [GAP]

## Workflow

1. State the audience's question: global behavior, one prediction, or debugging.
2. Establish that the model and evaluation are adequate before explaining them. [EXTERNAL: authoritative model-interpretation references]
3. Choose a method compatible with the model and data; check its assumptions.
4. Compare explanations across representative and failure cases.
5. Communicate that feature association is not causal proof. [EXTERNAL: authoritative explainability references]

```python
from sklearn.inspection import permutation_importance

result = permutation_importance(model, valid_features, valid_target, n_repeats=10, random_state=7)
ranked = result.importances_mean.argsort()[::-1]
```

## Checklist

- [ ] Explanation audience and scope are explicit.
- [ ] Validation data is representative and held out.
- [ ] Stability and subgroup behavior are checked.
- [ ] Limitations and non-causal interpretation are stated.

## Common Pitfalls

- Presenting feature importance as causal effect.
- Explaining a poorly validated model as if explanation implies correctness.

## Go Deeper

- [GAP] The course does not include explanation methods or their limitations.
- [EXTERNAL: official scikit-learn inspection documentation and authoritative interpretability papers]