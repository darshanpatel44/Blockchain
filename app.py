import streamlit as st
import hashlib
import os

st.set_page_config(
    page_title="Blockchain Visualization",
    page_icon="blockchain.png",
)
def SHA256(text):
    return hashlib.sha256(text.encode("ascii")).hexdigest()

MAX_NONCE = 500000     
def mine(block_number,transaction,previous_hash,prefix_zeros):
    prefix_str='0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text= str(block_number) + transaction + previous_hash + str(nonce)
        hash = SHA256(text)
        # print(hash)
        if hash.startswith(prefix_str):
            # print("Bitcoin mined with nonce value :",nonce)
            return [nonce,hash]
    # print("Could not find a hash in the given range of upto", MAX_NONCE)

if "nonce" not in st.session_state:
    st.session_state.nonce = '72608'
if "hash" not in st.session_state:
    st.session_state.hash = '0000000000000000000000000000000000000000000000000000000000000000'

def app():
    st.title('Blockchain Demo')
    st.markdown("""
    ***
    """)
    
    choice = st.sidebar.radio(
        "",
    ("Hash", "Block", "Blockchain","Distributed Blockchain","Tokens")
    )

    if choice == "Hash":

        st.image("sha.png",width=40)
        st.subheader('SHA256 Hash')
        txt = st.text_area('Data:', '''''')
        result = SHA256(txt)
        st.text("Hash:")
        st.info(result)

    if choice == "Block":
        st.subheader('Block')
        l=[]
        previous_hash = "0000000000000000000000000000000000000000000000000000000000000000"        
        if not st.button("Mine"):
            block_no = st.text_input('Block #: ', '1')
            nonce = st.text_input('Nonce : ', '72608')
            txt = st.text_area('Data:', '')
            text= str(block_no) + txt + previous_hash + str(nonce)
            text
            result = SHA256(text)
            st.text("Hash:")
            st.text(result)
            st.session_state.l = mine(block_no,txt,result,4)
            state.nonce = st.session_state.l[0]
            st.text(st.session_state.l)
        else:
        
            st.success(l)
            block_no = st.text_input('Block #: ', '1')
            nonce = st.text_input('Nonce : ', l[0])
            txt = st.text_area('Data:', '')
            
            # st.empty()
            # st.text("Nonce:")    
            # st.text(l[0])
            # nonce = st.text_input('Nonce : ', l[0])
            st.text("Hash:")    
            st.text(l[1])
            
        
        # st.success("success")
        # st.error("error")
        # st.balloons()

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
    app()