class Solution:
  def subtraction(self, n: int, sub: int) -> int:
    while sub > 0 and n > 0:
        last_digit = n % 10

        if last_digit == 0:
            n //= 10
            sub -= 1

        else:
            steps_to_take = min(sub, last_digit)
            n -= steps_to_take
            sub -= steps_to_take

    return n

n, sub = map(int, input().split())
print(Solution().subtraction(n, sub))