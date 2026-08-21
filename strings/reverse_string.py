class Solution(object):
    def reverseString(self, s):
        s[:] = s[::-1]

s = list(map(input().split()))
print(Solution().reverseString(s))