
---

# 🎵 Cover Searching App

This project is a Python-based application that allows users to search for similar song covers by analyzing the lyrics of YouTube videos. It leverages advanced tools such as **OpenAI Whisper** for audio transcription, **SentenceTransformers** for lyric embeddings, and **FAISS** for similarity search.

## 🚀 Features

- **Add Songs**: Extract lyrics and metadata from YouTube videos and store them in the application's database.  
- **Search for Covers**: Compare the lyrics of a query song with stored songs to find the most similar ones.  
- **Interactive Interface**: A simple interface for adding songs and performing searches.  

## ❗ Limitations and Deployment Decision

This project was initially developed for deployment on **Hugging Face Spaces**. However, due to the following limitations, it has been optimized to run on **Google Colab**:

1. **Issues with `pytubefix`:**
   - The library, used for handling YouTube URLs, has known issues related to authentication (`po_token_verifier`) in non-interactive terminal environments.
   - No viable solution was found with alternatives like `yt-dlp`, which encounter similar challenges.

2. **Hugging Face Spaces Constraints:**
   - Lack of GPU support in certain environments, which affects performance when using **OpenAI Whisper**.
   - Dependency conflicts with **FAISS** and **Torch** during deployment.

Given these challenges, **Google Colab** was chosen as the primary environment for this project due to its flexibility and access to GPU resources.

## 🛠️ Technologies Used

- **Gradio**: For creating the graphical user interface.  
- **OpenAI Whisper**: For transcribing audio into text.  
- **SentenceTransformers**: For generating embeddings of song lyrics.  
- **FAISS**: For efficient similarity search.  
- **PyTube**: For handling YouTube video extraction.  

## 📦 Prerequisites

1. **Google Colab**: Recommended for running the project due to its flexibility and GPU support.  
2. **Python 3.8 or later** (for local setups).  
3. **Required dependencies**: See `requirements.txt`.  

## 🖥️ How to Run on Google Colab

1. Open the project's notebook in Google Colab.  
2. Execute each cell in order to install dependencies and run the application.  
3. **Adding Songs**:  
   - Enter a valid YouTube URL in the input text box.  
   - Click the "➕ Add Song" button.  
4. **Searching for Covers**:  
   - Enter the YouTube URL of the song to search for covers.  
   - Specify the number of most similar results (`Top K`) and click the "🔍 Search" button.  

## 📑 Project Structure

- **app.py**: Main application logic using Gradio.  
- **data_URL_handling.py**: Functions for handling YouTube URLs and extracting lyrics.  
- **db_management.py**: Database management for storing song metadata and performing similarity searches.  
- **requirements.txt**: List of required Python libraries.  
- **search_covers.ipynb**: Colab notebook to run the project end-to-end.  

## ⚠️ Note

Support for `pytubefix` and similar YouTube libraries is still under development. This may limit the usability of this project in deployment environments like Hugging Face Spaces. For contributors, improving YouTube URL handling is a significant area of opportunity.  

## 🤝 Contributions

Contributions are welcome, especially to resolve `pytubefix` issues or explore viable alternatives.  

--- 
