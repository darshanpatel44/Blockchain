import streamlit as st
import hashlib
import os

PREFIX_ZEROES=4
MAX_NONCE = 500000     

class Block:

    def __init__():
        self.block_no='1'
        self.nonce='4444'
        self.data=""
        self.hash=""
        self.hash_str=""
        self.flag=False

        self.nonce,self.hash=self.mine(PREFIX_ZEROES)

    def mine(self,PREFIX_ZEROES):
        prefix_str='0'*PREFIX_ZEROES

        for nonc in range(MAX_NONCE):
            text= self.block_no+ self.nonce + self.data 
            hashh = SHA256(text)

            if hashh.startswith(prefix_str):
                return str(nonce),hashh






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

def get_var():
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
    

def touch():
    st.session_state.flag = True


def update_val():
    st.session_state.nonce , st.session_state.hash = mine(st.session_state.block_no,st.session_state.data,4)
    st.session_state.flag=False
    


def block():
    st.session_state.block_no = st.text_input("Block #:",st.session_state.block_no,on_change=touch)
    st.session_state.nonce = st.text_input("Nonce:",st.session_state.nonce,on_change=touch)
    st.session_state.data = st.text_area("Data:", st.session_state.data,on_change=touch)

    st.session_state.hash_str = str(st.session_state.block_no) + str(st.session_state.nonce) + str(st.session_state.data) 

    st.session_state.hash = SHA256(st.session_state.hash_str)
    st.write("Hash:")
    if st.session_state.flag:
        st.error(st.session_state.hash)
    else:
        st.success(st.session_state.hash)
        # st.balloons()
    
    st.button("Mine",on_click=update_val)    


def main_block():
    get_var()
    block()

if __name__ == "__main__":
    app()