store = {}
def bidder():
    name = input("Enter your name")
    amount = int(input("Enter your amount"))
    store[name] = amount
    option = int(input("Is there any other persons press 0 otherwise press 1 to stop bidding"))
    if option == 0:
        bidder()
    else:
        current_value=0
        for key,value in store.items():
            if value>current_value:
                current_value = value
                winner = key
        print(f"winner is {winner}")
bidder()