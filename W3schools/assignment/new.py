def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num  
    return result

list1 =[1,2,5]
print(singleNumber(list1))
