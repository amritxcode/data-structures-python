class Solution():
    def check(self, s:str) -> str:
        upper = 0
        for char in s:
            if "A" <= char <= "Z":
                upper += 1
        if len(s)-upper >= upper:
            return s.lower()
        return s.upper()

s = input()
print(Solution().check(s))