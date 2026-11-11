---
name: rag
description: "Use when grounding an LLM response in an approved document collection through retrieval-augmented generation."
---

# Retrieval-Augmented Generation

## Course Grounding

RAG and embeddings are named in the Week 5 learning path; implementation details are not taught. [COURSE: 05 Expert Guide C2 W5 Live Event.pdf#slide 3] [GAP]

## Workflow

1. Define source authority, access rules, update cadence, and answerable questions.
2. Parse documents while preserving source IDs, headings, and access metadata. [EXTERNAL: official provider and vector-store documentation]
3. Evaluate chunking and retrieval on known queries before adding generation.
4. Require evidence-linked answers and abstention when retrieved support is weak. [EXTERNAL: authoritative RAG evaluation references]
5. Test permissions, stale sources, prompt injection, and unsupported answers.

```python
retrieved = retriever.search(query, filters={"access_group": caller_group}, k=5)
answer = generate(query=query, context=[item.text for item in retrieved])
```

The API is schematic; enforce access controls in the retrieval layer, not by prompt alone. [EXTERNAL: official provider/vector-store security documentation]

## Checklist

- [ ] Source documents and permission metadata are authoritative.
- [ ] Retrieval quality is evaluated separately from answer quality.
- [ ] Citations map to exact source passages.
- [ ] Staleness, deletion, and access revocation are handled.

## Common Pitfalls

- Assuming embeddings guarantee factual answers.
- Retrieving content the caller is not authorized to see. [EXTERNAL: official provider security documentation]

## Go Deeper

- [GAP] The course does not cover indexing, retrieval metrics, access-aware search, or RAG-specific tests.
- [EXTERNAL: official LLM-provider and vector-store docs plus authoritative RAG evaluation/security papers]