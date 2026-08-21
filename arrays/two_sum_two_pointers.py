class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            total = nums[left] + nums[right]

            if total == target:
                return [left, right]
            elif total < target:
                left += 1
            else:
                right -= 1

        return []
nums = list(map(int, input().split()))
target = int(input())

print(Solution().twoSum(nums, target))