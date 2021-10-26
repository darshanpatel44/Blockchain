import streamlit as st
import hashlib
import os
from blockClass import main_block
from blockchain import main_blockchain
from distributed import main_distributed
from hash import main_hash

st.set_page_config(
    page_title="Blockchain Visualization",
    page_icon="sha.png",
)


def app():
    # st.title('Blockchain Demo')
    # st.markdown("""
    # ***
    # """)

    choice = st.sidebar.radio(
        "",
        # ("Hash", "Block", "Blockchain", "Distributed Blockchain", "Tokens")
        ("Distributed Blockchain", "Block", "Hash", "Blockchain", "Tokens")
    )
    st.sidebar.markdown("""
    ***
    """)
    if choice == "Hash":
        st.title('SHA256 Hash')
        st.markdown("""***""")
        main_hash()

    if choice == "Block":
        st.title('Block')
        st.markdown("""***""")
        main_block()

    if choice == "Blockchain":
        st.title('Blockchain')
        st.markdown("""***""")
        main_blockchain()

    if choice == "Distributed Blockchain":
        st.title('Distributed Blockchain')
        st.markdown("""***""")
        main_distributed()

    if choice == "Tokens":
        st.title('Tokens')
        st.markdown("""***""")

    hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)


if __name__ == "__main__":

    app()
