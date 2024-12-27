try:
    with open("", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file does not exist.")
