def reverse_at_index(lst, index):
    return lst[:index] + lst[index:][::-1]

print("Reverse at index:", reverse_at_index([1, 2, 3, 4, 5], 3))