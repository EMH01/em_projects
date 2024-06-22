from openai import OpenAI
import streamlit as st
from streamlit_chat import message  # es para desplegar chat de mensajes con avatares
from st_login_form import login_form
from supabase import create_client, Client
import fitz  # PyMuPDF
from sumyNLP import summarize, split_text, summarize_text
# import os #para acceder a la variable de entorno local

# Initializar conexion DB usuarios desde archivos de st.secrets
# Para hacerlo desde el servidor local se le pueden pasar directamente por parametro
@st.cache_resource
def conectDB()-> Client:
  return create_client(st.secrets["connections"]["supabase"]["SUPABASE_URL"], st.secrets["connections"]["supabase"]["SUPABASE_KEY"])

def login_page():
  client = login_form()
  if st.session_state["authenticated"]:
    if "messages" in st.session_state: del st.session_state["messages"]
    st.rerun()  # Redireccionar a la página principal una vez autenticado

# Función para eliminar la cuenta
def delete_form():
  client = conectDB()
  with st.form("delete_account_form"):
    st.write("Are you sure you want to delete your account?")
    username = st.text_input("Enter your username", value=st.session_state["username"])
    password = st.text_input("Enter your password", type="password")
    confirm = st.form_submit_button("Delete account")
    if confirm:
      response = client.table("users").select("name, psw").eq("name", username).eq("psw", password).execute()
      if len(response.data) > 0:
        client.table("users").delete().eq("name", username).eq("psw", password).execute()
        st.success("Account deleted successfully.")
        st.session_state["authenticated"] = False
        st.session_state["username"] = None
        st.session_state["to_delete"] = False
        st.rerun()
      else:
        st.error("Invalid username or password.")
        
    if st.form_submit_button("Cancel"):
      st.session_state["to_delete"] = False
      st.session_state["authenticated"] = True
      st.rerun()

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
        
def submit_page():
  content = ""
  uploaded_file = st.file_uploader("Upload a file",type=["txt","pdf"])
  if uploaded_file:
    # Para archivos de texto (.txt)
    if uploaded_file.type == "text/plain":
      # Leer el archivo de texto
      content = uploaded_file.read().decode("utf-8")
    # Para archivos pdf (.pdf)
    if uploaded_file.type == "application/pdf":
      # Leer el archivo de pdf
      with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
          content += page.get_text()
    if uploaded_file.type not in ["text/plain","application/pdf"]:
      st.error("Invalid document type. Try to submit a txt or pdf file.")
  
  if content != "":
    st.session_state["file"]= content
    st.session_state["submit_file"]=False
    st.rerun()  
  else:
    st.warning("No file submitted")
    
  if st.button("Cancel"):
    st.session_state["submit_file"]=False
    st.rerun()
  
def main_page():
  st.title("Assiend: Your assistant and friend")
  # Barra de cierre de sesion o eliminacion de cuenta 
  username = st.session_state["username"]
  
  if username == None: 
    text_header = f"Hello :smiley: :wave:"
  else:
    text_header = f"Hello, {username} :smiley: :wave:"

  st.sidebar.header(text_header)

  with st.sidebar:
    if not st.toggle("Log out",True):
      st.session_state["authenticated"]=False
      st.session_state["username"] = None
      st.rerun() 
    if (username is not None):
      if st.button("Delete account"):
        st.session_state["to_delete"]=True
        st.session_state["authenticated"]=False
        st.rerun()

  
  # Crear instancia del cliente de OpenAI
  # client = OpenAI(api_key=open('apikey.txt').read()) # usando la clave desde archivo de texto
  # client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))  # usando la clave desde v.entorno local
  client = OpenAI(api_key=st.secrets["keys"]["OPENAI_API_KEY"]) # usando la clave desde v.entorno en streamlit secrets

  # Definir avatares de los roles del chat segun los avatares predefinidos en streamlit_chat
  avatar = {
  'user': 'personas',
  'assistant': 'thumbs'
  }

  messages = st.container(height=300,border=False)
  placeholder = st.empty()

  # Formulario de entrada, columna a campo de entrada de texto, b boton de envio, c boton de archivo adjunto
  a,b,c = st.columns([20,2,2])
  user_input = a.chat_input("Write here your message",key='user_message')
  if b.button(":wastebasket:"):
    if username: 
      clean_message(username)
    else:
      if "messages" in st.session_state: del st.session_state["messages"]
  if c.button(":paperclip:"):
    st.session_state["submit_file"] = True
    st.rerun()


  
  # Guardar estados de la sesion en streamlit para tener historial de mensajes
  if "messages" not in st.session_state: 
    # si el historial esta vacio, verificar historial anterior o mandar el primer msj predefinido
    # Cargar el historial de mensajes
    list_messages = load_messages(username) if username else None
    if list_messages: 
      # Resumir el historial de mensajes si existe
      st.session_state["messages"] = list_messages
      st.session_state["messages"].append({"role": "assistant", "content": "Hi I'm your personal assistant chatbot ¿What can I do for you today?"})
    else:
      st.session_state["messages"] = [{"role": "assistant","content": "Hi! I'm your personal assistant chatbot. How can I assist you today?"}]

  # Enviar  archivo al modelo y actualizar el historial de mensajes
  if "file" in st.session_state: 
    text = st.session_state["file"]
    chunks = split_text(text)
    summaries = [summarize_text(chunk) for chunk in chunks]
    combined_summary = " ".join(summaries)
    prompt = f"Please summarize the following text and generate a debate on the key points presented in the same language of the text. The provided text is as follows: {combined_summary}. Please synthesize the main ideas and develop arguments for and against, highlighting the most relevant implications."
    ask = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(model="gpt-3.5-turbo",messages=ask,max_tokens=400,temperature=1.0)
    msg = response.choices[0].message.content
    st.session_state.messages.append({'role': 'assistant', 'content': msg})
    del st.session_state["file"]

  # Enviar todos los mensajes al modelo y actualizar el historial de mensajes
  if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input}) #agrega msj entrado a la sesion e historial
  
    with placeholder.container():
      with st.spinner('Loading...'):
          if username:
            save_message(username, "user", user_input)
            summarized_messages = summarize(st.session_state.messages)
            summarized_messages.append({"role": "user", "content": user_input}) #agrega msj entrado 
            response = client.chat.completions.create(model="gpt-3.5-turbo",messages=summarized_messages,max_tokens=400,temperature=1.0)
            msg = response.choices[0].message.content
          else:
            response = client.chat.completions.create(model="gpt-3.5-turbo",messages=st.session_state.messages,max_tokens=400,temperature=1.0)
            msg = response.choices[0].message.content
      st.session_state.messages.append({'role': 'assistant', 'content': msg})
      if username: save_message(username, "assistant", msg)

  # Mostrar los mensajes en el chat
  for i, msg in enumerate(st.session_state.messages):
    with messages:
      message(msg["content"], is_user=msg["role"] == "user", key=str(i), avatar_style=avatar[msg["role"]])


if "authenticated" not in st.session_state:
  st.session_state["authenticated"] = False
if "to_delete" not in st.session_state:
  st.session_state["to_delete"] = False
if "submit_file" not in st.session_state:
  st.session_state["submit_file"] = False


if st.session_state["authenticated"]:
    if st.session_state["submit_file"]:
      submit_page()
    else:
      main_page()
else:
    if st.session_state["to_delete"]:
      delete_form()
    else:
      login_page()


