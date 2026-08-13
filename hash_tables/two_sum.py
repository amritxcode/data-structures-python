def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
        
    return []


nums = list(map(int, input().split()))
target = int(input())

print(two_sum(nums, target))