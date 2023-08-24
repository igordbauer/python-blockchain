genesis_block = {
    "previous_hash": "",
    "index": 0,
    "transactions": [],
}
blockchain = [genesis_block]
open_transactions = []
owner = "Igor"
participants = {"Igor"}


def hash_block(block):
    return "-".join([str(block[key]) for key in block])


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def get_balance(participant):
    tx_sender = [
        [tx["amount"] for tx in block["transactions"] if tx["sender"] == participant]
        for block in blockchain
    ]
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    return amount_sent


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
    participants.add(sender)
    participants.add(recipient)


# stats = [("age", 19), ("weight", 45), ("heigth", 178)]

# dict_stats = {key: value for (key, value) in stats}
# ==> {'age':29, 'weight':72, 'height':178}


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    block = {
        "previous_hash": hashed_block,
        "index": len(blockchain),
        "transactions": open_transactions,
    }
    blockchain.append(block)
    return True


def verify_chain():
    for index, block in enumerate(blockchain):
        if index == 0:
            continue
        if block["previous_hash"] != hash_block(blockchain[index - 1]):
            return False
    return True


waiting_for_input = True

while waiting_for_input:
    print("Please choose")
    print("1: Add a new transaction value: ")
    print("2: Mine a new block")
    print("3: Output the blockchain blocks: ")
    print("4: Output the participants:  ")
    print("h: Manipulate the chain: ")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        addTransaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == "2":
        if mine_block():
            open_transactions = []
    elif user_choice == "3":
        print_blockchain_elements()
    elif user_choice == "4":
        print(participants)
    elif user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = [
                {
                    "previous_hash": "",
                    "index": 0,
                    "transactions": [
                        {"sender": "Chris", "recipient": "Igor", "amount": 1000}
                    ],
                }
            ]
    elif user_choice == "q":
        waiting_for_input = False
    else:
        print("invalid choice!")
    if not verify_chain():
        print_blockchain_elements()
        print("invalid blockchain!")
        break
    print(get_balance("Igor"))
else:
    print("User left!")
print("Done!")
