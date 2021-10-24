import streamlit as st
import hashlib
import os

st.set_page_config(
    page_title="Blockchain Visualization",
    page_icon="sha.png",
)


MAX_NONCE = 500000     
def mine(block_number,transaction,prefix_zeros):
    prefix_str='0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text= str(block_number)+ str(nonce) + transaction 
        hashh = SHA256(text)
        # print(hash)
        if hashh.startswith(prefix_str):
            return str(nonce),hashh


def SHA256(text):
    return hashlib.sha256(text.encode("ascii")).hexdigest()


if "block_no" not in st.session_state:
    st.session_state.block_no = '1'

if "nonce" not in st.session_state:
    st.session_state.nonce = '4444'

if "data" not in st.session_state:
    st.session_state.data = ''

if "hash" not in st.session_state:
    st.session_state.hash = '0000000000000000000000000000000000000000000000000000000000000000'
    st.session_state.nonce , st.session_state.hash = mine(st.session_state.block_no,st.session_state.data,4)

if "hash_str" not in st.session_state:
    st.session_state.hash_str = ''

if "flag" not in st.session_state:
    st.session_state.flag = False

if "button" not in st.session_state:
    st.session_state.button = False

def touch():
    st.session_state.flag = True
    st.session_state.flag

def update_val():
    st.session_state.nonce , st.session_state.hash = mine(st.session_state.block_no,st.session_state.data,4)
    st.write(st.session_state.nonce)
    # st.write(st.session_state.hash)
    st.session_state.flag=False
    


def app():
    st.title('Demo')

    st.session_state.hash_str
    st.markdown("""
    ***
    """)

    st.session_state.block_no = st.text_input("Block #:", st.session_state.block_no,on_change=touch)
    st.session_state.nonce = st.text_input("Nonce:",st.session_state.nonce,on_change=touch)
    st.session_state.data = st.text_input("Data:", st.session_state.data,on_change=touch)

    st.session_state.hash_str = str(st.session_state.block_no) + str(st.session_state.nonce) + str(st.session_state.data) 
    # st.session_state.button = st.button("Mine")
    # val_hash = st.warning(st.session_state.hash)
    st.write("Hash:")

    st.session_state.hash = SHA256(st.session_state.hash_str)
    if st.button("Mine"):
        st.session_state.nonce , st.session_state.hash = mine(st.session_state.block_no,st.session_state.data,4)
        st.write(st.session_state.nonce)
        # st.write(st.session_state.hash)
        st.session_state.flag=False
        # st.experimental_rerun()
        

    if st.session_state.flag:
        st.error(st.session_state.hash)
    else:
        st.success(st.session_state.hash)
        # st.balloons()
    
    

def main():
    st.title('State Demo')
    st.text_input("Input", key="text",on_change=update_this)

    
if __name__ == "__main__":
    app()