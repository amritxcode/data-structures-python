class Solution:
    def watermelon(self, w: int) -> str:
        if w <= 2 or w % 2 != 0:
            return 'NO'

        return 'YES'

n = int(input())

print(Solution().watermelon(n))