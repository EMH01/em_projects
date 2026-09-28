# Reference-guided Windshield Inspection

A small multimodal prompting experiment for reference-guided visual inspection.

The task supplies:

1. one reference windshield in good condition
2. one damaged reference
3. one target image

A vision-capable model is then asked to classify the visible target condition and explain the visual evidence.

The modernization removes hard-coded image URLs and migrates the request to the Responses API.

Run:

```bash
pip install -e ".[multimodal]"
export OPENAI_API_KEY=...
export OPENAI_VISION_MODEL=...

python labs/multimodal-ai/windshield-inspection/run.py \
  --good-reference GOOD_URL \
  --damaged-reference DAMAGED_URL \
  --target TARGET_URL
```

## Scope

This is a **prompting prototype**, not a validated damage-detection system. It should not be presented as a safety or automotive diagnostic tool.

A proper evaluation would require a labelled image dataset, damage taxonomy, controlled reference images, robust output parsing, and false-negative analysis.
