class Solution():
    def compare(self, s1: str,s2:str)-> int:
        if s1 > s2:
            return 1
        elif s2 > s1:
            return -1
        else:
            return 0

s1 = input().lower()
s2 = input().lower()

print(Solution().compare(s1, s2))