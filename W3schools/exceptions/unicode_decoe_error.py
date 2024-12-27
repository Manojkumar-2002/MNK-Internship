try:
    with open("example.txt", "r", encoding="ascii") as file:
        content = file.read()
except UnicodeDecodeError:
    print("Error: Unable to decode the file with the given encoding.")
