def max_sum_subsequence(lst):
    max_sum = 0
    current_sum = 0
    for num in lst:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

print("Max sum subsequence:", max_sum_subsequence([-2, -3, 4, -1, -2, 1, 5, -3]))


def min_sum_subsequence(lst):
    min_sum = 0
    current_sum = 0
    for num in lst:
        current_sum = min(num, current_sum + num)
        min_sum = min(min_sum, current_sum)
    return min_sum

print("Min sum subsequence:", min_sum_subsequence([-2, -3, 4, -1, -2, 1, 5, -3]))
