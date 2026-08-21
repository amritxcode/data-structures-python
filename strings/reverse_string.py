class Solution(object):
    def reverseString(self, s):
        s[:] = s[::-1]
        return s
s = list(input().split())
print(Solution().reverseString(s))