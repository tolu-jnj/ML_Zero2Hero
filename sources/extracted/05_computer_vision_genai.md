# 05 - Computer Vision, Metrics, and GenAI Guardrails

## Summary

- The session expands from CNN classification to semantic/instance segmentation, object detection, and tracking, then presents an orthopedic instrument-tray inspection case using computer vision. [COURSE: 05_Week_5_Transcript.txt#lines 46-147] [COURSE: 05 Expert Guide C2 W5 Live Event.pdf#slide 6]
- The same session discusses selecting metrics based on the cost of different error types and introduces hallucination reduction, prompting, model settings, deterministic tools, and human review as guardrail themes. [COURSE: 05_Week_5_Transcript.txt#lines 150-180, 221-300]

## Key Concepts

- The instructor describes an encoder/decoder segmentation architecture: the encoder reduces image detail to semantic features and the decoder upsamples to recover object regions. [COURSE: 05_Week_5_Transcript.txt#lines 61-102]
- The case combines classification, detection, segmentation, and quality checks to inspect component presence, placement, and defects. [COURSE: 05_Week_5_Transcript.txt#lines 120-147]
- The metric discussion explains why accuracy may be misleading when defects are rare and why recall can be prioritized when missed defects are especially costly. [COURSE: 05_Week_5_Transcript.txt#lines 150-180]
- GenAI content includes LLMs, prompt engineering, embeddings, fine-tuning, RAG, and agentic AI as topics in the self-directed learning. [COURSE: 05 Expert Guide C2 W5 Live Event.pdf#slide 3] [COURSE: 05_Week_5_Transcript.txt#lines 40-46]
- The transcript describes hallucination as a risk and mentions prompts, temperature, domain context, deterministic tools, and human review as parts of a response. [COURSE: 05_Week_5_Transcript.txt#lines 221-300]

## Worked Examples and Case Studies

- Orthopedic loaner trays are described as manually checked for item presence and placement before shipping and after return; the slide describes an AI-based pipeline and iPad workflow. [COURSE: 05 Expert Guide C2 W5 Live Event.pdf#slide 6]
- The expert uses a defect-inspection example to explain why recall may matter more than precision when a missed defect is more consequential than a false alarm. [COURSE: 05_Week_5_Transcript.txt#lines 160-180]
- A learner's sales-report example illustrates that a language model should not substitute for deterministic filters when exact report matching depends on fields such as billing type. [COURSE: 05_Week_5_Transcript.txt#lines 265-300]

## Tools and Algorithms Named

- CNNs, semantic segmentation, instance segmentation, object detection, object tracking, vision transformers, LLMs, RAG, prompt engineering, embeddings, fine-tuning, and temperature are named. [COURSE: 05_Week_5_Transcript.txt#lines 46-112, 221-256]
- The case slide describes the inspection pipeline as GxP validated; this is a property of the presented case and not general validation guidance. [COURSE: 05 Expert Guide C2 W5 Live Event.pdf#slide 6]

## Q&A

- Asked whether higher temperature is useful, the expert says it may suit exploratory insight generation, while exact-match tasks call for deterministic logic and tighter controls. [COURSE: 05_Week_5_Transcript.txt#lines 339-365]
- Learners ask how to ensure generated reporting matches existing spreadsheets; the answer recommends integrating AI with deterministic tools and explicit constraints rather than relying on a chat response alone. [COURSE: 05_Week_5_Transcript.txt#lines 265-308]

## Unclear Points

- The extracted slide text on pages 4-5 contains only "More on Computer Vision"; the transcript supplies the spoken explanation but the diagrams themselves are not represented in extracted text. [?] [COURSE: 05 Expert Guide C2 W5 Live Event.pdf#slides 4-5]
- The transcript's discussion of temperature as a hallucination-control mechanism is high-level and does not specify model/provider behavior or an evaluation protocol. [?] [COURSE: 05_Week_5_Transcript.txt#lines 239-256]

## Go Deeper

- [GAP] Annotation protocols, dataset splits, segmentation metrics, calibration, clinical/regulated validation, red-team testing, retrieval evaluation, and release governance are not covered in operational detail.
- [EXTERNAL: official PyTorch/Torchvision documentation, official provider documentation for the chosen LLM, and authoritative computer-vision/medical-device validation references] Select task-specific metrics and validate the full workflow, not only model outputs.