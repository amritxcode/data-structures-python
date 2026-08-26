class Solution():
    def minSizeSum(self, nums, target):
        left = 0
        window_sum = 0
        answer = float('inf')
        for right in range(len(nums)):    
            window_sum += nums[left]
            while window_sum >= target:
                current_len = right - left + 1
                answer = min(current_len, answer)
                window_sum -= nums[left]
                left += 1
        return 0 if answer == float('inf') else answer

nums = list(map(int, input().split()))
target = int(input())

print(Solution().minSizeSum(nums, target))
