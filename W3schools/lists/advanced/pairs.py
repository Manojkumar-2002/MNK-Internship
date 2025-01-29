def find_pairs(lst, target):
    pairs = []
    seen = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

print("Find pairs:", find_pairs([1, 2, 3, 4, 5], 6))