def contains_sublist(lst, sublst):
    n, m = len(lst), len(sublst)
    for i in range(n - m + 1):
        if lst[i:i + m] == sublst:
            return True
    return False
print("Contains Sublist:", contains_sublist([1, 2, 3, 4, 5], [3, 4])) 