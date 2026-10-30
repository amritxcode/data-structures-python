class Solution:
    def two_sum_ii(self, nums:list[int], target:int)-> list[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                return [left+1, right+1]
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1

        return []

nums = list(map(int, input().split()))
target = int(input())
print(Solution().two_sum_ii(nums, target))