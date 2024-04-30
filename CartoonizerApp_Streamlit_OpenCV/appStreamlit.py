import base64
import streamlit as st
import cv2
import numpy as np
from cartoonizer import image_to_cartoon

# # Para incrustar imagen directamente en html: leer archivo binario y convertirlo en cadena Based64
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# # Se trabaja con html para manejos de estilos mas avanzados
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('background.png')

# Insertar múltiples espacios en blanco para separar visualmente
st.markdown("<br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)

# Crear las pestañas y asignarlas a variables individuales
tab1, tab2 = st.tabs(["Upload image", "Take a photo"])

def toCartoon_and_show(img):
    cartoon = image_to_cartoon(img)
    # Dividir pantalla en columnas
    col1,col2 = st.columns(2,gap="small") 
    col1.image(img,channels="RGB")
    col2.image(cartoon,channels="RGB")
    return cartoon

# Subir archivo
with tab1:
    fl = st.file_uploader(
        label = "Upload your image here"
    )
    if fl:
        if "image" in fl.type:
            img = cv2.imdecode(np.fromstring(fl.read(), np.uint8), cv2.IMREAD_COLOR)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)   # convertir a formato BGR
            img = cv2.resize(img, (400, 600))
            imgc = toCartoon_and_show(img)

            img_bytes = cv2.cvtColor(imgc, cv2.COLOR_BGR2RGB)
            img_bytes = cv2.imencode('.jpg', img_bytes)[1].tobytes()
            st.download_button(
                                label="Save",
                                data=img_bytes,
                                file_name="cartoon_image.jpg",
                                key=1,
                                mime="image/jpeg"
            )
        else:
            st.error("Enter a correct file, image type")
            st.stop()
    
with tab2:
    # Si la pestaña "Take It" está seleccionada
    picture = st.camera_input("Take a pic")
        # Mostrar la imagen capturada
    if picture is not None:
        img = cv2.imdecode(np.fromstring(picture.read(), np.uint8), cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)   # convertir a formato BGR
        imgc = toCartoon_and_show(img)

        img_bytes = cv2.cvtColor(imgc, cv2.COLOR_BGR2RGB)
        img_bytes = cv2.imencode('.jpg', img_bytes)[1].tobytes()
        st.download_button(
                            label="Save",
                            data=img_bytes,
                            file_name="cartoon_image.jpg",
                            key = 2,
                            mime="image/jpeg"
        )

        
