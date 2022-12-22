import hashlib
import time
from Crypto.PublicKey import ECC

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
    def __init__(self, previous_transaction_hash, sender, receivers, amount : float) -> None:
        self.previous_transaction_hash = previous_transaction_hash
        self.sender = sender
        self.receivers = receivers
        self.amount = amount
        self.transaction_data = previous_transaction_hash + "-" + sender + "-"
        for receiver in receivers :
            self.transaction_data += self.transaction_data + receiver + "-" + amount
        self.transaction_hash = hashlib.sha256(self.transaction_data.encode()).hexdigest()
    

def validate_chain():
    pass

CURVE_TYPE = 'NIST P-384'
x_a = 31137593094541320334154391440831305925551671014794486124035480450335618828506606831891903939641097389122215362308966
y_a = 22637953351106541126132837576185609566565900682258513854521947094461113636183736302157328686289774132852407609761549
d_a = 33252182191698304726704506596698740821971976555623914616713532247054465763626847622042470584186555723636012179190468
x_b = 34174568388613786440552075263371392602253480877195135397248593161004679250445611165171313788459453278057126205607813
y_b = 11230597964891356689819947823682990423790146055641866626696575539479343296742167021574821970895110359749818546741352
d_b = 19982141819426314660351935628052369474853001519284649627994870695873674185960301276907338584021074879859810665662782

key_a = ECC.construct(curve=CURVE_TYPE, point_x=x_a, point_y=y_a, d=d_a)
key_b = ECC.construct(curve=CURVE_TYPE, point_x=x_b, point_y=y_b, d=d_b)

validate_chain()

adam = CardboardWallet("adam")
bob = CardboardWallet("bob")

class TestWallet:
    def __init__(self, address):
        self.address = address
    def __str__(self):
        return self.address

class TestTransaction:
    def __init__(self,sender,receiver,amount:float):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
    def __str__(self) -> str:
        data = str(self.sender)
        data += "-" + str(self.receiver)
        data += "-" + str(self.amount)
        return data

class TestBlock:
    def __init__(self,data) -> None:
        self.block_data = block_data

class TestChain:
    def __init__(self) -> None:
        pass

class TransactionPool:
    class Candidate:
        def __init__(self, id : int, transaction : TestTransaction) -> None:
            self.id = id
            self.transaction = transaction
            self.timestamp = time.time()
            pass
        
    def __init__(self) -> None:
        self.candidates = []
        self.approved = []
        self.rejected = []
    
    def add(self, to_add : Candidate):
        self.candidates.append(to_add)

    def confirm_transactions(self):
        addresses = {}
        for candidate in self.candidates:
            sender = candidate.sender
            receiver = candidate.receiver
            amount = candidate.amount
            if (sender != "reserve" and not sender in addresses):
                addresses[sender.address] = 0
            if (receiver != "reserve" and not receiver in addresses):
                addresses[receiver.address] = 0
            if (sender == "reserve"):
                addresses[receiver.address] += amount
                self.approved.append(candidate)
            elif (receiver == "reserve" and addresses[sender] > amount):
                addresses[sender] -= amount
                self.approved.append(candidate)
            elif (addresses[sender] > amount):
                addresses[sender] -= amount
                addresses[receiver] += amount
                self.approved.append(candidate)
            else:
                self.rejected.append(candidate)

    def display_approved(self):
        print("Approved Transactions:")
        for transaction in self.approved:
            print(transaction)
        print()

    def display_rejected(self):
        print("Rejected Transactions:")
        for transaction in self.rejected:
            print(transaction)
        print()



reserve = TestWallet("reserve")
alice = TestWallet("alice")
bryan = TestWallet("bryan")
cadence = TestWallet("cadence")
darrell = TestWallet("darrell")
evan = TestWallet("evan")
fred = TestWallet("fred")

t1 = TestTransaction(reserve.address,alice,500.0)
t2 = TestTransaction(reserve.address,bryan,500.0)
t3 = TestTransaction(reserve.address,cadence,500.0)
t4 = TestTransaction(reserve.address,darrell,500.0)
t5 = TestTransaction(reserve.address,evan,500.0)
t6 = TestTransaction(reserve.address,fred,500.0)

tran_alpha = TestTransaction(alice.address,bryan.address,24.43)
tran_beta = TestTransaction(bryan.address,cadence.address,19.36)
tran_gamma = TestTransaction(cadence.address,darrell.address,21.23)
tran_delta = TestTransaction(darrell.address,evan.address,67.12)
tran_epsilon = TestTransaction(evan.address,fred.address,93.02)
tran_eta = TestTransaction(fred.address,alice.address,68.35)
tran_theta = TestTransaction(darrell.address, reserve.address, 200)
tran_f1 = TestTransaction(alice.address, reserve.address, 1000)
tran_f2 = TestTransaction(evan.address, cadence.address, 800)


pool = TransactionPool()
pool.add(t1)
pool.add(t2)
pool.add(t3)
pool.add(t4)
pool.add(t5)
pool.add(t6)
pool.add(tran_alpha)
pool.add(tran_beta)
pool.add(tran_gamma)
pool.add(tran_delta)
pool.add(tran_epsilon)
pool.add(tran_eta)
pool.add(tran_theta)
pool.add(tran_f1)
pool.add(tran_f2)

pool.confirm_transactions()
pool.display_approved()
pool.display_rejected()

