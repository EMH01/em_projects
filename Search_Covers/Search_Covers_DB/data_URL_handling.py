from pytubefix import YouTube
import numpy as np
import pandas as pd
import whisper
import torch
import torchvision
import torchaudio
import re

def is_valid_youtube_url(url):
  """
  Check if a URL is valid for YouTube.
  Args:
      url (str): URL to be validated.
  Returns:
      bool: True if valid, False otherwise.
  """
  youtube_regex = re.compile(
      r"^(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+$"
  )
  return youtube_regex.match(url) is not None
    
def get_details_from_youtube_url(youtube_url):
  """
    Extract the lyrics from a YouTube video using openai-whisper.
    Args:
        youtube_url: The URL of the YouTube video.
    Returns:
        A dictionary with the video details and the transcribed lyrics.
    """
  if not is_valid_youtube_url(youtube_url):
    raise ValueError(f"Error: The URL '{youtube_url}' is invalid. Tray another")

  try:
    model = whisper.load_model("base",device="cuda") #large-v2, large

    yt = YouTube(youtube_url)

    # Prepare video details
    audio_stream = yt.streams.filter(only_audio=True).first()

    if not audio_stream:
        raise ValueError("No audio stream found for the video.")

    video_details = {
      "title": yt.title,
      "author": yt.author,
      "audio_url": audio_stream.url,
      "lyrics": ""
      }

    # Transcribe lyrics
    lyrics = model.transcribe(video_details['audio_url'])
    lyrics = [segment["text"] for segment in lyrics["segments"]] # divided in segments of sentences
    # lyrics = lyrics["text"]  # complete song in a text
    video_details['lyrics'] = lyrics
    video_details.pop('audio_url') # Remove temporary audio URL

    return video_details

  except Exception as e:
    return f"Error processing YouTube URL {youtube_url}: {e}"