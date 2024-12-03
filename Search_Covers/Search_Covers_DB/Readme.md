# Search_Covers_DB: A Song Cover Detection System

This project uses machine learning to identify song covers based on their lyrics.  It leverages sentence transformers for embedding generation, Faiss for efficient similarity search, and Whisper for audio transcription. The entire process is designed to run within a Google Colab environment utilizing a GPU for accelerated processing.

## Overview

The system works in the following stages:

1. **Data Loading:**  Loads a pre-processed dataset of song lyrics (assumed to be available as `top_songs.csv`, containing 'title', 'artist', and 'lyrics' columns).  This dataset should be pre-downloaded and stored locally before running the notebook. The notebook itself contains code to download the dataset from Kaggle if necessary.

2. **Embedding Generation:**  Generates embeddings for each song's lyrics using the SentenceTransformer model ("all-MiniLM-L6-v2").  The GPU accelerates this computationally intensive task.

3. **Vector Database Creation:**  Builds a Faiss index using the generated embeddings, optimized for fast similarity searches.

4. **Query Processing:**  Given a YouTube URL, the system:
    - Downloads the audio using `pytubefix`.
    - Transcribes the audio into text using the `openai-whisper` library's Whisper model (using the GPU).
    - Generates embeddings for the transcribed lyrics.
    - Searches the Faiss index for the nearest neighbors (songs with similar lyrics).

5. **Results:** Returns a list of the top-k most similar songs from the database, along with their similarity scores.

## Prerequisites

- Google Colab with GPU runtime enabled.
- Python 3
- Libraries: `pytubefix`, `json`, `subprocess`, `sentence_transformers`, `faiss`, `numpy`, `pandas`, `kaggle`, `torch`, `torchvision`, `torchaudio`, `openai-whisper` (Installation instructions provided in the notebook).

## Installation

1. Open this notebook in Google Colab.
2. Enable GPU acceleration in the "Runtime" -> "Change runtime type" menu.
3. Run all cells in the notebook sequentially.  This will install necessary libraries and download the required dataset (if not already present).

## Usage

1.  **Ensure `top_songs.csv` exists:**  This CSV file, created by a previous step in the notebook, contains the pre-processed song lyrics data. Make sure it's in your Colab environment.
2.  **Provide a YouTube URL:** Replace `"https://youtu.be/TWX0SAh3T1I"`  (or other example URLs in the evaluation section) with the YouTube URL of the song you want to analyze.
3.  **Specify k:** Change the value of `k` to adjust the number of similar songs returned.
4.  **Run the `get_covers` function:** Execute the cell containing the `get_covers` function call.  This will perform the entire cover detection pipeline and print the results.

## Evaluation

The notebook includes a section for evaluating the system's performance on several example YouTube URLs.  A comprehensive evaluation would require ground truth data (a list of known covers for each URL) to calculate precision and recall.  The current evaluation provides a qualitative assessment.

##  Note on `torch.load` warning

The notebook may issue a `FutureWarning` related to `torch.load`. This warning is related to security concerns when loading untrusted models. Since we are loading a pre-trained model from a trusted source, this warning can be ignored for now, but in future applications,  using `weights_only=True` is recommended.


This project offers a basic framework for song cover detection.  Improvements could include using more sophisticated embedding models, larger datasets, and more robust audio processing techniques.
