"""Synthetic segmentation-mask metrics; no real images or trained weights."""

import numpy as np


def segmentation_metrics(
    truth: np.ndarray, prediction: np.ndarray, num_classes: int
) -> dict[str, object]:
    if truth.shape != prediction.shape:
        raise ValueError("truth and prediction must have the same shape")
    if truth.size == 0 or num_classes < 2:
        raise ValueError("masks must be non-empty and num_classes must be at least 2")

    per_class_iou = []
    per_class_dice = []
    for label in range(num_classes):
        true_mask = truth == label
        predicted_mask = prediction == label
        intersection = int(np.logical_and(true_mask, predicted_mask).sum())
        union = int(np.logical_or(true_mask, predicted_mask).sum())
        denominator = int(true_mask.sum() + predicted_mask.sum())
        per_class_iou.append(float(intersection / union) if union else float("nan"))
        per_class_dice.append(float(2 * intersection / denominator) if denominator else float("nan"))

    accuracy = float((truth == prediction).mean())
    mean_iou = float(np.nanmean(per_class_iou))
    return {
        "pixel_accuracy": accuracy,
        "mean_iou": mean_iou,
        "per_class_iou": per_class_iou,
        "per_class_dice": per_class_dice,
    }


def make_masks(size: int = 32) -> tuple[np.ndarray, np.ndarray]:
    truth = np.zeros((size, size), dtype=np.uint8)
    prediction = np.zeros_like(truth)
    truth[8:24, 9:23] = 1
    prediction[9:24, 10:23] = 1
    return truth, prediction


def run_demo() -> dict[str, object]:
    truth, prediction = make_masks()
    scores = segmentation_metrics(truth, prediction, num_classes=2)
    print("Pixel accuracy:", round(scores["pixel_accuracy"], 3))
    print("Mean IoU:", round(scores["mean_iou"], 3))
    print("Per-class Dice:", [round(value, 3) for value in scores["per_class_dice"]])
    return scores


if __name__ == "__main__":
    run_demo()