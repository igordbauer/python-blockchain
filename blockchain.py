blockchain = []


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def get_user_amount():
    return float(input("Your transittion amount please: "))


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


def addTransaction(transaction_amount, last_transaction=[1]):
    if last_transaction == None:
        last_transaction = [1]

    blockchain.append([last_transaction, transaction_amount])


while True:
    print("Please choose")
    print("1: Add a new transaction value: ")
    print("2: Output de blockchain blocks: ")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_amount = get_user_transaction()
        addTransaction(tx_amount, get_last_blockchain_value())
    elif user_choice == "2":
        print_blockchain_elements()
    elif user_choice == "q":
        break
    else:
        print("invalid choice!")

print("Done!")
