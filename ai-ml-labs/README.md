# AI / ML Labs

A curated collection of **smaller AI, Machine Learning, and Computer Vision experiments** that are useful to keep, but do not need standalone repositories.

These labs evolved from smaller experiments and follow the same principle used for the larger portfolio projects:

> preserve the idea and learning value, update the engineering, correct known issues, and never present historical results as freshly reproduced results.

## Why these experiments live together

The main portfolio projects have enough scope to stand on their own:

- Document AI / RAG
- Semantic Cover Search
- Explainable AI Research
- Spanish NLP Toolkit
- Weather AI Assistant

The experiments here are narrower. Splitting each of them into a separate public repository would add noise without adding much signal. Together they provide useful evidence of breadth across classical CV, transfer learning, Spark ML, and multimodal AI.

## Labs

| Lab | Area | What it demonstrates | Status |
|---|---|---|---|
| [OpenCV Cartoonizer](labs/computer-vision/cartoonizer/) | Classical CV | image filtering, edge extraction, Streamlit UI | Modernized |
| [CIFAR-10 + VGG19-BN](labs/computer-vision/cifar10-transfer-learning/) | Deep Learning | transfer learning, PyTorch, reproducible evaluation | Modernized; results need rerun |
| [Cats vs Dogs with Spark ML](labs/distributed-ml/cats-vs-dogs-spark/) | Distributed ML | Spark feature engineering, feature selection, DT/SVM/MLP comparison | Modernized; results need rerun |
| [Zero-shot Vision](labs/multimodal-ai/zero-shot-vision/) | Multimodal AI | zero-shot image classification with a vision-capable model | Modernized example |
| [Windshield Inspection](labs/multimodal-ai/windshield-inspection/) | Multimodal AI | reference-guided visual prompting | Modernized prototype |

## Repository structure

```text
.
├── labs/
│   ├── computer-vision/
│   │   ├── cartoonizer/
│   │   └── cifar10-transfer-learning/
│   ├── distributed-ml/
│   │   └── cats-vs-dogs-spark/
│   └── multimodal-ai/
│       ├── zero-shot-vision/
│       └── windshield-inspection/
├── src/ai_ml_labs/
│   ├── cartoonizer.py
│   └── multimodal.py
├── tests/
└── pyproject.toml
```

Shared reusable logic lives under `src/ai_ml_labs/`. Each lab keeps its executable example and its own focused README.

## Setup

Base environment:

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\Scripts\activate       # Windows

pip install -e ".[dev]"
```

Install only the extra dependencies needed for the lab you want to run:

```bash
# Streamlit cartoonizer
pip install -e ".[streamlit]"

# PyTorch / CIFAR-10
pip install -e ".[torch]"

# Spark experiment
pip install -e ".[spark]"

# OpenAI multimodal examples
pip install -e ".[multimodal]"
```

Extras can be combined.

## Modernization policy

### Historical results stay historical

If an original notebook or README reported a metric, the corresponding lab can document that number as a historical result.

It does **not** become a new benchmark result until the modernized code has been rerun in a documented environment.

### Known implementation errors are corrected

Modernization is not a byte-for-byte transcription. For example, the original Cats vs Dogs notebook used a 10-unit MLP output layer for a binary task and accidentally routed one selected-feature experiment back through the raw feature column. The new lab fixes those issues and records the changes.

### Small experiments stay small

These labs are not artificially wrapped in microservices, vector databases, Docker stacks, or complex abstractions just to look larger.

The engineering level should match the experiment.

### External datasets and assets are not duplicated blindly

Datasets remain external unless their redistribution terms are clear. Each lab documents how its data was originally obtained.

## Quality

The shared components are covered by lightweight tests:

```bash
ruff check .
pytest -q
```

CI installs only the base + development dependencies. Heavy optional stacks such as PyTorch and Spark are not downloaded for every commit to this secondary experiments repository.
