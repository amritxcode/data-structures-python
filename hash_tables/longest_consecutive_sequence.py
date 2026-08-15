class Solution():
    def longestConsecutive(self, nums:list[int])->int:
        seen = set(nums)
        ans = 0
        for num in seen:
            if num - 1 not in seen:
                length = 1
                current = num
                while current + 1 in seen:
                    length += 1
                    current += 1
                ans = max(ans, length)

        return ans

nums = list(map(int, input().split()))
print(Solution().longestConsecutive(nums))