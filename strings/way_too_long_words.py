class Solution:
    def long(self, n:str) -> str:
        if len(n) < 11:
            return n
        else:
            return n[0]+str(len(n[1:-1]))+n[-1]

n = int(input())

for _ in range(n):
    word = input()
    print(Solution().long(word))