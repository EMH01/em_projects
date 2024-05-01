import streamlit as st
import cv2
import numpy as np
from cartoonizer import image_to_cartoon

# Función para detectar si el dispositivo es móvil o no
def is_mobile():
    return "config" not in st.session_state
# Seleccionar el fondo dependiendo del dispositivo
background_url = "https://github.com/EMH01/em_projects/blob/main/CartoonizerApp_Streamlit_OpenCV/background_movil.png?raw=true" if is_mobile() else "https://github.com/EMH01/em_projects/blob/main/CartoonizerApp_Streamlit_OpenCV/background.png?raw=true"
background_size =  "100% 20%" if is_mobile() else " 100% 100%"
# Se utiliza html por ausencia de ajustes avanzados en streamlit
page_bg_img = f'''
<style>
.stApp {{
background-image: url("{"https://github.com/EMH01/em_projects/blob/main/CartoonizerApp_Streamlit_OpenCV/background.png?raw=true"}");
background-size: {background_size};
}}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

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
        
