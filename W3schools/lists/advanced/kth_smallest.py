def kth_smallest(lst, k):
    return sorted(lst)[k-1]

print("Kth smallest:", kth_smallest([7, 10, 4, 3, 20, 15], 3))