def isPalindrome(x):
    if x < 0:
        return False

    original_number = x
    reversed_num = 0
            
    while x > 0:
        last_digit = x % 10
        reversed_num = (reversed_num * 10) + last_digit
        x = x // 10

    return original_number == reversed_num