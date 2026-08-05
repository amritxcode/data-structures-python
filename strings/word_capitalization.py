class Solution():
    def check(self, s:str) -> str:
        return s[0].upper() + s[1:]

string = input()
print(Solution().check(string))