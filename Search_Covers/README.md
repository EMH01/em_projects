# 🎵 Cover Searching App

This project is a Python-based application that allows users to search for similar song covers by analyzing the lyrics of YouTube videos. The app provides a user-friendly graphical interface powered by **Gradio** and utilizes advanced tools such as **OpenAI Whisper** for audio transcription, **SentenceTransformers** for lyric embeddings, and **FAISS** for similarity search.

## 🚀 Features

- **Add Songs:** Extract lyrics and metadata from YouTube videos and store them in the application's database.
- **Search for Covers:** Compare the lyrics of a query song with stored songs to find the most similar ones.
- **Interactive Interface:** A clean and simple interface for adding songs and performing searches.
- **Note:** The objective use is a small-scale search.

## 🛠️ Technologies Used

- **Gradio**: For creating the graphical user interface.
- **OpenAI Whisper**: For transcribing audio into text.
- **SentenceTransformers**: For generating embeddings of song lyrics.
- **FAISS**: For efficient similarity search.
- **PyTube**: For handling YouTube video extraction.
- **Torch/Torchaudio**: For audio processing.

## 🌐 Access the Deployed App

You can try the application directly in your browser! It is deployed on Hugging Face Spaces and available at the following link:

➡️ [Cover Searching App on Hugging Face Spaces](https://esthermariamh-search-music-cover.hf.space)

## 📦 Prerequisites

- Python 3.8 or later
- GPU-enabled environment (for OpenAI Whisper and SentenceTransformers)
- Required Python libraries (see Installation section)

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository-url.git
   cd cover-searching-app
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure your system supports GPU acceleration for better performance:
   - Install CUDA drivers for your GPU (if not already installed).

## 🖥️ Usage

1. Run the application:
   ```bash
   python app.py
   ```

2. Open the local URL displayed in your terminal to access the application interface.

3. **Adding Songs**:
   - Enter a YouTube URL in the input box.
   - Click "➕ Add Song" to extract lyrics and store the song in the database.

4. **Searching for Covers**:
   - Provide a YouTube URL of the song you want to find similar covers for.
   - Specify the number of top results (`Top K`) to display.
   - Click "🔍 Search" to view the results with similarity scores.

## 📝 Project Structure

- **app.py**: Main application logic and interface using Gradio.
- **data_URL_handling.py**: Functions for handling YouTube URLs and extracting lyrics.
- **db_management.py**: Database management for storing song metadata and performing similarity searches.
- **requirements.txt**: List of required Python libraries.

## 🧪 Testing

To test the functionality:
1. Add songs using valid YouTube URLs.
2. Search for covers using other YouTube URLs and observe the results.

**Note:** Make sure to test in a GPU-enabled environment for optimal performance with large datasets or longer songs.
