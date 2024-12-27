my_dict = {1: 10, 2: 20, 3: 15, 4: 5}
sorted_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted by value (ascending):", sorted_asc)
sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Sorted by value (descending):", sorted_desc)
