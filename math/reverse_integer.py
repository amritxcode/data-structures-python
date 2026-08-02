class Solution():
    def reverse_integer(self, x:int)-> int:
        if x < -2**31 or x > 2**31-1:
            return 0
        
        is_negative = x < 0
        temp =abs(x)
        x = 0
        while temp > 0:
            digit = temp % 10
            x = (x * 10) + digit
            temp = temp // 10

        if is_negative:
            x = -x

        if x < -2**31 or x > 2**31-1:
            return 0

        return x

print(Solution().reverse_integer(12345))