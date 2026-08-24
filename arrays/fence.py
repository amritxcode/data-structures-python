class Solution():
    def minSubArray(self, n, k, nums):
        left = 0
        best_left = 0
        answer = float('inf')
        window_sum = 0
        for right in range(n):
            window_sum += nums[right]
            if right - left + 1 == k:
                if window_sum < answer:
                    answer = window_sum
                    best_left = left
                window_sum -= nums[left]
                left += 1
        return best_left + 1

n, k = map(int, input().split())
nums = list(map(int, input().split()))

print(Solution().minSubArray(n, k, nums))