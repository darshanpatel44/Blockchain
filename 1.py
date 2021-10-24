import hashlib

def SHA256(text):
    return type(hashlib.sha256(text.encode("ascii")).hexdigest())

MAX_NONCE = 500000     
def mine(block_number,transaction,previous_hash,prefix_zeros):
    prefix_str='0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text= str(block_number) + transaction + previous_hash + str(nonce)
        hash = SHA256(text)
        if hash.startswith(prefix_str):
            print("Bitcoin mined with nonce value :",nonce)
            return hash
    print("Could not find a hash in the given range of upto", MAX_NONCE)

print(mine(1,"1234","7add57b43ea8dfff264dd92e1d1fe6a7dff0475c355d2ea378e5e7e686cd1cec",4))