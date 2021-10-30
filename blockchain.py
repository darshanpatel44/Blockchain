import streamlit as st
import hashlib

PREFIX_ZEROES = 4
MAX_NONCE = 500000


# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def SHA256(text):
    return hashlib.sha256(text.encode("ascii")).hexdigest()


class Block:

    def __init__(self, prev, id):

        self.idx = id
        self.block_no = str(self.idx)
        self.nonce = 4444
        self.data = ""
        self.hash = {}
        self.hash_str=""
        self.prev = prev
        self.flag = False
        self.mine()

    
    def hasChanged(self):

        text = self.block_no + str(self.nonce) + str(self.data) + str(self.prev['hash'])

        if text==self.hash_str:
            self.flag=False

        else:
            self.flag=True


    def UpdateHash(self):

        hash_str = self.block_no + str(self.nonce) + str(self.data) + str(self.prev['hash'])
        self.hash['hash'] = SHA256(hash_str)

    def mine(self):
        prefix_str = '0'*PREFIX_ZEROES
        for nonce in range(MAX_NONCE):
            text = self.block_no + str(nonce) + self.data + self.prev['hash']
            hashh = SHA256(text)
            # text
            if hashh.startswith(prefix_str):
                self.nonce = nonce
                self.hash['hash'] = hashh
                self.hash_str=text
                self.flag=False
                break
        return


    def touch(self):
        self.block_no=st.session_state[f'block_no{self.idx}']
        self.nonce=st.session_state[f'nonce{self.idx}']
        self.data=st.session_state[f'data{self.idx}']
        

    def single_block(self):

        st.text_input("Block #:", self.block_no, on_change=self.touch, key=f'block_no{self.idx}')

        st.text_input("Nonce:", self.nonce, on_change=self.touch, key=f'nonce{self.idx}')

        st.text_area("Data:", self.data, on_change=self.touch, key=f'data{self.idx}')

        st.write("Prev:")
        st.info(self.prev['hash'])
        self.hasChanged()
        self.UpdateHash()

        st.write("Hash:")
        if self.flag:
            st.error(self.hash['hash'])
        else:
            st.success(self.hash['hash'])

        st.button("Mine", on_click=self.mine, key=f'button{self.idx}')

        st.markdown("""
        ***
        """)

    @staticmethod        
    def addNewBlock():

        chain = st.session_state.chain
        last_mined_block = chain[len(chain)]
        new_block = Block(last_mined_block.hash, last_mined_block.idx+1)
        if new_block.idx not in chain:
            chain[new_block.idx] = new_block




def main_blockchain():

    if "chain" not in st.session_state:
        st.session_state.chain = {}
        prev={}
        prev['hash']='0000000000000000000000000000000000000000000000000000000000000000'
        st.session_state.chain[1] = Block(
            prev, 1)

    chain = st.session_state.chain

    for i in range(1, len(chain)+1):
        chain[i].single_block()

    st.sidebar.write(f"Total Blocks: {len(chain)}")
    st.sidebar.button("Add New Block", on_click=Block.addNewBlock)
