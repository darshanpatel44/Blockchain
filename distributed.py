import streamlit as st
from blockchain import Blockchain, main_blockchain
import hashlib


class DistributedBlockchain():

    def __init__(self):
        self.chain={}
        self.chain[1] = Blockchain()
        self.total_chains=1

    def add_chain(self):

        self.total_chains += 1
        self.chain[self.total_chains] = Blockchain()


# A block should be verified by all the peers before adding to the chain


def main_distributed():

    
    if 'dist_blockchain' not in st.session_state:
        st.session_state.dist_blockchain = DistributedBlockchain()

    
    if st.session_state.dist_blockchain.total_chains == 1:
        for i in range(2):
            st.session_state.dist_blockchain.add_chain()
            

    st.markdown("""
    <style>
    .css-1vgnld3 {
        font-size: 17px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    peer = st.sidebar.radio("Peers :", ["Peer A", "Peer B", "Peer C"])

    st.sidebar.markdown("""***""")

    # for i in range(3):
    #     if peer == "Peer A":
    #         st.session_state['chain_network'][i].single_chain()

    if peer == "Peer A":
        st.subheader("Peer A")
        st.session_state.dist_blockchain.chain[1].render_chain()
        

    elif peer == "Peer B":
        st.subheader("Peer B")
        st.session_state.dist_blockchain.chain[2].render_chain()

    elif peer == "Peer C":
        st.subheader("Peer C")
        st.session_state.dist_blockchain.chain[3].render_chain()
