# Zero-shot Vision Classification

A minimal multimodal inference lab for zero-shot image classification.

The original notebook used a vision-capable chat model to decide whether a house was present in a remote image. The modernized example keeps that small scope while moving to the **Responses API** and making the model configurable rather than hard-coding a dated model ID.

Run:

```bash
pip install -e ".[multimodal]"
export OPENAI_API_KEY=...
export OPENAI_VISION_MODEL=...
python labs/multimodal-ai/zero-shot-vision/run.py IMAGE_URL
```

The important concept here is **zero-shot multimodal inference**: no task-specific training dataset or fine-tuning is used.

This remains a lab, not a benchmark. A serious classification study would require a labelled evaluation set, stable output parsing, confidence/calibration analysis, and error analysis.
