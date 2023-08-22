genesis_block = {
    "previous_hash": "",
    "index": 0,
    "transactions": [],
}
blockchain = []
open_transactions = []
owner = "Igor"


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def get_user_amount():
    return float(input("Your transittion amount please: "))


def get_transaction_value():
    tx_recipient = input("Enter the sender of the transaction: ")
    tx_amount = float(input("Your transaction amount please: "))
    return (tx_recipient, tx_amount)


def get_user_transaction():
    return float(input("Your transaction value: "))


def get_user_input():
    user_input = input("Your choice: ")
    return user_input


def get_user_choice():
    user_input = input("Your choice: ")
    return user_input


def print_blockchain_elements():
    for element in blockchain:
        print("Element: ")
        print(element)
    else:
        print("-" * 20)


def addTransaction(recipient, sender=owner, amount=1.0):
    transaction = {"sender": sender, "amount": amount, "recipient": recipient}
    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    block = {
        "previous_hash": "XYZ",
        "index": len(blockchain),
        "transactions": open_transactions,
    }
    blockchain.append(block)


def verify_chain():
    is_valid = True
    block_index = 0
    for block in blockchain:
        if block_index == 1:
            block_index += 1
        if block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
        break
    return is_valid


waiting_for_input = True

while waiting_for_input:
    print("Please choose")
    print("1: Add a new transaction value: ")
    print("2: Output de blockchain blocks: ")
    print("h: Manipulate the chain: ")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        addTransaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == "2":
        print_blockchain_elements()
    elif user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == "q":
        waiting_for_input = False
    else:
        print("invalid choice!")
    if not verify_chain():
        print("invalid blockchain!")
        break
else:
    print("User left!")
print("Done!")
