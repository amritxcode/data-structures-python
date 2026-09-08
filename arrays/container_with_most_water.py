
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            width = right - left
            shorter = min(height[left], height[right])
            area = max(area, width*shorter)
            if shorter == height[left]:
                left += 1
            else:
                right -= 1
        
        return area

height = list(map(int,input().split()))
print(Solution().maxArea(height))
