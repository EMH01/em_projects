import cv2
import numpy as np
import streamlit as st

from ai_ml_labs.cartoonizer import cartoonize

st.set_page_config(page_title="OpenCV Cartoonizer", page_icon="🎨")
st.title("🎨 OpenCV Cartoonizer")
st.caption("A small classical-computer-vision demo using edge extraction and bilateral filtering.")

uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "webp"])
camera = st.camera_input("Or take a photo")

source = uploaded or camera
if source is not None:
    encoded = np.frombuffer(source.getvalue(), dtype=np.uint8)
    image_bgr = cv2.imdecode(encoded, cv2.IMREAD_COLOR)
    if image_bgr is None:
        st.error("The image could not be decoded.")
        st.stop()

    result_bgr = cartoonize(image_bgr)
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    result_rgb = cv2.cvtColor(result_bgr, cv2.COLOR_BGR2RGB)

    original_col, result_col = st.columns(2)
    original_col.image(image_rgb, caption="Original", use_container_width=True)
    result_col.image(result_rgb, caption="Cartoonized", use_container_width=True)

    ok, png = cv2.imencode(".png", result_bgr)
    if ok:
        st.download_button(
            "Save result",
            data=png.tobytes(),
            file_name="cartoonized.png",
            mime="image/png",
        )
