class Solution():
    def check(self, s:str) -> str:
        s = set(s)
        if len(s) % 2 == 0:
            return "CHAT WITH HER!"
        return "IGNORE HIM!"

string = input()
print(Solution().check(string))