nums = [1,2,3,4]
n =2

list1 = []
list2 = []
half = len(nums)//n

list1.extend(nums[:half])
list2.extend(nums[half:])

print(list1, list2)
shuffled = []

for i in range(len(list1)):
    shuffled.append(list1[i])
    shuffled.append(list2[i])

print(shuffled)