import faiss  
import numpy as np  
from sklearn.preprocessing import normalize  
from sentence_transformers import SentenceTransformer  
from data_URL_handling import get_details_from_youtube_url  

class SongDatabase:
    def __init__(self):
        self.index = None
        self.song_data = []  # List to store song metadata (title, author, lyrics)
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def add_song(self, url_yt):
        """
        Adds a song to the database by extracting its lyrics and embeddings.
        Args:
            youtube_url (str): The YouTube URL of the song.
        Returns:
            bool: True if the song was added successfully, False otherwise. -- There was adapted to raise exceptions for gradio app
        """
        # Extract lyrics from song url
        song = get_details_from_youtube_url(url_yt)
            
        if not song or not song["lyrics"]:
          raise ValueError("There was an error trying to extract the data from the URL")

        if self.song_exists(song['title'],song['author']):
          raise ValueError("The song already exists")

        lyrics = song['lyrics']

        # Extract the embedidngs of the lyrics
        embeddings = self.extract_embeddings([lyrics])

        if embeddings is None:
          raise ValueError("There was an error trying to extract the embeddings from the data lyrics")

        # Initialize FAISS index if not already created
        if self.index is None:
            self.index = faiss.IndexFlatIP(embeddings.shape[1])
        # IndexFlatIP, which is an index based on internal product vectors and does not support direct elimination

        # Add to index and store song details
        self.index.add(embeddings)
        self.song_data.append({
            'title': song['title'],
            'author': song['author'],
            'lyrics': lyrics
            }
        )

        return True

    def song_exists(self, title,author):
      """
      Checks if a song exists in the database by its title.
      Args:
          title (str): The title of the song to check.
          author (str): The author of the song to check.
      Returns:
          bool: True if the song exists, False otherwise.
      """
      return any(song["title"] == title and song['author']==author for song in self.song_data)


    def extract_embeddings(self, texts):
      """
        Extracts normalized embeddings for the given texts.
        Args:
            texts (list of str): List of texts to encode.
        Returns:
            np.ndarray: Normalized embeddings.
        """
      try:
        embeddings = self.model.encode(texts, convert_to_numpy=True)
        return normalize(embeddings, norm="l2")
      except Exception as e:
        return f"Error extracting embeddings: {e}"


    def search_covers(self, query_url, top_k):
      """
        Searches for the most similar songs in the database to the song in the query URL.
        Args:
            query_url (str): The YouTube URL of the query song.
            top_k (int): Number of top similar results to retrieve.
        Returns:
            list of dict: List of dictionaries with song title, author, and similarity score.
        """

      if self.index is None or not self.song_data:
        raise ValueError("The database is empty. Please add songs before searching.")

      query_details = get_details_from_youtube_url(query_url)
      if not query_details or not query_details["lyrics"]:
        raise ValueError("There was an error trying to extract the data from the URL")

      if top_k > len(self.song_data):
        raise ValueError(f"Invalid 'top_k' value: {top_k}. Must be <= {len(self.song_data)}.")

      query_embedding = self.extract_embeddings([query_details["lyrics"]])
      if query_embedding is None:
        raise ValueError("There was an error trying to extract the embeddings from the data lyrics")

      D, I = self.index.search(query_embedding, top_k)
      results = []

      for i, idx in enumerate(I[0]):
        if idx < len(self.song_data):
          song = self.song_data[idx]
          print(song)
          similarity = D[0][i]*100
          results.append({
              "title": song["title"],
              "author": song["author"],
              "similarity": f"{similarity:.1f}%"
          })
      return results
