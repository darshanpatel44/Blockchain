import streamlit as st
import hashlib
import os
from blockClass import main_block
from blockchain import main_blockchain
from hash import main_hash

st.set_page_config(
    page_title="Blockchain Visualization",
    page_icon="sha.png",
)


def app():
    st.title('Blockchain Demo')
    st.markdown("""
    ***
    """)

    choice = st.sidebar.radio(
        "",
        # ("Hash", "Block", "Blockchain", "Distributed Blockchain", "Tokens")
        ("Blockchain", "Block", "Hash", "Distributed Blockchain", "Tokens")
    )

    if choice == "Hash":
        main_hash()

    if choice == "Block":
        main_block()

    if choice == "Blockchain":
        st.subheader('Blockchain')
        main_blockchain()

    if choice == "Distributed Blockchain":
        st.subheader('Distributed Blockchain')
    if choice == "Tokens":
        st.subheader('Tokens')

    hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)


if __name__ == "__main__":

    app()
