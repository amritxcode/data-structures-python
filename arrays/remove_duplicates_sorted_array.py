def removeDuplicates(nums):
    if not nums:
        return 0
    k = 1
    for num in range(1,len(nums)):
        if nums[num] > nums[num -1]:
            num[k] = nums[num]
            k += 1
        return k
    
print(removeDuplicates([1,1,2,3,3,4,4,5,5]))