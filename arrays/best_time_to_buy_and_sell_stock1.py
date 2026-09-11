class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        best = 0
        cheapest = prices[0]
        for price in prices:
            cheapest = min(price, cheapest)
            best = max(best, price - cheapest)
        return best

prices = list(map(int,input().split()))
print(Solution().maxProfit(prices))