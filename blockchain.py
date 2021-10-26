import streamlit as st
import hashlib

from streamlit.legacy_caching.caching import clear_cache

PREFIX_ZEROES = 4
MAX_NONCE = 500000


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def SHA256(text):
    return hashlib.sha256(text.encode("ascii")).hexdigest()


class Block:

    def __init__(self, prev, id):

        self.idx = id
        self.block_no = str(self.idx)
        self.nonce = 4444
        self.data = ""
        self.hash = ""
        self.prev = prev
        self.flag = False
        self.mine()

    def UpdateHash(self):

        hash_str = self.block_no + \
            str(self.nonce) + str(self.data) + str(self.prev)
        self.hash = SHA256(hash_str)

    def mine(self):
        prefix_str = '0'*PREFIX_ZEROES
        for nonce in range(MAX_NONCE):
            text = self.block_no + str(nonce) + self.data + self.prev
            hashh = SHA256(text)
            # text
            if hashh.startswith(prefix_str):
                self.nonce = nonce
                self.hash = hashh
                break

        i = self.idx+1

        while i < len(st.session_state.chain):
            st.session_state.chain[i].prev = hashh
            st.session_state.chain[i].UpdateHash()
            st.session_state.chain[i].flag = True
            hashh = st.session_state.chain[i]

            i += 1
            pass

        return

    def single_block(self):

        self.block_no = st.text_input(
            "Block #:", self.block_no, on_change=touch, args=(self,), key=f'block_no{self.idx}')

        self.nonce = st.text_input(
            "Nonce:", self.nonce, on_change=touch, args=(self,), key=f'nonce{self.idx}')

        self.data = st.text_area("Data:", self.data, on_change=touch, args=(
            self,), key=f'data{self.idx}')

        st.write("Prev:")
        st.info(self.prev)

        self.UpdateHash()

        st.write("Hash:")
        if self.flag:
            st.error(self.hash)
        else:
            st.success(self.hash)

        st.markdown("""
        ***
        """)


def addNewBlock():

    chain = st.session_state.chain
    last_mined_block = chain[len(chain)]
    new_block = Block(last_mined_block.hash, last_mined_block.idx+1)
    if new_block.idx not in chain:
        chain[new_block.idx] = new_block


def touch(obj):
    obj.flag = True


def main_blockchain():

    if "chain" not in st.session_state:
        st.session_state.chain = {}
        st.session_state.chain[1] = Block(
            '0000000000000000000000000000000000000000000000000000000000000000', 1)

    chain = st.session_state.chain

    for i in range(1, len(chain)+1):
        chain[i].single_block()

    st.sidebar.write(f"Total Blocks: {len(chain)}")
    st.sidebar.button("Add New Block", on_click=addNewBlock)
