# AI & Machine Learning Projects

A curated collection of **Data Science, Machine Learning, and AI Engineering projects** covering document intelligence, semantic search, explainable AI, NLP, computer vision, multimodal systems, and applied AI applications.

The repository contains the maintained implementations only: substantial projects live as self-contained directories, while smaller experiments are grouped under **AI / ML Labs**.

## Projects

| Project | Area | Main technologies | Focus |
|---|---|---|---|
| [Document AI Assistant](document-ai-assistant/) | RAG · Document AI · Multimodal AI | Python, OpenAI API, PyMuPDF, NumPy, Streamlit | Grounded question answering over PDFs with semantic retrieval and optional image understanding |
| [Semantic Cover Search](semantic-cover-search/) | Semantic Search · Audio AI | Python, transcription, embeddings, FAISS, Gradio | Discover covers and lyrically similar performances through transcription and vector similarity |
| [XAI Perturbation Research](xai-perturbation-research/) | Explainable AI · Computer Vision · Research | PyTorch, TorchVision, VGG19-BN | Reproducible implementation of learned perturbation-based image explanations |
| [Spanish NLP Toolkit](spanish-nlp-toolkit/) | NLP · Topic Modeling · Sentiment Analysis | spaCy, scikit-learn, FastAPI | Deterministic Spanish topic clustering and lexical sentiment analysis |
| [Weather AI Assistant](weather-ai-assistant/) | AI Engineering · APIs · GraphQL | Python, OpenWeather, Strawberry GraphQL, OpenAI API, Gradio, Docker | Grounded conversational weather assistant backed by verified external data |
| [AI / ML Labs](ai-ml-labs/) | ML Experiments · CV · Distributed ML · Multimodal AI | PyTorch, OpenCV, Spark ML, OpenAI API | Curated smaller experiments that do not require standalone repositories |

## Engineering baseline

The projects are maintained with a common set of engineering principles:

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
- documentation of methodological changes, limitations, and reported results

The goal is not to add infrastructure for its own sake. Each project uses the level of engineering appropriate to its scope.

## Project highlights

### Document AI Assistant

A compact multimodal RAG system for PDF question answering.

The architecture keeps chunking, embeddings, retrieval, provenance, and prompting explicit rather than hiding the complete pipeline behind a large framework. Retrieved context is inspectable and answers are grounded in source markers.

[Explore the project →](document-ai-assistant/)

### Semantic Cover Search

A semantic audio-search pipeline built around:

```text
audio → transcription → normalized text → embeddings → FAISS → similarity ranking
```

Uploaded audio is the stable primary input, while YouTube support is isolated as an optional adapter.

[Explore the project →](semantic-cover-search/)

### XAI Perturbation Research

A reproducible implementation of research on learned perturbation functions for explaining image-classifier decisions.

The project preserves the dense pixel-mask explainer and VGG19-BN research design while separating data preparation, training, evaluation, explanation generation, and checkpointing. The original research thesis is preserved inside the project documentation.

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

## Running a project

Each project is self-contained and has its own README.

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

## Portfolio structure

The repository intentionally distinguishes between:

- **substantial projects**, each with its own architecture, tests, CI, and documentation;
- **AI / ML Labs**, which groups smaller experiments where a standalone repository would add more noise than signal.

Selected substantial projects may later be extracted into independent repositories as the public GitHub portfolio is finalized.
