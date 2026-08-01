class Solution():
    def bit(self, n:int) -> int:
        count = 0

        for _ in range(n):
            s = input()
            if "++X" in s or "X++" in s:
                count += 1
            elif "--X" in s or "X--" in s:
                count -= 1
        return count

n = int(input())
print(Solution().bit(n))