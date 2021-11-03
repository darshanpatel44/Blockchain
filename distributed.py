import streamlit as st
from blockchain import Blockchain, main_blockchain
import hashlib


class DistributedBlockchain():

    chain_cntr = 0

    def __init__(self):
        self.node_counter = 1
        DistributedBlockchain.chain_cntr += 1
        st.write('Chain #', DistributedBlockchain.chain_cntr)
        prev = {}
        prev['hash'] = '0000000000000000000000000000000000000000000000000000000000000000'
        st.session_state.chain_network[DistributedBlockchain.chain_cntr] = {}
        st.session_state.chain_network[DistributedBlockchain.chain_cntr][self.node_counter] = Blockchain(
            prev, self.node_counter)

    def single_chain(self):
        pass


def main_distributed():

    if 'chain_network' not in st.session_state:
        for i in range(3):
            DistributedBlockchain()
        st.warning('No chains created yet')
        st.session_state.chain_network = {}

    else:

        st.write('Chains present')

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
        st.session_state['chain_network'][1]

    elif peer == "Peer B":
        st.subheader("Peer B")
        st.session_state['chain_network'][2]

    elif peer == "Peer C":
        st.subheader("Peer C")
        st.session_state['chain_network'][3]
