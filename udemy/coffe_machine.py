
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

menu = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 30},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 60},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 70},
}


def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_payment(cost):
    print(f"The cost is ₹{cost}. Please insert coins.")
    total = int(input("How many ₹10 coins?: ")) * 10
    total += int(input("How many ₹5 coins?: ")) * 5
    total += int(input("How many ₹2 coins?: ")) * 2
    total += int(input("How many ₹1 coins?: ")) * 1

    if total >= cost:
        change = total - cost
        print(f"Transaction successful! Here is your ₹{change} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


def coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            print("Turning off the coffee machine. Goodbye!")
            break
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
        elif choice in menu:
            drink = menu[choice]
            if check_resources(drink):
                if process_payment(drink["cost"]):
                    make_coffee(choice, drink)
        else:
            print("Invalid choice. Please select a valid drink.")



coffee_machine()
