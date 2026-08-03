class Solution:
    def sqrt(self, x:int) -> int:
        if x <= 1:
            return x

        num = x // 2

        while num * num > x:
            num = num // 2

        if num == 0:
            num = 1

        while num * num <= x:
            num = num + 1

        return num - 1

print(Solution().sqrt(5))