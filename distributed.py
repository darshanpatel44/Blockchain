import streamlit as st
from blockchain import Blockchain, main_blockchain
import hashlib


class DistributedBlockchain():

    chain_cntr = 0

    def __init__(self):
        DistributedBlockchain.chain_cntr += 1
        st.write('Chain #', DistributedBlockchain.chain_cntr)
        prev = {}
        prev['hash'] = '0000000000000000000000000000000000000000000000000000000000000000'
        st.session_state.chain_network[DistributedBlockchain.chain_cntr] = {}
        st.session_state.chain_network[DistributedBlockchain.chain_cntr][1] = Blockchain(
            prev, 1)

def single_chain(chain_ptr):

    chain=st.session_state.chain_network[chain_ptr]
    
    ptr=1
    while ptr<= len(chain):
        chain[ptr].single_block()
        ptr+=1


def main_distributed():

    
    if 'chain_network' not in st.session_state:

        st.write('Chains not present')
        st.session_state.chain_network = {}
    else:
        st.write('Chains present')

    if DistributedBlockchain.chain_cntr == 0:
        for i in range(3):
            DistributedBlockchain()

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
        # st.session_state['chain_network'][1]
        single_chain(1)

    elif peer == "Peer B":
        st.subheader("Peer B")
        single_chain(2)

    elif peer == "Peer C":
        st.subheader("Peer C")
        single_chain(3)
