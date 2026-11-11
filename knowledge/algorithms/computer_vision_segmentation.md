# Computer Vision and Segmentation

## Course Grounding

- The Week 5 session contrasts classification, semantic segmentation, object detection, and instance segmentation using image examples. [COURSE: 05 Expert Guide C2 W5 Live Event.pdf#slide 4]
- The transcript describes an encoder that extracts semantic features and a decoder that upsamples to recover object regions. [COURSE: 05_Week_5_Transcript.txt#lines 61-102] [COURSE: 05 Expert Guide C2 W5 Live Event.pdf#slide 5]
- The case combines classification, detection, segmentation, and quality checks for orthopedic instrument trays. [COURSE: 05 Expert Guide C2 W5 Live Event.pdf#slide 6]
- The instructor argues for recall when missing a defect is more consequential than a false alarm in the example. [COURSE: 05_Week_5_Transcript.txt#lines 160-180]

## Practical Reading

- Keep image resizing, normalization, annotation conventions, and splits consistent between training and inference. [EXTERNAL: official PyTorch/Torchvision documentation]
- Select segmentation metrics and thresholds based on task and downstream impact; inspect overlays and per-class errors. [EXTERNAL: official computer-vision library documentation and authoritative vision evaluation references]
- The course case's GxP label describes that case and is not a general validation standard. [COURSE: 05 Expert Guide C2 W5 Live Event.pdf#slide 6] [GAP]

## Minimal Pattern

```python
import torch

model.eval()
with torch.inference_mode():
    logits = model(images)
    predicted_mask = logits.argmax(dim=1)
```

This is a minimal inference pattern; input preprocessing and output interpretation depend on the model. [EXTERNAL: official PyTorch documentation]

## Checklist and Pitfalls

- [ ] Document class labels and annotation policy.
- [ ] Split by subject/device/site when correlated images could leak across sets. [EXTERNAL: authoritative computer-vision evaluation references]
- [ ] Review false negatives and false positives by class.
- [ ] Do not equate pixel accuracy with useful object-level performance. [EXTERNAL: authoritative segmentation metric references]
- [GAP] Annotation QA, segmentation metrics, regulated validation, and deployment are not fully taught.

## Go Deeper

- [EXTERNAL: official PyTorch/Torchvision documentation and authoritative medical/computer-vision validation references]