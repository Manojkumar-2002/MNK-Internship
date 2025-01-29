class TwoSum:
    def find_indices(self, numbers, target):
        lookup = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in lookup:
                print(lookup[diff], i)
            lookup[num] = i
two_sum = TwoSum()
two_sum.find_indices([2,3,4,6,5,75,23],7)