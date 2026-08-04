class Solution():
    def even_digits(self, nums:int)->int:
        count = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count += 1
        return count

print(Solution().even_digits([555,901,482,11,22,33]))