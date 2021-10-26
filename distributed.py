import streamlit as st
from blockchain import main_blockchain
import hashlib


def main_distributed():
    st.markdown("""
    <style>
    .css-1vgnld3 {
        font-size: 17px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    peer = st.sidebar.radio("Peers :", ["Peer A", "Peer B", "Peer C"])

    st.sidebar.markdown("""***""")

    if peer == "Peer A":
        st.subheader("Peer A")
        main_blockchain()

    elif peer == "Peer B":
        st.subheader("Peer B")
        main_blockchain()

    elif peer == "Peer C":
        st.subheader("Peer C")
        main_blockchain()
