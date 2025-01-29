from itertools import combinations

class ThreeSum:
    def find_triplets(self, nums):
        nums = sorted(nums)
        triplets = set()
        for subset in combinations(nums, 3):
            if sum(subset) == 0:
                triplets.add(subset)
        return [list(triplet) for triplet in triplets]

nums = [-25, -10, -7, -3, 2, 4, 8, 10]
three_sum = ThreeSum()
result = three_sum.find_triplets(nums)
print(result)
