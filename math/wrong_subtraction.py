class Solution():
    def subtraction(self, n:int, sub:int)-> int:
        for i in range(sub):
            if n % 10 != 0:
                n -= 1
            elif n % 10 == 0:
                n //= 10
        return n

n, sub = map(int, input().split())

print(Solution().subtraction(n, sub))
