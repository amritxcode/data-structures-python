class Solution:
    def longestSubarray(self, arr: list[int], k: int) -> int:
        left = 0
        total = 0
        length = 0

        for right in range(len(arr)):
            total += arr[right]

            while total > k:
                total -= arr[left]
                left += 1

            if total == k:
                length = max(length, right - left + 1)

        return length
    
arr = list(map(int, input().split()))
k = int(input())

print(Solution().longestSubarray(arr, k))