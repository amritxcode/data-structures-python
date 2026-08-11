class Solution():
    def min_step(self, n:int)->int:
        steps = n // 5
        extra = 0
        if n % 5 != 0:
            extra += 1
        return steps + extra

n = int(input())
print(Solution().min_step(n))