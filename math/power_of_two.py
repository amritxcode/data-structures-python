class Solution():
    def power(self, x:int)-> bool:
        return x > 0 and (x & (x -1) == 0)

print(Solution().power(16))