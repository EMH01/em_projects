from openai import OpenAI
import streamlit as st
from sumyNLP import summarize, split_text, summarize_text
from DB_op import save_message

# import os #para acceder a la variable de entorno local
    # Crear instancia del cliente de OpenAI
def ini_openAI():
  # client = OpenAI(api_key=open('apikey.txt').read()) # usando la clave desde archivo de texto
  # client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))  # usando la clave desde v.entorno local
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"]) # usando la clave desde v.entorno en streamlit secrets
    return client

# Enviar  archivo al modelo y actualizar el historial de mensajes
def file_gpt(text,username):
    client = ini_openAI()
    chunks = split_text(text)
    summaries = [summarize_text(chunk) for chunk in chunks]
    combined_summary = " ".join(summaries)
    prompt = f"Please summarize the following text and generate a debate on the key points presented in the same language of the text. The provided text is as follows: {combined_summary}. Please synthesize the main ideas and develop arguments for and against, highlighting the most relevant implications."
    ask = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(model="gpt-3.5-turbo",messages=ask,max_tokens=400,temperature=1.0)
    msg = response.choices[0].message.content
    if username: save_message(username, "assistant", msg)
    return msg

# Enviar todos los mensajes al modelo y actualizar el historial de mensajes
def ask_gpt(username,user_input):
    client = ini_openAI()
    if username:
        save_message(username, "user", user_input)
        summarized_messages = summarize(st.session_state.messages)
        summarized_messages.append({"role": "user", "content": user_input}) #agrega msj entrado 
        response = client.chat.completions.create(model="gpt-3.5-turbo",messages=summarized_messages,max_tokens=400,temperature=1.0)
        msg = response.choices[0].message.content
        save_message(username, "assistant", msg)
    else:
        response = client.chat.completions.create(model="gpt-3.5-turbo",messages=st.session_state.messages,max_tokens=400,temperature=1.0)
        msg = response.choices[0].message.content
    return msg