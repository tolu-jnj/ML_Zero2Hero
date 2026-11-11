---
name: llm-guardrails
description: "Use when designing LLM constraints, grounding, deterministic checks, human review, refusal, and safe failure behavior."
---

# LLM Guardrails

## Course Grounding

The course discusses hallucinations, prompting, temperature, deterministic tools, domain context, and human review. [COURSE: 05_Week_5_Transcript.txt#lines 221-300, 339-365]

## Workflow

1. Identify harmful or unsupported outcomes and define allowed behavior.
2. Use trusted context and explicit output schemas; do not rely on prompt wording alone. [EXTERNAL: official provider safety documentation]
3. Validate outputs deterministically before they trigger downstream actions.
4. Require human approval for consequential or irreversible steps. [COURSE: 06_Week_6_Transcript.txt#lines 20-40]
5. Test refusal, unsupported claims, malformed output, prompt injection, and tool failures. [EXTERNAL: authoritative LLM safety/evaluation references]

```python
def accept_result(result, evidence_ids, schema_valid):
    return bool(schema_valid and evidence_ids and result.get("status") == "supported")
```

## Checklist

- [ ] Trusted evidence and refusal conditions are defined.
- [ ] Output schema and downstream checks are enforced.
- [ ] Human review and escalation are risk-based.
- [ ] Safety tests run before each release.

## Common Pitfalls

- Treating low temperature or a prompt as a guarantee against hallucination. [COURSE: 05_Week_5_Transcript.txt#lines 239-256] [EXTERNAL: official provider documentation]
- Letting generated text directly perform privileged actions.

## Go Deeper

- [GAP] The course does not provide a complete safety policy or adversarial test suite.
- [EXTERNAL: official provider safety/evaluation docs and organizational security policy]