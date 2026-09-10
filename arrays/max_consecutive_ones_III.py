class Solution():
    def maxCons(self, nums: list[int], k: int) -> int:

        left = 0
        zero = 0
        answer = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                zero += 1

            while zero > k:
                if nums[left] == 0:
                    zero -= 1
                left += 1

            answer = max(right - left + 1, answer)
        return answer

nums = list(map(int, input().split()))
k = int(input())

print(Solution().maxCons(nums, k))