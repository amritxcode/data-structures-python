class Solution:
    def plus_one(self, digits):
        combined = int("".join(map(str, digits)))
        combined += 1
        separate = list(map(int,str(combined)))

        return separate

print(Solution().plus_one([1,2,3,9,99,9,9]))