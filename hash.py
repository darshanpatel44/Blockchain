import streamlit as st
import hashlib


def SHA256(text):
    return hashlib.sha256(text.encode("ascii")).hexdigest()


def main_hash():
    # st.subheader('SHA256 Hash')
    txt = st.text_area('Data:', '''''')
    result = SHA256(txt)
    st.text("Hash:")
    st.info(result)
