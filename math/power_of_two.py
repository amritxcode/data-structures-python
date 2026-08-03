class Solution():
    def power(self, n:int)-> bool:
        return n > 0 and (n & (n -1) == 0)

print(Solution().power(16))