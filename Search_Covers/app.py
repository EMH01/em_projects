import gradio as gr
from db_management import SongDatabase

# Data Base Instance
db = SongDatabase()

# Functions for Gradio
def add_song(url):
  try:
    success = db.add_song(url)
    if success:
      stored_songs = [f"{song['title']} - {song['author']}" for song in db.song_data]
      gr.Info(f"✅ Song added successfully from '{url}'!")
      return "\n".join(stored_songs),"" #clean ""
    else:
      raise gr.Error(f"❌ Failed to add song from URL '{url}'. Please check the URL.")
  except Exception as e:
    raise gr.Error(f"❌ Failed to add song from URL '{url}'. Error during search: {e}")

def search_covers(query_url, top_k):
  try:
    results = db.search_covers(query_url, int(top_k))
    if not results:
      return "<div style='color: red;'>No similar songs found.</div>",""

    formatted_results = []
    for i, res in enumerate(results):
      color = "green" if float(res["similarity"].strip('%')) > 30 else "red"
      formatted_results.append(
        f"<div style='color:{color}; margin-bottom:10px;'>"
        f"<strong>{i+1}. {res['title']} - {res['author']}</strong> "
        f"(Similarity: {res['similarity']})"
        f"</div>"
      )
    return "\n".join(formatted_results),""

  except Exception as e:
    raise gr.Error(f"❌ Error during search: {e}")

# Gradio Interface
with gr.Blocks(theme=gr.themes.Soft()) as app:
  gr.Markdown("# 🎵 **Cover Searching App**")

  with gr.Row():
    with gr.Column():
      gr.Markdown("### 🎼 **Add Songs to the Album**")
      song_url_input = gr.Textbox(label="YouTube URL", placeholder="Enter the song's YouTube URL...")
      add_button = gr.Button("➕ Add Song")
      stored_songs_output = gr.Textbox(label="Stored Songs", lines=10, interactive=False)
      add_button.click(add_song, inputs=song_url_input, outputs=[stored_songs_output, song_url_input])

      with gr.Column():
        gr.Markdown("### 🔍 **Search for Similar Covers**")
        with gr.Row():
          query_url_input = gr.Textbox(label="Search Cover URL", placeholder="Enter a YouTube URL to search...")
          top_k_input = gr.Number(label="Top Results to Show", value=1, precision=0)
        search_button = gr.Button("🔍 Search")
        search_output = gr.HTML(label="Results")
        search_button.click(search_covers, inputs=[query_url_input, top_k_input], outputs=[search_output, query_url_input])

# App Execute
app.launch()
