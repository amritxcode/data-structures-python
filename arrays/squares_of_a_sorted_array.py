class Solution:
    def squaresOfSortedArray(self, nums:list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)
        pos = len(nums) - 1
        while left <= right:
            if nums[left]**2 > nums[right]**2:
                result[pos] = nums[left]**2
                left += 1
            else:
                result[pos] = nums[right]**2
                right -= 1
            pos -= 1

        return result
        

nums = list(map(int, input().split()))
print(Solution().squaresOfSortedArray(nums))