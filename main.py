import hashlib

class CardboardBlock:
    def __init__(self, previous_block_hash, transaction_list) -> None:
        self.prervious_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

class CardboardWallet:
    def __init__(self, private_key) -> None:
        self.public_key = ""
        self.address = ""
        
class CardboardTransaction:
    def __init__(self, previous_transaction_hash, sender, receiver, amount : float) -> None:
        self.previous_transaction_hash = previous_transaction_hash
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.transaction_data = previous_transaction_hash + "-" + sender + "-" + receiver + "-" + amount
        self.transaction_hash = hashlib.sha256(self.transaction_data.encode()).hexdigest()
    


print("lol")