def first_non_repeated(lst):
    count = {}
    for num in lst:
        count[num] = count.get(num, 0) + 1
    for num in lst:
        if count[num] == 1:
            return num
    return None

print("First non-repeated element:", first_non_repeated([1, 2, 2, 3, 4, 3, 5]))