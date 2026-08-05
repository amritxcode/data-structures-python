class Solution():
    def add_digits(self, num:int)-> int:
        if num == 0:
            return 0
        return 1 + (num -1) % 9

print(Solution().add_digits(789))