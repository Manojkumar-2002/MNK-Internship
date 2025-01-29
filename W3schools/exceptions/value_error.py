try:
    user_input = input("Enter an integer: ")
    number = int(user_input)
    print("You entered:", number)
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
