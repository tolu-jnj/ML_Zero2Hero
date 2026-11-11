# Generative AI and Agentic AI

## Course Grounding

- The course pathway names LLMs, prompt engineering, embeddings, fine-tuning, RAG, and agentic AI. [COURSE: 05 Expert Guide C2 W5 Live Event.pdf#slides 3, 8]
- Week 6 describes GenAI as generating content and agentic AI as coordinating tools/workflow steps toward a task, with human review retained for some actions. [COURSE: 06_Week_6_Transcript.txt#lines 20-40]
- A comparison graphic presents agentic systems as autonomous, goal-oriented, tool-using, and adaptive, while presenting generative AI as content-oriented; this is a simplified slide-level distinction. [COURSE: 06 Expert Guide C2 W6 Live Event.pdf#slide 5]
- The ILA case combines an LLM with deterministic/statistical tools and human approval. [COURSE: 06_Week_6_Transcript.txt#lines 45-160]

## Apply It

1. Define the user task, allowed actions, data boundary, and failure cost before selecting an LLM or agent. [EXTERNAL: official provider safety documentation and organizational governance policy]
2. Prefer deterministic code for exact calculations, permissions, and state transitions. [COURSE: 05_Week_5_Transcript.txt#lines 265-308]
3. Keep tool access bounded and require human approval for consequential or irreversible actions. [COURSE: 06_Week_6_Transcript.txt#lines 20-40] [EXTERNAL: official agent-framework safety documentation]
4. Evaluate end-to-end outcomes, not only fluency of generated text. [EXTERNAL: official model-provider evaluation documentation]

## Checklist

- [ ] Model, tools, and human responsibilities are explicit.
- [ ] Tool schemas and permissions are narrowly scoped.
- [ ] Failure path and escalation are defined.
- [ ] Quality, latency, cost, and safety are evaluated.

## Go Deeper

- [GAP] The course does not specify agent architecture, authorization, prompt-injection defense, tool-call reliability, or a full evaluation harness.
- [EXTERNAL: official provider/agent-framework docs and authoritative agent safety/evaluation papers]