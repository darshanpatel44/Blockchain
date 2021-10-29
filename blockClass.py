import streamlit as st
import hashlib
import os
import copy

PREFIX_ZEROES = 4
MAX_NONCE = 500000


def SHA256(text):
    return hashlib.sha256(text.encode("ascii")).hexdigest()


class Block:

    def __init__(self):
        self.block_no = "1"
        self.nonce = "4444"
        self.data = ""
        self.hash = ""
        self.hash_str = ""
        self.flag = False

    def mine(self):
        # st.write("mine called")
        prefix_str = '0'*PREFIX_ZEROES
        for nonce in range(MAX_NONCE):
            text = self.block_no + \
                str(nonce) + self.data
            hashh = SHA256(text)
            # text
            if hashh.startswith(prefix_str):
                self.nonce = str(nonce)
                self.hash = hashh
                self.flag = False
                self.hash_str=text
                return


    def hasChanged(self):

        text = self.block_no + self.nonce + self.data

        if text==self.hash_str:
            self.flag=False

        else:
            self.flag=True



def update_val(obj):
    obj.mine()
    # st.warning(obj.hash)


def touch(obj):
    obj.block_no=st.session_state.block_no
    obj.nonce=st.session_state.nonce
    obj.data=st.session_state.data




def block():

    obj = st.session_state.block

    st.text_input("Block #:",obj.block_no, key='block_no',on_change=touch,args=(obj,))
    st.text_input("Nonce:",obj.nonce, key='nonce',on_change=touch,args=(obj,))
    st.text_area("Data:",obj.data, key='data',on_change=touch,args=(obj,))


    obj.hasChanged()
    text = obj.block_no + obj.nonce + obj.data
    obj.hash=SHA256(text)

    # if st.button('Mine'):
    #     update_val(obj)

    if obj.flag:
        st.error(obj.hash)
    else:
        st.success(obj.hash)

    st.button("Mine", on_click=update_val, args=(obj,))

    


def main_block():
    if 'block' not in st.session_state:
        st.session_state.default=[]
        st.session_state.block = Block()
        st.session_state.block.mine()


    block()


if __name__ == "__main__":
    main_block()
