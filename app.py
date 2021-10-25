import streamlit as st
import hashlib
import os
from blockClass import Block, mine, block
from hash import main_hash

st.set_page_config(
    page_title="Blockchain Visualization",
    page_icon="blockchain.png",
)


def app():
    st.title('Blockchain Demo')
    st.markdown("""
    ***
    """)

    choice = st.sidebar.radio(
        "",
        ("Hash", "Block", "Blockchain", "Distributed Blockchain", "Tokens")
    )

    if choice == "Hash":
        main_hash()
        # st.image("sha.png",width=40)
        # st.subheader('SHA256 Hash')
        # txt = st.text_area('Data:', '''''')
        # result = SHA256(txt)
        # st.text("Hash:")
        # st.info(result)

    if choice == "Block":
        block(st.session_state.obj)

    if choice == "Blockchain":
        st.subheader('Blockchain')
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
    if 'obj' not in st.session_state:
        st.session_state.obj = Block()
        mine(4)

    app()
