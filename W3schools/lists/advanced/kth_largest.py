def kth_largest(lst, k):
    return sorted(lst, reverse=True)[k-1]

print("Kth largest:", kth_largest([7, 10, 4, 3, 20, 15], 2))