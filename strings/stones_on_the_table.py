class Solution():
    def stone(self, n:int, s: str)->int:
        count = 0
        for i in range(n-1):
            if s[i] == s[i+1]:
                count += 1

        return count

n = int(input())
s = input()
print(Solution().stone(n,s))