def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if val != nums[i]:
           nums[k] = nums[i] 
           k+= 1
    return k
print(remove_element([3,2,2,3],3))