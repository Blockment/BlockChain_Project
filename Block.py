# global variable
from Client import Client
from Miners import Miner
from Transaction import Transaction


class Block:
    def __init__(self):
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.Nonce = ""

    def dump_blockChain(self):
        print("Number of blocks in the chain: " + str(len(self)))
        for x in range(len(TPCoins)):
            block_temp = TPCoins[x]
            print("block # " + str(x))
            for transaction in block_temp.verified_transactions:
                display_transaction(transaction)
                print('--------------')
            print('=====================================')


def display_transaction(transaction):
    # for transaction in transactions:
    dict = transaction.to_dict()
    print("sender: " + dict['sender'])
    print('-----')
    print("recipient: " + dict['recipient'])
    print('-----')
    print("value: " + str(dict['value']))
    print('-----')
    print("time: " + str(dict['time']))
    print('-----')



# global variable
last_transaction_index = 0
transactions = []
last_block_hash = ""
TPCoins = []


Dinesh = Client()
Ramesh = Client()
Seema = Client()
Vijay = Client()

t2 = Transaction(
   Dinesh,
   Seema.identity,
   6.0
)
t2.sign_transaction()
transactions.append(t2)
t3 = Transaction(
   Ramesh,
   Vijay.identity,
   2.0
)
t3.sign_transaction()
transactions.append(t3)
t4 = Transaction(
   Seema,
   Ramesh.identity,
   4.0
)
t4.sign_transaction()
transactions.append(t4)
t5 = Transaction(
   Vijay,
   Seema.identity,
   7.0
)
t5.sign_transaction()
transactions.append(t5)
t6 = Transaction(
   Ramesh,
   Seema.identity,
   3.0
)
t6.sign_transaction()
transactions.append(t6)
t7 = Transaction(
   Seema,
   Dinesh.identity,
   8.0
)
t7.sign_transaction()
transactions.append(t7)
t8 = Transaction(
   Seema,
   Ramesh.identity,
   1.0
)
t8.sign_transaction()
transactions.append(t8)
t9 = Transaction(
   Vijay,
   Dinesh.identity,
   5.0
)
t9.sign_transaction()
transactions.append(t9)
t10 = Transaction(
   Vijay,
   Ramesh.identity,
   3.0
)
t10.sign_transaction()
transactions.append(t10)

block = Block()
for i in range(3):
    temp_transaction = transactions[last_transaction_index]
    # validate transaction
    # if valid
    block.verified_transactions.append(temp_transaction)
    last_transaction_index += 1

block.previous_block_hash = last_block_hash
miner = Miner()
block.Nonce = miner.main(block, 2)
digest = hash(block)
TPCoins.append(block)
last_block_hash = digest

dump_blockchain(TPCoins)
