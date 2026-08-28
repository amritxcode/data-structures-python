class Solution():
    def books(self, book, mins,  nums):
        left = 0
        window_sum = 0
        answer = 0
        for right in range(book):
            window_sum += nums[right]
            while window_sum > mins:
                window_sum -= nums[left]
                left += 1
            answer = max(answer, right - left + 1)
        return answer

book, mins = map(int,input().split())
nums = list(map(int, input().split()))

print(Solution().books(book, mins, nums))