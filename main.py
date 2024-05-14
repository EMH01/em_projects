from openai import OpenAI
import streamlit as st
from streamlit_chat import message  # es para desplegar chat de mensajes con avatares

st.title("Assiend: Your assistant and friend")

# Formulario de entrada, columna a campo de entrada de texto, b boton de envio
with st.form("chat_input", clear_on_submit=True):
  a, b = st.columns([10, 2])

  user_input = a.text_input(key='user_message',label="Your message:",placeholder="Write here your message",label_visibility='collapsed')
  b.form_submit_button("\>", use_container_width=True)

# Guardar estados de la sesion en streamlit para tener historial de mensajes
if "messages" not in st.session_state: # si el historial esta vacio, mandar el primer msj predefinido
    st.session_state["messages"] = [{"role": "assistant", "content": "Hi I'm your personal assistant chatbot ¿What can I do for you today?"}]

# Crear instancia del cliente de OpenAI
client = OpenAI(api_key=open('apikey.txt').read())

# Definir avatares de los roles del chat segun los avatares predefinidos en streamlit_chat
avatar = {
  'user': 'avataaars',
  'assistant': 'bottts'
}

# # temperature: un valor entre 0 y 2 que controla la aleatoriedad o creatividad de la generación.
# # Un valor cercano a 0 genera respuestas más predecibles y conservadoras,
# # cercano a 1 genera respuestas más variadas e innovadoras.
# # placeholder es para agregar un simbolo de cargando mientras se espera respuesta despues de enviar un mensaje
placeholder = st.empty()
# Enviar todos los mensajes al modelo y actualizar el historial de mensajes
if user_input:
  st.session_state.messages.append({"role": "user", "content": user_input}) #agrega msj entrado a la sesion e historial

  with placeholder.container():
    with st.spinner('Loading...'):
      response = client.chat.completions.create(model="gpt-3.5-turbo",messages=st.session_state.messages,max_tokens=400,temperature=1.0)
      msg = response.choices[0].message.content
    st.session_state.messages.append({'role': 'assistant', 'content': msg})

# Mostrar los mensajes en el chat
for i, msg in enumerate(reversed(st.session_state.messages)):
  message(msg["content"], is_user=msg["role"] == "user", key=str(i), avatar_style=avatar[msg["role"]])
