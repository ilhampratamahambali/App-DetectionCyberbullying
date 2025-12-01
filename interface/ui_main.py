import streamlit as st
import base64
from utils.helper import predict_text

def run_ui(model, tfidf, encoder):

    st.set_page_config(page_title="Cyberbullying Detector", layout="centered")
    with open("assets/style.css") as css:
        st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)
    try:
        with open("assets/logo.png", "rb") as img_f:
            img_b64 = base64.b64encode(img_f.read()).decode()
        img_src = f"data:image/png;base64,{img_b64}"
    except FileNotFoundError:
        img_src = ""  

    st.markdown(f"""
    <div class="header-container">
        <img src="{img_src}" alt="Logo">
        <h1 class="header-title">Cyberbullying Detection System 💬</h1>
    </div>
    """, unsafe_allow_html=True)

    # --- Text Input ---
    text = st.text_area("Masukkan komentar atau teks:")

    if st.button("Prediksi"):
        if text.strip() == "":
            st.warning("Masukkan teks terlebih dahulu!")
        else:
            hasil = predict_text(text, model, tfidf, encoder)
            formatted = hasil.replace("_", " ").title()
            st.success(f"Cyberbullying - {formatted}")
