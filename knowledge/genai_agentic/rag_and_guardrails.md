# RAG and Guardrails

## Course Grounding

- The Week 5 pathway names embeddings and retrieval-augmented generation; the Week 6 discussion says domain documents can provide context to a language-model workflow. [COURSE: 05 Expert Guide C2 W5 Live Event.pdf#slide 3] [COURSE: 06_Week_6_Transcript.txt#lines 320-350]
- The expert discusses hallucination, prompts, model temperature, deterministic tools, and human review as guardrail themes. [COURSE: 05_Week_5_Transcript.txt#lines 221-300, 339-365]
- The sales-report example emphasizes deterministic filters when exact report matching depends on fields such as billing type. [COURSE: 05_Week_5_Transcript.txt#lines 265-308]

## Apply It

1. Define what evidence is authoritative and who may access it. [EXTERNAL: organizational data-access policy]
2. Retrieve relevant passages with source identifiers; instruct the model to abstain when evidence is insufficient. [EXTERNAL: official provider RAG documentation]
3. Evaluate retrieval recall/relevance and answer correctness separately using curated cases. [EXTERNAL: authoritative RAG evaluation references]
4. Treat retrieved content as untrusted input; do not let it grant permissions or override system constraints. [EXTERNAL: official provider prompt-injection/safety documentation]
5. Route exact calculations and validation to deterministic functions, then log evidence and decisions. [COURSE: 05_Week_5_Transcript.txt#lines 265-308] [EXTERNAL: official provider tool-use documentation]

## Checklist

- [ ] Source permissions match user permissions.
- [ ] Chunks retain source identity and update dates.
- [ ] Retrieval and generation are measured independently.
- [ ] Prompt injection, unsupported answers, and abstention are tested.
- [ ] Sensitive inputs/outputs are handled under policy.

## Go Deeper

- [GAP] The course does not teach chunking, retrieval evaluation, citation grounding, access-aware retrieval, or adversarial testing.
- [EXTERNAL: official vector database/provider docs and authoritative RAG evaluation and security references]