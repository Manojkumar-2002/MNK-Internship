my_dict = {'a': 10, 'b': 20, 'c': 30}
total = sum(my_dict.values())
print("Sum of all items:", total)


product = 1
for value in my_dict.values():
    product *= value
print("Product of all items:", product)
