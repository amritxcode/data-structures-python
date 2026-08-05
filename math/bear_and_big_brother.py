class Solution():
    def big(self, a:int, b:int)-> int:
        count = 0
        while a <= b:
            a,b = a*3, b*2
            count += 1
        return count

wt1,wt2 = map(int,input().split())

print(Solution().big(wt1, wt2))