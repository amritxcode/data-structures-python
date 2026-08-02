class Solution:
    def next_round(self,x,k):
        cutoff = x[k-1]
        count = 0
        for score in x:
            if score >= cutoff and score > 0:
                count += 1

        return count


n, k= map(int,input().split())
x = [int(score) for score in input().split()]
print(Solution().next_round(x,k))