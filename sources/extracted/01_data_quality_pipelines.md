# 01 - Data Types, Quality, and Pipelines

## Summary

- The live session introduces structured, unstructured, and semi-structured data, a set of data-quality dimensions, and a high-level data-pipeline flow. [COURSE: 01 Expert Guide C2 W1 Live Event.pdf#slides 6-8]
- The instructor emphasizes that a model depends on relevant, representative, and sufficiently prepared data, and that business-domain collaboration matters when translating a use case into a model. [COURSE: 01_Week_1_Transcript.txt#lines 40-60, 117-136]

## Key Concepts

- Structured data examples include spreadsheets and CSV; unstructured examples include documents, images, and video; JSON and XML are given as semi-structured examples. [COURSE: 01 Expert Guide C2 W1 Live Event.pdf#slide 6] [COURSE: 01_Week_1_Transcript.txt#lines 61-65]
- The deck names completeness, accuracy, timeliness, consistency, validity, and uniqueness as data-quality questions, and separately calls out privacy/security, data bias, and scalability. [COURSE: 01 Expert Guide C2 W1 Live Event.pdf#slide 7]
- The pipeline overview is collection, ingestion, processing, storage, and analysis; the transcript discusses changing data patterns, preprocessing, missing values, and redundant features. [COURSE: 01 Expert Guide C2 W1 Live Event.pdf#slide 8] [COURSE: 01_Week_1_Transcript.txt#lines 116-136]
- The instructor distinguishes a continuous prediction objective from a classification objective when answering a question about linear and logistic regression. [COURSE: 01_Week_1_Transcript.txt#lines 84-96]

## Worked Examples and Case Studies

- The instructor uses completeness, shifting historical patterns, and inconsistent feature representations to explain why stale or partial data can harm model behavior. [COURSE: 01_Week_1_Transcript.txt#lines 67-84]
- A question about correlated features leads to a height/weight example and discussion of removing redundant features or considering PCA. [COURSE: 01_Week_1_Transcript.txt#lines 99-111]
- The instructor cites historical underrepresentation of women in clinical studies as an example of how incomplete population coverage can affect downstream evidence. [COURSE: 01_Week_1_Transcript.txt#lines 117-123]

## Tools and Algorithms Named

- The session names Excel/CSV, PDF, images, video, JSON, XML, database/API/IoT sources, ETL/ELT, random forest, PCA, linear regression, and logistic regression. [COURSE: 01 Expert Guide C2 W1 Live Event.pdf#slides 6-8] [COURSE: 01_Week_1_Transcript.txt#lines 61-65, 90-111, 117-136]

## Q&A

- Asked whether feature correlation determines linear vs. logistic regression, the expert says the target objective distinguishes regression from classification; feature selection is a separate consideration. [COURSE: 01_Week_1_Transcript.txt#lines 84-96]
- Asked for a redundant-feature example, the expert uses correlated height and weight and mentions correlation analysis and PCA. [COURSE: 01_Week_1_Transcript.txt#lines 99-111]
- A learner asks how general-purpose GenAI use relates to the data-pipeline material; the response distinguishes using a pretrained service from developing and controlling an ML solution. [COURSE: 01_Week_1_Transcript.txt#lines 138-162]

## Unclear Points

- The transcript says "on a structured page" immediately before listing PDF text, images, and video; this appears to be an ASR error for "unstructured" because the deck places these examples under unstructured data. [?] [COURSE: 01_Week_1_Transcript.txt#lines 61-65] [COURSE: 01 Expert Guide C2 W1 Live Event.pdf#slide 6]
- The transcript's suggestion that random forests can handle missing data is not accompanied by method, library, or version details. [?] [COURSE: 01_Week_1_Transcript.txt#lines 130-135]

## Go Deeper

- [GAP] Data contracts, schema evolution, lineage, label quality, train/serve consistency, leakage prevention, privacy controls, and repeatable validation are not developed into actionable procedures here.
- [EXTERNAL: official pandas documentation, official database/warehouse documentation, and established data-quality engineering references] Learn profiling, validation contracts, lineage, and reliable ingestion separately from this introductory overview.