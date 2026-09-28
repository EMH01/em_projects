# AI & Machine Learning Projects

A curated collection of **Data Science, Machine Learning, and AI Engineering projects** covering document intelligence, semantic search, explainable AI, NLP, computer vision, multimodal systems, and applied AI applications.

This repository is currently being reorganized into a cleaner portfolio structure. The projects listed first below are the **maintained implementations** and are the versions intended for continued development and eventual extraction into standalone repositories.

## Maintained projects

| Project | Area | Main technologies | Focus |
|---|---|---|---|
| [Document AI Assistant](document-ai-assistant/) | RAG · Document AI · Multimodal AI | Python, OpenAI API, PyMuPDF, NumPy, Streamlit | Grounded question answering over PDFs with semantic retrieval and optional image understanding |
| [Semantic Cover Search](semantic-cover-search/) | Semantic Search · Audio AI | Python, transcription, embeddings, FAISS, Gradio | Discover covers and lyrically similar performances through transcription and vector similarity |
| [XAI Perturbation Research](xai-perturbation-research/) | Explainable AI · Computer Vision · Research | PyTorch, TorchVision, VGG19-BN | Reproducible implementation of learned perturbation-based image explanations |
| [Spanish NLP Toolkit](spanish-nlp-toolkit/) | NLP · Topic Modeling · Sentiment Analysis | spaCy, scikit-learn, FastAPI | Deterministic Spanish topic clustering and lexical sentiment analysis |
| [Weather AI Assistant](weather-ai-assistant/) | AI Engineering · APIs · GraphQL | Python, OpenWeather, Strawberry GraphQL, OpenAI API, Gradio, Docker | Grounded conversational weather assistant backed by verified external data |
| [AI / ML Labs](ai-ml-labs/) | ML Experiments · CV · Distributed ML · Multimodal AI | PyTorch, OpenCV, Spark ML, OpenAI API | Curated smaller experiments that do not require standalone repositories |

## Engineering standards

The maintained projects are being brought to a common engineering baseline:

- Python 3.11+ where appropriate
- `pyproject.toml`-based packaging
- explicit configuration through environment variables
- `.env.example` instead of committed credentials
- automated tests for core logic
- Ruff linting
- GitHub Actions CI
- reproducible random seeds where experiments depend on stochastic behavior
- portable model checkpoints using `state_dict`
- clear separation between external services and domain logic
- documentation of methodological changes, limitations, and historical results

The goal is not to add infrastructure for its own sake. Each project uses the level of engineering appropriate to its scope.

## Project highlights

### Document AI Assistant

A compact multimodal RAG system for PDF question answering.

The current architecture keeps chunking, embeddings, retrieval, provenance, and prompting explicit rather than hiding the complete pipeline behind a large framework. Retrieved context is inspectable and answers are grounded in source markers.

[Explore the project →](document-ai-assistant/)

### Semantic Cover Search

A semantic audio-search pipeline built around:

```text
audio → transcription → normalized text → embeddings → FAISS → similarity ranking
```

Uploaded audio is the stable primary input, while YouTube support is isolated as an optional adapter.

[Explore the project →](semantic-cover-search/)

### XAI Perturbation Research

A reproducible modernization of research on learned perturbation functions for explaining image-classifier decisions.

The implementation preserves the original dense pixel-mask explainer and VGG19-BN research design while separating data preparation, training, evaluation, explanation generation, and checkpointing.

[Explore the research project →](xai-perturbation-research/)

### Spanish NLP Toolkit

A transparent classical NLP baseline for Spanish text.

It combines spaCy linguistic processing, sentence embeddings, deterministic K-Means clustering, and Spanish SentiWordNet-style lexical sentiment analysis behind a FastAPI interface.

[Explore the project →](spanish-nlp-toolkit/)

### Weather AI Assistant

An applied AI system combining external weather data, GraphQL, optional historical data, and grounded LLM responses.

The application resolves locations through geocoding, retrieves verified measurements, and only then passes structured context to the language model.

[Explore the project →](weather-ai-assistant/)

### AI / ML Labs

A curated home for smaller experiments that are useful to preserve without turning every notebook or prototype into an independent repository.

Current labs include:

- OpenCV Cartoonizer
- CIFAR-10 transfer learning with VGG19-BN
- Cats vs Dogs with Spark ML
- Zero-shot multimodal vision
- reference-guided windshield inspection

[Explore the labs →](ai-ml-labs/)

## Historical source implementations

The following directories and notebooks are the earlier implementations from which the maintained projects above were rebuilt:

| Original source | Maintained destination |
|---|---|
| `Turing_Test/` + selected ideas from `Chatbot_Streamlit_OpenAI/` | `document-ai-assistant/` |
| `Search_Covers/` | `semantic-cover-search/` |
| `Trabajo de Diploma/` | `xai-perturbation-research/` |
| `topic detection and polarity calculation/` | `spanish-nlp-toolkit/` |
| `WeatherAPP/` | `weather-ai-assistant/` |
| `CartoonizerApp_Streamlit_OpenCV/` | `ai-ml-labs/labs/computer-vision/cartoonizer/` |
| `Pytorch_Classifier_Cifar10/` | `ai-ml-labs/labs/computer-vision/cifar10-transfer-learning/` |
| `Images_Classifier/` | `ai-ml-labs/labs/distributed-ml/cats-vs-dogs-spark/` |
| `Zero_Shot_Example.ipynb` | `ai-ml-labs/labs/multimodal-ai/zero-shot-vision/` |
| `Demo_Test_Windshield.ipynb` | `ai-ml-labs/labs/multimodal-ai/windshield-inspection/` |

These source implementations are retained during the migration so that the evolution of each project remains traceable. They are **not** the recommended entry point for running the current versions.

## Running a project

Each maintained project is self-contained and has its own README.

Typical setup:

```bash
git clone https://github.com/EMH01/em_projects.git
cd em_projects/<project>

python -m venv .venv
source .venv/bin/activate       # macOS/Linux
# .venv\Scripts\activate      # Windows

pip install -e ".[dev]"
```

Then follow the project-specific instructions.

Some projects require external credentials or optional datasets. Those requirements are documented locally and should be supplied through environment variables rather than committed files.

## Repository migration

The current repository is an intermediate workspace while the portfolio is being restructured.

The intended final structure is:

- substantial projects → **standalone repositories**
- smaller experiments → **AI / ML Labs**
- GitHub profile README → **portfolio index and professional overview**

Until that extraction is complete, the maintained directories above should be considered the canonical versions inside this repository.
