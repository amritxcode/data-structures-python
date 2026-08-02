class Solution:
    def isPalindrome(self, x):
        s = str(x)[::-1]
        if str(x) == s:
            return True
        else:
            return False

print(Solution().isPalindrome(121))