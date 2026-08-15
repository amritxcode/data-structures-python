class Solution():
    def dups(self,nums:list[int])-> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

n = list(map(int, input().split()))
print(Solution().dups(n))
