blockchain = []


def get_user_amount():
    return float(input("Your transittion amount please: "))


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])
    print(blockchain)


tx_amount = get_user_amount()
add_value(tx_amount)
tx_amount = get_user_amount()
add_value(tx_amount, get_last_blockchain_value())
tx_amount = get_user_amount()
add_value(tx_amount, get_last_blockchain_value())