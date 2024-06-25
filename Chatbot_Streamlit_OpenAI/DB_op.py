
import streamlit as st
from supabase import create_client, Client

# Initializar conexion DB usuarios desde archivos de st.secrets
# Para hacerlo desde el servidor local se le pueden pasar directamente por parametro
@st.cache_resource
def conectDB()-> Client:
  return create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

def delete_acc(username,password):
  resp = False
  client = conectDB()
  response = client.table("users").select("username, password").eq("username", username).eq("password", password).execute()
  if len(response.data) > 0:
    client.table("users").delete().eq("username", username).eq("password", password).execute()
    resp = True
  return resp
        
      

# GUARDAR EN BD LA SESION
def save_message(username, role, content):
  client = conectDB()
  client.table("messages").insert({
      "username": username,
      "role": role,
      "content": content
  }).execute()

def load_messages(username):
  client = conectDB()
  response = client.table("messages").select("role, content").eq("username", username).execute()
  return [{"role": msg["role"], "content": msg["content"]} for msg in response.data]

def clean_message(username):
  client = conectDB()
  response = client.table("messages").select("username").eq("username", username).execute()
  if len(response.data) > 0:
    client.table("messages").delete().eq("username",username).execute()
    if "messages" in st.session_state: del st.session_state["messages"]
    if "summarized_messages" in st.session_state: del st.session_state["summarized_messages"]
    st.rerun()
