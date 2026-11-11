# RAG/LLM Application Playbook

## Use When

An LLM should answer from an approved document collection and unsupported answers must be detectable.

## Course Connection

The course names embeddings/RAG and discusses domain context, hallucination, deterministic tools, and human review. [COURSE: 05 Expert Guide C2 W5 Live Event.pdf#slide 3] [COURSE: 05_Week_5_Transcript.txt#lines 221-300] [COURSE: 06_Week_6_Transcript.txt#lines 320-350]

## Workflow

1. Frame supported questions, users, permissions, and consequences.
2. Choose authoritative sources and preserve access metadata.
3. Implement retrieval and measure recall/relevance before generation. [EXTERNAL: official provider/vector-store docs]
4. Add grounded response format, source IDs, abstention, and deterministic checks.
5. Evaluate retrieval, answer correctness, citation support, refusal, latency, and cost separately.
6. Test prompt injection, revoked access, stale docs, and unsupported requests. [EXTERNAL: official provider safety documentation]
7. Release with logging, escalation, and human review appropriate to risk.

## Exit Criteria

- [ ] Access controls are applied at retrieval.
- [ ] Golden questions include expected abstentions.
- [ ] Claims are traceable to approved source passages.
- [ ] Safety and operational metrics meet agreed gates.

## Handoff

Deliver corpus/version, retrieval eval, prompt/model config, safety tests, and runbook to `mlops-deployer` and `ml-monitor`.

## Go Deeper

- [GAP] RAG architecture, evaluation, access-aware retrieval, and adversarial testing are not taught.
- [EXTERNAL: official provider/vector DB documentation and authoritative RAG evaluation/security references]