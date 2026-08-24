class Solution():
    def maxAvg(self, nums: list[int], k: int)-> float:
        left = 0
        answer = float('-inf')
        window_sum = 0
        for right in range(len(nums)):
            window_sum += nums[right]
            if right -left + 1 == k:
                answer = max(answer, window_sum)
                window_sum -= nums[left]
                left += 1
        return answer/k

nums = list(map(int, input().split()))
k = int(input())

print(Solution().maxAvg(nums, k))