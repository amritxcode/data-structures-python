class Solution():
    def valid_palindrome(self, s:str)-> bool:
            clean = "".join((i.lower() for i in s if 'A' <= i <= 'Z' or 'a' <= i <= 'z' or '0' <= i <= '9'))
            return clean == clean[::-1]

print(Solution().valid_palindrome("A man, a plan, a canal: Panama"))