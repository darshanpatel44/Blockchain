import streamlit as st
import hashlib
from annotated_text import annotated_text
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
        self.block_no = str(id)
        self.nonce = 4444
        self.data = ""
        self.hash = ""
        self.hash_str = ""
        self.prev = prev
        self.flag = False
        self.mine()

    def UpdateHash(self):
        hash_str = self.block_no + str(self.nonce) + \
        str(self.data) + str(self.prev)

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


def addNewBlock():

    chain = st.session_state.chain

    last_mined_block = chain[len(chain)]

    new_block = Block(last_mined_block.hash, last_mined_block.idx+1)

    if new_block.idx not in chain:

        chain[new_block.idx] = new_block


def touch(obj):
    obj.flag = True


def single_block(obj):

    # annotated_text(
    #     ("NEW BLOCK", "", "#8ef"),)
    # st.write(f"""**Block #{obj.block_no} :**""")
    # st.write(f"""**Nonce:** {obj.nonce}""")
    # st.write(f"""**Hash:** {obj.hash}""")
    # st.write(f"""**Data:** {obj.data}""")
    # st.write(f"""**Previous Hash:** {obj.prev}""")
    st.success(obj.idx)
    obj.block_no = st.text_input(
        "Block #:", obj.block_no, on_change=touch, args=(obj,), key=f'block_no{obj.idx}')

    obj.nonce = st.text_input(
        "Nonce:", obj.nonce, on_change=touch, args=(obj,), key=f'nonce{obj.idx}')

    obj.data = st.text_area("Data:", obj.data, on_change=touch, args=(
        obj,), key=f'data{obj.idx}')

    st.write("Prev:")
    st.info(obj.prev)
    # st.text_input("Prev:", obj.prev, key="prev_hash")
    # obj.hash = st.text_input("Hash:", obj.hash)

    obj.UpdateHash()

    st.write("Hash:")
    if obj.flag:
        st.error(obj.hash)
    else:
        st.success(obj.hash)

    obj.block_no = str(int(obj.block_no)+1)
    st.markdown("""
    ***
    """)


def main_blockchain():
    # if 'id' not in st.session_state:
    #     st.session_state.id = 0
    #     st.write("kjsahkdjhashdkhkaskjdhkahskjd")
    #     st.session_state.id

    if "chain" not in st.session_state:
        st.session_state.chain = {}
        st.session_state.chain[1] = Block(
            '0000000000000000000000000000000000000000000000000000000000000000', 1)

    chain = st.session_state.chain

    for i in range(1, len(chain)+1):
        single_block(chain[i])

    st.sidebar.write(f"Total Blocks: {len(chain)}")
    st.sidebar.button("Add New Block", on_click=addNewBlock)
