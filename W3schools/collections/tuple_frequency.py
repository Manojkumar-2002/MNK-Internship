from collections import Counter
nums = [(['1', '4'], ['4', '1'], ['3', '4'], ['2', '7'], ['6', '8'], ['5', '8'], ['6', '8'], ['5', '7'], ['2', '7'])]
ch =Counter(tuple(i) for i in nums[0])
print(ch.most_common(2))
print(ch)

