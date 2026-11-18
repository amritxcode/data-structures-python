def palindrome(x):
    if x < 0:
        return False

    ori_num = x
    rev = 0

    while x > 0:
        last_digit = x % 10
        rev = (rev*10) + last_digit
        x = x//10

    return ori_num == rev

x = int(input())
print(palindrome(x))