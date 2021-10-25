import streamlit as st
import hashlib
import os

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
        # obj = st.session_state.obj
        prefix_str = '0'*PREFIX_ZEROES
        for nonce in range(MAX_NONCE):
            text = self.block_no + \
                str(nonce) + self.data
            hashh = SHA256(text)
            # text
            if hashh.startswith(prefix_str):
                self.nonce = str(nonce)
                self.hash = hashh
                return


def update_val(obj):
    obj.mine()
    obj.flag = False


def touch(obj):
    obj.flag = True


def block():

    obj = st.session_state.block
    # st.session_state.obj
    obj.block_no = st.text_input(
        "Block #:", obj.block_no, on_change=touch, args=(obj,))
    obj.nonce = st.text_input(
        "Nonce:", obj.nonce, on_change=touch, args=(obj,))
    obj.data = st.text_area("Data:", obj.data, on_change=touch, args=(obj,))

    obj.hash_str = obj.block_no + obj.nonce + obj.data

    obj.hash = SHA256(obj.hash_str)
    st.write("Hash:")
    obj.hash

    if obj.flag:
        st.error(obj.hash)
    else:
        st.success(obj.hash)
        # st.balloons()

    st.button("Mine", on_click=update_val, args=(obj,))

    # st.session_state.obj.block_no
    # st.session_state.obj.nonce
    # st.session_state.obj.data
    # st.session_state.obj.hash_str


def main_block():
    if 'block' not in st.session_state:
        st.session_state.block = Block()
        st.session_state.block.mine()
    block()


if __name__ == "__main__":
    main_block()