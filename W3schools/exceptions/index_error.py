try:
    my_list = [1, 2, 3]
    index = int(input("Enter an index: "))
    print("Element at index:", my_list[index])
except IndexError:
    print("Error: Index out of range.")
