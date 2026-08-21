class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        return sorted(freq, key= lambda x: freq[x], reverse = True)[:k]

nums = list(map(int,input().split()))
k = int(input())
print(Solution().topKFrequent(nums, k))