nums = [5,6,7,8,9,10]

def twoSum(nums, target):
    check = {}
    for index, num in enumerate(nums):
        missing = target - num
        if missing in check:
            return [check[missing],index]
        
        check[num] = index


print(twoSum([5,6,7,8,9,10],11))