class Solution:
    def cards(self, n: int, nums:list[int] )-> list[int]:
        s= 0
        d= 0
        l = 0
        r = n - 1
        s_turn = True
        while l <= r:
            if s_turn:    
                if nums[l] > nums[r]:
                    s += nums[l]
                    l += 1
                else:
                    s += nums[r]
                    r -= 1
                    
            else:
                if nums[l] > nums[r]:
                    d += nums[l]
                    l += 1
                else:
                   d += nums[r]
                   r -= 1
            s_turn = not s_turn
        return s, d

n = int(input())
nums = list(map(int, input().split()))
print(*Solution().cards(n, nums))